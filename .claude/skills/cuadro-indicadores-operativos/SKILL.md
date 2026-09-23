---
name: cuadro-indicadores-operativos
description: Diseña un cuadro de mando de indicadores operativos (KPIs) — selección de indicadores, definiciones, fuentes de datos, niveles de reunión (tiers) y diseño del dashboard en Power BI o Excel — y su rutina de seguimiento. Úsala siempre que se hable de KPIs, indicadores, cuadro de mando, dashboard, Power BI, OEE, seguimiento de producción, reuniones diarias de resultados o "no sabemos cómo vamos", aunque no se diga "cuadro de mando".
---

# Cuadro de Indicadores Operativos

Un cuadro de mando no es un informe bonito: es la herramienta con la que cada nivel de la organización decide qué hacer hoy. Si nadie toma decisiones con él, sobra. Pocos indicadores, bien definidos, con dueño y revisados en una rutina fija.

## Flujo

### 1. Qué decisiones hay que tomar
Antes de hablar de indicadores, entrevista (`facilitador`) a cada nivel: dirección, jefes de área, mandos de turno. Pregunta qué deciden, cada cuánto y con qué información. Los indicadores salen de las decisiones, no al revés.

### 2. Selección de indicadores
Estructura por las dimensiones clásicas: **Seguridad, Calidad, Plazo (entrega), Coste y Personas**. Por nivel:
- Dirección: 6-10 indicadores, visión mensual y tendencia.
- Área: 5-8, semanal.
- Turno o equipo: 3-5, diario, muy visuales.
Combina indicadores de resultado (OEE, cumplimiento de plazos, coste por unidad) con indicadores que se anticipan (paradas, rechazos en la primera pieza, absentismo).

### 3. Ficha de cada indicador
Nombre · qué mide y para qué decisión · fórmula exacta · fuente de datos · frecuencia · responsable · objetivo y umbrales de alerta (verde/ámbar/rojo) · qué se hace cuando está en rojo.
Sin ficha, cada área calculará el indicador a su manera y los números no cuadrarán.

### 4. Datos (delegar en `analista-datos`)
Comprueba que cada indicador se puede calcular con datos existentes y de calidad. Si hay que capturar datos nuevos, diseña la captura más simple posible (hoja de turno, lector, exportación del ERP). Calcula el valor actual de todos los indicadores: será la línea base.

### 5. Diseño del dashboard
- Power BI si el cliente ya lo usa o tiene datos en varias fuentes; Excel bien diseñado si es una pyme pequeña. No impongas herramienta.
- Una página por nivel. Lo importante arriba a la izquierda. Tendencia siempre visible, no solo el valor del día.
- Colores solo para el estado (verde/ámbar/rojo), no decorativos.
- Entrega un prototipo con datos reales y ajústalo con los usuarios.

### 6. Rutina de seguimiento (tiers)
- Tier 1: reunión de turno de 10 min delante del tablero.
- Tier 2: reunión diaria de área de 15 min.
- Tier 3: revisión semanal de dirección de 30-45 min.
Cada reunión: indicadores en rojo → causa → acción con responsable y fecha → escalar al nivel superior lo que no se puede resolver.

## Entregables
Catálogo de indicadores con fichas · mapa de fuentes de datos · prototipo del dashboard · diseño de la rutina de reuniones con agenda tipo · línea base.

## Checklist
- [ ] Cada indicador responde a una decisión concreta de un nivel concreto.
- [ ] Cada indicador tiene ficha completa y responsable.
- [ ] Todos se pueden calcular con datos disponibles, o está diseñada la captura.
- [ ] Hay rutina de reunión y regla de escalado.

## Límites
Los indicadores de equipo no se usan para evaluar a personas individuales sin revisión del consultor humano y del área de personas. El acceso a datos del ERP u otros sistemas requiere autorización expresa del cliente.
