---
audio: false
generated: true
lang: es
layout: post
title: DeepSeek V3
translated: true
type: note
---

### Resumen y Aspectos Destacados
1. **Nombre del Modelo**: DeepSeek-V3, un modelo de lenguaje Mixture-of-Experts (MoE) con 671 mil millones de parámetros, de los cuales 37 mil millones se activan por token.
2. **Conjunto de Datos de Entrenamiento**: Pre-entrenado con 14.8 billones de tokens diversos y de alta calidad.
3. **Innovaciones Principales**: Incorpora arquitecturas Multi-Head Latent Attention (MLA) y DeepSeekMoE con equilibrio de carga sin pérdidas auxiliares para mayor eficiencia.
4. **Eficiencia de Entrenamiento**: Logra el entrenamiento completo con solo 2.788 millones de horas de GPU H800.
5. **Eficiencia de Costos**: El costo de entrenamiento se estima en 5.576 millones de USD, asumiendo 2 USD por hora de GPU.

---

### Innovaciones Arquitectónicas
6. **Marco Basado en Transformer**: Conserva la arquitectura Transformer para escalabilidad y flexibilidad.
7. **Multi-Head Latent Attention (MLA)**: Reduce la memoria de inferencia comprimiendo las cachés clave-valor sin pérdida de rendimiento.
8. **DeepSeekMoE**: Utiliza una combinación de expertos compartidos y enrutados para un entrenamiento rentable y alta eficiencia computacional.
9. **Equilibrio de Carga Sin Pérdidas Auxiliares**: Introduce términos de sesgo para mantener cargas equilibradas en los expertos sin comprometer el rendimiento.
10. **Predicción Multi-Token (MTP)**: Predice secuencialmente múltiples tokens por posición, mejorando la eficiencia de datos y la pre-planificación de representaciones.

---

### Marco de Entrenamiento
11. **Entrenamiento en Precisión Mixta FP8**: Aprovecha la cuantización de grano fino y el almacenamiento de baja precisión para optimizar memoria y computación.
12. **Algoritmo DualPipe**: Superpone las fases de computación y comunicación, reduciendo burbujas en el pipeline y mejorando el paralelismo.
13. **Comunicación Eficiente entre Nodos**: Emplea kernels optimizados para operaciones all-to-all, utilizando los anchos de banda de NVLink e InfiniBand.
14. **Estados del Optimizador en Baja Precisión**: Almacena los estados del optimizador en BF16, reduciendo el consumo de memoria sin pérdida de rendimiento.
15. **Técnicas de Optimización de Memoria**: Recalcula ciertas operaciones (ej., RMSNorm) durante la retropropagación para ahorrar memoria.

---

### Detalles del Pre-entrenamiento
16. **Proceso de Entrenamiento Estable**: No ocurrieron picos de pérdida irrecuperables ni reversiones durante el pre-entrenamiento.
17. **Extensión de Longitud de Contexto**: La longitud de contexto se extendió a 32K y posteriormente a 128K en dos etapas.
18. **Costos de Entrenamiento**: El pre-entrenamiento requirió 2.664M de horas de GPU, la extensión de contexto 119K horas de GPU y el post-entrenamiento 5K horas de GPU.
19. **Eficiencia de Tokens**: La eficiencia del entrenamiento asegurada minimizando las horas de GPU por billón de tokens.
20. **Datos de Alta Calidad**: Conjunto de datos de pre-entrenamiento curado para diversidad y relevancia.

---

### Mejoras Post-entrenamiento
21. **Ajuste Fino Supervisado (SFT)**: Alinea las salidas del modelo con las preferencias humanas.
22. **Aprendizaje por Refuerzo (RL)**: Emplea Group Relative Policy Optimization para el ajuste fino.
23. **Distilación de Conocimiento**: Integra capacidades de razonamiento de los modelos DeepSeek-R1.
24. **Control del Estilo de Salida**: Equilibra la precisión con la longitud y el estilo de generación.
25. **Refinamiento del Rendimiento**: El post-entrenamiento mejora aún más los resultados en benchmarks.

---

