---
audio: false
generated: true
lang: ar
layout: post
title: مكتبة بايثون ريكويستس
translated: true
type: note
---

لاستبدال Postman بالكامل بمكتبة `requests` في Python، يمكنك تنفيذ جميع عمليات HTTP الشائعة مثل إرسال أنواع مختلفة من الطلبات، والتعامل مع الرؤوس، والعمل مع بيانات JSON، وتحميل الملفات، واستخدام الوكالات، والتحقق من الاستجابات. أدناه، سأرشدك عبر أمثلة لكل من هذه الوظائف خطوة بخطوة، مما يضمن أن لديك دليلًا كاملاً وعمليًا.

### الخطوة 1: تثبيت مكتبة Requests
قبل أن تبدأ، تأكد من تثبيت مكتبة `requests`. قم بتشغيل هذا الأمر في الطرفية:

```bash
pip install requests
```

الآن، دعنا نتعمق في الأمثلة.

---

### إرسال طلبات HTTP
تدعم مكتبة `requests` جميع طرق HTTP مثل GET، POST، PUT، DELETE، إلخ. إليك كيفية إرسال طلب GET و POST بسيطين:

#### طلب GET
```python
import requests

# إرسال طلب GET
response = requests.get('https://api.example.com/data')

# طباعة رمز الحالة ونص الاستجابة
print("Status Code:", response.status_code)
print("Response Body:", response.text)
```

#### طلب POST
```python
# إرسال طلب POST بدون بيانات
response = requests.post('https://api.example.com/submit')

print("Status Code:", response.status_code)
print("Response Body:", response.text)
```

---

### إضافة الرؤوس
غالبًا ما تُستخدم الرؤوس للمصادقة، أو أنواع المحتوى، أو البيانات الوصفية المخصصة. قم بتمريرها كقاموس إلى المعامل `headers`.

```python
# تعريف رؤوس مخصصة
headers = {
    'Authorization': 'Bearer my_token',
    'Content-Type': 'application/json',
    'User-Agent': 'MyApp/1.0'
}

# إرسال طلب GET مع الرؤوس
response = requests.get('https://api.example.com/data', headers=headers)

print("Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Response Body:", response.text)
```

---

### إرسال بيانات JSON
لإرسال بيانات JSON في طلب POST (مثل اختيار JSON في علامة تبويب body في Postman)، استخدم المعامل `json`. هذا يضبط تلقائيًا `Content-Type` إلى `application/json`.

```python
# تعريف بيانات JSON
data = {
    'key1': 'value1',
    'key2': 'value2'
}

# إرسال طلب POST ببيانات JSON
response = requests.post('https://api.example.com/submit', json=data, headers=headers)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
```

---

### تحميل الملفات
لتحميل الملفات (مشابه لخيار form-data في Postman)، استخدم المعامل `files`. افتح الملفات في الوضع الثنائي (`'rb'`) وقم بتضمين بيانات النموذج الإضافية اختياريًا.

#### تحميل ملف بسيط
```python
# تحضير الملف للتحميل
files = {
    'file': open('myfile.txt', 'rb')
}

# إرسال طلب POST مع الملف
response = requests.post('https://api.example.com/upload', files=files)

print("Status Code:", response.status_code)
print("Response Body:", response.text)

# أغلق الملف يدويًا
files['file'].close()
```

#### تحميل ملف مع بيانات النموذج (النُهج الموصى به)
استخدام عبارة `with` يضمن إغلاق الملف تلقائيًا:
```python
# بيانات نموذج إضافية
form_data = {
    'description': 'My file upload'
}

# فتح وتحويل الملف
with open('myfile.txt', 'rb') as f:
    files = {
        'file': f
    }
    response = requests.post('https://api.example.com/upload', data=form_data, files=files)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
```

---

### استخدام الوكالات
لتوجيه الطلبات عبر وكيل (مشابه لإعدادات الوكيل في Postman)، استخدم المعامل `proxies` مع قاموس.

```python
# تعريف إعدادات الوكيل
proxies = {
    'http': 'http://myproxy:8080',
    'https': 'https://myproxy:8080'
}

# إرسال طلب عبر وكيل
response = requests.get('https://api.example.com/data', proxies=proxies)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
```

---

### التعامل مع الاستجابات والتحقق منها
توفر مكتبة `requests` وصولاً سهلاً إلى تفاصيل الاستجابة مثل رموز الحالة، وبيانات JSON، والرؤوس، وملفات تعريف الارتباط. يمكنك استخدام عبارات `assert` في Python للتحقق من صحة الاستجابات، مشابهًا لنصوص الاختبار في Postman.

