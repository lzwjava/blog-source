---
audio: false
generated: true
image: false
lang: ar
layout: post
title: دليل أساسيات التغطية في بايثون
translated: true
type: note
---

إليك مقدمة عملية تركز على المطورين لحزمة **coverage** (coverage.py) — ما الذي تقيسه، وكيفية استخدامها بشكل جيد، والإعدادات التي ستهتم بها فعليًا.

# ما هي coverage.py

* أداة بايثون **تقيس أي الأسطر والفروع في الكود الخاص بك تعمل** أثناء الاختبارات أو أي تنفيذ.
* تُخرج تقاريرًا بصيغ **نص، HTML، XML، و JSON** حتى تتمكن من رؤية الفجوات وربطها ببوابات الجودة في التكامل المستمر (CI).
* تعمل مع unittest، pytest، nose، أو النصوص البرمجية العادية.

# المفاهيم الأساسية (بعبارات بسيطة)

* **تغطية الأسطر**: هل تم تنفيذ السطر مرة واحدة على الأقل؟
* **تغطية الفروع**: هل تم تنفيذ كل فرع محتمل من قرار ما؟ (if/else، الدوائر القصيرة المنطقية boolean short-circuit، الاستثناءات، الـ comprehensions، إلخ)
* **اختيار المصدر**: قم بقياس الكود الخاص بك فقط لتجنب الضوضاء من venv/site-packages.
* **تخزين البيانات**: عمليات التشغيل تنشئ ملف بيانات `.coverage` (SQLite)؛ يمكنك دمج عمليات تشغيل عديدة.
* **السياقات**: ضع علامات على التنفيذ باستخدام تسميات (مثل، لكل اختبار)، حتى تتمكن من تقسيم التقارير حسب أسماء الاختبارات، الأوامر، إلخ.

# البدء السريع

```bash
# 1) التثبيت
pip install coverage

# 2) شغّل اختباراتك تحت coverage (pytest مجرد مثال)
coverage run -m pytest

# 3) اعرض تقريرًا في الطرفية (مع أرقام الأسطر المفقودة)
coverage report -m

# 4) أنشئ تقرير HTML (افتح htmlcov/index.html في المتصفح)
coverage html

# اختياري: تقارير قابلة للقراءة آليًا
coverage xml        # لأدوات CI مثل Sonar، Jenkins، Azure DevOps
coverage json       # للتحليل البرمجي
```

# إعداد .coveragerc الموصى به

أنشئ ملف تكوين في جذر مستودعك لجعل النتائج متسقة محليًا وفي CI.

```ini
[run]
# قم بقياس حزمك فقط لتقليل الضوضاء
source = src, your_package
branch = True
parallel = True                 # اسمح لعمليات/تشغيلات متعددة بكتابة بياناتها الخاصة
relative_files = True           # مسارات أنظف في التقارير (ملائمة لـ CI)
concurrency = thread, multiprocessing

# يمكنك أيضًا استبعاد ملفات أو أنماط كليًا
omit =
    */tests/*
    */.venv/*
    */site-packages/*
    */migrations/*

[report]
show_missing = True
skip_covered = False            # اضبط على True إذا أردت تقريرًا أقصر
fail_under = 90                 # اجعل CI يفشل إذا كانت التغطية أقل من 90%
exclude_lines =
    pragma: no cover            # التوجيه القياسي pragma لتجاهل الأسطر
    if TYPE_CHECKING:
    raise NotImplementedError

[html]
directory = htmlcov
title = Coverage Report

[xml]
output = coverage.xml

[json]
output = coverage.json

[paths]
# مفيد عند دمج البيانات من أجهزة/حاويات مختلفة
source =
    src
    */workspace/src
    */checkouts/your_repo/src
```

# قياس العمليات الفرعية والتشغيلات المتوازية

إذا كان الكود الخاص بك يُنشئ عمليات فرعية (multiprocessing، أدوات CLI)، قم بإعداد **تغطية العمليات الفرعية**:

1. في `[run]`، حافظ على `parallel = True`.
2. صدّر متغير بيئة حتى تبدأ العمليات الفرعية coverage تلقائيًا بنفس التكوين:

```bash
export COVERAGE_PROCESS_START=$(pwd)/.coveragerc
```

3. شغّل برنامجك/اختباراتك بشكل طبيعي (أو لا يزال عبر `coverage run -m ...`).
4. بعد انتهاء جميع عمليات التشغيل، ادمج البيانات وأعد التقرير:

```bash
coverage combine
coverage report -m
```

