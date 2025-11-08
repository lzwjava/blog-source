---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: ज़ेड को एमाक्स की-बाइंडिंग्स के साथ कॉन्फ़िगर करना
translated: true
type: note
---

### Zed एडिटर को Emacs की-बाइंडिंग्स के साथ कॉन्फ़िगर करना

ऐसा लगता है कि आपका मतलब **Zed** (हाई-परफॉर्मेंस कोड एडिटर) से है, क्योंकि "Zig एडिटर" किसी मानक टूल को रेफर नहीं करता—Zig एक प्रोग्रामिंग लैंग्वेज है जिसमें बिल्ट-इन एडिटर नहीं होता। अगर आपका यह इरादा नहीं था, तो कृपया स्पष्ट करें! Zed मानकर, इसमें Emacs की-बाइंडिंग्स के लिए बिल्ट-इन सपोर्ट है (जिसे "Emacs (Beta)" लेबल किया गया है)। यह बेसिक कार्यों को बॉक्स से बाहर ही कवर कर लेता है, जैसे मूवमेंट (`Ctrl-b/f/n/p`) और एडिटिंग (`Ctrl-d` करैक्टर डिलीट करने के लिए, `Ctrl-k` लाइन के अंत तक कट करने के लिए)। आप इसे आसानी से एनेबल कर सकते हैं, और फिर जरूरत पड़ने पर और कस्टमाइज कर सकते हैं।

#### चरण 1: बिल्ट-इन Emacs कीमैप को एनेबल करें
Zed का Emacs मोड पहले से डिफाइंड है और बेसिक कार्यों के लिए मैन्युअल बाइंडिंग सेटअप की जरूरत नहीं होती। इसे एक्टिवेट करने का तरीका यहां बताया गया है:

1. Zed की सेटिंग्स खोलें:
   - macOS: `Cmd-,`
   - Windows/Linux: `Ctrl-,`

2. सेटिंग्स UI में, "base keymap" सर्च करें और इसे **Emacs** पर सेट करें।

   *या, सीधे `settings.json` में एडिट करें* (macOS पर `Cmd-Alt-,` या Windows/Linux पर `Ctrl-Alt-,` दबाकर खोलें):
   ```json
   {
     "base_keymap": "Emacs"
   }
   ```

   सेव करें और Zed को रीलोड करें (`Cmd-R` या `Ctrl-R`)। बस—बीटा Emacs कीमैप तुरंत एक्टिव हो जाएगा।

   वैकल्पिक रूप से, कमांड पैलेट (`Cmd-Shift-P` या `Ctrl-Shift-P`) का उपयोग करें, "toggle base keymap" टाइप करें, और Emacs को सेलेक्ट करें।

यह आपको एक्स्ट्रा काम किए बिना कोर Emacs की आदतों को यूज करने देता है। बिल्ट-इन बाइंडिंग्स की पूरी लिस्ट के लिए, Zed के डिफॉल्ट कीमैप फाइल्स को सोर्स (जैसे, GitHub के जरिए) में चेक करें, लेकिन बेसिक्स में शामिल हैं:
- **मूवमेंट**: `Ctrl-b` (बायां करैक्टर), `Ctrl-f` (दायां करैक्टर), `Ctrl-p` (ऊपर लाइन), `Ctrl-n` (नीचे लाइन), `Alt-b/f` (पिछला/अगला शब्द)।
- **एडिटिंग**: `Ctrl-d` (करैक्टर डिलीट), `Ctrl-k` (लाइन के अंत तक कट), `Ctrl-y` (यैंक/पेस्ट), `Ctrl-@` (रीजन के लिए मार्क सेट), `Ctrl-w` (रीजन कट)।
- **अन्य**: `Ctrl-x Ctrl-s` (सेव), `Ctrl-g` (कैंसल), `Ctrl-/` (अंडू)।

