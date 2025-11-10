---
audio: false
generated: true
image: false
lang: ar
layout: post
title: دروس تصميم مكتبات بايثون من أوبن أيه آي
translated: true
type: note
---

إليك تحليل سريع لمستودع `openai/openai-python` والدروس التي يمكنك استخلاصها لبناء مكتبة Python رائعة.

# ما يظهره المستودع (لمحة سريعة)

*   **هيكل "src" واضح**: `src/openai` للكود؛ والمستوى الأعلى `tests/`، `examples/`، `scripts/`، `.github/`، `pyproject.toml`، `mypy.ini`، `noxfile.py`، إلخ. هذا الفصل يحافظ على مسارات الاستيراد نظيفة واكتشاف الاختبارات يمكن التنبؤ به. ([GitHub][1])
*   **واجهة عامة مكتوبة**: الطلبات تستخدم `TypedDict`، والاستجابات هي نماذج **Pydantic**؛ تجربة مطور رائعة وإعادة هيكلة أكثر أمانًا. ([GitHub][1])
*   **تكافؤ بين المتزامن وغير المتزامن**: `OpenAI` و `AsyncOpenAI` يتشاركان نفس الـ API؛ النقل الافتراضي هو `httpx`، مع `aiohttp` اختياري. ([GitHub][1])
*   **البث المباشر من الدرجة الأولى**: أحداث مرسلة من الخادم مع تكرار بسيط في كل من الوضع المتزامن وغير المتزامن. ([GitHub][1])
*   **ترقيم تلقائي للصفحات**: نقاط نهاية قائمة قابلة للتكرار حتى لا يضطر المستخدمون لكتابة حلقات التصفح يدويًا. ([GitHub][1])
*   **عميل الوقت الفعلي/WebSocket**: عميل فرعي اختياري مع أمثلة وإرشادات معالجة الأخطاء. ([GitHub][1])
*   **خط أنابيب توليد الكود**: تم إنشاء الـ SDK من مواصفات OpenAPI (عبر Stainless)، مما يفرض الاتساق وتغطية الأنواع. ([GitHub][1])

# استنتاجات تصميم يمكنك إعادة استخدامها

*   **الحفاظ على "الطريقة الواضحة الوحيدة"**: اعرض `Client` واحدًا (بالإضافة إلى `AsyncClient`) بأسماء طرق متطابقة. لا ينبغي أن يتساءل المستخدمون "أي فئة يجب أن أستخدم؟". يوضح OpenAI SDK هذا مع `OpenAI` و `AsyncOpenAI`. ([GitHub][1])
*   **نقل محمول**: الافتراضي هو `httpx`، ولكن اسمح بتبديل خلفية HTTP (مثل `aiohttp`)، حتى لا يُحصر مستخدمو الإنجاز العالي. ([GitHub][1])
*   **طلبات ونماذج مكتوبة**: زود حمولات الطلبات المكتوبة ونماذج الاستجابة الغنية. هذا يمنحك الإكمال التلقائي في المحرر، وأمثلة قابلة للفحص، وتغييرات كاسرة أكثر أمانًا. ([GitHub][1])
*   **بث مباشر بدون احتكاك**: صمم البث المباشر كمكرر عادي / مكرر غير متزامن. لا حاجة لمضخات أحداث مخصصة. ([GitHub][1])
*   **ترقيم الصفحات القائم على المكرر**: اعرض `for item in client.resource.list(limit=...)` وقم جلب الصفحات بكسل. هذا يحافظ على كود المستخدم صغيرًا مع بقائه فعالاً. ([GitHub][1])
*   **النظم الفرعية هي عملاء فرعيون**: ضع الميزات المتخصصة (مثل realtime) خلف مساحة اسم واضحة (`client.beta.realtime`) للحفاظ على الواجهة الرئيسية نظيفة. ([GitHub][1])
*   **قم بالتوليد حيثما يساعد**: إذا كان الـ API الخاص بك مدفوعًا بالمواصفات، دع توليد الكود ينشئ الطبقات المملة ذات الأنواع القوية وصمم يدويًا الأجزاء المريحة. ([GitHub][1])

