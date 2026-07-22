# Kodowanie Nazw Plików NAM – Dokumentacja Schematu

## 1. Format Nazwy

```
[AMP]_[NN]_[GAIN]_[TONE]_[CHAR].nam
```

| Segment  | Długość | Opis |
|----------|---------|------|
| `[AMP]`  | 5 znaków | Skrót nazwy wzmacniacza |
| `[NN]`   | 2 cyfry  | Numer porządkowy (od najniższego gainu `01`) |
| `[GAIN]` | 3 znaki  | Poziom nasycenia gainu |
| `[TONE]` | 3 znaki  | Charakter EQ / barwa tonu |
| `[CHAR]` | 3 znaki  | Tryb pracy / kanał / zastosowany boost |

**Łączna długość nazwy: maksymalnie 35 znaków** (wymaganie systemu Sonulab StompStation PRO).

---

## 2. Kody Wzmacniaczy (`[AMP]`)

| Kod     | Wzmacniacz                             |
|---------|----------------------------------------|
| `SLO30` | Soldano SLO-30 (Emil Rohbe A2 Pack)    |
| `TWEX`  | Ceriatone TW Express AA (Trainwreck)   |
| `DSMIN` | Friedman Dirty Shirley Mini 20W        |

---

## 3. Kody Poziomu Gainu (`[GAIN]`)

Pliki w każdym folderze posortowane są rosnąco od pozycji `01` (najczystszy) do ostatniej (najwyższy gain).

| Kod   | Poziom                              | Opis                                              |
|-------|-------------------------------------|---------------------------------------------------|
| `CLN` | Clean                               | Brak przesterowania. Krystaliczny, czysty dźwięk |
| `LOW` | Low Gain                            | Lekkie nasycenie, reaktywny na atak w strunę      |
| `CRN` | Crunch                              | Klasyczny rock/blues. Średni poziom gain          |
| `MID` | Mid Gain                            | Cięższa rytmika, na granicy high-gain             |
| `HI`  | High Gain                           | Pełna saturacja, solowy lead                      |

---

## 4. Kody Barwy EQ (`[TONE]`)

| Kod   | Charakter EQ                         | Opis                                                   |
|-------|--------------------------------------|--------------------------------------------------------|
| `NAT` | Natural (Naturalny)                  | Płaski, zbalansowany EQ. Neutralna barwa               |
| `DRK` | Dark (Ciemny)                        | Podbite niskie środki, przytłumiona góra               |
| `BRT` | Bright (Jasny)                       | Podbita góra, tnący i otwarty dźwięk                   |
| `FUL` | Full (Pełny)                         | Podbite niskie środki, gruba masa basu                 |
| `TIG` | Tight (Zwarty)                       | Podkreślony atak, napięty bas, precyzyjny dołu         |
| `FLT` | Fuller + Tight                       | Tłusty i równocześnie zwarty – dla rytmiki z masą      |
| `FDR` | Fuller + Dark                        | Gruba masa basu z wygładzoną górą                      |
| `BAS` | Bassman (Clean Bassman-inspired)     | Czyste brzmienie inspirowane Fender Bassman            |
| `DRV` | Drive (Reaktywny overdrive)          | Organiczny, reaktywny overdrive; dynamiczny             |

---

## 5. Kody Trybu / Kanału / Boostu (`[CHAR]`)

| Kod   | Charakter                            | Opis                                                   |
|-------|--------------------------------------|--------------------------------------------------------|
| `STD` | Standard                             | Bez dopalacza. Czyste ujęcie wzmacniacza               |
| `RHY` | Rhythm (Rytmika)                     | Nastawione pod rytmikę (niższy gain, więcej mas)        |
| `LD`  | Lead (Solowy)                        | Nastawione pod solówkę (wyższy gain, więcej środków)   |
| `C1`  | Channel 1                            | Kanał 1 (zazwyczaj czystszy, niższy gain)              |
| `C2`  | Channel 2                            | Kanał 2 (zazwyczaj wyższy gain, więcej agresji)        |
| `KLN` | Klon Centaur                         | Aktywny boost Klon Centaur przed wzmacniaczem          |
| `BUX` | BuxBoost                             | Aktywny BuxBoost (zwiera bas, zaostrza atak)           |
| `PRQ` | Pre-EQ Filter                        | Aktywny filtr Pre-EQ (wygładza zębate górne pasmo)     |
| `MB`  | Mid Boost                            | Aktywny boost środka pasma                             |
| `AND` | Andertons                            | Ujęcie ze studia Andertons Music                       |

