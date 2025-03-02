---
audio: false
generated: true
lang: es
layout: post
title: Intentando llama.cpp
translated: true
---

## llama.cpp

Al intentar ejecutar `llama.cpp` con un modelo, es posible que encuentres un error como este:

```bash
% ./main -m models/7B/Phi-3-mini-4k-instruct-q4.gguf
main: build = 964 (f3c3b4b)
main: seed  = 1737736417
llama.cpp: cargando modelo desde models/7B/Phi-3-mini-4k-instruct-q4.gguf
error loading model: combinación desconocida (mágica, versión): 46554747, 00000003; ¿es esto realmente un archivo GGML?
llama_load_model_from_file: falló al cargar el modelo
llama_init_from_gpt_params: error: falló al cargar el modelo 'models/7B/Phi-3-mini-4k-instruct-q4.gguf'
main: error: no se pudo cargar el modelo
```

Este error ocurre porque estás ejecutando el programa `main`. Ejecutar los programas `llama-cli` o `llama-server` ubicados en `build/bin` debería resolver el problema.

El programa `main` se creó el 8 de agosto de 2023, lo que significa que no es el build actual.

Otra solución es instalar `llama.cpp` usando Homebrew:

```bash
brew install llama.cpp
```

Esto asegura que tengas una versión compatible de la biblioteca.

## Servir el Modelo

```bash
/home/lzw/Projects/llama.cpp/build/bin/llama-server -m /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-Distill-Qwen-14B-Q5_K_M.gguf --port 8000  --ctx-size 2048 --batch-size 512 --n-gpu-layers 49 --threads 8 --parallel 1
```

Los parámetros `--ctx-size 2048 --batch-size 512 --n-gpu-layers 49 --threads 8 --parallel 1` son importantes. Aumentarán la velocidad.

## LLM Farm

Es una excelente aplicación para iOS. En la configuración, hay alrededor de 20 modelos. Al importar un modelo GGUF por nosotros mismos, que se descargan de Hugging Face, puede llevar a un bloqueo.

## Beneficios

Al alojar estos modelos LLM localmente, puedes ejecutarlos sin necesidad de acceso a la red. Por ejemplo, al descargar archivos grandes que congestionan la red, ejecutar un modelo local puede ser beneficioso.

## Recursos

*   [Modelos GGML de Hugging Face](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [Repositorio GitHub de llama.cpp](https://github.com/ggerganov/llama.cpp)
*   [Repositorio GitHub de ggml](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)