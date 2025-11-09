---
audio: false
date: 2025-09-10
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: قائمة التحقق من تعليق اختبارات الوحدة
translated: true
type: note
---

يتعطل `unittest` عادةً بسبب حالات الجمود (الخيوط/غير المتزامن)، أو توقف الإدخال/الإخراج، أو مشاكل العمليات الفرعية/المتعددة، أو انتظار اختبار لاستدعاء شبكة. إليك قائمة تدقيق دقيقة *لرؤية مكان التوقف* و*إصلاحه* — تعمل على Python 3.9–3.11.

### 1) تشغيل unittest بوضع التفصيل (وبشكل صحيح)

```bash
# إذا كان xx.py يستدعي unittest.main()
python xx.py -v

# أو استخدم الاكتشاف (مُوصى به)
python -m unittest -v
python -m unittest discover -v -s tests -p "test_*.py"
```

> ملاحظة: `python -v` هو **وضع تفصيل استيراد المترجم**، وليس وضع تفصيل الاختبار. استخدم `-m unittest -v` لأسماء الاختبار والتقدم.

### 2) تشغيل faulthandler + وضع المطور (تفريغ المكدس عند التوقف، تحذيرات أكثر صرامة)

```bash
# تشغيل لمرة واحدة
python -X faulthandler -X dev -u -m unittest -v
# أو عبر المتغيرات البيئية
export PYTHONFAULTHANDLER=1
python -X dev -u -m unittest -v
```

* `-X faulthandler` يسمح لـ Python بطبعة تتبع مكدس الخيوط عند إشارات الخطأ القاتلة/انتهاء المهلة.
* `-X dev` يجعل التحذيرات/الأخطاء أعلى صوتًا.
* `-u` يزيل التخزين المؤقت لـ stdout/stderr حتى *ترى* المخرجات في الوقت الفعلي.

### 3) إجبار طباعة تتبع المكدس عندما يبدو متوقفًا

الخيار أ — من طرفية أخرى (Linux/macOS):

```bash
kill -SIGUSR1 <pid>  # مع تفعيل faulthandler، يقوم بتفريغ مكدسات جميع الخيوط
```

الخيار ب — أضف هذا إلى بداية تشغيل الاختبار (أعلى `xx.py`):

```python
import faulthandler, signal, sys
faulthandler.enable()
# تفريغ المكدسات عند إشارة SIGUSR1:
faulthandler.register(signal.SIGUSR1, all_threads=True)
# أيضًا تفريغ تلقائي إذا توقف لأكثر من 120 ثانية:
faulthandler.dump_traceback_later(120, repeat=True)
```

### 4) تتبع التنفيذ خطوة بخطوة (مكثف لكن حاسم)

```bash
python -m trace --trace xx.py
# أو
python -m trace --trace -m unittest discover -v
```

سترى كل سطر يتم تنفيذه؛ توقف عندما "يتجمد" الناتج — هذه هي نقطة التوقف.

### 5) استخدام المصحح على الفور

```bash
python -m pdb xx.py         # إذا كان xx.py يستدعي unittest.main()
# أوقف التنفيذ عند سطر مشبوه:
# (Pdb) b mymodule.py:123
# (Pdb) c
```

لجلسات الاكتشاف، أضف `import pdb; pdb.set_trace()` في المكان المشبوه.

### 6) الأسباب الشائعة والإصلاحات السريعة

* **العمليات المتعددة على macOS/Windows**: دائمًا احمِ نقطة الدخول للاختبار.

  ```python
  if __name__ == "__main__":
      import unittest
      unittest.main()
  ```

  إذا قمت بإنشاء عمليات في الاختبارات على macOS:

  ```python
  import multiprocessing as mp
  if __name__ == "__main__":
      mp.set_start_method("fork")  # يتجنب أحيانًا التوقف مقابل الوضع الافتراضي "spawn"
  ```

  (افعل هذا فقط إذا كنت تعلم أن الكود الخاص بك آمن مع fork.)

* **جمود الخيوط**: تحقق من `join()` بدون مهلة، أو أقفال لم يتم تحريرها، أو خيوط خلفية تنتظر الخيط الرئيسي. استبدل:

  ```python
  t.join()
  ```

  بـ:

  ```python
  t.join(timeout=5); assert not t.is_alive()
  ```

* **الاختبارات غير المتزامنة**: تأكد من استخدام `IsolatedAsyncioTestCase` (3.8+) أو `asyncio.run()`. غالبًا ما يتسبب وجود حلقات أحداث مزدوجة أو نسيان `await` في التوقف.

* **استدعاءات الشبكة**: أضف **مهلات قصيرة** في كل مكان:

  ```python
  requests.get(url, timeout=5)
  ```

* **انتظار الإدخال**: أزل `input()` أو احمِها في الاختبارات؛ قد يحظر CI/stdin إلى الأبد.

* **المحاكاة الخاطئة**: طريقة محاكاة لا تحل أبدًا `Future`/وعد أو خادم مبتدئ لم يبدأ.

### 7) رؤية إضافية

* اعرض التخصيصات إذا اشتبه في تسرب/دوران:

  ```bash
  python -X tracemalloc=25 -m unittest -v
  ```
* اعرض ضوضاء الاستيراد (نادرًا ما يحتاج للتوقف):

  ```bash
  python -v -m unittest -v
  ```

### 8) إذا توقف فقط على إصدار Python واحد

* جرب كليهما:

  ```bash
  pyenv local 3.11.9
  python -X faulthandler -X dev -m unittest -v

  pyenv local 3.9.19
  python -X faulthandler -X dev -m unittest -v
  ```

  عادةً ما تظهر الاختلافات حول سلوك `multiprocessing`، أو `asyncio`، أو الامتدادات C.

---

إذا قمت بلصق تتبع المكدس من `faulthandler` (أو الأسطر الأخيرة من `trace --trace`)، سأشير إلى السبب المحدد وأقترح إصلاحًا مستهدفًا.