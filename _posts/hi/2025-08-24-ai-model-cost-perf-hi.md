---
audio: false
generated: true
image: false
lang: hi
layout: post
title: एआई मॉडल लागत और प्रदर्शन गाइड
translated: true
type: note
---

यहां **बेंचमार्क स्कोर** और **एपीआई मूल्य निर्धारण** का प्रत्येक मॉडल—Claude 4 Opus (जिसे Claude Opus 4 भी कहा जाता है), GPT‑5 (मानक/पूर्ण), GPT‑5 Mini, GPT‑5 Nano, साथ ही o3 (OpenAI), और Claude 4 Sonnet—के लिए एक स्पष्ट विवरण दिया गया है, जो चीजों को साफ और पठनीय बनाए रखने के लिए तालिकाओं का उपयोग किए बिना है।

---

## बेंचमार्क प्रदर्शन (SWE-bench)

यह दर्शाता है कि मॉडल सॉफ्टवेयर इंजीनियरिंग कार्यों पर कितना अच्छा प्रदर्शन करते हैं:

* **Claude 4 Opus (14 मई, 2025)**: 67.60
* **GPT‑5 (7 अगस्त, 2025, मध्यम रीजनिंग)**: 65.00
* **Claude 4 Sonnet (14 मई, 2025)**: 64.93 ([SWE-bench][1])

**मुख्य बात**: Claude 4 Opus SWE-bench प्रदर्शन में थोड़ा बढ़त पर है, जिसके बाद GPT-5 और Claude-Sonnet करीब-करीब बराबर हैं।

---

## एपीआई मूल्य निर्धारण (प्रति मिलियन टोकन)

### **Claude 4 Opus**

* इनपुट: **\$15**
* आउटपुट: **\$75** ([Anthropic][2], [LaoZhang AI][3], [Simon Willison’s Weblog][4])

### **GPT-5 (मानक/पूर्ण)**

* इनपुट: **\$1.25**
* कैश्ड इनपुट (पुन: उपयोग होने पर): **\$0.125**
* आउटपुट: **\$10** ([OpenAI][5])

### **GPT-5 Mini**

* इनपुट: **\$0.25**
* आउटपुट: **\$2** ([OpenAI][5], [WIRED][6])

### **GPT-5 Nano**

* इनपुट: **\$0.05**
* आउटपुट: **\$0.40** ([OpenAI][5], [WIRED][6])

### **o3-mini** (संदर्भ के लिए)

* मूल्य निर्धारण o4‑mini संदर्भ के माध्यम से उपलब्ध:
* इनपुट: **\$1.10**, आउटपुट: **\$4.40** ([Simon Willison’s Weblog][4])

### **Claude 4 Sonnet**

* इनपुट: **\$3**, आउटपुट: **\$15** ([LaoZhang AI][3])

---

## त्वरित तुलना के मुख्य बिंदु

* **सर्वश्रेष्ठ प्रदर्शन**: Claude 4 Opus कोडिंग बेंचमार्क में GPT-5 और Claude Sonnet दोनों से थोड़ा बेहतर प्रदर्शन करता है।
* **प्रति टोकन सबसे कम लागत**:

  * **GPT-5 Nano** अब तक का सबसे सस्ता विकल्प है—सारांशण जैसे हल्के-फुल्के कार्यों के लिए बिल्कुल उपयुक्त।
  * **GPT-5 Mini** गति और किफायतीपन का एक अच्छा संतुलन प्रदान करता है।
  * **GPT-5 मानक** काफी लागत-प्रभावी बना हुआ है, खासकर सस्ते कैश के साथ।
* **Claude मॉडल**, Opus और Sonnet दोनों, प्रति टोकन काफी अधिक महंगे हैं लेकिन मजबूत रीजनिंग और एजेंट क्षमताओं के कारण अपनी कीमत को उचित ठहराते हैं।

---

## सारांश (स्पष्ट और संक्षिप्त):

* **Claude 4 Opus**: शीर्ष प्रदर्शन, उच्च लागत (\$15 इनपुट / \$75 आउटपुट)।
* **GPT-5 (पूर्ण)**: बेहतरीन प्रदर्शन (Opus से बस थोड़ा पीछे), कहीं अधिक सस्ता (\$1.25 इनपुट / \$10 आउटपुट)।
* **GPT-5 Mini**: मध्यम-स्तरीय बजट-अनुकूल विकल्प (\$0.25 इनपुट / \$2 आउटपुट)।
* **GPT-5 Nano**: हल्के-फुल्के कार्यों या बड़े पैमाने पर कम लागत वाले उपयोग के लिए आदर्श (\$0.05 इनपुट / \$0.40 आउटपुट)।
* **Claude 4 Sonnet**: मध्यम लागत/प्रदर्शन (\$3 इनपुट / \$15 आउटपुट), लेकिन बेंचमार्क दूसरों से थोड़ा नीचे है।

---

अगर आप किसी विशेष उपयोग पैटर्न के लिए **मासिक लागत** का अनुमान लगाने में सहायता चाहते हैं, या प्रॉम्प्ट कैशिंग और बैच छूट को शामिल करते हुए तुलना की आवश्यकता है, तो मुझे बताएं!

[1]: https://www.swebench.com/?utm_source=chatgpt.com "SWE-bench Leaderboards"
[2]: https://www.anthropic.com/pricing?utm_source=chatgpt.com "Pricing"
[3]: https://blog.laozhang.ai/ai-tools/claude-4-pricing-guide-2025/?utm_source=chatgpt.com "Claude 4.0 Pricing Guide: Complete Cost Analysis & Best ..."
[4]: https://simonwillison.net/2025/Aug/7/gpt-5/?utm_source=chatgpt.com "GPT-5: Key characteristics, pricing and model card"
[5]: https://openai.com/api/pricing/?utm_source=chatgpt.com "API Pricing"
[6]: https://www.wired.com/story/openais-gpt-5-is-here/?utm_source=chatgpt.com "OpenAI Finally Launched GPT-5. Here's Everything You ..."