---

## 6. Opis Zawartości Folderów i Plików

### 📁 `01_Soldano_SLO30` – Soldano SLO-30 *(11 modeli)*

Autor ujęć: **Emil Rohbe** (A2), uzupełnienie cleanu: **carav76** (A2)  
Wzmacniacz: **Soldano SLO-30** (Super Lead Overdrive 30W)  
Charakter: Wysokonapięciowy, śpiewny, dynamiczny. Klasyk high-gain lat 80.

| Plik | Gain | Barwa | Tryb | Opis |
|------|------|-------|------|------|
| `SLO30_01_CLN_NAT_STD.nam` | CLN | NAT | STD | Krystaliczny czysty kanał SLO |
| `SLO30_02_LOW_NAT_RHY.nam` | LOW | NAT | RHY | Lekki breakup Gain 5, naturalny |
| `SLO30_03_CRN_NAT_RHY.nam` | CRN | NAT | RHY | Klasyczny crunch Gain 6 naturalny |
| `SLO30_04_CRN_FUL_RHY.nam` | CRN | FUL | RHY | Crunch Gain 6, pełna masa basu |
| `SLO30_05_CRN_TIG_RHY.nam` | CRN | TIG | RHY | Crunch Gain 6, zwarty zwięzły bas |
| `SLO30_06_MID_NAT_LD.nam`  | MID | NAT | LD  | Mid-Gain Lead, naturalny EQ |
| `SLO30_07_MID_FLT_LD.nam`  | MID | FLT | LD  | Mid-Gain Lead, Fuller+Tight |
| `SLO30_08_HI_DRK_LD.nam`   | HI  | DRK | LD  | High-Gain Lead Gain 8, ciemny |
| `SLO30_09_HI_TIG_LD.nam`   | HI  | TIG | LD  | High-Gain Lead Gain 8, zwarty |
| `SLO30_10_HI_FDR_LD.nam`   | HI  | FDR | LD  | High-Gain Lead Gain 8, pełny+ciemny |
| `SLO30_11_HI_FLT_LD.nam`   | HI  | FLT | LD  | High-Gain Lead Gain 9, pełny+zwarty |

---

### 📁 `02_Ceriatone_TW_Express` – Ceriatone TW Express AA *(10 modeli)*

Autor ujęć: **Emil Rohbe / Headfirst** (A2), uzupełnienie cleanu: **jamborinski** (A2)  
Wzmacniacz: **Ceriatone TW Express AA** (klon Trainwreck Express)  
Charakter: Glassy, otwarty, śpiewny i dynamiczny. Reaguje na siłę uderzenia jak prawdziwy wzmacniacz.

| Plik | Gain | Barwa | Tryb | Opis |
|------|------|-------|------|------|
| `TWEX_01_CLN_BAS_C1.nam`  | CLN | BAS | C1 | Czysty Bassman-style Kanał 1 |
| `TWEX_02_LOW_NAT_C1.nam`  | LOW | NAT | C1 | Low Gain Gain 4.4 Kanał 1 Natural |
| `TWEX_03_CRN_NAT_C1.nam`  | CRN | NAT | C1 | Crunch Gain 7.5 Kanał 1 |
| `TWEX_04_CRN_FUL_C1.nam`  | CRN | FUL | C1 | Crunch Gain 8.7 Kanał 1 Mid Boost |
| `TWEX_05_CRN_FUL_C2.nam`  | CRN | FUL | C2 | Crunch Gain 2.5 Kanał 2 Mid Boost |
| `TWEX_06_MID_NAT_C2.nam`  | MID | NAT | C2 | Mid Gain 2.5 Kanał 2 naturalny |
| `TWEX_07_MID_FUL_C2.nam`  | MID | FUL | C2 | Mid Gain 7.5 Kanał 2 Mid Boost |
| `TWEX_08_HI_NAT_C2.nam`   | HI  | NAT | C2 | High Gain 3.7 Kanał 2 G3 naturalny |
| `TWEX_09_HI_FUL_C2.nam`   | HI  | FUL | C2 | High Gain 4.4 Kanał 2 G3 Mid Boost |
| `TWEX_10_HI_FLT_C2.nam`   | HI  | FLT | C2 | High Gain 5.6 Kanał 2 G3 – Max Lead |

