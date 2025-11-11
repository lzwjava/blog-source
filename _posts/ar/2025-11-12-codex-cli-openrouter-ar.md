---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تهيئة Codex CLI لـ OpenRouter
translated: true
type: note
---

### إعداد تكوين Codex CLI لـ OpenRouter

Codex CLI (من OpenAI) هو وكيل برمجة يعتمد على الطرفية ويدعم مقدمي النماذج المخصصين مثل OpenRouter عبر ملف التكوين الخاص به. يوفر OpenRouter واجهة برمجة تطبيقات متوافقة مع OpenAI، لذا يمكنك توجيه الطلبات من خلاله عن طريق تعريف موفر بعنوان URL الأساسي المناسب. هذا يسمح بالوصول إلى نطاق أوسع من النماذج (مثل تلك من Anthropic أو Google أو موفري المصادر المفتوحة) أثناء استخدام Codex.

يتم تخزين التكوين في ملف TOML في المسار `~/.codex/config.toml` (قم بإنشائه إذا لم يكن موجودًا). سوف تقوم بتعريف قسم **لموفر النموذج** لـ OpenRouter ثم الإشارة إليه في **ملف تعريف** لنماذج محددة.

#### الخطوة 1: الحصول على مفتاح واجهة برمجة التطبيقات (API Key) لـ OpenRouter
- سجل في [openrouter.ai](https://openrouter.ai) إذا لم تكن قد قمت بذلك.
- أنشئ مفتاح واجهة برمجة تطبيقات من لوحة تحكم حسابك.
- عيّنه كمتغير بيئة:  
  ```
  export OPENROUTER_API_KEY=your_api_key_here
  ```
  أضف هذا إلى ملف تعريف shell الخاص بك (مثل `~/.bashrc` أو `~/.zshrc`) للحفظ الدائم.

#### الخطوة 2: تعديل ملف التكوين
افتح `~/.codex/config.toml` في محررك وأضف الأقسام التالية. هذا يضبط عنوان URL الأساسي ليصل إلى نقطة نهاية OpenRouter (`https://openrouter.ai/api/v1`)، وهو متوافق مع OpenAI (يقوم Codex تلقائيًا بإلحاق `/chat/completions`).

```toml
# تعريف موفر OpenRouter
[model_providers.openrouter]
name = "OpenRouter"
base_url = "https://openrouter.ai/api/v1"
env_key = "OPENROUTER_API_KEY"  # يقرأ من متغير البيئة الخاص بك للمصادقة

# تعريف ملف تعريف باستخدام هذا الموفر (مثال: استخدام نموذج مشابه لـ GPT)
[profiles.openrouter-gpt]
model_provider = "openrouter"
model = "openai/gpt-4o-mini"  # استبدل بأي معرف نموذج من OpenRouter، مثل "anthropic/claude-3.5-sonnet"
```

- **شرح الحقول الرئيسية**:
  - `base_url`: يشير إلى نقطة نهاية واجهة برمجة تطبيقات OpenRouter. هذا يتجاوز عنوان URL الأساسي الافتراضي لـ OpenAI.
  - `env_key`: يحدد متغير البيئة لرأس مصادقة Bearer token.
  - `model`: استخدم معرفات النماذج الدقيقة من [قائمة نماذج OpenRouter](https://openrouter.ai/models). لمهام البرمجة، جرب "openai/codex-mini-latest" أو "meta-llama/llama-3.1-405b-instruct".
  - يمكنك إضافة ملفات تعريف متعددة لنماذج مختلفة (مثل `[profiles.openrouter-claude]` مع `model = "anthropic/claude-3.5-sonnet"`).

#### الخطوة 3: استخدام التكوين
- قم بتثبيت Codex CLI إذا لزم الأمر: `npm install -g @openai/codex` (أو عبر Homebrew: `brew install codex`).
- شغّل Codex باستخدام ملف التعريف الخاص بك:  
  ```
  codex --profile openrouter-gpt
  ```
  أو عيّن ملف تعريف افتراضي في التكوين:  
  ```toml
  [default_profile]
  name = "openrouter-gpt"
  ```
- اختبره: شغّل `codex` وأعطه أمر برمجة بسيط. تحقق من لوحة تحكم OpenRouter لمعرفة الاستخدام.

#### استكشاف الأخطاء وإصلاحها
- **أخطاء المصادقة**: تأكد من تعيين `OPENROUTER_API_KEY` وتصديره.
- **النموذج غير موجود**: تحقق من معرف النموذج على OpenRouter — فهو حساس لحالة الأحرف وله بادئة (مثل "provider/model-name").
- **التحقق من الإصدار**: استخدم Codex CLI الإصدار v0.13+ أو أحدث للحصول على دعم كامل للموفر. قم بالتحديث باستخدام `npm update -g @openai/codex`.
- **التوجيه المتقدم**: لميزات OpenRouter المحددة مثل التوجيه الأمثل للتكلفة، أضف معلمات اختيارية مثل `provider = { sort = "price" }` تحت ملف التعريف (مدعوم في الإصدارات الأحدث).

هذا الإعداد يحافظ على توافق طلباتك مع واجهة برمجة تطبيقات Codex ذات الطراز OpenAI مع الاستفادة من نظام OpenRouter البيئي. لمزيد من التفاصيل، راجع [وثائق Codex CLI على npm](https://www.npmjs.com/package/@openai/codex) أو [دليل واجهة برمجة التطبيقات لـ OpenRouter](https://openrouter.ai/docs). إذا كنت تستخدم نسخة معدلة مثل Open Codex، فإن التكوين مشابه ولكن قد يحتوي على دعم إضافي لـ Gemini.