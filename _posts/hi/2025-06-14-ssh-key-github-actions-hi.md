---
audio: false
generated: true
lang: hi
layout: post
title: GitHub Actions JAR डिप्लॉयमेंट के लिए SSH कुंजी सेटअप
translated: true
type: note
---

GitHub Actions के माध्यम से JAR फ़ाइल डिप्लॉय करने के लिए SSH कुंजी जनरेट करने के लिए, इन चरणों का पालन करें:

1. **SSH कुंजी जोड़ी जनरेट करें**:
   - अपने लोकल मशीन या सुरक्षित वातावरण में, यह चलाएँ:
     ```bash
     ssh-keygen -t ed25519 -C "your_email@example.com" -f github-actions-deploy
     ```
   - यदि आपका सिस्टम Ed25519 को सपोर्ट नहीं करता है, तो यह उपयोग करें:
     ```bash
     ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f github-actions-deploy
     ```
   - डिफ़ॉल्ट फ़ाइल लोकेशन को स्वीकार करने के लिए Enter दबाएँ और वैकल्पिक रूप से एक पासफ़्रेज़ सेट करें (सुरक्षा के लिए अनुशंसित)। यह दो फ़ाइलें बनाता है:
     - `github-actions-deploy` (प्राइवेट कुंजी)
     - `github-actions-deploy.pub` (पब्लिक कुंजी)

2. **पब्लिक कुंजी को टार्गेट सर्वर में जोड़ें**:
   - पब्लिक कुंजी को कॉपी करें:
     ```bash
     cat github-actions-deploy.pub
     ```
   - उस सर्वर में लॉग इन करें जहाँ आप JAR फ़ाइल डिप्लॉय करेंगे।
   - सर्वर पर `~/.ssh/authorized_keys` फ़ाइल में पब्लिक कुंजी को जोड़ें:
     ```bash
     echo "your-public-key-content" >> ~/.ssh/authorized_keys
     ```
   - सुनिश्चित करें कि `authorized_keys` फ़ाइल की परमिशन सही हैं:
     ```bash
     chmod 600 ~/.ssh/authorized_keys
     ```

3. **प्राइवेट कुंजी को GitHub Secrets में स्टोर करें**:
   - अपने GitHub रिपॉजिटरी में जाएँ: `Settings > Secrets and variables > Actions > Secrets`.
   - **New repository secret** पर क्लिक करें।
   - सीक्रेट का नाम दें (उदाहरण के लिए, `SSH_PRIVATE_KEY`)।
   - प्राइवेट कुंजी (`github-actions-deploy`) की सामग्री को पेस्ट करें:
     ```bash
     cat github-actions-deploy
     ```
   - सीक्रेट को सेव करें।

