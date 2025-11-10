---
audio: false
generated: true
lang: hi
layout: post
title: उबुन्टू पर पायथन क्लिपबोर्ड एक्सेस
translated: true
type: note
---

Ubuntu में Python का उपयोग करके क्लिपबोर्ड (पेस्टबोर्ड) से पढ़ने के लिए, आप `pyperclip` जैसी लाइब्रेरीज़ का उपयोग कर सकते हैं या सिस्टम क्लिपबोर्ड यूटिलिटीज जैसे `xclip` या `xsel` के साथ इंटरैक्ट कर सकते हैं। नीचे दो सामान्य तरीके दिए गए हैं:

### तरीका 1: `pyperclip` का उपयोग करना
`pyperclip` क्लिपबोर्ड तक पहुंच के लिए एक क्रॉस-प्लेटफॉर्म Python लाइब्रेरी है।

1. **pyperclip इंस्टॉल करें**:
   ```bash
   pip install pyperclip
   ```

2. **क्लिपबोर्ड से पढ़ने के लिए Python कोड**:
   ```python
   import pyperclip

   # क्लिपबोर्ड की सामग्री पढ़ें
   clipboard_content = pyperclip.paste()
   print(clipboard_content)
   ```

3. **नोट्स**:
   - सुनिश्चित करें कि Ubuntu पर `xclip` या `xsel` इंस्टॉल है, क्योंकि `pyperclip` उन पर निर्भर करता है:
     ```bash
     sudo apt update
     sudo apt install xclip xsel
     ```
   - यह तरीका सरल है और सभी प्लेटफॉर्म्स पर काम करता है।

### तरीका 2: सीधे `xclip` का उपयोग करना
यदि आप सिस्टम क्लिपबोर्ड से सीधे इंटरैक्ट करना पसंद करते हैं, तो आप `xclip` का उपयोग कर सकते हैं।

1. **xclip इंस्टॉल करें**:
   ```bash
   sudo apt update
   sudo apt install xclip
   ```

2. **क्लिपबोर्ड से पढ़ने के लिए Python कोड `xclip` का उपयोग करके**:
   ```python
   import subprocess

   # क्लिपबोर्ड की सामग्री पढ़ें
   process = subprocess.run(['xclip', '-selection', 'clipboard', '-o'], capture_output=True, text=True)
   clipboard_content = process.stdout
   print(clipboard_content)
   ```

3. **नोट्स**:
   - यह तरीका सीधे `xclip` कमांड-लाइन टूल को कॉल करता है।
   - आधुनिक क्लिपबोर्ड (Ctrl+C/Ctrl+V) के लिए `-selection clipboard` या माउस-सिलेक्शन क्लिपबोर्ड के लिए `-selection primary` का उपयोग करें।
   - सुनिश्चित करें कि `xclip` इंस्टॉल है।

### सिफारिशें
- **`pyperclip` का उपयोग करें** सरलता और पोर्टेबिलिटी के लिए, जब तक कि आपके पास `xclip` या `xsel` का उपयोग करने के विशिष्ट कारण न हों।
- Ubuntu पर क्लिपबोर्ड एक्सेस के लिए दोनों तरीकों को `xclip` या `xsel` के इंस्टॉल होने की आवश्यकता होती है।
- यदि क्लिपबोर्ड की सामग्री टेक्स्ट नहीं है (जैसे, एक इमेज), तो यह तरीके अपेक्षा के अनुरूप काम नहीं कर सकते हैं, और आपको गैर-टेक्स्ट डेटा के लिए `pyclip` जैसी लाइब्रेरी या अतिरिक्त हैंडलिंग की आवश्यकता होगी।

Ubuntu 22.04 पर Python 3..10 के साथ टेस्ट किया गया। यदि आपको कोई समस्या आती है, तो सुनिश्चित करें कि आवश्यक टूल्स (`xclip` या `xsel`) इंस्टॉल हैं और क्लिपबोर्ड में टेक्स्ट डेटा है।