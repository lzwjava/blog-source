---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: कॉपायलट एंटरप्राइज़ मॉडल विकल्प अवलोकन
translated: true
type: note
---

आप **Copilot Enterprise** के लिए किस मॉडल का उपयोग किया जा सकता है, यह पूछ रहे हैं, विशेष रूप से क्या यह GPT-4.1, GPT-4o, या कुछ और है। **सितंबर 2025** तक यहाँ वर्तमान और प्रासंगिक जानकारी दी गई है:

---

### Copilot Enterprise के लिए कौन से मॉडल उपलब्ध हैं?

#### GitHub Copilot Enterprise और Copilot Chat

* **डिफ़ॉल्ट रूप से**, GitHub Copilot Enterprise (और Copilot Chat) **GPT-4o पर चलता है**, जो तेज़ प्रतिक्रिया और बेहतर गुणवत्ता प्रदान करता है। ([Reddit][1])
* हाल ही में, **GPT-4.1** उपलब्ध हुआ है—लेकिन व्यवस्थापकों को Copilot सेटिंग्स में **पॉलिसी के माध्यम से इसे स्पष्ट रूप से सक्षम** करना होगा। एक बार सक्षम होने के बाद, उपयोगकर्ता VS Code और github.com दोनों पर मॉडल सेलेक्टर से GPT-4.1 चुन सकते हैं। ([The GitHub Blog][2])

#### Visual Studio Copilot

* **जून 2025** तक, Visual Studio के Copilot ने अब **अपने डिफ़ॉल्ट मॉडल के रूप में GPT-4.1 का उपयोग** करना शुरू कर दिया है, GPT-4o के बजाय। Microsoft के परीक्षणों से पता चला कि GPT-4.1 **तेज़ प्रतिक्रिया, उच्च-गुणवत्ता वाले सुझाव और अधिक दक्षता** प्रदान करता है। ([Visual Studio Magazine][3], [Microsoft Learn][4])

#### Microsoft 365 Copilot (Office Productivity Tools)

* Microsoft ने **GPT-5** को व्यापक Copilot इकोसिस्टम—जिसमें Microsoft 365 Copilot, GitHub Copilot, Copilot Studio, और अन्य शामिल हैं—में एक नए "**स्मार्ट मोड**" के माध्यम से एकीकृत करना शुरू कर दिया है, जो आवश्यकता के आधार पर कार्यों को सबसे उपयुक्त मॉडल पर स्वचालित रूप से रूट करता है, जिससे तर्क, संदर्भ प्रतिधारण और इंटरैक्शन की गुणवत्ता में सुधार होता है। ([The Verge][5])
* इसके अतिरिक्त, Microsoft ने प्रस्तुति डिज़ाइन और स्प्रेडशीट ऑटोमेशन जैसे उन्नत कार्यों के लिए Anthropic के **Claude Sonnet 4** के एकीकरण की घोषणा की, जबकि अन्य कार्यों के लिए **GPT-5** (शेष GPT-आधारित रूट्स के साथ) का उपयोग जारी रखा। ([New York Post][6])

---

### सारांश — **Copilot Enterprise** के लिए कौन सा मॉडल सही है?

* **GitHub Copilot Enterprise / Copilot Chat**:

  * डिफ़ॉल्ट: **GPT-4o**
  * वैकल्पिक: **GPT-4.1** (यदि व्यवस्थापक द्वारा सक्षम किया गया हो)
* **Visual Studio Copilot**: डिफ़ॉल्ट अब **GPT-4.1** है
* **Microsoft 365 Copilot**: **GPT-5 स्मार्ट मोड** का लाभ उठा रहा है, जिसमें उच्च-प्रदर्शन रूटिंग और क्षमताएं शामिल हैं—और चुनिंदा एंटरप्राइज़ कार्यों के लिए **Claude Sonnet 4** को भी एकीकृत किया गया है।

---

### त्वरित अवलोकन (आपकी प्राथमिकता के अनुसार, चौड़ी तालिकाओं के बिना):

* **GPT-4o**: GitHub Copilot Enterprise में डिफ़ॉल्ट; एंटरप्राइज़ चैट में गति और गुणवत्ता के लिए जाना जाता है।
* **GPT-4.1**: अधिक शक्तिशाली उत्तराधिकारी—कोड, निर्देशों का पालन और लंबे संदर्भों में बेहतर। GitHub Copilot में उपलब्ध यदि सक्षम किया गया हो, और अब Visual Studio Copilot में डिफ़ॉल्ट है। ([OpenAI][7])
* **GPT-5**: नवीनतम मॉडल, अधिक स्मार्ट मॉडल चयन के लिए सभी Copilot प्लेटफ़ॉर्म में स्मार्ट मोड के माध्यम से M365 Copilot में एकीकृत। ([The Verge][5])
* **Claude Sonnet 4**: मुख्य रूप से PowerPoint और Excel ऑटोमेशन जैसे Office कार्यों के लिए GPT-5 के साथ जोड़ा गया। ([New York Post][6])

---

### आगे क्या करें?

* यदि आप GitHub Copilot Enterprise का प्रबंधन करने वाले **व्यवस्थापक** हैं, तो अपनी सेटिंग्स जांचें ताकि **GPT-4.1 को सक्षम** किया जा सके यदि आप चाहते हैं कि उपयोगकर्ता इसके प्रदर्शन सुधारों का लाभ उठाएं।
* यदि आप **Visual Studio Copilot** का उपयोग कर रहे हैं, तो आप पहले से ही **GPT-4.1** पर डिफ़ॉल्ट रूप से हैं।
* **Microsoft 365 Copilot** के लिए, आपको **GPT-5 स्मार्ट मोड** रोलआउट और **Claude Sonnet 4** एकीकरण का लाभ मिलेगा। किसी कार्रवाई की आवश्यकता नहीं है—यह पहले से ही सेवा परतों का हिस्सा है।

यदि आप इन सेटिंग्स को कॉन्फ़िगर करने या अपने संगठन के विशिष्ट वातावरण में मॉडल विकल्पों को नेविगेट करने में सहायता चाहते हैं, तो मुझे बताएं!

[1]: https://www.reddit.com/r/GithubCopilot/comments/1dx2iq1/github_copilot_enterprise_on_gpt4o/?utm_source=chatgpt.com "GitHub Copilot Enterprise on GPT-4o : r/GithubCopilot"
[2]: https://github.blog/changelog/2025-04-14-openai-gpt-4-1-now-available-in-public-preview-for-github-copilot-and-github-models/?utm_source=chatgpt.com "OpenAI GPT-4.1 now available in public preview for GitHub ..."
[3]: https://visualstudiomagazine.com/articles/2025/06/26/new-default-model-for-visual-studio-copilot-so-how-do-you-choose.aspx?utm_source=chatgpt.com "New Default Model for Visual Studio Copilot, So How Do ..."
[4]: https://learn.microsoft.com/en-us/visualstudio/ide/copilot-select-add-models?view=vs-2022&utm_source=chatgpt.com "Using AI models in Copilot Chat - Visual Studio (Windows)"
[5]: https://www.theverge.com/news/753984/microsoft-copilot-gpt-5-model-update?utm_source=chatgpt.com "Microsoft brings GPT-5 to Copilot with new smart mode"
[6]: https://nypost.com/2025/09/10/business/microsoft-to-add-anthropic-ai-models-as-rift-with-openai-grows-report/?utm_source=chatgpt.com "Microsoft to add Anthropic AI models - as rift with OpenAI grows: report"
[7]: https://openai.com/index/gpt-4-1/?utm_source=chatgpt.com "Introducing GPT-4.1 in the API"