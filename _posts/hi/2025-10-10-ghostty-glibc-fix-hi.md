---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: घोस्टटी जीएलआईबीसी संस्करण विरोधाभास का समाधान
translated: true
type: note
---

आपको जो समस्या आ रही है, वह सिर्फ conflicting installations के कारण नहीं है—मुख्य समस्या यह है कि Snap और आपके द्वारा डाउनलोड किए गए `.deb` दोनों ही GLIBC 2.38 (Ubuntu 24.04 से) के खिलाफ बनाए गए हैं, लेकिन आपका सिस्टम Ubuntu 22.04 पर है (आपके `libc-bin` पैकेज में GLIBC संस्करण 2.35 के आधार पर)। इससे बाइनरी को चलाने का प्रयास करते समय "version `GLIBC_2.38' not found" error आता है। दोनों इंस्टॉलेशन के सक्रिय होने से path conflicts भी हो सकते हैं (जैसे, कौन सी `ghostty` बाइनरी execute होती है), इसलिए हाँ, चीजों को साफ करने के लिए आपको पहले उन्हें हटा देना चाहिए।

### चरण 1: मौजूदा इंस्टॉलेशन हटाएं
दोनों को अनइंस्टॉल करने के लिए ये कमांड चलाएं:
```
sudo snap remove ghostty
sudo apt remove ghostty
```
- यह Snap version और `.deb` version को आपके सिस्टम को प्रभावित किए बिना हटा देगा।
- हटाने की पुष्टि `which ghostty` (कुछ नहीं return करना चाहिए) और `snap list | grep ghostty` (खाली होना चाहिए) से करें।

### चरण 2: एक Compatible Version इंस्टॉल करें
Ghostty के पास अभी तक Ubuntu 22.04 के लिए official `.deb` पैकेज नहीं हैं, लेकिन एक विश्वसनीय unofficial repository है जो इसके लिए (और अन्य versions के लिए) compatible `.deb` फाइलें बनाती है। यह GLIBC compatibility को स्वचालित रूप से संभालती है।

सबसे आसान तरीका है उनके automatic installer script का उपयोग करना, जो आपके Ubuntu version का पता लगाता है और सही पैकेज ले आता है:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/mkasberg/ghostty-ubuntu/HEAD/install.sh)"
```
- यह नवीनतम compatible `.deb` (हाल की रिलीज के अनुसार वर्तमान में लगभग v1.2.x) को डाउनलोड और इंस्टॉल करता है।
- समाप्त होने के बाद, `ghostty` चलाकर परीक्षण करें—यह GLIBC error के बिना लॉन्च होना चाहिए।
- यदि इंस्टॉल के दौरान आपको कोई dependency prompts दिखाई दे (जैसे, `libonig5` के लिए), तो उन्हें `Y` से स्वीकार कर दें।

यदि आप manual installation पसंद करते हैं:
1. [releases page](https://github.com/mkasberg/ghostty-ubuntu/releases) पर जाएं।
2. Ubuntu 22.04 के लिए लेबल वाली `.deb` फाइल डाउनलोड करें (जैसे, `ghostty_1.2.1-0.ppa1_amd64_22.04.deb` जैसा कुछ—सटीक नाम रिलीज के अनुसार अलग हो सकता है)।
3. इसे `sudo dpkg -i ghostty_*.deb` (download folder से चलाएं) के साथ इंस्टॉल करें।
4. यदि यह missing dependencies के बारे में शिकायत करता है, तो `sudo apt install -f` से ठीक करें।

### अतिरिक्त नोट्स
- **Why build from source isn't needed here**: Unofficial repo आपके लिए सारा भारी काम कर देती है, लेकिन यदि आप Ghostty को स्वयं build करना चाहते हैं (जैसे, custom version के लिए), तो [official source build guide](https://ghostty.org/docs/install/build) का पालन करें। इसके लिए Zig 0.13 और कुछ deps जैसे `libgtk-4-dev` की आवश्यकता होती है, लेकिन `.deb` रास्ता सरल है।
- **Upgrading Ubuntu?** यदि आप इसके लिए तैयार हैं, तो 24.04 पर जाने से आप बिना किसी समस्या के official Snap या आपके द्वारा पहले try किए गए 24.04 `.deb` का उपयोग कर पाएंगे।
- इंस्टॉल के बाद, आप `~/.config/ghostty/config` के माध्यम से Ghostty को configure कर सकते हैं (विकल्पों के लिए [docs](https://ghostty.org/docs/config) देखें)।

यदि इन चरणों के दौरान आपको कोई errors आती हैं, तो अधिक सहायता के लिए output यहाँ paste करें!