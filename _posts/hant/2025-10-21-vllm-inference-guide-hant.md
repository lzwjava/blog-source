---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: vLLM：快速LLM推論指南
translated: true
type: note
---

vLLM 是一個專為大型語言模型（LLM）提供快速且記憶體高效能推理與服務的開源函式庫。最初由加州大學柏克萊分校的 Sky Computing Lab 開發，現已發展成由學術界和產業界共同貢獻的社群驅動專案。vLLM 解決了 LLM 部署中的關鍵挑戰，例如高延遲、記憶體碎片化和低吞吐量，使其成為生產環境的理想選擇。它支援與 Hugging Face 模型的無縫整合，並提供與 OpenAI 相容的 API 以便輕鬆採用。

## 主要功能

vLLM 以其效能和靈活性脫穎而出：
- **PagedAttention**：高效管理鍵值（KV）快取記憶體，減少浪費並實現更高吞吐量。
- **連續批次處理**：動態批次處理傳入請求，無需等待完整批次，提升資源利用率。
- **最佳化核心**：整合 FlashAttention、FlashInfer 和自訂 CUDA/HIP 圖以加速執行。
- **量化支援**：包含 GPTQ、AWQ、INT4/INT8/FP8，以減少記憶體佔用。
- **解碼演算法**：支援平行取樣、波束搜尋、推測解碼和分塊預填充。
- **分散式推理**：支援張量、管道、資料和專家平行處理，適用於多 GPU 設定。
- **硬體相容性**：NVIDIA GPU、AMD/Intel CPU/GPU、PowerPC CPU、TPU，以及 Intel Gaudi、IBM Spyre、華為 Ascend 的外掛程式。
- **額外工具**：串流輸出、前綴快取、多 LoRA 支援，以及與 OpenAI 相容的伺服器。

這些功能使 vLLM 能夠實現最先進的服務吞吐量，同時易於使用。

## 先決條件

- **作業系統**：Linux（主要支援；其他平台部分功能可用）。
- **Python**：3.9 至 3.13。
- **硬體**：建議使用 NVIDIA GPU 以獲得完整功能；僅 CPU 模式可用但速度較慢。
- **相依性**：PyTorch（透過 CUDA 版本自動偵測）、Hugging Face Transformers。

## 安裝

vLLM 可透過 pip 安裝。使用 `uv`（一個快速的 Python 環境管理員）以獲得最佳設定：

