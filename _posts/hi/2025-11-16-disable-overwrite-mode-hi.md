---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: वीएस कोड ओवरराइट मोड अक्षम करना
translated: true
type: note
---

Visual Studio Code में, डिफ़ॉल्ट व्यवहार **Insert mode** (टाइपिंग टेक्स्ट इन्सर्ट करती है, मौजूदा टेक्स्ट को आगे धकेलती है) होता है।  
**Replace mode** (टाइपिंग मौजूदा टेक्स्ट को ओवरराइट करती है) तब सक्रिय होता है जब आप अपने कीबोर्ड पर **Insert** कुंजी दबाते हैं — यह Insert और Replace/Overwrite mode के बीच टॉगल करता है।

### Replace (Overwrite) mode से वापस Insert mode में कैसे स्विच करें

1. बस अपने कीबोर्ड पर **Insert** कुंजी एक बार दबाएँ।  
   → नीचे दाईं ओर स्थित स्टेटस बार **OVR** (Overwrite) से बदलकर **INS** (Insert) हो जाएगा।

### यदि आप दोबारा गलती से Overwrite mode में नहीं जाना चाहते हैं

आप Insert कुंजी टॉगल को पूरी तरह से अक्षम कर सकते हैं:

#### विधि 1: कीबोर्ड शॉर्टकट (अनुशंसित)
`Ctrl + Shift + P` दबाएँ → **"Toggle Insert/Overwrite"** टाइप करें → आपको कमांड दिखाई देगी  
`Preferences: Toggle Insert on Paste and Overtype` या इसी तरह की कोई कमांड।  
अधिक विश्वसनीय रूप से, इस डायरेक्ट सेटिंग का उपयोग करें:

#### विधि 2: इसे अपने `settings.json` में जोड़ें
```json
// Insert कुंजी द्वारा overwrite mode टॉगल होने से रोकें
"editor.occurencesHighlight": true,
"editor.overtypeMode": false,

// यह मुख्य सेटिंग है:
"keyboard.dispatch": "keyCode"
```

वास्तव में सबसे अच्छा और सामान्य समाधान यह है:

```json
// VS Code में Insert कुंजी को पूरी तरह से अक्षम करें
{
    "key": "insert",
    "command": "-editor.action.toggleOverwrite",
    "when": "editorTextFocus"
}
```

या बस overwrite को वैश्विक रूप से बंद कर दें:

```json
"editor.occurrencesHighlight": true,
"editor.overwriteMode": false   // यह एक वास्तविक सेटिंग नहीं है, इग्नोर करें

// Overwrite टॉगल को अक्षम करने की वास्तविक सेटिंग:
"editor.insertSpaces": true,  // असंबंधित

// सही तरीका:
{
    "key": "insert",
    "command": "noop"   // या डिफ़ॉल्ट बाइंडिंग हटा दें
}
```

#### सबसे सरल स्थायी समाधान (अधिकांश लोग इसे उपयोग करते हैं):
1. सेटिंग्स खोलें (`Ctrl + ,`)
2. **"overwrite"** खोजें
3. **Editor: Overtype** को अनचेक करें (यदि मौजूद हो) या बेहतर यह करें:
4. इस लाइन को अपने `settings.json` में जोड़ें (Ctrl + Shift + P → "Preferences: Open Settings (JSON)"):

```json
// Insert कुंजी द्वारा overwrite mode टॉगल होने को पूरी तरह से अक्षम करें
{
    "key": "insert",
    "command": "-editor.action.toggleOverwrite"
}
```

इसे जोड़ने के बाद, Insert कुंजी VS Code में कुछ नहीं करेगी, और आप हमेशा Insert mode में ही बने रहेंगे।

यह सबसे आम और विश्वसनीय समाधान है जिसे उन डेवलपर्स द्वारा उपयोग किया जाता है जो गलती से Insert (विशेष रूप से छोटे कीबोर्ड वाले लैपटॉप पर जहाँ Insert कुंजी आसानी से दब जाती है) दबा देते हैं।

मुझे बताएं यदि आप macOS पर हैं (अलग कुंजी का उपयोग करता है) या स्टेटस बार क्लिक समाधान चाहते हैं!