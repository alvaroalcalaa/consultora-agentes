"""Herramientas del agente sobre el vault de Obsidian.

Las docstrings importan: Ollama las convierte en la descripción de cada
herramienta que ve el modelo.
"""
import json
import re
from datetime import datetime
from pathlib import Path

import numpy as np
import ollama

from config import CARPETA_ESCRIBIBLE, INDICE, MODELO_EMBED, VAULT

_indice: dict | None = None


# ---------- utilidades internas ----------

def _ruta_segura(ruta: str) -> Path:
    """Convierte una ruta relativa del vault en absoluta, sin dejar salir del vault."""
    ruta = ruta.strip().strip("[]").lstrip("/")
    if not ruta.endswith(".md"):
        ruta += ".md"
    p = (VAULT / ruta).resolve()
    if not p.is_relative_to(VAULT):
        raise ValueError("Ruta fuera del vault.")
    return p


def _trozos(texto: str, max_chars: int = 1200) -> list[str]:
    """Parte una nota en fragmentos por párrafos."""
    partes, actual = [], ""
    for parrafo in re.split(r"\n\s*\n", texto):
        if actual and len(actual) + len(parrafo) > max_chars:
            partes.append(actual.strip())
            actual = ""
        actual += parrafo + "\n\n"
    if actual.strip():
        partes.append(actual.strip())
    return partes


def actualizar_indice() -> dict:
    """(Re)indexa solo las notas nuevas o modificadas."""
    global _indice
    if _indice is None:
        _indice = json.loads(INDICE.read_text(encoding="utf-8")) if INDICE.exists() else {}

    vistos, cambios = set(), False
    for f in VAULT.rglob("*.md"):
        rel = f.relative_to(VAULT).as_posix()
        if rel.startswith((".", "agentes/")):  # ni .obsidian ni los prompts de agentes
            continue
        vistos.add(rel)
        mtime = f.stat().st_mtime
        if rel in _indice and _indice[rel]["mtime"] == mtime:
            continue
        trozos = _trozos(f.read_text(encoding="utf-8"))
        if not trozos:
            continue
        embs = ollama.embed(
            model=MODELO_EMBED, input=[f"search_document: {t}" for t in trozos]
        ).embeddings
        _indice[rel] = {"mtime": mtime, "trozos": trozos, "embs": embs}
        cambios = True

    for rel in set(_indice) - vistos:  # notas borradas
        del _indice[rel]
        cambios = True

    if cambios:
        INDICE.write_text(json.dumps(_indice), encoding="utf-8")
    return _indice


# ---------- herramientas que ve el modelo ----------

def buscar_notas(consulta: str, carpeta: str = "", n: int = 5) -> str:
    """Búsqueda semántica en el vault. Devuelve los fragmentos más relevantes y la nota de origen.

    Args:
        consulta: Qué quieres encontrar, en lenguaje natural.
        carpeta: Opcional. Limita la búsqueda a una carpeta, p. ej. "clientes/ceramicas-levante" o "metodologias".
        n: Número de resultados (por defecto 5).
    """
    indice = actualizar_indice()
    q = np.array(ollama.embed(model=MODELO_EMBED, input=f"search_query: {consulta}").embeddings[0])
    prefijo = carpeta.strip("/ ") + "/" if carpeta.strip("/ ") else ""

    resultados = []
    for rel, d in indice.items():
        if prefijo and not rel.startswith(prefijo):
            continue
        m = np.array(d["embs"])
        sims = m @ q / (np.linalg.norm(m, axis=1) * np.linalg.norm(q) + 1e-9)
        resultados += [(float(s), rel, t) for t, s in zip(d["trozos"], sims)]

    if not resultados:
        return "Sin resultados."
    resultados.sort(key=lambda r: r[0], reverse=True)
    return "\n\n---\n\n".join(
        f"Fuente: [[{rel[:-3]}]] (relevancia {s:.2f})\n{t}"
        for s, rel, t in resultados[: int(n)]
    )


def leer_nota(ruta: str) -> str:
    """Lee una nota completa del vault.

    Args:
        ruta: Ruta relativa al vault, p. ej. "clientes/ceramicas-levante/contexto" o "plantillas/diagnostico-estrategico".
    """
    p = _ruta_segura(ruta)
    if not p.exists():
        return f"No existe la nota '{ruta}'. Usa listar_cliente o buscar_notas para encontrarla."
    return p.read_text(encoding="utf-8")


def listar_cliente(cliente: str) -> str:
    """Lista todas las notas de un cliente (contexto, reuniones, entregables).

    Args:
        cliente: Nombre de la carpeta del cliente dentro de clientes/, p. ej. "ceramicas-levante".
    """
    carpeta = (VAULT / "clientes" / cliente.strip("/ ")).resolve()
    if not carpeta.is_relative_to(VAULT) or not carpeta.exists():
        disponibles = sorted(d.name for d in (VAULT / "clientes").iterdir() if d.is_dir())
        return f"No existe el cliente '{cliente}'. Clientes disponibles: {', '.join(disponibles)}"
    notas = sorted(f.relative_to(VAULT).as_posix()[:-3] for f in carpeta.rglob("*.md"))
    return "\n".join(notas) or "El cliente no tiene notas."


def escribir_nota(ruta: str, contenido: str, area: str = "estrategia") -> str:
    """Guarda un entregable como nota nueva en la carpeta del cliente. Nunca sobrescribe notas existentes.

    Args:
        ruta: Ruta relativa dentro de clientes/, p. ej. "clientes/ceramicas-levante/entregables/diagnostico-estrategico".
        contenido: Texto completo en markdown. Usa [[enlaces]] a las notas en las que te basas.
        area: Área consultora que genera la nota.
    """
    p = _ruta_segura(ruta)
    if not p.is_relative_to((VAULT / CARPETA_ESCRIBIBLE).resolve()):
        return f"ERROR: solo puedes escribir dentro de '{CARPETA_ESCRIBIBLE}/'."
    if p.exists():  # nunca pisar trabajo previo: se versiona
        p = p.with_name(f"{p.stem} {datetime.now():%Y%m%d-%H%M}.md")

    if not contenido.lstrip().startswith("---"):
        cliente = p.relative_to(VAULT).parts[1] if len(p.relative_to(VAULT).parts) > 2 else ""
        contenido = (
            "---\n"
            f"cliente: {cliente}\n"
            f"area: {area}\n"
            f"fecha: {datetime.now():%Y-%m-%d}\n"
            "estado: borrador\n"
            "generado_por: agente\n"
            "---\n\n" + contenido
        )
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(contenido, encoding="utf-8")
    return f"Nota guardada en [[{p.relative_to(VAULT).as_posix()[:-3]}]]"


HERRAMIENTAS = [buscar_notas, leer_nota, listar_cliente, escribir_nota]
FUNCIONES = {f.__name__: f for f in HERRAMIENTAS}
