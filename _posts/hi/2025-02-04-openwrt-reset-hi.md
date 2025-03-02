---
audio: true
generated: false
lang: hi
layout: post
title: OpenWrt रीसेट
translated: true
---

## वेब इंटरफ़ेस के द्वारा रीसेट करना

इसे राउटर से ईथरनेट केबल द्वारा कनेक्ट करने की सलाह दी जाती है। रीसेट के बाद, वाई-फाई SSID अपनी डिफ़ॉल्ट सेटिंग्स पर वापस आ जाएगा, जो आपकी अपेक्षा के अनुरूप नहीं हो सकता है।

## कमांड लाइन (SSH) के द्वारा रीसेट करना

आप कमांड लाइन इंटरफ़ेस (SSH) का उपयोग करके OpenWrt को उसकी डिफ़ॉल्ट सेटिंग्स पर रीसेट कर सकते हैं।  यहाँ बताया गया है कैसे:

1. SSH के द्वारा अपने OpenWrt राउटर से कनेक्ट करें।
2. निम्न कमांड चलाएँ:

    ```bash
    root@OpenWrt:~# firstboot
    This will erase all settings and remove any installed packages. Are you sure? [N/y]
    y
    /dev/ubi0_1 is mounted as /overlay, only erasing files
    root@OpenWrt:~# reboot
    ```
3. राउटर डिफ़ॉल्ट सेटिंग्स के साथ रिबूट होगा।

**कमांड्स की व्याख्या:**

*   `firstboot`: यह कमांड रीसेट प्रक्रिया शुरू करता है, सभी कॉन्फ़िगरेशन और इंस्टॉल किए गए पैकेजों को मिटा देता है।
*   `reboot`: यह कमांड राउटर को पुनः प्रारंभ करता है, रीसेट को लागू करता है।
