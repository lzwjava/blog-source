---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تحليل ملف طلبات الإعداد
translated: true
type: note
---

### نظرة عامة
هذا ملف `setup.py`، وهو برنامج نصي قياسي في Python يُستخدم مع `setuptools` لتعريف وحزمة Python. على وجه التحديد، هذا الملف مخصص لمكتبة **Requests**—عميل HTTP شهير لـ Python. يتعامل مع البيانات الوصفية مثل اسم الحزمة، الإصدار، التبعيات، والمصنفات (لتوزيع PyPI). عندما تقوم بتشغيل `pip install requests`، هذا البرنامج النصي (أو نتائجه المُجمَّعة) هو ما يتم تنفيذه خلف الكواليس لتثبيت الحزمة.

هيكل البرنامج النصي هو استدعاء دالة `setup()` واحدة، ولكنه يتضمن بعض الحواجز، المساعدين، وقراءات ديناميكية من ملفات أخرى. سأقوم بتحليله قسمًا بقسم.

### 1. الاستيرادات والتحقق من إصدار Python
```python
#!/usr/bin/env python
import os
import sys
from codecs import open

from setuptools import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 9)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    # رسالة خطأ وخروج
    sys.exit(1)
```
- **السطر الأول (Shebang) (`#!/usr/bin/env python`)**: يجعل الملف قابلاً للتنفيذ في أنظمة تشبه Unix، مما يؤدي إلى تشغيله بمفسر Python الخاص بالنظام.
- **الاستيرادات**: تجلب `os` و `sys` للتفاعل مع النظام، و `codecs.open` لقراءة الملفات بترميز UTF-8 (للتعامل مع الأحرف غير ASCII بأمان)، و `setup` من `setuptools` لبناء الحزمة.
- **التحقق من الإصدار**: يضمن أن المستخدم يشغل Python 3.9 أو أعلى. إذا لم يكن الأمر كذلك، فإنه يطبع رسالة خطأ مفيدة تقترح التحديث أو التثبيت على إصدار أقدم من Requests (<2.32.0)، ثم يخرج بالرمز 1 (فشل). يفرض هذا التوافق، حيث توقفت Requests عن دعم إصدارات Python الأقدم.

### 2. اختصار النشر
```python
if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()
```
- تسهيل للمشرفين: إذا قمت بتشغيل `python setup.py publish`، فإنه:
  - يبني أرشيفات توزيع المصدر (`sdist`) والعجلة (`bdist_wheel`) في مجلد `dist/`.
  - يرفعها إلى PyPI باستخدام `twine` (أداة رفع آمنة).
- هذه طريقة سريعة لإصدار نسخة جديدة دون أوامر يدوية. يخرج بعد التشغيل.

### 3. التبعيات
```python
requires = [
    "charset_normalizer>=2,<4",
    "idna>=2.5,<4",
    "urllib3>=1.21.1,<3",
    "certifi>=2017.4.17",
]
test_requirements = [
    "pytest-httpbin==2.1.0",
    "pytest-cov",
    "pytest-mock",
    "pytest-xdist",
    "PySocks>=1.5.6, !=1.5.7",
    "pytest>=3",
]
```
- **`requires`**: التبعيات الأساسية المثبتة عند تشغيل `pip install requests`. تتعامل هذه مع الترميز (`charset_normalizer`)، وأسماء النطاقات الدولية (`idna`)، ونقل HTTP (`urllib3`)، وشهادات SSL (`certifi`).
- **`test_requirements`**: تُثبت فقط إذا قمت بتشغيل الاختبارات (على سبيل المثال، عبر `pip install -e '.[tests]'`). تتضمن أدوات اختبار مثل `pytest` المتغيرات لمحاكاة HTTP، والتغطية، والاختبار المتوازي. `PySocks` مخصص لدعم وكيل SOCKS في الاختبارات.

### 4. تحميل البيانات الوصفية الديناميكية
```python
about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "src", "requests", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", "utf-8") as f:
    readme = f.read()
```
- **قاموس `about`**: يقرأ البيانات الوصفية من `src/requests/__version__.py` (على سبيل المثال، `__title__`، `__version__`، `__description__`، إلخ) باستخدام `exec()`. يحافظ هذا على تركيز معلومات الإصدار—قم بتحديثها مرة واحدة، و `setup.py` يسحبها.
- **`readme`**: يحمّل ملف `README.md` بأكمله كسلسلة نصية للوصف الطويل للحزمة على PyPI.

