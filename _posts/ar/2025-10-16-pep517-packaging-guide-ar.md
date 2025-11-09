---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: دليل تعبئة بايثون PEP 517
translated: true
type: note
---

PEP 517، الذي تم قبوله في عام 2016، يحدد واجهة موحدة لبناء حزم Python التي تفصل بين خلفية البناء (المنطق الخاص بإنشاء التوزيعات) وواجهة المستخدم (الأدوات مثل pip التي تنسق العملية). هذا يسمح للمطورين باستخدام أدوات البناء الحديثة دون أن يكونوا مقيدين بالأنظمة القديمة مثل `setup.py` في setuptools. بالاقتران مع PEP 518 (الذي يحدد تبعيات البناء)، فإنه يمكّن من إجراء عمليات بناء معزولة وموثوقة من أشجار المصدر أو توزيعات المصدر (sdists). اعتبارًا من عام 2025، يُعد PEP 517 الأساس لتعبئة Python الحديثة، وهو مدعوم من قبل pip (بدءًا من الإصدار 10 لـ PEP 518 والإصدار 19 لـ PEP 517 الكامل) وأدوات مثل Poetry وFlit وPDM.

يغطي هذا الدافع، والمفاهيم الأساسية، والمواصفات، وسير العمل، والتنفيذ، وأفضل الممارسات.

## الدافع والخلفية

تطورت تعبئة Python من `distutils` (الذي تم تقديمه في Python 1.6، عام 2000) إلى `setuptools` (2004)، والذي أضاف إدارة التبعيات لكنه أدخل مشاكل:
- **أمرية وهشة**: اعتمدت عمليات البناء على تنفيذ `python setup.py`، وهو نص برمجي تعسفي يمكن أن يفشل بسبب افتراضات البيئة (مثل عدم وجود Cython للملحقات).
- **لا توجد تبعيات بناء**: الأدوات اللازمة للبناء (مثل المترجمات، Cython) لم يتم الإعلان عنها، مما أدى إلى تثبيت يدوي وتعارضات في الإصدارات.
- **اقتران شديد**: كان Pip يثبّت استدعاء `setup.py` بشكل ثابت، مما يحظر أنظمة البناء البديلة مثل Flit أو Bento.
- **تلوث بيئة المضيف**: استخدمت عمليات البناء بيئة Python العالمية للمستخدم، مما يعرضها لخطر الآثار الجانبية.

هذه المشاكل خنقت الابتكار وتسببت في أخطاء أثناء تثبيت المصدر (مثال: من Git). يحل PEP 517 هذه المشكلة من خلال توحيد واجهة دنيا: تستدعي واجهات المستخدم خطافات الخلفية في بيئات معزولة. تبسط العجلات (الملفات الثنائية المبنية مسبقًا، تم تقديمها عام 2014) التوزيع — تحتاج الخلفيات فقط إلى إنتاج عجلات/توزيعات مصدر متوافقة. يكمل PEP 518 ذلك من خلال الإعلان عن متطلبات البناء في `pyproject.toml`، مما يمكن العزل.

النتيجة: نظام بيئي تصريحي وقابل للتوسع حيث `setup.py` اختياري، ويمكن لأدوات مثل pip بناء أي مشروع متوافق بدون اللجوء إلى الأنظمة القديمة.

## المفاهيم الأساسية

### أشجار المصدر والتوزيعات
- **شجرة المصدر**: دليل (مثل نسخة من نظام التحكم بالإصدار VCS) يحتوي على كود الحزمة وملف `pyproject.toml`. أدوات مثل `pip install .` تبني منه.
- **توزيع المصدر (Sdist)**: أرشيف مضغوط (`.tar.gz`) مثل `package-1.0.tar.gz`، يُفك إلى دليل `{name}-{version}` يحتوي على `pyproject.toml` وبيانات وصفية (PKG-INFO). يُستخدم للإصدارات والتعبئة اللاحقة (مثل Debian).
- **العجلة**: توزيع ثنائي `.whl` — مبني مسبقًا، خاص بالمنصة، وقابل للتثبيت دون تجميع. يفرض PEP 517 استخدام العجلات لإمكانية إعادة الإنتاج.

توزيعات المصدر القديمة (ما قبل PEP 517) تُفك إلى أشجار قابلة للتنفيذ ولكن يجب أن تتضمن الآن `pyproject.toml` للتوافق.

### pyproject.toml
هذا الملف TOML يركّز التهيئة. قسم `[build-system]` (من PEP 518/517) يحدد:
- `requires`: قائمة تبعيات PEP 508 اللازمة للبناء (مثال: `["setuptools>=40.8.0", "wheel"]`).
- `build-backend`: نقطة الدخول إلى الخلفية (مثال: `"setuptools.build_meta"` أو `"poetry.masonry.api"`).
- `backend-path` (اختياري): مسارات داخل الشجرة تُضاف إلى `sys.path` للخلفيات المستضافة ذاتيًا (مثال: `["src/backend"]`).

