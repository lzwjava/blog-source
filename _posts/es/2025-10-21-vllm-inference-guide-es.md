---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: 'vLLM: Guía Rápida de Inferencia de LLM'
translated: true
type: note
---

vLLM es una biblioteca de código abierto diseñada para la inferencia y el servicio rápido y eficiente en memoria de modelos de lenguaje grandes (LLMs). Desarrollada inicialmente en el Sky Computing Lab de UC Berkeley, ha crecido hasta convertirse en un proyecto impulsado por la comunidad con contribuciones de la academia y la industria. vLLM aborda desafíos clave en el despliegue de LLMs, como la alta latencia, la fragmentación de memoria y el bajo rendimiento, lo que lo hace ideal para entornos de producción. Soporta una integración perfecta con modelos de Hugging Face y proporciona una API compatible con OpenAI para una fácil adopción.

## Características Principales

vLLM destaca por su rendimiento y flexibilidad:
- **PagedAttention**: Gestiona eficientemente la memoria de la caché de clave-valor (KV) para reducir el desperdicio y permitir un mayor rendimiento.
- **Continuous Batching**: Agrupa dinámicamente las solicitudes entrantes sin esperar a que se completen los lotes, mejorando la utilización de recursos.
- **Kernels Optimizados**: Integra FlashAttention, FlashInfer y grafos personalizados CUDA/HIP para una ejecución más rápida.
- **Soporte de Cuantización**: Incluye GPTQ, AWQ, INT4/INT8/FP8 para reducir la huella de memoria.
- **Algoritmos de Decodificación**: Soporta muestreo paralelo, búsqueda por haz, decodificación especulativa y prefill por fragmentos.
- **Inferencia Distribuida**: Paralelismo de tensor, pipeline, datos y expertos para configuraciones multi-GPU.
- **Compatibilidad de Hardware**: GPUs NVIDIA, CPUs/GPUs AMD/Intel, CPUs PowerPC, TPUs, y plugins para Intel Gaudi, IBM Spyre, Huawei Ascend.
- **Herramientas Adicionales**: Salidas en streaming, caché de prefijos, soporte multi-LoRA y un servidor compatible con OpenAI.

Estas características permiten a vLLM lograr un rendimiento de servicio de vanguardia siendo fácil de usar.

## Prerrequisitos

- **Sistema Operativo**: Linux (soporte principal; algunas funciones en otras plataformas).
- **Python**: 3.9 a 3.13.
- **Hardware**: Se recomiendan GPUs NVIDIA para todas las funciones; modo solo CPU disponible pero más lento.
- **Dependencias**: PyTorch (autodetectado vía versión de CUDA), Hugging Face Transformers.

## Instalación

vLLM se puede instalar vía pip. Usa `uv` (un gestor de entornos Python rápido) para una configuración óptima:

