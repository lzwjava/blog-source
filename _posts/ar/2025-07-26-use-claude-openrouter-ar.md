---
audio: false
generated: true
lang: ar
layout: post
title: الوصول إلى كلود عبر أوبن روتر
translated: true
type: note
---

### كيفية استخدام نماذج Claude عبر OpenRouter (للمستخدمين الصينيين بدون وصول إلى واجهة برمجة تطبيقات Anthropic)

كمستخدم صيني، قد تواجه قيودًا في الوصول المباشر إلى واجهة برمجة تطبيقات Anthropic's Claude بسبب الحجب الإقليمي. ومع ذلك، يعد OpenRouter بديلاً موثوقًا يعمل كبوابة موحدة لواجهات برمجة التطبيقات للعديد من مزودي الذكاء الاصطناعي، بما في ذلك نماذج Claude من Anthropic. OpenRouter يمكن الوصول إليه في الصين (كل من الموقع ونقاط نهاية واجهة برمجة التطبيقات غير محجوبة)، مما يسمح لك بتوجيه الطلبات إلى Claude دون الحاجة إلى حساب Anthropic مباشر أو مفتاح واجهة برمجة تطبيقات. إنه نظام الدفع مقابل الاستخدام (ستحتاج إلى إضافة طريقة دفع)، ولكن التسجيل مجاني، وهو يدوي مستوى مجاني للاستخدام المحدود.

واجهة برمجة تطبيقات OpenRouter متوافقة مع تنسيق OpenAI، لذا يمكنك استخدام مكتبات مألوفة مثل OpenAI Python SDK. أدناه، سأوضح الخطوات للبدء وأقدم أمثلة على التعليمات البرمجية لاستخدام Claude في Python.

#### الخطوة 1: التسجيل في OpenRouter
1. قم بزيارة موقع OpenRouter: https://openrouter.ai.
2. انقر على "Sign Up" أو "Get Started" (عادة في أعلى اليمين).
3. أنشئ حسابًا باستخدام بريدك الإلكتروني (أو عبر تسجيل الدخول بواسطة GitHub/Google إذا كان متاحًا). لا حاجة لاستخدام VPN، لأن الموقع يعمل في الصين.
4. بعد التسجيل، قم بتأكيد بريدك الإلكتروني إذا لزم الأمر.
5. انتقل إلى لوحة التحكم وأضف طريقة دفع (مثل بطاقة الائتمان) لتمويل حسابك. OpenRouter يتقاضى رسومًا بناءً على استخدام الرموز (tokens)، ولكن يمكنك البدء بإيداع صغير. تحقق من صفحة الأسعار للحصول على تفاصيل حول نماذج Claude.

#### الخطوة 2: إنشاء مفتاح واجهة برمجة تطبيقات (API Key)
1. في لوحة تحكم OpenRouter، انتقل إلى قسم "API Keys" أو "Keys".
2. أنشئ مفتاح واجهة برمجة تطبيقات جديد (سيبدو كسلسلة طويلة، مثل `sk-or-v1-...`).
3. انسخه واحفظه بأمان — عامله مثل كلمة مرور. ستستخدمه في الكود الخاص بك بدلاً من مفتاح Anthropic.

#### الخطوة 3: اختر نموذج Claude
يسرد OpenRouter نماذج Claude من Anthropic برموز مثل:
- `anthropic/claude-3.5-sonnet` (موصى به لمعظم المهام؛ متوازن وقادر).
- `anthropic/claude-3-opus` (أكثر قوة ولكن أكثر تكلفة).
- الإصدارات الأحدث (مثل Claude 3.7 إذا كانت متاحة في 2025) سيتم سردها على https://openrouter.ai/models?providers=anthropic.

يمكنك تصفح صفحة النماذج لرؤية التكاليف وحدود السياق (context) والتوفر.

#### الخطوة 4: إعداد بيئتك
- قم بتثبيت Python إذا لم يكن لديكه (الإصدار 3.8+ موصى به).
- قم بتثبيت مكتبة OpenAI: قم بتشغيل `pip install openai` في طرفيتك (terminal).

