"""Bucle del agente: el modelo decide qué herramienta usar hasta terminar la tarea."""
import ollama

from config import MAX_PASOS, MODELO, VAULT
from vault_tools import FUNCIONES, HERRAMIENTAS


def cargar_prompt(area: str) -> str:
    """El system prompt de cada área vive en el vault: agentes/<area>.md"""
    ruta = VAULT / "agentes" / f"{area}.md"
    if not ruta.exists():
        raise FileNotFoundError(f"No hay prompt para el área '{area}' en {ruta}")
    return ruta.read_text(encoding="utf-8")


def ejecutar(area: str, tarea: str, verbose: bool = True) -> str:
    mensajes = [
        {"role": "system", "content": cargar_prompt(area)},
        {"role": "user", "content": tarea},
    ]
    for paso in range(1, MAX_PASOS + 1):
        resp = ollama.chat(
            model=MODELO, messages=mensajes, tools=HERRAMIENTAS,
            options={"temperature": 0.3},
        )
        mensajes.append(resp.message)

        if not resp.message.tool_calls:  # ya no pide herramientas -> ha terminado
            return resp.message.content

        for call in resp.message.tool_calls:
            nombre, args = call.function.name, call.function.arguments or {}
            if verbose:
                resumen = ", ".join(f"{k}={str(v)[:40]!r}" for k, v in args.items())
                print(f"  [{paso}] {nombre}({resumen})")
            try:
                resultado = FUNCIONES[nombre](**args)
            except Exception as e:  # el error vuelve al modelo para que se corrija
                resultado = f"ERROR en {nombre}: {e}"
            mensajes.append({"role": "tool", "content": str(resultado), "tool_name": nombre})

    return "Se alcanzó el máximo de pasos sin terminar la tarea."
