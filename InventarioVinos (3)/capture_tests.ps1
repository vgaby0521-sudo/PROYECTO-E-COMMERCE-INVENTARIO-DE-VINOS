Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$projectPath = "C:\Users\ASUS\Downloads\InventarioVinos (3)"
$capturesPath = Join-Path $projectPath "captures_unit_tests"

# Crear carpeta si no existe
if (-Not (Test-Path $capturesPath)) {
    New-Item -ItemType Directory -Path $capturesPath | Out-Null
}

Write-Host "Iniciando capturas cada 5 segundos... Ctrl+C para detener."

while ($true) {
    $file = Join-Path $capturesPath ("captura_{0}.png" -f (Get-Date -Format "yyyyMMdd_HHmmss"))

    $bitmap = New-Object System.Drawing.Bitmap(
        [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Width,
        [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Height
    )

    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    $graphics.CopyFromScreen(0, 0, 0, 0, $bitmap.Size)
    $bitmap.Save($file)

    Start-Sleep -Seconds 5
}
