---
name: propuesta-solucion-agentes
description: Diseña la propuesta técnica y funcional de una solución con agentes de IA o automatización para un cliente — caso de uso, alcance, arquitectura, integraciones, supervisión humana, seguridad y cumplimiento, evals, plan de piloto, costes de operación y riesgos. Úsala siempre que haya que concretar cómo se construiría un agente, un asistente, una automatización o una integración para un cliente, o preparar un piloto técnico, aunque no se diga "propuesta".
---

# Propuesta de Solución con Agentes

Va después de `diagnostico-digitalizacion`, para el caso de uso priorizado. El objetivo es una propuesta que un director de negocio entienda y un responsable de sistemas apruebe. Un agente solo es "funcional" si funciona en producción con datos reales, se puede medir, se puede supervisar y alguien sabe mantenerlo.

## Flujo

### 1. Definir el caso de uso con precisión
- Proceso actual paso a paso, volumen (casos/mes) y tiempo por caso.
- Qué hará el agente y, sobre todo, **qué no hará**.
- Qué decisiones toma el agente y cuáles una persona.
- Métrica de éxito: horas ahorradas, tiempo de respuesta, errores, satisfacción.

### 2. Elegir el tipo de solución
Usa la solución más simple que resuelva el problema:
| Si… | Entonces |
|---|---|
| Las reglas son fijas y los datos estructurados | Automatización clásica (n8n, Power Automate, scripts), sin IA |
| Hay que entender texto o documentos, pero el flujo es fijo | Flujo con pasos de IA |
| Hay que decidir pasos según el caso y usar varias herramientas | Agente |
| Hay varias tareas muy distintas con contextos grandes | Agente orquestador con subagentes |
Justifica la elección. Proponer un agente donde basta una automatización encarece y hace menos fiable la solución.

### 3. Arquitectura
- Modelo(s) y proveedor, con motivo (calidad, coste, ubicación de los datos).
- Integraciones: sistemas del cliente, preferiblemente mediante APIs o MCP, con permisos de mínimo privilegio.
- Base de conocimiento: qué documentos, cómo se actualizan y quién es responsable.
- Supervisión humana: en qué puntos aprueba una persona antes de que el agente actúe.
- Observabilidad: trazas, costes y registro de decisiones.
- Diagrama sencillo (pídelo al `redactor`).

### 4. Seguridad y cumplimiento
- Datos personales: base legal, minimización, ubicación y retención (RGPD). Si hace falta, contrato de encargo de tratamiento.
- AI Act: clasifica el caso. Si es de alto riesgo (selección de personal, evaluación de trabajadores, crédito…), escala al consultor humano antes de seguir. Si el agente interactúa con personas, estas deben saber que hablan con una IA.
- Riesgos específicos de agentes: inyección de instrucciones a través de documentos o correos, acciones no autorizadas, fuga de datos. Contramedidas para cada uno.

### 5. Evals
Conjunto de 20-50 casos reales (anonimizados) con la respuesta correcta, criterios de aceptación y umbral para pasar a producción. Sin evals no se sabe si el agente funciona.

### 6. Plan de piloto
6-10 semanas: construcción, pruebas con evals, piloto con usuarios reales en un ámbito limitado y decisión de pasar a producción con los datos del piloto.

### 7. Costes
Construcción (una vez) + operación mensual (consumo del modelo estimado por volumen, infraestructura, mantenimiento y mejora). Compara con el coste actual del proceso. Marca las estimaciones como tales.

## Entregables
Documento de propuesta (resumen para dirección + anexo técnico) · diagrama de arquitectura · plan de evals · plan de piloto con criterios de éxito · estimación de costes y retorno · registro de riesgos.

## Checklist
- [ ] Está escrito qué NO hace el agente.
- [ ] Se ha justificado por qué no basta una solución más simple.
- [ ] Supervisión humana definida en las acciones con impacto.
- [ ] Clasificación AI Act y análisis RGPD hechos.
- [ ] Hay evals y un umbral de aceptación antes de producción.
- [ ] Coste de operación mensual estimado, no solo el de construcción.

## Límites
No propongas accesos a sistemas con más permisos de los necesarios ni almacenar credenciales en texto plano. Cualquier caso de alto riesgo según el AI Act, o que automatice decisiones sobre personas, se escala al consultor humano antes de proponerse.