> نصيحة: `concurrency = multiprocessing, thread, gevent, eventlet, greenlet` تسمح لـ coverage بالارتباط بنماذج الـ async المختلفة.

# تغطية الفروع والتوجيهات البرمجية pragmas

* فعّل `branch = True` في `[run]`. هذا يلتقط أفرع `else` المفقودة، والدوائر القصيرة short-circuits، مسارات الاستثناءات، إلخ.
* تجاهل الأسطر غير القابلة للاختبار باستخدام تعليق في نهاية السطر:

  * `# pragma: no cover` — استبعد هذا السطر من التغطية.
  * بالنسبة للفروع المعقدة، قم بإعادة الهيكلة بدلاً من الإفراط في استخدام التوجيهات البرمجية pragmas.

# السياقات (قسّم التغطية حسب الاختبار أو المهمة)

تعلق السياقات تسميات على الأسطر المنفذة حتى تتمكن من الإجابة على: "أي الاختبارات تغطي هذا الكود؟"

* أسهل مع pytest:

  * في `.coveragerc` أضف `dynamic_context = test_function`.
  * ثم استخدم `coverage html --show-contexts` أو افحص البيانات لكل سياق لترى أي اختبار مسّ سطرًا ما.
* يمكنك أيضًا ضبط `dynamic_context = test` (test nodeid) أو `dynacontext` عبر متغير البيئة في مشغلات الاختبار المخصصة.

# التكامل مع Pytest

نموذجان شائعان:

**أ. واجهة سطر الأوامر الأصلية لـ coverage (بسيطة وسريعة)**

```bash
coverage run -m pytest -q
coverage report -m
```

**ب. إضافة pytest-cov (تضيف تحسينات لسطر الأوامر)**

```bash
pip install pytest-cov
pytest --cov=your_package --cov-branch --cov-report=term-missing --cov-report=html
```

كلا النموذجين يستخدمان coverage.py في النهاية؛ استخدم أيهما يناسب أعراف فريقك.

# ربط نموذجي في CI (مخطط GitHub Actions)

```yaml
- name: Install
  run: pip install -U pip coverage pytest

- name: Test with coverage
  run: |
    coverage run -m pytest -q
    coverage report -m
    coverage xml
- name: Enforce threshold
  run: coverage report --fail-under=90
- name: Upload HTML
  if: always()
  uses: actions/upload-artifact@v4
  with:
    name: htmlcov
    path: htmlcov/
```

# المزالق الشائعة والإصلاحات

* **تقارير ضخمة/بطيئة**: قيّد `source=` واستخدم `omit=` لتخطي venv، الاختبارات، الكود المُنشأ.
* **مسارات مختلفة على CI مقابل المحلي**: أضف قسم `[paths]` حتى يقوم `coverage combine` بدمج مجموعات البيانات.
* **العمليات الفرعية غير مُقاسة**: عيّن `COVERAGE_PROCESS_START` وحافظ على `parallel = True`، ثم `coverage combine`.
* **أطر العمل غير المتزامنة**: أضف الإدخال ذو الصلة إلى `concurrency = ...`.
* **امتدادات C**: coverage.py تقيس بايثون، وليس الكود الأصلي — اكتب اختبارات غلاف حول الحدود البايثونية.
* **سلبيات كاذبة على الكود غير القابل للوصول**: علّمه بـ `# pragma: no cover`، ولكن فكر في إعادة الهيكلة لجعل السلوك قابلًا للاختبار.

# أوامر مفيدة ستستخدمها فعليًا

```bash
coverage erase                       # امسح البيانات السابقة
coverage run -m pytest               # اجمع البيانات
coverage report -m                   # ملخص نصي مع الأسطر المفقودة
coverage html                        # افتح htmlcov/index.html
coverage xml                         # لمحللي CI
coverage json                        # للنصوص البرمجية/الأتمتة
coverage combine                     # ادمج بيانات العمليات الفرعية/المتوازية
coverage annotate                    # لكل سطر .py، يوضح أي الأسطر تم تشغيلها
```

# متى تتوقف عن الضبط

استهدف **حدًا ذا معنى** (مثل، 80–95%)، فرضه باستخدام `fail_under`، وركز المراجعات على **تغطية الاختلافات** (هل الأسطر الجديدة/المعدلة مختبرة؟). لا تسعى لتحقيق 100% على الكود الصعب اختباره (مفاتيح الميزات feature flags، الحمايات الدفاعية) — استخدم التوجيهات البرمجية pragmas باعتدال وفضل التصميم الأبسط القابل للاختبار.