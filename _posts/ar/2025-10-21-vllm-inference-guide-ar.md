---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: دليل الاستدلال السريع للغة النماذج اللغوية الكبيرة باستخدام vLLM
translated: true
type: note
---

vLLM هي مكتبة مفتوحة المصدر مصممة لاستدلال وخدمة نماذج اللغة الكبيرة (LLMs) بشكل سريع وموفر للذاكرة. تم تطويرها في البداية في مختبر Sky Computing في جامعة كاليفورنيا، بيركلي، وقد نمت لتصبح مشروعًا يقوده المجتمع مع مساهمات من الأوساط الأكاديمية والصناعة. تعالج vLLM التحديات الرئيسية في نشر نماذج اللغة الكبيرة، مثل الكمون العالي، وتجزئة الذاكرة، والإنتاجية المنخفضة، مما يجعلها مثالية لبيئات الإنتاج. وهي تدعم التكامل السلس مع نماذج Hugging Face وتوفر واجهة برمجة تطبيقات (API) متوافقة مع OpenAI لتبني سهل.

## الميزات الرئيسية

تتميز vLLM بأدائها ومرونتها:
- **PagedAttention**: تدير ذاكرة التخزين المؤقت للمفتاح-القيمة (KV) بكفاءة لتقليل الهدر وتمكين إنتاجية أعلى.
- **التجميع المستمر**: يقوم بتجميع الطلبات الواردة ديناميكيًا دون انتظار تجميعات كاملة، مما يحسن استخدام الموارد.
- **النواة المُحسنة**: تدمج FlashAttention، وFlashInfer، ورسومات CUDA/HIP مخصصة لتنفيذ أسرع.
- **دعم التكميم**: تتضمن GPTQ، وAWQ، وINT4/INT8/FP8 لتقليل بصمة الذاكرة.
- **خوارزميات فك الترميز**: تدعم أخذ العينات المتوازي، والبحث الحزمي، وفك الترميز التخميني، وملء مسبق مجزأ.
- **الاستدلال الموزع**: توازي الموتر، وخط الأنابيب، والبيانات، والخبراء لإعدادات multi-GPU.
- **توافق الأجهزة**: بطاقات NVIDIA GPU، ووحدات AMD/Intel CPUs/GPUs، ووحدات PowerPC CPUs، ووحدات TPUs، وإضافات لـ Intel Gaudi، وIBM Spyre، وHuawei Ascend.
- **أدوات إضافية**: مخرجات متدفقة، تخزين مؤقت للبادئات، دعم multi-LoRA، وخادم متوافق مع OpenAI.

تمكن هذه الميزات vLLM من تحقيق أحدث إنتاجية في الخدمة مع سهولة الاستخدام.

## المتطلبات الأساسية

- **نظام التشغيل**: Linux (الدعم الأساسي؛ بعض الميزات على منصات أخرى).
- **Python**: 3.9 إلى 3.13.
- **الأجهزة**: يوصى بـ NVIDIA GPUs للحصول على الميزات الكاملة؛ يتوفر وضع CPU-only ولكنه أبطأ.
- **التبعيات**: PyTorch (يتم الكشف عنه تلقائيًا عبر إصدار CUDA)، Hugging Face Transformers.

## التثبيت

يمكن تثبيت vLLM عبر pip. استخدم `uv` (مدير بيئة Python سريع) للإعداد الأمثل:

