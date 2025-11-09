---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: بناء خادم طقس أساسي لـ MCP
translated: true
type: note
---

### ما هو بروتوكول سياق النموذج (MCP)؟

بروتوكول سياق النموذج (MCP) هو معيار مفتوح يحدد كيفية تبادل التطبيقات وأنظمة الذكاء الاصطناعي (مثل النماذج اللغوية الكبيرة) للسياق، مثل الأدوات والموارد والإرشادات. فهو يمكّن التكامل السلس بين النماذج اللغوية الكبيرة (مثل Claude) والخدمات الخارجية، مما يسهل بناء وكلاء ذكاء اصطناعي قابلة للتوسيع. يركز هذا الدليل على إعداد خادم MCP أساسي باستخدام Python عادي (بدون `uv`)، استنادًا إلى البرنامج التعليمي الرسمي للبدء السريع لخادم طقس بسيط يتصل بـ National Weather Service API. يعرض هذا الخادم أداتين: `get_alerts` (لتنبيهات الطقس حسب الولاية) و `get_forecast` (لتنبؤات الطقس حسب الموقع).

### المتطلبات الأساسية
- معرفة أساسية بـ Python والنماذج اللغوية الكبيرة (مثل Claude).
- تثبيت Python 3.10 أو إصدار أحدث.
- الوصول إلى طرفية (يوصى بـ macOS/Linux؛ تعليمات Windows مشابهة ولكن استخدم PowerShell).
- للاختبار: تطبيق Claude for Desktop (متاح لـ macOS/Windows؛ وليس Linux — استخدم عميلًا مخصصًا إذا لزم الأمر).
- ملاحظة: تتواصل خوادم MCP عبر JSON-RPC عبر stdio (stdin/stdout). تجنب الطباعة إلى stdout في الكود الخاص بك لمنع تلف الرسائل؛ استخدم التسجيل إلى stderr بدلاً من ذلك.

### الخطوة 1: إعداد البيئة الخاصة بك
1. أنشئ دليل مشروع جديد:
   ```
   mkdir weather
   cd weather
   ```

2. أنشئ بيئة افتراضية وقم بتنشيطها:
   ```
   python -m venv .venv
   source .venv/bin/activate  # في Windows: .venv\Scripts\activate
   ```

3. قم بترقية pip (موصى به لتحسين الموثوقية):
   ```
   python -m pip install --upgrade pip
   ```

4. قم بتثبيت التبعيات (MCP SDK و HTTP client):
   ```
   pip install "mcp[cli]" httpx
   ```

5. أنشئ ملف الخادم:
   ```
   touch weather.py  # أو استخدم محرر النصوص لإنشائه
   ```

### الخطوة 2: بناء خادم MCP
افتح `weather.py` في محرر النصوص وأضف الكود التالي. يستخدم هذا الكود الفئة `FastMCP` من MCP SDK، والتي تولد تلقائيًا مخططات الأدوات من تلميحات الأنواع و docstrings.

```python
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# تهيئة خادم MCP
mcp = FastMCP("weather")

# ثوابت لـ National Weather Service API
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """تقديم طلب إلى NWS API مع معالجة الأخطاء المناسبة."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

def format_alert(feature: dict) -> str:
    """تنسيق ميزة التنبيه إلى سلسلة نصية قابلة للقراءة."""
    props = feature["properties"]
    return f"""
الحدث: {props.get('event', 'Unknown')}
المنطقة: {props.get('areaDesc', 'Unknown')}
الشدة: {props.get('severity', 'Unknown')}
الوصف: {props.get('description', 'No description available')}
التعليمات: {props.get('instruction', 'No specific instructions provided')}
"""

@mcp.tool()
async def get_alerts(state: str) -> str:
    """الحصول على تنبيهات الطقس لولاية أمريكية.

    الوسائط:
        state: رمز ولاية أمريكية مكون من حرفين (مثال: CA, NY)
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "تعذر جلب التنبيهات أو لم يتم العثور على أي تنبيهات."

    if not data["features"]:
        return "لا توجد تنبيهات نشطة لهذه الولاية."

    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)

@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """الحصول على توقعات الطقس لموقع معين.

    الوسائط:
        latitude: خط عرض الموقع
        longitude: خط طول الموقع
    """
    # أولاً، الحصول على نقطة نهاية شبكة التنبؤ
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    if not points_data:
        return "تعذر جلب بيانات التنبؤ لهذا الموقع."

    # الحصول على رابط التنبؤ من استجابة النقاط
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        return "تعذر جلب التنبؤ التفصيلي."

    # تنسيق الفترات إلى تنبؤ قابل للقراءة
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # إظهار الفترات الخمس القادمة فقط
        forecast = f"""
{period['name']}:
درجة الحرارة: {period['temperature']}°{period['temperatureUnit']}
الرياح: {period['windSpeed']} {period['windDirection']}
التنبؤ: {period['detailedForecast']}
"""
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)

def main():
    # تشغيل الخادم عبر stdio
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
```

