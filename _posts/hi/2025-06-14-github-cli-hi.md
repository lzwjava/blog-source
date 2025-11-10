---
audio: false
generated: true
lang: hi
layout: post
title: GitHub CLI इंस्टॉल करें
translated: true
type: note
---

Ubuntu पर GitHub CLI (`gh`) इंस्टॉल करने और `gh workflow run` कमांड के साथ GitHub Actions workflows को ट्रिगर करने के लिए, इन चरणों का पालन करें:

### Ubuntu पर GitHub CLI (`gh`) इंस्टॉलेशन चरण

1. **GitHub CLI repository और GPG key जोड़ें**:
   आधिकारिक GitHub CLI पैकेज रिपॉजिटरी को सेट अप करने के लिए अपने टर्मिनल में निम्नलिखित कमांड चलाएं:

   ```bash
   (type -p wget >/dev/null || (sudo apt update && sudo apt-get install wget -y)) \
   && sudo mkdir -p -m 755 /etc/apt/keyrings \
   && wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
   && sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
   && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
   ```

   यह स्क्रिप्ट:
   - `wget` इंस्टॉल करती है अगर पहले से मौजूद नहीं है।
   - APT keyrings के लिए एक डायरेक्टरी बनाती है।
   - GitHub CLI GPG key को डाउनलोड और एड करती है।
   - आपके सिस्टम के लिए GitHub CLI रिपॉजिटरी को कॉन्फ़िगर करती है।

2. **पैकेज इंडेक्स अपडेट करें और `gh` इंस्टॉल करें**:
   अपनी पैकेज लिस्ट को अपडेट करें और `gh` कमांड-लाइन टूल इंस्टॉल करें:

   ```bash
   sudo apt update
   sudo apt install gh -y
   ```

3. **इंस्टॉलेशन वेरिफाई करें**:
   यह चेक करने के लिए कि `gh` सही तरीके से इंस्टॉल हो गया है, यह कमांड चलाएं:

   ```bash
   gh --version
   ```

   आपको `gh version X.Y.Z (YYYY-MM-DD)` जैसा आउटपुट दिखना चाहिए, जो इंस्टॉलेशन की पुष्टि करता है।

4. **GitHub के साथ ऑथेंटिकेट करें**:
   `gh` का उपयोग करने से पहले, अपने GitHub अकाउंट के साथ ऑथेंटिकेट करें:

   ```bash
   gh auth login
   ```

   प्रॉम्प्ट का पालन करें:
   - `GitHub.com` चुनें (या आपके एंटरप्राइज़ सर्वर के लिए यदि लागू हो)।
   - अपने पसंदीदा प्रोटोकॉल का चयन करें (`HTTPS` या `SSH`; `SSH` की सिफारिश की जाती है अगर आपने SSH key सेट अप की है)।
   - ऑथेंटिकेशन विधि चुनें (ब्राउज़र सबसे आसान है; यह लॉग इन करने के लिए एक वेबपेज खोलता है)।
   - प्रदान किए गए वन-टाइम कोड को कॉपी करें, इसे ब्राउज़र में पेस्ट करें, और `gh` को अथॉराइज़ करें।
   - डिफ़ॉल्ट सेटिंग्स की पुष्टि करें या आवश्यकतानुसार एडजस्ट करें।

   सफल ऑथेंटिकेशन के बाद, आपको एक कन्फर्मेशन मैसेज दिखेगा।

### GitHub Actions के लिए `gh workflow run` का उपयोग

`gh workflow run` कमांड एक GitHub Actions workflow को ट्रिगर करता है। यहां बताया गया है कि इसका उपयोग कैसे करें:

1. **अपने रिपॉजिटरी में नेविगेट करें** (वैकल्पिक):
   यदि आप GitHub से लिंक्ड लोकल Git रिपॉजिटरी में हैं, तो `gh` इसे स्वचालित रूप से डिटेक्ट कर लेगा। अन्यथा, `--repo` फ्लैग के साथ रिपॉजिटरी निर्दिष्ट करें।

2. **उपलब्ध workflows की सूची बनाएं** (वैकल्पिक):
   workflow ID या filename खोजने के लिए, यह कमांड चलाएं:

   ```bash
   gh workflow list
   ```

   यह रिपॉजिटरी में सभी workflows को दिखाता है, उनके नाम, IDs, और स्टेटस (जैसे `active`) दिखाते हुए।

