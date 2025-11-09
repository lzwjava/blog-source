---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Optimización del Servicio de LLM con Múltiples SLO
translated: true
type: note
---

### Resumen
El artículo "SLOs-Serve: Optimized Serving of Multi-SLO LLMs" presenta SLOs-Serve, un sistema diseñado para servir eficientemente modelos de lenguaje grandes (LLMs) en aplicaciones multi-etapa donde cada etapa (por ejemplo, prefill para el procesamiento de entrada, decode para la generación de tokens) y cada aplicación (por ejemplo, chatbots, asistentes de codificación) tiene objetivos de nivel de servicio (SLOs) específicos. Estos SLOs garantizan una baja latencia para los aspectos orientados al usuario, como el tiempo hasta el primer token (TTFT) para el prefill y los tokens por tiempo de salida (TPOT) para el decode. Los sistemas de servicio tradicionales como vLLM o Sarathi-Serve priorizan el rendimiento pero a menudo violan estos SLOs granulares bajo recursos compartidos, especialmente durante ráfagas o cargas de trabajo mixtas.

### Desafíos Clave y Contribuciones
Los autores identifican desafíos en el servicio multi-SLO:
- **Solicitudes multi-etapa**: Aplicaciones como LLMs de razonamiento (SLOs estrictos durante las etapas de "pensamiento") o agentes que llaman a herramientas (bucles con prefill/decode estrictos) requieren garantías específicas por etapa.
- **Contención de recursos**: Las GPUs compartidas conducen a violaciones de SLO en configuraciones co-localizadas o desagregadas.
- **Tráfico en ráfagas**: Los picos repentinos saturan los planificadores.

Las contribuciones de SLOs-Serve incluyen:
- Un planificador basado en programación dinámica (DP) que optimiza las asignaciones de tokens (presupuesto de prefill, tamaños de lote) para cumplir con los SLOs mientras maximiza el rendimiento.
- Soporte para prefill en fragmentos, decodificación especulativa adaptativa a SLOs (personalizando longitudes de especulación por nivel de SLO) y control de admisión flexible (garantizando SLOs para las solicitudes admitidas, posponiendo otras).
- Una arquitectura distribuida con enrutamiento multi-réplica y resistencia a ráfagas, construida sobre vLLM para el procesamiento por lotes y Ray para la orquestación.

| Aplicación | SLO de Prefill | SLO de Decode | Ejemplo |
|-------------|-------------|------------|---------|
| Resumen | Estricto (ej., 3x ralentización máx.) | Flexible (100ms TPOT) | Procesamiento de documentos |
| Codificación | Flexible | Estricto (50ms TPOT) | Generación de código |
| Chatbot | Flexible | Flexible | Consultas interactivas |
| Llamada a herramientas | Estricto (bucles) | Estricto (bucles), flexible (final) | Flujos de trabajo de agentes |
| Razonamiento | Estricto (pensamiento) | Estricto (pensamiento), flexible (respuesta) | Cadena de pensamiento |

### Diseño del Sistema
- **Planificador (Algoritmo 1)**: Utiliza DP para admitir solicitudes y planificar lotes, modelando el tiempo de ejecución mediante un predictor inspirado en Roofline (precisión R² > 0.8). Los estados rastrean la memoria, el presupuesto de prefill y las solicitudes aceptadas; las transiciones priorizan los plazos más tempranos y el cumplimiento de los SLOs.
- **Formación de Lotes**: Tamaño dinámico (hasta 512+ tokens) basado en el TPOT más estricto, permitiendo lotes más grandes para un mayor rendimiento sin violaciones de SLO.
- **Decodificación Especulativa**: Adapta las longitudes de especulación (ej., 1-10 tokens) por nivel de SLO para aumentar el presupuesto de prefill, resolviendo mediante enumeración para un equilibrio óptimo entre prefill y decode.
- **Múltiples Réplicas y Ráfagas**: Un controlador centralizado enruta las solicitudes de forma proactiva; las solicitudes inalcanzables van a una cola de mejor esfuerzo, se preemptan si es necesario.

El diseño explora compensaciones, como lotes más grandes que aumentan el rendimiento pero arriesgan la latencia (visualizado en figuras que muestran regiones factibles para SLOs).

### Evaluación
Probado en 6 escenarios (chatbot, codificación, resumen, mixto, llamada a herramientas, razonamiento) utilizando trazas reales (cargas de trabajo de Azure LLM) y conjuntos de datos (ShareGPT, HumanEval, etc.). Modelos: OPT-7B/13B/30B, ToolLlama-7B. Hardware: 4×A100 GPUs (principal), hasta 8×H100.

- **Ganancias de Capacidad**: Mejora promedio de 2.2× sobre vLLM/Sarathi-Serve/DistServe (media geométrica entre escenarios). Por ej., 2.4× en razonamiento, 2.1× en codificación con ráfagas.
- **Escalado**: Super-lineal con réplicas (hasta 6.2× en llamada a herramientas bajo ráfagas) mediante enrutamiento.
- **Ablaciones**: La especulación añade 1.66×, el enrutamiento 1.19×, el manejo de ráfagas 1.34×.
- Sobrecarga: <10ms por invocación de planificación.

Las figuras muestran que SLOs-Serve mantiene las latencias p99 cerca de los objetivos durante los picos, mientras que los sistemas de referencia se degradan.

### Conclusiones
SLOs-Serve avanza en el servicio de LLMs al garantizar múltiples SLOs en entornos diversos y con ráfagas, desbloqueando ganancias de eficiencia superiores a 2x. Trabajos futuros podrían extenderse a longitudes de decode desconocidas o más etapas. El sistema demuestra que la planificación personalizada para SLOs es clave para las implementaciones de LLMs de grado de producción.

[SLOs-Serve: Optimized Serving of Multi-SLO LLMs](https://arxiv.org/abs/2504.08784)