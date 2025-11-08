---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: NanoGPT y NanoChat de Karpathy Explicados
translated: true
type: note
---

### Resumen
Tanto **nanoGPT** como **nanochat** son proyectos de código abierto creados por Andrej Karpathy (exlíder de IA en OpenAI/Tesla) para enseñar los fundamentos internos de los grandes modelos de lenguaje (LLMs) a través de implementaciones mínimas desde cero en PyTorch. Son herramientas educativas más que sistemas listos para producción, que enfatizan la simplicidad y la legibilidad sobre las optimizaciones.

- **nanoGPT** (lanzado en 2023): Un framework ligero para entrenar modelos transformadores tipo GPT en datos de texto sin procesar, centrándose únicamente en la fase de preentrenamiento.
- **nanochat** (lanzado en octubre de 2025): Una evolución expandida y de pila completa de nanoGPT, que permite el entrenamiento end-to-end, el fine-tuning, la inferencia y el despliegue de una IA conversacional al estilo de ChatGPT.

### Diferencias Clave
Aquí hay una comparación lado a lado:

| Aspecto             | nanoGPT                                                                 | nanochat                                                                 |
|---------------------|-------------------------------------------------------------------------|--------------------------------------------------------------------------|
| **Enfoque Principal** | Preentrenar un modelo GPT en texto no estructurado (ej. dataset de Shakespeare). | Pipeline completo: Preentrenamiento + fine-tuning para chat + inferencia en una interfaz web. |
| **Alcance**           | Implementación mínima del transformador (~400 líneas de código central). Sin interfaz de chat. | ~8,000 líneas en total, incluyendo fine-tuning tipo RLHF, sampling y una demo de chat basada en Streamlit. |
| **Entrenamiento**     | Modelado de lenguaje causal en la predicción del siguiente token. | Se extiende al fine-tuning supervisado (SFT) y a la optimización de preferencias (ej. DPO) para diálogo. |
| **Inferencia**        | Generación básica de texto. | Modo de chat interactivo con prompts de sistema/usuario/asistente, sampling de temperatura y filtros de seguridad. |
| **Hardware/Costo**    | Entrenable en una sola GPU (ej. 125M de parámetros en horas). | Eficiencia similar; afirma ser el "mejor ChatGPT que $100 pueden comprar" mediante GPUs baratas en la nube. |
| **Inspiraciones**     | Enseña los fundamentos del transformador. | Se basa en nanoGPT + modded-nanoGPT (versión gamificada); aspira a ser un "clon de ChatGPT" completo. |
| **Caso de Uso**       | Aprender el preentrenamiento de LLMs. | Construir/desplegar una IA conversacional básica desde cero. |
| **Estrellas en GitHub** | ~30k+ (en 2025). | Recién lanzado; crecimiento rápido a 10k+ en días. |

En esencia, nanoGPT es como construir el "cerebro" de un modelo GPT, mientras que nanochat añade la "boca" (interfaz de chat) y los "oídos" (manejo de diálogo), convirtiéndolo en un tutorial más completo para aplicaciones modernas de LLMs. Si te estás iniciando, comienza con nanoGPT para los fundamentos, y luego pasa a nanochat para las extensiones específicas de chat.

### Referencias
- [Repositorio de nanochat en GitHub](https://github.com/karpathy/nanochat)
- [Anuncio de Karpathy en X](https://x.com/karpathy/status/1977755427569111362)
- [Artículo de Forbes sobre nanochat](https://www.forbes.com/sites/lanceeliot/2025/10/15/make-your-own-chatgpt-clone-for-just-100-via-newly-released-nanochat-but-theres-a-catch/)
- [Post en Medium: De nanoGPT a NanoChat](https://medium.com/@sebuzdugan/nanochat-build-your-own-chatgpt-clone-in-8-000-lines-of-code-e07a70cc435e)