---

### 📁 `03_Friedman_Dirty_Shirley` – Friedman Dirty Shirley Mini 20W *(8 modeli)*

Autor ujęć: **saschas** (A2) – legendarny inżynier dźwięku NAM  
Sprzęt: RME Fireface UCX, Palmer Daccapo Reamp, Suhr Reactive Load  
Wzmacniacz: **Friedman Dirty Shirley Mini 20W**  
Charakter: Elastyczny, reaktywny. Od czystego Fender-like po mocny przester w stylu JCM800.

| Plik | Gain | Barwa | Tryb | Opis |
|------|------|-------|------|------|
| `DSMIN_01_CLN_NAT_STD.nam` | CLN | NAT | STD | Czysty kanał – MV10 Gain 4 (saschas) |
| `DSMIN_02_LOW_NAT_KLN.nam` | LOW | NAT | KLN | Low Gain 3.5 + dopalacz Klon Centaur |
| `DSMIN_03_LOW_DRV_STD.nam` | LOW | DRV | STD | Low Drive Gain 6 – reaktywny overdrive |
| `DSMIN_04_CRN_NAT_STD.nam` | CRN | NAT | STD | Klasyczny Crunch Gain 4 bez boostu |
| `DSMIN_05_CRN_TIG_BUX.nam` | CRN | TIG | BUX | Crunch Gain 4 + BuxBoost (tight bas) |
| `DSMIN_06_CRN_FUL_STD.nam` | CRN | FUL | STD | Śpiewny Crunch Gain 6, pełna masa |
| `DSMIN_07_CRN_BRT_PRQ.nam` | CRN | BRT | PRQ | Crunch Gain 6 + Pre-EQ (wygładzona góra) |
| `DSMIN_08_HI_NAT_STD.nam`  | HI  | NAT | STD | High Gain 8 – pełny przester solowy |

---

## 7. Szybki Klucz Dekodowania

Aby zdekodować nazwę pliku:

```
SLO30_08_HI_DRK_LD.nam
│     │  │   │   └── CHAR: Lead voiced (solo)
│     │  │   └────── TONE: Dark EQ (warm, treble rolled off)
│     │  └────────── GAIN: High Gain (full distortion)
│     └───────────── NN: Pozycja numer 08 w kolejności gainu
└─────────────────── AMP: Soldano SLO-30
```

```
DSMIN_05_CRN_TIG_BUX.nam
│      │  │   │   └── CHAR: BuxBoost aktywny (tight low-end)
│      │  │   └────── TONE: Tight EQ (punchy bass, cuts)
│      │  └────────── GAIN: Crunch (medium saturation)
│      └───────────── NN: Pozycja numer 05 w kolejności gainu
└──────────────────── AMP: Friedman Dirty Shirley Mini
```

---

## 8. Zasady i Konwencje

1. **Kolejność numeryczna** (`NN`) zawsze odpowiada rosnącemu poziomowi nasycenia gainu.
2. **Clean (`CLN`) zawsze na pozycji `01`** – jeśli wzmacniacz nie miał dedykowanego modelu clean, pobierany jest z najlepszej paczki tego samego wzmacniacza.
3. **Maksymalnie 35 znaków** łącznie z rozszerzeniem `.nam` (wymóg Sonulab StompStation PRO).
4. **Wszystkie modele są Architecture 2 (A2)** – format obsługiwany przez Sonulab StompStation PRO.
5. **Kopie zapasowe** przechowywane są w `C:\Users\dariu\Documents\nam_ir\nam_copy\`.

---

*Dokumentacja wygenerowana: 2026-07-22*  
*Projekt: Sonulab StompStation PRO – Kolekcja NAM / IR*
