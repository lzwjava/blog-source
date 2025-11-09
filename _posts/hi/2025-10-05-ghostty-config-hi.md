---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: घोस्टी शेल कॉन्फ़िगरेशन गाइड
translated: true
type: note
---

### Ghostty और Ubuntu पर .bashrc

Ubuntu (और अन्य Linux डिस्ट्रो) पर .bashrc लोड करने के मामले में Ghostty डिफ़ॉल्ट GNOME टर्मिनल की तरह ही व्यवहार करता है। डिफ़ॉल्ट रूप से, Ghostty bash के लिए **नॉन-लॉगिन इंटरैक्टिव शेल** शुरू करता है, जिसका मतलब है कि यह सीधे `~/.bashrc` को सोर्स करता है—ठीक GNOME टर्मिनल की तरह। यह ज़्यादातर Linux टर्मिनलों के लिए स्टैंडर्ड व्यवहार है, जहां `.bashrc` इंटरैक्टिव शेल सेटअप (जैसे, aliases, prompts, नॉन-लॉगिन सेशन के लिए एनवायरनमेंट वेरिएबल्स) को हैंडल करता है।

#### यह .bashrc को कैसे लोड करता है
- जब आप एक नई Ghostty विंडो या टैब खोलते हैं, तो यह `bash` (या आपका डिफ़ॉल्ट शेल) को एक नॉन-लॉगिन शेल के रूप में एक्ज़िक्यूट करता है।
- Bash जाँच करता है और `~/.bashrc` को सोर्स करता है अगर शेल इंटरैक्टिव है (जो कि डिफ़ॉल्ट रूप से होता है)।
- अगर आपके पास `~/.bash_profile` है (आमतौर पर लॉगिन शेल्स के लिए), तो इसे तब तक सोर्स नहीं किया जाएगा जब तक आप explicitly Ghostty को लॉगिन शेल शुरू करने के लिए कॉन्फ़िगर नहीं करते (जैसे, `~/.config/ghostty/config` में `initial-command = bash --login` ऐड करके)।
- संभावित समस्याएँ: कुछ यूज़र्स नए यूज़र्स के लिए पहले लॉन्च पर या specific सेटअप (जैसे, Ubuntu पर रिमोट SSH सेशन) में `.bashrc` के न लोड होने की रिपोर्ट करते हैं। इसे अक्सर यह सुनिश्चित करके ठीक किया जा सकता है कि कोई conflict वाला `~/.bash_profile` मौजूद न हो, या अपने कॉन्फ़िग में मैन्युअल रूप से इसे सोर्स करके। `.bashrc` में `[[ $- != *i* ]] && return` जैसा एक गार्ड ऐड करने से नॉन-इंटरैक्टिव कॉन्टेक्स्ट में समस्याओं को रोका जा सकता है।

संक्षेप में, हाँ—Ubuntu पर `.bashrc` के उपयोग के लिए Ghostty डिफ़ॉल्ट टर्मिनल के समान है, उसी नॉन-लॉगिन डिफ़ॉल्ट के साथ।

### macOS पर Ghostty: .zprofile या .bash_profile?

macOS पर, Ghostty प्लेटफ़ॉर्म की परंपरा (जैसे Terminal.app) का पालन करता है और डिफ़ॉल्ट रूप से **लॉगिन शेल** शुरू करता है, भले ही शेल कोई भी हो। यह प्रभावित करता है कि कौन सा प्रोफ़ाइल लोड होता है:

- **अगर zsh का उपयोग कर रहे हैं (Catalina के बाद से macOS डिफ़ॉल्ट)**: यह हर बार एक नया टर्मिनल खुलने पर `~/.zprofile` (लॉगिन सेटअप के लिए) *और* `~/.zshrc` (इंटरैक्टिव सेटअप के लिए) दोनों को सोर्स करता है।
- **अगर bash का उपयोग कर रहे हैं**: यह `~/.bash_profile` (लॉगिन शेल) को सोर्स करता है। Bash यहाँ सीधे `~/.bashrc` को सोर्स नहीं करेगा—`~/.bashrc` केवल नॉन-लॉगिन इंटरैक्टिव शेल्स के लिए है। `.bashrc` कंटेंट को शामिल करने के लिए, इसे अपने `~/.bash_profile` में ऐड करें:
  ```
  if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
  ```

तो, यह डिफ़ॉल्ट zsh सेटअप के लिए `~/.zprofile` लोड करता है, या `~/.bash_profile` अगर आप bash का उपयोग कर रहे हैं। ज़रूरत पड़ने पर आप शेल्स को स्विच कर सकते हैं या Ghostty के कॉन्फ़िग के ज़रिए ट्वीक कर सकते हैं।

[Shell Integration - Ghostty](https://ghostty.org/docs/features/shell-integration)  
[macOS Login Shells - Ghostty](https://ghostty.org/docs/help/macos-login-shells)  
[Potential bug, .bashrc not read on startup - GitHub Discussion](https://github.com/ghostty-org/ghostty/discussions/3437)  
[Bash Startup Files - GNU Manual](https://www.gnu.org/software/bash/manual/bash.html#Bash-Startup-Files)