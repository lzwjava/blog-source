---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تهيئة بروكسي Python Requests عبر .env
translated: true
type: note
---

### استخدام ملف `.env` لتعيين بروكسي HTTP/HTTPS لمكتبة Requests في بايثون

تلتزم مكتبة `requests` في بايثون تلقائيًا بمتغيرات البيئة القياسية مثل `HTTP_PROXY` و `HTTPS_PROXY` لتكوين البروكسي. لإدارة هذه المتغيرات بشكل آمن (على سبيل المثال، دون ترميزها مباشرة في السكريبت)، يمكنك تخزينها في ملف `.env` وتحميلها باستخدام مكتبة `python-dotenv`. هذا يحافظ على تفاصيل البروكسي الحساسة خارج الكود الخاص بك.

#### الخطوة 1: تثبيت الحزم المطلوبة
ستحتاج إلى `requests` (إذا لم تكن مثبتة مسبقًا) و `python-dotenv` لتحميل ملف `.env`.

```bash
pip install requests python-dotenv
```

#### الخطوة 2: إنشاء ملف `.env`
في المجلد الجذري لمشروعك، أنشئ ملفًا باسم `.env` (بدون امتداد) وأضف إعدادات البروكسي الخاصة بك. استخدم التنسيق `http://` أو `https://` لرابط البروكسي، بما في ذلك اسم المستخدم/كلمة المرور إذا لزم الأمر.

مثال محتوى ملف `.env`:
```
HTTP_PROXY=http://username:password@proxy-host:port
HTTPS_PROXY=https://username:password@proxy-host:port
NO_PROXY=localhost,127.0.0.1,example.com  # اختياري: استبعاد النطاقات من استخدام البروكسي
```

- `HTTP_PROXY`: لحركة مرور HTTP.
- `HTTPS_PROXY`: لحركة مرور HTTPS (غالبًا ما تكون نفس `HTTP_PROXY`).
- `NO_PROXY`: قائمة مفصولة بفواصل من الخوادم/عنوانات IP لتجاوز البروكسي.
- ملاحظة: متغيرات البيئة لا تفرق بين الأحرف الكبيرة والصغيرة، ولكن استخدام الأحرف الكبيرة هو الاتفاق السائد.

أضف `.env` إلى ملف `.gitignore` الخاص بك لتجنب حفظ المعلومات الحساسة في نظام التحكم بالإصدار.

#### الخطوة 3: تحميل ملف `.env` في سكريبت بايثون الخاص بك
في أعلى السكريبت، قم بتحميل متغيرات البيئة:

```python
from dotenv import load_dotenv
import requests

# تحميل المتغيرات من ملف .env
load_dotenv()  # يبحث عن ملف .env في المجلد الحالي افتراضيًا

# الآن قم بإجراء طلب – سيتم تطبيق إعدادات البروكسي تلقائيًا
response = requests.get('https://httpbin.org/ip')
print(response.json())
```

- `load_dotenv()` يقرأ ملف `.env` ويضبط المتغيرات في `os.environ`.
- `requests` سيكتشف `HTTP_PROXY`/`HTTPS_PROXY` تلقائيًا – لا حاجة لتمرير قاموس `proxies` إلا إذا كنت تريد التجاوز.

#### الخطوة 4: التحقق من استخدام البروكسي (اختياري)
لتأكيد عمل البروكسي، اختبر باستخدام خدمة مثل httpbin.org:

```python
import requests
from dotenv import load_dotenv

load_dotenv()

proxies = requests.utils.get_environ_proxies('https://httpbin.org/ip')  # فحص إعدادات البروكسي المحملة
print("إعدادات البروكسي المحملة:", proxies)

response = requests.get('https://httpbin.org/ip')
print("عنوان IP الخاص بك عبر البروكسي:", response.json())
```

يجب أن يظهر هذا عنوان IP لخادم البروكسي إذا تم تكوينه بشكل صحيح.

#### المشاكل الشائعة والنصائح
- **مصادقة البروكسي**: قم بتضمين `username:password@` في الرابط إذا لزم الأمر.
- **بروكسي SOCKS**: استخدم البادئة `socks5://` (تتطلب تثبيت `requests[socks]` الإضافي: `pip install requests[socks]`).
- **التجاوز لكل طلب**: إذا كنت تحتاج إلى بروكسي مختلف لطلب محدد، قم بتمرير قاموس:
  ```python:disable-run
  proxies = {'http': 'http://custom-proxy:port', 'https': 'https://custom-proxy:port'}
  response = requests.get('url', proxies=proxies)
  ```
- **البيئة**: يعمل على Windows/Linux/macOS. على Windows، استخدم `set` في موجه الأوامر أو أوامر PowerShell المكافئة.
- **الأمان**: لا تقم أبدًا بحفظ ملف `.env` في نظام التحكم بالإصدار.

هذا الإعداد بسيط، آمن، ويتبع أفضل الممارسات للتكوين القائم على البيئة.

[توثيق Requests: البروكسي](https://requests.readthedocs.io/en/latest/user/advanced/#proxies)  
[توثيق python-dotenv](https://github.com/theskumar/python-dotenv)