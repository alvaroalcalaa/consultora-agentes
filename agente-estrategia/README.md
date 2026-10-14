# Agente de Estrategia sobre Obsidian + Ollama

Agente consultor que lee y escribe en un vault de Obsidian. Primer agente de área para `consultora-agentes`.

## Puesta en marcha (Windows / PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

ollama pull qwen3:8b
ollama pull nomic-embed-text

python main.py --indexar
python main.py "Haz un diagnóstico estratégico de ceramicas-levante a partir del kickoff del 14/10"
```

El entregable aparece en `vault_ejemplo/clientes/ceramicas-levante/entregables/`.
Abre `vault_ejemplo` como vault en Obsidian para verlo con sus enlaces y el grafo.

## Usar tu propio vault o un modelo cloud

```powershell
$env:VAULT_PATH = "C:\ruta\a\tu\vault"
$env:MODELO = "gemma4:cloud"   # antes: ollama signin
```

## Estructura

| Fichero | Qué hace |
|---|---|
| `config.py` | Rutas y modelos (sobrescribibles con variables de entorno) |
| `vault_tools.py` | Herramientas: `buscar_notas`, `leer_nota`, `listar_cliente`, `escribir_nota` + índice semántico |
| `agente.py` | Bucle del agente (tool calling con Ollama) |
| `main.py` | CLI |
| `vault_ejemplo/agentes/<area>.md` | System prompt de cada área: se edita desde Obsidian |

## Guardarraíles incluidos

- El agente no puede leer ni escribir fuera del vault.
- Solo escribe en `clientes/`, y nunca sobrescribe: si la nota existe, crea una versión con fecha.
- Toda nota generada lleva frontmatter con `estado: borrador` y `generado_por: agente`.
- El índice solo re-embebe notas modificadas y se guarda en `.indice_agente.json` (ignorado por Obsidian y git).

## Añadir un área nueva

Crea `vault_ejemplo/agentes/operaciones.md` con su prompt y ejecuta:

```powershell
python main.py --area operaciones "..."
```
