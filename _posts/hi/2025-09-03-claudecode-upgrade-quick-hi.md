---
audio: false
generated: true
image: false
lang: hi
layout: post
title: क्लॉड कोड को तुरंत अपग्रेड करें
translated: true
type: note
---

अगर आप **Claude Code** को अपग्रेड करना चाहते हैं, जो कि Anthropic का कमांड-लाइन कोडिंग एजेंट है, तो यहां बताया गया है कि आप कैसे कर सकते हैं—और नई क्षमताएं जैसे लर्निंग मोड और कस्टम सबएजेंट को सही तरीके से काम करते हुए पा सकते हैं।

---

### Claude Code को कैसे अपग्रेड करें

1.  **अपना वर्तमान वर्जन चेक करें**
    रन करें:

    ```
    claude --version
    ```

    इससे आप देख सकते हैं कि आप वर्तमान में कौन सा वर्जन चला रहे हैं।

2.  **npm के जरिए अपडेट करें**
    सबसे आसान अपग्रेड विधि है:

    ```
    npm install -g @anthropic-ai/claude-code@latest
    ```

    यह npm से नवीनतम रिलीज डाउनलोड करता है।
    Reddit पर उपयोगकर्ताओं ने बताया है कि इससे बग्स ठीक हुए और रिस्पॉन्सिवनेस में सुधार हुआ। एक ने लिखा:

    > "नवीनतम वर्जन (1.0.18) में अपडेट करने के बाद, यह दिन और रात जैसा अंतर है — यह कहीं अधिक स्मार्ट और रिस्पॉन्सिव लगता है।"
    > ([Reddit][1], [Anthropic][2])

3.  **वैकल्पिक रूप से, नेटिव इंस्टॉलर (Beta) का उपयोग करें**
    अगर आप एक स्टैंडअलोन बाइनरी (npm के बजाय) पसंद करते हैं, तो आज़माएं:

    ```
    curl -fsSL https://claude.ai/install.sh | bash -s latest
    ```

    (Windows पर, PowerShell वर्जन का उपयोग करें)
    ([Anthropic][3])

4.  **अपडेट को वेरीफाई करें**
    इंस्टालेशन के बाद, अपनी टर्मिनल को रीस्टार्ट करें और फिर से `claude --version` रन करके पुष्टि करें कि नया वर्जन एक्टिव है।

5.  **इंस्टालेशन समस्याओं का समाधान**
    अगर आपको समस्याओं का सामना करना पड़े, तो पहले अनइंस्टॉल करने का प्रयास करें:

    ```
    npm uninstall -g @anthropic-ai/claude-code
    npm install -g @anthropic-ai/claude-code
    ```

    कुछ उपयोगकर्ताओं ने पाया कि इस क्रम से अपडेट ग्लिचेस ठीक हो गए। ([Anthropic][4], [Reddit][1], [Anthropic][5], [The Verge][6])

---

### हाल के अपडेट्स में क्या नया है?

#### लर्निंग मोड

Anthropic ने हाल ही में Claude Code के भीतर दो नई लर्निंग स्टाइल जोड़ी हैं: **"Explanatory"** और **"Learning"**। ये आपको सिर्फ सॉल्यूशन देने के बजाय जनरेट किए गए कोड के पीछे के तर्क को समझने में मदद करती हैं। इन्हें एनेबल करने के लिए:

