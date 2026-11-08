<#
.SYNOPSIS
  Installs the reverse-engineering toolchain on the Windows analysis machine.
.DESCRIPTION
  Run from an elevated PowerShell:  powershell -ExecutionPolicy Bypass -File scripts\windows\setup-tools.ps1
  Every step is best-effort: failures are reported at the end, nothing aborts the run.
  Use -CheckOnly to only report what is installed.
#>
param([switch]$CheckOnly)

$ErrorActionPreference = 'Continue'
$failed = New-Object System.Collections.Generic.List[string]

function Test-Admin {
  $id = [Security.Principal.WindowsIdentity]::GetCurrent()
  (New-Object Security.Principal.WindowsPrincipal $id).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

function Install-Winget($id, $name) {
  $present = winget list --id $id -e --accept-source-agreements 2>$null | Select-String -SimpleMatch $id
  if ($present) { Write-Host "[ok]      $name" -ForegroundColor Green; return }
  if ($CheckOnly) { Write-Host "[missing] $name ($id)" -ForegroundColor Yellow; return }
  Write-Host "[install] $name ($id)" -ForegroundColor Cyan
  winget install --id $id -e --silent --accept-package-agreements --accept-source-agreements
  if ($LASTEXITCODE -ne 0) { $failed.Add("$name ($id)") }
}

if (-not $CheckOnly -and -not (Test-Admin)) {
  Write-Warning 'Run this script from an elevated (Administrator) PowerShell.'; exit 1
}

# --- Base -------------------------------------------------------------------
$packages = [ordered]@{
  'Git.Git'                                  = 'Git for Windows (bash used by Claude Code)'
  'Python.Python.3.12'                       = 'Python 3.12 (Frida tools)'
  'Microsoft.DotNet.SDK.8'                   = '.NET 8 SDK (ilspycmd)'
  'EclipseAdoptium.Temurin.21.JDK'           = 'JDK 21 (Ghidra)'
  '7zip.7zip'                                = '7-Zip (installer extraction)'
  # --- Monitoring ---
  'Microsoft.Sysinternals.ProcessMonitor'    = 'Sysinternals Process Monitor'
  'Microsoft.Sysinternals.ProcessExplorer'   = 'Sysinternals Process Explorer'
  'WiresharkFoundation.Wireshark'            = 'Wireshark'
  'Telerik.Fiddler.Classic'                  = 'Fiddler Classic'
  # --- Databases ---
  'DBBrowserForSQLite.DBBrowserForSQLite'    = 'DB Browser for SQLite'
  'Microsoft.SQLServerManagementStudio'      = 'SQL Server Management Studio'
  # --- UI and capture ---
  'Microsoft.AccessibilityInsights'          = 'Accessibility Insights for Windows'
  'ShareX.ShareX'                            = 'ShareX (screenshots)'
  'OBSProject.OBSStudio'                     = 'OBS Studio (workflow recordings)'
}
foreach ($k in $packages.Keys) { Install-Winget $k $packages[$k] }

# --- Claude Code (native installer) -----------------------------------------
if (Get-Command claude -ErrorAction SilentlyContinue) {
  Write-Host '[ok]      Claude Code' -ForegroundColor Green
} elseif ($CheckOnly) {
  Write-Host '[missing] Claude Code' -ForegroundColor Yellow
} else {
  Write-Host '[install] Claude Code' -ForegroundColor Cyan
  try { Invoke-RestMethod https://claude.ai/install.ps1 | Invoke-Expression } catch { $failed.Add('Claude Code') }
}

if (-not $CheckOnly) {
  # Refresh PATH for this session so dotnet/pip are visible
  $env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User')

  # --- .NET decompiler CLI ---
  Write-Host '[install] ilspycmd' -ForegroundColor Cyan
  dotnet tool install -g ilspycmd 2>$null; if ($LASTEXITCODE -ne 0) { dotnet tool update -g ilspycmd | Out-Null }

  # --- Frida ---
  Write-Host '[install] frida-tools' -ForegroundColor Cyan
  python -m pip install --upgrade frida-tools
  if ($LASTEXITCODE -ne 0) { $failed.Add('frida-tools (pip)') }

  # --- Long paths (deep decompiled trees) ---
  Write-Host '[config]  Long paths' -ForegroundColor Cyan
  New-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem' -Name 'LongPathsEnabled' -Value 1 -PropertyType DWORD -Force | Out-Null
  git config --system core.longpaths true
}

# --- Manual installs ----------------------------------------------------------
Write-Host ''
Write-Host 'Install manually (no reliable winget package):' -ForegroundColor Yellow
Write-Host '  - Ghidra        https://github.com/NationalSecurityAgency/ghidra/releases  -> C:\Tools\ghidra'
Write-Host '  - dnSpyEx       https://github.com/dnSpyEx/dnSpy/releases                  -> C:\Tools\dnSpyEx'
Write-Host '  - de4dot        (only if .NET binaries are obfuscated)                      -> C:\Tools\de4dot'
Write-Host '  - x64dbg        https://x64dbg.com                                         -> C:\Tools\x64dbg'
Write-Host '  - FlaUInspect   https://github.com/FlaUI/FlaUInspect/releases              -> C:\Tools\FlaUInspect'
Write-Host '  - IDR (Delphi)  only if the app is Delphi                                   -> C:\Tools\IDR'
Write-Host '  - rea MCP server: follow its own install docs, then: claude mcp add rea ...'
Write-Host ''
Write-Host 'Add a Windows Defender exclusion for C:\Tools (Frida, x64dbg and de4dot get flagged).' -ForegroundColor Yellow

# --- Verify the app-protection guard can run (Claude Code hook needs a real python on PATH) ---
$py = Get-Command python -ErrorAction SilentlyContinue
if (-not $py -or $py.Source -like '*WindowsApps*') {
  Write-Host '[WARN]    python is missing or is the Microsoft Store stub: the app-protection guard hook will NOT run.' -ForegroundColor Red
  $failed.Add('python on PATH for .claude/hooks/app_guard.py')
} else {
  Write-Host "[ok]      python for app-protection guard: $($py.Source)" -ForegroundColor Green
}

if ($failed.Count -gt 0) {
  Write-Host ''
  Write-Host 'Failed (install manually):' -ForegroundColor Red
  $failed | ForEach-Object { Write-Host "  - $_" }
}
