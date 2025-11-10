---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إصلاح تعارضات أداة ديب سيك
translated: true
type: note
---

أنت تواجه **خطأ في التحقق من استدعاء الأداة**. يتم استخدام DeepSeek (بنمط OpenAI) في تدفق Claude Code الذي يتوقع رسائل أداة بنمط Anthropic. إليك حلان آمنان:

* **توجيه جميع أعمال Claude Code إلى Anthropic (عبر الوكيل)**.
* **عندما تستخدم DeepSeek، قم بإيقاف تشغيل الأدوات** (بحيث يُرجع نصًا عاديًا فقط) وقم بإيقاف تدفقات التفكير.

إليك تكوين ملف مفرد محدث يقوم بكليهما. الصقه كما هو:

```json
{
  "PROXY_URL": "http://127.0.0.1:7890",
  "LOG": true,
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "",
      "models": [
        "moonshotai/kimi-k2",
        "anthropic/claude-sonnet-4",
        "anthropic/claude-3.5-sonnet",
        "anthropic/claude-3.7-sonnet:thinking",
        "anthropic/claude-opus-4",
        "google/gemini-2.5-flash",
        "google/gemini-2.5-pro",
        "deepseek/deepseek-chat-v3-0324",
        "deepseek/deepseek-chat-v3.1",
        "deepseek/deepseek-r1",
        "mistralai/mistral-medium-3.1",
        "qwen/qwen3-coder",
        "openai/gpt-oss-120b",
        "openai/gpt-5",
        "openai/gpt-5-mini",
        "x-ai/grok-3-mini"
      ],
      "transformer": {
        "use": ["openrouter"]
      },
      "params": {
        "deepseek/deepseek-chat-v3.1": {
          "tool_choice": "none",
          "reasoning": { "exclude": true }
        },
        "deepseek/deepseek-r1": {
          "tool_choice": "none",
          "reasoning": { "exclude": true }
        }
      }
    },
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
  ],
  "Router": {
    "default": "anthropic-proxy,anthropic/claude-sonnet-4",
    "background": "anthropic-proxy,anthropic/claude-sonnet-4",
    "think": "anthropic-proxy,anthropic/claude-sonnet-4",
    "longContext": "openrouter,moonshotai/kimi-k2",
    "longContextThreshold": 2000,
    "webSearch": "openrouter,mistralai/mistral-medium-3.1",
    "overrides": {
      "deepseek/deepseek-chat-v3.1": "openrouter,deepseek/deepseek-chat-v3.1",
      "deepseek/deepseek-r1": "openrouter,deepseek/deepseek-r1",
      "google/gemini-2.5-flash": "openrouter,google/gemini-2.5-flash",
      "google/gemini-2.5-pro": "openrouter,google/gemini-2.5-pro",
      "qwen/qwen3-coder": "openrouter,qwen/qwen3-coder",
      "openai/gpt-5-mini": "openrouter,openai/gpt-5-mini"
    }
  }
}
```

ما يفعله هذا:

* مسارات Claude Code (`default/background/think`) تذهب إلى **Anthropic عبر `anthropic-proxy`**، حتى تعمل استخدامات الأدوات.
* يظل DeepSeek متاحًا، ولكن مع `"tool_choice":"none"` و `"reasoning.exclude": true`، لذلك لن يصدر استدعاءات أدوات أو كتل تفكير تعطل وكيل بيئة التطوير المتكاملة الخاص بك.
* لا يزال بإمكانك اختيار DeepSeek explicitly (على سبيل المثال، للدردشة العادية أو الصياغة)، وسيتم توجيهه عبر OpenRouter بشكل نظيف.

إذا كنت لا تزال ترى "Invalid tool parameters"، فهذا يعني أن هناك طبقة ما *لا تزال* تسمح لـ DeepSeek بإصدار استدعاء أداة. في هذه الحالة، تأكد من أن برنامج التشغيل الخاص بك يحترم فعليًا `params` الخاص بالنموذج. إذا لم يفعل ذلك، فاضبط استخدامك لـ DeepSeek فقط في السياقات التي يتم فيها تعطيل الأدوات، أو اعيد `default` إلى `openai/gpt-5-mini` واحتفظ بـ DeepSeek لملف تعريف يدوي "بدون أدوات".