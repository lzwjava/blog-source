---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: एक बुनियादी एमसीपी वेदर सर्वर का निर्माण
translated: true
type: note
---

### मॉडल कॉन्टेक्स्ट प्रोटोकॉल (MCP) क्या है?

मॉडल कॉन्टेक्स्ट प्रोटोकॉल (MCP) एक ओपन स्टैंडर्ड है जो परिभाषित करता है कि एप्लिकेशन और AI सिस्टम (जैसे लार्ज लैंग्वेज मॉडल) कैसे टूल्स, रिसोर्सेज और प्रॉम्प्ट्स जैसे कॉन्टेक्स्ट का आदान-प्रदान करते हैं। यह LLMs (जैसे क्लॉड) और बाहरी सेवाओं के बीच सीमलेस इंटीग्रेशन को सक्षम बनाता है, जिससे एक्स्टेंसिबल AI एजेंट बनाना आसान हो जाता है। यह गाइड नेशनल वेदर सर्विस API से कनेक्ट होने वाले एक साधारण वेदर सर्वर के लिए ऑफिशियल क्विकस्टार्ट ट्यूटोरियल के आधार पर, सादे Python (बिना `uv` के) का उपयोग करके बेसिक MCP सर्वर सेट अप करने पर केंद्रित है। यह सर्वर दो टूल्स एक्सपोज़ करता है: `get_alerts` (राज्य वेदर अलर्ट्स के लिए) और `get_forecast` (लोकेशन फोरकास्ट के लिए)।

### आवश्यक शर्तें
- Python और LLMs (जैसे क्लॉड) से बेसिक परिचय।
- Python 3.10 या उच्चतर इंस्टॉल होना।
- टर्मिनल एक्सेस (macOS/Linux रिकमेंडेड; Windows के लिए निर्देश समान हैं लेकिन PowerShell का उपयोग करें)।
- टेस्टिंग के लिए: क्लॉड फॉर डेस्कटॉप ऐप (macOS/Windows के लिए उपलब्ध; Linux के लिए नहीं—अगर जरूरत हो तो कस्टम क्लाइंट का उपयोग करें)।
- नोट: MCP सर्वर stdio (stdin/stdout) के माध्यम से JSON-RPC पर कम्युनिकेट करते हैं। मैसेज करप्शन से बचने के लिए अपने कोड में stdout पर प्रिंट करने से बचें; इसके बजाय stderr पर लॉगिंग का उपयोग करें।

### चरण 1: अपना एनवायरनमेंट सेट अप करें
1. एक नया प्रोजेक्ट डायरेक्टरी बनाएं:
   ```
   mkdir weather
   cd weather
   ```

2. एक वर्चुअल एनवायरनमेंट बनाएं और एक्टिवेट करें:
   ```
   python -m venv .venv
   source .venv/bin/activate  # Windows पर: .venv\Scripts\activate
   ```

3. pip को अपग्रेड करें (रिलायबिलिटी के लिए रिकमेंडेड):
   ```
   python -m pip install --upgrade pip
   ```

4. डिपेंडेंसीज इंस्टॉल करें (MCP SDK और HTTP क्लाइंट):
   ```
   pip install "mcp[cli]" httpx
   ```

5. सर्वर फाइल बनाएं:
   ```
   touch weather.py  # या इसे बनाने के लिए अपने एडिटर का उपयोग करें
   ```

### चरण 2: MCP सर्वर बनाएं
`weather.py` को अपने एडिटर में खोलें और निम्नलिखित कोड जोड़ें। यह MCP SDK से `FastMCP` क्लास का उपयोग करता है, जो टाइप हिंट्स और डॉकस्ट्रिंग्स से ऑटो-जेनरेटेड टूल स्कीमा प्रदान करती है।

