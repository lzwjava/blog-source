---
audio: false
generated: true
image: false
lang: ar
layout: post
title: 'اختبار الوحدة مقابل باي تست: الفروق الأساسية'
translated: true
type: note
---

إليك مقارنة واضحة ومركزة بدون جداول حول ما يتغير فعليًا في اختباراتك اليومية.

# الفلسفة والأسلوب

*   **unittest**: أسلوب xUnit (يشبه Java/JUnit). اختبارات قائمة على الفئات، خطافات دورة الحياة مثل `setUp/tearDown`، يجب أن تبدأ أسماء الدوال بـ `test_`.
*   **pytest**: بسيط و"بايثوني". دوال الاختبار **أو** الفئات، أدوات مساعدة (fixtures) غنية، استخدام `assert` العادي مع إعادة كتابة التأكيدات (assertion rewriting).

# اكتشاف الاختبارات

*   **unittest**: `python -m unittest discover` (أو تحميل مجموعات الاختبار). يبحث عن `test*.py`، والفئات الفرعية لـ `TestCase`.
*   **pytest**: `pytest` يكتشف تلقائيًا ملفات `test_*.py` و `*_test.py`؛ والدوال `test_*` والطرق في فئات `Test*`.

# التأكيدات

*   **unittest**: العديد من الطرق المحددة (`assertEqual`, `assertTrue`, `assertRaises`, …).
*   **pytest**: استخدم `assert` العادي وسيقوم بطباعة فروقات توضيحية ("اليسار مقابل اليمين")، ويدعم `pytest.raises`.

# الأدوات المساعدة والإعداد

*   **unittest**: `setUp()/tearDown()`, `setUpClass/tearDownClass`, `setUpModule/tearDownModule`.
*   **pytest**: **أدوات مساعدة (Fixtures)** بنطاقات (function/class/module/session)، حقن التبعيات، الاستخدام التلقائي، أدوات التهيئة. يشجع على إعدادات صغيرة قابلة لإعادة الاستخدام.

# التمييز (Parametrization)

*   **unittest**: لا يوجد إصدار مدمج؛ استخدم الحلقات أو subTests أو مكتبات خارجية.
*   **pytest**: `@pytest.mark.parametrize` هو أسلوب أصلي (مصفوفة من المدخلات، تقارير نظيفة).

# التخطي، الإخفاقات المتوقعة، العلامات

*   **unittest**: `@skip`, `@skipIf`, `@expectedFailure`.
*   **pytest**: نفس الأفكار بالإضافة إلى **علامات** قوية (`@pytest.mark.slow`, `xfail`, `filterwarnings`, علامات مخصصة) والاختيار من سطر الأوامر (`-m slow`).

# الإضافات والنظام البيئي

*   **unittest**: شامل الأساسيات لكنه خفيف؛ يعتمد على أدوات وتشغيل خارجي للميزات المتقدمة.
*   **pytest**: نظام بيئي ضخم من الإضافات (`pytest-xdist` للتشغيل المتوازي، `pytest-randomly`, `pytest-cov`, `pytest-mock`, `pytest-asyncio`, `pytest-django`، إلخ).

# المحاكاة

*   **unittest**: `unittest.mock` هو المعيار؛ يعمل في كل مكان.
*   **pytest**: استخدم `unittest.mock` أو أداة `mocker` المساعدة في `pytest-mock` (ترقيع أنظف وإزالة تلقائية).

# اختبار Async

*   **unittest**: منذ الإصدار 3.8، يحتوي على `IsolatedAsyncioTestCase` (جيد لكنه مطول).
*   **pytest**: مع `pytest-asyncio` (أو إضافة trio) تحصل على `@pytest.mark.asyncio` ودعم الأدوات المساعدة لحلقات الأحداث.

# الأداء والتوازي

*   **unittest**: لا يوجد تشغيل متوازي مدمج؛ استخدم `unittest-parallel`/حيل CI.
*   **pytest**: `pytest-xdist -n auto` هو الحل الأمثل.

