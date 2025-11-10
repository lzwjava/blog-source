---
audio: false
generated: true
image: false
lang: ar
layout: post
title: الجلسات الدائمة باستخدام مكتبة الطلبات في بايثون
translated: true
type: note
---

`Session` في مكتبة `requests` الخاصة بـ Python هي طريقة للحفاظ على معلمات معينة، مثل ملفات تعريف الارتباط (cookies) والعناوين (headers) والمصادقة (authentication)، عبر طلبات HTTP متعددة. توفر واجهة مريحة لإجراء طلبات متكررة لنفس الخادم أو نقاط النهاية المرتبطة مع الحفاظ على الحالة، وتحسين الكفاءة، وتبسيط الكود. أدناه، سأشرح كيفية عمل `requests.Session`، وميزاتها الرئيسية، وسأقدم أمثلة لتوضيح استخدامها.

## ما هي `requests.Session`؟

مكتبة `requests` مستخدمة على نطاق واسع لإجراء طلبات HTTP في Python. بينما يمكنك استخدام الدوال المنفردة مثل `requests.get()` أو `requests.post()`، فإن كائن `Session` يسمح لك بإنشاء جلسة مستمرة تحتفظ بالإعدادات (مثل ملفات تعريف الارتباط والعناوين أو بيانات اعتماد المصادقة) عبر طلبات متعددة. هذا مفيد بشكل خاص للتفاعل مع المواقع الإلكترونية أو واجهات برمجة التطبيقات (APIs) التي تتطلب تفاعلات تحافظ على الحالة، مثل الحفاظ على جلسة تسجيل دخول أو إعادة استخدام اتصالات TCP.

كائن `Session`:
- يحافظ على ملفات تعريف الارتباط عبر الطلبات.
- يعيد استخدام اتصالات TCP الأساسية (عبر تجميع الاتصالات) لتحسين الأداء عند إجراء طلبات متعددة لنفس المضيف.
- يسمح لك بتعيين معلمات افتراضية (مثل العناوين، المهلات) تنطبق على جميع الطلبات التي تتم باستخدام الجلسة.
- يدعم المصادقة والإعدادات المخصصة.

## كيف تعمل `Session`؟

عندما تنشئ كائن `Session`، فإنه يعمل كحاوية لطلبات HTTP الخاصة بك. إليك تفصيل لكيفية عملها:

1.  **ملفات تعريف الارتباط المستمرة**: عندما تقوم بطلب باستخدام `Session`، يتم تخزين أي ملفات تعريف ارتباط يحددها الخادم (مثل ملفات تعريف ارتباط الجلسة بعد تسجيل الدخول) في الجلسة وإرسالها تلقائيًا في الطلبات اللاحقة. هذا أمر أساسي للحفاظ على الحالة، مثل البقاء مسجل الدخول.

2.  **تجميع الاتصالات**: للطلبات الموجهة لنفس المضيف، تعيد `Session` استخدام نفس اتصال TCP، مما يقلل زمن الويبح (latency) والنفقات العامة مقارنة بإنشاء اتصالات جديدة لكل طلب.

3.  **المعلمات الافتراضية**: يمكنك تعيين سمات مثل العناوين أو المصادقة أو المهلات على كائن `Session`، وسوف تنطبق على جميع الطلبات التي تتم باستخدام تلك الجلسة ما لم يتم تجاوزها.

4.  **قابلة للتخصيص**: يمكنك تكوين الوكلاء (proxies)، أو التحقق من SSL، أو حتى تركيب محولات مخصصة (على سبيل المثال، لإعادة المحاولة أو نقل مخصص) للتحكم في كيفية معالجة الطلبات.

## الاستخدام الأساسي

إليك مثالًا بسيطًا لكيفية استخدام `requests.Session`:

```python
import requests

# إنشاء جلسة
session = requests.Session()

# تعيين العناوين الافتراضية لجميع الطلبات في هذه الجلسة
session.headers.update({'User-Agent': 'MyApp/1.0'})

# إجراء طلب GET
response1 = session.get('https://api.example.com/data')
print(response1.json())

# إجراء طلب آخر؛ يتم إعادة استخدام ملفات تعريف الارتباط والعناوين
response2 = session.post('https://api.example.com/submit', data={'key': 'value'})
print(response2.json())

# إغلاق الجلسة لتحرير الموارد
session.close()
```

في هذا المثال:
- تم إنشاء `Session`، وتم تعيين عنوان `User-Agent` مخصص لجميع الطلبات.
- تتعامل الجلسة مع ملفات تعريف الارتباط تلقائيًا، لذا إذا قام `response1` بتعيين ملف تعريف ارتباط، فسيتم إرساله مع `response2`.
- تعيد الجلسة استخدام الاتصال بـ `api.example.com`، مما يحسن الأداء.

## الميزات الرئيسية والأمثلة

### 1. **الحفاظ على ملفات تعريف الارتباط**
الجلسات مفيدة بشكل خاص للمواقع الإلكترونية التي تستخدم ملفات تعريف الارتباط للحفاظ على الحالة، مثل جلسات تسجيل الدخول.