مثال على التهيئة الدنيا:
```
[build-system]
requires = ["setuptools>=40.8.0", "wheel"]
build-backend = "setuptools.build_meta"
```

تشكل المتطلبات رسمًا بيانيًا دوريًا غير موجه (بدون حلقات؛ تكتشف واجهات المستخدم ذلك وتفشل). الأقسام الأخرى مثل `[project]` (PEP 621) أو `[tool.poetry]` تحتوي على البيانات الوصفية/التبعيات.

### خلفيات البناء وواجهات المستخدم
- **الخلفية**: تنفذ منطق البناء عبر الخطافات (وظائف قابلة للاستدعاء). تعمل في عملية فرعية من أجل العزل.
- **واجهة المستخدم**: تنسق (مثل pip). تُنشئ العزل، تثبّت المتطلبات، تستدعي الخطافات.
- **فصل الاقتران**: تستدعي واجهات المستخدم خطافات موحدة، وليس `setup.py`. هذا يدعم خلفيات متنوعة بدون تغييرات على pip.

تستخدم الخطافات `config_settings` (قاموس للإشارات، مثال: `{"--debug": true}`) وقد تُخرج إلى stdout/stderr (بتنسيق UTF-8).

## المواصفات

### تفاصيل [build-system]
- `requires`: سلاسل نصية من PEP 508 (مثال: `">=1.0; sys_platform == 'win32'"`).
- `build-backend`: `module:object` (مثال: `flit_core.buildapi` يستورد `flit_core; backend = flit_core.buildapi`).
- لا تلوث لـ sys.path — الخلفيات تستورد عبر العزل.

### الخطافات
تعرض الخلفيات هذه كسمات:

**إلزامية:**
- `build_wheel(wheel_directory, config_settings=None, metadata_directory=None) -> str`: يبني عجلة في `wheel_directory`، يُرجع اسم الملف الأساسي (مثال: `"myproj-1.0-py3-none-any.whl"`). يستخدم البيانات الوصفية السابقة إذا وُفرت. يتعامل مع المصادر للقراءة فقط عبر الملفات المؤقتة.
- `build_sdist(sdist_directory, config_settings=None) -> str`: يبني توزيع مصدر في `sdist_directory` (بتنسيق pax، UTF-8). يرفع استثناء `UnsupportedOperation` إذا كان مستحيلاً (مثال: لا يوجد نظام تحكم بالإصدار VCS).

**اختيارية (القيم الافتراضية `[]` أو بدائل احتياطية):**
- `get_requires_for_build_wheel(config_settings=None) -> list[str]`: تبعيات إضافية للعجلة (مثال: `["cython"]`).
- `prepare_metadata_for_build_wheel(metadata_directory, config_settings=None) -> str`: يكتب البيانات الوصفية `{pkg}-{ver}.dist-info` (حسب مواصفات العجلة، بدون RECORD). يُرجع اسم الملف الأساسي؛ تستخرج واجهات المستخدم البيانات من العجلة إذا كانت مفقودة.
- `get_requires_for_build_sdist(config_settings=None) -> list[str]`: تبعيات إضافية لتوزيع المصدر.

ترفع الخطافات استثناءات للأخطاء. تستدعي واجهات المستخدم في بيئات معزولة (مثال: بيئة افتراضية تحتوي فقط على المكتبة القياسية + المتطلبات).

### بيئة البناء
- بيئة افتراضية معزولة: تهيئة أولية لـ `get_requires_*`، كاملة للبناء.
- أدوات سطر الأوامر (مثال: `flit`) في PATH.
- لا يوجد stdin؛ عمليات فرعية لكل خطاف.

## كيف تعمل عملية البناء

### سير العمل خطوة بخطوة
لـ `pip install .` (شجرة مصدر) أو تثبيت توزيع مصدر:

1.  **الاكتشاف**: تقرأ واجهة المستخدم `pyproject.toml`.
2.  **إعداد العزل**: إنشاء بيئة افتراضية؛ تثبيت `requires`.
3.  **استعلام المتطلبات**: استدعاء `get_requires_for_build_wheel` (تثبيت الإضافات).
4.  **تحضير البيانات الوصفية**: استدعاء `prepare_metadata_for_build_wheel` (أو بناء العجلة واستخراج البيانات).
5.  **بناء العجلة**: استدعاء `build_wheel` في بيئة معزولة؛ تثبيت العجلة الناتجة.
6.  **البدائل الاحتياطية**: إذا كان توزيع المصدر غير مدعوم، ابني عجلة؛ إذا لم توجد خطافات، استخدم `setup.py` القديم.

