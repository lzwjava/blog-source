---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ar
layout: post
model: mistralai/mistral-medium-3.1
title: فهم استخدام التركيبات في Pytest
translated: true
type: note
---

## ما هو `@pytest.fixture`؟

`@pytest.fixture` هو ديكوراتور يُعلّم دالة كـ **fixture** - وهي دالة خاصة توفر بيانات الاختبار، أو إعدادات الإعداد، أو وظيفة التفكيك لاختباراتك. تُعد الـ fixtures واحدة من أقوى ميزات pytest وهي سبب رئيسي لتفضيل العديد من المطورين لـ pytest بدلاً من الوحدة المضمنة في Python `unittest`.

## كيف تعمل الـ Fixtures

تتبع الـ fixtures نمطًا بسيطًا لكنه قوي:

1.  **الإعداد**: الكود قبل جملة `yield` يعمل قبل الاختبار
2.  **تنفيذ الاختبار**: يعمل الاختبار عندما يصل إلى جملة `yield`
3.  **التفكيك**: الكود بعد جملة `yield` يعمل بعد اكتمال الاختبار

### مثال أساسي للـ Fixture

```python
import pytest

@pytest.fixture
def sample_data():
    # كود الإعداد
    data = {"name": "John", "age": 30}
    yield data  # الاختبار يعمل هنا
    # كود التفكيك (يعمل بعد الاختبار)
    print("Cleaning up sample data")
```

## لماذا نحتاج إلى الـ Fixtures

تحل الـ fixtures عدة مشاكل شائعة في الاختبار:

1.  **عزل الاختبار**: التأكد من أن كل اختبار يعمل ببيانات جديدة ومتوقعة
2.  **إعادة استخدام الكود**: تجنب تكرار كود الإعداد/التفكيك عبر اختبارات متعددة
3.  **إدارة الموارد**: التعامل بشكل صحيح مع الموارد مثل اتصالات قاعدة البيانات، أو الملفات، أو اتصالات الشبكة
4.  **وضوح الاختبار**: الحفاظ على تركيز دوال الاختبار على ما يتم اختباره، وليس على الإعداد
5.  **حقن التبعية**: توفير ما يحتاجه كل اختبار بالضبط

## الميزات الرئيسية للـ Fixtures

### 1. حقن التبعية

يمكن للـ fixtures أن تعتمد على fixtures أخرى، مما ينشئ رسم بياني للتبعيات:

```python
@pytest.fixture
def database_connection():
    # إعداد اتصال قاعدة البيانات
    conn = create_connection()
    yield conn
    conn.close()

@pytest.fixture
def user_table(database_connection):
    # يستخدم fixture اتصال قاعدة البيانات
    create_table(database_connection, "users")
    yield
    drop_table(database_connection, "users")
```

### 2. التحكم في النطاق

يمكن أن يكون لـ fixtures أعمار مختلفة:

```python
@pytest.fixture(scope="function")  # الافتراضي - يعمل مرة واحدة لكل اختبار
def per_test_fixture():
    pass

@pytest.fixture(scope="module")  # يعمل مرة واحدة لكل وحدة
def per_module_fixture():
    pass

@pytest.fixture(scope="session")  # يعمل مرة واحدة لكل جلسة اختبار
def per_session_fixture():
    pass
```

### 3. الـ Fixtures التلقائية

يمكن أن تعمل الـ fixtures تلقائيًا دون الحاجة إلى طلبها:

```python
@pytest.fixture(autouse=True)
def always_run_this():
    # هذا يعمل قبل كل اختبار في الوحدة
    yield
    # هذا يعمل بعد كل اختبار
```

### 4. الـ Fixtures ذات المعاملات

يمكن لـ fixtures إنشاء مجموعات متعددة من البيانات:

```python
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param  # سيشغل الاختبارات باستخدام 1 و 2 و 3
```

## مثال عملي مع اختبار API

إليك كيف تساعد الـ fixtures في سيناريو اختبار الرأس المالي الخاص بك:

```python
import pytest
import requests

@pytest.fixture
def financial_header():
    # الإعداد - إنشاء الرأس
    headers = create_financial_header()  # منطق الإنشاء الخاص بك
    yield headers  # الاختبار يعمل هنا باستخدام هذه الرؤوس

    # التفكيك - حذف الرأس
    delete_financial_header(headers)  # منطق التنظيف الخاص بك

def test_submit_transaction(financial_header):
    # توفر الـ fixture الرؤوس تلقائيًا
    response = requests.post(
        "https://api.example.com/transactions",
        headers=financial_header,
        json={"amount": 100}
    )
    assert response.status_code == 201

def test_validate_header(financial_header):
    # نفس الـ fixture مستخدمة في اختبار آخر
    response = requests.get(
        "https://api.example.com/validate",
        headers=financial_header
    )
    assert response.json()["valid"] is True
```

## المقارنة مع unittest

| الميزة                  | pytest Fixtures                     | unittest setUp/tearDown          |
|-------------------------|-------------------------------------|----------------------------------|
| حقن التبعية             | ✅ نعم                              | ❌ لا                             |
| التحكم في النطاق        | ✅ دالة، صنف، وحدة، جلسة           | ❌ فقط على مستوى الأسلوب/الصنف   |
| بناء جملة نظيف         | ✅ ديكوراتور بسيط                  | ❌ يتطلب توريثًا                 |
| عزل الاختبار            | ✅ كل اختبار يحصل على fixtures جديدة | ❌ الحالة المشتركة قد تسبب مشاكل |
| استخدام المعاملات       | ✅ مدعوم مدمجًا                    | ❌ يحتاج إلى تنفيذ يدوي          |

## متى تستخدم الـ Fixtures

استخدم الـ fixtures عندما تحتاج إلى:
- إعداد بيانات أو كائنات للاختبار
- إدارة الموارد الخارجية (اتصالات قاعدة البيانات، الملفات، إلخ)
- تنفيذ عمليات تنظيف بعد الاختبارات
- مشاركة تبعيات الاختبار المشتركة
- إنشاء بيئات اختبار مختلفة
- تنفيذ منطق إعداد/تفكيك معقد

تُعد الـ fixtures ذات قيمة خاصة في اختبار API (مثل حالة الرأس المالي الخاصة بك) لأنها تساعد في إدارة دورة حياة موارد الاختبار بطريقة نظيفة ومتوقعة.