1. قم بتثبيت `uv` باتباع [توثيقه](https://docs.astral.sh/uv/getting-started/installation/).
2. أنشئ بيئة افتراضية وقم بتثبيت vLLM:

   ```
   uv venv --python 3.12 --seed
   source .venv/bin/activate
   uv pip install vllm --torch-backend=auto
   ```

   - `--torch-backend=auto` يختار PyTorch تلقائيًا بناءً على برنامج تشغيل CUDA الخاص بك.
   - للواجهات الخلفية المحددة (مثل CUDA 12.6): `--torch-backend=cu126`.

بدلاً من ذلك، استخدم `uv run` للأوامر لمرة واحدة بدون بيئة دائمة:

   ```
   uv run --with vllm vllm --help
   ```

لمستخدمي Conda:

   ```
   conda create -n myenv python=3.12 -y
   conda activate myenv
   pip install --upgrade uv
   uv pip install vllm --torch-backend=auto
   ```

لإعدادات غير NVIDIA (مثل AMD/Intel)، راجع [دليل التثبيت الرسمي](https://docs.vllm.ai/en/stable/getting_started/installation.html) للحصول على تعليمات محددة للمنصة، بما في ذلك builds CPU-only.

يتم اختيار واجهات الاهتمام الخلفية (FLASH_ATTN, FLASHINFER, XFORMERS) تلقائيًا؛ تجاوز ذلك باستخدام متغير البيئة `VLLM_ATTENTION_BACKEND` إذا لزم الأمر. ملاحظة: يتطلب FlashInfer التثبيت اليدوي لأنه غير متوفر في العجلات المبنية مسبقًا.

## البدء السريع

### استدلال مجمع دون اتصال

استخدم vLLM لتوليد نص من قائمة المطالبات. نموذج نصي (`basic.py`):

```python
from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

llm = LLM(model="facebook/opt-125m")  # يقوم بالتحميل من Hugging Face افتراضيًا
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

- **ملاحظات**:
  - افتراضيًا، يستخدم `generation_config.json` الخاص بالنموذج لمعلمات أخذ العينات؛ تجاوز ذلك باستخدام `generation_config="vllm"`.
  - لنماذج الدردشة/التعليمات، قم بتطبيق قوالب الدردشة يدويًا أو استخدم `llm.chat(messages_list, sampling_params)`.
  - عيّن `VLLM_USE_MODELSCOPE=True` لنماذج ModelScope.

### الخدمة عبر الإنترنت (واجهة برمجة تطبيقات متوافقة مع OpenAI)

قم بتشغيل خادم باستخدام:

```
vllm serve Qwen/Qwen2.5-1.5B-Instruct
```

يبدأ هذا في `http://localhost:8000`. خصص باستخدام `--host` و `--port`.

استعلام عبر curl (نقطة نهاية الاكتمال):

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

أو اكتمالات الدردشة:

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

باستخدام Python (عميل OpenAI):

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

قم بتمكين مصادقة مفتاح API باستخدام `--api-key <key>` أو `VLLM_API_KEY`.

## النماذج المدعومة

تدعم vLLM مجموعة واسعة من النماذج التوليدية ونماذج التجميع عبر التطبيقات الأصلية أو الواجهة الخلفية لـ Hugging Face Transformers. تشمل الفئات الرئيسية:

- **نماذج اللغة السببية**: Llama (3.1/3/2), Mistral, Gemma (2/3), Qwen, Phi (3/3.5), Mixtral, Falcon, BLOOM, GPT-NeoX/J/2, DeepSeek (V2/V3), InternLM (2/3), GLM (4/4.5), Command-R, DBRX, Yi, والمزيد.
- **خليط الخبراء (MoE)**: Mixtral, DeepSeek-V2/V3 MoE variants, Granite MoE.
- **متعددة الوسائط**: LLaVA (1.5/1.6/Next), Phi-3-Vision, Qwen2-VL, InternVL2, CogVLM, Llama-3.2-Vision.
- **لغة-رؤية**: CLIP, SigLIP (تجميع/تضمين).
- **أخرى**: مشفر-فك تشفير (T5, BART), نماذج الانتشار (Stable Diffusion), وهندسات مخصصة مثل Jamba, GritLM.

يشمل الدعم الكامل محولات LoRA، وتوازي خط الأنابيب (PP)، وتوافق محرك V1 لمعظمها. للحصول على القائمة الكاملة (أكثر من 100 هيكل)، راجع [توثيق النماذج المدعومة](https://docs.vllm.ai/en/stable/models/supported_models.html). يمكن دمج النماذج المخصصة بإجراء تغييرات طفيفة.

## خيارات النشر

### النشر باستخدام Docker

استخدم صورة `vllm/vllm-openai` الرسمية للخدمة السهلة:

```
docker run --runtime nvidia --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" \
    -p 8000:8000 \
    --ipc=host \
    vllm/vllm-openai:latest \
    --model Qwen/Qwen2.5-1.5B-Instruct
```

- `--ipc=host` أو `--shm-size=8g` للذاكرة المشتركة في إعدادات multi-GPU.
- يدعم Podman بشكل مشابه.
- للصور المخصصة: أنشئ من المصدر باستخدام `docker/Dockerfile` مع BuildKit:

  ```
  DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag vllm/custom --file docker/Dockerfile
  ```

- builds Arm64/aarch64: استخدم `--platform linux/arm64` (تجريبي؛ يتطلب PyTorch Nightly).
- أضف تبعيات اختيارية (مثل الصوت) أو Transformers من المصدر في Dockerfile مخصص.

تشمل الخيارات الأخرى Kubernetes، أو AWS SageMaker، أو التكامل المباشر مع أطر عمل مثل Ray Serve.

## ضبط الأداء

لتحسين الإنتاجية والكمون:

- **اختيار GPU**: استخدم A100/H100 لإنتاجية عالية؛ قم بالتحجيم مع توازي الموتر (`--tensor-parallel-size`).
- **حجم الدفعة**: عيّن `--max-num-seqs` و `--max-model-len` بناءً على ذاكرة التخزين المؤقت KV؛ استهدف تحقيق استخدام GPU بنسبة 80-90%.
- **التكميم**: قم بتمكين AWQ/GPTQ (`--quantization awq`) لتناسب النماذج الأكبر.
- **واجهة الاهتمام الخلفية**: فضّل FlashInfer لبطاقات GPU الأحدث؛ اختبر باستخدام `VLLM_ATTENTION_BACKEND=FLASHINFER`.
- **توازن الملء المسبق/فك الترميز**: استخدم `--chunked-prefill-size` للمدخلات الطويلة.
- **المعايير**: قم بتشغيل `vllm benchmark` أو مجموعات بيانات ShareGPT لقياس TTFT (وقت الوصول إلى الرمز المميز الأول) و TPOT (الوقت لكل رمز مميز مخرج).
- **أفضل الممارسات**:
  - راقب باستخدام Prometheus/Grafana.
  - لـ TPUs: استخدم الواجهة الخلفية JAX؛ اضبط التقسيم.
  - تجاوز التوازي؛ ابدأ بـ GPU مفرد وقم بالتحجيم.

للحصول على تكوينات xPU مفصلة، راجع أدلة الأجهزة المحددة.

## استخدام متقدم

- **الخدمة الموزعة**: `--tensor-parallel-size N` لـ multi-GPU؛ ادمج مع Ray للعناقيد.
- **LoRA**: قم بتحميل المحولات باستخدام `--lora-modules`.
- **فك الترميز التخميني**: قم بالدمج مع Medusa لتسريع بمقدار 2x.
- **النواة المخصصة**: قم بالتوسيع عبر الإضافات للأجهزة الجديدة.
- **المراقبة**: قم بتمكين `--enable-chunked-prefill` وسجل المقاييس.

استكشف [دليل المستخدم](https://docs.vllm.ai/en/stable/usage/) للمحركات والتكاملات.

## المراجع

- [التوثيق الرسمي لـ vLLM](https://docs.vllm.ai/)
- [دليل البدء السريع](https://docs.vllm.ai/en/stable/getting_started/quickstart.html)
- [النماذج المدعومة](https://docs.vllm.ai/en/stable/models/supported_models.html)
- [النشر باستخدام Docker](https://docs.vllm.ai/en/stable/serving/deploying_with_docker.html)
- [دليل ضبط أداء vLLM (Google Cloud)](https://cloud.google.com/blog/topics/developers-practitioners/vllm-performance-tuning-the-ultimate-guide-to-xpu-inference-configuration)
- [الدليل النهائي لـ vLLM (newline)](https://www.newline.co/@zaoyang/ultimate-guide-to-vllm--aad8b65d)
- [برنامج تعليمي لـ vLLM للمبتدئين](https://www.designveloper.com/blog/vllm-tutorial/)