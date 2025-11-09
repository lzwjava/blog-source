---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: उबुन्टू 24.04 पर ज़ेड इंस्टॉल करें
translated: true
type: note
---

Ubuntu 24.04 LTS के लिए, Zed (हाई-परफॉर्मेंस कोड एडिटर) को इंस्टॉल करने का सबसे सीधा और ऑफिशियल तरीका उनके द्वारा प्रदान किया गया shell script है, जो ज़्यादातर Linux डिस्ट्रीब्यूशन जैसे कि Ubuntu जैसे Debian-आधारित सिस्टम पर नेटिवली काम करता है। यह अपने आप डिपेंडेंसीज़ को हैंडल कर लेता है और यह सुनिश्चित करता है कि आपको नवीनतम स्टेबल रिलीज़ मिले।

### अनुशंसित इंस्टॉलेशन: ऑफिशियल स्क्रिप्ट
अपने टर्मिनल में यह चलाएं:
```
curl -f https://zed.dev/install.sh | sh
```
- यह Zed को `~/.local/bin/zed` में इंस्टॉल करता है (अगर ज़रूरत हो तो अपने PATH में ऐड करें: `~/.bashrc` या इसी तरह के फाइल में `export PATH="$HOME/.local/bin:$PATH"` लिखें)।
- पूर्व-आवश्यकताएं: आपका सिस्टम (kernel 6.14 पर glibc 2.39) आवश्यकताओं को पूरा करता है (x86_64 glibc >= 2.31)।
- इंस्टॉल होने के बाद, `zed` कमांड से या GNOME के app menu से लॉन्च करें।
- प्रीव्यू चैनल (नाइटली बिल्ड्स) के लिए: `curl -f https://zed.dev/install.sh | ZED_CHANNEL=preview sh`।

अगर आप एक सैंडबॉक्स्ड, यूनिवर्सल पैकेज पसंद करते हैं (जिसमें नेटिव डिपेंडेंसीज़ की चिंता नहीं करनी पड़ती), तो अपनी सूची से Flathub विकल्प (`dev.zed.Zed`) का उपयोग Flatpak के जरिए करें:
1. अगर Flatpak मौजूद नहीं है तो इंस्टॉल करें: `sudo apt update && sudo apt install flatpak`।
2. Flathub रिपोजिटरी ऐड करें: `flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo`।
3. इंस्टॉल करें: `flatpak install flathub dev.zed.Zed`।
4. चलाएं: `flatpak run dev.zed.Zed`।

GNOME जैसे डेस्कटॉप के लिए स्क्रिप्ट आम तौर पर तेज़ और ज़्यादा इंटीग्रेटेड होती है, लेकिन अगर आप आइसोलेशन चाहते हैं या पहले से ही दूसरे ऐप्स के लिए Flatpak का इस्तेमाल करते हैं तो यह बढ़िया विकल्प है। अपनी सूची में दिए गए दूसरे विकल्पों से बचें, क्योंकि वे नॉन-डेबियन डिस्ट्रोज़ के लिए हैं और बिना अतिरिक्त सेटअप के Ubuntu पर सीधे काम नहीं करेंगे।

### संदर्भ
- [Zed Linux Installation Docs](https://zed.dev/docs/linux)
- [Zed on Linux Announcement](https://zed.dev/linux)
- [Repology Zed Packages](https://repology.org/project/zed-editor/versions)