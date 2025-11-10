---
audio: false
generated: true
image: false
lang: ar
layout: post
title: أوضاع هجين DeepSeek V3.1
translated: true
type: note
---

إليك كيفية تعامل **واجهة برمجة تطبيقات DeepSeek V3.1** مع بنية الاستدلال الهجينة الجديدة الخاصة بها (وضعي "التفكير" مقابل "عدم التفكير"):

---

### نظرة عامة على تغييرات واجهة برمجة التطبيقات

#### 1. **نقطتا نهاية مختلفتان (وضعان)**

* **`deepseek-chat`** تتوافق مع **وضع عدم التفكير** — مُحسَّن للحصول على استجابات سريعة.
* **`deepseek-reasoner`** تتوافق مع **وضع التفكير** — مُصمَّم لمهام الاستدلال متعددة الخطط والأكثر تعمقًا.
  تعمل نقطتا النهاية الآن على نفس نموذج V3.1 مع نطاق سياق يصل إلى 128 ألف رمز. ([DeepSeek API Docs][1], [Data Science Dojo][2])

#### 2. **دعم سياق موسع**

* يدعم كلا الوضعين نطاق السياق الممتد البالغ 128 ألف رمز، وهو ترقية رئيسية تتيح التعامل مع مدخلات طويلة جدًا. ([DeepSeek API Docs][1], [Hugging Face][3])

#### 3. **تحسينات في التنسيق والإمكانيات**

* أصبح هناك دعم لتوافق **واجهة برمجة تطبيقات Anthropic**، مما يسهل دمج DeepSeek مع مكتبات العملاء ذات النمط المشابه لـ Anthropic. ([DeepSeek API Docs][1])
* هناك دعم لـ **استدعاء الوظائف الصارم** (في نسخة تجريبية)، مما يسمح باستدعاء أدوات أكثر متانة وتحققًا من خلال واجهة برمجة التطبيقات. ([DeepSeek API Docs][1])

#### 4. **التبديل عبر واجهة المستخدم مقابل الاستدعاء عبر واجهة برمجة التطبيقات**

* في واجهة المستخدم الخاصة بهم على الويب (زر "DeepThink")، يمكن للمستخدمين التبديل بين الوضعين بشكل تفاعلي.
* في **واجهة برمجة التطبيقات**، يجب عليك اختيار الوضع صراحةً عن طريق تعيين المعلمة `model` إما إلى `"deepseek-chat"` (لوضع عدم التفكير) أو `"deepseek-reasoner"` (لوضع التفكير). ([DeepSeek API Docs][1])

#### 5. **تحسينات أخرى**

* تم إدخال **المزيد من موارد واجهة برمجة التطبيقات** وتحسين تجربة المطور بشكل عام. ([DeepSeek API Docs][1])
* تم تحديث أداة الترميز (tokenizer) والقوالب (chat templates) الأساسية لدعم السلوك القائم على الوضع (مثل إدراج رمزي `` بشكل مناسب). ([Hugging Face][3])

---

### ملخص: ما الذي تغير — بدون جدول

* **تسمية جديدة**:

  * `deepseek-chat` → وضع عدم التفكير
  * `deepseek-reasoner` → وضع التفكير

* **بنية مشتركة**: كلا الوضعين مبنيان على نفس النموذج الذي يحتوي على 671 مليار معامل وبنطاق سياق طويل يصل إلى 128 ألف رمز.

* **خيارات دمج محسنة**:

  * يدعم واجهات برمجة تطبيقات ذات نمط Anthropic.
  * يقدم استدعاء وظائف صارم (نسخة تجريبية)، مما يتيح تفاعلات أدوات أكثر أمانًا تعتمد على مخططات (schemas).

* **تحديثات القوالب**: تستخدم واجهة برمجة التطبيقات الآن رموزًا خاصة (``) في المطالبات (prompts) للتمييز بين الوضعين، وقامت بتحديث منطق قوالب الدردشة.

* **تجربة المطور**: تشمل المنصة المزيد من الموارد، ووثائق محدثة، وعملية دمج أكثر سلاسة بشكل عام.

---

### مثال للاستخدام (Python/HTTP)

**وضع عدم التفكير (استجابات سريعة):**

```python
import openai  # or DeepSeek-compatible SDK
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role":"user","content":"Tell me a joke."}],
)
```

**وضع التفكير (استدلال أعمق):**

```python
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role":"user","content":"Explain why the sky is blue."}],
)
```

**استدعاء الوظائف (الوضع الصارم، نسخة تجريبية):**
يمكنك تعريف وظائف (أدوات) بمخططات JSON والسماح للنموذج باستدعائها، حيث تتلقى استدعاءات منظمة يمكنك تنفيذها وإعادة تغذيتها — رائع لبناء وكلاء مستقلين. ([DeepSeek API Docs][1], [Reddit][4], [apidog][5])

---

أعلمني إذا كنت تريد المساعدة في صياغة مطالب (prompts) لاستخدام الأدوات، أو التحسين للتكلفة أو السرعة، أو استكشاف واجهة التوافق مع Anthropic بمزيد من التفصيل!

[1]: https://api-docs.deepseek.com/news/news250821?utm_source=chatgpt.com "DeepSeek-V3.1 Release"
[2]: https://datasciencedojo.com/blog/deep-seek-v3-1/?utm_source=chatgpt.com "Deep Seek v3.1: The Next Leap in Open-Source Large ..."
[3]: https://huggingface.co/deepseek-ai/DeepSeek-V3.1?utm_source=chatgpt.com "deepseek-ai/DeepSeek-V3.1"
[4]: https://www.reddit.com/r/LocalLLaMA/comments/1munvj6/the_new_design_in_deepseek_v31/?utm_source=chatgpt.com "The new design in DeepSeek V3.1 : r/LocalLLaMA"
[5]: https://apidog.com/blog/deepseek-v3-1-api/?utm_source=chatgpt.com "How to Use DeepSeek-V3.1 API ?"