# هيكل أساسي يمكنك نسخه

```bash
yourlib/
  pyproject.toml
  noxfile.py
  mypy.ini
  README.md
  CHANGELOG.md
  SECURITY.md
  src/yourlib/
    __init__.py
    _version.py
    _types.py            # TypedDicts, enums
    _errors.py           # Exception hierarchy
    _http.py             # httpx client wrapper, retries, timeouts
    _pagination.py       # generic Pager[T]
    client.py            # Client + AsyncClient, auth, base URL
    resources/
      __init__.py
      widgets.py         # resource groups w/ sync+async methods
    streaming.py         # SSE helpers (sync/async)
  tests/
    test_client.py
    test_widgets.py
  examples/
    quickstart.py
    async_quickstart.py
```

## الواجهة العامة (`src/yourlib/__init__.py`)

*   أعد تصدير ما يحتاجه المستخدمون فقط:

```python
from .client import Client, AsyncClient
from ._errors import YourLibError, APIError, RateLimitError
__all__ = ["Client", "AsyncClient", "YourLibError", "APIError", "RateLimitError"]
```

## شكل العميل (متزامن وغير متزامن)

*   اعكس نفس أسماء الطرق؛ اختلف فقط في `await`/`async`:

```python
# src/yourlib/client.py
import httpx
from .resources.widgets import Widgets
from ._http import HttpTransport

class Client:
    def __init__(self, api_key=None, base_url="https://api.example.com", http_client=None):
        self._transport = HttpTransport(api_key, base_url, http_client or httpx.Client(timeout=30))
        self.widgets = Widgets(self._transport)

class AsyncClient:
    def __init__(self, api_key=None, base_url="https://api.example.com", http_client=None):
        self._transport = HttpTransport(api_key, base_url, http_client or httpx.AsyncClient(timeout=30))
        self.widgets = Widgets(self._transport)
```

## نمط ترقيم الصفحات

```python
# src/yourlib/_pagination.py
from typing import AsyncIterator, Iterator, Generic, TypeVar, Callable, Optional
T = TypeVar("T")
class Pager(Generic[T]):
    def __init__(self, fetch: Callable[..., dict], limit: int = 100):
        self._fetch = fetch
        self._limit = limit
        self._cursor = None
    def __iter__(self) -> Iterator[T]:
        while True:
            page = self._fetch(limit=self._limit, cursor=self._cursor)
            for item in page["data"]:
                yield item
            self._cursor = page.get("next_cursor")
            if not self._cursor:
                break
```

اعرضه حتى يتمكن المستخدمون من `for item in client.widgets.list(limit=50): ...`. (يتبع OpenAI SDK نفس النهج. ([GitHub][1]))

## نمط البث المباشر (SSE)

*   غلف البث المباشر لـ `httpx` بمكرر صغير ينتج الأحداث؛ اعكس متغيرًا غير متزامن. هذا ينتج تجربة المستخدم المريحة `for event in client.responses.create(..., stream=True)` كما تُرى في OpenAI SDK. ([GitHub][1])

# أدوات وسير عمل إصدار يتوسع

*   **`pyproject.toml` (PEP 621)** للبيانات الوصفية؛ اقفل تبعيات المطور بشكل منفصل.
*   **التحقق من الأنواع**: زود الأنواع، شغل `mypy` في CI (المستودع الخاص بهم يحتوي على `mypy.ini`). ([GitHub][1])
*   **منظم المهام**: جلسات `nox` للاختبار، والتدقيق، والتحقق من النوع، والبناء (يستخدمون `noxfile.py`). ([GitHub][1])
*   **CI**: إجراءات GitHub في `.github/` لتشغيل الاختبارات عبر إصدارات Python والمنصات. ([GitHub][2])
*   **سجل التغييرات** و **إدارة الإصدارات**: احتفظ بسجل مقروء للبشر؛ أتمتة الإصدارات (يستخدمون release-please). ([GitHub][1])
*   **مستندات الأمان والمساهمة**: حدد التوقعات للمبلغين والمساهمين. ([GitHub][1])

