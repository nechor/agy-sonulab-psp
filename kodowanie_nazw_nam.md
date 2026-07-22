# Standard Kodowania i Normalizacji Nazw Modeli NAM (.nam)

Dokument opisuje jednolity, zwięzły standard nazewnictwa plików `.nam` przyjęty w kolekcji Sonulab StompStation PRO.

---

## 1. Zasady Ogólne

1. **Maksymalna długość nazwy:** **35 znaków** (wliczając rozszerzenie `.nam`).
2. **Struktura nazwy:**
   ```
   [AMP]_[GAIN]_[TONE]_[EXTRA].nam
   ```
3. **Formatowanie:** Wyłącznie wielkie litery, cyfry oraz znaki podkreślenia `_` jako separatory sekcji. Brak spacji i znaków specjalnych.

---

## 2. Opis Sekcji Kodu

### 2.1 `[AMP]` – Kod Skrótowy Wzmacniacza (2–5 znaków)
Identyfikuje markę i model wzmacniacza:
* `SLO30` = Soldano SLO-30 (Super Lead Overdrive)
* `TWEX` = Ceriatone TW Express (Trainwreck Express)
* `DSMIN` = Friedman Dirty Shirley Mini
* `JMP22` = Marshall JMP 2204 (1980)
* `DR2` = Fender Deluxe Reverb II
* `MK4` = Mesa Boogie Mark IV
* `ORC12` = Orange Crush 12
* `AC30` = Vox AC30
* `EC101` = Bogner Ecstasy 101B (Crunch '80)

---

### 2.2 `[GAIN]` – Poziom / Kanał Przesterowania (2–5 znaków)
Opisuje nasycenie i kanał toru sygnałowego:
* `CLN` = Czystsze brzmienie (Clean)
* `LOW` / `GLOW` = Niski przester / Low gain
* `CRN` = Przester typu Crunch
* `MID` = Średni przester / Mid gain
* `HI` / `HIGH` = Wysoki przester / High gain / Lead
* `G03` ... `G10` = Poziom gainu w skali 1-10
* `C1` / `C2G1` / `C2G2` / `C2G3` = Sekcje i poziomy nasycenia dla konstrukcji wielokanałowych (np. Ceriatone TW Express: Channel 1 vs Channel 2 Gain 1/2/3)

---

### 2.3 `[TONE]` – Charakterystyka Tonalna / EQ (2–6 znaków)
Opisuje barwę, korekcję i voicingu:
* `NAT` = Naturalny, zbalansowany EQ (Natural)
* `FUL` = Tłusty, wyrazisty środek i dół (Fuller/Fat)
* `DRK` = Ciemniejsza, wygładzona góra (Darker)
* `TIG` = Zwarty, mocno kontrolowany bass (Tight)
* `FULTIG` = Tłusty i zwarty (Fuller Tight)
* `FULDRK` = Tłusty i ciemniejszy (Fuller Darker)
* `MB` = Aktywny dodatek Mid Boost
* `PRQ` = Dedykowane filtrowanie wstępne (Pre-EQ)
* `V3PB` / `V5G5` = Wybrane pozycje fizycznych potencjometrów Volume/Gain/EQ

---

### 2.4 `[EXTRA]` – Dodatki, Przeznaczenie i Dopalacze (2–8 znaków)
Dodatkowe informacje o zastosowaniu lub użytych efektach pomocniczych:
* `RHY` = Dedykowany do gry rytmicznej (Rhythm)
* `LD` = Dedykowany do gry solowej (Lead)
* `KLN` = Dopalacz Klon Centaur (Klon Boost)
* `BUX` = Dopalacz BuxBoost (Tight Boost)
* `80S` / `PPC212` = Kolumna lub profil brzmieniowy lat 80.
* `TS8` / `SD1` / `RAT` / `TIM` = Kostki dopalające (TS808, SD-1, RAT, Timmy)
* `57` / `P3` = Mikrofon SM57 / Sennheiser E609 / P3000
* `N01` ... `N99` = Numer wariantu w paczce sekwencyjnej

---

## 3. Przykłady Rozkodowania Nazw

| Nazwa Pliku | Odczyt Nazwy |
|---|---|
| `SLO30_G06_NAT_RHY.nam` | **Soldano SLO-30**, Gain 6, Barwa Naturalna, Rytmiczny |
| `SLO30_G09_FULTIG_LD.nam` | **Soldano SLO-30**, Gain 9, Tłusty i Zwarty, Solowy (Lead) |
| `TWEX_C1_G75_N1.nam` | **Trainwreck Express**, Kanał 1 (Clean), Gain 7.5, Wariant 1 |
| `TWEX_C2G3_MB_G56_N5.nam` | **Trainwreck Express**, Kanał 2 Gain 3 + Mid Boost, Wariant 5 |
| `DSMIN_CRN_BUX_G4.nam` | **Dirty Shirley Mini**, Crunch, Boost Bux, Gain 4 |
| `DSMIN_LOW_KLN_G35.nam` | **Dirty Shirley Mini**, Low Gain, Dopalacz Klon, Gain 3.5 |
| `JMP22_HI_HUNK.nam` | **Marshall JMP 2204**, High Gain, Profil 'Hunk' |
| `AC30_G05_TS808.nam` | **Vox AC30**, Gain 5, Dopalacz TS808 |

---
*Zdokumentowano i zaktualizowano dla kolekcji Sonulab StompStation PRO.*
