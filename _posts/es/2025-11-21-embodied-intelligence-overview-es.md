---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4.1-fast
title: Panorama de la Inteligencia Encarnada
translated: true
type: note
---

### Inteligencia Corporizada: Una Visión General

La inteligencia corporizada, también conocida como IA corporizada, se refiere a sistemas de inteligencia artificial que están físicamente situados en el mundo a través de un cuerpo (por ejemplo, un robot) y que aprenden, razonan y actúan mediante la interacción directa con su entorno. A diferencia de la IA tradicional, que procesa datos abstractos de forma aislada (por ejemplo, modelos de lenguaje como GPT), la IA corporizada enfatiza que la verdadera inteligencia emerge de los bucles sensoriomotores: percibir el mundo, actuar sobre él y adaptarse en base a la retroalimentación. Este paradigma se inspira en la ciencia cognitiva, donde la cognición se considera arraigada en la corporización física en lugar de en la computación pura.

Los principios clave incluyen:
- **Percepción multimodal**: Integrar visión, tacto, propiocepción y, a veces, lenguaje o sonido.
- **Aprendizaje impulsado por la interacción**: Los agentes mejoran mediante prueba y error en el mundo real o en simulaciones de alta fidelidad (transferencia de sim a real).
- **Generalización y adaptación**: Manejar entornos no estructurados y dinámicos con tareas de horizonte largo, multimodalidad (por ejemplo, combinar visión y lenguaje) y robustez frente a perturbaciones.

En 2025, la IA corporizada ha explotado gracias a los modelos fundacionales (grandes modelos de visión y lenguaje preentrenados), las técnicas de difusión y los conjuntos de datos masivos como Open X-Embodiment. Impulsa avances en robots humanoides, manipulación, navegación e interacción humano-robot. Los desafíos persisten en el rendimiento en tiempo real, la seguridad, las brechas entre simulación y realidad y la escalabilidad a tareas de mundo abierto. Los esfuerzos líderes incluyen la serie RT de Google, OpenVLA y políticas basadas en difusión, con el objetivo de lograr robots de propósito general.

### Tecnologías Clave: Diffusion Policy, RT-2 y ACT

Estas tres representan enfoques de vanguardia para aprender políticas robóticas (mapeos de observaciones a acciones) mediante aprendizaje por imitación—entrenando con demostraciones humanas o expertas sin recompensas explícitas.

#### ACT (Action Chunking with Transformer)
- **Origen**: Introducido en 2023 por Tony Zhao et al. (Covariant.ai, anteriormente de UC Berkeley) como parte del sistema ALOHA para manipulación bimanual de bajo costo.
- **Idea Central**: Una política basada en transformer que predice **fragmentos** de acciones futuras (por ejemplo, 100 pasos a la vez) en lugar de una acción por paso de tiempo. Esto reduce los errores temporales (errores acumulativos en horizontes largos) y permite un control suave y de alta frecuencia (por ejemplo, 50Hz).
- **Arquitectura**: Utiliza una base de Variational Autoencoder (VAE) o transformer. Entrada: Imágenes RGB multi-vista + propiocepción (estados de las articulaciones). Salida: Posiciones/velocidades de las articulaciones en fragmentos.
- **Fortalezas**:
  - Extremadamente eficiente en muestras (aprende tareas complejas con ~50 demostraciones).
  - Capaz de funcionar en tiempo real con hardware de consumo.
  - Destaca en tareas precisas y diestras (por ejemplo, enhebrar una aguja, doblar la ropa) con robots de bajo costo.
- **Limitaciones**: Principalmente basado en imitación; menos soporte inherente para instrucciones de lenguaje o generalización a escala web sin extensiones.
- **Impacto en el Mundo Real**: Impulsa sistemas como ALOHA (manipuladores móviles) y ha sido ampliamente adoptado para tareas bimanuales.

#### Diffusion Policy
- **Origen**: Artículo de 2023 por Cheng Chi et al. (Columbia University, Toyota Research Institute, MIT). Extendido en trabajos como 3D Diffusion Policy y ScaleDP (hasta 1B de parámetros en 2025).
- **Idea Central**: Trata las acciones del robot como muestras generativas de un modelo de difusión (inspirado en generadores de imágenes como Stable Diffusion). Comienza con acciones ruidosas, las desruida iterativamente condicionadas a las observaciones para producir secuencias de acciones de alta calidad y multimodales.
- **Arquitectura**: Modelo de difusión de desruido condicional (a menudo con transformers). Aprende la "función de puntuación" (gradiente de la distribución de acciones). La inferencia utiliza control de horizonte deslizante: planifica una secuencia, ejecuta la primera acción, replanifica.
- **Fortalezas**:
  - Maneja comportamientos **multimodales** de forma natural (por ejemplo, múltiples formas válidas de agarrar un objeto—la difusión muestrea una de forma coherente sin promediar).
  - Robusto a acciones de alta dimensión y demostraciones ruidosas.
  - Estado del arte en benchmarks (46%+ de mejora sobre trabajos anteriores en 2023; aún competitivo en 2025).
  - Extensiones como 3D Diffusion Policy utilizan nubes de puntos para una mejor comprensión 3D.
