---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إصلاح توجيه إعدادات كود كلود ديب سيك
translated: true
type: note
---

فهمتك. إعداداتك تُرسل **حركة مراسلات Claude Code ذات النمط الأنثروبي** إلى **نقطة النهاية ذات النمط المشابه لـ OpenAI في OpenRouter** من أجل DeepSeek V3.1. عندما يحاول Claude Code (وكيل بيئة التطوير) استخدام الأدوات / التخطيط / البث، فإن مخطط الرسالة لا يتطابق → مما يؤدي إلى أخطاء.

أدناه طريقة نظيفة لربطها بحيث تظل **نماذج Anthropic** تستخدم بوابة ذات نمط Anthropic، بينما يبقى **DeepSeek V3.1** (ذو النمط المشابه لـ OpenAI) على `/chat/completions`. سأعرض لك التعديلات الدقيقة التي يمكنك لصقها.

---

### 1) التحقق من معرف (slug) نموذج DeepSeek V3.1

معرف نموذج المحادثة على OpenRouter هو:

```
deepseek/deepseek-chat-v3.1
```

(هذا هو نموذج التعليمات/المحادثة - متميز عن النموذج "الأساسي"). ([OpenRouter][1])

---

### 2) إضافة وكيل (proxy) بتنسيق Anthropic لـ Claude Code

يتوقع Claude Code **رسائل Anthropic** (`/messages`، كتل `tool_use`). أبسط حل هو تشغيل وكيل صغير يحول من تنسيق Anthropic إلى OpenAI (OpenRouter) والعكس. يوجد واحد جاهز: **maxnowack/anthropic-proxy**. ابدأ تشغيله بهذه الطريقة (المتغير البيئي هو مفتاح OpenRouter الخاص بك):

```bash
OPENROUTER_API_KEY=YOUR_KEY npx anthropic-proxy
```

سيستمع محليًا ويقوم بتحويل المخططات نيابة عنك. ([GitHub][2])

الآن، أضف **مزودًا ثانيًا** يشير حركة مرور Claude Code إلى ذلك الوكيل.

#### 🔧 استبدل JSON الخاص بك بهذه التغييرات المركزة

**أضف هذا المزود (احتفظ بمزود `openrouter` الحالي كما هو):**

```json
{
  "name": "anthropic-proxy",
  "api_base_url": "http://127.0.0.1:3000/v1/messages",
  "api_key": "", 
  "models": [
    "anthropic/claude-sonnet-4",
    "anthropic/claude-3.5-sonnet",
    "anthropic/claude-3.7-sonnet:thinking",
    "anthropic/claude-opus-4"
  ]
}
```

**احتفظ بمزود OpenRouter الحالي الخاص بك (من الصحيح استخدام `/chat/completions` لـ DeepSeek ونماذج OpenAI-schema الأخرى).** يقوم OpenRouter بتطبيع المخطط ليكون متوافقًا مع OpenAI ويدعم إضافات مثل رموز التفكير (reasoning tokens)، والأدوات، إلخ. ([OpenRouter][3])

---

### 3) توجيه النماذج إلى المزود الصحيح

وجّه نماذج Anthropic إلى **anthropic-proxy**؛ ووجّه DeepSeek/GPT/Gemini/Qwen إلى **openrouter**.

مثال لكتلة Router يمكنك إضافتها:

```json
"Router": {
  "default": "openrouter,openai/gpt-5-mini",

  "background": "openrouter,google/gemini-2.5-flash",
  "think": "openrouter,qwen/qwen3-coder",
  "longContext": "openrouter,moonshotai/kimi-k2",
  "longContextThreshold": 2000,
  "webSearch": "openrouter,mistralai/mistral-medium-3.1",

  "overrides": {
    "anthropic/claude-sonnet-4": "anthropic-proxy,anthropic/claude-sonnet-4",
    "anthropic/claude-3.5-sonnet": "anthropic-proxy,anthropic/claude-3.5-sonnet",
    "anthropic/claude-3.7-sonnet:thinking": "anthropic-proxy,anthropic/claude-3.7-sonnet:thinking",
    "anthropic/claude-opus-4": "anthropic-proxy,anthropic/claude-opus-4",

    "deepseek/deepseek-chat-v3.1": "openrouter,deepseek/deepseek-chat-v3.1"
  }
}
```

> إذا كان جهاز التوجيه (router) الخاص بك لا يدعم خريطة `overrides`، فإن المكافئ هو: إنشاء "ملفات تعريف" منفصلة في تطبيقك (على سبيل المثال، "Claude Code via anthropic-proxy" مقابل "General chat via openrouter") واختر الملف الشخصي المناسب لكل إجراء.

---

### 4) تجنب تعارضات تدفق التفكير (reasoning stream) على DeepSeek (اختياري ولكنه أكثر أمانًا)

يدعم DeepSeek V3.1 **رموز "التفكير" (thinking tokens)**. العديد من الـ wrappers تواجه مشاكل إذا ظهرت هذه الرموز في منتصف التدفق. على OpenRouter، يمكنك **استبعاد التفكير** باستخدام علم طلب (request flag). إذا كان جهاز التوجيه الخاص بك يسمح لك بتعيين معلمات لكل نموذج، فقم بإرفاق:

```json
"params": {
  "reasoning": { "exclude": true }
}
```

(أو `include_reasoning: false` اعتمادًا على تسمية المعلمات في جهاز التوجيه الخاص بك). هذا يمنع محتوى `