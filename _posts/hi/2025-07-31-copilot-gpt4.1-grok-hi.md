---
audio: false
generated: true
image: false
lang: hi
layout: post
title: कस्टम मॉडल के लिए कोपायलट कॉन्फ़िगर करना
translated: true
type: note
---

जब आप GitHub Copilot में "managed models" चुनते हैं और फिर भी GPT-4.1 को डिफ़ॉल्ट के रूप में देखते हैं, या OpenRouter से Grok या Kimi मॉडल्स का उपयोग अपेक्षा के अनुरूप नहीं कर पाते हैं, तो इसके कुछ संभावित कारण और इसे हल करने के चरण हो सकते हैं। यहाँ इस मुद्दे का विवरण और Copilot को OpenRouter के माध्यम से Grok या Kimi मॉडल्स का उपयोग करने के लिए कॉन्फ़िगर करने का तरीका दिया गया है:

### GPT-4.1 का अभी भी उपयोग क्यों हो रहा है
1.  **डिफ़ॉल्ट मॉडल सेटिंग**: GitHub Copilot, Copilot Chat, Edits और Agent Mode के लिए GPT-4.1 को डिफ़ॉल्ट के रूप में उपयोग करता है, जब तक कि इसे स्पष्ट रूप से नहीं बदला जाता है। यहाँ तक कि जब आप "managed models" चुनते हैं, तब भी डिफ़ॉल्ट मॉडल बना रह सकता है यदि आपने OpenRouter इंटीग्रेशन को पूरी तरह से कॉन्फ़िगर नहीं किया है या कोई विशिष्ट मॉडल नहीं चुना है।[](https://github.blog/changelog/2025-05-08-openai-gpt-4-1-is-now-generally-available-in-github-copilot-as-the-new-default-model/)
2.  **संदर्भ-विशिष्ट मॉडल उपयोग**: Copilot में "फिक्स बॉक्स" (इनलाइन चैट या कोड कम्प्लीशन) कुछ संदर्भों में Grok या Kimi जैसे कस्टम मॉडल्स पर स्विच करने का सपोर्ट नहीं कर सकता है। उदाहरण के लिए, Copilot Chat पैनल या इनलाइन सुझाव डिफ़ॉल्ट मॉडल (GPT-4.1) का उपयोग कर सकते हैं, जब तक कि आप इमर्सिव व्यू या Agent Mode में स्पष्ट रूप से कस्टम मॉडल पर स्विच नहीं करते।[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model)
3.  **OpenRouter इंटीग्रेशन की सीमाएँ**: OpenRouter, Grok (xAI द्वारा निर्मित) और Kimi (Moonshot AI से) जैसे मॉडल्स तक पहुँच की अनुमति देता है, लेकिन Copilot का OpenRouter के साथ इंटीग्रेशन एक विशिष्ट सेटअप की मांग करता है, और सभी मॉडल API सीमाओं या कॉन्फ़िगरेशन समस्याओं के कारण तुरंत उपलब्ध नहीं हो सकते हैं। उदाहरण के लिए, OpenRouter का API सभी मॉडल्स के लिए टूल सपोर्ट की घोषणा नहीं कर सकता है, जो Agent Mode या कुछ फीचर्स को Grok या Kimi के साथ काम करने से रोक सकता है।[](https://bas.codes/posts/how-to-use-third-party-models-in-copilot-agent-mode/)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)
4.  **सब्सक्रिप्शन या कॉन्फ़िगरेशन प्रतिबंध**: यदि आप फ्री टियर या गैर-प्रो/बिजनेस Copilot सब्सक्रिप्शन का उपयोग कर रहे हैं, तो आप GPT-4.1 जैसे डिफ़ॉल्ट मॉडल्स तक सीमित हो सकते हैं। इसके अतिरिक्त, कुछ मॉडल (जैसे Grok या Kimi) के लिए OpenRouter के माध्यम से विशिष्ट कॉन्फ़िगरेशन या प्रीमियम एक्सेस की आवश्यकता हो सकती है।[](https://www.reddit.com/r/LocalLLaMA/comments/1jslnxb/github_copilot_now_supports_ollama_and_openrouter/)[](https://github.com/microsoft/vscode-copilot-release/issues/10193)

### OpenRouter के माध्यम से Copilot में Grok या Kimi मॉडल्स का उपयोग कैसे करें
Copilot में "फिक्स बॉक्स" (इनलाइन चैट या कोड कम्प्लीशन) के लिए OpenRouter से Grok या Kimi मॉडल्स का उपयोग करने के लिए, इन चरणों का पालन करें:

1.  **Copilot के साथ OpenRouter सेट करें**:
    -   **OpenRouter API Key प्राप्त करें**: [openrouter.ai](https://openrouter.ai) पर साइन अप करें और एक API key प्राप्त करें। सुनिश्चित करें कि आपके पास क्रेडिट या ऐसी योजना है जो Grok (xAI) और Kimi (Moonshot AI K2) मॉडल्स तक पहुँच का सपोर्ट करती है।[](https://openrouter.ai/models)[](https://openrouter.ai)
    -   **VS Code में OpenRouter कॉन्फ़िगर करें**:
        -   Visual Studio Code (VS Code) खोलें और सुनिश्चित करें कि नवीनतम GitHub Copilot एक्सटेंशन इंस्टॉल है (v1.100.2 या बाद का)।[](https://github.com/microsoft/vscode-copilot-release/issues/10193)
        -   Copilot डैशबोर्ड पर जाएं (स्टेटस बार में), या कमांड पैलेट (`Ctrl+Shift+P` या Mac पर `Command+Shift+P`) खोलें और `GitHub Copilot: Manage Models` टाइप करें।
        -   अपनी OpenRouter API key जोड़ें और एंडपॉइंट को OpenRouter मॉडल्स को शामिल करने के लिए कॉन्फ़िगर करें। VS Code के Copilot एक्सटेंशन के साथ इंटीग्रेट करने के लिए आपको OpenRouter के डॉक्यूमेंटेशन का पालन करने की आवश्यकता हो सकती है।[](https://www.reddit.com/r/LocalLLaMA/comments/1jslnxb/github_copilot_now_supports_ollama_and_openrouter/)
    -   **मॉडल उपलब्धता सत्यापित करें**: OpenRouter एंडपॉइंट जोड़ने के बाद, Copilot के "Manage Models" सेक्शन को चेक करें। `openrouter/xai/grok` या `openrouter/moonshotai/kimi-k2` जैसे मॉडल मॉडल पिकर में दिखाई देने चाहिए। यदि वे नहीं दिखते हैं, तो सुनिश्चित करें कि आपके OpenRouter अकाउंट की इन मॉडल्स तक पहुँच है और कोई प्रतिबंध (जैसे, फ्री टियर सीमाएँ) नहीं हैं।[](https://github.com/microsoft/vscode-copilot-release/issues/10193)

2.  **फिक्स बॉक्स के लिए मॉडल्स बदलें**:
    -   **इनलाइन चैट (फिक्स बॉक्स) के लिए**: "फिक्स बॉक्स" संभवतः Copilot के इनलाइन चैट या कोड कम्प्लीशन फीचर को संदर्भित करता है। इनलाइन चैट के लिए मॉडल बदलने के लिए:
        -   VS Code में Copilot Chat इंटरफेस खोलें (टाइटल बार या साइडबार में आइकन के माध्यम से)।
        -   चैट व्यू में, `CURRENT-MODEL` ड्रॉपडाउन मेनू (आमतौर पर नीचे दाईं ओर) का चयन करें और यदि उपलब्ध हो तो `openrouter/xai/grok` या `openrouter/moonshotai/kimi-k2` चुनें।[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model)
        -   यदि ड्रॉपडाउन में Grok या Kimi नहीं दिखाई देते हैं, तो इसका कारण OpenRouter के API द्वारा इन मॉडल्स के लिए टूल सपोर्ट की घोषणा न करना हो सकता है, जो Agent Mode या इनलाइन फिक्स जैसे कुछ Copilot फीचर्स में उनके उपयोग को सीमित कर सकता है।[](https://bas.codes/posts/how-to-use-third-party-models-in-copilot-agent-mode/)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)
    -   **कोड कम्प्लीशन के लिए**: कोड कम्प्लीशन (केवल चैट नहीं) के लिए मॉडल बदलने के लिए:
        -   कमांड पैलेट (`Ctrl+Shift+P` या Mac पर `Command+Shift+P`) खोलें और `GitHub Copilot: Change Completions Model` टाइप करें।
        -   सूची से वांछित OpenRouter मॉडल (जैसे, Grok या Kimi) का चयन करें। ध्यान दें कि VS Code की वर्तमान सीमा (जो कस्टम मॉडल्स के लिए केवल Ollama एंडपॉइंट्स का सपोर्ट करती है) के कारण सभी OpenRouter मॉडल कोड कम्प्लीशन का सपोर्ट नहीं कर सकते हैं, हालाँकि OpenRouter एक प्रॉक्सी वर्कअराउंड के साथ काम कर सकता है।[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-completion-model)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)

3.  **OpenRouter मॉडल्स के लिए वर्कअराउंड**:
    -   **प्रॉक्सी सॉल्यूशन**: चूँकि OpenRouter का API हमेशा टूल सपोर्ट (Agent Mode या एडवांस्ड फीचर्स के लिए आवश्यक) की घोषणा नहीं करता है, आप Copilot में Grok या Kimi को सक्षम करने के लिए `litellm` जैसे प्रॉक्सी का उपयोग कर सकते हैं। `config.yaml` फ़ाइल को शामिल करने के लिए एडिट करें:
        ```yaml
        model_list:
          - model_name: grok
            litellm_params:
              model: openrouter/xai/grok
          - model_name: kimi-k2
            litellm_params:
              model: openrouter/moonshotai/kimi-k2
        ```
        -   प्रॉक्सी को कॉन्फ़िगर करने के विस्तृत चरणों के लिए [Bas codes](https://bas.codes) या [DEV Community](https://dev.to) जैसे स्रोतों से सेटअप निर्देशों का पालन करें।[](https://bas.codes/posts/how-to-use-third-party-models-in-copilot-agent-mode/)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)
    -   **VS Code रीस्टार्ट करें**: प्रॉक्सी को कॉन्फ़िगर करने के बाद, यह सुनिश्चित करने के लिए VS Code को रीस्टार्ट करें कि नए मॉडल मॉडल पिकर में उपलब्ध हैं।

4.  **सब्सक्रिप्शन और अनुमतियाँ जाँचें**:
    -   **Copilot सब्सक्रिप्शन**: सुनिश्चित करें कि आपके पास Copilot Pro या Business सब्सक्रिप्शन है, क्योंकि फ्री-टियर उपयोगकर्ताओं के पास कस्टम मॉडल जोड़ने का विकल्प नहीं हो सकता है।[](https://www.reddit.com/r/LocalLLaMA/comments/1jslnxb/github_copilot_now_supports_ollama_and_openrouter/)
    -   **बिजनेस प्रतिबंध**: यदि आप Copilot Business सब्सक्रिप्शन का उपयोग कर रहे हैं, तो आपकी संगठन को मॉडल स्विचिंग को सक्षम करना होगा। अपने एडमिन से जाँच करें या Copilot पॉलिसियों को प्रबंधित करने के लिए GitHub के डॉक्यूमेंटेशन का संदर्भ लें।[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model)
    -   **OpenRouter क्रेडिट्स**: सत्यापित करें कि आपके OpenRouter अकाउंट में Grok या Kimi जैसे प्रीमियम मॉडल्स तक पहुँचने के लिए पर्याप्त क्रेडिट हैं, क्योंकि ये अन्य की तुलना में अधिक क्रेडिट का उपयोग कर सकते हैं।[](https://www.reddit.com/r/GithubCopilot/comments/1la87wr/why_are_gh_copilot_pro_models_so_much_worse_than/)

5.  **फिक्स बॉक्स का ट्रबलशूटिंग**:
    -   यदि फिक्स बॉक्स अभी भी GPT-4.1 का उपयोग कर रहा है, तो इसका कारण यह हो सकता है कि इनलाइन चैट फीचर कुछ संदर्भों (जैसे, गैर-इमर्सिव व्यू) में डिफ़ॉल्ट मॉडल पर लॉक है। Grok या Kimi को स्पष्ट रूप से चुनने के लिए Copilot Chat के इमर्सिव व्यू (`https://github.com/copilot`) पर स्विच करने का प्रयास करें।[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model)
    -   यदि Grok या Kimi मॉडल पिकर में नहीं दिखाई देते हैं, तो `Manage Models` में OpenRouter इंटीग्रेशन को डबल-चेक करें। आपको मॉडल सूची को रिफ्रेश करने या OpenRouter API key को फिर से जोड़ने की आवश्यकता हो सकती है।[](https://github.com/microsoft/vscode-copilot-release/issues/10193)
    -   यदि समस्या बनी रहती है, तो पहले यह पुष्टि करने के लिए कि वे काम कर रहे हैं, Copilot के Agent Mode या चैट इंटरफेस में मॉडल्स का परीक्षण करें, फिर उन्हें इनलाइन फिक्स पर लागू करने का प्रयास करें।

6.  **वैकल्पिक टूल्स**:
    -   यदि Copilot के साथ OpenRouter इंटीग्रेशन समस्याग्रस्त बना रहता है, तो Grok का सीधे [grok.com](https://grok.com) के माध्यम से या Grok iOS/Android ऐप्स का उपयोग करने पर विचार करें, जो उपयोग कोटा के साथ मुफ्त पहुँच प्रदान करते हैं। Kimi मॉडल्स का परीक्षण OpenRouter के चैट इंटरफेस के माध्यम से भी किया जा सकता है ताकि यह सुनिश्चित हो सके कि वे सुलभ हैं।[](https://openrouter.ai)
    -   अधिक सहज अनुभव के लिए, आप अन्य IDE या टूल्स जैसे Cursor का पता लगा सकते हैं, जो OpenRouter के Kimi K2 मॉडल के साथ अच्छी तरह से काम करने के लिए नोट किया गया है।[](https://openrouter.ai)

### अतिरिक्त नोट्स
-   **मॉडल परफॉर्मेंस**: Grok रीजनिंग और ट्रुथ-सीकिंग के लिए ऑप्टिमाइज़ है, जो इसे जटिल डीबगिंग या आर्किटेक्चरल टास्क्स के लिए उपयुक्त बनाता है, जबकि Kimi (K2) विशिष्ट कोडिंग परिदृश्यों में बेहतर प्रदर्शन कर सकती है। अपने उपयोग के मामले के लिए बेहतर प्रदर्शन करने वाले को देखने के लिए दोनों का परीक्षण करें।[](https://github.blog/ai-and-ml/github-copilot/which-ai-model-should-i-use-with-github-copilot/)
-   **कम्युनिटी फीडबैक**: कुछ उपयोगकर्ता Copilot के मॉडल पिकर में OpenRouter मॉडल्स के न दिखने की समस्याओं की रिपोर्ट करते हैं, खासकर फ्री-टियर अकाउंट्स के साथ। इसे हल करने के लिए पेड OpenRouter प्लान या Copilot Pro सब्सक्रिप्शन की आवश्यकता हो सकती है।[](https://github.com/microsoft/vscode-copilot-release/issues/10193)[](https://www.reddit.com/r/GithubCopilot/comments/1la87wr/why_are_gh_copilot_pro_models_so_much_worse_than/)
-   **चल रही सीमाएँ**: Copilot में सीधे कस्टम API एंडपॉइंट्स को सक्षम करने के बारे में एक खुली चर्चा है (देखें [microsoft/vscode-copilot-release#7518](https://github.com/microsoft/vscode-copilot-release/issues/7518))। जब तक इसे लागू नहीं किया जाता है, Grok या Kimi का उपयोग करने के लिए प्रॉक्सी वर्कअराउंड सबसे विश्वसनीय तरीका है।[](https://bas.codes/posts/how-to-use-third-party-models-in-copilot-agent-mode/)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)

### साइटेशन्स
-   [Changing the AI model for Copilot Chat - GitHub Docs](https://docs.github.com/en/copilot/managing-copilot/changing-the-ai-model-for-copilot-chat)[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model)
-   [How to Use Third Party Models in GitHub Copilot Agent Mode - Bas codes](https://bas.codes)[](https://bas.codes/posts/how-to-use-third-party-models-in-copilot-agent-mode/)
-   [Openrouter - openrouter.ai](https://openrouter.ai)[](https://openrouter.ai/models)
-   [Agent Mode With Third-Party Models in Copilot - DEV Community](https://dev.to)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)
-   [Openrouter - openrouter.ai](https://openrouter.ai)[](https://openrouter.ai)
-   [r/LocalLLaMA on Reddit: Github Copilot now supports Ollama and OpenRouter Models](https://www.reddit.com)[](https://www.reddit.com/r/LocalLLaMA/comments/1jslnxb/github_copilot_now_supports_ollama_and_openrouter/)
-   [Which AI model should I use with GitHub Copilot? - The GitHub Blog](https://github.blog)[](https://github.blog/ai-and-ml/github-copilot/which-ai-model-should-i-use-with-github-copilot/)
-   [OpenAI GPT-4.1 is now generally available in GitHub Copilot - GitHub Changelog](https://github.blog)[](https://github.blog/changelog/2025-05-08-openai-gpt-4-1-is-now-generally-available-in-github-copilot-as-the-new-default-model/)
-   [OpenRouter (free) Models Missing from Manage Models - GitHub Issues](https://github.com/microsoft/vscode-copilot-release/issues/10193)[](https://github.com/microsoft/vscode-copilot-release/issues/10193)

यदि आप विशिष्ट त्रुटियों का सामना करते हैं या सेटअप के साथ और सहायता की आवश्यकता है, तो कृपया अधिक विवरण प्रदान करें (जैसे, त्रुटि संदेश, VS Code संस्करण, या सब्सक्रिप्शन प्रकार), और मैं समाधान को और अधिक अनुरूप बना सकता हूँ!