---
audio: false
generated: true
image: false
lang: ar
layout: post
title: المخطط الوكيل غير مدعوم
translated: true
type: note
---

يشير الخطأ إلى أن مكتبة `httpx`، التي يستخدمها عميل `openai` في سكريبت `gitmessageai.py` الخاص بك، تحاول تكوين وكيل بروكسي بعنوان URL `socks://127.0.0.1:7891/`، لكن المخطط `socks` غير مدعوم أو معترف به، مما يؤدي إلى حدوث خطأ `ValueError: Unknown scheme for proxy URL`. يشير هذا إلى أن تكوين الوكيل يتم التقاطه من بيئتك أو كودك، وهو يستخدم مخطط وكيل SOCKS غير مدعوم.

دعنا نحلل مصدر الوكيل المحتمل وكيفية إصلاحه.

### من أين يأتي الوكيل؟

من المرجح أن يكون تكوين الوكيل (`socks://127.0.0.1:7891/`) مصدره أحد الأماكن التالية:

1. **متغيرات البيئة**
   - تتحقق مكتبة `httpx` تلقائيًا من إعدادات الوكيل في متغيرات البيئة مثل `HTTP_PROXY`، `HTTPS_PROXY`، `ALL_PROXY`، أو ما يعادلها بالأحرف الصغيرة (`http_proxy`، `https_proxy`، `all_proxy`).
   - تشير قيمة مثل `socks://127.0.0.1:7891/` إلى أن وكيل SOCKS (شائع في أدوات مثل Shadowsocks أو شبكات VPN) تم تعيينه في أحد هذه المتغيرات.
   - للتحقق مما إذا كانت هذه المتغيرات مضبوطة، قم بتشغيل الأمر التالي في الطرفية:
     ```bash
     env | grep -i proxy
     ```
     ابحث عن متغيرات مثل `HTTP_PROXY=socks://127.0.0.1:7891` أو `HTTPS_PROXY=socks://127.0.0.1:7891`.

2. **إعدادات الوكيل على مستوى النظام**
   - إذا كنت تستخدم نظام Linux، فقد تكون إعدادات الوكيل مضبوطة بشكل عام (على سبيل المثال، في `/etc/environment`، `/etc/profile`، أو تكوين shell الخاص بك مثل `~/.bashrc`، `~/.zshrc`، أو `~/.profile`).
   - افحص هذه الملفات للعثور على أسطر مثل:
     ```bash
     export HTTP_PROXY="socks://127.0.0.1:7891"
     export HTTPS_PROXY="socks://127.0.0.1:7891"
     ```
   - يمكنك عرض هذه الملفات باستخدام:
     ```bash
     cat ~/.bashrc | grep -i proxy
     cat ~/.zshrc | grep -i proxy
     cat /etc/environment | grep -i proxy
     ```

3. **تكوين الوكيل في أداة بروكسي**
   - العنوان `127.0.0.1:7891` يشيع استخدامه بواسطة أدوات الوكيل أو VPN مثل Shadowsocks أو V2Ray أو Clash، والتي غالبًا ما تستخدم وكلاء SOCKS5 افتراضيًا على منافذ مثل 7890 أو 7891.
   - إذا قمت بتثبيت أو تكوين مثل هذه الأداة، فقد تكون قد عينت متغيرات البيئة أو إعدادات الوكيل على مستوى النظام تلقائيًا.

4. **وكيل صريح في الكود**
   - على الرغم من أنه أقل احتمالًا، قد يكون سكريبت `gitmessageai.py` الخاص بك أو إحدى المكتبات التي يستخدمها يقوم بتكوين وكيل بشكل صريح. نظرًا لأن الخطأ يحدث في `httpx`، تحقق مما إذا كان السكريبت الخاص بك يمرر وكيلًا إلى عميل `OpenAI` أو عميل `httpx`.
   - ابحث في سكريبتك عن مصطلحات مثل `proxy`، `proxies`، أو `httpx.Client`:
     ```bash
     grep -r -i proxy /home/lzwjava/bin/gitmessageai.py
     ```

5. **تكوين مكتبة Python**
   - قد ترث بعض مكتبات Python (مثل `requests` أو `httpx`) إعدادات الوكيل من ملف تكوين أو إعداد سابق. ومع ذلك، تعتمد `httpx` بشكل أساسي على متغيرات البيئة أو الكود الصريح.

### لماذا يتسبب `socks://` في مشكلة؟

- مكتبة `httpx` (المستخدمة من قبل `openai`) لا تدعم بشكل أصلي مخطط `socks` (وكلاء SOCKS4/SOCKS5) إلا إذا تم تثبيت تبعيات إضافية مثل `httpx-socks`.
- يحدث الخطأ `Unknown scheme for proxy URL` لأن `httpx` تتوقع وكلاء بمخططات مثل `http://` أو `https://`، وليس `socks://`.

### كيفية إصلاح المشكلة

لديك خياران: **إزالة الوكيل أو تجاوزه** إذا لم يكن مطلوبًا، أو **دعم وكيل SOCKS** إذا كنت تنوي استخدامه.

#### الخيار 1: إزالة الوكيل أو تجاوزه

إذا كنت لا تحتاج إلى وكيل لـ DeepSeek API، يمكنك تعطيل أو تجاوز تكوين الوكيل.

1. **إلغاء ضبط متغيرات البيئة**
   - إذا تم تعيين الوكيل في متغيرات البيئة، قم بإلغاء ضبطها لجلسة العمل الخاصة بك:
     ```bash
     unset HTTP_PROXY
     unset HTTPS_PROXY
     unset ALL_PROXY
     unset http_proxy
     unset https_proxy
     unset all_proxy
     ```
   - لجعل هذا التغيير دائمًا، قم بإزالة أسطر `export` المقابلة من `~/.bashrc`، `~/.zshrc`، `/etc/environment`، أو ملفات تكوين shell الأخرى.

