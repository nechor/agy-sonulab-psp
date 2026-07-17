# Lista Wzmacniaczy w Sonulab StompStation PRO

Poniżej znajduje się szczegółowa analiza i identyfikacja fabrycznych/użytkownika profili wzmacniaczy (NAM) zainstalowanych w urządzeniu. 

---

## Klucz do klasyfikacji (Wzmacniacz + Kolumna vs. Sam Wzmacniacz)

Po analizie nazewnictwa plików możemy podzielić profile na trzy główne kategorie:
1. **[RIG / CAB] (Pełna symulacja wzmacniacza i kolumny głośnikowej):**
   * **Sygnowane `CR -` (prawdopodobnie "Capture Rig" lub Choptones Rig):** Są to pełne profile brzmieniowe (Rig) przechwycone wraz z kolumną głośnikową i mikrofonem.
   * **Sygnowane `CAB`:** Pliki bezpośrednio wskazujące na obecność kolumny głośnikowej w profilu.
   * **Sygnowane `SUM / SU`:** Prawdopodobnie "Studio Setup" / "Studio Capture", czyli pełny tor mikrofonowy z kolumną.
2. **[AMP ONLY] (Tylko wzmacniacz / Direct Capture / Preamp):**
   * **Sygnowane `[AMP]`:** Profile czyste, reprezentujące wyłącznie głowę wzmacniacza (lub przedwzmacniacz). Wymagają aktywacji bloku **IR** w StompStation dla uzyskania naturalnego brzmienia.
3. **[Niejednoznaczne / Do weryfikacji]:**
   * Standardowe profile bez wyraźnego oznaczenia. Zazwyczaj w domyślnych paczkach NAM są to pełne profile typu Rig, ale na urządzeniach wieloefektowych czasami instaluje się wersje Direct (Amp only), aby użytkownik mógł samodzielnie nakładać impulsy z bloku IR.

---

## Szczegółowa Tabela Identyfikacji Wzmacniaczy

| Lp. | Oryginalna nazwa w sprzęcie | Rozpoznany model (Oryginalny wzmacniacz) | Typ profilu (Szacowany) | Uzasadnienie klasyfikacji |
|---|---|---|---|---|
| **1** | CR - American Clean | Fender (np. Twin Reverb / Deluxe Reverb) | **[RIG / CAB]** | Przedrostek `CR` sugeruje Capture Rig. |
| **2** | CR - British 900 | Marshall JCM900 | **[RIG / CAB]** | Przedrostek `CR` sugeruje Capture Rig. |
| **3** | CR - British Clean | Marshall (klasyczny kanał Clean, np. Plexi/JTM45) | **[RIG / CAB]** | Przedrostek `CR` sugeruje Capture Rig. |
| **4** | CR - British Crunch | Marshall (brzmienie Plexi / JCM800 na krawędzi przesteru) | **[RIG / CAB]** | Przedrostek `CR` sugeruje Capture Rig. |
| **5** | CR - British Lead | Marshall (kanał przesterowany JCM800 / JCM2000) | **[RIG / CAB]** | Przedrostek `CR` sugeruje Capture Rig. |
| **6** | CR - Cali | Mesa Boogie (seria Dual Rectifier lub Mark) | **[RIG / CAB]** | Przedrostek `CR` sugeruje Capture Rig. |
| **7** | CR - Compound Pre | Prawdopodobnie przedwzmacniacz wielokanałowy lub miks | **[RIG / CAB]** | Przedrostek `CR` sugeruje Capture Rig. |
| **8** | CR - Ed Van Blue | Peavey 5150 / EVH 5150 III (kanał niebieski "Blue") | **[RIG / CAB]** | Przedrostek `CR` sugeruje Capture Rig. |
| **9** | CR - Pivi 65 | Peavey 5150 / 6505 | **[RIG / CAB]** | Przedrostek `CR` sugeruje Capture Rig. |
| **10**| CR - SenzAMP | Tech 21 SansAmp (preamp analogowy / emulator) | **[RIG / CAB]** | Przedrostek `CR` sugeruje Capture Rig. |
| **13**| Voz 30 | Vox AC30 | **[Niejednoznaczne]** | Brak oznaczenia, prawdopodobnie Rig. |
| **14**| [AMP] DiZLVH4-CH4 Lead the Way | Diezel VH4 (Kanał 4 - Lead) | **[AMP ONLY]** | Wyraźne oznaczenie `[AMP]`. |
| **15**| 800 Lo Gain | Marshall JCM800 (niskie nasycenie / Low Gain) | **[Niejednoznaczne]** | Prawdopodobnie Rig. |
| **16**| AP-AC30_06_Ch1 Bright On V3 TC7 | Vox AC30HW2X (kanał 1 z filtrem Bright, autor: A. Perfilyev) | **[Niejednoznaczne]** | Nazwa techniczna, może być Direct (Amp) lub Rig. |
| **17**| BallOfFire 100 | ENGL Fireball 100 | **[Niejednoznaczne]** | Prawdopodobnie Rig. |
| **18**| Bogie IIC Thrash | Mesa Boogie Mark IIC+ (brzmienie thrash metalowe) | **[Niejednoznaczne]** | Prawdopodobnie Rig. |
| **19**| Edgy Plex | Marshall Plexi (z agresywnym, ostrym charakterem) | **[Niejednoznaczne]** | Prawdopodobnie Rig. |
| **20**| Fender - Princeton Clean 3 SUM | Fender Princeton Reverb (kanał Clean) | **[RIG / CAB]** | Dopisek `SUM` sugeruje sumaryczne ujęcie (Rig/Studio). |
| **21**| Fender - Princeton EOB Vol 5 SU | Fender Princeton (EOB = sygnatura Ed O'Brien z Radiohead) | **[RIG / CAB]** | Dopisek `SU` sugeruje Studio Setup (Rig). |
| **22**| Hi Wattage 103 | Hiwatt Custom 103 | **[Niejednoznaczne]** | Prawdopodobnie Rig. |
| **23**| MRSH MJR I Dimed BAL3 CAB | Marshall Major (odkręcony głośno / "Dimed") | **[RIG / CAB]** | Wyraźny dopisek `CAB` na końcu nazwy. |
| **24**| Recty II Rhythm | Mesa Boogie Dual Rectifier (kanał 2, brzmienie rytmiczne) | **[Niejednoznaczne]** | Prawdopodobnie Rig. |
| **25**| SL 100 | Soldano SLO-100 (Super Lead Overdrive) | **[Niejednoznaczne]** | Prawdopodobnie Rig. |
| **26**| Voz 15 Clean | Vox AC15 (kanał czysty / Clean) | **[Niejednoznaczne]** | Prawdopodobnie Rig. |

*Ostatnia aktualizacja analizy: 2026-07-18*
