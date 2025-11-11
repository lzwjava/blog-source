---
audio: false
generated: true
lang: hi
layout: post
title: गिट ब्रांच विज़ुअलाइज़ेशन टूल्स
translated: true
type: note
---

Windows पर Git रिपॉजिटरी में कई ब्रांचों को विज़ुअलाइज़ करने के लिए, आप TortoiseGit या अन्य टूल्स का उपयोग करके चयनित ब्रांचों का ग्राफ़ दिखा सकते हैं। TortoiseGit का Revision Graph शक्तिशाली है, लेकिन सभी ब्रांचों को दिखाते समय यह अत्यधिक जटिल हो सकता है। नीचे TortoiseGit का उपयोग करके कई विशिष्ट ब्रांचों का ग्राफ़ देखने के चरण दिए गए हैं, साथ ही अधिक लचीलापन प्रदान करने वाले वैकल्पिक टूल्स भी दिए गए हैं।

### TortoiseGit का उपयोग करके कई ब्रांचें देखना
TortoiseGit का Revision Graph कई ब्रांचें दिखा सकता है, लेकिन यह इंटरफेस में सीधे विशिष्ट ब्रांचों को चुनने की अनुमति नहीं देता। हालाँकि, आप संबंधित ब्रांचों पर ध्यान केंद्रित करने के लिए दृश्य को फ़िल्टर कर सकते हैं।

1. **Revision Graph खोलें**:
   - Windows Explorer में अपनी रिपॉजिटरी फ़ोल्डर पर नेविगेट करें।
   - फ़ोल्डर पर राइट-क्लिक करें, **TortoiseGit** > **Revision Graph** चुनें।
   - यह डिफ़ॉल्ट रूप से सभी संदर्भों (ब्रांचों, टैग्स, आदि) का एक ग्राफ़ दिखाता है, जो अव्यवस्थित हो सकता है यदि आपके पास कई ब्रांचें हैं।[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-revgraph.html)

