---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إضافة النصوص البرمجية التنفيذية إلى حزم Pip
translated: true
type: note
---

### إنشاء نصوص برمجية قابلة للتنفيذ في حزمة Python Pip

لتضمين نصوص برمجية قابلة للتنفيذ (أي أدوات سطر الأوامر) في حزمة Python يمكن تثبيتها عبر `pip`، تقوم بتعريف **نقاط الدخول (entry points)** في ملف التهيئة الخاص بحزمتك. هذا يسمح للمستخدمين بتشغيل نصوصك البرمجية مباشرة بعد التثبيت (مثل `my-script` من الطرفية).

سنستخدم مثالًا بسيطًا: حزمة تسمى `mytools` مع نص برمجي `greet` يطبع تحية.

#### الخطوة 1: إعداد هيكل الحزمة
أنشئ هيكل مجلدات كالتالي:

```
mytools/
├── pyproject.toml          # ملف تهيئة حديث (موصى به بدلاً من setup.py)
├── README.md
└── src/
    └── mytools/
        ├── __init__.py     # يجعلها حزمة
        └── greet.py        # منطق النص البرمجي الخاص بك
```

في `src/mytools/__init__.py` (يمكن أن يكون فارغًا أو يحتوي على معلومات الإصدار):
```python
__version__ = "0.1.0"
```

في `src/mytools/greet.py` (الدالة التي سيتصل بها النص البرمجي الخاص بك):
```python
import sys

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
```

#### الخطوة 2: تهيئة نقاط الدخول في `pyproject.toml`
استخدم قسم `[project.scripts]` لتعريف نصوص الكونسول. هذا يخبر pip بإنشاء أغلفة قابلة للتنفيذ.

```toml
[build-system]
requires = ["hatchling"]  # أو "setuptools", "flit"، إلخ.
build-backend = "hatchling.build"

[project]
name = "mytools"
version = "0.1.0"
description = "A simple tool package"
readme = "README.md"
requires-python = ">=3.8"
dependencies = []  # أضف تبعياتك هنا، مثلاً "requests"

[project.scripts]
greet = "mytools.greet:main"  # التنسيق: script_name = package.module:function
```

- `greet` هو الأمر الذي سيشغله المستخدمون (مثل `greet Alice`).
- `mytools.greet:main` يشير إلى دالة `main()` في `greet.py`.

إذا كنت تفضل استخدام `setup.py` القديم (لا يزال يعمل ولكن غير موصى به بشدة):
```python
from setuptools import setup, find_packages

setup(
    name="mytools",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "greet = mytools.greet:main"
        ]
    },
    # ... حقول أخرى مثل description, install_requires
)
```

#### الخطوة 3: بناء وتثبيت الحزمة
1.  ثبّت أدوات البناء: `pip install build twine` (أو `hatchling` إذا كنت تستخدم ذلك backend).

2.  ابنِ الحزمة:
    ```
    python -m build
    ```
    هذا ينشئ مجلد `dist/` بملفات `.tar.gz` و `.whl`.

3.  ثبّت محليًا للاختبار:
    ```
    pip install -e .  # وضع قابل للتعديل (التغييرات تنعكس فورًا)
    ```
    أو للتثبيت النظيف: `pip install dist/mytools-0.1.0-py3-none-any.whl`.

4.  اختبر: شغّل `greet Alice` في طرفيتك. يجب أن ينتج "Hello, Alice!".

#### الخطوة 4: التوزيع (اختياري)
-   رفع إلى PyPI: `twine upload dist/*` (يتطلب حساب PyPI).
-   يمكن للمستخدمين بعدها استخدام `pip install mytools` وتشغيل `greet`.

#### نصائح
-   **نصوص برمجية متعددة**: أضف المزيد من الأسطر إلى `[project.scripts]`، مثلاً `another-script = mytools.other:main`.
-   **الوسائط (Arguments)**: استخدم `argparse` في دالة `main()` الخاصة بك للتعامل الأفضل مع واجهة سطر الأوامر.
-   **التبعيات (Dependencies)**: اذكرها في `[project.dependencies]` (مثلاً `click` لأطر عمل واجهة سطر الأوامر).
-   **بيئة افتراضية (Virtual env)**: استخدمها دائمًا (`python -m venv env; source env/bin/activate`) لتجنب التعارضات.
-   **أخطاء؟** تحقق من `pip install --verbose` للتفاصيل. تأكد من أن الدالة الخاصة بك لا تأخذ وسائط (أو تتعامل مع `sys.argv`).

لإعدادات أكثر تقدمًا (مثل استخدام Poetry أو Flit)، راجع الوثائق الرسمية.

#### المراجع
-   [Python Packaging User Guide: Entry Points](https://packaging.python.org/en/latest/guides/writing-entry-points/)
-   [PyPI: Building and Publishing](https://packaging.python.org/en/latest/tutorials/packaging-projects/)