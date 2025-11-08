---
audio: false
generated: true
image: false
lang: hi
layout: post
model: anthropic/claude-4.5-sonnet
title: पाइटॉर्च के लिए इंटेल जीपीयू सपोर्ट सक्षम करें
translated: true
type: note
---

अच्छी प्रगति! PyTorch और IPEX अब एक साथ काम कर रहे हैं। हालाँकि, आपके सिस्टम में Intel GPU सपोर्ट सक्षम नहीं है। मैं आपको यह समझने में मदद करता हूँ कि क्या हो रहा है और इसे कैसे ठीक करें:

## वर्तमान स्थिति
- ✓ PyTorch + IPEX सही ढंग से इंस्टॉल हो गए हैं
- ✗ Intel GPU (XPU) सपोर्ट उपलब्ध नहीं है
- ✗ कुछ वैकल्पिक पैकेज (`dpctl`, `scikit-learn-intelex`) गायब हैं

## Intel GPU सपोर्ट सक्षम करने के लिए

### 1. **जाँचें कि क्या आपके पास Intel GPU है**
```bash
# अपने GPU हार्डवेयर की जाँच करें
lspci | grep -i vga
# या
lspci | grep -i display
```

### 2. **Intel GPU ड्राइवर इंस्टॉल करें** (यदि आपके पास Intel Arc/Iris/UHD ग्राफ़िक्स हैं)

Ubuntu/Debian के लिए:
```bash
# Intel GPU रिपॉजिटरी जोड़ें
wget -qO - https://repositories.intel.com/gpu/intel-graphics.key | \
  sudo gpg --dearmor --output /usr/share/keyrings/intel-graphics.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/intel-graphics.gpg] https://repositories.intel.com/gpu/ubuntu jammy client" | \
  sudo tee /etc/apt/sources.list.d/intel-gpu-jammy.list

sudo apt update

# Level Zero और OpenCL रनटाइम इंस्टॉल करें
sudo apt install -y \
  intel-opencl-icd \
  intel-level-zero-gpu \
  level-zero \
  level-zero-dev
```

### 3. **अतिरिक्त Python पैकेज इंस्टॉल करें**
```bash
# Intel GPU डिवाइस प्रबंधन के लिए dpctl इंस्टॉल करें
pip install dpctl

# Intel ऑप्टिमाइज़ेशन के साथ scikit-learn इंस्टॉल करें
pip install scikit-learn-intelex
```

### 4. **XPU सपोर्ट के साथ PyTorch इंस्टॉल करें**
```bash
# केवल-CPU वाले PyTorch को अनइंस्टॉल करें
pip uninstall torch torchvision torchaudio

# Intel XPU सपोर्ट के साथ PyTorch इंस्टॉल करें
pip install torch==2.8.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/xpu

# सुनिश्चित करें कि IPEX मेल खाता है
pip install intel-extension-for-pytorch==2.8.0
```

### 5. **इंस्टॉलेशन सत्यापित करें**
```bash
python -c "import torch; import intel_extension_for_pytorch as ipex; print('XPU available:', torch.xpu.is_available()); print('XPU device count:', torch.xpu.device_count() if torch.xpu.is_available() else 0)"
```

## ट्रेनिंग एरर के बारे में

`"The optimizer should be given for training mode"` एरर आपकी स्क्रिप्ट में एक बग है। ट्रेनिंग करते समय आपको एक ऑप्टिमाइज़र पास करना होगा। अपनी `try_intel_gpu.py` फ़ाइल जाँचें और सुनिश्चित करें कि ट्रेनिंग फ़ंक्शन में एक ऑप्टिमाइज़र पैरामीटर शामिल है।

**आपके पास कौन सा Intel GPU हार्डवेयर है?** जाँचने के लिए `lspci | grep -i vga` चलाएँ, और मैं आपको और अधिक विशिष्ट निर्देश दे सकता हूँ।