1.  सुनिश्चित करें कि आपने Claude Code अपडेट कर लिया है।
2.  अपने Claude Code सेशन में `/output-styles` रन करें।
3.  **Default**, **Explanatory**, या **Learning** स्टाइल के बीच चयन करें।
    यह फीचर **14 अगस्त, 2025** को लॉन्च हुआ था। ([Tom's Guide][7])

#### कस्टम सबएजेंट

Claude Code अब **सबएजेंट** को सपोर्ट करता है—विशिष्ट कार्यों (जैसे, बग फिक्सिंग, रिफैक्टरिंग, डॉक्युमेंटेशन) के लिए तैयार किए गए विशेष AI असिस्टेंट। आप प्रत्येक के लिए अलग-अलग सिस्टम प्रॉम्प्ट, टूल परमिशन, और कॉन्टेक्स्ट विंडो सेट कर सकते हैं।
एक सेट अप करने के लिए:

1.  `/agents` रन करें
2.  "Create New Agent" चुनें (या तो यूजर-लेवल या प्रोजेक्ट-लेवल)
3.  इसके बिहेवियर, अनुमत टूल्स को परिभाषित करें और सेव करें
    सबएजेंट आपके वर्कफ़्लो को साफ, अधिक फोकस्ड और कॉन्टेक्स्ट-अवेयर रखने में मदद करते हैं। ([Anthropic][8])

---

### त्वरित सारांश (कोई टेबल नहीं, सिर्फ स्पष्ट चरण)

*   **अपग्रेड करने के लिए**:

    ```
    npm install -g @anthropic-ai/claude-code@latest
    ```

    या नेटिव इंस्टॉल का उपयोग करें `curl | bash -s latest` के साथ।

*   **लर्निंग मोड एनेबल करें**:

    *   अपडेट करें
    *   Claude Code के अंदर: `/output-styles` रन करें और अपना मोड चुनें।

*   **सबएजेंट बनाएं**:

    *   Claude Code के अंदर: `/agents` रन करें
    *   टूल एक्सेस, सिस्टम प्रॉम्प्ट और बिहेवियर को कस्टमाइज़ करें।

---

### अंतिम विचार

Claude Code को अपग्रेड करना सीधा-सादा है—npm या नेटिव इंस्टॉलर का उपयोग करें, जांचें कि आप नवीनतम वर्जन पर हैं, फिर नए **लर्निंग मोड** और **सबएजेंट** फीचर्स को एक्सप्लोर करें। ये जोड़ Claude Code को सिर्फ एक कोडिंग असिस्टेंट होने के बजाय आपके डेवलपमेंट वर्कफ़्लो में एक टीचिंग पार्टनर और एजेंटिक कोलैबोरेटर जैसा बना देते हैं।

अगर आप अपना पहला सबएजेंट क्राफ्ट करने या लर्निंग मोड का प्रभावी ढंग से उपयोग करने में मदद चाहते हैं, तो मैं आपको इसमें मार्गदर्शन करने में प्रसन्न रहूंगा!

[1]: https://www.reddit.com/r/ClaudeAI/comments/1l8gbfo/dont_forget_to_update_your_claude_cli_it_makes_a/?utm_source=chatgpt.com "Don't forget to update your Claude CLI! It makes a huge ..."
[2]: https://www.anthropic.com/solutions/agents?utm_source=chatgpt.com "Claude Agents | Intelligent AI Solutions \ Anthropic"
[3]: https://docs.anthropic.com/en/docs/claude-code/quickstart?utm_source=chatgpt.com "Quickstart - Claude Code"
[4]: https://docs.anthropic.com/en/docs/claude-code/settings?utm_source=chatgpt.com "Claude Code settings"
[5]: https://docs.anthropic.com/en/docs/claude-code/overview?utm_source=chatgpt.com "Claude Code overview"
[6]: https://www.theverge.com/2024/11/25/24305774/anthropic-model-context-protocol-data-sources?utm_source=chatgpt.com "Anthropic launches tool to connect AI systems directly to datasets"
[7]: https://www.tomsguide.com/ai/claudes-new-learning-modes-take-on-chatgpts-study-mode-heres-what-they-do?utm_source=chatgpt.com "Claude's new 'learning modes' take on ChatGPT's Study Mode - here's what they do"
[8]: https://docs.anthropic.com/en/docs/claude-code/sub-agents?utm_source=chatgpt.com "Subagents"