- **ملاحظات رئيسية**:
  - يتم تعريف الأدوات باستخدام ديكورات `@mcp.tool()`. سيستدعيها مضيف النموذج اللغوي الكبير (مثل Claude) استنادًا إلى استعلامات المستخدم.
  - يستخدم هذا المثال دوال غير متزامنة لاستدعاءات API.
  - تضمن معالجة الأخطاء الفشل بشكل أنيق (على سبيل المثال، عدم وجود بيانات يعيد رسالة ودية للمستخدم).
  - للإنتاج، أضف التسجيل (على سبيل المثال، عبر وحدة `logging` إلى stderr) وتحديد معدل الاستخدام.

### الخطوة 3: اختبار الخادم محليًا
شغّل الخادم:
```
python weather.py
```
يجب أن يبدأ في الاستماع على stdio دون إخراج (هذا طبيعي). للاختبار يدويًا، ستحتاج إلى عميل MCP، ولكن انتقل إلى التكامل للاختبار الكامل.

### الخطوة 4: الاتصال بمضيف (مثل Claude for Desktop)
1. حمّل وقم بتثبيت Claude for Desktop من [claude.ai/download](https://claude.ai/download).

2. قم بتكوين التطبيق عن طريق إنشاء/تحرير `~/Library/Application Support/Claude/claude_desktop_config.json` (في macOS) أو المكافئ في Windows (`%APPDATA%\Claude\claude_desktop_config.json`):
   ```json
   {
     "mcpServers": {
       "weather": {
         "command": "python",
         "args": [
           "/المسار/المطلق/إلى/weather/weather.py"  // استبدل هذا بمسار مشروعك (استخدم pwd للعثور عليه)
         ],
         "cwd": "/المسار/المطلق/إلى/weather"  // اختياري: حدد دليل العمل إذا لزم الأمر
       }
     }
   }
   ```
   - استخدم المسارات المطلقة (على سبيل المثال، `/Users/اسمك/weather/weather.py` على macOS).
   - في Windows، استخدم الشرطة المائلة `/` أو شرطتين مائلتين للخلف `\\`.
   - تأكد من تفعيل البيئة الافتراضية عند الاختبار محليًا، ولكن بالنسبة لـ Claude، فهو يشغل ملف Python القابل للتنفيذ من نظامك (تأكد من إمكانية الوصول إلى site-packages للبيئة الافتراضية أو قم بالتثبيت عالميًا إذا فضلت — على الرغم من أن البيئة الافتراضية موصى بها).
   - ابحث عن مسار Python باستخدام `which python` (macOS/Linux) أو `where python` (Windows).

3. أعد تشغيل Claude for Desktop بالكامل (أغلقه تمامًا، على سبيل المثال، Cmd+Q على macOS).

4. اختبر في Claude:
   - افتح Claude وانقر على أيقونة "البحث والأدوات" (أيقونة المنزلق).
   - يجب أن ترى `get_alerts` و `get_forecast` مدرجين.
   - أمثلة على الاستعلامات:
     - "ما هي تنبيهات الطقس النشطة في كاليفورنيا؟"
     - "ما هي توقعات الطقس لخط عرض 37.77، وخط طول -122.41؟" (إحداثيات سان فرانسيسكو).
   - سيقوم Claude باستدعاء الأدوات تلقائيًا ودمج النتائج في رده.
   - ملاحظة: تدعم واجهة برمجة التطبيقات هذه المواقع الأمريكية فقط.

### استكشاف الأخطاء وإصلاحها
- **الخادم لا يظهر في Claude**: تحقق من صيغة JSON، والمسارات المطلقة، وإعادة التشغيل الكامل للتطبيق. تحقق من السجلات في `~/Library/Logs/Claude/mcp*.log`.
- **أخطاء في الأدوات**: تأكد من تشغيل الخادم بدون أخطاء محليًا. أضف تأخيرات لحدود معدل استدعاءات API إذا لزم الأمر.
- **استعلامات غير أمريكية**: واجهة برمجة التطبيقات NWS مخصصة للولايات المتحدة فقط؛ قم بالتوسع باستخدام واجهات برمجة تطبيقات أخرى لدعم عالمي.
- للميزات المتقدمة (الموارد، الإرشادات، الإشعارات)، راجع وثائق MCP الكاملة.

هذا يجهز خادم MCP وظيفيًا باستخدام Python عادي. للبدائل باستخدام TypeScript/Node.js أو المزيد من الأمثلة، تحقق من الموارد أدناه.

### المراجع
- [Build an MCP Server (Official Docs)](https://modelcontextprotocol.io/docs/develop/build-server)
- [MCP Quickstart Guide](https://modelcontextprotocol.info/docs/quickstart/quickstart/)
- [Model Context Protocol Guide with Demo](https://www.datacamp.com/tutorial/mcp-model-context-protocol)
- [How the Model Context Protocol Works](https://www.freecodecamp.org/news/how-the-model-context-protocol-works/)
- [Practical Introduction to MCP](https://medium.com/@davidlfliang/guide-a-practical-introduction-to-model-context-protocol-mcp-2f63b636f510)