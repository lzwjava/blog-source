---
audio: false
generated: true
image: false
lang: hi
layout: post
title: क्लॉड एपीआई मूल्य निर्धारण विवरण 2025
translated: true
type: note
---

यहां आपके द्वारा सूचीबद्ध Anthropic Claude मॉडल्स के लिए API उपयोग मूल्य निर्धारण की एक स्पष्ट व्याख्या दी गई है—कोई टेबल नहीं, बस सीधी-सादी, आसानी से पढ़ी जा सकने वाली भाषा:

---

### Claude Sonnet 4

* **इनपुट टोकन:** प्रति मिलियन \$3
* **आउटपुट टोकन:** प्रति मिलियन \$15
* **उपलब्ध छूट:** प्रॉम्प्ट कैशिंग के साथ **90% तक की छूट**, और बैच प्रोसेसिंग के साथ **50% तक की छूट**। ([custom.typingmind.com][1], [Reddit][2], [Anthropic][3], [Anthropic][4])

---

### Claude 3.5 Sonnet (अब अप्रचलित)

* **इनपुट टोकन:** प्रति मिलियन \$3
* **आउटपुट टोकन:** प्रति मिलियन \$15
* **बैच और कैश दरें:** अन्य Sonnet संस्करणों जैसी ही स्तरीय प्रणाली: बैच इनपुट के लिए \$1.50, बैच आउटपुट के लिए \$7.50, और 5‑मिनट कैश हिट के लिए \$0.30। ([Anthropic Docs][5])

---

### Claude 3.7 Sonnet

* **मूल मूल्य निर्धारण:** 3.5 के बिल्कुल समान—प्रति मिलियन इनपुट \$3, प्रति मिलियन आउटपुट \$15—हाइब्रिड "थिंकिंग" मोड का उपयोग करते समय भी। ([Reddit][6], [Anthropic Docs][5])

---

### Claude Opus 4

* **इनपुट टोकन:** प्रति मिलियन \$15
* **आउटपुट टोकन:** प्रति मिलियन \$75
* **बैच और कैश छूट:** बैच इनपुट \$7.50 है; बैच आउटपुट \$37.50 है; कैश हिट की लागत \$1.50 है। ([Anthropic][7], [Amazon Web Services, Inc.][8], [Anthropic Docs][5], [Wikipedia][9])

---

### संक्षिप्त सारांश

* **सभी Sonnet वेरिएंट (3.5, 3.7, 4):** प्रति मिलियन इनपुट \$3 / प्रति मिलियन आउटपुट \$15, बैच और कैशिंग के लिए गहरी छूट के साथ।
* **Opus 4:** काफी अधिक दरें, प्रति मिलियन \$15 / \$75 पर, लेकिन गहन तर्क, लंबे कार्यों और उच्च प्रदर्शन के लिए अनुकूलित।

---

### अतिरिक्त जानकारी

* **मॉडल विकास:** Claude 3.5 Sonnet ने जून 2024 में लॉन्च होने पर कोडिंग क्षमता में नए मानक स्थापित किए, लेकिन फरवरी 2025 में 3.7 और मई 2025 में Sonnet 4 के साथ प्रदर्शन में सुधार के बावजूद मूल्य निर्धारण अपरिवर्तित रहा। ([Business Insider][10], [Anthropic][7], [Anthropic Docs][5], [Wikipedia][11])
* **उपयोग के मामलों का संरेखण:** यदि आका वर्कलोड चैट-केंद्रित या उच्च-वॉल्यूम है, तो Sonnet मॉडल प्रति-प्रदर्शन उत्कृष्ट मूल्य प्रदान करते हैं। गहन जटिल कार्यों या लंबे एजेंटिक वर्कफ़्लो के लिए, Opus या दोनों को मिलाने वाली हाइब्रिड रणनीति अधिक कुशल हो सकती है।

---

मुझे बताएं कि क्या आप विशिष्ट टोकन मात्रा, कैशिंग के साथ तुलना, या किस मॉडल को कब चुनें इसके मार्गदर्शन के आधार पर लागत उदाहरण चाहते हैं—आपको इसमें मदद करके खुशी होगी!

[1]: https://custom.typingmind.com/tools/estimate-llm-usage-costs/claude-3.5-sonnet?utm_source=chatgpt.com "Anthropic claude-3.5-sonnet API Pricing Calculator"
[2]: https://www.reddit.com/r/ClaudeAI/comments/1jclyjp/can_anthropic_keep_up_with_those_pricing/?utm_source=chatgpt.com "Can Anthropic keep up with those pricing ? : r/ClaudeAI"
[3]: https://www.anthropic.com/news/claude-3-5-sonnet?utm_source=chatgpt.com "Introducing Claude 3.5 Sonnet"
[4]: https://www.anthropic.com/claude/sonnet?utm_source=chatgpt.com "Claude Sonnet 4"
[5]: https://docs.anthropic.com/en/docs/about-claude/pricing?utm_source=chatgpt.com "Pricing"
[6]: https://www.reddit.com/r/ClaudeAI/comments/1ixtyj0/sonnet_37_x_cline_costs_are_skyrocketing/?utm_source=chatgpt.com "Sonnet 3.7 x Cline: Costs are skyrocketing? : r/ClaudeAI"
[7]: https://www.anthropic.com/news/claude-3-7-sonnet?utm_source=chatgpt.com "Claude 3.7 Sonnet and Claude Code"
[8]: https://aws.amazon.com/marketplace/pp/prodview-h2mamlwah46ym?utm_source=chatgpt.com "AWS Marketplace: Claude 3.5 Sonnet (Amazon Bedrock Edition)"
[9]: https://zh.wikipedia.org/wiki/Claude_%28%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%29?utm_source=chatgpt.com "Claude (语言模型)"
[10]: https://www.businessinsider.com/anthropic-ai-breakthrough-vibe-coding-revolution-2025-7?utm_source=chatgpt.com "'The Trillion-Dollar Question': How did Anthropic make AI so good at coding?"
[11]: https://en.wikipedia.org/wiki/Claude_%28language_model%29?utm_source=chatgpt.com "Claude (language model)"