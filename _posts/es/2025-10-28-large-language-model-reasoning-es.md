---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Técnicas de Razonamiento de Modelos de Lenguaje Grandes
translated: true
type: note
---

### Resumen
Denny Zhou (probablemente el "Danny Zhou" previsto) impartió una conferencia titulada "Razonamiento en Modelos de Lenguaje Grandes" como parte del curso CS25 de Stanford: Transformers United (Versión 5). En ella, ofrece una visión general completa del razonamiento en los grandes modelos de lenguaje (LLMs), haciendo hincapié en técnicas prácticas, fundamentos teóricos y desafíos en curso. A continuación se presenta un resumen estructurado de sus puntos clave, extraído directamente de sus diapositivas y notas adjuntas.

### Definición de Razonamiento en LLMs
- El razonamiento en los LLMs se trata fundamentalmente de **generar tokens intermedios** (o pasos) entre el prompt de entrada y la salida final, en lugar de saltar directamente a una respuesta. Este proceso permite al modelo descomponer problemas complejos.
- No necesita imitar exactamente el razonamiento humano; el objetivo es la resolución efectiva de problemas. Por ejemplo, resolver "¿Cuáles son las dos últimas letras de 'inteligencia artificial'?" concatenando las terminaciones de las palabras paso a paso da como resultado "le", mostrando cómo los intermedios ayudan en el cálculo.
- Respaldo teórico: Para problemas resolubles por circuitos booleanos de tamaño *T*, los transformadores de tamaño constante pueden manejarlos produciendo *O(T)* tokens intermedios, evitando la necesidad de un escalado masivo del modelo.

### Motivaciones
- Los LLMs preentrenados son inherentemente capaces de razonar sin prompts especiales o fine-tuning; se desmiente el mito de que no pueden; los problemas surgen de métodos de decodificación que no logran sacar a la luz las salidas razonadas.
- Este enfoque se alinea con "La Lección Amarga": Aprovechar la computación (mediante la generación de tokens) por encima de los atajos similares a los humanos, permitiendo comportamientos emergentes similares a los humanos a través de la predicción del siguiente token.
- Enfocarse en optimizar para métricas de objetivo final como la corrección, utilizando datos generados por el modelo en lugar de anotaciones humanas costosas.

### Ideas Centrales
- **Decodificación Cadena de Pensamiento (CoT)**: Generar múltiples respuestas candidatas y seleccionar la que tenga mayor confianza en la respuesta final. Las rutas razonadas a menudo tienen mayor confianza que las conjeturas directas (por ejemplo, contar manzanas en un escenario).
- **Escalado mediante Longitud, no Profundidad**: Entrenar modelos para generar secuencias más largas (*O(T)* tokens) para problemas en serie, haciéndolos arbitrariamente potentes sin inflar el tamaño del modelo.
- **Agregación sobre Salidas Únicas**: Generar y combinar múltiples respuestas (por ejemplo, mediante voto mayoritario) supera a las salidas únicas; la recuperación de problemas similares + razonamiento supera al razonamiento solo.
- Ejemplo: El "modo pensamiento" de Gemini 2.0 resuelve acertijos como formar 2025 con los números del 1 al 10 priorizando operaciones (por ejemplo, 45 × 45 = 2025).

### Técnicas Clave
- **Prompting**: Usar ejemplos few-shot o frases como "Pensemos paso a paso" para obtener intermedios (por ejemplo, para problemas de matemáticas con texto). Zero-shot funciona pero es menos confiable.
- **Fine-Tuning Supervisado (SFT)**: Entrenar con soluciones paso a paso anotadas por humanos para aumentar la probabilidad de rutas razonadas.
- **Auto-Mejora**: Generar tus propios datos de entrenamiento filtrando soluciones razonadas correctas de las salidas del modelo.
- **Fine-Tuning con RL (ReFT)**: Recompensar iterativamente las respuestas completas correctas (razonamiento + respuesta) y penalizar las incorrectas, usando un verificador. Esto generaliza mejor para tareas verificables; crédito a miembros del equipo como Jonathan Lai.
- **Auto-Consistencia**: Muestrear múltiples rutas, luego agregar (por ejemplo, la respuesta más frecuente). La variante universal para tareas de respuesta abierta permite que el modelo se auto-seleccione.
- **Recuperación + Razonamiento**: Incorporar ejemplos relacionados para impulsar el proceso (por ejemplo, recordar fórmulas de distancia para consultas de área).
- **Otros Potenciadores**: "Da un Paso Atrás" para la abstracción; marginalización para corregir sesgos de decodificación probabilística.

### Limitaciones
- **Prompting**: Simple pero frágil—necesita ejemplos específicos de la tarea; los prompts genéricos tienen un rendimiento inferior.
- **SFT**: No generaliza bien a problemas fuera de distribución (por ejemplo, falla en un nuevo conteo de letras de "fresa" a pesar del entrenamiento).
- **RL**: Depende de verificadores confiables, que no están disponibles para todas las tareas (por ejemplo, escritura creativa).
- **Desafíos Generales**: Los LLMs son predictores probabilísticos, por lo que la decodificación greedy favorece respuestas fluidas pero incorrectas. La agregación ayuda pero no resuelve los dominios no verificables.
- Desalineación de la decodificación: Incluso los modelos fuertes pueden no clasificar más alto las salidas razonadas sin intervención.

### Direcciones Futuras
- Ir más allá de los benchmarks hacia aplicaciones del mundo real, especialmente tareas no verificables (por ejemplo, optimización de traducción sin métricas perfectas).
- Escalar la agregación y la recuperación para obtener mayores ganancias.
- Mejorar la decodificación (por ejemplo, mediante marginalización) para alinear mejor las salidas probabilísticas con la corrección.
- Construir hacia sistemas que "recuerden" rutas de razonamiento exitosas entre sesiones.

Esta conferencia destaca el fine-tuning con RL como la potencia actual, con un cambio hacia ver el razonamiento como un problema de generación escalable.

### Referencias
- [Diapositivas sobre Razonamiento en LLMs (PDF)](https://dennyzhou.github.io/LLM-Reasoning-Stanford-CS-25.pdf)
- [Publicación de Denny Zhou en X con Puntos Clave](https://x.com/denny_zhou/status/1948499173986201915)
- [Vídeo de la Conferencia en YouTube](https://www.youtube.com/watch?v=ebnX5Ur1hBk)
- [Página del Curso CS25](https://web.stanford.edu/class/cs25/)