1. Instala `uv` siguiendo su [documentación](https://docs.astral.sh/uv/getting-started/installation/).
2. Crea un entorno virtual e instala vLLM:

   ```
   uv venv --python 3.12 --seed
   source .venv/bin/activate
   uv pip install vllm --torch-backend=auto
   ```

   - `--torch-backend=auto` selecciona automáticamente PyTorch basado en tu controlador CUDA.
   - Para backends específicos (ej., CUDA 12.6): `--torch-backend=cu126`.

Alternativamente, usa `uv run` para comandos únicos sin un entorno permanente:

   ```
   uv run --with vllm vllm --help
   ```

Para usuarios de Conda:

   ```
   conda create -n myenv python=3.12 -y
   conda activate myenv
   pip install --upgrade uv
   uv pip install vllm --torch-backend=auto
   ```

Para configuraciones no-NVIDIA (ej., AMD/Intel), consulta la [guía de instalación oficial](https://docs.vllm.ai/en/stable/getting_started/installation.html) para instrucciones específicas de la plataforma, incluyendo compilaciones solo CPU.

Los backends de atención (FLASH_ATTN, FLASHINFER, XFORMERS) se seleccionan automáticamente; anula con la variable de entorno `VLLM_ATTENTION_BACKEND` si es necesario. Nota: FlashInfer requiere instalación manual ya que no está en las ruedas preconstruidas.

## Inicio Rápido

### Inferencia por Lotes Offline

Usa vLLM para generar texto a partir de una lista de prompts. Script de ejemplo (`basic.py`):

```python
from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

llm = LLM(model="facebook/opt-125m")  # Descarga de Hugging Face por defecto
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

- **Notas**:
  - Por defecto, usa el `generation_config.json` del modelo para los parámetros de muestreo; anula con `generation_config="vllm"`.
  - Para modelos de chat/instruct, aplica las plantillas de chat manualmente o usa `llm.chat(messages_list, sampling_params)`.
  - Establece `VLLM_USE_MODELSCOPE=True` para modelos de ModelScope.

### Servicio Online (API Compatible con OpenAI)

Inicia un servidor con:

```
vllm serve Qwen/Qwen2.5-1.5B-Instruct
```

Esto inicia en `http://localhost:8000`. Personaliza con `--host` y `--port`.

Consulta vía curl (endpoint de completions):

```
curl http://localhost:8000/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "Qwen/Qwen2.5-1.5B-Instruct",
        "prompt": "San Francisco is a",
        "max_tokens": 7,
        "temperature": 0
    }'
```

O chat completions:

```
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "Qwen/Qwen2.5-1.5B-Instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]
    }'
```

Usando Python (cliente OpenAI):

```python
from openai import OpenAI

openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
client = OpenAI(api_key=openai_api_key, base_url=openai_api_base)

completion = client.completions.create(
    model="Qwen/Qwen2.5-1.5B-Instruct",
    prompt="San Francisco is a"
)
print("Completion result:", completion)
```

Habilita la autenticación por clave API con `--api-key <clave>` o `VLLM_API_KEY`.

## Modelos Soportados

vLLM soporta una gran variedad de modelos generativos y de agrupación (pooling) mediante implementaciones nativas o el backend de Hugging Face Transformers. Las categorías clave incluyen:

- **Modelos de Lenguaje Causal**: Llama (3.1/3/2), Mistral, Gemma (2/3), Qwen, Phi (3/3.5), Mixtral, Falcon, BLOOM, GPT-NeoX/J/2, DeepSeek (V2/V3), InternLM (2/3), GLM (4/4.5), Command-R, DBRX, Yi, y más.
- **Mezcla de Expertos (MoE)**: Mixtral, variantes MoE de DeepSeek-V2/V3, Granite MoE.
- **Multimodal**: LLaVA (1.5/1.6/Next), Phi-3-Vision, Qwen2-VL, InternVL2, CogVLM, Llama-3.2-Vision.
- **Lenguaje-Visión**: CLIP, SigLIP (agrupación/incrustación).
- **Otros**: Codificador-decodificador (T5, BART), modelos de difusión (Stable Diffusion), y arquitecturas personalizadas como Jamba, GritLM.

El soporte completo incluye adaptadores LoRA, paralelismo de pipeline (PP) y compatibilidad con el motor V1 para la mayoría. Para la lista completa (más de 100 arquitecturas), consulta la [documentación de modelos soportados](https://docs.vllm.ai/en/stable/models/supported_models.html). Los modelos personalizados se pueden integrar con cambios mínimos.

## Opciones de Despliegue

### Despliegue con Docker

Usa la imagen oficial `vllm/vllm-openai` para un servicio fácil:

```
docker run --runtime nvidia --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" \
    -p 8000:8000 \
    --ipc=host \
    vllm/vllm-openai:latest \
    --model Qwen/Qwen2.5-1.5B-Instruct
```

- `--ipc=host` o `--shm-size=8g` para memoria compartida en configuraciones multi-GPU.
- Soporta Podman de manera similar.
- Para imágenes personalizadas: Construye desde el código fuente usando `docker/Dockerfile` con BuildKit:

  ```
  DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag vllm/custom --file docker/Dockerfile
  ```

- Compilaciones Arm64/aarch64: Usa `--platform linux/arm64` (experimental; requiere PyTorch Nightly).
- Añade dependencias opcionales (ej., audio) o Transformers desde el código fuente en un Dockerfile personalizado.

Otras opciones incluyen Kubernetes, AWS SageMaker o integración directa con frameworks como Ray Serve.

## Optimización del Rendimiento

Para optimizar el rendimiento y la latencia:

- **Selección de GPU**: Usa A100/H100 para alto rendimiento; escala con paralelismo de tensor (`--tensor-parallel-size`).
- **Tamaño del Lote**: Establece `--max-num-seqs` y `--max-model-len` basado en la caché KV; apunta a un 80-90% de utilización de la GPU.
- **Cuantización**: Habilita AWQ/GPTQ (`--quantization awq`) para ajustar modelos más grandes.
- **Backend de Atención**: Prefiere FlashInfer para GPUs más nuevas; prueba con `VLLM_ATTENTION_BACKEND=FLASHINFER`.
- **Balance Prefill/Decodificación**: Usa `--chunked-prefill-size` para entradas largas.
- **Benchmarking**: Ejecuta `vllm benchmark` o conjuntos de datos ShareGPT para medir TTFT (tiempo hasta el primer token) y TPOT (tiempo por token de salida).
- **Mejores Prácticas**:
  - Monitoriza con Prometheus/Grafana.
  - Para TPUs: Usa el backend JAX; ajusta el sharding.
  - Evita el sobre-paralelismo; comienza con una sola GPU y escala.

Para configuraciones detalladas de xPU, consulta las guías específicas de hardware.

## Uso Avanzado

- **Servicio Distribuido**: `--tensor-parallel-size N` para multi-GPU; combina con Ray para clústeres.
- **LoRA**: Carga adaptadores con `--lora-modules`.
- **Decodificación Especulativa**: Integra con Medusa para aceleraciones de 2x.
- **Kernels Personalizados**: Extiende mediante plugins para nuevo hardware.
- **Monitorización**: Habilita `--enable-chunked-prefill` y registra métricas.

Explora la [guía de usuario](https://docs.vllm.ai/en/stable/usage/) para motores e integraciones.

## Referencias

- [Documentación Oficial de vLLM](https://docs.vllm.ai/)
- [Guía de Inicio Rápido](https://docs.vllm.ai/en/stable/getting_started/quickstart.html)
- [Modelos Soportados](https://docs.vllm.ai/en/stable/models/supported_models.html)
- [Despliegue con Docker](https://docs.vllm.ai/en/stable/serving/deploying_with_docker.html)
- [Guía de Optimización de Rendimiento de vLLM (Google Cloud)](https://cloud.google.com/blog/topics/developers-practitioners/vllm-performance-tuning-the-ultimate-guide-to-xpu-inference-configuration)
- [Guía Definitiva de vLLM (newline)](https://www.newline.co/@zaoyang/ultimate-guide-to-vllm--aad8b65d)
- [Tutorial de vLLM para Principiantes](https://www.designveloper.com/blog/vllm-tutorial/)