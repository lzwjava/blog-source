---
audio: false
generated: true
image: false
lang: hi
layout: post
title: एआई मॉडल संदर्भ विंडो तुलना २०२५
translated: true
type: note
---

यहां आपके द्वारा सूचीबद्ध मॉडलों के संदर्भ विंडो आकारों का एक स्पष्ट विवरण दिया गया है—बिना तालिका के:

---

### अग्रणी संदर्भ विंडो

**Gemini-2.5-Pro**
Google का Gemini 2.5 Pro **1 मिलियन टोकन** की एक संदर्भ विंडो प्रदान करता है—और जल्द ही इसे **2 मिलियन टोकन** तक विस्तारित करने की योजना है ([Google AI for Developers][1], [blog.google][2])। यह उल्लिखित मॉडलों में वर्तमान में सबसे बड़ी है।

---

### Claude मॉडल (Anthropic परिवार)

* **Claude‑3 Opus** (और Sonnet जैसे परिवार) ने शुरू में **200 k टोकन** प्रदान किए, जिसमें चुनिंदा उपयोगकर्ताओं के लिए 1 मिलियन से अधिक की क्षमताएं थीं ([Reddit][3], [Wikipedia][4])।
* भुगतान योजनाओं पर, संदर्भ विंडो **200 k+ टोकन** (लगभग 500 पृष्ठ) ही रहती है ([Anthropic Help Center][5])।
* एंटरप्राइज योजनाओं पर **Sonnet 4** **500 k टोकन** तक प्रदान करता है ([Anthropic Help Center][6])।
* और, Claude Code API के माध्यम से, **Claude 4 Sonnet** **1 मिलियन टोकन** का समर्थन कर सकता है ([ClaudeLog][7])।

अतः अधिकतम संदर्भ:

* मानक Claude Opus 4: \~200 k टोकन।
* Sonnet 4 (Enterprise): 500 k टोकन तक।
* API के माध्यम से Claude 4 Sonnet (Claude Code): 1 मिलियन टोकन तक।

---

### GPT-5 (OpenAI)

* OpenAI आधिकारिक तौर पर GPT‑5 के लिए **256 k टोकन** की संदर्भ विंडो बताता है ([WIRED][8], [Amazon Web Services, Inc.][9], [Anthropic Help Center][10])।
* कुछ स्रोतों का सुझाव है कि निःशुल्क ChatGPT इंटरफेस 256 k टोकन का समर्थन करता है, जबकि API वेरिएंट अधिक हो सकते हैं—लेकिन GPT‑5 के लिए 1M टोकन की पुष्टि नहीं हुई है ([Cinco Días][11])।
* समुदाय रिपोर्टों में एक ऊपरी सीमा की अटकलों का उल्लेख है, लेकिन प्रलेखन 256 k पर स्थिर दिखता है ([OpenAI Community][12], [Encord][13]).

---

### अन्य मॉडल

* **Gemini-Flash** के संभवतः अन्य Gemini मॉडलों के समान ही बड़ी संदर्भ विंडो (1 मिलियन+) है, लेकिन विशेष रूप से "Flash" के लिए विवरण पुष्टि नहीं हैं।
* **अन्य सूचीबद्ध मॉडल**—जैसे "kimi-k2", "deepseek-v3/x", "mistral-medium", "qwen-coder", और "gpt-oss"—संदर्भ विंडो आकार के संबंध में मेरे द्वारा खोजे गए स्रोतों में प्रमुखता से प्रलेखित नहीं हैं। संभवतः वे अधिक मानक सीमा (जैसे, <200 k) प्रदान करते हैं, हालांकि बिना स्पष्ट पुष्टि के।

---

### निष्कर्ष

* **कुल मिलाकर सबसे बड़ी संदर्भ विंडो:** **Gemini 2.5 Pro** (1 मिलियन टोकन, 2 मिलियन तक विस्तारणीय)
* **नज़दीकी दूसरे स्थान पर:** **API के माध्यम से Claude 4 Sonnet** (\~1 मिलियन टोकन)
* **फिर:** **GPT-5** (\~256 k टोकन)
* **इसके बाद:** मानक **Claude मॉडल** (\~200 k टोकन), जिसमें **Sonnet 4 Enterprise** 500 k टोकन तक बढ़ जाता है।

---

[1]: https://ai.google.dev/gemini-api/docs/long-context?utm_source=chatgpt.com "Long context | Gemini API | Google AI for Developers"
[2]: https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/?utm_source=chatgpt.com "Gemini 2.5: Our most intelligent AI model - The Keyword"
[3]: https://www.reddit.com/r/singularity/comments/1b6e0id/claude_3_context_window_is_a_big_deal/?utm_source=chatgpt.com "Claude 3 context window is a big deal : r/singularity - Reddit"
[4]: https://en.wikipedia.org/wiki/Claude_%28language_model%29?utm_source=chatgpt.com "Claude (language model)"
[5]: https://support.anthropic.com/en/articles/7996856-what-is-the-maximum-prompt-length?utm_source=chatgpt.com "What is the maximum prompt length? | Anthropic Help Center"
[6]: https://support.anthropic.com/en/articles/11647753-understanding-usage-and-length-limits?utm_source=chatgpt.com "Understanding Usage and Length Limits | Anthropic Help Center"
[7]: https://www.claudelog.com/faqs/what-is-context-window-in-claude-code/?utm_source=chatgpt.com "What is Context Window in Claude Code"
[8]: https://www.wired.com/story/openais-gpt-5-is-here/?utm_source=chatgpt.com "OpenAI Finally Launched GPT-5. Here's Everything You ..."
[9]: https://aws.amazon.com/bedrock/anthropic/?utm_source=chatgpt.com "Anthropic's Claude in Amazon Bedrock - AWS"
[10]: https://support.anthropic.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans?utm_source=chatgpt.com "How large is the context window on paid Claude plans?"
[11]: https://cincodias.elpais.com/smartlife/lifestyle/2025-08-11/gpt-5-openai-grandes-novedades.html?utm_source=chatgpt.com "GPT-5 de OpenAI: estas son sus grandes novedades para gobernar la IA en 2025"
[12]: https://community.openai.com/t/huge-gpt-5-documentation-gap-flaw-causing-bugs-input-tokens-exceed-the-configured-limit-of-272-000-tokens/1344734?utm_source=chatgpt.com "HUGE GPT-5 DOCUMENTATION GAP/FLAW causing bugs"
[13]: https://encord.com/blog/gpt-5-a-technical-breakdown/?utm_source=chatgpt.com "GPT-5: A Technical Breakdown"