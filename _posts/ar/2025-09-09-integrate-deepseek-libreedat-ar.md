---
audio: false
date: 2025-09-09
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: دليل دمج DeepSeek مع LibreChat
translated: true
type: note
---

إليك أسرع طريقة لتشغيل **DeepSeek في LibreChat**. سأعرض خيارين—استخدم **الـ API الرسمي من DeepSeek** (موصى به)، أو استخدم **OpenRouter**.

---

## الخيار أ — استخدم الـ API الرسمي من DeepSeek (موصى به)

1.  **احصل على مفتاح API من DeepSeek**
    أنشئ واحدًا في حسابك على DeepSeek، ثم لاحظ عنوان URL الأساسي:
    `https://api.deepseek.com` (أو الإصدار المتوافق مع OpenAI `https://api.deepseek.com/v1`). ([وثائق DeepSeek API][1], [deepseek.apidog.io][2])

2.  **أضف نقطة نهاية DeepSeek في ملف `librechat.yaml`**
    ضع هذا تحت `endpoints:` → `custom:`:

```yaml
- name: deepseek
  apiKey: ${DEEPSEEK_API_KEY}
  baseURL: https://api.deepseek.com/v1
  models:
    default: deepseek-chat
    fetch: true
    list:
      - deepseek-chat        # V3 (عام)
      - deepseek-coder       # مخصص للبرمجة
      - deepseek-reasoner    # R1 للاستدلال
  titleConvo: true
  dropParams: null
```

يأتي LibreChat مع دليل إعداد **DeepSeek** ويؤكد أسماء النماذج (`deepseek-chat`, `deepseek-coder`, `deepseek-reasoner`) وملاحظات حول R1 الذي يبث "عملية التفكير". ([LibreChat][3])

3.  **عرض مفتاح API عبر ملف `.env`**
    في ملف `.env` الخاص بـ LibreChat:

```
DEEPSEEK_API_KEY=sk-...
```

يدعم LibreChat مزودي خدمات متوافقين مع OpenAI مخصصين عبر `librechat.yaml` + `.env`. ([LibreChat][4])

4.  **أعد تشغيل الـ stack**
    من مجلد LibreChat:

```bash
docker compose down
docker compose up -d --build
```

(مطلوب حتى تعيد حاوية API تحميل `librechat.yaml` و `.env`.) إذا لم تظهر نقاط النهاية المخصصة، تحقق من سجلات حاوية `api` للبحث عن أخطاء في الإعداد. ([GitHub][5])

---

## الخيار ب — استخدم DeepSeek عبر OpenRouter

إذا كنت تستخدم OpenRouter بالفعل، فما عليك سوى تسجيل نماذج DeepSeek في كتلة نقطة نهاية OpenRouter.

`librechat.yaml`:

```yaml
- name: openrouter
  apiKey: ${OPENROUTER_KEY}
  baseURL: https://openrouter.ai/api/v1
  models:
    default: deepseek/deepseek-chat
    list:
      - deepseek/deepseek-chat
      - deepseek/deepseek-coder
      - deepseek/deepseek-reasoner
```

ملاحظتان مهمتان من وثائق LibreChat:
• لا تضبط اسم متغير البيئة `OPENROUTER_API_KEY` (استخدم اسمًا مختلفًا مثل `OPENROUTER_KEY`) وإلا ستقوم عن طريق الخطأ بتجاوز نقطة نهاية OpenAI.
• OpenRouter معتمد بشكل أساسي في قائمة نقاط النهاية المخصصة في LibreChat. ([LibreChat][6])

يعرض OpenRouter نماذج DeepSeek بواجهة متوافقة مع OpenAI. ([OpenRouter][7])

---

## نصائح ومحاذير

*   **R1 / `deepseek-reasoner`**: يمكنه بث سلسلة أفكاره ("عملية التفكير"). بعض معاملات OpenAI قد لا تنطبق. إذا رأيت ناتجًا غريبًا، اختبر أولاً باستخدام `deepseek-chat`. ([LibreChat][3])
*   **جلب النماذج**: يسمح تعيين `fetch: true` لـ LibreChat بسحب أحدث قائمة نماذج عندما يكون ذلك مدعومًا؛ وإلا سيتم استخدام القائمة `list:` التي تحددها. ([LibreChat][8])
*   **مكان هذه الإعدادات**: `librechat.yaml` هو ملف نقاط النهاية المخصصة؛ `.env` يحمل المفاتيح وإعدادات الوكيل. ([LibreChat][8])

إذا أردت، الصق محتوى ملف `librechat.yaml` الحالي وسأقوم بتعديله لإضافة DeepSeek بطريقة نظيفة (بدون جداول، أعدك).

[1]: https://api-docs.deepseek.com/?utm_source=chatgpt.com "DeepSeek API Docs: Your First API Call"
[2]: https://deepseek.apidog.io/your-first-api-call-835227m0?utm_source=chatgpt.com "DeepSeek API: Your First API Call"
[3]: https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/deepseek?utm_source=chatgpt.com "Deepseek"
[4]: https://www.librechat.ai/docs/quick_start/custom_endpoints?utm_source=chatgpt.com "Custom Endpoints"
[5]: https://github.com/danny-avila/LibreChat/discussions/2487?utm_source=chatgpt.com "Fix the librechat.yaml file in the main repository. #2487"
[6]: https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/openrouter?utm_source=chatgpt.com "Openrouter"
[7]: https://openrouter.ai/deepseek/deepseek-v3-base%3Afree/api?utm_source=chatgpt.com "DeepSeek V3 Base – Run with an API"
[8]: https://www.librechat.ai/docs/configuration/librechat_yaml?utm_source=chatgpt.com "librechat.yaml config file"