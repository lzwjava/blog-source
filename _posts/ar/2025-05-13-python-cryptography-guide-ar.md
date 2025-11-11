---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: دليل التشفير في بايثون
translated: true
type: note
---

### مقدمة عن حزمة التشفير (Cryptography)
حزمة `cryptography` هي مكتبة بايثون شائعة توفر أساسيات التشفير ووصفات لبروتوكولات آمنة. تركز على سهولة الاستخدام والأمان، وتنفذ معايير مثل AES وRSA والمزيد. لا تُستخدم لتنفيذ بروتوكولات عالية المستوى مثل SSH أو TLS مباشرة—استخدمها كلبنة بناء. تأكد دائمًا من تحديثها بانتظام للحصول على تصحيحات الأمان.

### التثبيت
ثبّت عبر pip:
```bash
pip install cryptography
```
لتحسين الأداء (خاصة للمفاتيح الكبيرة أو العمليات المتكررة)، ثبّت مع دعم OpenSSL:
```bash
pip install cryptography[openssl]
```
ملاحظة: في بعض الأنظمة، قد تحتاج إلى تثبيت رؤوس OpenSSL بشكل منفصل (مثل `apt install libssl-dev` على أوبونتو).

### المفاهيم الأساسية
- **الأساسيات (Primitives)**: عمليات منخفضة المستوى مثل التشفير/فك التشفير.
- **الوصفات (Recipes)**: وظائف عالية المستوى وموجهة (مثل Fernet للتشفير المتماثل).
- **تحذيرات المخاطر (Hazard Warnings)**: تستخدم المكتبة تحذيرات للاستخدام غير الآمن—انتبه لها.

استورد المكتبة:
```python
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes, asyncioc as a
from cryptography.hazmat.primitives.asymmetric import rsa, padding
```

### أمثلة

#### 1. التشفير المتماثل باستخدام Fernet (الأسهل للمبتدئين)
يستخدم Fernet نمط AES-128 في CBC مع HMAC لضمان السلامة. مثالي لتخزين البيانات المشفرة.

```python
from cryptography.fernet import Fernet

# إنشاء مفتاح (خزنه بأمان، مثل متغيرات البيئة)
key = Fernet.generate_key()
cipher = Fernet(key)

# تشفير
plaintext = b"This is a secret message."
token = cipher.encrypt(plaintext)
print("Encrypted:", token)

# فك التشفير
decrypted = cipher.decrypt(token)
print("Decrypted:", decrypted)
```
- **ملاحظات**: المفاتيح بصيغة base64 آمنة للروابط (44 حرفًا). لا تخزن المفاتيح مباشرة في الكود؛ قم بتدويرها دوريًا.

#### 2. التشفير غير المتماثل باستخدام RSA
أنشئ زوج مفاتيح عام/خاص وقم بتشفير البيانات التي يمكن فقط لحامل المفتاح الخاص فكها.

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# إنشاء مفتاح خاص
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# تسلسل المفتاح للتخزين
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()  # استخدم BestAvailableEncryption() لحماية بكلمة مرور
)

# الحصول على المفتاح العام وتسلسله
public_key = private_key.public_key()
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# التشفير باستخدام المفتاح العام
plaintext = b"Secret message"
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

# فك التشفير باستخدام المفتاح الخاص
decrypted = private_key.decrypt(
    ciphertext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)
print("Decrypted:", decrypted)
```
- **ملاحظات**: RSA بطيء للبيانات الكبيرة؛ استخدمه لتبادل المفاتيح أو الرسائل الصغيرة. الحشو OAEP يمنع الهجمات.

#### 3. إنشاء واستخدام التجزئة (Hashes)
لفحص السلامة أو تجزئة كلمات المرور.

```python
from cryptography.hazmat.primitives import hashes

# تجزئة البيانات
digest = hashes.Hash(hashes.SHA256())
digest.update(b"Some data")
hash_result = digest.finalize()
print("SHA256 Hash:", hash_result.hex())
```

لكلمات المرور، استخدم `cryptography.hazmat.primitives.kdf.pbkdf2` لاشتقاق المفاتيح (مثل PBKDF2 للتجزئة البطيئة المملحة).

#### 4. التوقيعات الرقمية باستخدام RSA
وقّع البيانات لإثبات صحتها.

```python
# باستخدام مفاتيح RSA من الأمثلة السابقة
message = b"Data to sign"
signature = private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)

# التحقق باستخدام المفتاح العام
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    print("Signature valid")
except Exception:
    print("Signature invalid")
```

### أفضل الممارسات
- **إدارة المفاتيح**: خزن المفاتيح بأمان (مثل استخدام AWS KMS أو وحدات الأمان المادية). لا تعيد استخدام المفاتيح مطلقًا.
- **الحشو والأنماط**: استخدم دائمًا حشوًا آمنًا (مثل OAEP لـ RSA وGCM لـ AES).
- **العشوائية**: استخدم `os.urandom()` أو وحدة `secrets` للبذور؛ تجنب `random`.
- **التحديثات**: التشفير يتطور—تحقق من الثغرات الأمنية في استخدامك.
- **تجنب التطوير الذاتي**: للاحتياجات المعقدة، استخدم الوصفات أو ادمج مع مكتبات عالية المستوى مثل `pyjwt` أو `boto3`.
- **الاختبار**: استخدم ثوابت واستثناءات المكتبة لمعالجة الأخطاء.

### قراءات إضافية
- [الوثائق الرسمية](https://cryptography.io/en/latest/) – مرجع مفصل للواجهة وبرامج تعليمية.
- [صفحة PyPI](https://pypi.org/project/cryptography/) – تاريخ الإصدارات والتكاملات.
- للمواضيع المتقدمة، استكشف ويكي `cryptography` أو RFCs (مثل RFC 8017 لـ PKCS#1).

إذا كان لديك حالة استخدام محددة (مثل تشفير الملفات أو أمان واجهات البرمجة)، قدم المزيد من التفاصيل للحصول على أمثلة مخصصة.