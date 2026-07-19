---
name: new-nam
description: >-
  Scans recently downloaded files and ZIPs in the user's Downloads directory.
  If it detects Neural Amp Modeler (.nam), Impulse Response (.wav/.ir) or Sonulab Preset (.pst)
  files, it extracts and organizes them into C:\Users\dariu\Documents\nam_ir\nam,
  C:\Users\dariu\Documents\nam_ir\ir, or C:\Users\dariu\Documents\nam_ir\presets folders.
---

# New NAM, IR, and Preset Organizer

## Overview
This skill scans the user's `Downloads` folder for recently modified/downloaded ZIP files or direct files. It inspects them for:
- `.nam` files (Neural Amp Modeler profiles)
- `.wav` / `.ir` files (Impulse Responses)
- `.pst` files (Sonulab Presets)

Based on the file type, it moves or extracts them into:
- `C:\Users\dariu\Documents\nam_ir\nam\`
- `C:\Users\dariu\Documents\nam_ir\ir\`
- `C:\Users\dariu\Documents\nam_ir\presets\`

## Dependencies
- Python 3.x
- Virtual environment `.venv` configured in the workspace root.

## Quick Start
To trigger this skill, the user can say "new nam". The agent then runs the Python organizer script:

```powershell
.\.venv\Scripts\python.exe c:\Users\dariu\agy\agy-sonulab\.agents\skills\new-nam\organize_nam_ir.py
```

## Workflow
When the user says "new nam":
1. Run the Python helper script:
   ```powershell
   .\.venv\Scripts\python.exe c:\Users\dariu\agy\agy-sonulab\.agents\skills\new-nam\organize_nam_ir.py
   ```
2. Display the output logs of the script to the user, highlighting which files or ZIPs were detected, where they were moved/extracted, and the final count of processed files.

## Common Mistakes
- **No files found**: If no files are processed, ensure the downloaded files have `.nam`, `.wav`, `.ir`, `.pst`, or `.zip` extensions and are located in `Downloads`.
- **ZIP not extracted**: The ZIP file must contain at least one `.nam`, `.wav`/`.ir`, or `.pst` file at some level inside the archive to trigger extraction.
