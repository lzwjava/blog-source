---
audio: false
generated: true
lang: hi
layout: post
title: टीसीमैलोक त्रुटि को ठीक करें
translated: true
type: note
---

त्रुटि "Cannot locate TCMalloc. Do you have tcmalloc or google-perftool installed on your system? (improves CPU memory usage)" यह दर्शाती है कि TCMalloc लाइब्रेरी, जो Google के gperftools का हिस्सा है, आपके Linux सिस्टम पर इंस्टॉल या ठीक से कॉन्फ़िगर नहीं है। TCMalloc एक मेमोरी एलोकेटर है जो प्रदर्शन में सुधार कर सकता है और मेमोरी उपयोग कम कर सकता है, खासकर Stable Diffusion जैसे एप्लिकेशन में। इस समस्या को ठीक करने के तरीके यहां दिए गए हैं:

### TCMalloc त्रुटि को ठीक करने के चरण

1. **TCMalloc और Google Perftools इंस्टॉल करें**
   अपने Linux डिस्ट्रीब्यूशन के आधार पर, आवश्यक लाइब्रेरीज़ इंस्टॉल करने के लिए उपयुक्त पैकेज मैनेजर का उपयोग करें।

   - **Ubuntu/Debian-आधारित सिस्टम के लिए**:
     ```bash
     sudo apt-get update
     sudo apt-get install libgoogle-perftools-dev libtcmalloc-minimal4 -y
     ```
     यह पूर्ण `libgoogle-perftools-dev` (TCMalloc शामिल है) और `libtcmalloc-minimal4` (एक लाइटवेट संस्करण) दोनों को इंस्टॉल करता है।

   - **Fedora-आधारित सिस्टम के लिए**:
     ```bash
     sudo dnf install gperftools-libs -y
     ```
     यह आवश्यक TCMalloc लाइब्रेरीज़ इंस्टॉल करता है।

   - **CentOS/RHEL-आधारित सिस्टम के लिए**:
     ```bash
     sudo yum install gperftools-libs -y
     ```
     यदि डिफ़ॉल्ट रिपॉजिटरी में पैकेज उपलब्ध नहीं है, तो आपको पहले EPEL रिपॉजिटरी सक्षम करनी पड़ सकती है:
     ```bash
     sudo yum install epel-release
     sudo yum install gperftools-libs -y
     ```

2. **इंस्टॉलेशन सत्यापित करें**
   इंस्टॉलेशन के बाद, जांचें कि क्या TCMalloc इंस्टॉल है:
   ```bash
   dpkg -l | grep tcmalloc
   ```
   आपको `libtcmalloc-minimal4` या इसी तरह के पैकेज सूचीबद्ध दिखाई देने चाहिए। वैकल्पिक रूप से, लाइब्रेरी पथ जांचें:
   ```bash
   dpkg -L libgoogle-perftools-dev | grep libtcmalloc.so
   ```
   यह TCMalloc लाइब्रेरी का पथ दिखाएगा (उदाहरण के लिए, `/usr/lib/libtcmalloc.so.4`)।

3. **LD_PRELOAD एनवायरनमेंट वेरिएबल सेट करें**
   यह सुनिश्चित करने के लिए कि आपका एप्लिकेशन TCMalloc का उपयोग करे, `LD_PRELOAD` एनवायरनमेंट वेरिएबल को TCMalloc लाइब्रेरी की ओर इंगित करने के लिए सेट करें। इसे अस्थायी या स्थायी रूप से किया जा सकता है।

   - **अस्थायी रूप से (वर्तमान सत्र के लिए)**:
     `LD_PRELOAD` सेट करके अपना एप्लिकेशन चलाएं:
     ```bash
     export LD_PRELOAD=/usr/lib/libtcmalloc.so.4
     ./launch.py
     ```
     यदि अलग है तो चरण 2 में मिले वास्तविक पथ से `/usr/lib/libtcmalloc.so.4` को बदलें।

   - **स्थायी रूप से (Stable Diffusion या इसी तरह के लिए)**:
     यदि आप `webui.sh` जैसी स्क्रिप्ट (Stable Diffusion में आम) का उपयोग कर रहे हैं, तो स्क्रिप्ट (जैसे `webui-user.sh`) को संपादित करें ताकि इसमें शामिल हो:
     ```bash
     export LD_PRELOAD=libtcmalloc.so.4
     ```
     फ़ाइल को सेव करें और स्क्रिप्ट को दोबारा चलाएं:
     ```bash
     ./webui.sh
     ```
     वैकल्पिक रूप से, इसे अपने शेल कॉन्फ़िगरेशन (जैसे `~/.bashrc` या `~/.zshrc`) में जोड़ें:
     ```bash
     echo 'export LD_PRELOAD=/usr/lib/libtcmalloc.so.4' >> ~/.bashrc
     source ~/.bashrc
     ```

