---
audio: false
generated: true
lang: hi
layout: post
title: प्रोग्रामिंग कार्यों के लिए क्लॉड का उपयोग
translated: true
type: note
---

### प्रोग्रामिंग टास्क्स के लिए Claude का उपयोग कैसे करें (OpenRouter के माध्यम से)

चूंकि आप OpenRouter के माध्यम से Claude मॉडल्स का उपयोग कर रहे हैं (जैसा कि पहले चर्चा की गई थी), आप कोड जनरेट करने, डीबग करने, कॉन्सेप्ट्स समझाने, रीफैक्टर करने, या छोटे प्रोजेक्ट्स बनाने जैसे टास्क्स के लिए Claude की मजबूत कोडिंग क्षमताओं का लाभ उठा सकते हैं। प्रोग्रामिंग के लिए Claude 3.5 Sonnet या Opus विशेष रूप से अच्छे हैं क्योंकि इनमें बेहतर रीजनिंग और कोड समझ है। नीचे, मैं आपको प्रोग्रामिंग के लिए इसे प्रभावी ढंग से उपयोग करने का चरण-दर-चरण मार्गदर्शन दूंगा।

#### 1. **अपना एनवायरनमेंट सेट अप करें**
   - पहले वाले OpenRouter API सेटअप का उपयोग करें। सुनिश्चित करें कि आपके पास OpenAI Python SDK इंस्टॉल है (`pip install openai`)।
   - अधिकांश कोडिंग टास्क्स के लिए `anthropic/claude-3.5-sonnet` जैसे मॉडल को चुनें—यह कुशल है और Python, JavaScript, Java, C++, आदि जैसी भाषाओं को हैंडल करता है।
   - यदि आप कोड के लिए प्रॉम्प्टिंग में नए हैं, तो सरल अनुरोधों से शुरुआत करें और इटरेट करें।

#### 2. **प्रोग्रामिंग में Claude को प्रॉम्प्ट करने के लिए बेस्ट प्रैक्टिसेज**
   - **स्पष्ट रहें**: संदर्भ, भाषा, बाधाएं और उदाहरण प्रदान करें। Claude स्टेप-बाय-स्टेप रीजनिंग में माहिर है, इसलिए कोड जनरेट करने से पहले इसे "जोर से सोचने" के लिए कहें।
   - **सिस्टम प्रॉम्प्ट्स का उपयोग करें**: प्रतिक्रियाओं को केंद्रित करने के लिए "You are an expert Python developer" जैसी भूमिका सेट करें।
   - **एरर्स को हैंडल करें**: यदि कोड काम नहीं करता है, तो एरर मैसेज वापस फीड करें और फिक्स के लिए कहें।
   - **दोहराएं**: कोड को रिफाइन करने के लिए कन्वर्सेशन में फॉलो-अप मैसेजेज का उपयोग करें।
   - **सुरक्षा नोट**: संवेदनशील कोड या डेटा साझा न करें, क्योंकि API कॉल OpenRouter के माध्यम से जाती हैं।
   - **समर्थित भाषाएं**: Claude अधिकांश लोकप्रिय भाषाओं (Python, JS, HTML/CSS, SQL, आदि) को हैंडल करता है। कम चलन वाली भाषाओं के लिए, स्पष्ट रूप से निर्दिष्ट करें।
   - **टोकन सीमाएं**: ट्रंकेशन से बचने के लिए प्रॉम्प्ट्स को मॉडल की कॉन्टेक्स्ट विंडो (जैसे Claude 3.5 Sonnet के लिए 200K टोकन) के अंदर रखें।

