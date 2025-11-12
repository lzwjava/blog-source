---
audio: false
generated: true
lang: hi
layout: post
title: वीएसकोड एक्सटेंशन बनाना
translated: true
type: note
---

Visual Studio Code (VSCode) एक्सटेंशन बनाना आपके विकास वर्कफ्लो को बेहतर बनाने या समुदाय में योगदान देने का एक फायदेमंद तरीका हो सकता है। VSCode प्लगइन लिखना शुरू करने में आपकी मदद करने के लिए यहां एक व्यापक गाइड दी गई है:

### 1. आवश्यक शर्तें
- **Node.js और npm**: सुनिश्चित करें कि आपके पास Node.js और npm इंस्टॉल हैं। आप उन्हें [nodejs.org](https://nodejs.org/) से डाउनलोड कर सकते हैं।
- **Yeoman और VSCode Extension Generator**: npm का उपयोग करके Yeoman और VSCode Extension Generator को वैश्विक रूप से इंस्टॉल करें।

```bash
npm install -g yo generator-code
```

### 2. अपने डेवलपमेंट एनवायरनमेंट को सेट अप करना
- **Visual Studio Code इंस्टॉल करें**: सुनिश्चित करें कि आपके पास VSCode इंस्टॉल है। आप इसे [code.visualstudio.com](https://code.visualstudio.com/) से डाउनलोड कर सकते हैं।

### 3. एक नया एक्सटेंशन जनरेट करें
एक नया एक्सटेंशन स्कैफोल्ड करने के लिए Yeoman जनरेटर का उपयोग करें। एक टर्मिनल खोलें और चलाएं:

```bash
yo code
```

अपना एक्सटेंशन सेट अप करने के लिए प्रॉम्प्ट का पालन करें। आपसे पूछा जाएगा:
- एक्सटेंशन का प्रकार (जैसे, New Extension, New Color Theme, आदि)
- आपके एक्सटेंशन का नाम
- एक आइडेंटिफायर (जैसे, `my-extension`)
- एक विवरण
- एक git रिपॉजिटरी इनिशियलाइज़ करना
- भाषा चुनना (TypeScript या JavaScript)
- आवश्यक डिपेंडेंसीज़ इंस्टॉल करना

### 4. प्रोजेक्ट स्ट्रक्चर को समझना
आपके नए एक्सटेंशन की निम्नलिखित संरचना होगी:
- `.vscode/`: डीबगिंग के लिए लॉन्च कॉन्फ़िगरेशन शामिल हैं।
- `src/`: आपके एक्सटेंशन का सोर्स कोड शामिल है।
- `package.json`: आपके एक्सटेंशन के लिए मेनिफेस्ट फ़ाइल।
- `tsconfig.json`: TypeScript कॉन्फ़िगरेशन फ़ाइल (यदि TypeScript का उपयोग कर रहे हैं)।

### 5. अपना एक्सटेंशन लिखना
- **एक्टिवेशन**: परिभाषित करें कि आपका एक्सटेंशन कब एक्टिवेट होना चाहिए, `package.json` में `activationEvents` फ़ील्ड के अंतर्गत।
- **कंट्रीब्यूशन पॉइंट्स**: परिभाषित करें कि आपका एक्सटेंशन VSCode में क्या योगदान देता है, जैसे कमांड्स, व्यू, या भाषाएं, `package.json` के `contributes` सेक्शन में।

### 6. कमांड्स को इम्प्लीमेंट करना
ऐसी कमांड्स बनाएं जिन्हें उपयोगकर्ता इनवोक कर सकें। उन्हें `package.json` में परिभाषित करें और उन्हें अपनी मुख्य एक्सटेंशन फ़ाइल (जैसे, `src/extension.ts` या `src/extension.js`) में इम्प्लीमेंट करें।

`package.json` में एक कमांड का उदाहरण:

```json
"contributes": {
    "commands": [
        {
            "command": "extension.sayHello",
            "title": "Say Hello"
        }
    ]
}
```

कमांड को `src/extension.ts` में इम्प्लीमेंट करें:

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('extension.sayHello', () => {
        vscode.window.showInformationMessage('Hello, World!');
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
```

### 7. अपने एक्सटेंशन को डीबग करना
- अपना एक्सटेंशन लोड किए हुए एक नया VSCode विंडो खोलने के लिए `F5` दबाएं।
- ब्रेकपॉइंट्स सेट करें और अपने एक्सटेंशन को टेस्ट करने के लिए डीबग कंसोल का उपयोग करें।

### 8. पैकेजिंग और प्रकाशन
- **एक्सटेंशन पैकेज करें**: अपने एक्सटेंशन को पैकेज करने के लिए `vsce` टूल का उपयोग करें।

```bash
npm install -g vsce
vsce package
```

- **मार्केटप्लेस पर प्रकाशित करें**: अपने एक्सटेंशन को प्रकाशित करने के लिए [VSCode Marketplace](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) पर दिए गए निर्देशों का पालन करें।

### 9. डॉक्यूमेंटेशन और बेस्ट प्रैक्टिसेज़
- **डॉक्यूमेंटेशन**: अपने एक्सटेंशन के लिए `README.md` फ़ाइल में स्पष्ट डॉक्यूमेंटेशन प्रदान करें।
- **टेस्टिंग**: यह सुनिश्चित करने के लिए टेस्ट लिखें कि आपका एक्सटेंशन अपेक्षा के अनुरूप काम करता है।
- **वर्जनिंग**: अपने एक्सटेंशन रिलीज़ के लिए सेमेंटिक वर्जनिंग का पालन करें।

### 10. अतिरिक्त संसाधन
- **VSCode API डॉक्यूमेंटेशन**: [vscode-api](https://code.visualstudio.com/api)
- **एक्सटेंशन सैंपल**: [vscode-extension-samples](https://github.com/microsoft/vscode-extension-samples)

इन चरणों का पालन करके, आप एक कार्यात्मक और उपयोगी VSCode एक्सटेंशन बनाने के अपने रास्ते पर अच्छी तरह से आगे बढ़ जाएंगे। हैप्पी कोडिंग!