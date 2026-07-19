# organize_nam_ir.ps1
# Script to organize NAM and IR files from Downloads into Documents/nam_ir

$downloadsPath = Join-Path $env:USERPROFILE "Downloads"
$documentsPath = Join-Path $env:USERPROFILE "Documents"
$namIrBase = Join-Path $documentsPath "nam_ir"

if (-not (Test-Path $downloadsPath)) {
    Write-Error "Downloads folder not found at $downloadsPath"
    exit 1
}

# Load ZIP helper
[System.Reflection.Assembly]::LoadWithPartialName('System.IO.Compression.FileSystem') | Out-Null

function Process-ZipFiles($zipList) {
    $processed = 0
    foreach ($zipFile in $zipList) {
        if (-not (Test-Path -LiteralPath $zipFile.FullName)) { continue }
        $zipPath = $zipFile.FullName
        $zipName = $zipFile.BaseName
        
        try {
            $zip = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
            $hasNam = $false
            $hasIr = $false
            
            foreach ($entry in $zip.Entries) {
                $ext = [System.IO.Path]::GetExtension($entry.Name).ToLower()
                if ($ext -eq ".nam") {
                    $hasNam = $true
                }
                elseif ($ext -eq ".wav" -or $ext -eq ".ir") {
                    $hasIr = $true
                }
            }
            $zip.Dispose()
            
            $subFolder = $null
            if ($hasNam) {
                $subFolder = "nam"
            }
            elseif ($hasIr) {
                $subFolder = "ir"
            }
            
            if ($subFolder) {
                $targetDir = Join-Path $namIrBase $subFolder
                $targetDir = Join-Path $targetDir $zipName
                
                # Ensure destination folder does not exist before extracting
                if (Test-Path -LiteralPath $targetDir) {
                    Remove-Item -LiteralPath $targetDir -Recurse -Force | Out-Null
                }
                
                Write-Host "Extracting: $($zipFile.Name) to Documents\nam_ir\$subFolder\$zipName..."
                [System.IO.Compression.ZipFile]::ExtractToDirectory($zipPath, $targetDir)
                
                # Remove the source zip file after successful extraction
                Remove-Item -LiteralPath $zipPath -Force
                Write-Host "Removed source zip: $($zipFile.Name)"
                $processed++
            }
        }
        catch {
            Write-Warning "Could not process zip file: $($zipFile.Name). Error: $_"
            if ($zip) { $zip.Dispose() }
        }
    }
    return $processed
}

# 1. Look for ZIPs in the last 24 hours
$recentZips = Get-ChildItem -Path $downloadsPath -Filter *.zip | Where-Object { $_.LastWriteTime -gt (Get-Date).AddHours(-24) }
$processedCount = 0

if ($recentZips) {
    $processedCount = Process-ZipFiles $recentZips
}

# 2. If nothing processed from the last 24 hours, fallback to the 5 most recent ZIPs in Downloads
if ($processedCount -eq 0) {
    $fallbackZips = Get-ChildItem -Path $downloadsPath -Filter *.zip | Sort-Object LastWriteTime -Descending | Select-Object -First 5
    if ($fallbackZips) {
        Write-Host "No NAM/IR files processed in the last 24 hours. Checking fallback (5 most recent ZIPs)..."
        $processedCount = Process-ZipFiles $fallbackZips
    }
}

Write-Host "Done. Processed $processedCount file(s)."
