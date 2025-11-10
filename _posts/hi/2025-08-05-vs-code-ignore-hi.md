---
audio: false
generated: true
image: false
lang: hi
layout: post
title: वीएस कोड में अनदेखी फ़ाइलें छुपाएँ
translated: true
type: note
---

आप अपनी `settings.json` में तीन सेटिंग्स को बदलकर "Go to File" (Quick Open, Ctrl + P) में उन फ़ाइलों को शामिल कर सकते हैं जो आपके `.gitignore` में हैं:

1. **सर्च को अपने `.gitignore` नियमों को नज़रअंदाज़ करने के लिए कहें**

   ```jsonc
   "search.useIgnoreFiles": false,      // .gitignore का सम्मान न करें
   "search.useGlobalIgnoreFiles": false // अपने ग्लोबल gitignore का सम्मान न करें
   ```
2. **सुनिश्चित करें कि आपके एक्सक्लूज़न ग्लोब्स उन फ़ाइलों को छुपा नहीं रहे हैं**
   डिफ़ॉल्ट रूप से VS Code `files.exclude` से सभी पैटर्न को `search.exclude` में इनहेरिट करता है। यदि आपने वहाँ `.gitignore`-डायरेक्टरीज़ को मैन्युअली एक्सक्लूड किया है, तो उन्हें फिर से सक्षम करें:

   ```jsonc
   "search.exclude": {
     "**/.git": false,          // .git को इंडेक्स करें (यदि आप चाहते हैं)
     "**/.gitignore": false     // निश्चित रूप से अपनी .gitignore फ़ाइल को मत छुपाएं
     // ...कोई अन्य पैटर्न जिसे आप ओवरराइड करना चाहते हैं
   }
   ```
3. **विंडो को रीलोड करें**
   अपनी यूज़र या वर्कस्पेस सेटिंग्स सेव करने के बाद, **Developer: Reload Window** (⇧ ⌘ P → "Reload Window") चलाएं ताकि फ़ाइल-इंडेक्सर इस बदलाव को पकड़ सके।

अब जब आप Ctrl + P दबाएंगे, तो आपको *सभी* फ़ाइलें उनके नाम से दिखाई देंगी—चाहे वे इग्नोर हों या न हों। ([stackoverflow.com][1])

[1]: https://stackoverflow.com/questions/62855190/how-do-you-include-git-ignored-files-in-vscode-quick-search?utm_source=chatgpt.com "How do you include git ignored files in VSCode quick search"