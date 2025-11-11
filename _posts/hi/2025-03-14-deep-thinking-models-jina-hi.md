---
audio: false
generated: true
lang: hi
layout: post
title: गहन चिंतन मॉडल
translated: true
type: note
---

यह जानकारी https://search.jina.ai से प्राप्त क्वेरी पर आधारित है।

---

गहन रीजनिंग मॉडल और उनकी API उपलब्धता का विवरण यहां दिया गया है, जो गहन समझ प्रदान करने और आपकी आवश्यकताओं के लिए सही मॉडल चुनने में मदद करने के लिए डिज़ाइन किया गया है:

*   **OpenAI o-series मॉडल (o1, o3-mini, आदि)**: ये मॉडल, Azure OpenAI Service के माध्यम से उपलब्ध [^1], जटिल रीजनिंग के लिए डिज़ाइन किए गए हैं, जो विज्ञान, कोडिंग और गणित में उत्कृष्ट प्रदर्शन करते हैं। उदाहरण के लिए, `o1` मॉडल में 200,000-टोकन की संदर्भ विंडो (context window) है और प्रसंस्करण समय को समायोजित करने के लिए `reasoning_effort` पैरामीटर के साथ फाइन-ट्यून किया जा सकता है [^2]।

    *   **API एक्सेस:** Azure OpenAI Service API के माध्यम से `2024-12-01-preview` API संस्करण के साथ एक्सेस किया जा सकता है [^1]।
    *   **मूल्य निर्धारण (Pricing):** Azure OpenAI की कीमत मॉडल और उपयोग के आधार पर अलग-अलग होती है। विस्तृत जानकारी के लिए Azure OpenAI Service मूल्य निर्धारण पृष्ठ देखें।
    *   **दर सीमाएँ (Rate Limits):** दर सीमाएँ Azure OpenAI टियर और क्षेत्र पर निर्भर करती हैं। विवरण के लिए Azure OpenAI दस्तावेज़ देखें।
    *   **समर्थित सुविधाएँ:** फ़ंक्शन कॉलिंग, JSON मोड, समायोज्य सुरक्षा सेटिंग्स [^3]।
    *   **कोड उदाहरण (Python):**
        ```python
        from openai import AzureOpenAI
        client = AzureOpenAI(
          azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
          api_key=os.getenv("AZURE_OPENAI_API_KEY"),
          api_version="2024-12-01-preview"
        )
        response = client.chat.completions.create(
            model="o1-new", # अपने o1 डिप्लॉयमेंट के मॉडल डिप्लॉयमेंट नाम से बदलें।
            messages=[
                {"role": "user", "content": "What steps should I think about when writing my first Python API?"},
            ],
            max_completion_tokens = 5000
        )
        print(response.model_dump_json(indent=2))
        ```
*   **DeepSeek R1**: OpenAI के o1 के साथ रीजनिंग बेंचमार्क में प्रतिस्पर्धा करने के लिए जाना जाता है, DeepSeek अपने R1 मॉडल को API के माध्यम से प्रदान करता है [^4]। API मॉडल द्वारा उत्पन्न चेन ऑफ़ थॉट (CoT) कंटेंट तक पहुंच प्रदान करता है, जो उपयोगकर्ताओं को मॉडल की रीजनिंग प्रक्रिया को देखने की अनुमति देता है [^5]। DeepSeek OpenAI के लिए एक लागत-प्रभावी विकल्प भी प्रदान करता है, जिसका पूरा R1 API लागत के एक अंश पर पेश किया जाता है [^6]। DeepSeek-V3 API भी उपलब्ध है, जिसका प्रदर्शन अग्रणी बंद-स्रोत मॉडल के बराबर है [^7]।

    *   **API एक्सेस:** DeepSeek API, OpenAI API फॉर्मेट के साथ संगत [^8]।
    *   **मूल्य निर्धारण (Pricing):** इनपुट टोकन प्रति 1M टोकन \$0.14, आउटपुट टोकन प्रति 1M टोकन \$0.55 [^9]।
    *   **दर सीमाएँ (Rate Limits):** विशिष्ट दर सीमाओं के लिए DeepSeek API दस्तावेज़ देखें।
    *   **समर्थित सुविधाएँ:** चैट कम्प्लीशन, चैट प्रीफिक्स कम्प्लीशन (बीटा) [^10]।
    *   **कोड उदाहरण (Python):**
        ```python
        from openai import OpenAI
        client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")
        messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=messages
        )
        print(response.choices[0].message.content)
        ```

