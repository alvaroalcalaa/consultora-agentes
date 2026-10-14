"""Configuración del agente. Todo se puede sobrescribir con variables de entorno."""
import os
from pathlib import Path

# Ruta a tu vault de Obsidian (por defecto, el vault de ejemplo del repo)
VAULT = Path(os.getenv("VAULT_PATH", Path(__file__).parent / "vault_ejemplo")).resolve()

MODELO = os.getenv("MODELO", "qwen3:8b")                     # o "gemma4:cloud"
MODELO_EMBED = os.getenv("MODELO_EMBED", "nomic-embed-text")  # embeddings locales

INDICE = VAULT / ".indice_agente.json"  # empieza por "." -> Obsidian lo ignora
MAX_PASOS = int(os.getenv("MAX_PASOS", "12"))
CARPETA_ESCRIBIBLE = "clientes"         # el agente solo puede escribir aquí