#### الخطوة 5: استخدام Claude في الكود
استخدم OpenAI SDK مع عنوان URL الأساسي لـ OpenRouter (`https://openrouter.ai/api/v1`). حدد معرف نموذج Claude في طلباتك.

إليك مثالاً بسيطًا باستخدام Python للدردشة مع Claude 3.5 Sonnet:

```python
from openai import OpenAI

# تهيئة العميل مع نقطة نهاية OpenRouter ومفتاح واجهة برمجة التطبيقات الخاص بك
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_OPENROUTER_API_KEY_HERE",  # استبدله بمفتاحك الفعلي
)

# تقديم طلب إلى Claude
completion = client.chat.completions.create(
    model="anthropic/claude-3.5-sonnet",  # استخدم معرف نموذج Claude
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, what is the capital of China?"}
    ],
    temperature=0.7,  # اختياري: اضبط للإبداع (0-1)
    max_tokens=150    # اختياري: حدد طول الرد
)

# اطبع الرد
print(completion.choices[0].message.content)
```

- **الشرح**: يرسل هذا الأمر موجه النظام (system prompt) ورسالة المستخدم إلى Claude، ويحصل على رد، ويطبعه. استبدل مفتاح واجهة برمجة التطبيقات وضبط المعلمات حسب الحاجة.
- **إذا كنت تفضل طلبات HTTP مباشرة** (بدون مكتبة OpenAI):

```python
import requests
import json

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer YOUR_OPENROUTER_API_KEY_HERE",
        "Content-Type": "application/json"
    },
    data=json.dumps({
        "model": "anthropic/claude-3.5-sonnet",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, what is the capital of China?"}
        ]
    })
)

# Parse and print the response
data = response.json()
print(data['choices'][0]['message']['content'])
```

- **نصائح**:
  - أضف رؤوسًا (headers) اختيارية مثل `"HTTP-Referer": "your-site-url"` و `"X-Title": "Your App Name"` لتعريف الاستخدام (يساعد في لوحات المتصدرين والحصول على رصيد مجاني محتمل).
  - راقب الاستخدام في لوحة تحكم OpenRouter لتجنب التكاليف غير المتوقعة.
  - للردود المتدفقة (streaming responses) أو الميزات المتقدمة (مثل الأدوات Tools)، راجع وثائق OpenRouter الكاملة.
  - إذا واجهت حدود معدل (rate limits) أو أخطاء، تحقق من رصيدك أو جرب نموذجًا مختلفًا.

#### استكشاف الأخطاء وإصلاحها
- **أخطاء واجهة برمجة التطبيقات**: تأكد من صحة مفتاحك وتمويله. اختبر أولاً باستخدام نموذج رخيص.
- **مشاكل إقليمية**: إذا حدث أي حجب (غير مرجح)، استخدم VPN، ولكن OpenRouter مصمم لتجاوز مثل هذه القيود للنماذج المدعومة.
- **بدائل مجانية**: للوصول المجاني المحدود، استكشف الوكالات (proxies) مثل Puter.js (ولكن قد يكون لها قيود).

هذا الإعداد يسمح لك باستخدام Claude برمجيًا بدون وصول مباشر إلى Anthropic. إذا كنت بحاجة إلى التكامل مع أدوات محددة (مثل Cursor IDE أو Make.com)، فابحث عن دروس تعليمية عنها.

المراجع:  
[OpenRouter Documentation](https://openrouter.ai/docs)  
[Anthropic Claude on OpenRouter](https://openrouter.ai/anthropic/claude-3.5-sonnet)  
[Using OpenRouter in China](https://medium.com/ai-simplified-in-plain-english/not-re-inventing-the-wheel-in-ai-2ec3e76ae2bd)  
[How to Use Claude in China](https://www.comparitech.com/blog/vpn-privacy/how-to-use-claude-in-china/)