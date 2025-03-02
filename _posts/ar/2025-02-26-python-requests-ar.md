---
audio: false
generated: true
lang: ar
layout: post
title: مكتبة طلبات Python
translated: true
---

لإستبدال Postman بالكامل باستخدام مكتبة Python `requests`، يمكنك تنفيذ جميع العمليات الشائعة HTTP مثل إرسال أنواع مختلفة من الطلبات، معالجة الرؤوس، العمل مع بيانات JSON، تحميل الملفات، استخدام الوكالات، وإثبات الاستجابات. أدناه، سأقودك عبر أمثلة لكل من هذه الوظائف خطوة بخطوة، لضمان أن لديك دليلًا شاملًا وممارسًا.

### الخطوة 1: تثبيت مكتبة Requests
قبل البدء، تأكد من تثبيت مكتبة `requests`. قم بتشغيل هذا الأمر في مستودعك:

```bash
pip install requests
```

الآن، دعونا نغوص في الأمثلة.

---

### إرسال طلبات HTTP
دعمت مكتبة `requests` جميع طرق HTTP مثل GET، POST، PUT، DELETE، إلخ. إليك كيفية إرسال طلب GET و POST بسيط:

#### طلب GET
```python
import requests

# إرسال طلب GET
response = requests.get('https://api.example.com/data')

# طباعة رمز الحالة وجسم الاستجابة
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

### إضافة رؤوس
تستخدم الرؤوس غالبًا للتصديق، أنواع المحتوى، أو البيانات المتخصصة. قم بإرسالها كقائمة إلى معلمة `headers`.

```python
# تعريف رؤوس مخصصة
headers = {
    'Authorization': 'Bearer my_token',
    'Content-Type': 'application/json',
    'User-Agent': 'MyApp/1.0'
}

# إرسال طلب GET مع رؤوس
response = requests.get('https://api.example.com/data', headers=headers)

print("Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Response Body:", response.text)
```

---

### إرسال بيانات JSON
لإرسال بيانات JSON في طلب POST (مثل اختيار JSON في علامة Postman’s body)، استخدم معلمة `json`. هذا يحدد تلقائيًا `Content-Type` إلى `application/json`.

```python
# تعريف بيانات JSON
data = {
    'key1': 'value1',
    'key2': 'value2'
}

# إرسال طلب POST مع بيانات JSON
response = requests.post('https://api.example.com/submit', json=data, headers=headers)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
```

---

### تحميل الملفات
لتحميل الملفات (مثل خيار form-data في Postman)، استخدم معلمة `files`. افتح الملفات في وضع الثنائي (`'rb'`) وضمن البيانات الإضافية للموضوع.

#### تحميل ملف بسيط
```python
# إعداد الملف للتحميل
files = {
    'file': open('myfile.txt', 'rb')
}

# إرسال طلب POST مع الملف
response = requests.post('https://api.example.com/upload', files=files)

print("Status Code:", response.status_code)
print("Response Body:", response.text)

# إغلاق الملف يدويًا
files['file'].close()
```

#### تحميل ملف مع بيانات النموذج (الطريقة الموصى بها)
استخدام بيان `with` يضمن إغلاق الملف تلقائيًا:
```python
# بيانات النموذج الإضافية
form_data = {
    'description': 'My file upload'
}

# فتح وتحميل الملف
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
لإعادة توجيه الطلبات عبر وكالة (مثل إعدادات وكالة Postman)، استخدم معلمة `proxies` مع قائمة.

```python
# تعريف إعدادات الوكالة
proxies = {
    'http': 'http://myproxy:8080',
    'https': 'https://myproxy:8080'
}

# إرسال طلب عبر وكالة
response = requests.get('https://api.example.com/data', proxies=proxies)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
```

---

### معالجة وإثبات الاستجابات
توفر مكتبة `requests` وصولًا سهلًا إلى تفاصيل الاستجابة مثل رموز الحالة، بيانات JSON، الرؤوس، والمعجنات. يمكنك استخدام بيان `assert` في Python لتأكيد الاستجابات، مثل Scripts اختبار Postman.

#### تحليل استجابات JSON
```python
response = requests.get('https://api.example.com/data')

# التحقق من رمز الحالة وتحليل JSON
if response.status_code == 200:
    data = response.json()  # تحويل الاستجابة إلى قائمة/قائمة Python
    print("JSON Data:", data)
else:
    print("Error:", response.status_code)
```

#### إثبات تفاصيل الاستجابة
```python
response = requests.get('https://api.example.com/data')

# إثبات رمز الحالة
assert response.status_code == 200, f"Expected 200, got {response.status_code}"

# تحليل JSON وإثبات المحتوى
data = response.json()
assert 'key' in data, "Key not found in response"
assert data['key'] == 'expected_value', "Value does not match"

# التحقق من رؤوس الاستجابة
assert 'Content-Type' in response.headers, "Content-Type header missing"
assert response.headers['Content-Type'] == 'application/json', "Unexpected Content-Type"

# التحقق من المعجنات
cookies = response.cookies
assert 'session_id' in cookies, "Session ID cookie missing"

print("All assertions passed!")
```

#### معالجة الأخطاء
أغلف الطلبات في كتلة `try-except` لالتقاط الأخطاء الشبكية أو HTTP:
```python
try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()  # يرفع استثناءًا للأخطاء 4xx/5xx
    data = response.json()
    print("Data:", data)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
```

---

### مثال شامل
هنا مثال شامل يجمع بين الرؤوس، تحميل الملف، الوكالات، وإثبات الاستجابات:

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

# إعدادات الوكالة
proxies = {
    'http': 'http://myproxy:8080',
    'https': 'https://myproxy:8080'
}

# إرسال الطلب مع تحميل الملف
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
        response.raise_for_status()  # التحقق من الأخطاء HTTP

        # تحليل وإثبات الاستجابة
        data = response.json()
        assert 'upload_id' in data, "Upload ID not found in response"
        print("Upload successful, ID:", data['upload_id'])

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
```

---

### وظائف قابلة لإعادة الاستخدام (إستبدال مجموعات Postman)
لتمثيل طلبات Postman المحفوظة أو المجموعات، قم بتحفيز المنطقية في وظائف:

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
- **جلسات**: استخدم `requests.Session()` للحفاظ على المعجنات أو الرؤوس عبر الطلبات.
- **أوقات الانتظار**: أضف `timeout=5` (ثواني) إلى الطلبات لمنع التعلق.
- **إعادة التوجيه**: التحكم بها مع `allow_redirects=True/False`.

---

### ملخص
مع مكتبة `requests`، يمكنك:
- إرسال طلبات HTTP (`get`, `post`, إلخ.)
- تضمين الرؤوس، بيانات JSON، وتحميل الملفات
- استخدام الوكالات
- تحليل وإثبات الاستجابات (الحالة، JSON، الرؤوس، المعجنات)
- تنظيم الكود في وظائف قابلة لإعادة الاستخدام

هذا يوفر لك بديلًا برمجيًا مرنًا لـ Postman، مناسبًا للبرمجة والتوظيف!