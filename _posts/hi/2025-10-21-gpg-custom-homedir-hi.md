---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: कस्टम होमडायरेक्टरी के साथ जीपीजी का उपयोग
translated: true
type: note
---

### GPG के `--homedir` विकल्प का उपयोग

`--homedir` फ्लैग (नोट: यह `--homedir` है, `--home-dir` नहीं—GPG एक शब्द का उपयोग करता है) GPG को कॉन्फ़िगरेशन फ़ाइलें, कीरिंग, ट्रस्ट डेटाबेस और अन्य डेटा संग्रहीत करने के लिए एक कस्टम डायरेक्टरी को अपना "होम" के रूप में उपयोग करने के लिए कहता है। डिफ़ॉल्ट रूप से, GPG `~/.gnupg` का उपयोग करता है (उदाहरण के लिए, Windows पर Git Bash में `/c/Users/YourName/.gnupg`)। यह विकल्प निम्नलिखित के लिए उपयोगी है:
- एकाधिक GPG सेटअप को अलग करने के लिए (उदाहरण के लिए, एक व्यक्तिगत कुंजियों के लिए, दूसरा काम के लिए)।
- सिस्टम-व्यापी GPG कॉन्फ़िग से टकराव से बचने या परीक्षण करने के लिए।
- GPG को एक पोर्टेबल या कस्टम वातावरण में चलाने के लिए।

#### बेसिक सिंटैक्स
```
gpg --homedir /path/to/custom/dir [other gpg commands]
```
- `/path/to/custom/dir` को अपनी वांछित डायरेक्टरी पथ से बदलें।
- Windows पर Git Bash में, पथ के लिए **हमेशा फॉरवर्ड स्लैश (`/`) का उपयोग करें**, भले ही Windows ड्राइव के लिए हो (उदाहरण के लिए, `/c/Users/YourName/my-gpg-dir`)।
- डायरेक्टरी का अस्तित्व में होना आवश्यक है; GPG इसे स्वचालित रूप से नहीं बनाएगा। पहले `mkdir -p /path/to/custom/dir` से इसे बनाएँ।

#### उदाहरण: कस्टम होम डायरेक्टरी सेट अप करना और उपयोग करना
1. **कस्टम डायरेक्टरी बनाएँ** (Git Bash में):
   ```
   mkdir -p /c/Users/YourName/my-custom-gpg
   ```

2. **कस्टम homedir का उपयोग करके keypair जनरेट करें**:
   ```
   gpg --homedir /c/Users/YourName/my-custom-gpg --full-generate-key
   ```
   - यह आपकी कुंजियों और कॉन्फ़िग को `my-custom-gpg` में संग्रहीत करता है, डिफ़ॉल्ट में नहीं।

3. **उस डायरेक्टरी से keys की सूची बनाएँ**:
   ```
   gpg --homedir /c/Users/YourName/my-custom-gpg --list-secret-keys --keyid-format LONG
   ```

4. **कस्टम डायरेक्टरी से keys का उपयोग करके एक फ़ाइल एन्क्रिप्ट करें**:
   ```
   gpg --homedir /c/Users/YourName/my-custom-gpg --encrypt --recipient RECIPIENT_EMAIL secret.txt
   ```

5. **एक फ़ाइल डिक्रिप्ट करें**:
   ```
   gpg --homedir /c/Users/YourName/my-custom-gpg --output decrypted.txt --decrypt secret.txt.gpg
   ```

#### Windows पर Git Bash के लिए टिप्स
- **पथ:** `/` का ही उपयोग करें—उदाहरण के लिए, `\` या मिश्रित स्लैश से बचें, क्योंकि वे कमांड्स को तोड़ सकते हैं।
- **अनुमतियाँ:** सुनिश्चित करें कि कस्टम डायरेक्टरी में पढ़ने/लिखने की पहुंच हो (सुरक्षा के लिए `chmod 700 /path/to/custom/dir` का उपयोग करें, जैसे डिफ़ॉल्ट `.gnupg`)।
- **एनवायरनमेंट वेरिएबल विकल्प:** हर बार `--homedir` का उपयोग करने के बजाय, अपने `.bashrc` में `export GNUPGHOME=/c/Users/YourName/my-custom-gpg` सेट करें (संपादन के बाद `source ~/.bashrc` चलाएँ)। फिर GPG इसका स्वचालित रूप से उपयोग करेगा।
- **Git इंटीग्रेशन:** यदि Git साइनिंग के लिए उपयोग कर रहे हैं, तो इस फ्लैग के साथ कॉन्फ़िगर करें:
  ```
  git config --global gpg.program "gpg --homedir /c/Users/YourName/my-custom-gpg"
  ```
- **सामान्य समस्याएँ:** यदि GPG गुम फ़ाइलों के बारे में शिकायत करता है, तो हो सकता है कि उसे इनिशियलाइज़ेशन की आवश्यकता हो—पहले `gpg --homedir /path --gen-key` चलाएँ। Windows पर, बिना उद्धरण के रिक्त स्थान वाले पथों से बचें।

पूर्ण विवरण के लिए, GPG मैनुअल देखें: [GnuPG Documentation](https://www.gnupg.org/documentation/manuals/gnupg/)