*   **Grok (xAI)**: xAI के Grok मॉडल, जिनमें Grok-3 और Grok-3 mini शामिल हैं, मजबूत रीजनिंग क्षमताओं के साथ डिज़ाइन किए गए हैं। जबकि Grok-1.5 शुरुआती परीक्षकों के लिए उपलब्ध था, Grok 3 जल्द ही API के माध्यम से आ रहा है [^11]। Grok 3 (Think) और Grok 3 mini (Think) मॉडल को इसकी चेन-ऑफ-थॉट प्रक्रिया को परिष्कृत करने के लिए रीइन्फोर्समेंट लर्निंग का उपयोग करके प्रशिक्षित किया गया था, जो डेटा-कुशल तरीके से उन्नत रीजनिंग को सक्षम करता है [^12]।

    *   **API एक्सेस:** Grok 3 API के जल्द ही जारी होने की उम्मीद है [^11]।
    *   **मूल्य निर्धारण (Pricing):** मूल्य निर्धारण विवरण अभी तक सार्वजनिक रूप से उपलब्ध नहीं है। अपडेट के लिए xAI की वेबसाइट देखें।
    *   **दर सीमाएँ (Rate Limits):** दर सीमाएँ अभी तक सार्वजनिक रूप से उपलब्ध नहीं हैं। अपडेट के लिए xAI की वेबसाइट देखें।
    *   **समर्थित सुविधाएँ:** टूल यूज, कोड एक्सिक्यूशन, और उन्नत एजेंट क्षमताएं Enterprise API के लिए नियोजित हैं [^12]।
*   **Gemini 1.5 Pro**: एक Google मॉडल के रूप में, Gemini 1.5 Pro बड़ी मात्रा में जानकारी में रीजनिंग में उत्कृष्ट है और रीजनिंग कार्यों की एक विस्तृत श्रृंखला के लिए अनुकूलित है [^13]। यह एक मल्टीमॉडल मॉडल है और मजबूत रीजनिंग क्षमताएं प्रदान करता है, जिसमें प्रतिक्रियाओं में सोचने की प्रक्रिया भी शामिल है [^14]। Gemini API डेवलपर्स को 2 मिलियन संदर्भ विंडो (context window) तक पहुंच प्रदान करती है [^15]।

    *   **API एक्सेस:** Gemini API के माध्यम से उपलब्ध [^15]।
    *   **मूल्य निर्धारण (Pricing):** विस्तृत जानकारी के लिए Google AI Studio मूल्य निर्धारण पृष्ठ देखें।
    *   **दर सीमाएँ (Rate Limits):** टेक्स्ट एम्बेडिंग के लिए प्रति मिनट 1,500 अनुरोध [^16]। अन्य दर सीमाओं के लिए Google AI Studio दस्तावेज़ देखें।
    *   **समर्थित सुविधाएँ:** फ़ंक्शन कॉलिंग, कोड एक्सिक्यूशन, समायोज्य सुरक्षा सेटिंग्स, JSON मोड [^17]।

**तुलनात्मक अंतर्दृष्टि:**

| फीचर           | OpenAI o-series | DeepSeek R1      | Grok (xAI)       | Gemini 1.5 Pro   |
| :-------------- | :-------------- | :--------------- | :--------------- | :--------------- |
| प्रदर्शन        | STEM में मजबूत  | o1-mini के बराबर/बेहतर | मजबूत रीजनिंग    | समग्र रूप से मजबूत |
| API एक्सेस      | Azure OpenAI    | DeepSeek API     | जल्द ही आ रहा    | Gemini API       |
| लागत (Cost)     | अलग-अलग         | लागत-प्रभावी     | अभी उपलब्ध नहीं  | Google AI Studio देखें |
| संदर्भ विंडो (Context Window) | 200K टोकन | 64K टोकन         | 1M टोकन          | 2M टोकन          |
| इच्छित उपयोग के मामले | जटिल कार्य     | गणित, कोड        | व्यापक रीजनिंग   | डेटा विश्लेषण    |

**सीमाएँ:**

*   **OpenAI o-series:** डिफ़ॉल्ट रूप से मार्कडाउन फ़ॉर्मेटिंग उत्पन्न नहीं कर सकता है [^1]।
*   **DeepSeek R1:** गैर-अंग्रेजी/चीनी क्वेरी के लिए प्रदर्शन खराब हो सकता है [^18]।
*   **Grok (xAI):** API अभी तक जारी नहीं हुआ है; विशिष्ट क्षमताओं पर सीमित जानकारी।
*   **Gemini 1.5 Pro:** प्रायोगिक मॉडल उत्पादन उपयोग के लिए नहीं हैं [^19]।

[^1]: Azure OpenAI o सीरीज़ मॉडल बढ़ी हुई फोकस और क्षमता के साथ रीजनिंग और समस्या समाधान कार्यों को हल करने के लिए डिज़ाइन किए गए हैं [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/reasoning)

[^2]: रीजनिंग मॉडल में कम्प्लीशन टोकन के हिस्से के रूप में रीजनिंग टोकन होते हैं, विवरण मॉडल प्रतिक्रिया में है [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/reasoning)

