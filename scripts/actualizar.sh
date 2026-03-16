#!/bin/bash
# actualizar.sh — Reconstruye y reinicia el contenedor de documentación
# Uso: ./scripts/actualizar.sh

set -e  # Para si cualquier comando falla

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
LOG_FILE="$PROJECT_DIR/scripts/logs/actualizar.log"
FECHA=$(date '+%Y-%m-%d %H:%M:%S')

mkdir -p "$PROJECT_DIR/scripts/logs"

echo "[$FECHA] Iniciando actualización..." | tee -a "$LOG_FILE"

cd "$PROJECT_DIR"

echo "[$FECHA] Bajando contenedor..." | tee -a "$LOG_FILE"
docker compose down

echo "[$FECHA] Reconstruyendo imagen..." | tee -a "$LOG_FILE"
docker compose build --no-cache

echo "[$FECHA] Levantando contenedor..." | tee -a "$LOG_FILE"
docker compose up -d

echo "[$FECHA] Actualización completada. Disponible en http://localhost:8080" | tee -a "$LOG_FILE"
