---
audio: false
generated: true
image: false
lang: hi
layout: post
model: anthropic/claude-sonnet-4
title: लिनक्स पर एक्सडोटूल की स्थापना और उपयोग
translated: true
type: note
---

`xdotool` को अपने Linux सिस्टम पर इंस्टॉल करने के लिए, आप अपने डिस्ट्रीब्यूशन के पैकेज मैनेजर का उपयोग कर सकते हैं। आपके होस्टनाम में "XiaoXin" दिखने के आधार पर, संभावना है कि आप Ubuntu या Debian-आधारित डिस्ट्रीब्यूशन का उपयोग कर रहे हैं। यहाँ सामान्य Linux डिस्ट्रीब्यूशन के लिए इंस्टॉलेशन कमांड दी गई हैं:

## Ubuntu/Debian:
```bash
sudo apt update
sudo apt install xdotool
```

## CentOS/RHEL/Fedora:
```bash
# नए वर्जन के लिए (dnf)
sudo dnf install xdotool

# पुराने वर्जन के लिए (yum)
sudo yum install xdotool
```

## Arch Linux:
```bash
sudo pacman -S xdotool
```

## openSUSE:
```bash
sudo zypper install xdotool
```

इंस्टॉलेशन के बाद, आप यह चलाकर सत्यापित कर सकते हैं कि यह काम कर रहा है:
```bash
xdotool --version
```

एक बार इंस्टॉल हो जाने के बाद, आपका Python स्क्रिप्ट ब्राउज़र टाइटल प्राप्त करने के लिए `xdotool` का उपयोग करने में सक्षम होना चाहिए। `xdotool` यूटिलिटी आमतौर पर X11 डेस्कटॉप कार्यों को स्वचालित करने के लिए उपयोग की जाती है, जिसमें विंडो टाइटल प्राप्त करना भी शामिल है, जो आपकी स्क्रिप्ट करने का प्रयास कर रही प्रतीत होती है।

यदि इंस्टॉलेशन के बाद भी आपको समस्याएँ आ रही हैं, तो सुनिश्चित करें:
1. आप स्क्रिप्ट को X11 एनवायरनमेंट में चला रहे हैं (Wayland में नहीं)
2. आपके पास एक सक्रिय ब्राउज़र विंडो खुली है
3. ब्राउज़र विंडो फोकस में है या दृश्यमान है