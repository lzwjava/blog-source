---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: अनुवाद एपीआई प्रमाणीकरण त्रुटि ठीक करें
translated: true
type: note
---

### वर्कफ़्लो और त्रुटि के कारण का विश्लेषण

आपका "Translate Recent Notes" के लिए GitHub Actions वर्कफ़्लो समग्र रूप से अच्छी तरह से संरचित लगता है—यह रेपो को चेक आउट कर रहा है, Python सेटअप कर रहा है, निर्भरताएँ इंस्टॉल कर रहा है, N सबसे हाल के पोस्ट पर एक अनुवाद स्क्रिप्ट चला रहा है, और `_notes/` में परिवर्तन कमिट कर रहा है। हालाँकि, आपके द्वारा पहले साझा किए गए लॉग (ar, de, fr, आदि जैसी भाषाओं में अनुवाद के दौरान 401 त्रुटियों के साथ) के आधार पर, समस्या `scripts/translation/update_lang_notes.py` के अंदर अनुवाद API कॉल के लिए प्रमाणीकरण में है।

#### मूल कारण
- त्रुटि `"No cookie auth credentials found"` (HTTP 401) विशिष्ट रूप से **OpenRouter API** (या इसके साथ इंटरैक्ट करने वाले Python क्लाइंट/लाइब्रेरी, जैसे LiteLLM या एक अनौपचारिक SDK) के लिए है। यह तब होता है जब API अनुरोध में उचित प्रमाणीकरण हेडर का अभाव होता है।
- OpenRouter अनुरोधों में `Authorization: Bearer <your_openrouter_api_key>` की अपेक्षा करता है। यदि कुंजी सही ढंग से पास नहीं की जाती है, तो कुछ क्लाइंट कुकी-आधारित सत्र प्रमाणीकरण की आवश्यकता के रूप में वापस गिर जाते हैं (या गलत व्याख्या करते हैं), जिससे यह सटीक त्रुटि ट्रिगर होती है।
- आपके वर्कफ़्लो में:
  - आप `OPENROUTER_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}` सेट कर रहे हैं, जो स्क्रिप्ट के वातावरण में एक गुप्त मान पास करता है।
  - लेकिन स्क्रिप्ट संभवतः इस env var को सही ढंग से पढ़/उपयोग नहीं कर रही है। सामान्य बेमेल:
    - स्क्रिप्ट `OPENAI_API_KEY` की अपेक्षा करती है (OpenRouter जैसे OpenAI-संगत एंडपॉइंट के लिए)।
    - या यह बेस URL को `https://openrouter.ai/api/v1` पर सेट किए बिना किसी लाइब्रेरी (जैसे, `openai` Python SDK) का उपयोग कर रही है।
    - सीक्रेट `DEEPSEEK_API_KEY` वास्तव में आपकी **OpenRouter API कुंजी** (DeepSeek/Grok मॉडल पर रूटेड) रख सकता है, लेकिन अगर यह एक सीधी DeepSeek कुंजी है, तो यह OpenRouter के लिए काम नहीं करेगी।
- लॉग से, स्क्रिप्ट मॉडल `'x-ai/grok-4-fast'` (OpenRouter के माध्यम से Grok 4) का उपयोग कर रही है, और यह फ्रंट मैटर/शीर्षक को सफलतापूर्वक प्रोसेस कर रही है लेकिन प्रति भाषा सामग्री अनुवाद पर विफल हो रही है।
- यह GitHub Actions समस्या नहीं है—यह Python स्क्रिप्ट के API क्लाइंट सेटअप में है। वर्कफ़्लो कमिट चरण पर जारी रहता है (इसलिए `git config user.name "github-actions[bot]"` लॉग), लेकिन अनुवाद के बिना, केवल अंग्रेजी फाइलें जोड़ी जाती हैं।

