---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 高速LLM推論ガイド vLLM
translated: true
type: note
---

vLLMは、大規模言語モデル(LLM)の推論とサービス提供を高速かつメモリ効率的に行うために設計されたオープンソースライブラリです。UCバークレーのSky Computing Labで最初に開発され、学界と産業界の貢献を通じてコミュニティ主導のプロジェクトへと成長しました。vLLMは、高レイテンシ、メモリの断片化、低スループットといったLLM導入における主要な課題に対処し、本番環境に最適です。Hugging Faceモデルとのシームレスな統合をサポートし、導入を容易にするOpenAI互換APIを提供します。

## 主な特徴

vLLMはそのパフォーマンスと柔軟性で際立っています：
- **PagedAttention**: キー値(KV)キャッシュメモリを効率的に管理し、無駄を削減して高いスループットを実現
- **Continuous Batching**: 完全なバッチを待たずに着信リクエストを動的にバッチ処理し、リソース利用率を向上
- **最適化されたカーネル**: FlashAttention、FlashInfer、カスタムCUDA/HIPグラフを統合して高速実行を実現
- **量子化サポート**: GPTQ、AWQ、INT4/INT8/FP8を含み、メモリ使用量を削減
- **デコードアルゴリズム**: 並列サンプリング、ビームサーチ、投機的デコード、チャンク化プレフィルをサポート
- **分散推論**: マルチGPU設定向けにテンソル、パイプライン、データ、エキスパート並列処理
- **ハードウェア互換性**: NVIDIA GPU、AMD/Intel CPU/GPU、PowerPC CPU、TPU、およびIntel Gaudi、IBM Spyre、Huawei Ascend向けプラグイン
- **追加ツール**: ストリーミング出力、プレフィックスキャッシング、マルチLoRAサポート、OpenAI互換サーバー

これらの特徴により、vLLMは使いやすさを保ちながら最先端のサービス提供スループットを達成できます。

## 前提条件

- **OS**: Linux（主要サポート；他のプラットフォームでは一部機能）
- **Python**: 3.9から3.13
- **ハードウェア**: 全機能にはNVIDIA GPU推奨；CPU専用モード利用可能だが低速
- **依存関係**: PyTorch（CUDAバージョン経由で自動検出）、Hugging Face Transformers

## インストール

vLLMはpip経由でインストールできます。最適な設定には`uv`（高速Python環境マネージャー）を使用：