[^3]: JSON मोड समर्थित [ai.google.dev](https://ai.google.dev/models/gemini)

[^4]: हमारा API उपयोगकर्ताओं को deepseek रीजनर द्वारा उत्पन्न CoT कंटेंट तक पहुंच प्रदान करता है, जिससे वे इसे देख, प्रदर्शित और निखार सकते हैं [searchenginejournal.com](https://www.searchenginejournal.com/googles-ai-search-is-improving-but-still-lags-behind-human-quality-results/508459/)

[^5]: बहुत कम लागत पर और उच्च प्रदर्शन क्षमता के साथ, DeepSeek OpenAI की तुलना में अपनी पूरी R1 API लागत के एक अंश पर पेश करता है [seo-kueche.de](https://www.seo-kueche.de/blog/google-stellt-gemini-vor-das-kann-der-neue-ki-chatbot/)

[^6]: पूरी श्रृंखला के मॉडल उच्च-परिशुद्धि फाइन-ट्यूनिंग से गुजरे हैं, निर्देश अनुपालन मजबूत हुआ है, जटिल भाषा समझ, गहन तर्क, पाठ उत्पादन में उत्कृष्ट परिणाम प्रदर्शित करते हैं [cloud.baidu.com](https://cloud.baidu.com/doc/wenxinworkshop/s/jlil5u56k)

[^7]: xAI Grok 3 API आने वाले हफ्तों में लॉन्च होगी [t.me](https://t.me/s/GPT4Telegram)

[^8]: आज हम दो बीटा रीजनिंग मॉडल की घोषणा कर रहे हैं: Grok 3 Think और Grok 3 mini Think [x.ai](https://x.ai/blog/grok-3)

[^9]: Gemini 1.5 Pro एक मध्यम आकार का मल्टीमॉडल मॉडल है जो रीजनिंग कार्यों की एक विस्तृत श्रृंखला के लिए अनुकूलित है [ai.google.dev](https://ai.google.dev/models/gemini)

[^10]: मजबूत रीजनिंग क्षमताएं प्रदान करता है और प्रतिक्रियाओं में सोचने की प्रक्रिया को शामिल करता है [youtube.com](https://www.youtube.com/watch?v=YQAydVlHV7c)

[^11]: इनपुट टोकन सीमा 2,097,152 [ai.google.dev](https://ai.google.dev/models/gemini)

[^12]: रीजनिंग बंद होने पर, Grok 3 तत्काल, उच्च-गुणवत्ता वाली प्रतिक्रियाएं देता है [x.ai](https://x.ai/blog/grok-3)

[^13]: Gemini 1.5 Pro एक मध्यम आकार का मल्टीमॉडल मॉडल है जो रीजनिंग कार्यों की एक विस्तृत श्रृंखला के लिए अनुकूलित है, 1.5 Pro एक साथ बड़ी मात्रा में डेटा प्रोसेस कर सकता है [ai.google.dev](https://ai.google.dev/models/gemini)

[^14]: डिफ़ॉल्ट रूप से, o3 mini और o1 मॉडल आउटपुट उत्पन्न करने का प्रयास नहीं करेंगे जिसमें मार्कडाउन फ़ॉर्मेटिंग शामिल हो [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/reasoning)

[^15]: DeepSeek R1 अंग्रेजी और चीनी के लिए अनुकूलित है, लेकिन अन्य भाषाओं में क्वेरी के लिए इसका प्रदर्शन खराब हो सकता है [datacamp.com](https://datacamp.com/blog/deepseek-r1)

[^16]: API प्रायोगिक मॉडल प्रदान करता है जो पूर्वावलोकन (Preview) में उपलब्ध हैं, जैसा कि नियमों में परिभाषित किया गया है, अर्थात मॉडल उत्पादन उपयोग के लिए नहीं हैं [ai.google.dev](https://ai.google.dev/models/gemini)

[^17]: API एक्सेस कस्टम AI डेवलपमेंट डेवलपर्स के लिए xAI Grok 3 तक API एक्सेस जारी करने की योजना बना रहा है, जिससे डेवलपर्स इसके एकीकरण को सक्षम कर सकेंगे [medium.com](https://medium.com/@gerardnico/a-timeline-to-grok-3-the-race-to-catch-up-54e0c0d1886c)

[^18]: हम DeepSeek R1 पेश करते हैं, जिसमें RL से पहले कोल्ड स्टार्ट डेटा शामिल है। DeepSeek R1 गणित, कोड और अन्य क्षेत्रों में OpenAI o1 के बराबर प्रदर्शन हासिल करता है [api-docs.deepseek.com](https://api-docs.deepseek.com/guides/reasoning_model)

[^19]: Gemini 1.5 Pro एक मध्यम आकार का मल्टीमॉडल मॉडल है जो रीजनिंग कार्यों की एक विस्तृत श्रृंखला के लिए अनुकूलित है [ai.google.dev](https://ai.google.dev/models/gemini)