2. **تشغيل السكريبت بدون وكيل**
   - قم بتشغيل السكريبت الخاص بك مؤقتًا بدون إعدادات الوكيل:
     ```bash
     HTTP_PROXY= HTTPS_PROXY= ALL_PROXY= python3 /home/lzwjava/bin/gitmessageai.py
     ```
   - إذا نجح هذا، فإن الوكيل كان هو المشكلة.

3. **تجاوز الوكيل في الكود**
   - قم بتعديل سكريبت `gitmessageai.py` الخاص بك لتعطيل الوكلاء بشكل صريح في عميل `OpenAI`:
     ```python
     from openai import OpenAI
     import httpx

     def call_deepseek_api(prompt):
         api_key = os.getenv("DEEPSEEK_API_KEY")
         if not api_key:
             raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
         client = OpenAI(
             api_key=api_key,
             base_url="https://api.deepseek.com",
             http_client=httpx.Client(proxies=None)  # Disable proxies
         )
         # Your API call logic here
         response = client.chat.completions.create(
             model="deepseek",  # Replace with correct model
             messages=[{"role": "user", "content": prompt}]
         )
         return response.choices[0].message.content
     ```
   - يضمن تعيين `proxies=None` أن `httpx` تتجاهل أي إعدادات وكيل بيئية.

#### الخيار 2: دعم وكيل SOCKS

إذا كنت بحاجة إلى استخدام وكيل SOCKS (على سبيل المثال، للوصول إلى DeepSeek API عبر VPN أو خادم وكيل)، يجب عليك إضافة دعم SOCKS إلى `httpx`.

1. **تثبيت `httpx-socks`**
   - قم بتثبيت حزمة `httpx-socks` لتمكين دعم وكيل SOCKS4/SOCKS5:
     ```bash
     pip install httpx-socks
     ```
   - هذا يمتد `httpx` للتعامل مع المخططات `socks://` و `socks5://`.

2. **تحديث الكود الخاص بك**
   - قم بتعديل السكريبت الخاص بك لاستخدام وكيل SOCKS بشكل صريح:
     ```python
     from openai import OpenAI
     import httpx
     from httpx_socks import SyncProxyTransport

     def call_deepseek_api(prompt):
         api_key = os.getenv("DEEPSEEK_API_KEY")
         if not api_key:
             raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
         # Configure SOCKS5 proxy
         proxy_transport = SyncProxyTransport.from_url("socks5://127.0.0.1:7891")
         client = OpenAI(
             api_key=api_key,
             base_url="https://api.deepseek.com",
             http_client=httpx.Client(transport=proxy_transport)
         )
         # Your API call logic here
         response = client.chat.completions.create(
             model="deepseek",  # Replace with correct model
             messages=[{"role": "user", "content": prompt}]
         )
         return response.choices[0].message.content
     ```
   - استبدل `socks5://` بـ `socks4://` إذا كان الوكيل الخاص بك يستخدم SOCKS4.

3. **التحقق من خادم الوكيل**
   - تأكد من أن خادم الوكيل على `127.0.0.1:7891` قيد التشغيل. إذا كنت تستخدم أداة مثل Clash أو Shadowsocks، تحقق من حالتها:
     ```bash
     netstat -tuln | grep 7891
     ```
   - إذا لم تكن هناك عملية تستمع على المنفذ 7891، قم بتشغيل أداة الوكيل الخاصة بك أو صحح المنفذ في عنوان URL للوكيل.

### خطوات تصحيح إضافية

- **التحقق من تكوين أداة الوكيل**
  - إذا كنت تستخدم أداة وكيل مثل Clash أو Shadowsocks، تحقق من ملف التكوين الخاص بها (على سبيل المثال، `~/.config/clash/config.yaml`) للتأكد من أنها مضبوطة لاستخدام `127.0.0.1:7891` لـ SOCKS5.
  - تأكد من أن الأداة قيد التشغيل ويمكن الوصول إليها.

- **اختبار اتصال الوكيل**
   - اختبر الوكيل باستخدام أداة مثل `curl` (يتطلب `curl` مبنياً مع دعم SOCKS):
     ```bash
     curl --socks5 127.0.0.1:7891 https://api.deepseek.com
     ```
   - إذا فشل هذا، فإن خادم الوكيل إما معطل أو تم تكوينه بشكل خاطئ.

- **تسجيل استخدام الوكيل**
   - أضف تسجيلًا إلى السكريبت الخاص بك لتأكيد الوكيل المستخدم:
     ```python
     import logging
     logging.basicConfig(level=logging.DEBUG)
     ```

### الإصلاح الموصى به

إذا كنت لا تحتاج إلى الوكيل، فإن أبسط حل هو تعطيله عن طريق إلغاء ضبط متغيرات البيئة وتشغيل:
```bash
HTTP_PROXY= HTTPS_PROXY= ALL_PROXY= python3 /home/lzwjava/bin/gitmessageai.py
```

إذا كنت بحاجة إلى الوكيل، قم بتثبيت `httpx-socks` وقم بتحديث الكود الخاص بك لاستخدام `SyncProxyTransport` كما هو موضح أعلاه.

### المراجع
- [httpx Documentation](https://www.python-httpx.org/advanced/#proxy-support)
- [httpx-socks GitHub](https://github.com/romis2012/httpx-socks)
- [DeepSeek API Documentation](https://platform.deepseek.com/docs)