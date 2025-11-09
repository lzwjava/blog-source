---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide d'Inférence Rapide pour LLM avec vLLM
translated: true
type: note
---

vLLM est une bibliothèque open-source conçue pour l'inférence et le service rapides et efficaces en mémoire des grands modèles de langage (LLM). Développée initialement au Sky Computing Lab de l'UC Berkeley, elle est devenue un projet communautaire avec des contributions du monde universitaire et de l'industrie. vLLM résout les défis clés du déploiement des LLM, tels que la latence élevée, la fragmentation de la mémoire et le faible débit, ce qui la rend idéale pour les environnements de production. Elle prend en charge une intégration transparente avec les modèles Hugging Face et fournit une API compatible OpenAI pour une adoption facile.

## Fonctionnalités Clés

vLLM se distingue par ses performances et sa flexibilité :
- **PagedAttention** : Gère efficacement la mémoire cache clé-valeur (KV) pour réduire le gaspillage et permettre un débit plus élevé.
- **Batching Continu** : Traite dynamiquement les requêtes entrantes sans attendre des lots complets, améliorant l'utilisation des ressources.
- **Kernels Optimisés** : Intègre FlashAttention, FlashInfer et des graphes CUDA/HIP personnalisés pour une exécution plus rapide.
- **Prise en charge de la Quantification** : Inclut GPTQ, AWQ, INT4/INT8/FP8 pour réduire l'empreinte mémoire.
- **Algorithmes de Décodage** : Prend en charge l'échantillonnage parallèle, la recherche par faisceau, le décodage spéculatif et le pré-remplissage par blocs.
- **Inférence Distribuée** : Parallélisme de tenseur, de pipeline, de données et d'experts pour les configurations multi-GPU.
- **Compatibilité Matérielle** : GPU NVIDIA, CPU/GPU AMD/Intel, CPU PowerPC, TPU, et plugins pour Intel Gaudi, IBM Spyre, Huawei Ascend.
- **Outils Supplémentaires** : Sorties en flux, mise en cache des préfixes, prise en charge multi-LoRA et un serveur compatible OpenAI.

Ces fonctionnalités permettent à vLLM d'atteindre un débit de service de pointe tout en étant facile à utiliser.

## Prérequis

