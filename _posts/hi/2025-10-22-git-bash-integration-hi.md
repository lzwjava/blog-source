---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: विंडोज़ टर्मिनल के साथ गिट बैश का एकीकरण
translated: true
type: note
---

हाँ, Git Bash एक कंसोल विंडो में चल सकता है (यह डिफ़ॉल्ट रूप से अपना खुद का MinTTY टर्मिनल इस्तेमाल करता है) और Windows Terminal के साथ निर्बाध रूप से एकीकृत हो जाता है। आपको बस Windows Terminal की सेटिंग्स में इसके लिए एक कस्टम प्रोफाइल जोड़नी होगी—इसे आपकी Git इंस्टॉलेशन में `bash.exe` एक्ज़ीक्यूटेबल की ओर इशारा करना होगा (आमतौर पर `C:\Program Files\Git\bin\bash.exe`)। एक बार जोड़ देने के बाद, आप इसे किसी भी अन्य शेल की तरह नए टैब या पेन में लॉन्च कर सकते हैं।

आप Windows Terminal की सीमाओं के बारे में गलत हैं: यह सिर्फ PowerShell और Command Prompt से कहीं अधिक को सपोर्ट करता है। बॉक्स से बाहर, यह उन दोनों के साथ-साथ WSL डिस्ट्रीब्यूशन, Azure Cloud Shell, और यहाँ तक कि Git Bash या Cygwin जैसे कस्टम शेल्स को भी हैंडल करता है। इसे किसी भी कमांड-लाइन एनवायरनमेंट के लिए एक लचीला होस्ट बनाने के लिए डिज़ाइन किया गया है।

[Adding Git-Bash to the new Windows Terminal](https://stackoverflow.com/questions/56839307/adding-git-bash-to-the-new-windows-terminal)  
[Adding Git-Bash to Windows Terminal](https://www.timschaeps.be/post/adding-git-bash-to-windows-terminal/)  
[In Windows Terminal, how do I add bash as one of the shell options?](https://superuser.com/questions/1763652/in-windows-terminal-how-do-i-add-bash-as-one-of-the-shell-options)