#### تحليل استجابات JSON
```python
response = requests.get('https://api.example.com/data')

# التحقق من رمز الحالة وتحليل JSON
if response.status_code == 200:
    data = response.json()  # يحول الاستجابة إلى قاموس/قائمة Python
    print("JSON Data:", data)
else:
    print("Error:", response.status_code)
```

#### التحقق من تفاصيل الاستجابة
```python
response = requests.get('https://api.example.com/data')

# التحقق من رمز الحالة
assert response.status_code == 200, f"Expected 200, got {response.status_code}"

# تحليل JSON والتحقق من المحتوى
data = response.json()
assert 'key' in data, "Key not found in response"
assert data['key'] == 'expected_value', "Value does not match"

# التحقق من رؤوس الاستجابة
assert 'Content-Type' in response.headers, "Content-Type header missing"
assert response.headers['Content-Type'] == 'application/json', "Unexpected Content-Type"

# التحقق من ملفات تعريف الارتباط
cookies = response.cookies
assert 'session_id' in cookies, "Session ID cookie missing"

print("All assertions passed!")
```

#### معالجة الأخطاء
لف الطلبات في كتلة `try-except` لالتقاط أخطاء الشبكة أو HTTP:
```python
try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()  # يرفع استثناء لأخطاء 4xx/5xx
    data = response.json()
    print("Data:", data)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
```

---

### مثال شامل
إليك مثالاً كاملاً يجمع بين الرؤوس، وتحويل الملفات، والوكالات، والتحقق من الاستجابات:

```python
import requests

# تعريف الرؤوس
headers = {
    'Authorization': 'Bearer my_token'
}

# بيانات النموذج والملف
form_data = {
    'description': 'My file upload'
}

# إعدادات الوكيل
proxies = {
    'http': 'http://myproxy:8080',
    'https': 'https://myproxy:8080'
}

# إرسال طلب مع تحميل ملف
try:
    with open('myfile.txt', 'rb') as f:
        files = {'file': f}
        response = requests.post(
            'https://api.example.com/upload',
            headers=headers,
            data=form_data,
            files=files,
            proxies=proxies
        )
        response.raise_for_status()  # التحقق من أخطاء HTTP

        # تحليل والتحقق من الاستجابة
        data = response.json()
        assert 'upload_id' in data, "Upload ID not found in response"
        print("Upload successful, ID:", data['upload_id'])

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
```

---

### دوال قابلة لإعادة الاستخدام (استبدال Collections في Postman)
لتقليد الطلبات المحفوظة أو Collections في Postman، قم بتغليف المنطق في دوال:

```python
def upload_file(file_path, description, token, proxy=None):
    headers = {'Authorization': f'Bearer {token}'}
    data = {'description': description}
    proxies = {'http': proxy, 'https': proxy} if proxy else None

    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(
                'https://api.example.com/upload',
                headers=headers,
                data=data,
                files=files,
                proxies=proxies
            )
            response.raise_for_status()
            data = response.json()
            assert 'upload_id' in data, "Upload ID not found"
            return data['upload_id']
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None

# الاستخدام
upload_id = upload_file('myfile.txt', 'My file upload', 'my_token', 'http://myproxy:8080')
if upload_id:
    print("Upload successful, ID:", upload_id)
```

---

### ميزات إضافية
- **الجلسات**: استخدم `requests.Session()` للحفاظ على ملفات تعريف الارتباط أو الرؤوس عبر الطلبات.
- **المهلات**: أضف `timeout=5` (بالثواني) إلى الطلبات لتجنب التعلق.
- **إعادة التوجيه**: تحكم بها باستخدام `allow_redirects=True/False`.

---

### الملخص
باستخدام مكتبة `requests`، يمكنك:
- إرسال طلبات HTTP (`get`, `post`، إلخ)
- تضمين الرؤوس، وبيانات JSON، وتحويل الملفات
- استخدام الوكالات
- تحليل والتحقق من الاستجابات (الحالة، JSON، الرؤوس، ملفات تعريف الارتباط)
- تنظيم الكود في دوال قابلة لإعادة الاستخدام

هذا يمنحك بديلاً برمجيًا ومرنًا لـ Postman، مناسبًا للبرمجة النصية والأتمتة!