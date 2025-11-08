---
audio: false
generated: true
image: false
lang: ar
layout: post
model: anthropic/claude-4.5-sonnet
title: تمكين دعم وحدة معالجة الرسوميات من إنتل لبايتورش
translated: true
type: note
---

تقدم جيد! PyTorch و IPEX يعملان الآن معًا. ومع ذلك، نظامك لا يدعم معالج الرسوميات (GPU) من إنتل. دعني أساعدك في فهم ما يحدث وكيفية إصلاحه:

## الحالة الحالية
- ✓ PyTorch + IPEX مثبتان بشكل صحيح
- ✗ دعم معالج الرسوميات (GPU/XPU) من إنتل غير متوفر
- ✗ حزم اختيارية مفقودة (`dpctl`, `scikit-learn-intelex`)

## لتمكين دعم معالج الرسوميات من إنتل

### 1. **تحقق مما إذا كان لديك معالج رسوميات من إنتل**
```bash
# تحقق من عتاد معالج الرسوميات لديك
lspci | grep -i vga
# أو
lspci | grep -i display
```

### 2. **قم بتثبيت برامج تشغيل معالج الرسوميات من إنتل** (إذا كان لديك رسوميات Intel Arc/Iris/UHD)

لـ Ubuntu/Debian:
```bash
# أضف مستودع معالج الرسوميات من إنتل
wget -qO - https://repositories.intel.com/gpu/intel-graphics.key | \
  sudo gpg --dearmor --output /usr/share/keyrings/intel-graphics.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/intel-graphics.gpg] https://repositories.intel.com/gpu/ubuntu jammy client" | \
  sudo tee /etc/apt/sources.list.d/intel-gpu-jammy.list

sudo apt update

# قم بتثبيت بيئات تشغيل Level Zero و OpenCL
sudo apt install -y \
  intel-opencl-icd \
  intel-level-zero-gpu \
  level-zero \
  level-zero-dev
```

### 3. **قم بتثبيت حزم Python إضافية**
```bash
# قم بتثبيت dpctl لإدارة أجهزة معالج الرسوميات من إنتل
pip install dpctl

# قم بتثبيت scikit-learn مع تحسينات إنتل
pip install scikit-learn-intelex
```

### 4. **قم بتثبيت PyTorch مع دعم XPU**
```bash
# أزل تثبيت PyTorch للإصدار المقتصر على المعالج (CPU) فقط
pip uninstall torch torchvision torchaudio

# قم بتثبيت PyTorch مع دعم إنتل XPU
pip install torch==2.8.0 torchvision torchaudio --index-url https://download.pytytorch.org/whl/xpu

# تأكد من تطابق IPEX
pip install intel-extension-for-pytorch==2.8.0
```

### 5. **تحقق من التثبيت**
```bash
python -c "import torch; import intel_extension_for_pytorch as ipex; print('XPU available:', torch.xpu.is_available()); print('XPU device count:', torch.xpu.device_count() if torch.xpu.is_available() else 0)"
```

## حول خطأ التدريب

الخطأ `"The optimizer should be given for training mode"` هو خلل (bug) في السكريبت الخاص بك. تحتاج إلى تمرير مُحسّن (optimizer) عند التدريب. تحقق من ملف `try_intel_gpu.py` وتأكد من أن دالة التدريب تتضمن معاملًا للمُحسّن (optimizer).

**ما هو عتاد معالج الرسوميات من إنتل الذي تمتلكه؟** قم بتشغيل `lspci | grep -i vga` للتحقق، وسأقدم لك تعليمات أكثر تحديدًا.