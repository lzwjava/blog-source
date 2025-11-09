---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Comparación de Características de SLOs-Serve frente a vLLM
translated: true
type: note
---

### Comparación: SLOs-Serve vs. vLLM

SLOs-Serve extiende vLLM integrándolo como el motor central de procesamiento por lotes mientras añade capas para garantías multi-SLO (Service Level Objective), haciéndolo más adecuado para entornos de producción con cargas de trabajo diversas y sensibles a la latencia. vLLM se centra principalmente en la inferencia de alto rendimiento para escenarios de SLO único o de maximización de throughput, utilizando técnicas como PagedAttention para la eficiencia de memoria. A continuación se presenta una comparación estructurada basada en aspectos clave del artículo de SLOs-Serve y del diseño de vLLM.

| Aspecto                  | SLOs-Serve                                                                 | vLLM                                                                 |
|-------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------|
| **Enfoque Principal**      | Servicio multi-SLO para aplicaciones de LLM multi-etapa (ej., TTFT estricto para prefill en razonamiento, TPOT estricto para decode en programación). Maneja cargas de trabajo mixtas y con ráfagas con garantías específicas por etapa. | Procesamiento por lotes de alto throughput para decodificación continua, optimizado para cargas de trabajo limitadas por memoria mediante PagedAttention. Asume SLOs uniformes o prioriza el throughput agregado. |
| **Manejo de SLOs**       | Soporte explícito multi-SLO: SLOs por etapa (prefill/decode) y por aplicación (ej., 50ms TPOT para programación vs. 100ms para chat). Utiliza control de admisión suave para rechazar/diferir solicitudes que violen los SLOs. | Sin soporte nativo multi-SLO; depende de configuraciones estáticas (ej., tamaño máximo de lote). Las violaciones de SLO son comunes bajo contención (ej., picos de latencia >2x en ráfagas). |
| **Planificador**          | Basado en programación dinámica (DP): Optimiza los presupuestos de prefill, los tamaños de lote y las longitudes de especulación por nivel de SLO. Predice el tiempo de ejecución con un modelo Roofline (precisión R² > 0.8). | Planificador de procesamiento por lotes continuo: Empaqueta solicitudes de forma greedy en lotes dinámicos, centrándose en cargas de trabajo con decodificación intensiva. Sin planificación consciente de los SLOs. |
| **Optimización de Prefill**| Prefill fragmentado con especulación adaptativa (1-10 tokens por SLO). Asigna un "presupuesto de prefill" para equilibrarlo con la decodificación. | Prefill único por solicitud; soporta prefill fragmentado pero sin adaptación a SLOs. Propenso a bloqueos head-of-line en cargas mixtas. |
| **Optimización de Decodificación**| Tamaño de lote adaptable a SLOs (hasta 512+ tokens) y decodificación especulativa adaptada a objetivos de TPOT. | Decodificación continua eficiente con procesamiento por lotes con anticipación; alto throughput (ej., 10-20x sobre Hugging Face) pero ignora los deadlines por solicitud. |
| **Gestión de Recursos**| Enrutamiento multi-réplica mediante Ray; resistencia a ráfagas con colas de mejor esfuerzo y preempción. Maneja configuraciones desagregadas. | Nodo único o distribución básica (mediante integración con Ray); sin enrutamiento proactivo o asignación priorizada por SLOs. |
| **Rendimiento y Capacidad**| Ganancia de capacidad promedio de 2.2× sobre vLLM (media geométrica en 6 escenarios: chatbot, programación, etc.). Ej., 2.4× en ráfagas de razonamiento. Escalado superlineal con réplicas. | Línea base para el throughput: Hasta 24x más rápido que las alternativas en trazas con decodificación intensiva, pero se degrada bajo restricciones de SLO (ej., pérdida del 50% de capacidad en cargas de trabajo mixtas). |
| **Sobrecarga**           | <10ms por planificación; mínima debido a la eficiencia de la PD (estados O(n)).             | Baja (<1ms por lotes); pero carece de lógica de SLOs, por lo que no añade sobrecarga adicional.      |
| **Casos de Uso**          | Aplicaciones de producción con SLAs estrictos: Agentes que llaman a herramientas, cadenas de razonamiento, tráfico con ráfagas (ej., trazas de Azure). | Throughput para investigación/desarrollo: Servicio simple, generación de contexto largo, cargas uniformes. |
| **Limitaciones**        | Asume SLOs/deadlines conocidos; se necesitan extensiones futuras para longitudes desconocidas. Construido sobre vLLM, por lo que hereda sus fortalezas en decodificación. | Dificultades con SLOs multi-etapa/variables; altas latencias en la cola en configuraciones de GPU compartidas (p99 >2x el objetivo en evaluaciones). |
| **Implementación**     | Prototipo de código abierto sobre vLLM + Ray; soporta modelos OPT/ToolLlama en GPUs A100/H100. | Código abierto maduro (GitHub); ampliamente adoptado, soporta 100+ modelos, despliegue fácil. |

En resumen, vLLM sobresale en eficiencia bruta para el servicio orientado al throughput pero se queda corto en el cumplimiento de SLOs en escenarios complejos del mundo real, lo que conduce a las ganancias de 2x+ en SLOs-Serve mediante optimizaciones específicas. Si su carga de trabajo es puramente de maximización de throughput sin garantías de latencia, vLLM sigue siendo más simple y rápido de desplegar.

[SLOs-Serve: Optimized Serving of Multi-SLO LLMs](https://arxiv.org/abs/2504.08784)  
[vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180)