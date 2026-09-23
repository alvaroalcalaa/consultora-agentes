# Criterios de calidad comunes

Se aplican a todos los entregables, de cualquier área. Cada skill puede añadir criterios propios.

| Criterio | 1 (mal) | 3 (aceptable) | 5 (excelente) |
|---|---|---|---|
| Rigor de fuentes | Cifras sin fuente o inventadas (**eliminatorio**) | Casi todo con fuente, algún supuesto sin marcar | Todo con fuente y año; supuestos marcados y razonados |
| Estructura | Desordenado, se repite | Ordenado pero la conclusión llega tarde | Conclusión primero, sin solapamientos |
| Accionabilidad | Recomendaciones de manual | Acciones concretas sin plazo ni indicador | Qué, quién, cuándo y cómo se mide |
| Adaptación al cliente | Valdría para cualquier empresa | Adaptado al sector | Adaptado a esta empresa, su tamaño y su momento |
| Presentación | Errores, formato pobre | Correcto | Listo para un comité de dirección |

**Umbral para enviar al cliente:** ninguna puntuación por debajo de 3, media ≥ 4, y aprobación del consultor humano.

## Cómo usar las evals
1. Cada skill tiene su fichero en `evals/<skill>.json` con casos de prueba.
2. Ejecuta cada caso con `python main.py --cliente demo "<prompt del caso>"`.
3. Puntúa el resultado con esta tabla y anota fallos en `evals/resultados.md`.
4. Ajusta la skill o el subagente y repite. Guarda la versión que funciona.
