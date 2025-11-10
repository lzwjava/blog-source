---
audio: false
generated: true
lang: hi
layout: post
title: उबुन्टू में फ़ाइल का पूरा पथ प्राप्त करना
translated: true
type: note
---

उबंटू में, आप `realpath` या `readlink -f` कमांड का उपयोग करके किसी फ़ाइल का पूरा पथ प्राप्त कर सकते हैं। आपके `geckodriver` वाले उदाहरण के लिए, आप यह चला सकते हैं:

```bash
realpath ./geckodriver
```

या

```bash
readlink -f ./geckodriver
```

दोनों ही पूरा पथ आउटपुट करेंगे, उदाहरण के लिए:

```
/home/lzw/bin/geckodriver
```

`realpath` कमांड सीधा-सादा है और आमतौर पर इसी काम के लिए इस्तेमाल किया जाता है। यदि `realpath` इंस्टॉल नहीं है, तो आप इसे यह चलाकर इंस्टॉल कर सकते हैं:

```bash
sudo apt install realpath
```

वैकल्पिक रूप से, `readlink -f` आमतौर पर डिफ़ॉल्ट रूप से coreutils के हिस्से के रूप में उपलब्ध होता है।