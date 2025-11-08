---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: ट्रेसरूट डिफ़ॉल्ट रूप से इंस्टॉल नहीं है
translated: true
type: note
---

Traceroute निश्चित रूप से Linux पर उपलब्ध है - यह एक मानक नेटवर्क डायग्नोस्टिक टूल है जो पैकेट्स के गंतव्य तक पहुँचने के मार्ग को ट्रैक करता है। हालाँकि, आधार सिस्टम को हल्का रखने के लिए यह अक्सर **कई आधुनिक डिस्ट्रीब्यूशन (जैसे Ubuntu, Fedora, या Debian मिनिमल इंस्टॉल) में डिफ़ॉल्ट रूप से इंस्टॉल नहीं होता**। इसीलिए यह "trac" के लिए आपकी टैब कम्पलीशन में दिखाई नहीं दे रहा है।

### त्वरित समाधान
इसे अपने पैकेज मैनेजर के माध्यम से इंस्टॉल करें:
- **Debian/Ubuntu**: `sudo apt update && sudo apt install traceroute`
- **Fedora/RHEL/CentOS**: `sudo dnf install traceroute` (या पुराने वर्जन पर `sudo yum install traceroute`)
- **Arch**: `sudo pacman -S traceroute`

एक बार इंस्टॉल हो जाने पर, `trac` + Tab टाइप करने पर अब `traceroute` सूची में शामिल होगा। फिर आप टेस्ट करने के लिए इसे `traceroute example.com` की तरह चला सकते हैं।

यदि आप कंटेनराइज्ड या सुपर-मिनिमल सेटअप (जैसे, Alpine Linux) पर हैं, तो यह `tr` को एलियास के रूप में उपयोग कर सकता है या किसी अलग पैकेज की आवश्यकता हो सकती है—अधिक जानकारी के लिए मुझे अपना डिस्ट्रो बताएं!