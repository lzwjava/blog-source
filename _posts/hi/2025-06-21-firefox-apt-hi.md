---
audio: false
generated: true
lang: hi
layout: post
title: यूबंटू पर एपीटी के माध्यम से फ़ायरफ़ॉक्स स्थापित करना
translated: true
type: note
---

यह गाइड Ubuntu पर Mozilla APT रिपॉजिटरी से Firefox को इंस्टॉल करने का विवरण देती है, जो डिफ़ॉल्ट Snap पैकेज को प्रतिस्थापित करती है।

**APT वर्जन का उपयोग क्यों करें?**

Snap वर्जन सुविधाजनक है, लेकिन कुछ उपयोगकर्ता बेहतर एकीकरण और प्रदर्शन के लिए APT वर्जन पसंद करते हैं।

**चरण:**

1.  **Firefox Snap को अनइंस्टॉल करें:**

    ```bash
    sudo snap remove firefox
    ```

2.  **एक APT कीरिंग डायरेक्टरी बनाएँ (अगर यह मौजूद नहीं है):**

    ```bash
    sudo install -d -m 0755 /etc/apt/keyrings
    ```

3.  **Mozilla APT रिपो साइनिंग की को इम्पोर्ट करें:**

    ```bash
    wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null
    ```
    *अगर `wget` मौजूद नहीं है, तो पहले इसे इंस्टॉल करें: `sudo apt install wget`*

4.  **अपनी सोर्सेस लिस्ट में Mozilla रिपॉजिटरी को जोड़ें:**

    ```bash
    echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null
    ```

5.  **Mozilla DEB को प्राथमिकता देने के लिए पैकेज प्राथमिकता सेट करें:**

    यह Ubuntu के ट्रांज़िशन पैकेज को Snap को दोबारा इंस्टॉल करने से रोकता है।

    ```bash
    echo '
    Package: *
    Pin: origin packages.mozilla.org
    Pin-Priority: 1000

    Package: firefox*
    Pin: release o=Ubuntu
    Pin-Priority: -1' | sudo tee /etc/apt/preferences.d/mozilla
    ```

6.  **Ubuntu Firefox DEB को हटाएँ (अगर मौजूद हो) और Mozilla वर्जन इंस्टॉल करें:**

    ```bash
    sudo apt update && sudo apt remove firefox
    sudo apt install firefox
    ```

अब आपके पास आधिकारिक Mozilla APT रिपॉजिटरी से इंस्टॉल किया गया Firefox है!