1. [ドキュメント](https://docs.astral.sh/uv/getting-started/installation/)に従って`uv`をインストール
2. 仮想環境を作成しvLLMをインストール：

   ```
   uv venv --python 3.12 --seed
   source .venv/bin/activate
   uv pip install vllm --torch-backend=auto
   ```

   - `--torch-backend=auto`はCUDAドライバーに基づいてPyTorchを自動選択
   - 特定のバックエンド（例：CUDA 12.6）の場合：`--torch-backend=cu126`

代替として、永続的な環境なしで一時的なコマンド実行に`uv run`を使用：

   ```
   uv run --with vllm vllm --help
   ```

Condaユーザー向け：

   ```
   conda create -n myenv python=3.12 -y
   conda activate myenv
   pip install --upgrade uv
   uv pip install vllm --torch-backend=auto
   ```

非NVIDIA設定（例：AMD/Intel）の場合、プラットフォーム固有の手順については[公式インストールガイド](https://docs.vllm.ai/en/stable/getting_started/installation.html)を参照（CPU専用ビルドを含む）。

アテンションバックエンド（FLASH_ATTN、FLASHINFER、XFORMERS）は自動選択；必要に応じて`VLLM_ATTENTION_BACKEND`環境変数で上書き。注：FlashInferは事前ビルド済みホイールに含まれないため手動インストールが必要。

## クイックスタート

### オフラインバッチ推論

プロンプトリストからテキスト生成するvLLMの使用例。サンプルスクリプト（`basic.py`）：

```python
from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

llm = LLM(model="facebook/opt-125m")  # デフォルトでHugging Faceからダウンロード
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

- **注記**:
  - デフォルトではサンプリングパラメータにモデルの`generation_config.json`を使用；`generation_config="vllm"`で上書き
  - チャット/指示モデルの場合、チャットテンプレートを手動で適用するか`llm.chat(messages_list, sampling_params)`を使用
  - ModelScopeモデルの場合は`VLLM_USE_MODELSCOPE=True`を設定

### オンラインサービス（OpenAI互換API）

サーバー起動：

```
vllm serve Qwen/Qwen2.5-1.5B-Instruct
```

これは`http://localhost:8000`で開始。`--host`と`--port`でカスタマイズ可能。

curl経由でのクエリ（completionsエンドポイント）：

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

またはチャットcompletions：

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

Python（OpenAIクライアント）を使用：

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

APIキー認証を有効にするには`--api-key <key>`または`VLLM_API_KEY`を使用。

## サポートモデル

vLLMは、ネイティブ実装またはHugging Face Transformersバックエンド経由で、多数の生成モデルとプーリングモデルをサポートします。主要カテゴリ：

- **因果言語モデル**: Llama（3.1/3/2）、Mistral、Gemma（2/3）、Qwen、Phi（3/3.5）、Mixtral、Falcon、BLOOM、GPT-NeoX/J/2、DeepSeek（V2/V3）、InternLM（2/3）、GLM（4/4.5）、Command-R、DBRX、Yiなど
- **Mixture-of-Experts（MoE）**: Mixtral、DeepSeek-V2/V3 MoE変種、Granite MoE
- **マルチモーダル**: LLaVA（1.5/1.6/Next）、Phi-3-Vision、Qwen2-VL、InternVL2、CogVLM、Llama-3.2-Vision
- **ビジョン言語**: CLIP、SigLIP（プーリング/埋め込み）
- **その他**: エンコーダーデコーダー（T5、BART）、拡散モデル（Stable Diffusion）、Jamba、GritLMなどのカスタムアーキテクチャ

完全なサポートには、ほとんどのモデルでLoRAアダプター、パイプライン並列処理（PP）、V1エンジン互換性が含まれます。完全なリスト（100以上のアーキテクチャ）については、[サポートモデルドキュメント](https://docs.vllm.ai/en/stable/models/supported_models.html)を参照。カスタムモデルは最小限の変更で統合可能。

## デプロイオプション

### Dockerデプロイ

公式`vllm/vllm-openai`イメージを使用した簡単なサービス提供：

```
docker run --runtime nvidia --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" \
    -p 8000:8000 \
    --ipc=host \
    vllm/vllm-openai:latest \
    --model Qwen/Qwen2.5-1.5B-Instruct
```

- マルチGPU設定での共有メモリには`--ipc=host`または`--shm-size=8g`
- Podmanも同様にサポート
- カスタムイメージの場合：BuildKitを使用してソースからビルド：

  ```
  DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag vllm/custom --file docker/Dockerfile
  ```

- Arm64/aarch64ビルド：`--platform linux/arm64`を使用（実験的；PyTorch Nightlyが必要）
- カスタムDockerfileでオプション依存関係（例：オーディオ）やソースからのTransformersを追加

その他のオプションには、Kubernetes、AWS SageMaker、Ray Serveなどのフレームワークとの直接統合が含まれます。

## パフォーマンスチューニング

スループットとレイテンシを最適化するには：

- **GPU選択**: 高スループットにはA100/H100を使用；テンソル並列処理（`--tensor-parallel-size`）でスケール
- **バッチサイズ**: KVキャッシュに基づいて`--max-num-seqs`と`--max-model-len`を設定；GPU使用率80-90%を目標
- **量子化**: AWQ/GPTQ（`--quantization awq`）を有効化してより大きなモデルを適合
- **アテンションバックエンド**: 新しいGPUにはFlashInferを優先；`VLLM_ATTENTION_BACKEND=FLASHINFER`でテスト
- **プレフィル/デコードバランス**: 長い入力には`--chunked-prefill-size`を使用
- **ベンチマーク**: `vllm benchmark`またはShareGPTデータセットを実行してTTFT（最初のトークンまでの時間）とTPOT（出力トークンごとの時間）を測定
- **ベストプラクティス**:
  - Prometheus/Grafanaで監視
  - TPUの場合：JAXバックエンドを使用；シャーディングを調整
  - 過剰な並列処理を避け；単一GPUから開始してスケール

詳細なxPU設定については、ハードウェア固有のガイドを参照。

## 高度な使用方法

- **分散サービス**: マルチGPUに`--tensor-parallel-size N`；クラスターにはRayと組み合わせ
- **LoRA**: `--lora-modules`でアダプターをロード
- **投機的デコード**: Medusaと統合して2倍の高速化
- **カスタムカーネル**: 新しいハードウェア向けにプラグイン経由で拡張
- **監視**: `--enable-chunked-prefill`を有効化しメトリクスをログ

エンジン、エンジン、統合については[ユーザーガイド](https://docs.vllm.ai/en/stable/usage/)を探索。

## 参考文献

- [vLLM公式ドキュメント](https://docs.vllm.ai/)
- [クイックスタートガイド](https://docs.vllm.ai/en/stable/getting_started/quickstart.html)
- [サポートモデル](https://docs.vllm.ai/en/stable/models/supported_models.html)
- [Dockerデプロイ](https://docs.vllm.ai/en/stable/serving/deploying_with_docker.html)
- [vLLMパフォーマンスチューニングガイド（Google Cloud）](https://cloud.google.com/blog/topics/developers-practitioners/vllm-performance-tuning-the-ultimate-guide-to-xpu-inference-configuration)
- [vLLM究極ガイド（newline）](https://www.newline.co/@zaoyang/ultimate-guide-to-vllm--aad8b65d)
- [vLLM初心者向けチュートリアル](https://www.designveloper.com/blog/vllm-tutorial/)