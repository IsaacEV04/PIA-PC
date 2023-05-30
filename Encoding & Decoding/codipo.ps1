Write-Host "Bienvenido a un ejemplo de codificacion/ decodificacion base64 usando powershell" -ForegroundColor Green
Write-Host "Codificando un archivo de texto"
$inputfile = "C:\Users\isaac\OneDrive\Escritorio\secret.txt"
$fc = Get-Content $inputfile
$GB = [System.Text.Encoding]::UTF8.GetBytes($fc)
$etext = [System.Convert]::ToBase64String($GB)
Write-Host "El contenido del archivo CODIFICADO es:" $etext -ForegroundColor Green
Write-Host "DECODIFICANDO el texto previo:"
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($etext)) | Out-File -Encoding "ASCII" "C:\Users\isaac\OneDrive\Escritorio\decoder_posh.ps1"
$outfile12 = get-content C:\Users\isaac\OneDrive\Escritorio\decoder_posh.ps1
Write-Host "El texto decodificado es el siguiente:" -ForegroundColor Green
Write-Host "DECODIFICANDO:" $$outfile12