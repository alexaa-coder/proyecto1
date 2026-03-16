#!/bin/bash
# backup.sh — Crea backup comprimido de la documentación
# Uso: ./scripts/backup.sh

set -e

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BACKUP_DIR="$PROJECT_DIR/scripts/backups"
FECHA=$(date '+%Y-%m-%d_%H-%M')
NOMBRE_BACKUP="backup_docs_$FECHA.tar.gz"
LOG_FILE="$PROJECT_DIR/scripts/logs/backup.log"

mkdir -p "$BACKUP_DIR"
mkdir -p "$PROJECT_DIR/scripts/logs"

echo "[$FECHA] Iniciando backup..." | tee -a "$LOG_FILE"

tar -czf "$BACKUP_DIR/$NOMBRE_BACKUP" \
    -C "$PROJECT_DIR" \
    docs/ \
    docusaurus.config.js \
    sidebars.js \
    package.json \
    Dockerfile \
    docker-compose.yml \
    nginx.conf

TAMANIO=$(du -sh "$BACKUP_DIR/$NOMBRE_BACKUP" | cut -f1)
echo "[$FECHA] Backup creado: $NOMBRE_BACKUP ($TAMANIO)" | tee -a "$LOG_FILE"

# Conservar solo los últimos 5 backups
cd "$BACKUP_DIR"
ls -t backup_docs_*.tar.gz | tail -n +6 | xargs -r rm
echo "[$FECHA] Backups antiguos limpiados. Backups actuales: $(ls backup_docs_*.tar.gz | wc -l)" | tee -a "$LOG_FILE"
