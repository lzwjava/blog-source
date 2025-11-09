---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast:free
title: टूटे हुए पायथन जीआई बाइंडिंग्स को ठीक करना
translated: true
type: note
---

### अद्यतन निदान
नई जानकारी के आधार पर, आपकी Python 3.13.7 इंस्टालेशन (संभवतः मैन्युअल या PPA/स्रोत के माध्यम से) ने सिस्टम के GObject Introspection (GI) बाइंडिंग्स को खराब कर दिया है। `gi` मॉड्यूल का `_gi` C एक्सटेंशन आपके डिस्ट्रो की डिफ़ॉल्ट Python (संभवतः 3.10 या 3.11, `/usr/lib/python` में निर्देशिकाओं को देखते हुए) के लिए कंपाइल किया गया है, 3.13 के लिए नहीं। इससे `gnome-terminal` (एक Python स्क्रिप्ट) द्वारा इसे लोड करने का प्रयास करने पर सर्कुलर इम्पोर्ट एरर होती है। `/usr/lib/python` में मल्टी-वर्जन सेटअप इस मिसमैच की पुष्टि करता है—`python3-gi` जैसे सिस्टम पैकेज अभी तक 3.13 के लिए बिल्ड नहीं किए गए हैं (2025 तक, यह अधिकांश डिस्ट्रो के लिए बहुत नया है)।

UFW लॉग अप्रासंगिक शोर बने हुए हैं।

### अनुशंसित समाधान: सिस्टम डिफ़ॉल्ट Python पर वापस लौटें
सबसे साफ-सुथरा समाधान `/usr/bin/python3` को आपके डिस्ट्रो की डिफ़ॉल्ट (जैसे, 3.10) पर वापस स्विच करना है, फिर GI बाइंडिंग्स को पुनः इंस्टॉल करना है। यह `.so` फाइलों को कॉपी करने जैसे हैक्स से बचाता है, जो असंगतताएँ पैदा कर सकते हैं।

1.  **डिफ़ॉल्ट Python वर्जन की पहचान करें और उस पर स्विच करें** (अगर कॉन्फ़िगर किया गया हो तो `update-alternatives` का उपयोग करें; अन्यथा, मैन्युअल सिमलिंक):
    ```
    # जांचें कि क्या अल्टरनेटिव्स सेट अप हैं
    sudo update-alternatives --config python3
    ```
    - अगर यह विकल्प सूचीबद्ध करता है, तो सबसे कम प्राथमिकता वाला विकल्प चुनें (आमतौर पर डिस्ट्रो डिफ़ॉल्ट, जैसे 3.10)।
    - अगर कोई अल्टरनेटिव्स नहीं हैं (स्टॉक Ubuntu पर आम), मैन्युअली वापस लौटें:
      ```
      # मान लें कि डिफ़ॉल्ट 3.10 है (Ubuntu 22.04 के लिए आम; अगर आपका बेस 3.11 है तो उस पर स्विच करें)
      sudo rm /usr/bin/python3
      sudo ln -s /usr/bin/python3.10 /usr/bin/python3
      ```
    - सत्यापित करें: `python3 --version` अब 3.10.x (या आपका डिफ़ॉल्ट) दिखाना चाहिए।

2.  **GI और GNOME Terminal पैकेजों को पुनः इंस्टॉल करें**:
    ```
    sudo apt update
    sudo apt install --reinstall python3-gi gir1.2-glib-2.0 gnome-terminal
    ```

3.  **टेस्ट करें**:
    ```
    python3 -c "from gi.repository import GLib, Gio; print('GI OK')"
    gnome-terminal
    ```
    - अगर Python टेस्ट पास हो जाता है लेकिन टर्मिनल अभी भी फेल होता है, तो इसकी कॉन्फ़िग रीसेट करें: `dconf reset -f /org/gnome/terminal/`.

### अगर आप Python 3.13 रखना चाहते हैं
- यह अधिक पेचीदा है, क्योंकि आधिकारिक `python3-gi` अभी तक 3.13 के लिए मौजूद नहीं होगा। आपको स्रोत से PyGObject कंपाइल करना होगा:
  1.  बिल्ड डिपेंडेंसी इंस्टॉल करें: `sudo apt install libgirepository1.0-dev libcairo2-dev pkg-config python3.13-dev`.
  2.  PyGObject डाउनलोड करें और बिल्ड करें: [आधिकारिक गाइड](https://pygobject.gnome.org/install.html) का `--prefix=/usr/local` के साथ पालन करें।
  3.  लेकिन इससे अन्य सिस्टम टूल्स के खराब होने का जोखिम है—अगर कोई समस्या आए तो वापस लौट आएं।
- या, हैक के तौर पर `_gi` एक्सटेंशन को कॉपी करें (लंबे समय तक अनुशंसित नहीं):
  ```
  cd /usr/lib/python3/dist-packages/gi/
  sudo cp _gi.cpython-3[01]m*.so _gi.cpython-313m-x86_64-linux-gnu.so  # '3[01]' को अपने डिफ़ॉल्ट (3.10 या 3.11) के अनुसार एडजस्ट करें
  ```
  फिर `python3-gi` को ऊपर बताए अनुसार पुनः इंस्टॉल करें।

### रोकथाम
- `/usr/bin/python3` को मैन्युअली ओवरराइड न करें—3.13 की आवश्यकता वाले प्रोजेक्ट्स के लिए वर्चुअलएन्व का उपयोग करें (`python3 -m venv myenv`)।
- अगर आपने 3.13 को deadsnakes PPA के माध्यम से इंस्टॉल किया है, तो इसे हटा दें और डिस्ट्रो Python पर बने रहें।

अगर इससे समस्या ठीक नहीं होती है, तो `ls -l /usr/bin/python*` और `dpkg -l | grep python3 | grep -E 'gi|default'` चलाएं और आउटपुट साझा करें।

[gnome-terminal will not start after trying to install newer version of Python 3](https://askubuntu.com/questions/880188/gnome-terminal-will-not-start-after-trying-to-install-newer-version-of-python-3)  
[ImportError: cannot import name '_gi' from partially initialized module 'gi'](https://stackoverflow.com/questions/59838238/importerror-cannot-import-name-gi-from-partially-initialized-module-gi-mo)  
[Why won't terminal open?](https://www.reddit.com/r/Ubuntu/comments/1f9qh0a/why_wont_terminal_open/)