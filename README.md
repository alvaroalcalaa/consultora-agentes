# Consultora de agentes — repo base

Consultoría de negocio donde el trabajo lo hacen agentes de IA especializados, coordinados por un orquestador y **supervisados por consultores humanos**.

## Arquitectura

```
                  Director de Proyecto (orquestador) — CLAUDE.md
                                   │
   ┌────────────┬─────────────┬────┴───────┬───────────┬────────────┐
investigador analista-datos facilitador  redactor   revisor-qa   propuestas
                                   │
   Skills de áreas (.claude/skills): Estrategia · Operaciones ·
   Cultura y Talento · Agilidad/OPEX · Tech
                                   │
   Expediente del cliente (clientes/<slug>/) — memoria del proyecto
                                   │
   Evals y criterios comunes (evals/)
```

- **Áreas = conocimiento (skills).** Añadir un área o servicio nuevo es escribir una skill, no crear otro agente.
- **Agentes = funciones.** Seis subagentes transversales que sirven a todas las áreas.
- **Expediente = memoria.** Todo lo que se hace queda en la carpeta del cliente.
- **Revisor QA independiente + aprobación humana** antes de que nada llegue al cliente.

## Estructura

```
CLAUDE.md                  Instrucciones del orquestador
main.py                    Lanzador
.claude/agents/            Subagentes funcionales
.claude/skills/            Skills por área y servicio
clientes/_plantilla/       Plantilla del expediente (los reales no se suben)
evals/                     Casos de prueba y criterios de calidad
```

## Puesta en marcha

1. Requisitos: Python 3.10+ y Node.js (el Agent SDK usa el CLI de Claude Code por debajo; revisa la documentación del SDK por si cambia).
2. Instala:
   ```bash
   npm install -g @anthropic-ai/claude-code
   pip install -r requirements.txt
   cp .env.example .env   # y pon tu ANTHROPIC_API_KEY
   ```
3. Lanza una sesión:
   ```bash
   python main.py --cliente demo "Haz un diagnóstico estratégico express de ..."
   ```

## Skills disponibles

| Área | Skill | Estado |
|---|---|---|
| Estrategia | `diagnostico-estrategico-express` | ✅ v1 |
| Estrategia | `plan-estrategico-okrs` | ⏳ pendiente |
| Estrategia | `analisis-mercado-competencia` | ⏳ pendiente |
| Operaciones | — | ⏳ |
| Cultura y Talento | — | ⏳ |
| Agilidad / OPEX | — | ⏳ |
| Tech | — | ⏳ |

## Pendiente
- [ ] `precios.md` con el catálogo de tarifas (lo usa el subagente de propuestas)
- [ ] Plantilla de marca para docx/pptx
- [ ] Observabilidad (Langfuse) para trazas y costes
- [ ] Agente de captación (LinkedIn semiautomático → CRM)
