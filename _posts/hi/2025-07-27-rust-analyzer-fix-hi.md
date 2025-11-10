---
audio: false
generated: true
image: false
lang: hi
layout: post
title: रस्ट एनालाइज़र वर्कस्पेस समस्या
translated: true
type: note
---

आपको दिख रहे त्रुटि संदेश बताते हैं कि rust-analyzer (Rust लैंग्वेज सर्वर) निर्दिष्ट डायरेक्टरी `/Users/lzwjava/projects/lzwjava.github.io` में एक वैध Rust workspace का पता लगाने में असमर्थ है। यह आमतौर पर तब होता है जब फ़ोल्डर की जड़ में एक `Cargo.toml` फ़ाइल (या अन्य Rust प्रोजेक्ट मार्कर) की कमी होती है, या rust-analyzer सही जगह देखने के लिए कॉन्फ़िगर नहीं है। Rust-analyzer उम्मीद करता है कि खुले workspace में कम से कम एक Rust प्रोजेक्ट मिलेगा; अगर ऐसा नहीं होता है, तो यह लोड होने में विफल रहता है।

यह डायरेक्टरी नाम (`lzwjava.github.io`) संकेत देता है कि यह एक GitHub Pages साइट हो सकती है (जैसे, स्टैटिक ब्लॉग या वेबसाइट के लिए), जो आमतौर पर एक Rust प्रोजेक्ट नहीं है, जब तक कि आप Rust-आधारित टूल जैसे कस्टम स्टैटिक साइट जनरेटर का उपयोग नहीं कर रहे हैं। यदि यह Rust workspace नहीं है, तो rust-analyzer अनावश्यक रूप से सक्रिय हो सकता है (जैसे, आपके एडिटर में ग्लोबल एक्सटेंशन सेटिंग के कारण)।

यह मानते हुए कि आप VS Code का उपयोग कर रहे हैं (इस मुद्दे के लिए सबसे आम एडिटर; यदि नहीं, तो नीचे नोट देखें), इसे ठीक करने के चरण यहां दिए गए हैं:

### 1. **सही Workspace फ़ोल्डर सत्यापित करें और खोलें**
   - सुनिश्चित करें कि आप उस फ़ोल्डर को खोल रहे हैं जिसमें आपके Rust प्रोजेक्ट की `Cargo.toml` फ़ाइल VS Code workspace की जड़ के रूप में है।
   - यदि आपका प्रोजेक्ट एक सबडायरेक्टरी में है (जैसे, `/Users/lzwjava/projects/lzwjava.github.io/my-rust-app`), तो उस सबफ़ोल्डर को **File > Open Folder** के माध्यम से खोलें।
   - workspace बदलने के बाद VS Code को पुनरारंभ करें।

### 2. **rust-analyzer सेटिंग्स में Linked Projects कॉन्फ़िगर करें**
   - यदि `Cargo.toml` मौजूद है लेकिन workspace की जड़ पर नहीं है (जैसे, किसी सबफ़ोल्डर में), तो rust-analyzer को बताएं कि उसे कहां ढूंढना है:
     - VS Code सेटिंग्स खोलें (**Code > Preferences > Settings** या Mac पर Cmd+,)।
     - "rust-analyzer" खोजें।
     - **Rust-analyzer > Server: Extra Env** के अंतर्गत या सीधे एक्सटेंशन सेटिंग्स में, **Linked Projects** ढूंढें।
     - इसे एक ऐरे पर सेट करें जो आपके `Cargo.toml` पथ(पथों) की ओर इशारा करता हो। उदाहरण के लिए, इसे अपने workspace के `settings.json` में जोड़ें (**Preferences: Open Workspace Settings (JSON)** के माध्यम से):
       ```
       {
         "rust-analyzer.linkedProjects": [
           "./path/to/your/Cargo.toml"
         ]
       }
       ```
       `./path/to/your/Cargo.toml` को अपने workspace जड़ से रिलेटिव पथ से बदलें।
     - विंडो को सेव करें और रीलोड करें (कमांड पैलेट के माध्यम से **Developer: Reload Window**, Cmd+Shift+P)।