### Rendimiento en Benchmarks
26. **MMLU (Benchmarks Educativos)**: Logra 88.5, superando a otros modelos de código abierto.
27. **GPQA (Conocimiento General)**: Obtiene 59.1, comparable a GPT-4o y Claude-3.5-Sonnet.
28. **Benchmarks de Matemáticas**: Rendimiento state-of-the-art en tareas de razonamiento matemático.
29. **Competiciones de Código**: Sobresale en benchmarks de codificación como LiveCodeBench.
30. **Conocimiento Factual**: Demuestra resultados superiores en benchmarks de factualidad en inglés y chino.

---

### Inferencia y Despliegue
31. **Etapa de Prellenado**: Combina paralelismo de tensores (TP4), paralelismo de secuencias (SP) y paralelismo de expertos (EP32) para eficiencia.
32. **Etapa de Decodificación**: Utiliza EP320 con IBGDA para comunicación de baja latencia.
33. **Redundancia Dinámica**: Ajusta dinámicamente las cargas de los expertos para optimizar la utilización de recursos.
34. **Separación de Etapas**: Las etapas de prellenado y decodificación se separan para mejorar el throughput.
35. **Utilización de Hardware**: Optimizado para GPUs H800 con interconexiones NVLink e InfiniBand.

---

### Innovaciones en Equilibrio de Carga y Decodificación
36. **Enrutamiento Basado en Sesgo**: Introduce términos de sesgo para garantizar cargas equilibradas en los expertos de forma dinámica.
37. **Decodificación Especulativa**: Mejora la latencia de generación utilizando módulos MTP.
38. **Expertos Redundantes**: Duplica expertos de alta carga para equilibrar las cargas de trabajo de las GPU.
39. **Enrutamiento Limitado por Nodo**: Restringe el enrutamiento de tokens a un máximo de 4 nodos para reducir la sobrecarga de comunicación.
40. **Sin Eliminación de Tokens**: Garantiza que todos los tokens se conserven durante el entrenamiento y la inferencia.

---

### Detalles Técnicos
41. **Configuración del Clúster**: Entrenado en un clúster con 2048 GPUs NVIDIA H800.
42. **Paralelismo de Pipeline**: Emplea un esquema de paralelismo de 16 vías para escalabilidad.
43. **Huella de Memoria**: Evita el costoso paralelismo de tensores optimizando el uso de memoria.
44. **Kernels Personalizados**: Desarrolla kernels de comunicación especializados para manejar operaciones entre nodos de manera eficiente.
45. **Optimización de Precisión Mixta**: Combina formatos FP8 y BF16 para una dinámica de entrenamiento óptima.

---

### Evaluación y Resultados
46. **Benchmarks Integrales**: Evaluado en diversos dominios, incluyendo educación, codificación y razonamiento.
47. **Liderazgo en Código Abierto**: Se erige como el modelo base de código abierto más fuerte en su categoría.
48. **Comparación con Modelos de Código Cerrado**: Rendimiento comparable a GPT-4o y Claude-3.5-Sonnet.
49. **Fortaleza en Conocimiento Chino**: Supera a los modelos líderes en benchmarks de factualidad en chino.
50. **Manejo de Contexto Largo**: Sobresale en tareas que requieren procesamiento de contexto extendido.

---

### Direcciones Futuras
51. **Exploración de Redundancia Dinámica**: Investigando estrategias de redundancia más adaptativas.
52. **Expansión de la Decodificación Especulativa**: Explorando más usos de MTP para la aceleración de la inferencia.
53. **Co-diseño de Hardware**: Adaptándose a las GPUs de próxima generación para un rendimiento mejorado.
54. **Cobertura Más Amplia de Benchmarks**: Expandiendo las evaluaciones a tareas más diversas.
55. **Sostenibilidad**: Reduciendo aún más los costos de entrenamiento mediante optimizaciones algorítmicas y de hardware.

---

Este documento proporciona un resumen integral de DeepSeek-V3, encapsulando su arquitectura, metodologías de entrenamiento, rendimiento en benchmarks y perspectivas futuras. ¡Avísame si necesitas más detalles sobre secciones específicas o puntos adicionales!