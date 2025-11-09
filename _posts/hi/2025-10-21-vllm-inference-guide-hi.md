---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: 'वीएलएलएम: फास्ट एलएलएम इन्फेरेंस गाइड'
translated: true
type: note
---

vLLM एक ओपन-सोर्स लाइब्रेरी है जो बड़े भाषा मॉडल (LLM) के तीव्र और मेमोरी-कुशल अनुमान (inference) और सर्विंग के लिए डिज़ाइन की गई है। इसे最初 में UC Berkeley के Sky Computing Lab में विकसित किया गया था, और अब यह एक community-driven प्रोजेक्ट बन गया है जिसमें academia और industry के योगदान शामिल हैं। vLLM, LLM डिप्लॉयमेंट में आने वाली मुख्य चुनौतियों, जैसे high latency, memory fragmentation और low throughput, को हल करता है, जिससे यह production environments के लिए आदर्श बन जाता है। यह Hugging Face मॉडल्स के साथ seamless integration को सपोर्ट करता है और आसान अपनाने के लिए एक OpenAI-संगत API प्रदान करता है।

## मुख्य विशेषताएं

vLLM अपने performance और flexibility के लिए जाना जाता है:
- **PagedAttention**: Key-value (KV) कैश मेमोरी को कुशलतापूर्वक प्रबंधित करके waste को कम करता है और higher throughput को सक्षम बनाता है।
- **Continuous Batching**: आने वाले requests को full batches का इंतज़ार किए बिना dynamically batch करता है, जिससे resource utilization में सुधार होता है।
- **Optimized Kernels**: तेज़ execution के लिए FlashAttention, FlashInfer और custom CUDA/HIP graphs को इंटीग्रेट करता है।
- **Quantization Support**: कम मेमोरी footprint के लिए GPTQ, AWQ, INT4/INT8/FP8 को शामिल करता है।
- **Decoding Algorithms**: Parallel sampling, beam search, speculative decoding, और chunked prefill को सपोर्ट करता है।
- **Distributed Inference**: Multi-GPU setups के लिए tensor, pipeline, data, और expert parallelism।
- **Hardware Compatibility**: NVIDIA GPUs, AMD/Intel CPUs/GPUs, PowerPC CPUs, TPUs, और Intel Gaudi, IBM Spyre, Huawei Ascend के लिए plugins।
- **Additional Tools**: Streaming outputs, prefix caching, multi-LoRA support, और एक OpenAI-संगत server।

ये features vLLM को state-of-the-art serving throughput हासिल करने में सक्षम बनाते हैं, साथ ही यह उपयोग में आसान है।

## पूर्वापेक्षाएँ

- **OS**: Linux (प्राथमिक सपोर्ट; अन्य प्लेटफॉर्म पर कुछ features)।
- **Python**: 3.9 से 3.13।
- **Hardware**: पूर्ण features के लिए NVIDIA GPUs की सिफारिश की जाती है; CPU-only mode उपलब्ध है लेकिन धीमा है।
- **Dependencies**: PyTorch (CUDA वर्जन के through auto-detected), Hugging Face Transformers।

## इंस्टालेशन

vLLM को pip के through इंस्टॉल किया जा सकता है। इष्टतम सेटअप के लिए `uv` (एक तेज़ Python environment manager) का उपयोग करें:

1. `uv` को उसके [documentation](https://docs.astral.sh/uv/getting-started/installation/) के अनुसार इंस्टॉल करें।
2. एक virtual environment बनाएं और vLLM इंस्टॉल करें:

   ```
   uv venv --python 3.12 --seed
   source .venv/bin/activate
   uv pip install vllm --torch-backend=auto
   ```

   - `--torch-backend=auto` आपके CUDA ड्राइवर के आधार पर PyTorch को auto-select करता है।
   - विशिष्ट backends (जैसे, CUDA 12.6) के लिए: `--torch-backend=cu126`।

वैकल्पिक रूप से, स्थायी environment के बिना one-off commands के लिए `uv run` का उपयोग करें:

   ```
   uv run --with vllm vllm --help
   ```

Conda उपयोगकर्ताओं के लिए:

   ```
   conda create -n myenv python=3.12 -y
   conda activate myenv
   pip install --upgrade uv
   uv pip install vllm --torch-backend=auto
   ```

गैर-NVIDIA setups (जैसे, AMD/Intel) के लिए, प्लेटफ़ॉर्म-विशिष्ट निर्देशों के लिए, जिसमें CPU-only builds शामिल हैं, [official installation guide](https://docs.vllm.ai/en/stable/getting_started/installation.html) देखें।

Attention backends (FLASH_ATTN, FLASHINFER, XFORMERS) auto-selected होते हैं; आवश्यकता पड़ने पर `VLLM_ATTENTION_BACKEND` environment variable के साथ override करें। नोट: FlashInfer के लिए manual installation की आवश्यकता होती है क्योंकि यह pre-built wheels में नहीं है।

## क्विक स्टार्ट

### ऑफ़लाइन बैच्ड इन्फ़रेंस

पाठ उत्पन्न करने के लिए vLLM का उपयोग करें। उदाहरण स्क्रिप्ट (`basic.py`):

```python
from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

llm = LLM(model="facebook/opt-125m")  # डिफ़ॉल्ट रूप से Hugging Face से डाउनलोड करता है
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

- **नोट्स**:
  - डिफ़ॉल्ट रूप से, sampling params के लिए मॉडल के `generation_config.json` का उपयोग करता है; `generation_config="vllm"` के साथ override करें।
  - चैट/इंस्ट्रक्ट मॉडल्स के लिए, chat templates को manually apply करें या `llm.chat(messages_list, sampling_params)` का उपयोग करें।
  - ModelScope मॉडल्स के लिए `VLLM_USE_MODELSCOPE=True` सेट करें।

### ऑनलाइन सर्विंग (OpenAI-संगत API)

एक सर्वर लॉन्च करें:

```
vllm serve Qwen/Qwen2.5-1.5B-Instruct
```

यह `http://localhost:8000` पर शुरू होता है। `--host` और `--port` के साथ कस्टमाइज़ करें।

curl के through query करें (completions endpoint):

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

या chat completions:

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

Python का उपयोग करते हुए (OpenAI client):

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

API key auth को `--api-key <key>` या `VLLM_API_KEY` के साथ सक्षम करें।

## समर्थित मॉडल

vLLM native implementations या Hugging Face Transformers backend के through जनरेटिव और पूलिंग मॉडल्स की एक विशाल श्रृंखला को सपोर्ट करता है। मुख्य श्रेणियों में शामिल हैं:

- **Causal Language Models**: Llama (3.1/3/2), Mistral, Gemma (2/3), Qwen, Phi (3/3.5), Mixtral, Falcon, BLOOM, GPT-NeoX/J/2, DeepSeek (V2/V3), InternLM (2/3), GLM (4/4.5), Command-R, DBRX, Yi, और अधिक।
- **Mixture-of-Experts (MoE)**: Mixtral, DeepSeek-V2/V3 MoE variants, Granite MoE।
- **Multimodal**: LLaVA (1.5/1.6/Next), Phi-3-Vision, Qwen2-VL, InternVL2, CogVLM, Llama-3.2-Vision।
- **Vision-Language**: CLIP, SigLIP (pooling/embedding)।
- **अन्य**: Encoder-decoder (T5, BART), diffusion models (Stable Diffusion), और custom architectures जैसे Jamba, GritLM।

पूर्ण सपोर्ट में अधिकांश के लिए LoRA adapters, pipeline parallelism (PP), और V1 engine compatibility शामिल है। पूरी सूची (100 से अधिक architectures) के लिए [supported models documentation](https://docs.vllm.ai/en/stable/models/supported_models.html) देखें। Custom मॉडल्स को minimal changes के साथ integrate किया जा सकता है।

## डिप्लॉयमेंट विकल्प

### Docker डिप्लॉयमेंट

आसान सर्विंग के लिए official `vllm/vllm-openai` image का उपयोग करें:

```
docker run --runtime nvidia --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" \
    -p 8000:8000 \
    --ipc=host \
    vllm/vllm-openai:latest \
    --model Qwen/Qwen2.5-1.5B-Instruct
```

- Multi-GPU setups में shared memory के लिए `--ipc=host` या `--shm-size=8g`।
- Podman को समान रूप से सपोर्ट करता है।
- Custom images के लिए: BuildKit का उपयोग करके `docker/Dockerfile` से source build करें:

  ```
  DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag vllm/custom --file docker/Dockerfile
  ```

- Arm64/aarch64 builds: `--platform linux/arm64` का उपयोग करें (experimental; PyTorch Nightly की आवश्यकता है)।
- एक custom Dockerfile में optional deps (जैसे, audio) या Transformers from source add करें।

अन्य विकल्पों में Kubernetes, AWS SageMaker, या Ray Serve जैसे frameworks के साथ direct integration शामिल है।

## परफॉर्मेंस ट्यूनिंग

Throughput और latency को optimize करने के लिए:

- **GPU Selection**: High throughput के लिए A100/H100 का उपयोग करें; tensor parallelism (`--tensor-parallel-size`) के साथ scale करें।
- **Batch Size**: KV cache के आधार पर `--max-num-seqs` और `--max-model-len` सेट करें; 80-90% GPU utilization का लक्ष्य रखें।
- **Quantization**: बड़े मॉडल्स को fit करने के लिए AWQ/GPTQ (`--quantization awq`) सक्षम करें।
- **Attention Backend**: नए GPUs के लिए FlashInfer को प्राथमिकता दें; `VLLM_ATTENTION_BACKEND=FLASHINFER` के साथ test करें।
- **Prefill/Decode Balance**: लंबे inputs के लिए `--chunked-prefill-size` का उपयोग करें।
- **Benchmarking**: TTFT (time-to-first-token) और TPOT (time-per-output-token) को मापने के लिए `vllm benchmark` या ShareGPT datasets चलाएं।
- **Best Practices**:
  - Prometheus/Grafana के साथ monitor करें।
  - TPUs के लिए: JAX backend का उपयोग करें; sharding को tune करें।
  - over-parallelism से बचें; single GPU से शुरू करें और scale करें।

विस्तृत xPU configs के लिए, hardware-specific guides देखें।

## एडवांस्ड उपयोग

- **Distributed Serving**: Multi-GPU के लिए `--tensor-parallel-size N`; clusters के लिए Ray के साथ combine करें।
- **LoRA**: `--lora-modules` के साथ adapters लोड करें।
- **Speculative Decoding**: 2x speedups के लिए Medusa के साथ integrate करें।
- **Custom Kernels**: नए hardware के लिए plugins के through extend करें।
- **Monitoring**: `--enable-chunked-prefill` सक्षम करें और metrics log करें।

Engines और integrations के लिए [user guide](https://docs.vllm.ai/en/stable/usage/) एक्सप्लोर करें।

## संदर्भ

- [vLLM Official Documentation](https://docs.vllm.ai/)
- [Quickstart Guide](https://docs.vllm.ai/en/stable/getting_started/quickstart.html)
- [Supported Models](https://docs.vllm.ai/en/stable/models/supported_models.html)
- [Docker Deployment](https://docs.vllm.ai/en/stable/serving/deploying_with_docker.html)
- [vLLM Performance Tuning Guide (Google Cloud)](https://cloud.google.com/blog/topics/developers-practitioners/vllm-performance-tuning-the-ultimate-guide-to-xpu-inference-configuration)
- [Ultimate Guide to vLLM (newline)](https://www.newline.co/@zaoyang/ultimate-guide-to-vllm--aad8b65d)
- [vLLM Tutorial for Beginners](https://www.designveloper.com/blog/vllm-tutorial/)