4. **GitHub Actions वर्कफ़्लो को कॉन्फ़िगर करें**:
   - एक वर्कफ़्लो फ़ाइल बनाएँ या एडिट करें (उदाहरण के लिए, `.github/workflows/deploy.yml`)।
   - JAR को डिप्लॉय करने के लिए SSH कुंजी का उपयोग करने के लिए एक स्टेप जोड़ें। नीचे एक उदाहरण वर्कफ़्लो है:

     ```yaml
     name: Deploy JAR

     on:
       push:
         branches:
           - main

     jobs:
       deploy:
         runs-on: ubuntu-latest

         steps:
         - name: Checkout code
           uses: actions/checkout@v4

         - name: Set up Java
           uses: actions/setup-java@v4
           with:
             java-version: '17' # अपने Java वर्जन के अनुसार एडजस्ट करें
             distribution: 'temurin'

         - name: Build JAR
           run: mvn clean package # अपने बिल्ड टूल (जैसे Gradle) के लिए एडजस्ट करें

         - name: Install SSH Key
           uses: shimataro/ssh-key-action@v2
           with:
             key: ${{ secrets.SSH_PRIVATE_KEY }}
             known_hosts: 'optional-known-hosts' # नीचे नोट देखें

         - name: Add Known Hosts
           run: |
             ssh-keyscan -H <server-ip-or-hostname> >> ~/.ssh/known_hosts
           # <server-ip-or-hostname> को अपने सर्वर के IP या होस्टनेम से रिप्लेस करें

         - name: Deploy JAR to Server
           run: |
             scp target/your-app.jar user@<server-ip-or-hostname>:/path/to/deploy/
             ssh user@<server-ip-or-hostname> "sudo systemctl restart your-service" # अपने डिप्लॉयमेंट प्रोसेस के लिए एडजस्ट करें
     ```

   - **नोट्स**:
     - `target/your-app.jar` को अपनी JAR फ़ाइल के पथ से रिप्लेस करें।
     - `user@<server-ip-or-hostname>` को अपने सर्वर के SSH यूज़र और एड्रेस से रिप्लेस करें।
     - डिप्लॉयमेंट कमांड (जैसे, `sudo systemctl restart your-service`) को एडजस्ट करें ताकि यह मेल खाए कि आप अपने सर्वर पर JAR को कैसे स्टार्ट या डिप्लॉय करते हैं।
     - SSH होस्ट वेरिफिकेशन इश्यू से बचने के लिए `known_hosts` स्टेप महत्वपूर्ण है। यदि आप सर्वर की होस्ट कुंजी जानते हैं, तो आप इसे `shimataro/ssh-key-action` स्टेप में पहले से पॉपुलेट कर सकते हैं, या जैसा दिखाया गया है `ssh-keyscan` का उपयोग कर सकते हैं।

5. **वर्कफ़्लो को सुरक्षित करें**:
   - सुनिश्चित करें कि प्राइवेट कुंजी लॉग्स या आउटपुट में कभी एक्सपोज़ न हो।
   - सीक्रेट्स के लिए अनधिकृत एक्सेस को रोकने के लिए रिपॉजिटरी परमिशन को रिस्ट्रिक्ट करें।
   - यदि SSH कुंजी के लिए पासफ़्रेज़ का उपयोग कर रहे हैं, तो इसे एक और सीक्रेट के रूप में जोड़ें और इसे `shimataro/ssh-key-action` स्टेप में शामिल करें:
     ```yaml
     with:
       key: ${{ secrets.SSH_PRIVATE_KEY }}
       passphrase: ${{ secrets.SSH_KEY_PASSPHRASE }}
       known_hosts: 'optional-known-hosts'
     ```

6. **वर्कफ़्लो का टेस्ट करें**:
   - `main` ब्रांच (या वर्कफ़्लो में निर्दिष्ट ब्रांच) में एक बदलाव पुश करें।
   - यह सुनिश्चित करने के लिए अपनी GitHub रिपॉजिटरी के **Actions** टैब में वर्कफ़्लो की मॉनिटरिंग करें कि JAR सही तरीके से बिल्ड और डिप्लॉय हो रहा है।

7. **समस्या निवारण**:
   - **Permission denied**: सत्यापित करें कि SSH कुंजी सर्वर के `authorized_keys` में सही तरीके से जोड़ी गई है और यूज़र के पास टार्गेट डायरेक्टरी तक पहुँच की परमिशन है।
   - **Host verification failed**: सुनिश्चित करें कि `known_hosts` स्टेप सर्वर के IP या होस्टनेम के साथ सही तरीके से कॉन्फ़िगर किया गया है।
   - **Build issues**: पुष्टि करें कि Java वर्जन और बिल्ड कमांड आपके प्रोजेक्ट सेटअप से मेल खाते हैं।

यह सेटअप आपके GitHub Actions वर्कफ़्लो में JAR फ़ाइल को डिप्लॉय करने के लिए SSH-आधारित डिप्लॉयमेंट को सुरक्षित रूप से एकीकृत करता है। यदि आपको विशिष्ट एडजस्टमेंट की आवश्यकता है (जैसे, किसी विशेष सर्वर सेटअप या बिल्ड टूल के लिए), तो मुझे बताएं!