```python
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# MCP सर्वर को इनिशियलाइज़ करें
mcp = FastMCP("weather")

# नेशनल वेदर सर्विस API के लिए कॉन्स्टेंट्स
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """प्रॉपर एरर हैंडलिंग के साथ NWS API को रिक्वेस्ट भेजें।"""
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
    """एक अलर्ट फीचर को रीडेबल स्ट्रिंग में फॉर्मेट करें।"""
    props = feature["properties"]
    return f"""
Event: {props.get('event', 'Unknown')}
Area: {props.get('areaDesc', 'Unknown')}
Severity: {props.get('severity', 'Unknown')}
Description: {props.get('description', 'No description available')}
Instructions: {props.get('instruction', 'No specific instructions provided')}
"""

@mcp.tool()
async def get_alerts(state: str) -> str:
    """यूएस राज्य के लिए वेदर अलर्ट्स प्राप्त करें।

    Args:
        state: दो-अक्षर का यूएस राज्य कोड (जैसे CA, NY)
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "अलर्ट्स फ़ेच करने में असमर्थ या कोई अलर्ट नहीं मिला।"

    if not data["features"]:
        return "इस राज्य के लिए कोई एक्टिव अलर्ट नहीं हैं।"

    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)

@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """किसी लोकेशन के लिए वेदर फोरकास्ट प्राप्त करें।

    Args:
        latitude: लोकेशन का अक्षांश
        longitude: लोकेशन का देशांतर
    """
    # पहले फोरकास्ट ग्रिड एंडपॉइंट प्राप्त करें
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    if not points_data:
        return "इस लोकेशन के लिए फोरकास्ट डेटा फ़ेच करने में असमर्थ।"

    # पॉइंट्स रिस्पांस से फोरकास्ट URL प्राप्त करें
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        return "डिटेल्ड फोरकास्ट फ़ेच करने में असमर्थ।"

    # पीरियड्स को रीडेबल फोरकास्ट में फॉर्मेट करें
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # सिर्फ अगले 5 पीरियड दिखाएं
        forecast = f"""
{period['name']}:
Temperature: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Forecast: {period['detailedForecast']}
"""
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)

def main():
    # stdio पर सर्वर रन करें
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
```

- **मुख्य नोट्स**:
  - टूल्स `@mcp.tool()` डेकोरेटर्स के साथ डिफाइन किए गए हैं। LLM होस्ट (जैसे क्लॉड) उन्हें यूजर क्वेरी के आधार पर कॉल करेगा।
  - यह उदाहरण API कॉल के लिए async फंक्शन्स का उपयोग करता है।
  - एरर हैंडलिंग ग्रेसफुल फेल्योर सुनिश्चित करती है (जैसे, कोई डेटा न होने पर यूजर-फ्रेंडली मैसेज रिटर्न करता है)।
  - प्रोडक्शन के लिए, लॉगिंग (जैसे, `logging` मॉड्यूल से stderr पर) और रेट लिमिटिंग जोड़ें।

### चरण 3: सर्वर को लोकली टेस्ट करें
सर्वर रन करें:
```
python weather.py
```
यह बिना आउटपुट के stdio पर लिसनिंग शुरू कर देना चाहिए (यह नॉर्मल है)। मैन्युअली टेस्ट करने के लिए, आपको MCP क्लाइंट की आवश्यकता होगी, लेकिन फुल टेस्टिंग के लिए इंटीग्रेशन पर आगे बढ़ें।

