<#
.SYNOPSIS  Scaffold a new app folder from _templates/app and its _raw workspace.
.EXAMPLE   .\scripts\windows\new-app.ps1 -Slug bahikhata
#>
param([Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]+$')][string]$Slug)

$root = Resolve-Path (Join-Path $PSScriptRoot '..\..')
$dest = Join-Path $root $Slug
if (Test-Path $dest) { Write-Error "$Slug already exists"; exit 1 }

Copy-Item -Recurse (Join-Path $root '_templates\app') $dest
foreach ($d in 'bin','decompiled','dumps','captures','db-copies','screens','reports') {
  New-Item -ItemType Directory -Force -Path (Join-Path $root "_raw\$Slug\$d") | Out-Null
}
New-Item -ItemType File -Force -Path (Join-Path $root "_raw\$Slug\name-mapping.md") | Out-Null
Write-Host "Created $Slug\ and _raw\$Slug\. Register it in _platform\apps.md, then run /inventory $Slug in Claude Code."
