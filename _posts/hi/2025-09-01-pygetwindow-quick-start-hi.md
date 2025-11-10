---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: पाइगेटविंडो त्वरित प्रारंभ गाइड
translated: true
type: note
---

### इंस्टॉलेशन

PyGetWindow विंडोज, macOS, और Linux जैसे कई प्लेटफॉर्म पर विंडोज को मैनिपुलेट और क्वेरी करने के लिए एक Python लाइब्रेरी है। इसे pip के माध्यम से इंस्टॉल करें:

```bash
pip install pygetwindow
```

### मॉड्यूल को इम्पोर्ट करना

अपने Python स्क्रिप्ट में मॉड्यूल को इम्पोर्ट करके शुरुआत करें:

```python
import pygetwindow as gw
```

### विंडो ऑब्जेक्ट प्राप्त करना

PyGetWindow विंडोज को `Window` ऑब्जेक्ट के रूप में दर्शाता है। आप विंडोज को टाइटल, प्रोसेस, या अन्य विशेषताओं के आधार पर प्राप्त कर सकते हैं।

- **सभी विंडो ऑब्जेक्ट प्राप्त करें**:  
  सभी खुली विंडोज की सूची प्राप्त करने के लिए `gw.getAllWindows()` का उपयोग करें।

- **टाइटल के आधार पर विंडोज प्राप्त करें**:  
  आंशिक या सटीक मिलान के लिए `gw.getWindowsWithTitle(title)` या `gw.getFirstWindowWithTitle(title)` का उपयोग करें।

- **एक्टिव विंडो प्राप्त करें**:  
  वर्तमान में फोकस्ड विंडो प्राप्त करने के लिए `gw.getActiveWindow()` का उपयोग करें।

उदाहरण:
```python
windows = gw.getAllWindows()
active = gw.getActiveWindow()
notepad = gw.getWindowsWithTitle('Notepad')  # 'Notepad' वाले टाइटल की विंडोज की सूची
```

### विंडो ऑब्जेक्ट पर सामान्य मेथड्स

एक बार आपके पास `Window` ऑब्जेक्ट होने पर, आप प्रॉपर्टीज और मेथड्स तक पहुंच सकते हैं जैसे:

- **प्रॉपर्टीज**: `title`, `left`, `top`, `width`, `height`, `isMinimized`, `isMaximized`, `isActive`.
- **मेथड्स**:
  - `activate()`: विंडो को सामने लाएं और एक्टिव बनाएं।
  - `maximize()` / `minimize()` / `restore()` / `close()`: विंडो की स्थिति को नियंत्रित करें।
  - `resize() / move()`: आकार और स्थिति समायोजित करें।

उदाहरण:
```python
if notepad:
    win = notepad[0]
    print(win.title)  # आउटपुट: उदाहरण के लिए, 'Untitled - Notepad'
    win.activate()
    win.maximize()
    win.move(100, 100)  # पोजिशन (100, 100) पर ले जाएं
    win.resize(800, 600)  # आकार 800x600 करें
```

### एक से अधिक प्लेटफॉर्म को हैंडल करना

- Windows और macOS पर, यह नेटिव APIs का उपयोग करता है।
- Linux पर, यह X11 या Wayland सपोर्ट पर निर्भर करता है; सुनिश्चित करें कि आपके सिस्टम पर यह इंस्टॉल है (उदाहरण के लिए, Ubuntu पर `x11-utils`)।
- यदि कोई मेथड आपके OS पर सपोर्टेड नहीं है, तो यह `NotImplementedError` उठा सकता है।

### उदाहरण

यहां कुछ व्यावहारिक कोड स्निपेट दिए गए हैं:

1. **सभी विंडो टाइटल प्रिंट करें**:
   ```python
   for win in gw.getAllWindows():
       print(win.title)
   ```

2. **एक विशिष्ट विंडो बंद करें**:
   ```python
   firefox_wins = gw.getWindowsWithTitle('Mozilla Firefox')
   if firefox_wins:
       firefox_wins[0].close()
   ```

3. **एक से अधिक विंडोज को मूव और रीसाइज़ करें**:
   ```python
   windows = gw.getAllWindows()
   for i, win in enumerate(windows[:3]):  # पहली 3 विंडोज
       win.move(50 * i, 50 * i)
       win.resize(400, 400)
   ```

एडवांस्ड उपयोग के लिए, [ऑफिशियल डॉक्यूमेंटेशन](https://pygetwindow.readthedocs.io/) देखें। यदि आपको प्लेटफॉर्म-विशिष्ट समस्याओं का सामना करना पड़ता है, तो सिस्टम परमिशन या Linux पर `xdotool` जैसी डिपेंडेंसीज की जांच करें।