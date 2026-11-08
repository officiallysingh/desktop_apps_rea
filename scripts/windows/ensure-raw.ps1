<#
.SYNOPSIS  Recreate the git-ignored _raw\<app> workspaces after a fresh clone.
#>
$root = Resolve-Path (Join-Path $PSScriptRoot '..\..')
Get-ChildItem $root -Directory | Where-Object { Test-Path (Join-Path $_.FullName 'PROGRESS.md') } | ForEach-Object {
  foreach ($d in 'bin','decompiled','dumps','captures','db-copies','screens','reports') {
    New-Item -ItemType Directory -Force -Path (Join-Path $root "_raw\$($_.Name)\$d") | Out-Null
  }
  Write-Host "_raw\$($_.Name) ready"
}
