# Build degli asset immagine del D1 TEPO.
# Uso (Windows PowerShell 5.1; su questa macchina "pwsh" non e' installato):
#   powershell -NoProfile -ExecutionPolicy Bypass -File build.ps1 [-Root <repo>]
#   oppure, dalla cartella src:  & .\build.ps1
# Produce e verifica: 12 schermate del frontend, 3 diagrammi Use Case e 5 User Flow.
# Le slide del pitch (img/pitch-*.jpg) sono esportate dalla presentazione TEPO.pptx
# e non vengono rigenerate da questo script.
param(
    [string]$Root = "C:\Users\mirco\progetti\tepobozza"
)

$ErrorActionPreference = "Stop"
$D1  = Join-Path $Root "deliverable\D1"
$Img = Join-Path $D1 "img"
$Src = Join-Path $Img "src"
$Shot = Join-Path $Root "docs\screenshot\v2"

New-Item -ItemType Directory -Force -Path $Img | Out-Null

# 1. Schermate della versione corrente (registro Relazione salvo dove indicato).
$shots = @{
    "v2-01-dashboard-relazione.png"      = "dashboard-relazione.png"
    "v2-01-dashboard-sala-operativa.png" = "dashboard-sala-operativa.png"
    "v2-02-edifici.png"                  = "edifici.png"
    "v2-03-interventi.png"               = "interventi.png"
    "v2-04-scenario.png"                 = "scenario.png"
    "v2-05-risultato.png"                = "risultato.png"
    "v2-06-confronto.png"                = "confronto.png"
    "v2-07-mappa.png"                    = "mappa.png"
    "v2-08-import.png"                   = "import.png"
    "v2-09-sensibilita.png"              = "sensibilita.png"
    "v2-10-dashboard-mobile.png"         = "dashboard-mobile.png"
    "v2-13-risultato-laptop.png"         = "risultato-laptop.png"
}
foreach ($pair in $shots.GetEnumerator()) {
    $from = Join-Path $Shot $pair.Key
    if (-not (Test-Path $from)) { throw "Schermata mancante: $from" }
    Copy-Item $from (Join-Path $Img $pair.Value) -Force
    Write-Output "copia $($pair.Value)"
}

# 2. Verifica che le slide del pitch siano presenti (esportate da TEPO.pptx).
$pitch = @(
    "pitch-01-copertina.jpg",
    "pitch-02-problema.jpg",
    "pitch-03-soluzione.jpg",
    "pitch-04-benefici.jpg",
    "pitch-05-chiusura.jpg"
)
foreach ($name in $pitch) {
    $path = Join-Path $Img $name
    if (-not (Test-Path $path)) { throw "Slide del pitch mancante: $path" }
    Write-Output "presente $name"
}

# 3. Diagrammi PlantUML (use case e user flow).
& python (Join-Path $Src "render_puml.py") $Src $Img
if ($LASTEXITCODE -ne 0) { throw "Rendering PlantUML fallito" }

Write-Output "Asset generati in $Img"
