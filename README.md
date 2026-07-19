# Dokumentacja Projektu Sonulab StompStation PRO

Witaj w repozytorium wiedzy i analiz dla urządzenia **Sonulab StompStation PRO**. Znajdziesz tutaj zebraną i ustrukturyzowaną dokumentację ułatwiającą codzienną pracę z urządzeniem, konfigurację presetów oraz rozwiązywanie problemów.

## Spis Dokumentów

* ### 📄 [Instrukcja Obsługi StompStation PRO (Podsumowanie)](file:///c:/Users/dariu/agy/agy-sonulab/instrukcja.md)
  Szczegółowe streszczenie oficjalnej instrukcji PDF w języku polskim. Zawiera opisy:
  * Głównych funkcji i specyfikacji technicznej.
  * Nawigacji fizycznej (enkodery, przełączniki nożne, kombinacje przycisków do zmiany banków).
  * Łańcucha sygnałowego oraz poszczególnych efektów (Noise Gate, Compressor, Delay, Reverb, itp.).
  * Konfiguracji i mapowania komunikatów MIDI CC (wraz z tabelą kontrolerów) oraz MIDI PC.
  * Procedury aktualizacji oprogramowania (firmware) przy użyciu trybu UPD.

* ### 📄 [Lista Impulsów IR (Impulse Responses)](file:///c:/Users/dariu/agy/agy-sonulab/lista_ir.md)
  Spis fabrycznych i zaimportowanych impulsów głośnikowych (IR) w urządzeniu (22 pozycje). Zawiera nazwy i krótkie opisy ułatwiające orientację w dostępnych brzmieniach kolumn (np. British Cab, Daemon Cab, Bogner, Mesa, Fender).

* ### 📄 [Lista Wzmacniaczy (Profile NAM)](file:///c:/Users/dariu/agy/agy-sonulab/lista_wzmacniaczy.md)
  Analiza i identyfikacja 24 profili wzmacniaczy widocznych w urządzeniu:
  * Odszyfrowanie nazw handlowych i skrótów na oryginalne modele (np. Marshall, Fender, Vox, Mesa Boogie, Soldano, Diezel, ENGL, Hiwatt).
  * Klasyfikacja profili na wersje **[RIG / CAB]** (zawierające gotową symulację kolumny i mikrofonu) oraz **[AMP ONLY]** (czysty sygnał z samej głowy wzmacniacza, wymagający użycia bloku IR).

* ### 🛠️ [Skrypt Pobierania NAM A2 (download_nam.py)](file:///c:/Users/dariu/agy/agy-sonulab/download_nam.py)
  Narzędzie CLI w języku Python ułatwiające wyszukiwanie, sprawdzanie metadanych (pobrania, polubienia) i pobieranie modeli NAM A2 z portalu TONE3000.com.

* ### 🤖 Skille Agenta (w folderze [.agents/skills](file:///c:/Users/dariu/agy/agy-sonulab/.agents/skills)):
  * **[new-nam](file:///c:/Users/dariu/agy/agy-sonulab/.agents/skills/new-nam/SKILL.md):** Skrypujący organizator plików w Pythonie. Skanuje pobrane pliki ZIP oraz pliki bezpośrednie w Downloads, segregując profile `.nam`, impulsy `.wav`/`.ir` oraz presety `.pst` (Sonulab) do odpowiednich folderów w `Documents\nam_ir\`.
  * **[tone3000-search](file:///c:/Users/dariu/agy/agy-sonulab/.agents/skills/tone3000-search/SKILL.md):** Odpytywanie portalu o metadane i statystyki brzmień.
  * **[tone3000-download](file:///c:/Users/dariu/agy/agy-sonulab/.agents/skills/tone3000-download/SKILL.md):** Automatyczne pobieranie plików `.nam` na podstawie zapytań lub ID.

---

## Szybka Ściągawka (Fizyczna Nawigacja)

* **Wejście do edycji efektów (Edit Mode):** Wciśnij krótko pokrętło **BROWSE/VOLUME**.
* **Wejście do ustawień globalnych (Setup):** Przytrzymaj pokrętło **BROWSE/VOLUME**.
* **Włączenie Tunera:** Przytrzymaj przełącznik nożny **C**.
* **Zmiana banku w górę:** Kliknij jednocześnie przełączniki **B + C**.
* **Zmiana banku w dół:** Kliknij jednocześnie przełączniki **A + B**.