### चरण 4: एक होस्ट से कनेक्ट करें (जैसे क्लॉड फॉर डेस्कटॉप)
1. [claude.ai/download](https://claude.ai/download) से क्लॉड फॉर डेस्कटॉप डाउनलोड और इंस्टॉल करें।

2. ऐप को कॉन्फ़िगर करें `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) या Windows पर इसके समकक्ष (`%APPDATA%\Claude\claude_desktop_config.json`) बनाकर/एडिट करके:
   ```json
   {
     "mcpServers": {
       "weather": {
         "command": "python",
         "args": [
           "/ABSOLUTE/PATH/TO/weather/weather.py"  # अपने प्रोजेक्ट पथ से रिप्लेस करें (इसे ढूंढने के लिए pwd का उपयोग करें)
         ],
         "cwd": "/ABSOLUTE/PATH/TO/weather"  # ऑप्शनल: अगर जरूरत हो तो वर्किंग डायरेक्टरी सेट करें
       }
     }
   }
   ```
   - एब्सोल्यूट पथ का उपयोग करें (जैसे, macOS पर `/Users/yourname/weather/weather.py`)।
   - Windows पर, फॉरवर्ड स्लैश `/` या डबल बैकस्लैश `\\` का उपयोग करें।
   - सुनिश्चित करें कि लोकली टेस्टिंग के दौरान आपका वर्चुअल एनवायरनमेंट एक्टिवेटेड है, लेकिन क्लॉड के लिए, यह आपके सिस्टम से Python एक्जीक्यूटेबल रन करता है (सुनिश्चित करें कि venv के site-packages एक्सेसिबल हैं या प्रिफर करें तो ग्लोबली इंस्टॉल करें—हालांकि venv रिकमेंडेड है)।
   - Python पथ `which python` (macOS/Linux) या `where python` (Windows) से ढूंढें।

3. क्लॉड फॉर डेस्कटॉप को पूरी तरह रीस्टार्ट करें (पूरी तरह बंद करें, जैसे macOS पर Cmd+Q)।

4. क्लॉड में टेस्ट करें:
   - क्लॉड खोलें और "Search and tools" आइकन (स्लाइडर आइकन) पर क्लिक करें।
   - आपको `get_alerts` और `get_forecast` लिस्टेड दिखना चाहिए।
   - क्वेरी उदाहरण:
     - "कैलिफोर्निया में एक्टिव वेदर अलर्ट्स क्या हैं?"
     - "अक्षांश 37.77, देशांतर -122.41 के लिए वेदर फोरकास्ट क्या है?" (सैन फ्रांसिस्को कोऑर्डिनेट्स)।
   - क्लॉड ऑटोमैटिकली टूल्स को इनवोक करेगा और अपने रिस्पांस में रिजल्ट्स को शामिल करेगा।
   - नोट: यह API सिर्फ US लोकेशन सपोर्ट करता है।

### समस्या निवारण
- **क्लॉड में सर्वर दिखाई नहीं दे रहा**: JSON सिंटैक्स, एब्सोल्यूट पथ और ऐप के फुल रीस्टार्ट को वेरिफाई करें। `~/Library/Logs/Claude/mcp*.log` पर लॉग्स चेक करें।
- **टूल एरर्स**: सुनिश्चित करें कि सर्वर लोकली एरर-फ्री रन हो रहा है। अगर जरूरत हो तो API रेट लिमिट के लिए डिलेज जोड़ें।
- **नॉन-US क्वेरीज**: NWS API सिर्फ US के लिए है; ग्लोबल सपोर्ट के लिए अन्य APIs के साथ एक्सटेंड करें।
- एडवांस्ड फीचर्स (रिसोर्सेज, प्रॉम्प्ट्स, नोटिफिकेशन्स) के लिए, फुल MCP डॉक्स देखें।

यह सादे Python का उपयोग करके एक फंक्शनल MCP सर्वर सेट अप करता है। TypeScript/Node.js विकल्पों या अधिक उदाहरणों के लिए, नीचे दिए गए रिसोर्सेज देखें।

### संदर्भ
- [Build an MCP Server (Official Docs)](https://modelcontextprotocol.io/docs/develop/build-server)
- [MCP Quickstart Guide](https://modelcontextprotocol.info/docs/quickstart/quickstart/)
- [Model Context Protocol Guide with Demo](https://www.datacamp.com/tutorial/mcp-model-context-protocol)
- [How the Model Context Protocol Works](https://www.freecodecamp.org/news/how-the-model-context-protocol-works/)
- [Practical Introduction to MCP](https://medium.com/@davidlfliang/guide-a-practical-introduction-to-model-context-protocol-mcp-2f63b636f510)