### 5. استدعاء الدالة الرئيسية `setup()`
هذا هو جوهر الملف. يقوم بتكوين الحزمة للبناء/التثبيت:
```python
setup(
    name=about["__title__"],  # على سبيل المثال، "requests"
    version=about["__version__"],  # على سبيل المثال، "2.32.3"
    description=about["__description__"],  # ملخص قصير
    long_description=readme,  # README كامل
    long_description_content_type="text/markdown",  # يتم عرضه كـ Markdown على PyPI
    author=about["__author__"],  # على سبيل المثال، "Kenneth Reitz"
    author_email=about["__author_email__"],
    url=about["__url__"],  # على سبيل المثال، مستودع GitHub
    packages=["requests"],  # يثبت حزمة 'requests'
    package_data={"": ["LICENSE", "NOTICE"]},  # يتضمن ملفات غير Python
    package_dir={"": "src"},  # الكود المصدري في 'src/'
    include_package_data=True,  # يسحب جميع ملفات البيانات
    python_requires=">=3.9",  # يعكس التحقق من الإصدار
    install_requires=requires,  # من القسم السابق
    license=about["__license__"],  # على سبيل المثال، "Apache 2.0"
    zip_safe=False,  # يسمح بتحرير الملفات المثبتة (شائع للمكتبات)
    classifiers=[  # فئات PyPI لإمكانية الاكتشاف
        "Development Status :: 5 - Production/Stable",
        # ... (القائمة الكاملة تشمل إصدارات Python، نظام التشغيل، المواضيع)
    ],
    tests_require=test_requirements,  # لـ `pip install -e '.[tests]'`
    extras_require={  # تبعيات اختيارية
        "security": [],  # فارغ—ربما للاستخدام المستقبلي
        "socks": ["PySocks>=1.5.6, !=1.5.7"],  # دعم وكيل SOCKS
        "use_chardet_on_py3": ["chardet>=3.0.2,<6"],  # تراجع ترميز قديم
    },
    project_urls={  # روابط على صفحة PyPI
        "Documentation": "https://requests.readthedocs.io",
        "Source": "https://github.com/psf/requests",
    },
)
```
- **الوسائط الرئيسية**:
  - **الاسم/الإصدار/الوصف**: مسحوبة من `__version__.py` لسهولة الصيانة.
  - **الحزم/دليل الحزمة**: يخبر setuptools أن الحزمة موجودة تحت `src/requests/` وأن يقوم بتثبيتها كـ `import requests`.
  - **المصنفات**: قائمة من السلاسل النصية التي تصنف الحزمة (على سبيل المثال، مستقرة، Python 3.9+، رخصة Apache، موضوع ويب/HTTP). يساعد هذا المستخدمين في العثور عليها على PyPI.
  - **التبعيات الإضافية**: تسمح للمستخدمين بتثبيت ميزات اختيارية، مثل `pip install requests[socks]` لدعم الوكيل.
  - **روابط المشروع**: يضيف روابط قابلة للنقر للوثائق والمصدر على صفحة PyPI.

### كيف يعمل عمليًا
- **التثبيت**: `pip install .` (من المستودع) أو `pip install requests` (من PyPI) يشغل هذا لنسخ الملفات، تثبيت التبعيات، وإعداد الحزمة.
- **البناء**: `python setup.py sdist` ينشئ أرشيفات قابلة للتوزيع.
- **لماذا هذا الهيكل؟**: إنه "هيكل src" (الكود في `src/`)، وهو أفضل ممارسة حديثة لتجنب الاستيراد العرضي أثناء التطوير. الملف مكتوب ذاتيًا ولكنه يفوض التفاصيل إلى ملفات أخرى مثل `__version__.py`.

هذا الملف setup.py مأخوذ من المستودع الرسمي لـ Requests ولم يتغير كثيرًا عبر الإصدارات—لقد تم اختباره جيدًا من أجل الموثوقية.

### المراجع
- [Requests Documentation](https://requests.readthedocs.io/en/latest/)
- [Requests GitHub Repository](https://github.com/psf/requests)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)