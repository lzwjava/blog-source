---
audio: false
generated: true
image: false
lang: hi
layout: post
title: प्रॉक्सी योजना समर्थित नहीं
translated: true
type: note
---

त्रुटि इंगित करती है कि आपके `gitmessageai.py` स्क्रिप्ट में `openai` क्लाइंट द्वारा उपयोग किया जाने वाला `httpx` लाइब्रेरी, `socks://127.0.0.1:7891/` URL के साथ एक प्रॉक्सी कॉन्फ़िगर करने का प्रयास कर रहा है, लेकिन `socks` स्कीम समर्थित या पहचानी नहीं गई है, जिसके परिणामस्वरूप `ValueError: Unknown scheme for proxy URL` हो रहा है। इससे पता चलता है कि आपके वातावरण या कोड से एक प्रॉक्सी कॉन्फ़िगरेशन ली जा रही है, और यह एक असमर्थित SOCKS प्रॉक्सी स्कीम का उपयोग कर रही है।

आइए जानें कि प्रॉक्सी कहाँ से आ सकती है और इसे कैसे ठीक किया जाए।

### प्रॉक्सी कहाँ से आ रही है?

प्रॉक्सी कॉन्फ़िगरेशन (`socks://127.0.0.1:7891/`) संभवतः निम्नलिखित स्थानों में से किसी एक से प्राप्त हो रही है:

1. **पर्यावरण चर (Environment Variables)**
   - `httpx` लाइब्रेरी स्वचालित रूप से पर्यावरण चर जैसे `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`, या उनके लोअरकेस समकक्ष (`http_proxy`, `https_proxy`, `all_proxy`) में प्रॉक्सी सेटिंग्स की जांच करती है।
   - `socks://127.0.0.1:7891/` जैसा मान एक SOCKS प्रॉक्सी (Shadowsocks या VPN जैसे टूल्स के लिए आम) का संकेत देता है जो इनमें से किसी एक चर में सेट था।
   - जांचने के लिए कि क्या ये चर सेट हैं, अपने टर्मिनल में निम्नलिखित चलाएँ:
     ```bash
     env | grep -i proxy
     ```
     `HTTP_PROXY=socks://127.0.0.1:7891` या `HTTPS_PROXY=socks://127.0.0.1:7891` जैसे चर देखें।

2. **सिस्टम-वाइड प्रॉक्सी सेटिंग्स**
   - यदि आप Linux सिस्टम का उपयोग कर रहे हैं, तो प्रॉक्सी सेटिंग्स वैश्विक रूप से कॉन्फ़िगर की गई हो सकती हैं (जैसे, `/etc/environment`, `/etc/profile`, या आपकी शेल कॉन्फ़िगरेशन जैसे `~/.bashrc`, `~/.zshrc`, या `~/.profile`)।
   - इन फाइलों में निम्नलिखित जैसी लाइनों के लिए जांच करें:
     ```bash
     export HTTP_PROXY="socks://127.0.0.1:7891"
     export HTTPS_PROXY="socks://127.0.0.1:7891"
     ```
   - आप इन फाइलों को निम्नलिखित के साथ देख सकते हैं:
     ```bash
     cat ~/.bashrc | grep -i proxy
     cat ~/.zshrc | grep -i proxy
     cat /etc/environment | grep -i proxy
     ```

3. **प्रॉक्सी टूल में प्रॉक्सी कॉन्फ़िगरेशन**
   - पता `127.0.0.1:7891` आमतौर पर प्रॉक्सी या VPN टूल्स जैसे Shadowsocks, V2Ray, या Clash द्वारा उपयोग किया जाता है, जो अक्सर 7890 या 7891 जैसे पोर्ट पर SOCKS5 प्रॉक्सी का उपयोग करते हैं।
   - यदि आपने ऐसा कोई टूल इंस्टॉल या कॉन्फ़िगर किया है, तो उसने स्वचालित रूप से पर्यावरण चर या सिस्टम प्रॉक्सी सेटिंग्स सेट की हो सकती हैं।

4. **कोड में स्पष्ट प्रॉक्सी (Explicit Proxy)**
   - हालांकि कम संभावना है, आपकी `gitmessageai.py` स्क्रिप्ट या उसके द्वारा उपयोग की जाने वाली कोई लाइब्रेरी स्पष्ट रूप से एक प्रॉक्सी कॉन्फ़िगर कर रही हो सकती है। चूंकि त्रुटि `httpx` में होती है, जांचें कि क्या आपकी स्क्रिप्ट `OpenAI` क्लाइंट या `httpx` क्लाइंट को एक प्रॉक्सी पास करती है।
   - अपनी स्क्रिप्ट में `proxy`, `proxies`, या `httpx.Client` जैसे शब्दों के लिए खोजें:
     ```bash
     grep -r -i proxy /home/lzwjava/bin/gitmessageai.py
     ```

