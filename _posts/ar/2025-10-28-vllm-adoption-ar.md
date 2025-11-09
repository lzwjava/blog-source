---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: اعتماد مزودي الذكاء الاصطناعي لتقنية vLLM
translated: true
type: note
---

### استخدام vLLM من قبل مقدمي خدمات الذكاء الاصطناعي

vLLM هو محرك استدلال مفتوح المصدر يُوصى به عادةً لتقديم النماذج مفتوحة الأوزان بكفاءة. ومع ذلك، يختلف اعتماده في الخدمات الإنتاجية. فيما يلي تفصيل بناءً على المعلومات المتاحة:

| المزود/النموذج | هل يستخدم vLLM في الإنتاج؟ | التفاصيل |
|---------------|---------------------------|---------|
| **Claude (من Anthropic)** | لا | تعتمد Anthropic على بنية تحتية احتكارية لتقديم نماذج Claude. يوفر vLLM توافقًا للنشر المحلي أو من طرف ثالث يحاكي واجهة برمجة تطبيقات Anthropic، ولكن لا يوجد دليل على الاستخدام الداخلي له. |
| **OpenAI (نماذج GPT)** | لا | تستخدم OpenAI أنظمة تقديم مخصصة وداخلية مُحسنة للحجم الكبير. يدعم vLLM واجهات برمجة تطبيقات متوافقة مع OpenAI للاستدلال المحلي، ولكن OpenAI لا تعتمد على vLLM في إنتاجها. |
| **Minimax AI** | لا | تفتح MiniMax المصدر للنماذج مثل MiniMax-M1/M2 وتوصي باستخدام vLLM لنشر المستخدمين due إلى أدائه. لا يوجد تأكيد على استخدام vLLM في واجهة برمجة التطبيقات الإنتاجية الأساسية الخاصة بهم؛ قد يستخدمون نسخًا مشتقة أو إعدادات مخصصة. |
| **Kimi (من Moonshot AI)** | لا | توصي Moonshot باستخدام vLLM للاستضافة الذاتية لنموذج Kimi-K2، وأداة Checkpoint-Engine الخاصة بهم تندمج معه لتحديث الأوزان. ومع ذلك، من المرجح أن يستخدم الاستدلال الإنتاجي الخاص بهم تحسينات احتكارية إلى جانب محركات مثل SGLang أو TensorRT-LLM. |
| **DeepSeek AI** | نعم | قامت DeepSeek بفتح مصدر محرك استدلال مخصص مبني مباشرة على vLLM، مُدمجًا مع تحسينات من أبحاثهم. يُستخدم هذا للموديلات مثل DeepSeek-V3 و R1، مع مساهمات تعود إلى مشروع vLLM. |

### المراجع
- [DeepSeek تفتح مصدر محرك استدلال مخصص مبني على vLLM](https://www.ainews.com/p/deepseek-open-sources-custom-inference-engine-built-on-vllm)
- [الطريق إلى فتح مصدر محرك الاستدلال DeepSeek](https://news.ycombinator.com/item?id=43682088)
- [هندسة MiniMax-M1 الهجينة تلتقي مع vLLM](https://blog.vllm.ai/2025/06/30/minimax-m1.html)
- [Kimi K2: الذكاء الوكيلي المفتوح](https://moonshotai.github.io/Kimi-K2/)
- [خادم متوافق مع OpenAI - vLLM](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html)
- [دعم نقطة نهاية واجهة برمجة تطبيقات Anthropic `/v1/messages` · Issue #21313 · vllm-project/vllm](https://github.com/vllm-project/vllm/issues/21313)