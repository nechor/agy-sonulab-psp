import os
import sys
import argparse
import requests
import json
import re

API_URL = "https://www.tone3000.com/api/v1"

def get_api_key():
    api_key = os.environ.get("TONE3000_API_KEY")
    if api_key:
        return api_key
        
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("TONE3000_API_KEY="):
                    return line.strip().split("=")[1].strip("'\" ")
                    
    print("Klucz API TONE3000 nie został znaleziony.")
    print("Możesz go wygenerować w ustawieniach swojego konta na tone3000.com.")
    api_key = input("Wprowadź swój klucz Secret Key (t3k_cs_...): ").strip()
    if not api_key:
        print("Błąd: Klucz API jest wymagany.")
        sys.exit(1)
        
    try:
        with open(".env", "a", encoding="utf-8") as f:
            f.write(f"\nTONE3000_API_KEY={api_key}\n")
        print("Klucz API został zapisany w pliku .env")
    except Exception as e:
        print(f"Nie można zapisać klucza do pliku .env: {e}")
        
    return api_key

def get_headers(api_key):
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name).replace(" ", "_")

def download_file(url, headers, output_path):
    print(f"Pobieranie: {output_path}...", end="", flush=True)
    try:
        response = requests.get(url, headers=headers, stream=True)
        if response.status_code == 200:
            with open(output_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(" [OK]")
            return True
        else:
            print(f" [BŁĄD] Status: {response.status_code}")
            return False
    except Exception as e:
        print(f" [BŁĄD] {e}")
        return False

def print_tone_info(tone):
    tone_id = tone.get("id")
    title = tone.get("title", "Bez nazwy")
    author = tone.get("user", {}).get("username", "Nieznany")
    desc = tone.get("description") or "Brak opisu"
    gear = tone.get("gear", "Nieznane")
    fmt = tone.get("format", "Nieznany")
    models_count = tone.get("models_count", 0)
    a2_count = tone.get("a2_models_count", 0)
    downloads = tone.get("downloads_count", 0)
    favorites = tone.get("favorites_count", 0)
    url = tone.get("url") or f"https://tone3000.com/tones/{tone_id}"
    
    makes = [m.get("name") for m in tone.get("makes", []) if m.get("name")]
    tags = [t.get("name") for t in tone.get("tags", []) if t.get("name")]
    
    print("-" * 50)
    print(f"Tytuł:        {title}")
    print(f"ID Brzmienia: {tone_id}")
    print(f"Autor:        {author}")
    print(f"Opis:         {desc.strip()}")
    print(f"Urządzenie:   {gear}")
    print(f"Format:       {fmt}")
    print(f"Marki (Make): {', '.join(makes) if makes else 'Brak'}")
    print(f"Tagi:         {', '.join(tags) if tags else 'Brak'}")
    print(f"Liczba modeli: {models_count} (w tym A2: {a2_count})")
    print(f"Pobrania:     {downloads}")
    print(f"Polubienia:   {favorites}")
    print(f"Link WWW:     {url}")
    print("-" * 50)

def download_models_for_tone(tone_id, tone_title, headers, output_dir):
    url = f"{API_URL}/models"
    params = {
        "tone_id": tone_id,
        "architecture": "2" # NAM A2
    }
    
    try:
        res = requests.get(url, headers=headers, params=params)
        if res.status_code != 200:
            print(f"  Nie udało się pobrać listy modeli dla ID {tone_id} (status {res.status_code})")
            return
            
        models_data = res.json()
        models = models_data.get("data", []) if isinstance(models_data, dict) else models_data
        
        if not models:
            print(f"  Brak kompatybilnych modeli NAM A2 dla brzmienia: {tone_title}")
            return
            
        for model in models:
            model_url = model.get("model_url")
            filename = model.get("name") or model.get("filename") or f"{sanitize_filename(tone_title)}.nam"
            if not filename.endswith(".nam"):
                filename += ".nam"
                
            output_path = os.path.join(output_dir, filename)
            download_file(model_url, headers, output_path)
            
    except Exception as e:
        print(f"  Błąd podczas pobierania modeli dla brzmienia {tone_title}: {e}")

def search_and_download(query, headers, output_dir, limit=1, gears=None, sizes=None, sort=None, calibrated=False, info_only=False):
    print(f"\nWyszukiwanie w TONE3000 dla: '{query}'...")
    url = f"{API_URL}/tones/search"
    params = {
        "query": query,
        "format": "nam",
        "architecture": "2", # NAM A2
        "page_size": 10 if info_only else 5
    }
    
    if gears:
        params["gears"] = gears.replace(",", "_")
    if sizes:
        params["sizes"] = sizes.replace(",", "_")
    if sort:
        params["sort"] = sort
    if calibrated:
        params["calibrated"] = "true"
        
    try:
        res = requests.get(url, headers=headers, params=params)
        if res.status_code != 200:
            print(f"Błąd wyszukiwania (status {res.status_code}): {res.text}")
            return
            
        results = res.json().get("data", [])
        if not results:
            print(f"Brak wyników (NAM A2) pasujących do filtrów dla zapytania: '{query}'")
            return
            
        if info_only:
            print(f"Znaleziono {len(results)} brzmień pasujących do zapytania:")
            for tone in results:
                print_tone_info(tone)
        else:
            print(f"Znaleziono {len(results)} pasujących brzmień:")
            for idx, tone in enumerate(results[:limit]):
                tone_id = tone.get("id")
                title = tone.get("title", "Bez nazwy")
                author = tone.get("user", {}).get("username", "Nieznany")
                print(f" [{idx + 1}] {title} (autor: {author}, ID: {tone_id})")
                download_models_for_tone(tone_id, title, headers, output_dir)
            
    except Exception as e:
        print(f"Błąd komunikacji z API podczas wyszukiwania: {e}")

def get_tone_by_id(tone_id, headers):
    url = f"{API_URL}/tones/{tone_id}"
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            print(f"Błąd pobierania brzmienia o ID {tone_id} (status {res.status_code}): {res.text}")
            return None
    except Exception as e:
        print(f"Błąd połączenia z API: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Pobieranie i odpytywanie modeli NAM A2 z portalu TONE3000.com")
    parser.add_argument("--search", type=str, help="Wyszukaj model na podstawie frazy")
    parser.add_argument("--tone-id", type=int, help="Wyszukaj/pobierz model bezpośrednio na podstawie Tone ID")
    parser.add_argument("--file", type=str, help="Ścieżka do pliku tekstowego z listą fraz")
    parser.add_argument("--out-dir", type=str, default="./downloads", help="Folder docelowy")
    
    parser.add_argument("--gears", type=str)
    parser.add_argument("--sizes", type=str)
    parser.add_argument("--sort", type=str, choices=["best-match", "newest", "oldest", "trending", "downloads-all-time"])
    parser.add_argument("--calibrated", action="store_true")
    parser.add_argument("--info", action="store_true")
    
    args = parser.parse_args()
    
    if not (args.search or args.tone_id or args.file):
        parser.print_help()
        sys.exit(0)
        
    api_key = get_api_key()
    headers = get_headers(api_key)
    
    if args.info:
        if args.tone_id:
            tone = get_tone_by_id(args.tone_id, headers)
            if tone:
                print_tone_info(tone)
        elif args.search:
            search_and_download(
                args.search, headers, args.out_dir, 
                gears=args.gears, sizes=args.sizes, sort=args.sort, calibrated=args.calibrated,
                info_only=True
            )
    else:
        os.makedirs(args.out_dir, exist_ok=True)
        if args.tone_id:
            print(f"Rozpoczynanie pobierania dla Tone ID: {args.tone_id}...")
            download_models_for_tone(args.tone_id, f"tone_{args.tone_id}", headers, args.out_dir)
        elif args.search:
            search_and_download(
                args.search, headers, args.out_dir, 
                gears=args.gears, sizes=args.sizes, sort=args.sort, calibrated=args.calibrated,
                info_only=False
            )
        elif args.file:
            if not os.path.exists(args.file):
                print(f"Błąd: Plik wejściowy '{args.file}' nie istnieje.")
                sys.exit(1)
            with open(args.file, "r", encoding="utf-8") as f:
                queries = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]
            print(f"Wczytano {len(queries)} zapytania z pliku.")
            for query in queries:
                search_and_download(
                    query, headers, args.out_dir,
                    gears=args.gears, sizes=args.sizes, sort=args.sort, calibrated=args.calibrated,
                    info_only=False
                )
            
    print("\nProces zakończony.")

if __name__ == "__main__":
    main()