1. 按照其[文件](https://docs.astral.sh/uv/getting-started/installation/)安裝 `uv`。
2. 建立虛擬環境並安裝 vLLM：

   ```
   uv venv --python 3.12 --seed
   source .venv/bin/activate
   uv pip install vllm --torch-backend=auto
   ```

   - `--torch-backend=auto` 會根據您的 CUDA 驅動程式自動選擇 PyTorch。
   - 對於特定後端（例如 CUDA 12.6）：`--torch-backend=cu126`。

或者，使用 `uv run` 執行一次性指令而無需永久環境：

   ```
   uv run --with vllm vllm --help
   ```

對於 Conda 使用者：

   ```
   conda create -n myenv python=3.12 -y
   conda activate myenv
   pip install --upgrade uv
   uv pip install vllm --torch-backend=auto
   ```

對於非 NVIDIA 設定（例如 AMD/Intel），請參考[官方安裝指南](https://docs.vllm.ai/en/stable/getting_started/installation.html)以取得平台特定說明，包括僅 CPU 版本。

注意力後端（FLASH_ATTN、FLASHINFER、XFORMERS）會自動選擇；如有需要，可使用 `VLLM_ATTENTION_BACKEND` 環境變數覆寫。注意：FlashInfer 需要手動安裝，因為它不在預先建置的輪子中。

## 快速開始

### 離線批次推理

使用 vLLM 從提示列表中生成文字。範例指令碼（`basic.py`）：

```python
from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

llm = LLM(model="facebook/opt-125m")  # 預設從 Hugging Face 下載
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

- **注意事項**：
  - 預設使用模型的 `generation_config.json` 進行取樣參數設定；可使用 `generation_config="vllm"` 覆寫。
  - 對於聊天/指導模型，手動應用聊天模板或使用 `llm.chat(messages_list, sampling_params)`。
  - 對於 ModelScope 模型，設定 `VLLM_USE_MODELSCOPE=True`。

### 線上服務（OpenAI 相容 API）

啟動伺服器：

```
vllm serve Qwen/Qwen2.5-1.5B-Instruct
```

這將在 `http://localhost:8000` 啟動。使用 `--host` 和 `--port` 自訂。

透過 curl 查詢（completions 端點）：

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

或聊天 completions：

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

使用 Python（OpenAI 客戶端）：

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

使用 `--api-key <key>` 或 `VLLM_API_KEY` 啟用 API 金鑰驗證。

## 支援的模型

vLLM 透過原生實作或 Hugging Face Transformers 後端支援多種生成和池化模型。主要類別包括：

- **因果語言模型**：Llama (3.1/3/2)、Mistral、Gemma (2/3)、Qwen、Phi (3/3.5)、Mixtral、Falcon、BLOOM、GPT-NeoX/J/2、DeepSeek (V2/V3)、InternLM (2/3)、GLM (4/4.5)、Command-R、DBRX、Yi 等。
- **專家混合模型（MoE）**：Mixtral、DeepSeek-V2/V3 MoE 變體、Granite MoE。
- **多模態模型**：LLaVA (1.5/1.6/Next)、Phi-3-Vision、Qwen2-VL、InternVL2、CogVLM、Llama-3.2-Vision。
- **視覺語言模型**：CLIP、SigLIP（池化/嵌入）。
- **其他**：編碼器-解碼器（T5、BART）、擴散模型（Stable Diffusion），以及自訂架構如 Jamba、GritLM。

完整支援包括 LoRA 適配器、管道平行處理（PP）和 V1 引擎相容性。有關完整列表（超過 100 種架構），請參閱[支援模型文件](https://docs.vllm.ai/en/stable/models/supported_models.html)。自訂模型可以透過最小變更進行整合。

## 部署選項

### Docker 部署

使用官方 `vllm/vllm-openai` 映像進行簡易服務：

```
docker run --runtime nvidia --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" \
    -p 8000:8000 \
    --ipc=host \
    vllm/vllm-openai:latest \
    --model Qwen/Qwen2.5-1.5B-Instruct
```

- 在多 GPU 設定中使用 `--ipc=host` 或 `--shm-size=8g` 以獲得共享記憶體。
- 類似支援 Podman。
- 對於自訂映像：使用 BuildKit 從原始碼建置：

  ```
  DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag vllm/custom --file docker/Dockerfile
  ```

- Arm64/aarch64 建置：使用 `--platform linux/arm64`（實驗性；需要 PyTorch Nightly）。
- 在自訂 Dockerfile 中新增選用依賴項（例如音訊）或從原始碼安裝 Transformers。

其他選項包括 Kubernetes、AWS SageMaker 或直接與框架（如 Ray Serve）整合。

## 效能調校

為了最佳化吞吐量和延遲：

- **GPU 選擇**：使用 A100/H100 以獲得高吞吐量；透過張量平行處理（`--tensor-parallel-size`）進行擴展。
- **批次大小**：根據 KV 快取設定 `--max-num-seqs` 和 `--max-model-len`；目標為 80-90% GPU 使用率。
- **量化**：啟用 AWQ/GPTQ（`--quantization awq`）以容納更大模型。
- **注意力後端**：對於較新的 GPU 優先使用 FlashInfer；使用 `VLLM_ATTENTION_BACKEND=FLASHINFER` 進行測試。
- **預填充/解碼平衡**：對於長輸入使用 `--chunked-prefill-size`。
- **基準測試**：執行 `vllm benchmark` 或 ShareGPT 資料集以測量 TTFT（首個令牌時間）和 TPOT（每個輸出令牌時間）。
- **最佳實踐**：
  - 使用 Prometheus/Grafana 進行監控。
  - 對於 TPU：使用 JAX 後端；調整分片。
  - 避免過度平行處理；從單一 GPU 開始並擴展。

有關詳細的 xPU 配置，請參考硬體特定指南。

## 進階用法

- **分散式服務**：使用 `--tensor-parallel-size N` 進行多 GPU 設定；與 Ray 結合以用於叢集。
- **LoRA**：使用 `--lora-modules` 載入適配器。
- **推測解碼**：與 Medusa 整合以實現 2 倍加速。
- **自訂核心**：透過外掛程式擴展以支援新硬體。
- **監控**：啟用 `--enable-chunked-prefill` 並記錄指標。

探索[使用者指南](https://docs.vllm.ai/en/stable/usage/)以了解引擎和整合。

## 參考資料

- [vLLM 官方文件](https://docs.vllm.ai/)
- [快速開始指南](https://docs.vllm.ai/en/stable/getting_started/quickstart.html)
- [支援的模型](https://docs.vllm.ai/en/stable/models/supported_models.html)
- [Docker 部署](https://docs.vllm.ai/en/stable/serving/deploying_with_docker.html)
- [vLLM 效能調校指南（Google Cloud）](https://cloud.google.com/blog/topics/developers-practitioners/vllm-performance-tuning-the-ultimate-guide-to-xpu-inference-configuration)
- [vLLM 終極指南（newline）](https://www.newline.co/@zaoyang/ultimate-guide-to-vllm--aad8b65d)
- [vLLM 初學者教程](https://www.designveloper.com/blog/vllm-tutorial/)