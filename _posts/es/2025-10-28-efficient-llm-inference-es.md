---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Inferencia Eficiente de LLM con vLLM
translated: true
type: note
---

### vLLM: Inferencia y Servicio Eficiente de LLM

vLLM es una biblioteca de código abierto diseñada para la inferencia y el servicio rápido y eficiente en memoria de modelos de lenguaje grandes (LLM). Desarrollada inicialmente en el Sky Computing Lab de UC Berkeley, ahora es un proyecto impulsado por la comunidad y ampliamente utilizado en producción para implementar LLM como Llama o variantes de GPT. Su innovación central es **PagedAttention**, una técnica que trata la memoria caché de clave-valor (KV) como páginas de memoria virtual, reduciendo el desperdicio y permitiendo un mayor rendimiento mediante la asignación dinámica de bloques no contiguos.

#### Cómo Funciona
- **Continuous Batching**: A diferencia de los sistemas tradicionales que esperan por lotes completos, vLLM añade y elimina solicitudes dinámicamente durante la ejecución, minimizando el tiempo de inactividad de la GPU durante la decodificación.
- **Gestión de Memoria**: PagedAttention evita la fragmentación en la caché KV (que crece con la longitud de la secuencia), soportando contextos más largos sin errores de falta de memoria (OOM).
- **Ejecución Optimizada**: Utiliza grafos CUDA/HIP para lanzamientos de kernel más rápidos, integrado con FlashAttention/FlashInfer para el cálculo de atención, y soporta cuantización (por ejemplo, AWQ, GPTQ, FP8) para reducir el uso de memoria hasta en 4x.
- **Características Avanzadas**: Incluye decodificación especulativa (para adivinar tokens y verificar), prefill en fragmentos (para entradas largas), multi-LoRA (adaptando modelos sobre la marcha) y paralelismo distribuido (tensor, pipeline, experto).

vLLM expone un servidor API compatible con OpenAI, se integra perfectamente con modelos de Hugging Face y se ejecuta en hardware diverso (GPUs de NVIDIA/AMD/Intel, TPUs, CPUs). Es ideal para escenarios de alto rendimiento, logrando aceleraciones de 2-10x sobre líneas base como Hugging Face Transformers en benchmarks de servicio.

#### Casos de Uso Clave
- Servicio online para chatbots o APIs con salidas en streaming (streaming outputs).
- Inferencia por lotes offline para tareas como resumen.
- Escalado a clústeres multi-GPU sin necesidad de infraestructura personalizada.

### Ray: Framework Unificado para Escalar Aplicaciones de IA y Python

Ray es un framework de computación distribuida de código abierto que facilita escalar código Python—especialmente cargas de trabajo de IA/ML—desde una sola máquina a clústeres masivos. Creado por Anyscale (con raíces en UC Berkeley), abstrae las complejidades de los sistemas distribuidos como la planificación, la tolerancia a fallos y la orquestación, permitiendo a los desarrolladores centrarse en la lógica.

#### Componentes Principales
- **Ray Core**: La base—primitivas pitónicas para tareas (funciones paralelas), actores (servicios con estado) y objetos (intercambio de datos distribuido). Maneja automáticamente el autoescalado, los reintentos y la asignación de recursos.
- **Librerías de IA de Ray**: Herramientas específicas de dominio construidas sobre Core:
  - **Ray Data**: ETL escalable para preprocesar conjuntos de datos.
  - **Ray Train**: Entrenamiento distribuido con integraciones (PyTorch, TensorFlow, Hugging Face).
  - **Ray Tune**: Optimización de hiperparámetros a escala.
  - **Ray Serve**: Implementación de modelos para inferencia, con enrutamiento, procesamiento por lotes y pruebas A/B.
  - **RLlib**: Kit de herramientas para aprendizaje por refuerzo.
- **Clústeres Ray**: Capa de infraestructura gestionada para implementar en la nube (AWS, GCP), Kubernetes, o on-prem, con autoescalado basado en la demanda.

#### Cómo Funciona
Ray se ejecuta como un daemon en los nodos, formando un clúster con un nodo principal (head node) para la coordinación. Se decoran funciones con `@ray.remote` para paralelismo, y éste distribuye la ejecución a través de CPUs/GPUs. Para ML, librerías como Serve manejan endpoints HTTP y balanceo de carga, mientras que Core asegura un escalado tolerante a fallos (por ejemplo, reiniciando tareas fallidas).

#### Casos de Uso Clave en ML/IA
- Pipelines de principio a fin: Carga de datos → entrenamiento → ajuste → servicio.
- Búsquedas de hiperparámetros en 100s de GPUs.
- Flotas de inferencia en tiempo real, como en sistemas de recomendación.
- Aplicaciones distribuidas personalizadas, por ejemplo, simulaciones.

La fortaleza de Ray es su API unificada: Escribe una vez, escala en cualquier lugar, con bajo código repetitivo (boilerplate) en comparación con Spark o Dask.

### Relación Entre vLLM y Ray
En sistemas como SLOs-Serve (de nuestra discusión anterior), vLLM maneja el procesamiento por lotes/inferencia de bajo nivel del LLM, mientras que Ray orquesta las implementaciones multi-réplica, enrutando las solicitudes a través de los nodos para manejar picos de carga y el escalado.

[Documentación de vLLM](https://docs.vllm.ai/en/latest/)  
[Documentación de Ray](https://docs.ray.io/en/latest/ray-overview/index.html)