#### 3. **उदाहरण: कोड जनरेट करना**
   यहां बताया गया है कि एक साधारण Python फंक्शन जनरेट करने के लिए Claude का उपयोग कैसे करें। इसे अपने कोड में उपयोग करें:

   ```python
   from openai import OpenAI

   client = OpenAI(
       base_url="https://openrouter.ai/api/v1",
       api_key="YOUR_OPENROUTER_API_KEY_HERE",  # अपनी कुंजी से बदलें
   )

   # कोड जनरेट करने के लिए Claude को प्रॉम्प्ट करें
   response = client.chat.completions.create(
       model="anthropic/claude-3.5-sonnet",
       messages=[
           {"role": "system", "content": "You are an expert Python programmer. Provide clean, efficient code with comments."},
           {"role": "user", "content": "Write a Python function to calculate the factorial of a number using recursion. Include error handling for negative inputs."}
       ],
       temperature=0.2,  # निर्धारित कोड के लिए कम तापमान
       max_tokens=500
   )

   # जनरेट किया गया कोड निकालें और प्रिंट करें
   generated_code = response.choices[0].message.content
   print(generated_code)
   ```

   **अपेक्षित आउटपुट (उदाहरण)**:
   ```
   def factorial(n):
       """
       Calculate the factorial of a non-negative integer using recursion.
       
       Args:
       n (int): The number to calculate factorial for.
       
       Returns:
       int: The factorial of n.
       
       Raises:
       ValueError: If n is negative.
       """
       if n < 0:
           raise ValueError("Factorial is not defined for negative numbers.")
       if n == 0 or n == 1:
           return 1
       return n * factorial(n - 1)
   ```

#### 4. **उदाहरण: कोड डीबग करना**
   बगी कोड को Claude को फीड करें और फिक्स के लिए कहें।

   **प्रॉम्प्ट उदाहरण** (`messages` लिस्ट में जोड़ें):
   ```
   {"role": "user", "content": "Debug this Python code: def add(a, b): return a + c. Error: NameError: name 'c' is not defined. Fix it and explain."}
   ```

   Claude इस तरह प्रतिक्रिया दे सकता है: "The error is due to 'c' not being defined. Change to 'return a + b'. Explanation: Typo in variable name."

#### 5. **उदाहरण: कॉन्सेप्ट्स समझाना**
   सीखने के लिए, कोड स्निपेट्स के साथ स्पष्टीकरण के लिए कहें।

   **प्रॉम्प्ट उदाहरण**:
   ```
   {"role": "user", "content": "Explain how decorators work in Python, with a simple example."}
   ```

   इससे लॉगिंग डेकोरेटर जैसे कोड के साथ एक विस्तृत प्रतिक्रिया मिल सकती है।

#### 6. **एडवांस्ड उपयोग: प्रोजेक्ट बनाना**
   - मैसेज हिस्ट्री को मेंटेन करके एक कन्वर्सेशन शुरू करें। संदर्भ के लिए पिछली प्रतिक्रियाओं को `messages` लिस्ट में एपेंड करें।
   - उदाहरण: पहले वेब स्क्रैपर आउटलाइन के लिए प्रॉम्प्ट करें, फिर "Add error handling to the code you provided." के साथ रिफाइन करें।
   - टूल्स के साथ इंटीग्रेट करें: ऐसा कोड जनरेट करने के लिए Claude का उपयोग करें जिसे आप लोकली या अन्य APIs के माध्यम से टेस्ट कर सकें।

#### 7. **भारतीय उपयोगकर्ताओं के लिए सुझाव**
   - आप हिंदी में प्रॉम्प्ट कर सकते हैं: Claude मल्टीलिंगुअल इनपुट को सपोर्ट करता है। उदाहरण के लिए, {"role": "user", "content": "पायथन में फैक्टोरियल कैलकुलेट करने वाला एक फंक्शन लिखें, जिसमें नेगेटिव इनपुट के लिए एरर हैंडलिंग भी हो।"} (यदि हिंदी में प्रॉम्प्ट किया जाएगा तो यह हिंदी में प्रतिक्रिया देगा)।
   - लागत: कोडिंग प्रॉम्प्ट्स टोकन-हैवी होते हैं, इसलिए अपने OpenRouter बैलेंस पर नजर रखें। छोटे प्रॉम्प्ट्स से शुरुआत करें।
   - यदि आवश्यक हो तो विकल्प: यदि OpenRouter की सीमाएं हिट हो जाती हैं, तो अन्य प्लेटफॉर्म पर मुफ्त टायर्स पर विचार करें, लेकिन वे Claude तक रूट नहीं कर सकते हैं।

यदि आप एक विशिष्ट प्रोग्रामिंग टास्क या भाषा प्रदान करते हैं, तो मैं एक अनुरूप उदाहरण दे सकता हूं!

[OpenRouter Documentation](https://openrouter.ai/docs)  
[Anthropic Prompting Guide for Coding](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)  
[Claude 3.5 Sonnet Model Card](https://www.anthropic.com/news/claude-3-5-sonnet)