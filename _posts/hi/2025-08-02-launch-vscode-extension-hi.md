---
audio: false
generated: true
image: false
lang: hi
layout: post
title: वीएसकोड में एक्सटेंशन होस्ट लॉन्च करें
translated: true
type: note
---

Visual Studio Code (VSCode) में **Extension Development Host** लॉन्च करने के लिए, जो एक VSCode एक्सटेंशन डेवलप करने के लिए उपयोग होता है, **F5** दबाने के लिए इन चरणों का पालन करें:

1. **अपना एक्सटेंशन प्रोजेक्ट VSCode में खोलें**:
   - सुनिश्चित करें कि आपके पास एक VSCode एक्सटेंशन प्रोजेक्ट सेट अप है। इसमें आमतौर पर एक `package.json` फ़ाइल शामिल होती है जिसमें आवश्यक एक्सटेंशन कॉन्फ़िगरेशन (जैसे, `contributes`, `activationEvents`) होते हैं।
   - `File > Open Folder` चुनकर या `Ctrl+K, Ctrl+O` (Windows/Linux) या `Cmd+K, Cmd+O` (Mac) का उपयोग करके VSCode में अपना एक्सटेंशन प्रोजेक्ट वाला फ़ोल्डर खोलें।

2. **अपना एक्सटेंशन सेटअप सत्यापित करें**:
   - सुनिश्चित करें कि आपके प्रोजेक्ट रूट में एक वैध `package.json` फ़ाइल है जिसमें कम से कम निम्नलिखित फ़ील्ड हों:
     ```json
     {
       "name": "your-extension-name",
       "displayName": "Your Extension Name",
       "description": "Description of your extension",
       "version": "0.0.1",
       "engines": {
         "vscode": "^1.60.0"
       },
       "categories": ["Other"],
       "activationEvents": ["*"],
       "main": "./extension.js",
       "contributes": {}
     }
     ```
   - सुनिश्चित करें कि आपके पास एक `extension.js` (या समकक्ष) फ़ाइल है जो आपके एक्सटेंशन कोड के लिए एंट्री पॉइंट के रूप में कार्य करती है।
   - यदि आपका एक्सटेंशन Node.js मॉड्यूल्स का उपयोग करता है, तो इंटीग्रेटेड टर्मिनल (`Ctrl+``) में `npm install` चलाकर डिपेंडेंसीज़ इंस्टॉल करें।

3. **Extension Development Host लॉन्च करने के लिए F5 दबाएँ**:
   - जब आपका एक्सटेंशन प्रोजेक्ट VSCode में खुला हो, तो अपने कीबोर्ड पर **F5** दबाएँ।
   - यह **Extension Development Host** शुरू कर देगा, जो एक अलग VSCode विंडो है जहाँ आपका एक्सटेंशन टेस्टिंग के लिए लोड होता है।
   - VSCode स्वचालित रूप से:
     - आपके एक्सटेंशन को बिल्ड करेगा (यदि TypeScript का उपयोग कर रहे हैं, तो यह `.ts` फ़ाइलों को `.js` में कंपाइल करेगा)।
     - आपके एक्सटेंशन के सक्रिय होने के साथ एक नया VSCode इंस्टेंस लॉन्च करेगा।
     - Extension Host प्रक्रिया से जुड़ा एक डिबगर खोलेगा।

4. **डिबगिंग कॉन्फ़िगरेशन**:
   - VSCode डिबगिंग को कॉन्फ़िगर करने के लिए `.vscode` फ़ोल्डर में एक `launch.json` फ़ाइल का उपयोग करता है। यदि यह मौजूद नहीं है, तो जब आप पहली बार F5 दबाएंगे तो VSCode स्वचालित रूप से एक बना देगा।
   - एक एक्सटेंशन के लिए एक विशिष्ट `launch.json` इस प्रकार दिखती है:
     ```json
     {
       "version": "0.2.0",
       "configurations": [
         {
           "name": "Run Extension",
           "type": "extensionHost",
           "request": "launch",
           "args": ["--extensionDevelopmentPath=${workspaceFolder}"],
           "outFiles": ["${workspaceFolder}/out/**/*.js"],
           "preLaunchTask": "npm: watch"
         }
       ]
     }
     ```
   - सुनिश्चित करें कि `preLaunchTask` (यदि मौजूद है) आपके `tasks.json` में किसी टास्क से मेल खाता है (उदाहरण के लिए, TypeScript को कंपाइल करने के लिए)।

5. **अपने एक्सटेंशन का परीक्षण करें**:
   - Extension Development Host विंडो में, आपका एक्सटेंशन सक्रिय होना चाहिए। अपनी कार्यक्षमता (जैसे, कमांड्स, UI योगदान) का परीक्षण करें जैसा कि आपके `package.json` और कोड में परिभाषित है।
   - अपने एक्सटेंशन से लॉग या त्रुटियों को देखने के लिए मुख्य VSCode विंडो में **Debug Console** का उपयोग करें।

6. **समस्या निवारण**:
   - यदि F5 काम नहीं करता है:
     - सुनिश्चित करें कि Node.js और npm इंस्टॉल हैं, क्योंकि वे एक्सटेंशन डेवलपमेंट के लिए आवश्यक हैं।
     - जांचें कि आपके पास VSCode Extension API डिपेंडेंसीज़ इंस्टॉल हैं (`npm install @types/vscode`)।
     - सत्यापित करें कि `launch.json` कॉन्फ़िगरेशन सही पथों की ओर इशारा करता है।
     - यदि आपको त्रुटियाँ दिखाई देती हैं, तो Extension Development Host विंडो में **Output** पैनल (ड्रॉपडाउन में "Extension" चुनें) जांचें।
   - यदि Extension Host लॉन्च नहीं होता है, तो सुनिश्चित करें कि आपके प्रोजेक्ट में `package.json` या आपकी मुख्य एक्सटेंशन फ़ाइल में कोई सिंटैक्स त्रुटि नहीं है।

**अतिरिक्त नोट्स**:
- आप **Run and Debug** पैनल (`Ctrl+Shift+D` या Mac पर `Cmd+Shift+D`) खोलकर और ड्रॉपडाउन से "Run Extension" चुनकर, फिर हरे प्ले बटन पर क्लिक करके भी Extension Development Host शुरू कर सकते हैं।
- परिवर्तन करने के बाद Extension Host को रीलोड करने के लिए, Extension Development Host विंडो में `Ctrl+R` (Windows/Linux) या `Cmd+R` (Mac) का उपयोग करें, या इसे F5 से पुनः आरंभ करें।

अधिक जानकारी के लिए, आधिकारिक VSCode एक्सटेंशन डेवलपमेंट गाइड देखें:  
[VS Code Extension Development](https://code.visualstudio.com/api/get-started/your-first-extension)