- **Limitaciones**: Inferencia más lenta (10–100 pasos de desruido), aunque las optimizaciones (por ejemplo, menos pasos, destilación) la hacen viable en tiempo real.
- **Impacto en el Mundo Real**: Ampliamente utilizado para manipulación visuomotora; integrado en sistemas como PoCo (composición de políticas) y modelos escalados.

#### RT-2 (Robotics Transformer 2)
- **Origen**: 2023 por Google DeepMind (construyendo sobre RT-1). Parte de la familia Visión-Lenguaje-Acción (VLA).
- **Idea Central**: Co-fine-tune un gran modelo de visión y lenguaje preentrenado (por ejemplo, PaLM-E o PaLI-X, hasta 55B parámetros) en trayectorias robóticas. Las acciones se tokenizan como cadenas de texto, permitiendo que el modelo genere acciones directamente mientras aprovecha el conocimiento a escala web (imágenes + texto).
- **Arquitectura**: Transformer que toma imágenes + instrucciones de lenguaje → acciones tokenizadas. Habilidades emergentes del preentrenamiento web (por ejemplo, razonar sobre símbolos, cadena de pensamiento).
- **Fortalezas**:
  - **Generalización semántica**: Comprende comandos novedosos (por ejemplo, "recoge el animal extinto" → agarra el juguete de dinosaurio) sin entrenamiento específico para robots.
  - Transfiere conocimiento web a la robótica (por ejemplo, reconoce basura de imágenes de internet).
  - Hasta 3 veces mejor en habilidades emergentes vs. modelos robóticos anteriores.
- **Limitaciones**: Modelos grandes → mayor requerimiento computacional; menos preciso para control diestro de bajo nivel en comparación con ACT/Diffusion (mejor para razonamiento de alto nivel).
- **Impacto en el Mundo Real**: Impulsa la recolección de datos de la flota de robots de Google (AutoRT); evolucionó a RT-X y se integró con sistemas posteriores.

### Tabla Comparativa

| Aspecto                  | ACT                                      | Diffusion Policy                          | RT-2                                      |
|-------------------------|------------------------------------------|-------------------------------------------|-------------------------------------------|
| **Método Principal**    | Transformer + fragmentación de acciones (determinista/regresivo) | Difusión de desruido (generativo)         | VLA (acciones tokenizadas en LLM/VLM)     |
| **Entrada**             | Imágenes multi-vista + propiocepción     | Imágenes/nubes de puntos + propiocepción  | Imágenes + instrucciones de lenguaje      |
| **Salida**              | Acciones articulares en fragmentos       | Secuencias de acciones desruidadas        | Cadenas de texto de acciones tokenizadas  |
| **Fortaleza Clave**     | Eficiencia de muestras, precisión, tiempo real | Multimodalidad, robustez, expresividad    | Razonamiento semántico, generalización desde datos web |
| **Velocidad de Inferencia** | Rápida (paso único)                      | Más lenta (desruido iterativo)            | Media (transformer autoregresivo)         |
| **Eficiencia de Datos** | Muy alta (~50 demos/tarea)               | Alta                                      | Media (se beneficia del preentrenamiento web) |
| **Mejor Para**          | Manipulación diestra y precisa           | Tareas complejas y multimodales           | Tareas guiadas por lenguaje, tareas novedosas/emergentes |
| **Mejora Típica en Tasa de Éxito (vs. líneas base)** | Fuerte en benchmarks de robot real       | +46% (benchmarks de 2023)                 | 2–3× en habilidades emergentes            |
| **Estado en 2025**      | Línea base para hardware de bajo costo   | Escalado a miles de millones de parámetros | Base para sucesores OpenVLA/RT-X          |

### Cómo se Integran en la Inteligencia Corporizada

- **ACT y Diffusion Policy**: Políticas visuomotoras puras—sobresalen en habilidades sensoriomotoras de bajo nivel, el "cuerpo" de la IA corporizada. Permiten a los robots actuar de forma fluida en el mundo físico a partir de píxeles en bruto.
- **RT-2 (y modelos VLA)**: Puente hacia la cognición superior—añaden lenguaje para una interacción y razonamiento similares a los humanos, impulsando hacia agentes corporizados de propósito general.
- **Los híbridos son el futuro**: Las tendencias de 2025 los combinan (por ejemplo, OpenVLA = similar a RT-2 + cabezas de difusión; OCTO = modelos pequeños y eficientes con elementos de difusión). Objetivo final: Robots que perciben multimodalmente, razonan con LLMs/modelos del mundo y actúan con precisión mediante difusión/fragmentación.

Estos métodos han democratizado la robótica diestra: Tareas que antes requerían años de ingeniería ahora tienen éxito con docenas de demostraciones humanas. A medida que crecen los conjuntos de datos (por ejemplo, Open X-Embodiment) y mejora el hardware (humanoides como Figure 01, Tesla Optimus), la IA corporizada se acerca rápidamente a robots versátiles y útiles para el mundo real.

[Página del Proyecto Diffusion Policy](https://diffusion-policy.cs.columbia.edu/)  
[Anuncio de RT-2](https://deepmind.google/discover/blog/rt-2-new-model-translates-vision-and-language-into-action/)  
[Paper de ALOHA / ACT](https://tonyzhaozh.github.io/aloha/)  
[Conjunto de Datos Open X-Embodiment](https://robotics-transformer-x.github.io/)