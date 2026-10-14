"""Uso:
    python main.py "Haz un diagnóstico estratégico de ceramicas-levante a partir del kickoff"
    python main.py --area estrategia "..."
    python main.py --indexar
"""
import argparse

from agente import ejecutar
from config import MODELO, VAULT
from vault_tools import actualizar_indice


def main():
    parser = argparse.ArgumentParser(description="Agente consultor sobre un vault de Obsidian")
    parser.add_argument("tarea", nargs="?", help="Lo que quieres que haga el agente")
    parser.add_argument("--area", default="estrategia", help="Área (prompt en agentes/<area>.md)")
    parser.add_argument("--indexar", action="store_true", help="Solo (re)indexar el vault")
    args = parser.parse_args()

    if args.indexar:
        indice = actualizar_indice()
        print(f"Indexadas {len(indice)} notas de {VAULT}")
        return
    if not args.tarea:
        parser.error("Falta la tarea.")

    print(f"Agente '{args.area}' | modelo {MODELO} | vault {VAULT}\n")
    print("\n" + ejecutar(args.area, args.tarea))


if __name__ == "__main__":
    main()