```python
import requests

# إنشاء جلسة
session = requests.Session()

# تسجيل الدخول إلى موقع إلكتروني
login_data = {'username': 'user', 'password': 'pass'}
response = session.post('https://example.com/login', data=login_data)

# الوصول إلى صفحة محمية؛ ترسل الجلسة تلقائيًا ملف تعريف ارتباط تسجيل الدخول
protected_page = session.get('https://example.com/protected')
print(protected_page.text)

# إغلاق الجلسة
session.close()
```

هنا، تقوم الجلسة بتخزين ملف تعريف ارتباط المصادقة من طلب تسجيل الدخول وإرساله مع الطلب اللاحق للصفحة المحمية.

### 2. **تعيين المعلمات الافتراضية**
يمكنك تعيين العناوين الافتراضية أو المصادقة أو المعلمات الأخرى لجميع الطلبات في الجلسة.

```python
import requests

session = requests.Session()

# تعيين العناوين الافتراضية
session.headers.update({
    'Authorization': 'Bearer my_token',
    'Accept': 'application/json'
})

# تعيين المهلة الافتراضية
session.request = functools.partial(session.request, timeout=5)

# إجراء الطلبات؛ يتم تطبيق العناوين والمهلة تلقائيًا
response1 = session.get('https://api.example.com/endpoint1')
response2 = session.get('https://api.example.com/endpoint2')

session.close()
```

### 3. **تجميع الاتصالات**
عند إجراء طلبات متعددة لنفس المضيف، تعيد `Session` استخدام الاتصالات، مما يجعلها أكثر كفاءة من الطلبات المنفردة.

```python
import requests
import time

# بدون جلسة
start = time.time()
for _ in range(5):
    requests.get('https://api.example.com/data')
print(f"Without session: {time.time() - start} seconds")

# مع جلسة
session = requests.Session()
start = time.time()
for _ in range(5):
    session.get('https://api.example.com/data')
print(f"With session: {time.time() - start} seconds")
session.close()
```

الطلبات القائمة على الجلسة تكون عادةً أسرع لأنها تعيد استخدام اتصال TCP.

### 4. **المصادقة**
تبسط الجلسات التعامل مع المصادقة، مثل HTTP Basic Auth أو المصادقة القائمة على الرموز (tokens) المخصصة.

```python
import requests
from requests.auth import HTTPBasicAuth

session = requests.Session()
session.auth = HTTPBasicAuth('user', 'pass')

# جميع الطلبات ستتضمن Basic Auth
response = session.get('https://api.example.com/protected')
print(response.json())

session.close()
```

### 5. **المحولات المخصصة**
يمكنك تركيب محولات مخصصة للتحكم في أشياء مثل إعادة المحاولة أو سلوك تجميع الاتصالات.

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()

# تكوين إعادة المحاولة
retries = Retry(total=3, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))

# إجراء طلب مع منطق إعادة المحاولة
response = session.get('https://api.example.com/unstable_endpoint')
print(response.json())

session.close()
```

يقوم هذا المثال بإعداد إعادة المحاولة التلقائية لرموز خطأ HTTP محددة.

## متى تستخدم `Session`

استخدم `requests.Session` عندما:
- تحتاج إلى الحفاظ على الحالة (مثل ملفات تعريف الارتباط) عبر طلبات متعددة، كما في حالة المصادقة.
- تقوم بإجراء طلبات متعددة لنفس المضيف وتريد الاستفادة من تجميع الاتصالات.
- تريد تطبيق إعدادات متسقة (عناوين، مهلات، إلخ) عبر الطلبات.
- تتفاعل مع واجهات برمجة التطبيقات أو المواقع الإلكترونية التي تتطلب تفاعلات قائمة على الجلسة.

إذا كنت تقوم بطلب واحد أو لا تحتاج إلى الحفاظ على الحالة، فإن استخدام `requests.get()` أو `requests.post()` المنفردة يكون كافيًا.

## إغلاق الجلسة

أغلق الجلسة دائمًا عند الانتهاء لتحرير الموارد (مثل الاتصالات):

```python
session.close()
```

بدلاً من ذلك، استخدم الجلسة كمدير سياق (context manager) لضمان إغلاقها تلقائيًا:

```python
with requests.Session() as session:
    session.headers.update({'User-Agent': 'MyApp/1.0'})
    response = session.get('https://api.example.com/data')
    print(response.json())
# يتم إغلاق الجلسة تلقائيًا عند الخروج من الكتلة
```

## ملاحظات متقدمة
- **أمان الخيوط (Thread Safety)**: كائنات `Session` ليست آمنة للاستخدام في بيئة متعددة الخيوط (thread-safe). إذا كنت تستخدم تعدد الخيوط، فأنشئ `Session` منفصلة لكل خيط.
- **الوكلاء (Proxies)**: يمكنك تعيين الوكلاء على جلسة باستخدام `session.proxies = {'http': 'http://proxy.com', 'https': 'https://proxy.com'}`.
- **التحقق من SSL**: بشكل افتراضي، تقوم `Session` بالتحقق من شهادات SSL. لتعطيل ذلك (غير موصى به للإنتاج)، استخدم `session.verify = False`.

## المراجع
[Requests Documentation](https://requests.readthedocs.io/en/latest/)  
[Requests Session Objects](https://requests.readthedocs.io/en/latest/user/advanced/#session-objects)