### 3. **यदि यह Rust प्रोजेक्ट नहीं है**
   - इस workspace के लिए rust-analyzer को अक्षम करें:
     - एक्सटेंशन्स व्यू पर जाएं (Cmd+Shift+X)।
     - "rust-analyzer" ढूंढें > गियर आइकन पर क्लिक करें > **Disable (Workspace)**।
   - वैकल्पिक रूप से, यदि आपको इसकी बिल्कुल आवश्यकता नहीं है, तो एक्सटेंशन को अनइंस्टॉल कर दें।

### 4. **अन्य समस्या निवारण**
   - **rust-analyzer और Rustup को पुनः इंस्टॉल करें**: कभी-कभी दूषित इंस्टॉलेशन समस्याएं पैदा करते हैं। अपने टर्मिनल में `rustup self uninstall` और फिर `rustup self update` चलाएं, और VS Code एक्सटेंशन को पुनः इंस्टॉल करें।
   - **मल्टीपल वर्कस्पेस के लिए जांचें**: यदि आपके पास मल्टी-रूट workspace है, तो सुनिश्चित करें कि प्रत्येक जड़ का अपना वैध कॉन्फ़िगरेशन है।
   - **सब कुछ अपडेट करें**: सुनिश्चित करें कि VS Code, rust-analyzer एक्सटेंशन, और Rust टूलचेन (`rustup update`) अप-टू-डेट हैं।
   - **अधिक जानकारी के लिए लॉग देखें**: अतिरिक्त सुरागों के लिए VS Code में rust-analyzer का आउटपुट चेक करें (**View > Output**, ड्रॉपडाउन से "rust-analyzer" चुनें)।

यदि आप कोई अलग एडिटर इस्तेमाल कर रहे हैं:
- **Neovim या Vim**: सुनिश्चित करें कि आपका LSP कॉन्फ़िग (जैसे, lsp-zero या nvim-lspconfig के माध्यम से) सही रूट डायरेक्टरी की ओर इशारा करता है, `root_dir` पैटर्न जैसे `util.find_git_ancestor` का उपयोग करके या स्पष्ट रूप से इसे `Cargo.toml` ढूंढने के लिए सेट करें।
- **Kate या Emacs**: समस्या यह हो सकती है कि एडिटर प्रोजेक्ट पथ सही ढंग से पास नहीं कर रहा है—अपने LSP कॉन्फ़िग में मैन्युअल रूप से प्रोजेक्ट रूट सेट करने का प्रयास करें या एडिटर-विशिष्ट बग्स के लिए जांचें (जैसे, सुनिश्चित करें कि यदि आवश्यक हो तो `.git` फ़ोल्डर मौजूद है)।
- **अन्य IDE**: समकक्ष "linked projects" या "workspace root" सेटिंग्स देखें।

यदि इनमें से कुछ भी काम नहीं करता है, तो अधिक विवरण प्रदान करें जैसे आपका एडिटर, क्या यह एक Rust प्रोजेक्ट है, और उस डायरेक्टरी में कोई Rust फ़ाइलें हैं या नहीं।

[rust-analyzer failed to discover workspace in vscode - Stack Overflow](https://stackoverflow.com/questions/72062935/rust-analyzer-failed-to-discover-workspace-in-vscode)  
[Question about failed to find any projects in [AbsPathBuf...] - GitHub](https://github.com/rust-analyzer/rust-analyzer/issues/11666)  
[Problem with Rust-Analyzer - Rust Users Forum](https://users.rust-lang.org/t/problem-with-rust-analyzer/91453)  
[Configuration - rust-analyzer Manual](https://rust-analyzer.github.io/manual.html#configuration)