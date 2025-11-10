---
audio: false
generated: true
image: false
lang: hi
layout: post
title: GitHub Copilot CLI एकीकरण
translated: true
type: note
---

आप `code --plugin copilot "hi"` जैसे सिंटैक्स का उपयोग करके कमांड लाइन से सीधे GitHub Copilot को प्लगइन के रूप में इनवोक नहीं कर सकते हैं ताकि प्रतिक्रिया प्राप्त हो सके। हालाँकि, GitHub Copilot, GitHub CLI के माध्यम से `gh copilot` एक्सटेंशन के साथ कमांड-लाइन इंटीग्रेशन प्रदान करता है, जो कमांड सुझावों और स्पष्टीकरणों के लिए एक चैट जैसा इंटरफेस प्रदान करता है। यह `code` कमांड के माध्यम से इनवोक किए गए जेनेरिक प्लगइन के समान नहीं है, लेकिन यह कमांड-लाइन इंटरैक्शन के लिए एक समान उद्देश्य पूरा करता है।

### CLI में GitHub Copilot के विवरण
- **आवश्यकताएँ**: आपके पास एक GitHub Copilot सब्सक्रिप्शन, इंस्टॉल किया हुआ GitHub CLI (`gh`), और इंस्टॉल किया हुआ `gh-copilot` एक्सटेंशन होना चाहिए। सेटअप के निर्देश GitHub CLI रिपॉजिटरी या डॉक्यूमेंटेशन में उपलब्ध हैं [GitHub CLI Installation](https://cli.github.com/) और [Installing GitHub Copilot in the CLI](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line).
- **उपयोग**: एक बार सेटअप हो जाने के बाद, आप निम्नलिखित कमांड्स का उपयोग कर सकते हैं:
  - `gh copilot suggest -t shell "hi"` एक शेल कमांड सुझाव प्राप्त करने के लिए।
  - `gh copilot explain "hi"` किसी कमांड की व्याख्या प्राप्त करने के लिए।
  - उदाहरण: `gh copilot suggest -t shell "say hello"` चलाने से संदर्भ के आधार पर `echo "hello"` या macOS पर `say "hello"` जैसा टेक्स्ट-टू-स्पीच कमांड सुझाया जा सकता है।
- **सीमाएँ**: CLI इंटरफेस कमांड-लाइन से संबंधित कार्यों (जैसे, शेल, Git, या GitHub CLI कमांड्स) के लिए डिज़ाइन किया गया है और यह चैटबॉट की तरह सामान्य वार्तालाप प्रतिक्रियाओं का समर्थन नहीं करता है। यह केवल अंग्रेजी प्रॉम्प्ट्स का समर्थन करता है [Responsible use of GitHub Copilot in the CLI](https://docs.github.com/en/copilot/using-github-copilot/responsible-use-of-github-copilot-in-the-cli).[](https://docs.github.com/en/copilot/responsible-use/copilot-in-the-cli)[](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-in-the-cli)
- **इंटरैक्टिव मोड**: एक `suggest` कमांड चलाने के बाद, Copilot एक इंटरैक्टिव सेशन शुरू करता है जहाँ आप सुझाव को परिष्कृत कर सकते हैं, उसे एक्ज़िक्यूट कर सकते हैं (क्लिपबोर्ड पर कॉपी होता है), या उसका रेटिंग दे सकते हैं। स्वचालित एक्ज़िक्यूशन के लिए, आपको `ghcs` एलियास सेट अप करना होगा [Using GitHub Copilot in the command line](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line).[](https://docs.github.com/en/copilot/how-tos/use-copilot-for-common-tasks/use-copilot-in-the-cli)[](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)

### `code --plugin copilot "hi"` क्यों काम नहीं करता
- **Visual Studio Code CLI**: `code` कमांड (VS Code के लिए) `--install-extension` जैसे विकल्पों का समर्थन करता है, लेकिन इसमें `--plugin` फ्लैग नहीं है जो `"hi"` जैसे इनपुट के साथ सीधे एक्सटेंशन्स को इनवोक कर सके। GitHub Copilot जैसे एक्सटेंशन आमतौर पर VS Code एडिटर के भीतर काम करते हैं, जो इनलाइन सुझाव या चैट इंटरफेस प्रदान करते हैं, स्टैंडअलोन CLI टूल्स के रूप में नहीं [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview).[](https://code.visualstudio.com/docs/copilot/overview)
- **Copilot की आर्किटेक्चर**: GitHub Copilot का VS Code के लिए प्लगइन कोड कम्प्लीशन और चैट के लिए एक लैंग्वेज सर्वर और GitHub के बैकएंड के साथ संचार करता है। कमांड लाइन से सीधे `"hi"` जैसे मनमाने स्ट्रिंग्स को प्लगइन तक पहुँचाने और प्रतिक्रिया प्राप्त करने के लिए कोई सार्वजनिक API या CLI मैकेनिज्म नहीं है [How to invoke Github Copilot programmatically?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically).[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
- **जेनेरिक इनपुट के लिए विकल्प**: यदि आप Copilot को `"hi"` जैसा प्रॉम्प्ट भेजकर प्रतिक्रिया प्राप्त करना चाहते हैं, तो आपको VS Code या किसी अन्य समर्थित IDE के भीतर Copilot Chat का उपयोग करना होगा, या अन्य AI CLI टूल्स का पता लगाना होगा जो वार्तालाप प्रॉम्प्ट्स का समर्थन करते हैं (जैसे, Microsoft का AI Shell for Azure CLI) [Use Microsoft Copilot in Azure with AI Shell](https://learn.microsoft.com/en-us/azure/copilot/use-copilot-cli).[](https://learn.microsoft.com/en-us/azure/copilot/ai-shell-overview)

### आपके लक्ष्य के लिए वर्कअराउंड
यदि आपका लक्ष्य `"hi"` जैसे प्रॉम्प्ट के साथ कमांड लाइन से Copilot जैसे AI असिस्टेंट को इनवोक करना और प्रतिक्रिया प्राप्त करना है, तो आप यह कर सकते हैं:
1. **कमांड-लाइन कार्यों के लिए `gh copilot` का उपयोग करें**:
   - GitHub CLI और Copilot एक्सटेंशन इंस्टॉल करें।
   - `echo "hi"` जैसा कमांड प्राप्त करने के लिए `gh copilot suggest -t shell "greet with hi"` चलाएँ।
   - यह कमांड-लाइन संदर्भों तक सीमित है, इसलिए केवल `"hi"` का कोई सार्थक प्रतिक्रिया नहीं दे सकता जब तक कि इसे कमांड अनुरोध के रूप में फ्रेम न किया गया हो।
2. **VS Code के Copilot Chat का उपयोग करें**:
   - VS Code खोलें, Copilot Chat इंटरफेस का उपयोग करें (`⌃⌘I` या चैट आइकन के माध्यम से एक्सेस करें), और वार्तालाप प्रतिक्रिया प्राप्त करने के लिए `"hi"` टाइप करें।
   - इसके लिए एडिटर के भीतर मैन्युअल इंटरैक्शन की आवश्यकता होती है, CLI इनवोकेशन की नहीं [GitHub Copilot in VS Code cheat sheet](https://code.visualstudio.com/docs/copilot/copilot-cheat-sheet).[](https://code.visualstudio.com/docs/copilot/reference/copilot-vscode-features)
3. **अन्य AI CLI टूल्स का पता लगाएँ**:
   - **AI Shell**: Microsoft का AI Shell, Azure-संबंधित कार्यों के लिए CLI में प्राकृतिक-भाषा प्रॉम्प्ट्स की अनुमति देता है। आप इसे इंस्टॉल कर सकते हैं और `"hi"` जैसे प्रॉम्प्ट्स आज़मा सकते हैं, हालाँकि यह Azure CLI और PowerShell कमांड्स के लिए ऑप्टिमाइज़्ड है [Use Microsoft Copilot in Azure with AI Shell](https://learn.microsoft.com/en-us/azure/copilot/use-copilot-cli).[](https://learn.microsoft.com/en-us/azure/copilot/ai-shell-overview)
   - **कस्टम स्क्रिप्ट्स**: आप `"hi"` जैसे प्रॉम्प्ट्स को प्रोसेस करने के लिए किसी AI मॉडल के API (जैसे, OpenAI का API, यदि एक्सेसिबल हो) के साथ इंटरैक्ट करने के लिए एक स्क्रिप्ट लिख सकते हैं। हालाँकि, GitHub Copilot का API ऐसे उपयोग के लिए सार्वजनिक रूप से उपलब्ध नहीं है [How to invoke Github Copilot programmatically?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically).[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
4. **प्लगइन व्यवहार का अनुकरण करें**:
   - एक शेल स्क्रिप्ट या एलियास बनाएं जो इनपुट को `gh copilot suggest` या किसी अन्य AI CLI टूल में पाइप करे।
   - उदाहरण:
     ```bash
     alias ai='gh copilot suggest -t shell'
     ai "greet with hi"
     ```
     यह `echo "hi"` या इसी तरह का कमांड सुझाएगा।

### प्रोग्रामेटिक इनवोकेशन
यदि आप प्रोग्रामेटिक रूप से Copilot जैसी कार्यक्षमता को इनवोक करना चाह रहे हैं (जैसा कि आपके उदाहरण से संकेत मिलता है), तो ध्यान दें कि:
- GitHub Copilot सीधे प्रोग्रामेटिक एक्सेस के लिए कोई सार्वजनिक API एक्सपोज़ नहीं करता है। कुछ सामुदायिक प्रयासों ने सुझावों को कैप्चर करने के लिए लैंग्वेज सर्वर को रिवर्स-इंजीनियर किया है या प्रॉक्सी का उपयोग किया है, लेकिन ये जटिल और जोखिम भरे हैं (जैसे, अकाउंट बैन की संभावना) [How to invoke Github Copilot programmatically?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically).[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
- आप ओपन-सोर्स विकल्पों या CLI इंटीग्रेशन वाले अन्य AI मॉडल्स (जैसे, Hugging Face के CLI टूल्स या LLaMA जैसे स्थानीय LLMs के साथ कस्टम रैपर्स) का पता लगा सकते हैं।

### निष्कर्ष
जबकि `code --plugin copilot "hi"` समर्थित नहीं है, आप कमांड-लाइन कार्यों के लिए `gh copilot` का उपयोग करके या वार्तालाप प्रॉम्प्ट्स के लिए VS Code में Copilot Chat का उपयोग करके समान कार्यक्षमता प्राप्त कर सकते हैं। एक जेनेरिक CLI AI अनुभव के लिए, AI Shell जैसे टूल्स या अन्य AI APIs के साथ कस्टम स्क्रिप्ट्स पर विचार करें। सुझावों को हमेशा सत्यापित करें, क्योंकि Copilot की CLI प्रतिक्रियाओं में ट्रेनिंग डेटा से त्रुटियाँ या पूर्वाग्रह हो सकते हैं [Responsible use of GitHub Copilot in the CLI](https://docs.github.com/en/copilot/using-github-copilot/responsible-use-of-github-copilot-in-the-cli).[](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-in-the-cli)

यदि आपके पास कोई विशिष्ट उपयोग मामला है (जैसे, वार्तालाप AI बनाम कमांड जनरेशन), तो मुझे बताएं, और मैं समाधान को और अधिक अनुकूलित कर सकता हूँ!