3. **एक workflow चलाएं**:
   workflow के filename या ID के साथ `gh workflow run` कमांड का उपयोग करें। उदाहरण के लिए:

   ```bash
   gh workflow run workflow.yml
   ```

   या, workflow ID (जैसे `123456`) का उपयोग करके:

   ```bash
   gh workflow run 123456
   ```

   यदि workflow इनपुट स्वीकार करती है, तो उन्हें `--field` फ्लैग के साथ प्रदान करें:

   ```bash
   gh workflow run workflow.yml --field key=value
   ```

   एक ब्रांच या ref निर्दिष्ट करने के लिए, `--ref` फ्लैग का उपयोग करें:

   ```bash
   gh workflow run workflow.yml --ref branch-name
   ```

4. **Workflow की निगरानी करें**:
   ट्रिगर करने के बाद, रन की स्थिति की जांच करें:

   ```bash
   gh run list
   ```

   रियल-टाइम में किसी विशिष्ट रन को देखने के लिए, उपयोग करें:

   ```bash
   gh run watch <run-id>
   ```

   `<run-id>` को `gh run list` से प्राप्त रन ID से बदलें।

### समस्या निवारण युक्तियाँ

- **GPG सिग्नेचर एरर**: यदि `apt update` के दौरान आपको GPG-संबंधित समस्याएं आती हैं, तो फिक्स के लिए GitHub के issue tracker (जैसे `cli/cli#9569`) देखें या key import स्टेप को दोबारा करें।[](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- **फ़ायरवॉल समस्याएं**: यदि `keyserver.ubuntu.com` फेल हो जाता है, तो यह कोशिश करें:

   ```bash
   sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key C99B11DEB97541F0
   ```

   या अगर जरूरत हो तो `dirmngr` इंस्टॉल करें:

   ```bash
   sudo apt-get install dirmngr
   ```

  [](https://gist.github.com/Manoj-Paramsetti/dc957bdd6a4430275d0fc28a0dc43ae9)
- **Snap इंस्टॉलेशन चेतावनी**: रनटाइम समस्याओं के कारण GitHub `gh` के लिए Snap पैकेज का उपयोग करने से हतोत्साहित करता है। उपरोक्त APT विधि का पालन करें।[](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- **ऑथेंटिकेशन स्कोप**: यदि `gh workflow run` परमिशन के कारण फेल हो जाता है, तो सुनिश्चित करें कि आपके टोकन में `workflow` स्कोप है। इसके साथ दोबारा ऑथेंटिकेट करें:

   ```bash
   gh auth refresh -s workflow
   ```

### अतिरिक्त नोट्स

- **GitHub CLI मैन्युअल**: `gh` कमांड्स के अधिक विवरण के लिए, `gh help` चलाएं या आधिकारिक मैन्युअल पर जाएं [cli.github.com](https://cli.github.com)।[](https://cli.github.com/manual/)
- **Workflow आवश्यकताएँ**: सुनिश्चित करें कि workflow फ़ाइल (जैसे `workflow.yml`) आपकी रिपॉजिटरी की `.github/workflows/` डायरेक्टरी में मौजूद है और मैनुअल ट्रिगर्स (जैसे `workflow_dispatch` इवेंट) के लिए कॉन्फ़िगर की गई है।
- **वैकल्पिक इंस्टॉलेशन विधियाँ**: आप `gh` को Homebrew (`brew install gh`) के माध्यम से या [रिलीज़ पेज](https://github.com/cli/cli/releases) से बाइनरीज़ डाउनलोड करके भी इंस्टॉल कर सकते हैं, लेकिन Ubuntu के लिए APT विधि की सिफारिश की जाती है।[](https://github.com/cli/cli)

यह सेटअप आपको Ubuntu पर कमांड लाइन से GitHub Actions workflows को कुशलतापूर्वक प्रबंधित करने की अनुमति देता है। यदि आपको विशिष्ट `gh` कमांड्स या workflow कॉन्फ़िगरेशन में सहायता की आवश्यकता है तो मुझे बताएं!