5. **Python लाइब्रेरी कॉन्फ़िगरेशन**
   - कुछ Python लाइब्रेरीज़ (जैसे `requests` या `httpx`) प्रॉक्सी सेटिंग्स को कॉन्फ़िगरेशन फ़ाइल या पिछले सेटअप से प्राप्त कर सकती हैं। हालांकि, `httpx` मुख्य रूप से पर्यावरण चर या स्पष्ट कोड पर निर्भर करती है।

### `socks://` समस्या क्यों पैदा कर रहा है?

- `httpx` लाइब्रेरी (जिसका `openai` द्वारा उपयोग किया जाता है) मूल रूप से `socks` स्कीम (SOCKS4/SOCKS5 प्रॉक्सी) का समर्थन नहीं करती है जब तक कि अतिरिक्त निर्भरताएँ जैसे `httpx-socks` इंस्टॉल न हों।
- त्रुटि `Unknown scheme for proxy URL` इसलिए होती है क्योंकि `httpx` `http://` या `https://` जैसी स्कीम वाली प्रॉक्सी की अपेक्षा करती है, `socks://` की नहीं।

### समस्या को कैसे ठीक करें

आपके पास दो विकल्प हैं: यदि इसकी आवश्यकता नहीं है तो **प्रॉक्सी को हटा दें या बायपास करें**, या यदि आप इसका उपयोग करना चाहते हैं तो **SOCKS प्रॉक्सी का समर्थन करें**।

#### विकल्प 1: प्रॉक्सी को हटाएं या बायपास करें

यदि आपको DeepSeek API के लिए प्रॉक्सी की आवश्यकता नहीं है, तो आप प्रॉक्सी कॉन्फ़िगरेशन को अक्षम या बायपास कर सकते हैं।

1. **पर्यावरण चर अनसेट करें (Unset Environment Variables)**
   - यदि प्रॉक्सी पर्यावरण चर में सेट है, तो उन्हें अपने सत्र के लिए अनसेट करें:
     ```bash
     unset HTTP_PROXY
     unset HTTPS_PROXY
     unset ALL_PROXY
     unset http_proxy
     unset https_proxy
     unset all_proxy
     ```
   - इसे स्थायी बनाने के लिए, `~/.bashrc`, `~/.zshrc`, `/etc/environment`, या अन्य शेल कॉन्फ़िगरेशन फाइलों से संबंधित `export` लाइनों को हटा दें।

2. **प्रॉक्सी के बिना स्क्रिप्ट चलाएँ**
   - अस्थायी रूप से अपनी स्क्रिप्ट को प्रॉक्सी सेटिंग्स के बिना चलाएँ:
     ```bash
     HTTP_PROXY= HTTPS_PROXY= ALL_PROXY= python3 /home/lzwjava/bin/gitmessageai.py
     ```
   - यदि यह काम करता है, तो प्रॉक्सी ही समस्या थी।

3. **कोड में प्रॉक्सी बायपास करें**
   - अपनी `gitmessageai.py` स्क्रिप्ट को `OpenAI` क्लाइंट में प्रॉक्सी को स्पष्ट रूप से अक्षम करने के लिए संशोधित करें:
     ```python
     from openai import OpenAI
     import httpx

     def call_deepseek_api(prompt):
         api_key = os.getenv("DEEPSEEK_API_KEY")
         if not api_key:
             raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
         client = OpenAI(
             api_key=api_key,
             base_url="https://api.deepseek.com",
             http_client=httpx.Client(proxies=None)  # प्रॉक्सी अक्षम करें
         )
         # आपकी API कॉल लॉजिक यहाँ
         response = client.chat.completions.create(
             model="deepseek",  # सही मॉडल से बदलें
             messages=[{"role": "user", "content": prompt}]
         )
         return response.choices[0].message.content
     ```
   - `proxies=None` सेट करने से यह सुनिश्चित होता है कि `httpx` किसी भी पर्यावरण प्रॉक्सी सेटिंग्स को अनदेखा करती है।

#### विकल्प 2: SOCKS प्रॉक्सी का समर्थन करें

यदि आपको SOCKS प्रॉक्सी का उपयोग करने की आवश्यकता है (जैसे, VPN या प्रॉक्सी सर्वर के माध्यम से DeepSeek API तक पहुँचने के लिए), तो आपको `httpx` में SOCKS सपोर्ट जोड़ना होगा।