#### चरण 2: बेसिक बाइंडिंग्स जोड़ें या कस्टमाइज करें (अगर जरूरत हो)
ट्वीक्स या ज्यादा Emacs जैसा व्यवहार (जैसे, बेहतर home/end या पैराग्राफ नेविगेशन) के लिए, `keymap.json` एडिट करें:
- इसे कमांड पैलेट के जरिए खोलें: "open keymap file" टाइप करें।
- पाथ: `~/.config/zed/keymap.json` (macOS/Linux) या `~\AppData\Roaming\Zed\keymap.json` (Windows)।

बाइंडिंग्स को JSON ऐरे के रूप में "Editor" जैसे कॉन्टेक्स्ट्स के अंदर ऐड करें। यहां बेसिक मूवमेंट और एडिटिंग के लिए एक **मिनिमल उदाहरण** दिया गया है (कम्पैटिबिलिटी के लिए कम्युनिटी कॉन्फ़िग्स पर आधारित; इसे ऐरे में पेस्ट करें):

```json
[
  {
    "context": "Editor",
    "bindings": {
      // बेसिक मूवमेंट
      "ctrl-a": "editor::MoveToBeginningOfLine",
      "ctrl-e": "editor::MoveToEndOfLine",
      "ctrl-b": "editor::MoveLeft",
      "ctrl-f": "editor::MoveRight",
      "ctrl-p": "editor::MoveLineUp",
      "ctrl-n": "editor::MoveLineDown",
      "alt-b": "editor::MoveToPreviousWordStart",
      "alt-f": "editor::MoveToNextWordEnd",

      // बेसिक एडिटिंग
      "ctrl-d": "editor::DeleteRight",
      "ctrl-k": "editor::CutToEndOfLine",
      "ctrl-y": "editor::Paste",
      "ctrl-w": "editor::Cut",
      "ctrl-@": ["editor::SetSelectionAnchor", { "selection_id": 0 }],  // मार्क सेट करें
      "ctrl-x ctrl-x": "editor::FlipSelectionAnchor",  // पॉइंट/मार्क एक्सचेंज करें

      // नेविगेशन एक्स्ट्रा
      "ctrl-home": "editor::MoveToBeginning",
      "ctrl-end": "editor::MoveToEnd",
      "ctrl-g": "editor::Cancel"
    }
  }
]
```

- सेव करें और Zed को रीलोड करें। ये बेस Emacs मैप को ओवरराइड या ऐड करती हैं।
- एक एडिटर बफर में टेस्ट करें। सेलेक्शन के लिए, मार्क सेट करने के लिए `Ctrl-Space` (या `Ctrl-@`) यूज करें, फिर रीजन सेलेक्ट करने के लिए मूव करें।
- प्रो टिप: कॉन्फ्लिक्ट से बचने के लिए सेटिंग.json में `vim_mode: false` के साथ कॉम्बाइन करें।

#### टिप्स
- **बीटा स्टेटस**: Emacs मोड में सुधार हो रहा है (प्रोग्रेस [यहां](https://github.com/zed-industries/zed/issues/4856) ट्रैक करें)। Zed के GitHub पर इश्यू रिपोर्ट करें।
- **फुल कस्टम सेटअप**: एडवांस्ड (जैसे, `Ctrl-x o` के साथ पेन स्विचिंग) के लिए, नीचे डिस्कशन में कम्युनिटी उदाहरण देखें।
- अगर आप Vim/Helix मोड्स को साथ में चाहते हैं, तो सेटिंग्स में `vim_mode: true` या `helix_mode: true` सेट करें—वे ऊपर से लेयर हो जाते हैं।

यह आपको बेसिक Emacs फील का 80% दे देगा। बिल्ट-इन से शुरुआत करें, फिर इटरेट करें!

[की बाइंडिंग्स डॉक्स](https://zed.dev/docs/key-bindings)  
[Zed को कॉन्फ़िगर करना](https://zed.dev/docs/configuring-zed)  
[Emacs कीमैप डिस्कशन](https://github.com/zed-industries/zed/discussions/6572)  
[Emacs कम्पैटिबिलिटी इश्यू](https://github.com/zed-industries/zed/issues/4856)