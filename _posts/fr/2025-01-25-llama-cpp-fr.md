---
audio: false
lang: fr
layout: post
title: Essayer llama.cpp
translated: true
---

## llama.cpp

Lorsque vous essayez d'exécuter `llama.cpp` avec un modèle, vous pourriez rencontrer une erreur comme celle-ci :

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

Cette erreur survient parce que vous exécutez le programme `main`. L'exécution des programmes `llama-cli` ou `llama-server` situés sous `build/bin` devrait résoudre le problème.

Le programme `main` a été créé le 8 août 2023, ce qui signifie qu'il ne s'agit pas de la version actuelle.

Une autre solution consiste à installer `llama.cpp` à l'aide de Homebrew :

```bash
brew install llama.cpp
```

Cela garantit que vous disposez d'une version compatible de la bibliothèque.

## Ollama

```bash
% ollama list
NAME                   ID              SIZE      MODIFIED
deepseek-coder:6.7b    ce298d984115    3.8 GB    Il y a 14 heures
mistral:7b             f974a74358d6    4.1 GB    Il y a 15 heures
```

```bash
ollama remove model
```

C'est un excellent outil à utiliser. Il y a quelques bogues dans Ollamac. Par exemple, lorsqu'il reçoit une réponse de l'API locale, plusieurs zones de texte dans l'application sont mises à jour.

Cependant, sous Linux, Ollama s'exécute comme un service système. Voici le fichier de configuration du service :

`/etc/systemd/system/ollama.service` :

```bash
[Unit]
Description=Service Ollama
After=network-online.target

[Service]
ExecStart=/usr/local/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3
Environment="PATH=/home/lzw/.local/bin:/home/lzw/bin:/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"

[Install]
WantedBy=default.target
```

Utilisez les commandes suivantes pour contrôler le service Ollama :

```bash
sudo systemctl stop ollama.service
sudo systemctl disable ollama.service
sudo systemctl status ollama.service
```

## LLM Farm

C'est une excellente application iOS. Dans les paramètres, il y a environ 20 modèles. Lors de l'importation d'un modèle GGUF par nous-mêmes, téléchargés depuis Hugging Face, cela peut entraîner un plantage.

## Avantages

L'auto-hébergement de ces modèles LLM vous permet de les exécuter localement sans avoir besoin d'un accès réseau. Par exemple, lors du téléchargement de gros fichiers qui encombrent le réseau, l'exécution d'un modèle local peut être bénéfique.

## Ressources

*   [Modèles Hugging Face GGML](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [Répertoire GitHub llama.cpp](https://github.com/ggerganov/llama.cpp)
*   [Répertoire GitHub ggml](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)
