---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: घोस्ट्टी इंस्टॉलेशन और लॉन्च समस्याएँ
translated: true
type: note
---

### समस्या निदान

आपके साझा किए गए लॉग्स के आधार पर, Ghostty 1.1.3 की `.deb` पैकेज के माध्यम से इंस्टॉलेशन सफल रही, लेकिन इसे लॉन्च करने में विफलता दो मुख्य कारणों से हो रही है:

1.  **CLI आर्गुमेंट त्रुटि**: कमांड `ghostty .` `.` को एक अमान्य कॉन्फ़िगरेशन फ़ील्ड के रूप में मानता है (संभवतः एक डायरेक्टरी के रूप में इरादा था, लेकिन Ghostty उस सिंटैक्स का समर्थन नहीं करता है)। इसके कारण "invalid field" के साथ तुरंत बाहर निकल जाता है।

2.  **OpenGL/GTK अनुकूलता समस्या**: बिना आर्गुमेंट के `ghostty` चलाने पर, यह इनिशियलाइज़ होता है लेकिन "OpenGL version is too old. Ghostty requires OpenGL 3.3" (आपका सिस्टम Ghostty को 3.2 रिपोर्ट करता है) के कारण क्रैश हो जाता है। यह Ubuntu 22.04 पर एक ज्ञात समस्या है, खासकर X11 के तहत NVIDIA ड्राइवरों के साथ। इसके बावजूद कि `glxinfo` अक्सर OpenGL 4.6+ दिखाता है, Ghostty का GTK 4.6 रनटाइम NVIDIA GL के साथ उच्च वर्जन तक ठीक से एक्सेस नहीं कर पाता है। "GDK_DEBUG=vulkan-disable" चेतावनी एक वर्कअराउंड प्रयास है लेकिन मूल समस्या को हल नहीं करती है। अंतिम Gtk-CRITICAL त्रुटि विफल सतह रियलाइज़ेशन का एक लक्षण है।

यह Ubuntu 22.04 (और Pop!\_OS जैसे डेरिवेटिव) पर कई उपयोगकर्ताओं को प्रभावित करता है क्योंकि GTK का पुराना वर्जन (4.6 बनाम नए 4.12+ की जरूरत पूर्ण NVIDIA अनुकूलता के लिए) है।

### त्वरित जांचें
- अपने वास्तविक OpenGL सपोर्ट की पुष्टि करें (अगर जरूरत हो तो `mesa-utils` इंस्टॉल करें: `sudo apt install mesa-utils`):
  ```
  glxinfo | grep "OpenGL version"
  ```
  अगर यह 3.3+ रिपोर्ट करता है, तो समस्या वास्तव में GTK/NVIDIA-विशिष्ट है।
- अपने सत्र के प्रकार की जांच करें: `echo $XDG_SESSION_TYPE`। अगर यह `x11` है, तो यह इसमें योगदान दे रहा है।

### समाधान
यहां चरण-दर-चरण समाधान दिए गए हैं, सबसे सरल से शुरू करते हुए:

1.  **Wayland पर स्विच करें (अगर आपके पास हाइब्रिड ग्राफिक्स है, जैसे Intel + NVIDIA)**:
    - लॉग आउट करें और लॉगिन पर एक Wayland सत्र चुनें (या `/etc/gdm3/custom.conf` में `WaylandEnable=true` जोड़ें और GDM को रीस्टार्ट करें)।
    - इंटीग्रेटेड ग्राफिक्स के साथ Ghostty चलाएं: `prime-run --gpu intel ghostty` (अगर जरूरत हो तो `nvidia-prime` इंस्टॉल करें)।
    - यह कुछ उपयोगकर्ताओं के लिए NVIDIA X11 समस्याओं को बायपास करता है।

2.  **Snap के माध्यम से इंस्टॉल करें (आसान वैकल्पिक पैकेज)**:
    - आपके द्वारा उपयोग किए गए अनौपचारिक `.deb` में सिस्टम की खामियां आ सकती हैं। आधिकारिक Snap को आजमाएं, जो डिपेंडेंसीज़ को बंडल करता है:
      ```
      sudo snap install ghostty --classic
      ```
    - `snap run ghostty` से लॉन्च करें। अगर OpenGL अभी भी फेल होता है, तो अपग्रेड के लिए आगे बढ़ें।

3.  **Ubuntu को 24.04 में अपग्रेड करें (लॉन्ग-टर्म फिक्स के लिए सुझाया गया)**:
    - Ubuntu 24.04 में GTK 4.14+ शामिल है, जो NVIDIA अनुकूलता को हल करता है।
    - आधिकारिक अपग्रेड गाइड का पालन करें: `sudo do-release-upgrade`।
    - अपग्रेड करने के बाद, उसी `.deb` या Snap के माध्यम से Ghostty को फिर से इंस्टॉल करें। उपयोगकर्ता बताते हैं कि अपग्रेड के बाद यह बिना किसी समस्या के काम करता है।

4.  **GLFW बैकएंड के साथ सोर्स से बिल्ड करें (अस्थायी वर्कअराउंड)**:
    - यह OpenGL समस्या को बायपास करने के लिए एक नॉन-GTK रनटाइम का उपयोग करता है (नोट: इसमें टैब्स की कमी है, केवल टेस्टिंग के लिए)।
      ```
      sudo apt install git zig libgtk-4-dev libadwaita-1-dev libharfbuzz-dev libpango1.0-dev libcairo2-dev libgdk-pixbuf-2.0-dev libglib2.0-dev libwayland-dev libxkbcommon-dev libinput-dev libudev-dev libseat-dev libpipewire-0.3-dev libsystemd-dev libx11-dev libxext-dev libxfixes-dev libxi-dev libxrandr-dev libxtst-dev libxdamage-dev libxcomposite-dev libxrender-dev libxcursor-dev libxinerama-dev libxss-dev libxv-dev libxxf86vm-dev libgl1-mesa-dev libegl1-mesa-dev libgles2-mesa-dev libgbm-dev libdrm-dev libvulkan-dev libclang-dev
      git clone https://github.com/ghostty-org/ghostty.git
      cd ghostty
      zig build -Doptimize=ReleaseFast -Dapp-runtime=glfw
      sudo cp zig-out/bin/ghostty /usr/local/bin/
      ```
    - `ghostty` चलाएं। पूरी सुविधाओं के लिए, एक बार अपग्रेड होने के बाद वापस GTK पर स्विच करें।

### अतिरिक्त सुझाव
- अपने NVIDIA ड्राइवरों को अपडेट करें: `sudo ubuntu-drivers autoinstall` (या मैन्युअल रूप से 550+ सीरीज़ का उपयोग करें)।
- अगर आप केवल AMD/Intel पर हैं, तो सुनिश्चित करें कि Mesa अपडेटेड है: `sudo apt update && sudo apt upgrade mesa-vulkan-drivers`।
- आपकी टेम्पलेट फ़ाइल (`~/.config/ghostty/config`) में कॉन्फ़िग चेतावनी के लिए, किसी भी अमान्य लाइन (जैसे, अलग `.`) को हटाने के लिए इसे एडिट करें।

अगर इनमें से कोई भी काम नहीं करता है, तो अधिक विशिष्ट सलाह के लिए अपना `glxinfo` आउटपुट या GPU विवरण (`lspci | grep VGA`) साझा करें।

[OpenGL Too Old Discussion](https://github.com/ghostty-org/ghostty/discussions/3159)  
[Ghostty Ubuntu Builds](https://github.com/mkasberg/ghostty-ubuntu)  
[Ghostty Snap](https://snapcraft.io/ghostty)