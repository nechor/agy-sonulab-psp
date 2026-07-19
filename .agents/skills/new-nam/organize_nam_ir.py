import os
import sys
import shutil
import zipfile
from datetime import datetime, timedelta

def get_paths():
    user_profile = os.environ.get("USERPROFILE") or os.path.expanduser("~")
    downloads_dir = os.path.join(user_profile, "Downloads")
    documents_dir = os.path.join(user_profile, "Documents")
    nam_ir_dir = os.path.join(documents_dir, "nam_ir")
    return downloads_dir, nam_ir_dir

def process_direct_file(file_path, nam_ir_dir):
    filename = os.path.basename(file_path)
    ext = os.path.splitext(filename)[1].lower()
    
    if ext == ".nam":
        dest_dir = os.path.join(nam_ir_dir, "nam")
    elif ext in [".wav", ".ir"]:
        dest_dir = os.path.join(nam_ir_dir, "ir")
    elif ext == ".pst":
        dest_dir = os.path.join(nam_ir_dir, "presets")
    else:
        return False
        
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, filename)
    print(f"Przenoszenie bezpośredniego pliku: {filename} -> nam_ir/{os.path.basename(dest_dir)}/")
    try:
        shutil.move(file_path, dest_path)
        return True
    except Exception as e:
        print(f"Błąd podczas przenoszenia pliku {filename}: {e}")
        return False

def process_zip_file(zip_path, nam_ir_dir):
    filename = os.path.basename(zip_path)
    zip_name = os.path.splitext(filename)[0]
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            nam_count = 0
            ir_count = 0
            pst_count = 0
            
            for file_info in zip_ref.infolist():
                ext = os.path.splitext(file_info.filename)[1].lower()
                if ext == ".nam":
                    nam_count += 1
                elif ext in [".wav", ".ir"]:
                    ir_count += 1
                elif ext == ".pst":
                    pst_count += 1
                    
            subfolder = None
            if nam_count > 0:
                subfolder = "nam"
            elif ir_count > 0:
                subfolder = "ir"
            elif pst_count > 0:
                subfolder = "presets"
                
            if subfolder:
                target_dir = os.path.join(nam_ir_dir, subfolder, zip_name)
                if os.path.exists(target_dir):
                    shutil.rmtree(target_dir)
                    
                print(f"Rozpakowywanie: {filename} -> nam_ir/{subfolder}/{zip_name}/")
                zip_ref.extractall(target_dir)
                
                # Usuń plik ZIP po udanej ekstrakcji
                zip_ref.close()
                os.remove(zip_path)
                print(f"Usunięto plik ZIP: {filename}")
                return True
                
    except Exception as e:
        print(f"Błąd przetwarzania pliku ZIP {filename}: {e}")
        
    return False

def main():
    downloads_dir, nam_ir_dir = get_paths()
    
    if not os.path.exists(downloads_dir):
        print(f"Błąd: Nie znaleziono folderu Downloads pod ścieżką {downloads_dir}")
        sys.exit(1)
        
    # Upewnij się, że główne foldery istnieją
    os.makedirs(os.path.join(nam_ir_dir, "nam"), exist_ok=True)
    os.makedirs(os.path.join(nam_ir_dir, "ir"), exist_ok=True)
    os.makedirs(os.path.join(nam_ir_dir, "presets"), exist_ok=True)
    
    # Przeskanuj folder Downloads pod kątem plików o odpowiednich rozszerzeniach
    valid_extensions = {".zip", ".nam", ".wav", ".ir", ".pst"}
    files_to_process = []
    
    for f in os.listdir(downloads_dir):
        file_path = os.path.join(downloads_dir, f)
        if os.path.isfile(file_path):
            ext = os.path.splitext(f)[1].lower()
            if ext in valid_extensions:
                files_to_process.append(file_path)
                
    if not files_to_process:
        print("Brak plików NAM, IR lub Presetów w folderze Downloads.")
        sys.exit(0)
        
    # Filtruj pliki modyfikowane w ciągu ostatnich 24h
    now = datetime.now()
    one_day_ago = now - timedelta(hours=24)
    
    recent_files = [f for f in files_to_process if datetime.fromtimestamp(os.path.getmtime(f)) > one_day_ago]
    
    processed_count = 0
    
    # Przetwarzaj najnowsze
    files_to_run = recent_files
    if not files_to_run:
        # Jeśli nic nie ma z 24h, weź 5 najnowszych ogólnie
        print("Brak nowych plików z ostatnich 24 godzin. Sprawdzanie 5 najnowszych plików...")
        files_to_process.sort(key=os.path.getmtime, reverse=True)
        files_to_run = files_to_process[:5]
        
    for file_path in files_to_run:
        ext = os.path.splitext(file_path)[1].lower()
        if ext == ".zip":
            if process_zip_file(file_path, nam_ir_dir):
                processed_count += 1
        else:
            if process_direct_file(file_path, nam_ir_dir):
                processed_count += 1
                
    print(f"Zakończono. Przetworzono pomyślnie {processed_count} plik(ów).")

if __name__ == "__main__":
    main()
