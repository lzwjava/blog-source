---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: 'vLLM: Schneller LLM-Inferenz-Leitfaden'
translated: true
type: note
---

vLLM ist eine Open-Source-Bibliothek für schnelle und speichereffiziente Inferenz und das Bereitstellen von Large Language Models (LLMs). Ursprünglich im Sky Computing Lab an der UC Berkeley entwickelt, hat es sich zu einem community-getriebenen Projekt mit Beiträgen aus Wissenschaft und Industrie weiterentwickelt. vLLM adressiert zentrale Herausforderungen beim Deployment von LLMs, wie hohe Latenz, Speicherfragmentierung und geringen Durchsatz, was es ideal für Produktionsumgebungen macht. Es unterstützt nahtlose Integration mit Hugging-Face-Modellen und bietet eine OpenAI-kompatible API für einfache Übernahme.

## Wichtige Funktionen

vLLM zeichnet sich durch seine Leistung und Flexibilität aus:
- **PagedAttention**: Verwaltet den Key-Value (KV) Cache-Speicher effizient, um Verschwendung zu reduzieren und höheren Durchsatz zu ermöglichen.
- **Continuous Batching**: Batching eingehender Anfragen dynamisch, ohne auf vollständige Batches zu warten, und verbessert so die Ressourcennutzung.
- **Optimierte Kernels**: Integriert FlashAttention, FlashInfer und benutzerdefinierte CUDA/HIP Graphs für schnellere Ausführung.
- **Quantisierungsunterstützung**: Enthält GPTQ, AWQ, INT4/INT8/FP8 für einen reduzierten Speicherbedarf.
- **Decodierungsalgorithmen**: Unterstützt paralleles Sampling, Beam Search, spekulative Decodierung und Chunked Prefill.
- **Verteilte Inferenz**: Tensor-, Pipeline-, Data- und Expert-Parallelismus für Multi-GPU-Setups.
- **Hardware-Kompatibilität**: NVIDIA GPUs, AMD/Intel CPUs/GPUs, PowerPC CPUs, TPUs und Plugins für Intel Gaudi, IBM Spyre, Huawei Ascend.
- **Zusätzliche Tools**: Streaming-Ausgaben, Prefix Caching, Multi-LoRA-Unterstützung und ein OpenAI-kompatibler Server.

Diese Funktionen ermöglichen es vLLM, state-of-the-art Serving-Durchsatz zu erreichen und dabei einfach zu bedienen zu sein.

## Voraussetzungen

- **Betriebssystem**: Linux (primäre Unterstützung; einige Funktionen auf anderen Plattformen).
- **Python**: 3.9 bis 3.13.
- **Hardware**: NVIDIA GPUs werden für alle Funktionen empfohlen; CPU-only-Modus verfügbar, aber langsamer.
- **Abhängigkeiten**: PyTorch (automatisch erkannt über CUDA-Version), Hugging Face Transformers.

## Installation

vLLM kann über pip installiert werden. Verwenden Sie `uv` (einen schnellen Python-Umgebungsmanager) für ein optimales Setup:

1. Installieren Sie `uv` gemäß seiner [Dokumentation](https://docs.astral.sh/uv/getting-started/installation/).
2. Erstellen Sie eine virtuelle Umgebung und installieren Sie vLLM:

   ```
   uv venv --python 3.12 --seed
   source .venv/bin/activate
   uv pip install vllm --torch-backend=auto
   ```

   - `--torch-backend=auto` wählt PyTorch automatisch basierend auf Ihrem CUDA-Treiber aus.
   - Für spezifische Backends (z.B. CUDA 12.6): `--torch-backend=cu126`.

Alternativ können Sie `uv run` für einmalige Befehle ohne permanente Umgebung verwenden:

   ```
   uv run --with vllm vllm --help
   ```

Für Conda-Benutzer:

   ```
   conda create -n myenv python=3.12 -y
   conda activate myenv
   pip install --upgrade uv
   uv pip install vllm --torch-backend=auto
   ```

Für Nicht-NVIDIA-Setups (z.B. AMD/Intel) lesen Sie die [offizielle Installationsanleitung](https://docs.vllm.ai/en/stable/getting_started/installation.html) für plattformspezifische Anweisungen, einschließlich CPU-only-Builds.

Attention-Backends (FLASH_ATTN, FLASHINFER, XFORMERS) werden automatisch ausgewählt; überschreiben Sie diese bei Bedarf mit der Umgebungsvariable `VLLM_ATTENTION_BACKEND`. Hinweis: FlashInfer erfordert eine manuelle Installation, da es nicht in vorgefertigten Wheels enthalten ist.

## Schnellstart

### Offline Batch-Inferenz

Verwenden Sie vLLM, um Text aus einer Liste von Prompts zu generieren. Beispielskript (`basic.py`):

```python
from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

llm = LLM(model="facebook/opt-125m")  # Lädt standardmäßig von Hugging Face herunter
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

- **Hinweise**:
  - Standardmäßig wird die `generation_config.json` des Modells für Sampling-Parameter verwendet; überschreiben mit `generation_config="vllm"`.
  - Für Chat/Instruct-Modelle wenden Sie Chat-Templates manuell an oder verwenden Sie `llm.chat(messages_list, sampling_params)`.
  - Setzen Sie `VLLM_USE_MODELSCOPE=True` für ModelScope-Modelle.

### Online-Serving (OpenAI-kompatible API)

Starten Sie einen Server mit:

```
vllm serve Qwen/Qwen2.5-1.5B-Instruct
```

Dies startet den Server unter `http://localhost:8000`. Passen Sie dies mit `--host` und `--port` an.

Abfrage per curl (Completions-Endpoint):

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

Oder Chat Completions:

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

Verwendung mit Python (OpenAI-Client):

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

Aktivieren Sie die API-Schlüssel-Authentifizierung mit `--api-key <key>` oder `VLLM_API_KEY`.

## Unterstützte Modelle

vLLM unterstützt eine Vielzahl von generativen und Pooling-Modellen über native Implementierungen oder das Hugging Face Transformers-Backend. Wichtige Kategorien umfassen:

- **Causal Language Models**: Llama (3.1/3/2), Mistral, Gemma (2/3), Qwen, Phi (3/3.5), Mixtral, Falcon, BLOOM, GPT-NeoX/J/2, DeepSeek (V2/V3), InternLM (2/3), GLM (4/4.5), Command-R, DBRX, Yi und mehr.
- **Mixture-of-Experts (MoE)**: Mixtral, DeepSeek-V2/V3 MoE-Varianten, Granite MoE.
- **Multimodal**: LLaVA (1.5/1.6/Next), Phi-3-Vision, Qwen2-VL, InternVL2, CogVLM, Llama-3.2-Vision.
- **Vision-Language**: CLIP, SigLIP (Pooling/Embedding).
- **Andere**: Encoder-Decoder (T5, BART), Diffusionsmodelle (Stable Diffusion) und benutzerdefinierte Architekturen wie Jamba, GritLM.

Die volle Unterstützung umfasst LoRA-Adapter, Pipeline-Parallelismus (PP) und V1-Engine-Kompatibilität für die meisten. Für die vollständige Liste (über 100 Architekturen) siehe die [Dokumentation zu unterstützten Modellen](https://docs.vllm.ai/en/stable/models/supported_models.html). Benutzerdefinierte Modelle können mit minimalen Änderungen integriert werden.

## Bereitstellungsoptionen

### Docker-Bereitstellung

Verwenden Sie das offizielle `vllm/vllm-openai` Image für einfaches Serving:

```
docker run --runtime nvidia --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" \
    -p 8000:8000 \
    --ipc=host \
    vllm/vllm-openai:latest \
    --model Qwen/Qwen2.5-1.5B-Instruct
```

- `--ipc=host` oder `--shm-size=8g` für Shared Memory in Multi-GPU-Setups.
- Unterstützt Podman ähnlich.
- Für benutzerdefinierte Images: Bauen Sie aus dem Quellcode mit `docker/Dockerfile` und BuildKit:

  ```
  DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag vllm/custom --file docker/Dockerfile
  ```

- Arm64/aarch64 Builds: Verwenden Sie `--platform linux/arm64` (experimentell; erfordert PyTorch Nightly).
- Fügen Sie optionale Abhängigkeiten (z.B. Audio) oder Transformers aus dem Quellcode in einer benutzerdefinierten Dockerfile hinzu.

Andere Optionen umfassen Kubernetes, AWS SageMaker oder direkte Integration mit Frameworks wie Ray Serve.

## Leistungsoptimierung

Um Durchsatz und Latenz zu optimieren:

- **GPU-Auswahl**: Verwenden Sie A100/H100 für hohen Durchsatz; skalieren Sie mit Tensor-Parallelismus (`--tensor-parallel-size`).
- **Batch-Größe**: Setzen Sie `--max-num-seqs` und `--max-model-len` basierend auf dem KV-Cache; streben Sie 80-90% GPU-Auslastung an.
- **Quantisierung**: Aktivieren Sie AWQ/GPTQ (`--quantization awq`), um größere Modelle unterzubringen.
- **Attention-Backend**: Bevorzugen Sie FlashInfer für neuere GPUs; testen Sie mit `VLLM_ATTENTION_BACKEND=FLASHINFER`.
- **Prefill/Decode-Balance**: Verwenden Sie `--chunked-prefill-size` für lange Eingaben.
- **Benchmarking**: Führen Sie `vllm benchmark` oder ShareGPT-Datensätze aus, um TTFT (Time-To-First-Token) und TPOT (Time-Per-Output-Token) zu messen.
- **Best Practices**:
  - Überwachen Sie mit Prometheus/Grafana.
  - Für TPUs: Verwenden Sie JAX-Backend; optimieren Sie Sharding.
  - Vermeiden Sie Over-Parallelismus; beginnen Sie mit einer einzelnen GPU und skalieren Sie.

Für detaillierte xPU-Konfigurationen lesen Sie die hardware-spezifischen Anleitungen.

## Erweiterte Verwendung

- **Verteiltes Serving**: `--tensor-parallel-size N` für Multi-GPU; kombinieren mit Ray für Cluster.
- **LoRA**: Laden Sie Adapter mit `--lora-modules`.
- **Spekulative Decodierung**: Integrieren Sie Medusa für 2x Geschwindigkeitssteigerungen.
- **Benutzerdefinierte Kernels**: Erweitern Sie über Plugins für neue Hardware.
- **Monitoring**: Aktivieren Sie `--enable-chunked-prefill` und protokollieren Sie Metriken.

Erkunden Sie den [Benutzerleitfaden](https://docs.vllm.ai/en/stable/usage/) für Engines und Integrationen.

## Referenzen

- [vLLM Offizielle Dokumentation](https://docs.vllm.ai/)
- [Schnellstart-Leitfaden](https://docs.vllm.ai/en/stable/getting_started/quickstart.html)
- [Unterstützte Modelle](https://docs.vllm.ai/en/stable/models/supported_models.html)
- [Docker-Bereitstellung](https://docs.vllm.ai/en/stable/serving/deploying_with_docker.html)
- [vLLM Leistungsoptimierungsleitfaden (Google Cloud)](https://cloud.google.com/blog/topics/developers-practitioners/vllm-performance-tuning-the-ultimate-guide-to-xpu-inference-configuration)
- [Ultimativer Leitfaden zu vLLM (newline)](https://www.newline.co/@zaoyang/ultimate-guide-to-vllm--aad8b65d)
- [vLLM Tutorial für Anfänger](https://www.designveloper.com/blog/vllm-tutorial/)