- **OS** : Linux (support principal ; certaines fonctionnalités sur d'autres plateformes).
- **Python** : 3.9 à 3.13.
- **Matériel** : GPU NVIDIA recommandés pour toutes les fonctionnalités ; mode CPU uniquement disponible mais plus lent.
- **Dépendances** : PyTorch (détecté automatiquement via la version CUDA), Hugging Face Transformers.

## Installation

vLLM peut être installé via pip. Utilisez `uv` (un gestionnaire d'environnement Python rapide) pour une configuration optimale :

1. Installez `uv` en suivant sa [documentation](https://docs.astral.sh/uv/getting-started/installation/).
2. Créez un environnement virtuel et installez vLLM :

   ```
   uv venv --python 3.12 --seed
   source .venv/bin/activate
   uv pip install vllm --torch-backend=auto
   ```

   - `--torch-backend=auto` sélectionne automatiquement PyTorch en fonction de votre pilote CUDA.
   - Pour des backends spécifiques (par ex., CUDA 12.6) : `--torch-backend=cu126`.

Alternativement, utilisez `uv run` pour des commandes ponctuelles sans environnement permanent :

   ```
   uv run --with vllm vllm --help
   ```

Pour les utilisateurs de Conda :

   ```
   conda create -n myenv python=3.12 -y
   conda activate myenv
   pip install --upgrade uv
   uv pip install vllm --torch-backend=auto
   ```

Pour les configurations non-NVIDIA (par ex., AMD/Intel), reportez-vous au [guide d'installation officiel](https://docs.vllm.ai/en/stable/getting_started/installation.html) pour des instructions spécifiques à la plateforme, y compris les builds CPU uniquement.

Les backends d'attention (FLASH_ATTN, FLASHINFER, XFORMERS) sont sélectionnés automatiquement ; remplacez-les avec la variable d'environnement `VLLM_ATTENTION_BACKEND` si nécessaire. Note : FlashInfer nécessite une installation manuelle car il n'est pas dans les wheels pré-construits.

## Démarrage Rapide

### Inférence par Lots Hors Ligne

Utilisez vLLM pour générer du texte à partir d'une liste de prompts. Exemple de script (`basic.py`) :

```python
from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

llm = LLM(model="facebook/opt-125m")  # Télécharge depuis Hugging Face par défaut
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

- **Notes** :
  - Par défaut, utilise le `generation_config.json` du modèle pour les paramètres d'échantillonnage ; remplacez avec `generation_config="vllm"`.
  - Pour les modèles de chat/instruct, appliquez les modèles de chat manuellement ou utilisez `llm.chat(messages_list, sampling_params)`.
  - Définissez `VLLM_USE_MODELSCOPE=True` pour les modèles ModelScope.

### Service en Ligne (API Compatible OpenAI)

Lancez un serveur avec :

```
vllm serve Qwen/Qwen2.5-1.5B-Instruct
```

Cela démarre sur `http://localhost:8000`. Personnalisez avec `--host` et `--port`.

Interrogez via curl (point de terminaison des complétions) :

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

Ou les complétions de chat :

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

En utilisant Python (client OpenAI) :

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

Activez l'authentification par clé API avec `--api-key <key>` ou `VLLM_API_KEY`.

## Modèles Pris en Charge

vLLM prend en charge un vaste éventail de modèles génératifs et de pooling via des implémentations natives ou le backend Hugging Face Transformers. Les catégories clés incluent :

- **Modèles de Langage Causaux** : Llama (3.1/3/2), Mistral, Gemma (2/3), Qwen, Phi (3/3.5), Mixtral, Falcon, BLOOM, GPT-NeoX/J/2, DeepSeek (V2/V3), InternLM (2/3), GLM (4/4.5), Command-R, DBRX, Yi, et plus.
- **Mixture-of-Experts (MoE)** : Mixtral, variantes MoE de DeepSeek-V2/V3, Granite MoE.
- **Multimodaux** : LLaVA (1.5/1.6/Next), Phi-3-Vision, Qwen2-VL, InternVL2, CogVLM, Llama-3.2-Vision.
- **Vision-Langage** : CLIP, SigLIP (pooling/embedding).
- **Autres** : Encodeur-décodeur (T5, BART), modèles de diffusion (Stable Diffusion), et architectures personnalisées comme Jamba, GritLM.

La prise en charge complète inclut les adaptateurs LoRA, le parallélisme de pipeline (PP) et la compatibilité moteur V1 pour la plupart. Pour la liste complète (plus de 100 architectures), consultez la [documentation des modèles pris en charge](https://docs.vllm.ai/en/stable/models/supported_models.html). Les modèles personnalisés peuvent être intégrés avec des modifications minimales.

## Options de Déploiement

### Déploiement Docker

Utilisez l'image officielle `vllm/vllm-openai` pour un service facile :

```
docker run --runtime nvidia --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" \
    -p 8000:8000 \
    --ipc=host \
    vllm/vllm-openai:latest \
    --model Qwen/Qwen2.5-1.5B-Instruct
```

- `--ipc=host` ou `--shm-size=8g` pour la mémoire partagée dans les configurations multi-GPU.
- Prend en charge Podman de manière similaire.
- Pour les images personnalisées : Construisez à partir des sources en utilisant `docker/Dockerfile` avec BuildKit :

  ```
  DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag vllm/custom --file docker/Dockerfile
  ```

- Builds Arm64/aarch64 : Utilisez `--platform linux/arm64` (expérimental ; nécessite PyTorch Nightly).
- Ajoutez des dépendances optionnelles (par ex., audio) ou Transformers depuis les sources dans un Dockerfile personnalisé.

Les autres options incluent Kubernetes, AWS SageMaker ou une intégration directe avec des frameworks comme Ray Serve.

## Optimisation des Performances

Pour optimiser le débit et la latence :

- **Sélection du GPU** : Utilisez A100/H100 pour un débit élevé ; mise à l'échelle avec le parallélisme de tenseur (`--tensor-parallel-size`).
- **Taille du Lot** : Définissez `--max-num-seqs` et `--max-model-len` en fonction du cache KV ; visez 80-90% d'utilisation du GPU.
- **Quantification** : Activez AWQ/GPTQ (`--quantization awq`) pour exécuter des modèles plus grands.
- **Backend d'Attention** : Préférez FlashInfer pour les GPU plus récents ; testez avec `VLLM_ATTENTION_BACKEND=FLASHINFER`.
- **Équilibre Pré-remplissage/Décodage** : Utilisez `--chunked-prefill-size` pour les entrées longues.
- **Benchmarking** : Exécutez `vllm benchmark` ou des jeux de données ShareGPT pour mesurer le TTFT (time-to-first-token) et le TPOT (time-per-output-token).
- **Meilleures Pratiques** :
  - Surveillez avec Prometheus/Grafana.
  - Pour les TPU : Utilisez le backend JAX ; ajustez le sharding.
  - Évitez le sur-parallélisme ; commencez avec un seul GPU et mettez à l'échelle.

Pour les configurations xPU détaillées, reportez-vous aux guides spécifiques au matériel.

## Utilisation Avancée

- **Service Distribué** : `--tensor-parallel-size N` pour multi-GPU ; combinez avec Ray pour les clusters.
- **LoRA** : Chargez les adaptateurs avec `--lora-modules`.
- **Décodage Spéculatif** : Intégrez avec Medusa pour des accélérations de 2x.
- **Kernels Personnalisés** : Étendez via des plugins pour nouveau matériel.
- **Surveillance** : Activez `--enable-chunked-prefill` et enregistrez les métriques.

Explorez le [guide utilisateur](https://docs.vllm.ai/en/stable/usage/) pour les moteurs et les intégrations.

## Références

- [Documentation Officielle de vLLM](https://docs.vllm.ai/)
- [Guide de Démarrage Rapide](https://docs.vllm.ai/en/stable/getting_started/quickstart.html)
- [Modèles Pris en Charge](https://docs.vllm.ai/en/stable/models/supported_models.html)
- [Déploiement Docker](https://docs.vllm.ai/en/stable/serving/deploying_with_docker.html)
- [Guide d'Optimisation des Performances vLLM (Google Cloud)](https://cloud.google.com/blog/topics/developers-practitioners/vllm-performance-tuning-the-ultimate-guide-to-xpu-inference-configuration)
- [Guide Ultime de vLLM (newline)](https://www.newline.co/@zaoyang/ultimate-guide-to-vllm--aad8b65d)
- [Tutoriel vLLM pour Débutants](https://www.designveloper.com/blog/vllm-tutorial/)