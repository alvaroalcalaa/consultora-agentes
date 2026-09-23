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
| Estrategia | `plan-estrategico-okrs` (incluye seguimiento mensual) | ✅ v1 |
| Estrategia | `analisis-mercado-competencia` | ✅ v1 |
| Operaciones | `diagnostico-procesos-operaciones` | ✅ v1 |
| Operaciones | `plan-mejora-lean` | ✅ v1 |
| Operaciones | `cuadro-indicadores-operativos` | ✅ v1 |
| Cultura y Talento | `diagnostico-clima-cultura` | ✅ v1 |
| Cultura y Talento | `diseno-dinamicas-talleres` | ✅ v1 |
| Cultura y Talento | `plan-onboarding-desarrollo` | ✅ v1 |
| Agilidad / OPEX | `evaluacion-madurez-agil` | ✅ v1 |
| Agilidad / OPEX | `sistema-mejora-continua` (incluye servicio mensual) | ✅ v1 |
| Agilidad / OPEX | `plan-transformacion-agil` | ✅ v1 |
| Tech | `diagnostico-digitalizacion` | ✅ v1 |
| Tech | `propuesta-solucion-agentes` | ✅ v1 |

Todas las skills v1 están sin probar con casos reales: pásalas por sus evals (`evals/<skill>.json`) antes de usarlas con clientes.

## Automatizaciones (GitHub Actions)

| Automatización | Cuándo | Qué deja |
|---|---|---|
| `linkedin-diario.yml` | Lunes a viernes, 8:00 | Pull Request con un borrador de post en `contenido/linkedin/` |
| `skill-semanal.yml` | Lunes, 7:00 | Pull Request con una skill pendiente o, si no hay, una mejora de una skill existente |

Nada se publica sin tu revisión: aceptas (Merge) o descartas (Close) cada Pull Request.
Se pueden lanzar a mano desde la pestaña **Actions → Run workflow**.

## Pendiente
- [ ] `precios.md` con el catálogo de tarifas (lo usa el subagente de propuestas)
- [ ] Plantilla de marca para docx/pptx
- [ ] Observabilidad (Langfuse) para trazas y costes
- [ ] Agente de captación (LinkedIn semiautomático → CRM)
