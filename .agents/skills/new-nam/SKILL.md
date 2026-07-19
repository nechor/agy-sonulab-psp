---
name: new-nam
description: >-
  Scans recently downloaded ZIP files in the user's Downloads directory.
  If a ZIP contains Neural Amp Modeler (.nam) files or Impulse Response (.wav/.ir)
  files, it extracts and organizes them into C:\Users\dariu\Documents\nam_ir\nam or
  C:\Users\dariu\Documents\nam_ir\ir folders.
---

# New NAM Organizer

## Overview
This skill scans the user's `Downloads` folder for recently modified/downloaded ZIP files. It inspects their contents to check for `.nam` (Neural Amp Modeler profiles) or `.wav`/`.ir` (Impulse Responses) files. Based on the file type, it extracts the archive into a dedicated subfolder under `Documents\nam_ir\nam\` or `Documents\nam_ir\ir\`.

## Dependencies
- PowerShell 5.0 or newer.

## Quick Start
To trigger this skill, the user can say "new nam". The agent then runs the organization script:

```powershell
powershell -ExecutionPolicy Bypass -File "c:\Users\dariu\agy\agy-sonulab\.agents\skills\new-nam\organize_nam_ir.ps1"
```

## Workflow
When the user says "new nam":
1. Run the helper PowerShell script:
   ```powershell
   powershell -ExecutionPolicy Bypass -File "c:\Users\dariu\agy\agy-sonulab\.agents\skills\new-nam\organize_nam_ir.ps1"
   ```
2. Display the output logs of the script to the user, highlighting which ZIP files were detected, where they were extracted, and the final count of processed files.

## Common Mistakes
- **No ZIPs found**: If no ZIP files are in the Downloads directory, ensure the files have been downloaded as `.zip`.
- **Wrong extensions**: Files inside ZIP must end with `.nam`, `.wav`, or `.ir` to be detected and processed.
