---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Essayer llama.cpp
translated: true
type: post
---

## llama.cpp

Lors de l'exécution de `llama.cpp` avec un modèle, vous pourriez rencontrer une erreur comme celle-ci :

```bash
% ./main -m models/7B/Phi-3-mini-4k-instruct-q4.gguf
main: build = 964 (f3c3b4b)
main: seed  = 1737736417
llama.cpp: loading model from models/7B/Phi-3-mini-4k-instruct-q4.gguf
error loading model: unknown (magic, version) combination: 46554747, 00000003; is this really a GGML file?
llama_load_model_from_file: failed to load model
llama_init_from_gpt_params: error: failed to load model 'models/7B/Phi-3-mini-4k-instruct-q4.gguf'
main: error: unable to load model
```

Cette erreur se produit parce que vous exécutez le programme `main`. L'exécution des programmes `llama-cli` ou `llama-server` situés sous `build/bin` devrait résoudre le problème.

Le programme `main` a été créé le 8 août 2023, ce qui signifie qu'il n'est pas la version actuelle.

Une autre solution consiste à installer `llama.cpp` en utilisant Homebrew :

```bash
brew install llama.cpp
```

Cela garantit que vous disposez d'une version compatible de la bibliothèque.

## Servir le Modèle

```bash
/home/lzw/Projects/llama.cpp/build/bin/llama-server -m /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-Distill-Qwen-14B-Q5_K_M.gguf --port 8000  --ctx-size 2048 --batch-size 512 --n-gpu-layers 49 --threads 8 --parallel 1
```

Les paramètres `--ctx-size 2048 --batch-size 512 --n-gpu-layers 49 --threads 8 --parallel 1` sont importants. Ils augmenteront la vitesse.

## LLM Farm

C'est une excellente application iOS. Dans les paramètres, il y a environ 20 modèles. Lors de l'importation d'un modèle GGUF par nous-mêmes, qui sont téléchargés depuis Hugging Face, cela peut entraîner un plantage.

## Avantages

L'auto-hébergement de ces modèles LLM vous permet de les exécuter localement sans avoir besoin d'un accès réseau. Par exemple, lors du téléchargement de grands fichiers qui congestionnent le réseau, l'exécution d'un modèle local peut être bénéfique.

## Ressources

*   [Modèles GGML de Hugging Face](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [Dépôt GitHub de llama.cpp](https://github.com/ggerganov/llama.cpp)
*   [Dépôt GitHub de ggml](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)