$ErrorActionPreference = "Stop"

$projectName = (Get-Item .).Name.ToLower()

if (!(Test-Path "./a_core/.env") -and (Test-Path "./a_core/.env.example")) {
    Copy-Item "./a_core/.env.example" "./a_core/.env"
}

$env:COMPOSE_PROJECT_NAME = $projectName

docker compose down
docker compose up -d --build