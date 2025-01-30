---
audio: false
lang: fr
layout: post
title: Essayer llama.cpp
translated: true
---

## llama.cpp

Lorsque vous essayez d'exécuter `llama.cpp` avec un modèle, vous pourriez rencontrer une erreur comme celle-ci :

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

Cette erreur se produit parce que vous exécutez le programme `main`. Exécuter les programmes `llama-cli` ou `llama-server` situés sous `build/bin` devrait résoudre le problème.

Le programme `main` a été créé le 8 août 2023, ce qui signifie qu'il ne s'agit pas de la version actuelle.

Une autre solution consiste à installer `llama.cpp` en utilisant Homebrew :

```bash
brew install llama.cpp
```

Cela garantit que vous disposez d'une version compatible de la bibliothèque.

## Ollama

```bash
% ollama list
NAME                   ID              SIZE      MODIFIED
deepseek-coder:6.7b    ce298d984115    3.8 GB    14 hours ago
mistral:7b             f974a74358d6    4.1 GB    15 hours ago
```

```bash
ollama remove model
```

C'est un excellent outil à utiliser. Il y a quelques bugs dans Ollamac. Par exemple, lorsqu'il reçoit une réponse de l'API locale, plusieurs zones de texte de l'application sont mises à jour.

## LLM Farm

C'est une excellente application iOS. Dans les paramètres, il y a environ 20 modèles. Lors de l'importation d'un modèle GGUF par nous-mêmes, qui sont téléchargés depuis Hugging Face, cela peut entraîner un plantage.

## Avantages

L'auto-hébergement de ces modèles LLM vous permet de les exécuter localement sans avoir besoin d'accès au réseau. Par exemple, lors du téléchargement de gros fichiers qui encombrent le réseau, l'exécution d'un modèle local peut être bénéfique.

## Ressources

*   [Modèles GGML Hugging Face](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [Dépôt GitHub llama.cpp](https://github.com/ggerganov/llama.cpp)
*   [Dépôt GitHub ggml](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)