# المستندات والأمثلة

*   **أمثلة README** يجب أن تكون قابلة للتشغيل ويسهل نسخها ولصقها—متزامن، غير متزامن، بث مباشر، ترقيم صفحات، وأي "نقل خاص" (مثل `aiohttp`). يوضح README الخاص بـ OpenAI كل منها بإيجاز. ([GitHub][1])
*   **مرجع الـ API**: إذا تم إنشاؤه بواسطة الكود، انشر `api.md` / موقع مرجعي وحافظ على تزامنه مع الإصدارات. ([GitHub][1])
*   **مجلد الأمثلة**: ضم نصوصًا مركزة وحدية، بالإضافة إلى نموذج "كامل" واحد.

# الأخطاء، إعادة المحاولة، والانتهاء (ما يجب تنفيذه)

*   **تسلسل هرمي للأخطاء**: `YourLibError` → `APIError`، `AuthError`، `RateLimitError`، `TimeoutError`. اربط رموز حالة HTTP بالاستثناءات؛ شمل معرفات الطلبات.
*   **إعادة المحاولة**: يجب أن تعيد العمليات القابلة للإعادة المحاولة تلقائيًا مع التراجع الأسي + تباين على 429/5xx.
*   **المهلات**: حدد قيمًا افتراضية معقولة واجعلها قابلة للتكوين على مستوى العميل ومستوى كل استدعاء.
*   **خطاطات التسجيل**: تسجيل تصحيح منظم دون تسريب الأسرار.

# التعبئة والتغليف والتوافق

*   **ادعم 3-4 إصدارات Python نشطة ثانوية** (مثلًا، 3.9–3.13)، واختبرها في CI.
*   **لا توجد تأثيرات جانبية عند الاستيراد**؛ أجل إنشاء الشبكة/العميل حتى أول استخدام.
*   **تكوين البيئة**: اقبل متغير البيئة `API_KEY` ولكن اسمح للمستخدمين بتمرير بيانات الاعتماد بشكل صريح أيضًا (يظهر OpenAI `OPENAI_API_KEY` ونصيحة `.env`). ([GitHub][1])
*   **واجهة عامة مستقرة**: احتفظ بالأجزاء الداخلية خاصة (`_module.py`)، أعد تصدير واجهة مرتبة في `__init__.py`.

# المزالق التي يجب تجنبها

*   حشر كل شيء في وحدة واحدة؛ قم بالتقسيم حسب المورد وحافظ على استقرار الواردات العامة.
*   تسريب أنواع النقل؛ يجب أن تعتمد مواردك على "بروتوكول نقل" صغير، وليس `httpx` مباشرة.
*   جعل الوضع غير المتزامن يبدو من الدرجة الثانية؛ تأكد من أن الاختبارات والأمثلة تغطي كليهما بالتساوي (تكافؤ OpenAI هو نموذج جيد). ([GitHub][1])
*   بالنسبة للبث المباشر، لا تجبر المستخدمين على التلاعب بالخيوط أو استدعاءات الرجوع—المكررات أبسط. ([GitHub][1])

إذا أردت، يمكنني إنشاء هذا الهيكل لمجال محدد (مثل عميل مكتوب لخدمات REST الداخلية الخاصة بك، مع متزامن/غير متزامن، ترقيم صفحات، وبث مباشر) وإدراج نصوص `nox`، وCI، وأمثلة جاهزة للتشغيل.

[1]: https://github.com/openai/openai-python "GitHub - openai/openai-python: The official Python library for the OpenAI API"
[2]: https://github.com/openai/openai-python/tree/main/.github "openai-python/.github at main · openai/openai-python · GitHub"