1. **`httpx-socks` इंस्टॉल करें**
   - SOCKS4/SOCKS5 प्रॉक्सी सपोर्ट सक्षम करने के लिए `httpx-socks` पैकेज इंस्टॉल करें:
     ```bash
     pip install httpx-socks
     ```
   - यह `httpx` को `socks://` और `socks5://` स्कीम को हैंडल करने में सक्षम बनाता है।

2. **अपना कोड अपडेट करें**
   - SOCKS प्रॉक्सी का स्पष्ट रूप से उपयोग करने के लिए अपनी स्क्रिप्ट को संशोधित करें:
     ```python
     from openai import OpenAI
     import httpx
     from httpx_socks import SyncProxyTransport

     def call_deepseek_api(prompt):
         api_key = os.getenv("DEEPSEEK_API_KEY")
         if not api_key:
             raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
         # SOCKS5 प्रॉक्सी कॉन्फ़िगर करें
         proxy_transport = SyncProxyTransport.from_url("socks5://127.0.0.1:7891")
         client = OpenAI(
             api_key=api_key,
             base_url="https://api.deepseek.com",
             http_client=httpx.Client(transport=proxy_transport)
         )
         # आपकी API कॉल लॉजिक यहाँ
         response = client.chat.completions.create(
             model="deepseek",  # सही मॉडल से बदलें
             messages=[{"role": "user", "content": prompt}]
         )
         return response.choices[0].message.content
     ```
   - यदि आपकी प्रॉक्सी SOCKS4 का उपयोग करती है तो `socks5://` को `socks4://` से बदलें।

3. **प्रॉक्सी सर्वर सत्यापित करें**
   - सुनिश्चित करें कि `127.0.0.1:7891` पर प्रॉक्सी सर्वर चल रहा है। यदि आप Clash या Shadowsocks जैसे टूल का उपयोग कर रहे हैं, तो इसकी स्थिति जांचें:
     ```bash
     netstat -tuln | grep 7891
     ```
   - यदि पोर्ट 7891 पर कोई प्रक्रिया सुन नहीं रही है, तो अपना प्रॉक्सी टूल शुरू करें या प्रॉक्सी URL में पोर्ट सही करें।

### अतिरिक्त डीबगिंग चरण

- **प्रॉक्सी टूल कॉन्फ़िगरेशन जांचें**
  - यदि आप Clash या Shadowsocks जैसे प्रॉक्सी टूल का उपयोग कर रहे हैं, तो इसकी कॉन्फ़िगरेशन फ़ाइल (जैसे `~/.config/clash/config.yaml`) सत्यापित करें कि यह SOCKS5 के लिए `127.0.0.1:7891` का उपयोग करने के लिए सेट है।
  - सुनिश्चित करें कि टूल चल रहा है और पहुँच योग्य है।

- **प्रॉक्सी कनेक्टिविटी टेस्ट करें**
  - `curl` जैसे टूल के साथ प्रॉक्सी का परीक्षण करें (इसके लिए `curl` का SOCKS सपोर्ट के साथ बिल्ट होना आवश्यक है):
    ```bash
    curl --socks5 127.0.0.1:7891 https://api.deepseek.com
    ```
  - यदि यह विफल हो जाता है, तो प्रॉक्सी सर्वर या तो डाउन है या गलत तरीके से कॉन्फ़िगर किया गया है।

- **प्रॉक्सी उपयोग लॉग करें**
  - पुष्टि करने के लिए कि किस प्रॉक्सी का उपयोग किया जा रहा है, अपनी स्क्रिप्ट में लॉगिंग जोड़ें:
    ```python
    import logging
    logging.basicConfig(level=logging.DEBUG)
    ```

### अनुशंसित फिक्स

यदि आपको प्रॉक्सी की आवश्यकता नहीं है, तो सबसे सरल फिक्स पर्यावरण चर को अनसेट करके और निम्नलिखित चलाकर इसे अक्षम करना है:
```bash
HTTP_PROXY= HTTPS_PROXY= ALL_PROXY= python3 /home/lzwjava/bin/gitmessageai.py
```

यदि आपको प्रॉक्सी की आवश्यकता है, तो `httpx-socks` इंस्टॉल करें और ऊपर दिखाए गए अनुसार `SyncProxyTransport` का उपयोग करने के लिए अपना कोड अपडेट करें।

### संदर्भ
- [httpx Documentation](https://www.python-httpx.org/advanced/#proxy-support)
- [httpx-socks GitHub](https://github.com/romis2012/httpx-socks)
- [DeepSeek API Documentation](https://platform.deepseek.com/docs)