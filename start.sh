#!/bin/sh
set -e

if [ ! -f ./a_core/.env ] && [ -f ./a_core/.env.example ]; then
    cp ./a_core/.env.example ./a_core/.env
fi

chmod +x ./entrypoint.sh 2>/dev/null || true
chmod +x ./start.sh 2>/dev/null || true

export COMPOSE_PROJECT_NAME=$(basename "$PWD" | tr '[:upper:]' '[:lower:]')

docker compose down
docker compose up -d --build