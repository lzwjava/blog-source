---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: फ़ायरफ़ॉक्स एपीटी रिपॉजिटरी त्रुटि को ठीक करना
translated: true
type: note
---

आपके द्वारा देखी जा रही त्रुटि Mozilla Firefox APT रिपॉजिटरी (`https://packages.mozilla.org/apt`) से विशिष्ट है, जहाँ `binary-all/Packages` इंडेक्स फ़ाइल को फ़ेच करने में 400 Bad Request के साथ विफलता होती है। यह एक ज्ञात और कभी-कभार होने वाली समस्या है जिसकी अन्य Ubuntu/Debian उपयोगकर्ताओं ने शिकायत की है, और यह अक्सर प्रॉक्सी कॉन्फ़िगरेशन (आपका लोकल प्रॉक्सी `127.0.0.1:7890` संकेत देता है कि Clash, V2Ray, या इसी तरह का कोई टूल चल रहा है, जो APT के लिए HTTPS रिक्वेस्ट को खराब कर सकता है) से जुड़ी होती है। अच्छी खबर यह है कि APT इस विफलता को नजरअंदाज कर देता है और कैश्ड/पुराने इंडेक्स का उपयोग कर लेता है, इसलिए सिस्टम अपडेट ब्लॉक नहीं होते—लेकिन इससे Firefox के नवीनतम deb पैकेज प्राप्त करने में रुकावट आ सकती है।

### आजमाने के लिए त्वरित समाधान (क्रम में)
1.  **APT कैशे साफ़ करें** (यह खराब या पुरानी इंडेक्स फ़ाइलों को ठीक करता है, जिससे कई उपयोगकर्ताओं की समस्या हल हुई है):
    ```
    sudo apt clean
    sudo apt update
    ```

2.  **APT के लिए अपने प्रॉक्सी को अस्थायी रूप से बायपास करें** (चूंकि 400 त्रुटि अक्सर रिपॉजिटरी के HTTPS के साथ प्रॉक्सी के हस्तक्षेप से उत्पन्न होती है):
    ```
    unset http_proxy https_proxy all_proxy
    sudo -E apt update
    ```
    - इसे उसी टर्मिनल सत्र में चलाएं। अगर यह काम करता है, तो आप इसे स्थायी बना सकते हैं `~/.bashrc` में `unset` लाइनें जोड़कर (या सिर्फ APT कमांड से पहले) या प्रॉक्सी ऐप को थोड़ी देर के लिए अक्षम करके।
    - यदि आपका प्रॉक्सी सिस्टम-वाइड सेट है (जैसे, `/etc/environment` में), तो APT को बाहर करने के लिए उस फ़ाइल को एडिट करें या लाइनों को अस्थायी रूप से कमेंट आउट कर दें।

3.  **APT के लिए प्रॉक्सी को वैश्विक रूप से अक्षम करें** (यदि उपरोक्त काम करता है लेकिन आप एक स्थायी विकल्प चाहते हैं):
    ```
    echo 'Acquire::http::Proxy "";
    Acquire::https::Proxy "";' | sudo tee /etc/apt/apt.conf.d/99no-proxy
    sudo apt update
    ```
    - यह APT को प्रॉक्सी को पूरी तरह से नजरअंदाज करने के लिए कहता है। यदि आवश्यक हो तो `/etc/apt/apt.conf.d/99no-proxy` को डिलीट करके इसे वापस ले सकते हैं।

### यदि आपको रिपॉजिटरी के बिना नवीनतम Firefox चाहिए
यदि रिपॉजिटरी लगातार विफल हो रही है और आप बस अपडेटेड Firefox चाहते हैं:
-   **Snap पर स्विच करें** (Ubuntu का डिफ़ॉल्ट, आसान अपडेट, रिपॉजिटरी की परेशानी नहीं):
    ```
    sudo snap install firefox
    ```
-   **या Flatpak** (यदि आप पसंद करते हैं):
    ```
    sudo apt install flatpak
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
    flatpak install flathub org.mozilla.firefox
    ```

### रोकथाम/नोट्स
- Mozilla रिपॉजिटरी अनऑफिशियल है और ब्लीडिंग-एज Firefox debs प्राप्त करने के लिए है—जब तक कि आपको विशेष रूप से deb वर्जन की आवश्यकता न हो, Ubuntu के snap वर्जन से चिपके रहने पर विचार करें।
- यदि इनमें से कुछ भी काम नहीं करता है, तो `packages.mozilla.org` की अस्वीकृत रिक्वेस्ट के लिए अपने प्रॉक्सी लॉग (जैसे, Clash डैशबोर्ड) जांचें, या पूरी तरह से प्रॉक्सी के बिना टेस्ट करें।
- सुधारों के बाद `sudo apt update` फिर से चलाकर पुष्टि करें।

यदि ये समाधान इसे ठीक नहीं करते हैं, तो गहन समस्या निवारण के लिए अपने प्रॉक्सी सेटअप या `/etc/apt/sources.list.d/mozilla.list` की पूरी सामग्री जैसे अधिक विवरण साझा करें।

[Ubuntu 23.10 - Update Problems](https://askubuntu.com/questions/1507571/ubuntu-23-10-update-problems-some-index-files-failed-to-download)  
[Firefox apt repository error](https://www.reddit.com/r/firefox/comments/1ois308/firefox_apt_repository_error/)