4. **एप्लिकेशन को दोबारा चलाएं**
   TCMalloc इंस्टॉल करने और `LD_PRELOAD` सेट करने के बाद, अपने एप्लिकेशन को पुनरारंभ करें:
   ```bash
   ./launch.py
   ```
   अब त्रुटि दिखाई नहीं देनी चाहिए, और आपको बेहतर मेमोरी उपयोग या प्रदर्शन दिखाई दे सकता है।

5. **समस्या निवारण**
   - **यदि लाइब्रेरी पथ गलत है**: यदि `LD_PRELOAD` विफल हो जाता है (जैसे "cannot open shared object file"), सटीक लाइब्रेरी नाम और पथ सत्यापित करें:
     ```bash
     find /usr/lib -name "libtcmalloc*.so*"
     ```
     सही पथ (जैसे, यदि मिनिमल वर्जन का उपयोग कर रहे हैं तो `libtcmalloc_minimal.so.4`) के साथ `LD_PRELOAD` अपडेट करें।
   - **यदि त्रुटि बनी रहती है**: सुनिश्चित करें कि इंस्टॉल किया गया TCMalloc वर्जन आपके सिस्टम (आपके मामले में glibc 2.35 और GCC 11.4.0) के साथ संगत है। यदि समस्या जारी रहती है, तो सोर्स से इंस्टॉल करने का प्रयास करें:
     ```bash
     git clone https://github.com/google/tcmalloc.git
     cd tcmalloc
     bazel build //tcmalloc:hello_main
     bazel run //tcmalloc:hello_main
     ```
     विस्तृत निर्देशों के लिए TCMalloc Quickstart गाइड का पालन करें।
   - **मेमोरी समस्याएं**: यदि आपको एलोकेशन विफलताएं या क्रैश आते हैं, तो सुनिश्चित करें कि आपके सिस्टम में पर्याप्त मेमोरी है और TCMalloc अन्य एलोकेटर के साथ संघर्ष नहीं कर रहा है।

6. **वैकल्पिक: TCMalloc उपयोग सत्यापित करें**
   यह पुष्टि करने के लिए कि TCMalloc काम कर रहा है, आप एक सरल टेस्ट प्रोग्राम चला सकते हैं या अपने एप्लिकेशन के चलते समय `top` या `htop` जैसे टूल से मेमोरी उपयोग जांच सकते हैं। TCMalloc आमतौर पर मेमोरी फ़्रैग्मेंटेशन को कम करता है और प्रदर्शन में मामूली सुधार प्रदान कर सकता है।

### अतिरिक्त नोट्स
- **TCMalloc क्यों?** TCMalloc एक हाई-परफॉर्मेंस मेमोरी एलोकेटर है जो CPU मेमोरी उपयोग और फ़्रैग्मेंटेशन को कम करता है, खासकर Stable Diffusion जैसे थ्रेडेड एप्लिकेशन में। यह सख्ती से आवश्यक नहीं है लेकिन प्रदर्शन में सुधार कर सकता है।
- **संगतता**: आपका सिस्टम (glibc 2.35, Python 3.10.12, GCC 11.4.0) नवीनतम TCMalloc वर्जन के साथ संगत है, इसलिए उपरोक्त चरण काम करने चाहिए। यदि आप कस्टम-बिल्ट एप्लिकेशन का उपयोग कर रहे हैं, तो सुनिश्चित करें कि इसे TCMalloc सपोर्ट के साथ कंपाइल किया गया है।
- **Stable Diffusion संदर्भ**: यह त्रुटि अक्सर AUTOMATIC1111 के Stable Diffusion WebUI के साथ दिखाई देती है। उपरोक्त चरण, विशेष रूप से `libgoogle-perftools-dev` इंस्टॉल करना और `LD_PRELOAD` सेट करना, इसे हल करने के लिए जाने जाते हैं।

यदि आपको कोई विशिष्ट त्रुटि मिलती है या किसी विशेष Linux डिस्ट्रीब्यूशन के साथ सहायता की आवश्यकता है, तो मुझे बताएं, और मैं निर्देशों को और अधिक विशिष्ट बना सकता हूं!