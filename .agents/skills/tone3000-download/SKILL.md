---
name: tone3000-download
description: >-
  Downloads NAM A2 files (.nam) from TONE3000.com based on a search query or a specific Tone ID.
---

# TONE3000 Download Skill

## Overview
This skill allows the agent to download NAM A2 amplifier and rig models (.nam files) from TONE3000.com directly to a local directory (by default `./downloads` or a user-specified path).

## Dependencies
- Virtual environment `.venv` with `requests` library installed.
- Python (`py` / `python`).
- Valid API Secret Key in `c:\Users\dariu\agy\agy-sonulab\.env`.

## Usage
To download tones, run the Python script using the virtual environment:

### Download by Search Query (downloads the top match):
```powershell
.\.venv\Scripts\python.exe c:\Users\dariu\agy\agy-sonulab\download_nam.py --search "<QUERY>" --out-dir "<OUTPUT_DIRECTORY>"
```

### Download by specific Tone ID:
```powershell
.\.venv\Scripts\python.exe c:\Users\dariu\agy\agy-sonulab\download_nam.py --tone-id <TONE_ID> --out-dir "<OUTPUT_DIRECTORY>"
```

### Download multiple tones using a text file list:
```powershell
.\.venv\Scripts\python.exe c:\Users\dariu\agy\agy-sonulab\download_nam.py --file "<PATH_TO_TEXT_FILE>" --out-dir "<OUTPUT_DIRECTORY>"
```

### Filters
You can apply filters when searching to download the correct tone:
- `--gears`: Filter by gear type (`amp`, `amp-cab`, `pedal`, etc.).
- `--sizes`: Filter by model size (`standard`, `lite`, `feather`, `nano`, `custom`).
- `--sort`: Sort by `best-match`, `newest`, `oldest`, `trending`, or `downloads-all-time`.
- `--calibrated`: Only download calibrated models.

## Workflow
When the user asks to download a tone:
1. Extract the search query, Tone ID, or file list from the user request.
2. Determine the desired output directory (if specified).
3. Run the python command with matching parameters.
4. Verify the download succeeded (check if `.nam` files were saved in the output directory) and report the files back to the user.
