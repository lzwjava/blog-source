---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: उबुन्टू पर वेज़टर्म इंस्टॉल करना
translated: true
type: note
---

त्रुटि "Unable to locate package wezterm" इसलिए होती है क्योंकि WezTerm Ubuntu के डिफ़ॉल्ट रिपॉजिटरी में उपलब्ध नहीं है। आपको पहले आधिकारिक थर्ड-पार्टी रिपॉजिटरी को जोड़ना होगा। यहां एपीटी विधि (सहज एकीकरण के लिए अनुशंसित) का उपयोग करके चरण-दर-चरण समाधान दिया गया है:

1. रिपॉजिटरी के लिए GPG कुंजी जोड़ें:  
   ```
   curl -fsSL https://apt.fury.io/wez/gpg.key | sudo gpg --yes --dearmor -o /usr/share/keyrings/wezterm-fury.gpg
   ```

2. आपके स्रोतों में रिपॉजिटरी जोड़ें:  
   ```
   echo 'deb [signed-by=/usr/share/keyrings/wezterm-fury.gpg] https://apt.fury.io/wez/ * *' | sudo tee /etc/apt/sources.list.d/wezterm.list
   ```

3. कुंजी फ़ाइल पर सही अनुमतियाँ सेट करें:  
   ```
   sudo chmod 644 /usr/share/keyrings/wezterm-fury.gpg
   ```

4. अपनी पैकेज सूची अपडेट करें:  
   ```
   sudo apt update
   ```

5. अब WezTerm इंस्टॉल करें:  
   ```
   sudo apt install wezterm
   ```

एक बार इंस्टॉल हो जाने के बाद, आप इसे टर्मिनल से `wezterm` कमांड से चला सकते हैं। यदि आप नाइटली (ब्लीडिंग-एज) वर्जन चाहते हैं, तो चरण 5 में `sudo apt install wezterm-nightly` का उपयोग करें—लेकिन ध्यान दें कि यह स्टेबल वर्जन के साथ एक साथ नहीं चल सकता।

### विकल्प: Flatpak (रिपो की आवश्यकता नहीं)
यदि आप एपीटी स्रोतों को संशोधित किए बिना सैंडबॉक्स्ड इंस्टॉलेशन पसंद करते हैं:  
1. Flatpak इंस्टॉल करें यदि पहले से मौजूद नहीं है: `sudo apt install flatpak`।  
2. Flathub जोड़ें: `flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo`।  
3. इंस्टॉल करें: `flatpak install flathub org.wezfurlong.wezterm`।  
4. चलाएँ: `flatpak run org.wezfurlong.wezterm` (या एक उपनाम जोड़ें: `alias wezterm='flatpak run org.wezfurlong.wezterm'`)।  

Flatpak अलग-थलग है, इसलिए यह कुछ उन्नत सुविधाओं को सीमित कर सकता है, लेकिन परीक्षण के लिए यह सरल है।

[WezTerm Linux Installation Guide](https://wezterm.org/install/linux.html)