لتوزيعات المصدر: فك الضغط، عالج كشجرة مصدر. سير عمل المطور (مثال: `pip wheel .`):
1.  عزل البيئة.
2.  استدعاء خطافات الخلفية لبناء العجلة/توزيع المصدر.

### عزل البناء (PEP 518)
ينشئ بيئة افتراضية مؤقتة للبناء، متجنبًا تلوث المضيف. `--no-build-isolation` في pip يعطل هذا (استخدم بحذر). الأدوات مثل tox تفترض العزل افتراضيًا.

القديم مقابل الجديد:
- **القديم**: `python setup.py install` في بيئة المضيف — مخاطر تعارض.
- **الجديد**: خطافات معزولة — قابلة لإعادة الإنتاج، آمنة.

## تنفيذ خلفية بناء

لإنشاء واحدة:
1.  حدد وحدة تحتوي على خطافات (مثال: `mybackend.py`).
2.  وجّه `build-backend` إليها.

مثال بسيط (حزمة Python خالصة):
```python
# mybackend.py
from zipfile import ZipFile
import os
from pathlib import Path

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    # انسخ المصدر إلى دليل العجلات، وضغط كـ .whl
    dist = Path(wheel_directory) / "myproj-1.0-py3-none-any.whl"
    with ZipFile(dist, 'w') as z:
        for src in Path('.').rglob('*'):
            z.write(src, src.relative_to('.'))
    return str(dist.relative_to(wheel_directory))

# خطافات اختيارية
def get_requires_for_build_wheel(config_settings=None):
    return []

def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    # اكتب METADATA، إلخ.
    return "myproj-1.0.dist-info"
```

في `pyproject.toml`:
```
[build-system]
requires = []
build-backend = "mybackend:build_wheel"  # يشير فعليًا إلى كائن الوحدة
```

استخدم مكتبات مثل `pyproject-hooks` للنماذج الجاهزة. للملحقات، ادمج مترجمات C عبر `config_settings`.

## استخدام PEP 517 مع الأدوات

- **pip**: يكتشف `pyproject.toml` تلقائيًا؛ استخدم `--use-pep517` (افتراضي منذ 19.1). للوضع القابل للتعديل: `pip install -e .` يستدعي الخطافات.
- **Poetry**: أداة تصريحية. تُنشئ:
  ```
  [build-system]
  requires = ["poetry-core>=1.0.0"]
  build-backend = "poetry.core.masonry.api"
  ```
  التثبيت عبر `poetry build`؛ متوافق مع pip.
- **Flit**: بسيط لـ Python الخالص. يستخدم:
  ```
  [build-system]
  requires = ["flit_core >=3.2,<4"]
  build-backend = "flit_core.buildapi"
  ```
  `flit publish` يبني/يرفع.
- **Setuptools**: جسر للتراث:
  ```
  [build-system]
  requires = ["setuptools>=40.8.0", "wheel"]
  build-backend = "setuptools.build_meta"
  ```
  يدعم `setup.cfg` للبيانات الوصفية التصريحية.

الهجرة من النظام القديم: أضف `[build-system]`؛ أزل استدعاءات `setup.py`.

## معالجة الأخطاء وأفضل الممارسات

- **الأخطاء**: ترفع الخطافات استثناءات (مثال: `ValueError` لتهيئة غير صالحة). الحلقات: تفشل واجهة المستخدم مع رسالة. توزيع المصدر غير المدعوم: البديل الاحتياطي هو العجلة.
- **أفضل الممارسات**:
  - فضّل التصريحية (`setup.cfg` أو `[project]`).
  - عيّن تبعيات البناء بدقة (مثال: `cython==0.29`).
  - اختبر العزل: `pip wheel . --no-build-isolation` لتصحيح الأخطاء.
  - للخلفيات داخل الشجرة: استخدم `backend-path`؛ تجنب الحلقات.
  - الأمان: الخطافات في عمليات فرعية؛ لا يوجد كود تعسفي.
  - التوافق: ضمّن `setup.py` للأدوات القديمة.

اعتبارًا من عام 2025، يهيمن setuptools (حسب الاستبيانات)، لكن اعتماد Poetry/Flit ينمو بسبب البساطة.

## المراجع
- [PEP 517 – A build-system independent format for source trees](https://peps.python.org/pep-0517/)
- [PEP 517 and 518 in Plain English](https://chadsmith-software.medium.com/pep-517-and-518-in-plain-english-47208ca8b7a6)
- [Python packaging - Past, Present, Future](https://bernat.tech/posts/pep-517-518/)
- [What is PEP 517/518 compatibility?](https://pydevtools.com/handbook/explanation/what-is-pep-517/)
- [Modern pip build process (–use-pep517)](https://fromkk.com/posts/modern-pip-build-process-use-pep517/)
- [What is a build backend?](https://pydevtools.com/handbook/explanation/what-is-a-build-backend/)