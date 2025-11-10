---
audio: false
generated: true
image: false
lang: hi
layout: post
title: GitHub Copilot CLI एक्सटेंशन इंस्टॉल करें
translated: true
type: note
---

`gh extension install github/gh-copilot` कमांड GitHub CLI के लिए GitHub Copilot एक्सटेंशन इंस्टॉल करती है, जो कमांड-लाइन सुझाव और स्पष्टीकरण जैसी Copilot सुविधाएँ सक्षम करती है। एंटरप्राइज़ उपयोगकर्ताओं के लिए, यह कमांड लागू होती है या नहीं, यह विशिष्ट शर्तों पर निर्भर करता है:

- **एंटरप्राइज़ कॉन्फ़िगरेशन**: एंटरप्राइज़ उपयोगकर्ता Copilot CLI एक्सटेंशन का उपयोग तभी कर सकते हैं यदि उनकी संगठन या एंटरप्राइज़ के पास GitHub Copilot Business या Copilot Enterprise सब्सक्रिप्शन है और प्रशासकों द्वारा CLI सुविधा सक्षम की गई है। यदि संगठन मालिक या एंटरप्राइज़ प्रशासक ने CLI में Copilot अक्षम कर दिया है, तो एक्सटेंशन इंस्टॉल होने के बाद भी उपयोग नहीं किया जा सकता है।[](https://docs.github.com/fr/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)
- **प्रमाणीकरण**: एंटरप्राइज़ उपयोगकर्ताओं को GitHub CLI में एक ऐसे GitHub खाते से प्रमाणित होना होगा जिसे Copilot सीट आवंटित की गई हो। GitHub Enterprise Cloud (GHE.com) पर प्रबंधित उपयोगकर्ता खातों के लिए, साइन इन करने से पहले सेटिंग्स अपडेट करना जैसी अतिरिक्त सेटअप आवश्यकताएँ हो सकती हैं।[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-extension)
- **इंस्टॉलेशन आवश्यकताएँ**: कमांड चलाने से पहले GitHub CLI इंस्टॉल होना चाहिए। इंस्टॉलेशन प्रक्रिया स्वयं एंटरप्राइज़ और व्यक्तिगत उपयोगकर्ताओं के लिए समान है, लेकिन एंटरप्राइज़ नीतियाँ उपयोग को प्रतिबंधित कर सकती हैं।[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)

**एंटरप्राइज़ उपयोगकर्ताओं के लिए चरण**:
1. सुनिश्चित करें कि GitHub CLI इंस्टॉल है (निर्देशों के लिए [GitHub CLI रिपॉजिटरी](https://github.com/cli/cli) देखें)।
2. अपने एंटरप्राइज़ प्रशासक से पुष्टि करें कि आपके संगठन के लिए Copilot CLI सक्षम है।
3. अपने टर्मिनल में `gh extension install github/gh-copilot` चलाएँ।
4. अपने एंटरप्राइज़-आवंटित GitHub खाते का उपयोग करके `gh auth login` के साथ प्रमाणित हों।
5. यदि GHE.com पर एक प्रबंधित उपयोगकर्ता खाते का उपयोग कर रहे हैं, तो [GHE.com पर एक खाते के साथ GitHub Copilot का उपयोग करना](https://docs.github.com/en/enterprise-cloud@latest/copilot/configuring-github-copilot-in-your-environment/using-github-copilot-with-an-account-on-ghecom) में बताए गए अतिरिक्त सेटअप चरणों का पालन करें।[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-extension)

यदि आपकी एंटरप्राइज़ CLI एक्सेस को प्रतिबंधित करती है या उसने Copilot सक्षम नहीं किया है, तो एक्सटेंशन इंस्टॉल तो हो सकती है लेकिन कार्य नहीं करेगी। नीति विवरण के लिए अपने प्रशासक से जाँच करें।

[CLI में GitHub Copilot इंस्टॉल करना](https://docs.github.com/en/enterprise-cloud@latest/copilot/installing-github-copilot-in-the-cli)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)
[अपनी एंटरप्राइज़ के लिए GitHub Copilot सेट अप करना](https://docs.github.com/en/enterprise-cloud@latest/copilot/setting-up-github-copilot-for-your-enterprise)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/set-up-for-enterprise)