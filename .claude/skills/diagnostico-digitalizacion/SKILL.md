---
name: diagnostico-digitalizacion
description: Realiza un diagnóstico de digitalización y oportunidades de IA/automatización — inventario de sistemas, flujos de datos, procesos manuales, madurez digital y casos de uso priorizados con propuesta de solución (agentes, automatizaciones, integraciones). Úsala siempre que se hable de digitalizar, automatizar, implantar IA o agentes, integrar sistemas, "qué podemos automatizar", ERP/CRM o transformación digital.
---

# Diagnóstico de Digitalización e IA

Es la puerta de entrada del Hub Tech. El error típico del sector es empezar por la tecnología ("pongamos un chatbot"). Aquí se empieza por el proceso y el problema de negocio, y la tecnología llega al final. Un buen diagnóstico descarta casos de uso tanto como propone.

## Flujo

### 1. Inventario de sistemas
Qué herramientas usan (ERP, CRM, Excel, correo, gestor documental, herramientas sectoriales), quién las usa, cómo se conectan entre sí y dónde viven los datos importantes. Dibuja un mapa de sistemas simple.

### 2. Procesos manuales y fricciones (`facilitador`)
Entrevistas por área: qué tareas repetitivas hacen, cuánto tiempo les llevan, dónde se copian datos a mano entre sistemas, qué errores se repiten. Estima horas/mes por tarea con los propios usuarios.

### 3. Madurez digital
Puntúa de 1 a 5 con evidencia: sistemas, calidad e integración de datos, procesos digitalizados, competencias digitales del equipo, ciberseguridad básica (copias de seguridad, accesos, doble factor, formación) y gobierno de la tecnología.

### 4. Casos de uso
Para cada oportunidad:
- Problema y proceso afectado.
- Solución propuesta y tipo: automatización simple (n8n, Power Automate), integración entre sistemas, agente de IA, analítica/dashboard, o cambio de sistema.
- **Beneficio**: horas ahorradas/mes, errores evitados o ingresos, marcado como estimación.
- **Esfuerzo y coste** orientativo, y **riesgo** (datos personales, errores con impacto en cliente, dependencia de un proveedor).
- **Viabilidad de datos**: ¿los datos necesarios existen y son de calidad?

Prioriza en matriz valor/esfuerzo. Recomienda empezar por 1-2 casos de alto valor, bajo riesgo y datos disponibles.

### 5. Propuesta de piloto
Para el caso prioritario: alcance, arquitectura a alto nivel, integraciones, supervisión humana, métricas de éxito, plazo y siguiente fase si funciona.

## Estructura del entregable
1. Resumen ejecutivo: madurez, top 3 casos de uso y piloto propuesto.
2. Mapa de sistemas y datos.
3. Procesos manuales y coste en horas.
4. Madurez digital por dimensión.
5. Casos de uso priorizados (matriz y fichas).
6. Propuesta de piloto.
7. Riesgos, ciberseguridad y cumplimiento (RGPD, AI Act).

## Checklist
- [ ] Cada caso de uso parte de un problema real con horas o coste estimado por los usuarios.
- [ ] Se han descartado casos explícitamente, con motivo.
- [ ] El piloto tiene métricas de éxito y supervisión humana definida.
- [ ] Se revisa si algún caso cae en IA de alto riesgo según el AI Act (por ejemplo, selección de personal) o trata datos personales.

## Límites
No accedas a sistemas del cliente sin autorización expresa y credenciales de mínimo privilegio. Si detectas vulnerabilidades graves de seguridad, informa al consultor humano de inmediato en vez de detallarlas en un entregable general.
