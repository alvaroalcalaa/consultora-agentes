"""
Lanzador de la consultora de agentes.

Uso:
    python main.py --cliente <slug-cliente>
    python main.py --cliente demo "Haz un diagnóstico estratégico express de ..."

Abre una sesión con el Director de Proyecto (orquestador) trabajando sobre el
expediente del cliente. Si el expediente no existe, lo crea desde la plantilla.
"""
import argparse
import asyncio
import shutil
from pathlib import Path

from dotenv import load_dotenv
from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ClaudeSDKClient,
    ResultMessage,
    TextBlock,
)

RAIZ = Path(__file__).parent.resolve()
CLIENTES = RAIZ / "clientes"


def preparar_expediente(slug: str) -> Path:
    expediente = CLIENTES / slug
    if not expediente.exists():
        shutil.copytree(CLIENTES / "_plantilla", expediente)
        print(f"📁 Expediente nuevo creado en {expediente}")
    return expediente


def opciones(slug: str) -> ClaudeAgentOptions:
    instrucciones = (RAIZ / "CLAUDE.md").read_text(encoding="utf-8")
    instrucciones += (
        f"\n\n## Sesión actual\nCliente: `{slug}`. "
        f"Expediente: `clientes/{slug}/`. Empieza leyendo su ficha, registro y decisiones."
    )
    return ClaudeAgentOptions(
        cwd=str(RAIZ),
        system_prompt=instrucciones,
        # Carga skills (.claude/skills) y subagentes (.claude/agents) del proyecto
        setting_sources=["project"],
        # "Task" es la herramienta con la que el orquestador delega en subagentes.
        # Si tu versión del SDK la llama distinto, revisa la documentación del SDK.
        allowed_tools=[
            "Skill", "Task", "Read", "Write", "Edit", "Bash",
            "Glob", "Grep", "WebSearch", "WebFetch",
        ],
        permission_mode="acceptEdits",
    )


async def imprimir_respuesta(cliente: ClaudeSDKClient) -> None:
    async for mensaje in cliente.receive_response():
        if isinstance(mensaje, AssistantMessage):
            for bloque in mensaje.content:
                if isinstance(bloque, TextBlock):
                    print(bloque.text)
        elif isinstance(mensaje, ResultMessage) and mensaje.total_cost_usd:
            print(f"\n💶 Coste de este turno: ${mensaje.total_cost_usd:.3f}")


async def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(description="Consultora de agentes")
    parser.add_argument("--cliente", required=True, help="slug del cliente, p.ej. envases-levante")
    parser.add_argument("peticion", nargs="?", help="petición inicial (opcional)")
    args = parser.parse_args()

    preparar_expediente(args.cliente)

    async with ClaudeSDKClient(options=opciones(args.cliente)) as cliente:
        peticion = args.peticion or input("\nTú > ")
        while peticion.strip().lower() not in {"salir", "exit", "q"}:
            await cliente.query(peticion)
            await imprimir_respuesta(cliente)
            peticion = input("\nTú > ")


if __name__ == "__main__":
    asyncio.run(main())
