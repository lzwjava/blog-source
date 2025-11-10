---
audio: false
generated: true
lang: hi
layout: post
title: जेकिल YAML और फ़ाइल त्रुटियों को ठीक करना
translated: true
type: note
---

आपके द्वारा दिए गए आउटपुट में दो प्रकार की त्रुटियाँ दिख रही हैं:

1.  **YAML अपवाद:** यह आपकी Markdown फ़ाइलों के सबसे ऊपर मौजूद फ्रंट मैटर (YAML ब्लॉक) में किसी समस्या की ओर इशारा करता है:
      * `/Users/lzwjava/projects/lzwjava.github.io/notes/2025-06-25-company-valuation-comparison-en.md`
      * `/Users/lzwjava/projects/lzwjava.github.io/notes/2025-06-25-top-companies-evolve-en.md`
        "did not find expected key while parsing a block mapping at line 2 column 1" त्रुटि बताती है कि इन फ़ाइलों में YAML सिंटैक्स गलत है, संभवतः फ्रंट मैटर में कोई key गायब है या इंडेंटेशन में कोई समस्या है।

2.  **`Errno::ENOENT: No such file or directory @ rb_sysopen - /Users/lzwjava/projects/lzwjava.github.io/wandb/debug-internal.log`**: यह त्रुटि बताती है कि Jekyll एक ऐसी फ़ाइल या डायरेक्टरी तक पहुँचने का प्रयास कर रहा है जो मौजूद नहीं है, विशेष रूप से `/wandb/debug-internal.log`। यह कोई अस्थायी फ़ाइल या किसी अन्य टूल (जैसे Weights & Biases - `wandb`) की निर्भरता हो सकती है जिसे Jekyll प्रोसेस करने की कोशिश कर रहा है।

आपके सवाल का जवाब, कि Jekyll को कुछ डायरेक्टरीज़ को कैसे अनदेखा करने दें, के लिए आप अपनी `_config.yml` फ़ाइल में `exclude` विकल्प का उपयोग कर सकते हैं।

इसे करने का तरीका यहाँ बताया गया है:

1.  **अपनी `_config.yml` फ़ाइल खोलें** (आपकी Jekyll प्रोजेक्ट की रूट डायरेक्टरी में स्थित)।

2.  **`exclude` निर्देश जोड़ें या संशोधित करें।** यह निर्देश पथों (फ़ाइलों या डायरेक्टरीज़) की एक सूची लेता है जिन्हें Jekyll को अपनी बिल्ड प्रक्रिया के दौरान अनदेखा करना चाहिए।

    उदाहरण के लिए, `wandb` डायरेक्टरी और कोई अन्य डायरेक्टरी जिसे आप बाहर रखना चाहते हैं, उसे अनदेखा करने के लिए, अपनी `_config.yml` में निम्नलिखित जोड़ें:

    ```yaml
    exclude:
      - wandb/
      - some_other_directory/
      - another_file_to_ignore.md
    ```

    **महत्वपूर्ण नोट:**

      * यह सुनिश्चित करने के लिए कि उनके अंदर की सभी सामग्री अनदेखी हो जाए, डायरेक्टरीज़ के लिए अंत में स्लैश (`/`) जोड़ना सुनिश्चित करें।
      * पथ आपकी Jekyll प्रोजेक्ट की रूट डायरेक्टरी के सापेक्ष होते हैं।

**`exclude` के साथ आपकी विशिष्ट त्रुटियों का समाधान:**

  * **`wandb` डायरेक्टरी त्रुटि के लिए:** अपनी `_config.yml` में `exclude` सूची में `wandb/` जोड़ने से Jekyll उसके अंदर की फ़ाइलों को पढ़ने का प्रयास करना बंद कर देगा, जिससे `wandb/debug-internal.log` के लिए `No such file or directory` त्रुटि हल हो जाएगी।

  * **YAML अपवाद के लिए:** `exclude` निर्देश आपकी Markdown फ़ाइलों में YAML त्रुटियों को ठीक नहीं करेगा। आपको `notes/2025-06-25-company-valuation-comparison-en.md` और `notes/2025-06-25-top-companies-evolve-en.md` में **मैन्युअल रूप से फ्रंट मैटर को सही करने** की आवश्यकता है।

    **विशिष्ट Jekyll फ्रंट मैटर संरचना:**

    ```yaml
    ---
    layout: post
    title: "My Awesome Post"
    date: 2025-07-02 10:00:00 +0800
    categories: [notes, tech]
    tags: [jekyll, markdown]
    ---

    Your content goes here.
    ```

    YAML अपवाद में उल्लिखित फ़ाइलों को दोबारा जांचें ताकि यह सुनिश्चित हो सके कि वे इस संरचना का पालन करती हैं, विशेष रूप से इंडेंटेशन और सही key-value जोड़े के संदर्भ में। "did not find expected key while parsing a block mapping at line 2 column 1" त्रुटि बताती है कि आपके फ्रंट मैटर की शुरुआत में ही कुछ गड़बड़ है, संभवतः कोई key गायब है या वहाँ एक अतिरिक्त स्पेस है जहाँ एक key होनी चाहिए।

अपनी `_config.yml` में ये परिवर्तन करने और अपनी Markdown फ़ाइलों को सही करने के बाद, अपना Jekyll बिल्ड या सर्व कमांड फिर से चलाने का प्रयास करें।