2. **विशिष्ट ब्रांचों को फ़िल्टर करें**:
   - Revision Graph विंडो में, अव्यवस्था कम करने के लिए **फ़िल्टर विकल्पों** का उपयोग करें:
     - **View** मेनू पर जाएं और **Show branchings and mergings** चुनें ताकि ब्रांच रिलेशनशिप पर ज़ोर दिया जा सके।[](https://stackoverflow.com/questions/67642974/tortoisegit-log-can-i-view-only-branch-and-merge-commits)
     - विशिष्ट ब्रांचों पर ध्यान केंद्रित करने के लिए, किसी कमिट पर राइट-क्लिक करें और **Show Log** चुनें ताकि लॉग डायलॉग देख सकें, जहाँ आप **View > Labels > Local branches** या **Remote branches** को टॉगल करके केवल प्रासंगिक संदर्भ दिखा सकते हैं।[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-showlog.html)
   - वैकल्पिक रूप से, ग्राफ़ को सरल बनाने के लिए लॉग डायलॉग में **Walk Behavior > Compressed Graph** विकल्प का उपयोग करें, जो केवल मर्ज पॉइंट्स और संदर्भों वाली कमिट्स (जैसे ब्रांच टिप्स) दिखाता है।[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-showlog.html)[](https://stackoverflow.com/questions/67642974/tortoisegit-log-can-i-view-only-branch-and-merge-commits)

3. **ग्राफ़ में नेविगेट करें**:
   - बड़े ग्राफ़ में नेविगेट करने के लिए **ओवरव्यू विंडो** का उपयोग करके हाइलाइट किए गए क्षेत्र को ड्रैग करें।[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-revgraph.html)
   - विवरण जैसे तारीख, लेखक और टिप्पणियाँ देखने के लिए किसी रिविज़न नोड पर होवर करें।[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-revgraph.html)
   - उनकी तुलना करने के लिए दो रिविज़न पर Ctrl-क्लिक करें और कॉन्टेक्स्ट मेनू (जैसे, **Compare Revisions**) का उपयोग करें।[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-revgraph.html)

4. **सीमाएँ**:
   - TortoiseGit का Revision Graph फ़िल्टर किए बिना सभी ब्रांचें दिखाता है, और ग्राफ़ दृश्य में केवल विशिष्ट ब्रांचों को चुनने का कोई सीधा विकल्प नहीं है।[](https://stackoverflow.com/questions/60244772/how-to-interpret-tortoise-git-revision-graph)
   - एक साफ़ दृश्य के लिए, नीचे दिए गए वैकल्पिक टूल्स पर विचार करें।

### कई ब्रांचें देखने के लिए वैकल्पिक टूल्स
यदि विशिष्ट ब्रांचों को चुनने के लिए TortoiseGit का इंटरफेस बहुत सीमित है, तो इन टूल्स को आज़माएं, जो ब्रांच विज़ुअलाइज़ेशन पर अधिक नियंत्रण प्रदान करते हैं:

#### 1. **Visual Studio Code with Git Graph Extension**
   - **इंस्टॉल करें**: Visual Studio Code डाउनलोड करें और **Git Graph** एक्सटेंशन इंस्टॉल करें।[](https://x.com/midudev/status/1797990974917927150)
   - **उपयोग**:
     - VS Code में अपनी रिपॉजिटरी खोलें।
     - सोर्स कंट्रोल टैब या कमांड पैलेट (`Ctrl+Shift+P` दबाएं, "Git Graph" टाइप करें) से Git Graph दृश्य तक पहुंचें।
     - इंटरफेस में ब्रांच नामों पर क्लिक करके ग्राफ़ में दिखाने के लिए विशिष्ट ब्रांचों का चयन करें।
     - ग्राफ़ स्पष्टता के लिए रंग-कोडित लाइनों के साथ कमिट्स, ब्रांचों और मर्जेस को दिखाता है।[](https://ardalis.com/git-graph-visualizes-branches-in-vs-code-for-free/)
   - **लाभ**: हल्का-फुल्का, मुफ्त, और इंटरैक्टिव रूप से कई ब्रांचों को चुनने की अनुमति देता है। कमिट्स की तुलना और बेसिक Git ऑपरेशन्स को सपोर्ट करता है।[](https://ardalis.com/git-graph-visualizes-branches-in-vs-code-for-free/)

#### 2. **SourceTree**
   - **इंस्टॉल करें**: Windows के लिए SourceTree (मुफ्त) डाउनलोड करें।[](https://stackoverflow.com/questions/12324050/how-can-i-visualize-github-branch-history-on-windows)[](https://stackoverflow.com/questions/12912985/git-visual-diff-between-branches)
   - **उपयोग**:
     - SourceTree में अपनी रिपॉजिटरी खोलें।
     - **History** दृश्य ब्रांचों और कमिट्स का ग्राफ़िकल प्रतिनिधित्व दिखाता है।
     - बाईं ओर ब्रांच सूची का उपयोग विशिष्ट ब्रांचों की दृश्यता को टॉगल करने के लिए करें, केवल उन्हीं पर ध्यान केंद्रित करें जिन्हें आप देखना चाहते हैं।
     - मर्जिंग या तुलना जैसी क्रियाओं के लिए ब्रांचों या कमिट्स पर राइट-क्लिक करें।[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)
   - **लाभ**: स्पष्ट ब्रांच विज़ुअलाइज़ेशन जिसमें सुसंगत रंग और इंटरैक्टिव फीचर्स जैसे ड्रैग-एंड-ड्रॉप मर्जिंग शामिल हैं।[](https://superuser.com/questions/699094/how-can-i-visualize-git-flow-branches)[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)

#### 3. **GitKraken**
   - **इंस्टॉल करें**: GitKraken डाउनलोड करें (ओपन-सोर्स प्रोजेक्ट्स के लिए मुफ्त, प्राइवेट रिपॉजिटरीज़ के लिए भुगतान आवश्यक)।[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)[](https://stackoverflow.com/questions/1838873/visualizing-branch-topology-in-git)
   - **उपयोग**:
     - GitKraken में अपनी रिपॉजिटरी खोलें।
     - केंद्रीय ग्राफ़ सभी ब्रांचों को दिखाता है, जिसमें ब्रांच सूची के माध्यम से विशिष्ट ब्रांचों को छिपाने/दिखाने के विकल्प शामिल होते हैं।
     - विशिष्ट ब्रांचों पर ध्यान केंद्रित करने के लिए ब्रांच लेबल पर क्लिक करें या कमिट्स को फ़िल्टर करने के लिए खोज का उपयोग करें।[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)
   - **लाभ**: सहज और दृष्टिगत रूप से आकर्षक, जिसमें सुसंगत ब्रांच रंग और उन्नत सुविधाएँ जैसे कंफ्लिक्ट रेजोल्यूशन शामिल हैं।[](https://superuser.com/questions/699094/how-can-i-visualize-git-flow-branches)[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)

#### 4. **Command Line with `git log`**
   - यदि आप टर्मिनल-आधारित समाधान पसंद करते हैं, तो Git के बिल्ट-इन ग्राफ़ दृश्य का उपयोग करें:
     ```bash
     git log --graph --oneline --decorate --branches=<branch1> --branches=<branch2>
     ```
     `<branch1>` और `<branch2>` को उन ब्रांचों के नामों से बदलें जिन्हें आप विज़ुअलाइज़ करना चाहते हैं (जैसे, `feature1`, `feature2`)। सभी ब्रांचों के लिए `--branches=*` का उपयोग करें या एक्सप्लिसिटली कई ब्रांचों को निर्दिष्ट करें।[](https://how-to.dev/how-to-display-git-branches-as-a-tree-in-cli)
   - **सुविधा के लिए Alias**:
     आसान पहुंच के लिए एक Git alias बनाएं:
     ```bash
     git config --global alias.tree "log --graph --oneline --decorate --branches="
     ```
     फिर केवल उन ब्रांचों का ग्राफ़ देखने के लिए `git tree feature1 feature2` चलाएं।[](https://how-to.dev/how-to-display-git-branches-as-a-tree-in-cli)
   - **लाभ**: किसी अतिरिक्त सॉफ़्टवेयर की आवश्यकता नहीं है, और आप सटीक ब्रांचों को निर्दिष्ट कर सकते हैं। आउटपुट टेक्स्ट-आधारित है लेकिन छोटी रिपॉजिटरीज़ के लिए स्पष्ट है।[](https://x.com/GWierzowiecki/status/1927657575048179899)

### सिफारिशें
- **सरलता और एकीकरण के लिए**: एक हल्के-फुल्के, मुफ्त समाधान के लिए **VS Code with Git Graph** का उपयोग करें जो आपको विशिष्ट ब्रांचों को चुनने देता है।[](https://x.com/midudev/status/1797990974917927150)
- **उन्नत विज़ुअलाइज़ेशन के लिए**: अधिक पॉलिश किए गए GUI के लिए **GitKraken** या **SourceTree** का उपयोग करें जिसमें इंटरैक्टिव ब्रांच चयन और सुसंगत रंग शामिल हों।[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)
- **TortoiseGit उपयोगकर्ताओं के लिए**: Revision Graph के साथ बने रहें और मुख्य ब्रांचों पर ध्यान केंद्रित करने के लिए **Compressed Graph** या **Show branchings and mergings** जैसे फ़िल्टर का उपयोग करें, लेकिन विशिष्ट ब्रांचों को चुनने में इसकी सीमाओं से अवगत रहें।[](https://stackoverflow.com/questions/67642974/tortoisegit-log-can-i-view-only-branch-and-merge-commits)
- **टर्मिनल उपयोगकर्ताओं के लिए**: अतिरिक्त टूल्स के बिना त्वरित, सटीक विज़ुअलाइज़ेशन के लिए विशिष्ट ब्रांच फ़िल्टर के साथ `git log` कमांड का उपयोग करें।[](https://how-to.dev/how-to-display-git-branches-as-a-tree-in-cli)

यदि आपके पास बड़ी संख्या में ब्रांचें हैं, तो GitKraken या SourceTree संभवतः केवल उन्हीं ब्रांचों को चुनिंदा रूप से विज़ुअलाइज़ करने के लिए सबसे अच्छे विकल्प हैं, जिनकी आपको परवाह है, क्योंकि वे सहज ब्रांच टॉगलिंग प्रदान करते हैं। यदि आपको इनमें से किसी भी टूल को सेट अप करने में सहायता या और स्पष्टीकरण की आवश्यकता हो तो मुझे बताएं!