#### अनुशंसित सुधार
1. **वर्कफ़्लो में Environment Variables अपडेट करें**:
   - सामान्य OpenRouter सेटअप (OpenAI-संगत) के साथ संरेखित करें। "Translate posts" स्टेप में `env` ब्लॉक को इस प्रकार बदलें:
     ```
     env:
       GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
       OPENAI_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}  # वेरिएबल का नाम बदलें जिसकी स्क्रिप्ट अपेक्षा करती है
       OPENAI_BASE_URL: https://openrouter.ai/api/v1   # OpenRouter पर रूटिंग के लिए आवश्यक
     ```
   - यदि `DEEPSEEK_API_KEY` आपकी OpenRouter कुंजी है, तो बढ़िया। यदि यह सीधी DeepSeek कुंजी है, तो रेपो सेटिंग्स में एक नया सीक्रेट `OPENROUTER_API_KEY` बनाएं जिसमें आपकी वास्तविक OpenRouter कुंजी हो ([openrouter.ai/keys](https://openrouter.ai/keys) पर प्राप्त करें)।
   - परीक्षण: लॉग में डीबगिंग के लिए रन स्टेप में `echo $OPENAI_API_KEY` (redacted) जोड़ें।

2. **Python स्क्रिप्ट (`update_lang_notes.py`) को ठीक करें**:
   - सुनिश्चित करें कि यह OpenAI क्लाइंट को इस प्रकार इनिशियलाइज़ करती है (मानते हुए कि `openai` लाइब्रेरी है):
     ```python
     import os
     from openai import OpenAI

     client = OpenAI(
         api_key=os.getenv("OPENAI_API_KEY"),
         base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")  # सेट न होने पर डिफ़ॉल्ट रूप से OpenAI पर जाता है
     )

     # फिर उपयोग करें client.chat.completions.create(..., model="x-ai/grok-4-fast")
     ```
   - यदि LiteLLM (मल्टी-प्रोवाइडर के लिए सामान्य) का उपयोग कर रहे हैं: यदि `requirements.txt` में नहीं है तो इसे इंस्टॉल करें, और कॉल करें `completion(model="openrouter/x-ai/grok-4-fast", api_key=os.getenv("OPENAI_API_KEY"), api_base="https://openrouter.ai/api/v1", ...)`।
   - अनुवाद लूप के लिए: प्रति भाषा त्रुटि हैंडलिंग जोड़ें (जैसे, API कॉल के आसपास `try/except`, विफलताओं को लॉग करें, 401 होने पर स्किप करें)।
   - कुकीज़ को स्पष्ट रूप से हैंडल करें? संभावना नहीं है कि आवश्यकता है—API कुंजी से चिपके रहें। यदि स्क्रिप्ट में ब्राउज़र/Selenium कोड है, तो CI विश्वसनीयता के लिए इसे हटा दें।

3. **वर्कफ़्लो सुधार**:
   - **इनपुट वैलिडेशन**: कुछ भी प्रोसेस न करने से बचने के लिए N=0 या अमान्य `--n` के लिए एक चेक जोड़ें।
   - **सशर्त कमिट**: आपका `git diff --cached --quiet || git commit` अच्छा है, लेकिन संदेश को सभी भाषाओं को दर्शाने के लिए अपडेट करें: `-m "Add translated posts (ar, de, es, fr, hi, ja, zh, hant)"`।
   - **कैशिंग**: इंस्टॉल को तेज करने के लिए `actions/cache` for `pip` जोड़ें।
   - **डीबग मोड**: वर्बोज़ लॉगिंग के लिए स्क्रिप्ट में एक वैकल्पिक इनपुट `debug: true` और `--debug` फ्लैग जोड़ें।
   - **अनुमतियाँ**: सुनिश्चित करें कि `github-pages` वातावरण में आवश्यकता पड़ने पर पढ़ने/लिखने की पहुंच है।
   - "Translate posts" स्टेप के लिए अपडेट किया गया पूर्ण YAML स्निपेट:
     ```
     - name: Translate posts
       run: |
         python scripts/translation/update_lang_notes.py --n ${{ inputs.n }}
       env:
         GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
         OPENAI_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}
         OPENAI_BASE_URL: https://openrouter.ai/api/v1
     ```

4. **परीक्षण चरण**:
   - **लोकल टेस्ट**: env var एक्सपोर्ट करके (जैसे, `export OPENAI_API_KEY=your_key`) लोकल पर `python scripts/translation/update_lang_notes.py --n 1` चलाएँ।
   - **वर्कफ़्लो टेस्ट**: `workflow_dispatch` और N=1 के साथ ट्रिगर करें, API कॉल के लिए लॉग जांचें।
   - **सीक्रेट सत्यापित करें**: रेपो सेटिंग्स > Secrets में, पुष्टि करें कि `DEEPSEEK_API_KEY` के पास एक वैध OpenRouter कुंजी है (`sk-or-...` से शुरू होती है)।
   - यदि अभी भी विफल हो रहा है, तो स्क्रिप्ट में `--verbose` जोड़ें और अनुरोध हेडर का निरीक्षण करें (जैसे, `print(client.api_key)` के माध्यम से)।

इससे 401 त्रुटियाँ हल होनी चाहिए और अनुवाद प्रवाहित होने चाहिए। यदि आप `update_lang_notes.py` से स्निपेट साझा करते हैं (जैसे, API क्लाइंट init), तो मैं और अधिक सटीक रूप से पता लगा सकता हूँ।

#### संदर्भ
- [OpenRouter Quickstart (API Auth Setup)](https://openrouter.ai/docs/quickstart)
- [LiteLLM OpenRouter Integration](https://docs.litellm.ai/docs/providers/openrouter) (यदि उपयोग कर रहे हैं)
- [GitHub Issue on Similar OpenRouter Auth Error](https://github.com/mendableai/firecrawl/issues/1352)
- [Reddit Thread on OpenRouter 401 Errors](https://www.reddit.com/r/openrouter/comments/1oqiaol/error_401_no_cookie_auth_credentials_found/)