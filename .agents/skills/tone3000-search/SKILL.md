---
name: tone3000-search
description: >-
  Searches the TONE3000.com database for NAM A2 models and displays detailed metadata
  such as description, gear type, model size, downloads, and favorites.
---

# TONE3000 Search Skill

## Overview
This skill allows the agent to search for NAM A2 models and rig profiles on TONE3000.com and retrieve detailed metadata without downloading files. It uses the `download_nam.py` script with the `--info` flag.

## Dependencies
- Virtual environment `.venv` with `requests` library installed.
- Python (`py` / `python`).
- Valid API Secret Key in `c:\Users\dariu\agy\agy-sonulab\.env`.

## Usage
To search for tones, run the Python script using the virtual environment:

```powershell
.\.venv\Scripts\python.exe c:\Users\dariu\agy\agy-sonulab\download_nam.py --search "<QUERY>" --info
```

### Filters
You can combine the search with the following filters:
- `--gears`: Filter by gear type (`amp`, `amp-cab`, `pedal`, `outboard`, `cab`, `space`, `experimental`). Multiple values joined by `_`.
- `--sizes`: Filter by model size (`standard`, `lite`, `feather`, `nano`, `custom`). Multiple values joined by `_`.
- `--sort`: Sort by `best-match`, `newest`, `oldest`, `trending`, or `downloads-all-time`.
- `--calibrated`: Restrict results to calibrated models only.

Example:
```powershell
.\.venv\Scripts\python.exe c:\Users\dariu\agy\agy-sonulab\download_nam.py --search "Peavey 5150" --gears "amp" --sort "downloads-all-time" --info
```

## Workflow
When the user asks to search or check for tones:
1. Extract the search terms and any filters from the user request.
2. Run the python command with `--info` and matching parameters.
3. Parse the results and display the formatted report (downloads, likes, description, URL) to the user.
