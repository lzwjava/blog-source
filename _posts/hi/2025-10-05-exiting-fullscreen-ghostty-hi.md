---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: गोस्टी में पूर्ण स्क्रीन से बाहर निकलना
translated: true
type: note
---

उबंटू पर Ghostty टर्मिनल में फुल-स्क्रीन मोड से बाहर निकलने के लिए, **Ctrl + Enter** दबाएं। यह फुल-स्क्रीन को चालू/बंद करने के लिए डिफ़ॉल्ट कीबाइंडिंग है।

यदि यह काम नहीं करता है (उदाहरण के लिए, कस्टम कॉन्फ़िग के कारण), इन विकल्पों को आज़माएं:
- टर्मिनल विंडो के अंदर राइट-क्लिक करें और कॉन्टेक्स्ट मेनू में "Leave Fullscreen" या इसी तरह का विकल्प ढूंढें।
- मेनू बार का उपयोग करें यदि दिख रहा हो: **View > Leave Fullscreen** पर जाएं (इसे प्रकट करने के लिए आपको स्क्रीन के शीर्ष पर होवर करने की आवश्यकता हो सकती है)।
- अंतिम उपाय के रूप में, Ghostty को दूसरे टर्मिनल में `ghostty` कमांड से बंद करके फिर से खोलें, या प्रक्रिया को `pkill ghostty` के माध्यम से समाप्त करके पुनः लॉन्च करें।

[ghostty-shortcuts.md](https://gist.github.com/hensg/43bc71c21d1f79385892352a390aa2ca)  
[Keybindings for Midnight Commander (Reddit)](https://www.reddit.com/r/Ghostty/comments/1lfxvsf/keybindings_for_midnight_commander/)