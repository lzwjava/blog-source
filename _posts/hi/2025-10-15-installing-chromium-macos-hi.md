---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: मैकओएस पर क्रोमियम स्थापित करना
translated: true
type: note
---

हां, macOS निश्चित रूप से Google Chrome के विकल्प के रूप में Chromium इंस्टॉल कर सकता है। Chromium वह ओपन-सोर्स आधार है जिस पर Chrome बनाया गया है, इसलिए यह कार्यक्षमता में बहुत समान है लेकिन इसमें स्वचालित अपडेट और कुछ कोडेक्स जैसी कुछ मालिकाना Google सुविधाओं का अभाव है।

### इसे कैसे इंस्टॉल करें
इसके कुछ सीधे तरीके हैं:

1. **Homebrew के माध्यम से (अधिकांश उपयोगकर्ताओं के लिए सबसे आसान)**:
   - यदि आपने पहले से इंस्टॉल नहीं किया है तो Homebrew इंस्टॉल करें: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
   - फिर चलाएं: `brew install --cask chromium`
   - यह Intel और Apple Silicon (M1/M2/M3) दोनों Macs पर काम करता है।

2. **सीधा डाउनलोड**:
   - आधिकारिक Chromium साइट पर जाएं और Mac के लिए नवीनतम बिल्ड डाउनलोड करें।
   - अनज़िप करें और ऐप को अपने Applications फ़ोल्डर में खींच कर छोड़ें।

3. **डेवलपर्स या कस्टम बिल्ड के लिए**:
   - प्री-बिल्ट रिलीज़ के लिए Woolyss जैसे टूल्स का उपयोग करें, या आवश्यकता होने पर सोर्स से बिल्ड करें (इसके लिए Xcode की आवश्यकता होती है)।

एक बार इंस्टॉल हो जाने के बाद, आप System Settings > Desktop & Dock > Default web browser में Chromium को अपना डिफ़ॉल्ट ब्राउज़र सेट कर सकते हैं।

[Chromium डाउनलोड करें](https://www.chromium.org/getting-involved/download-chromium/)  
[Homebrew Formula](https://formulae.brew.sh/cask/chromium)  
[Apple Silicon पर इंस्टॉलेशन](https://dev.to/pixelrena/installing-chromium-on-mac-apple-m2-pro-tutorial-4i4i)  
[MacUpdate डाउनलोड](https://chromium.macupdate.com/)  
[नवीनतम रिलीज़](https://chromium.woolyss.com/download/en/)