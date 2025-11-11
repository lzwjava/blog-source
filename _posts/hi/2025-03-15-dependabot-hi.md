---
audio: false
generated: true
lang: hi
layout: post
title: डिपेंडाबॉट हटाना
translated: true
type: note
---

GitHub Actions से Dependabot को हटाने के लिए, आपको उसकी pull request बनाने की क्षमता को अक्षम करना होगा जो workflows को ट्रिगर करती हैं, और वैकल्पिक रूप से, Dependabot से जुड़े किसी भी कस्टम workflow को हटाना होगा। इसके लिए नीचे दिए गए चरणों का पालन करें। ध्यान दें कि मैं मान रहा हूं कि आपके प्रश्न में "dependant bot" से तात्पर्य "Dependabot" से है, जो GitHub में dependency management के लिए एक सामान्य टूल है।

---

### चरण 1: Dependabot Version Updates को अक्षम करें
Dependabot version updates आपकी dependencies को अप-टू-डेट रखने के लिए स्वचालित रूप से pull request बनाता है। ये pull request GitHub Actions workflows को ट्रिगर कर सकती हैं। इस सुविधा को अक्षम करने के लिए:

- **कॉन्फ़िगरेशन फ़ाइल ढूंढें**: अपने repository में `.github` डायरेक्टरी में `dependabot.yml` नाम की फ़ाइल की जांच करें।
- **फ़ाइल हटाएं**: यदि यह फ़ाइल मौजूद है, तो इसे डिलीट कर दें और इस बदलाव को कमिट करें। इससे Dependabot द्वारा version updates के लिए pull request बनाना बंद हो जाएगा।
- **सत्यापित करें**: यदि कोई `dependabot.yml` फ़ाइल मौजूद नहीं है, तो version updates पहले से ही अक्षम हैं।

---

### चरण 2: Dependabot Security Updates को अक्षम करें
Dependabot security updates आपकी dependencies में vulnerabilities को ठीक करने के लिए pull request जनरेट करता है, जो GitHub Actions workflows को भी ट्रिगर कर सकता है। इसे बंद करने के लिए:

- **Repository Settings पर जाएं**: अपने GitHub repository में, **Settings** टैब पर क्लिक करें।
- **Security Settings पर नेविगेट करें**: **Security & analysis** (या आपके GitHub इंटरफेस के आधार पर **Code security and analysis**) तक स्क्रॉल करें।
- **Security Updates अक्षम करें**: **Dependabot security updates** ढूंढें और **Disable** पर क्लिक करें।

इससे Dependabot द्वारा security fixes के लिए pull request बनाना बंद हो जाएगा।

---

### चरण 3: (वैकल्पिक) कस्टम Dependabot-संबंधित Workflows को हटाएं
यदि आपने विशेष रूप से Dependabot pull requests को हैंडल करने के लिए GitHub Actions workflows सेटअप किए हैं (जैसे ऑटो-मर्जिंग, लेबलिंग, या Dependabot metadata का उपयोग), तो आप उन्हें साफ करना चाह सकते हैं:

- **Workflow फ़ाइलें जांचें**: `.github/workflows` डायरेक्टरी में YAML फ़ाइलों को देखें।
- **Dependabot लॉजिक पहचानें**: शर्तों जैसे `if: github.event.pull_request.user.login == 'dependabot[bot]'` या एक्शन जैसे `dependabot/fetch-metadata` के लिए खोजें।
- **हटाएं या संशोधित करें**: इन workflows को डिलीट कर दें या Dependabot-विशिष्ट लॉजिक को हटाने के लिए उन्हें एडजस्ट करें, फिर बदलावों को कमिट करें।

यह चरण वैकल्पिक है क्योंकि चरण 1 और 2 में Dependabot को अक्षम करने से यह नई pull request बनाना बंद कर देगा, जिसका मतलब है कि मौजूदा workflows अब Dependabot द्वारा ट्रिगर नहीं होंगे। हालांकि, इन workflows को हटाने से एक पूर्ण सफाई सुनिश्चित होती है।

---

### अतिरिक्त नोट्स
- **मौजूदा Pull Requests**: Dependabot को अक्षम करने से इसके द्वारा बनाई गई मौजूदा pull requests स्वतः बंद नहीं होतीं। यदि इन्हें अपडेट किया जाता है तो ये अभी भी workflows को ट्रिगर कर सकती हैं। आवश्यकता पड़ने पर आप उन्हें मैन्युअली बंद कर सकते हैं।
- **Dependabot Alerts**: यदि आप vulnerability नोटिफिकेशन (जो सीधे GitHub Actions से नहीं जुड़े हैं) को भी रोकना चाहते हैं, तो **Settings > Security & analysis** पर जाएं और **Dependabot alerts** को अक्षम करें। यह वैकल्पिक है और workflow triggers से असंबंधित है।

---

### परिणाम
चरण 1 और 2 को पूरा करके, Dependabot अब आपके repository में pull request नहीं बनाएगा, जिससे GitHub Actions पर इसका प्रभाव प्रभावी रूप से "हट" जाएगा। यदि आपने Dependabot के लिए workflows को कस्टमाइज़ किया है, तो चरण 3 यह सुनिश्चित करता है कि संबंधित सभी ऑटोमेशन हट जाएं। अब आपका GitHub Actions केवल अन्य इवेंट्स के आधार पर चलेगा, Dependabot से अप्रभावित।