# IDE/CI/التغطية

*   كلاهما يتكامل مع IDEs و CI. التغطية عبر `coverage.py`:
  * **unittest**: `coverage run -m unittest` → `coverage report`.
  * **pytest**: `pytest --cov=your_pkg` مع `pytest-cov`.

# متى تختار أيهما

*   **اختر unittest** إذا:
  *   كنت تحتاج فقط المكتبة القياسية (بدون تبعيات خارجية).
  *   تقوم بالتكامل مع قاعدة كود قديمة/أسلوب xUnit أو سياسات مؤسسية صارمة.
*   **اختر pytest** إذا:
  *   أردت كتابة أسرع للاختبارات، وفشل أوضح، وأدوات مساعدة/تمييز قوية.
  *   ستستفيد من نظامه البيئي للإضافات والتشغيل المتوازي.

# التشغيل المتبادل والهجرة

يمكنك تشغيل مجموعات **unittest** باستخدام **pytest** (pytest يجد `unittest.TestCase`s). هذا يتيح لك الهجرة تدريجيًا:

1.  ابدأ باستدعاء `pytest` كأداة تشغيل.
2.  أضف اختبارات pytest بجانب الاختبارات الحالية.
3.  قدّم الأدوات المساعدة/التمييز حيثما تساعد.
4.  يمكنك لاحقًا إعادة هيكلة فئات `TestCase` القديمة إلى دوال.

# أمثلة صغيرة جنبًا إلى جنب

## نفس الاختبار

**unittest**

```python
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3]

    def test_sum(self):
        self.assertEqual(sum(self.data), 6)

    def test_raises(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

if __name__ == "__main__":
    unittest.main()
```

**pytest**

```python
import pytest

@pytest.fixture
def data():
    return [1, 2, 3]

def test_sum(data):
    assert sum(data) == 6

def test_raises():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

## التمييز

**unittest (subTest)**

```python
import unittest

class TestParity(unittest.TestCase):
    def test_even(self):
        for n in [0, 2, 4]:
            with self.subTest(n=n):
                self.assertEqual(n % 2, 0)
```

**pytest**

```python
import pytest

@pytest.mark.parametrize("n", [0, 2, 4])
def test_even(n):
    assert n % 2 == 0
```

## المحاكاة

**unittest.mock**

```python
from unittest.mock import patch

@patch("pkg.api.fetch_user", return_value={"id": 1})
def test_uses_api(mock_fetch):
    from pkg.service import get_user
    assert get_user(1)["id"] == 1
    mock_fetch.assert_called_once_with(1)
```

**pytest-mock**

```python
def test_uses_api(mocker):
    mock_fetch = mocker.patch("pkg.api.fetch_user", return_value={"id": 1})
    from pkg.service import get_user
    assert get_user(1)["id"] == 1
    mock_fetch.assert_called_once_with(1)
```

# توصيات عملية

*   المشاريع الجديدة: افترض استخدام **pytest** للسرعة، القابلية للقراءة، والنظام البيئي.
*   البيئات القديمة أو التي تستخدم المكتبة القياسية فقط: التزم بـ **unittest**، لكن فكر في تشغيله عبر **pytest** لفتح مخرجات أفضل وإضافات دون إعادة كتابة الاختبارات.
*   أضف `pytest-xdist` مبكرًا لـ CI أسرع، و `pytest-cov` للتغطية.
*   استخدم الأدوات المساعدة بدلاً من إعدادات الفئات الكبيرة؛ حافظ على كونها صغيرة وقابلة للتركيب.
*   استخدم العلامات لتنظيم مجموعات الاختبار (`slow`, `integration`, `db`) وتشغيل مجموعات فرعية في مراحل CI.

إذا أردت، أخبرني بهيكل مشروعك وقواعده (المكتبة القياسية فقط؟ تحتاج توازي؟ async؟ Django/Flask/FastAPI?) وسأرسم لك إعداد اختبار بسيط وآرائي.