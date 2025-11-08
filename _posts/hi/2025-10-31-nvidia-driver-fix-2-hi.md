---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: एनवीडिया ड्राइवर पैकेज संघर्ष को ठीक करना
translated: true
type: note
---

यह Ubuntu (पैकेज वर्ज़न के आधार पर संभवतः 22.04) पर NVIDIA ड्राइवर अपडेट के दौरान एक क्लासिक पैकेज कॉन्फ्लिक्ट जैसा दिख रहा है। `nvidia-kernel-common-535` पैकेज एक फर्मवेयर फ़ाइल (`gsp_ga10x.bin`) को ओवरराइट करने की कोशिश कर रहा है जो पहले से ही `nvidia-firmware-535` के स्वामित्व में है, जिसके कारण dpkg एरर दे रहा है। यह Ubuntu रिपॉजिटरीज के NVIDIA 535-सीरीज़ ड्राइवर्स के साथ एक ज्ञात समस्या है।

घबराएं नहीं—आपकी सिस्टम अभी भी बूट होनी चाहिए (हालांकि अगर ड्राइवर आंशिक रूप से टूट गया है तो ग्राफिक्स सॉफ्टवेयर रेंडरिंग मोड में हो सकते हैं)। इसे सुरक्षित रूप से ठीक करने के लिए यहां चरण-दर-चरण समाधान दिया गया है। इन्हें टर्मिनल में चलाएं (अगर GUI अस्थिर है तो TTY का उपयोग करें: स्विच करने के लिए Ctrl+Alt+F3 दबाएं)।

### त्वरित समाधान प्रयास (पहले सबसे सुरक्षित)
1. टूटे हुए पैकेजों को स्वचालित रूप से ठीक करने का प्रयास करें:
   ```
   sudo apt --fix-broken install
   ```
   यह अक्सर मैन्युअल हस्तक्षेप के बिना ही डिपेंडेंसी/अनपैक समस्याओं को हल कर देता है।

2. अगर यह विफल हो जाता है (या आंशिक रूप से सफल होता है लेकिन एरर छोड़ देता है), तो बीच में रुकी इंस्टॉलेशन को साफ करें:
   ```
   sudo dpkg --configure -a
   sudo apt update
   sudo apt upgrade
   ```

### यदि अभी भी अटका हुआ है: कॉन्फ्लिक्ट करने वाली फ़ाइल को फोर्स ओवरराइट करें
एरर विशेष रूप से `nvidia-kernel-common-535` डेब फ़ाइल पर है। डुप्लिकेट फ़ाइल कॉन्फ्लिक्ट को नजरअंदाज करते हुए dpkg को फोर्स करें:
```
sudo dpkg -i --force-overwrite /var/cache/apt/archives/nvidia-kernel-common-535_535.274.02-0ubuntu1_amd64.deb
```
- यह सिर्फ उस पैकेज को इंस्टॉल करता है, फ़ाइल कॉन्फ्लिक्ट को नजरअंदाज करते हुए।
- फिर चलाएं:
  ```
  sudo apt --fix-broken install
  sudo apt autoremove
  sudo apt upgrade
  ```
- इसके बाद रीबूट करें: `sudo reboot`।

### अंतिम विकल्प: NVIDIA पैकेजों को पर्ज और रीइंस्टॉल करें
यदि उपरोक्त काम नहीं करता है (उदाहरण के लिए, गहरा वर्ज़न मिसमैच), तो कॉन्फ्लिक्ट कर रहे NVIDIA पैकेजों को हटाकर दोबारा इंस्टॉल करें:
1. समस्या वाले पैकेजों को पर्ज करें (अगर ज़रूरत हो तो वर्ज़न अडैप्ट करें—`dpkg -l | grep nvidia` से चेक करें):
   ```
   sudo dpkg --force-all -P nvidia-firmware-535-535.274.02 nvidia-kernel-common-535
   ```
2. क्लीन अप करें:
   ```
   sudo apt autoremove --purge
   sudo apt autoclean
   ```
3. ड्राइवर को दोबारा इंस्टॉल करें:
   ```
   sudo apt update
   sudo apt install nvidia-driver-535
   ```
4. रीबूट करें।

### रोकथाम/सुझाव
- अधिक स्थिर NVIDIA अपडेट्स के लिए graphics-drivers PPA जोड़ें: `sudo add-apt-repository ppa:graphics-drivers/ppa && sudo apt update`।
- अगर आप लैपटॉप पर हैं, तो ड्राइवर इंस्टॉलेशन से पहले BIOS में Secure Boot अक्षम करना सुनिश्चित करें।
- रीबूट के बाद `nvidia-smi` (आपकी GPU दिखानी चाहिए) या `prime-select query` (अगर NVIDIA Optimus है) से टेस्ट करें।
- अगर इससे आपकी डिस्प्ले पूरी तरह से टूट जाती है, तो रिकवरी मोड में बूट करें और वहां से फिक्सेस चलाएं।

अगर इनमें से कुछ भी काम नहीं करता है या आपको कोई नया एरर मिलता है, तो पूरा आउटपुट यहां पेस्ट करें ताकि और समाधान सुझाए जा सकें।

### संदर्भ
- [Unmet dependencies nvidia-dkms-535 - package conflict breaks Ubuntu 22.04 install](https://forums.developer.nvidia.com/t/unmet-dependencies-nvidia-dkms-535-package-conflict-breaks-ubuntu-22-04-install/265788)
- [Ubuntu and NVIDIA-provided packages conflict, breaking installation](https://forums.developer.nvidia.com/t/ubuntu-and-nvidia-provided-packages-conflict-breaking-installation/259150)
- [Problem with nvidia package dependencies](https://askubuntu.com/questions/1491916/problem-with-nvidia-package-dependencies)
- [nvidia-kernel-common-535 conflicts with nvidia-firmware-535](https://superuser.com/questions/1833427/nvidia-kernel-common-535-conflicts-with-nvidia-firmware-535-535-161-07-535-161-0)