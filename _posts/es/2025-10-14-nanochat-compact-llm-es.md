---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: NanoChat Compacto Full Stack LLM
translated: true
type: note
---

### ¿Qué es NanoChat?

NanoChat es una implementación compacta y full-stack de un sistema de modelo de lenguaje grande (LLM) similar a ChatGPT, construido en una única base de código mínima que es fácil de modificar y requiere pocas dependencias. Creado por Andrej Karpathy (famoso por su trabajo en IA, como nanoGPT), está diseñado para ejecutar la canalización completa de un LLM—desde la tokenización y el preentrenamiento hasta el ajuste fino, la evaluación, la inferencia e incluso una interfaz web simple para chatear con tu modelo—en hardware asequible como un solo nodo con 8xH100 GPUs.

Se posiciona como el "mejor ChatGPT que 100 dólares pueden comprar", sirviendo como una línea base para el desarrollo de LLM económico (menos de 1000 dólares en total). Esto lo convierte en un proyecto final para el próximo curso LLM101n de Eureka Labs de Karpathy, haciendo hincapié en la simplicidad frente a configuraciones complejas.

### Características Principales
- **Canalización Integral**: Maneja todo en ~2000 líneas de código (con un archivo `uv.lock` pequeño para las dependencias). Entrena un modelo competente con 4e19 FLOPs en aproximadamente 4 horas en una configuración 8xH100 que cuesta ~$24/hora.
- **Interfaz de Usuario Similar a ChatGPT**: Después del entrenamiento, inicia un servidor web para interactuar con tu modelo como si fuera el ChatGPT real.
- **Informe de Evaluación**: Genera automáticamente un `report.md` con puntuaciones de evaluación en tareas como ARC-Challenge, GSM8K, HumanEval, MMLU y más. Por ejemplo, una ejecución de muestra de $100 muestra mejoras progresivas a través de las etapas (BASE, MID, SFT, RL):

| Métrica        | BASE   | MID    | SFT    | RL     |
|---------------|--------|--------|--------|--------|
| CORE          | 0.2219 | -      | -      | -      |
| ARC-Challenge | -      | 0.2875 | 0.2807 | -      |
| ARC-Easy      | -      | 0.3561 | 0.3876 | -      |
| GSM8K         | -      | 0.0250 | 0.0455 | 0.0758 |
| HumanEval     | -      | 0.0671 | 0.0854 | -      |
| MMLU          | -      | 0.3111 | 0.3151 | -      |
| ChatCORE      | -      | 0.0730 | 0.0884 | -      |

(Tiempo total: ~3h51m para la ejecución completa.)
- **Flexibilidad de Hardware**: Funciona en Ampere 8xA100 (más lento), GPUs individuales (con acumulación automática de gradientes) o configuraciones con menos VRAM ajustando los tamaños de lote. Utiliza PyTorch estándar; adaptable a otros dispositivos con ajustes.
- **Fuentes de Datos**: Obtiene datos de conjuntos de Hugging Face como FineWeb y SmolTalk.
- **Extras**: Incluye tests (por ejemplo, para el tokenizador basado en Rust), y es fácil empaquetar todo el repositorio (~330KB) para consultarlo con otros LLMs.

Está inspirado en proyectos anteriores de Karpathy como nanoGPT y modded-nanoGPT, pero escalado para una experiencia de chat completa.

### Cómo Empezar
La forma más rápida es el script `speedrun.sh`, que maneja el modelo de nivel $100 de principio a fin en una 8xH100 (por ejemplo, a través de Lambda Labs):

1. Inicia una instancia 8xH100 y clona el repositorio.
2. Ejecuta:
   ```
   bash speedrun.sh
   ```
   (O en una sesión de screen para registrar: `screen -L -Logfile speedrun.log -S speedrun bash speedrun.sh`. Sepárate con Ctrl+A+D y sigue el registro con `tail`).

3. Una vez terminado (~4 horas), activa el entorno (`source .venv/bin/activate`) y sirve la interfaz web:
   ```
   python -m scripts.chat_web
   ```
   Abre la URL local (por ejemplo, http://tu-ip:8000) para chatear con tu modelo. Revisa `report.md` para ver los resultados.

Para modelos más grandes (por ejemplo, nivel $300 en ~12 horas, superando a GPT-2 en algunas puntuaciones), edita `speedrun.sh` para descargar más fragmentos de datos y ajusta las profundidades/tamaños de lote. Ejecuta tests como `python -m pytest tests/test_rustbpe.py -v -s`.

Tiene licencia MIT y está abierto a contribuciones para impulsar aún más los micro-modelos. Para un recorrido detallado, consulta los Discussions del repositorio.

[Repositorio de NanoChat en GitHub](https://github.com/karpathy/nanochat)