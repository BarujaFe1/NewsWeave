# Trigger de ingestão manual
$apiUrl = "http://localhost:8000/api/ingest"
Write-Host "Disparando ingestão em $apiUrl..."
try {
    $response = Invoke-RestMethod -Uri $apiUrl -Method Post
    Write-Host "OK: $($response.message) - $($response.articles) artigos"
} catch {
    Write-Host "Erro: $_"
}
