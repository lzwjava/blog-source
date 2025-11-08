---
audio: false
generated: true
image: false
lang: ar
layout: post
model: anthropic/claude-4.5-sonnet
title: الحوسبة باستخدام وحدات معالجة الرسوميات من إنتل وبايثون
translated: true
type: note
---

إليك كيفية إعداد واستخدام Intel oneAPI مع Python للحوسبة باستخدام وحدة معالجة الرسوميات:

## التثبيت

```bash
# تثبيت Intel Extension for PyTorch (يتضمن وقت تشغيل oneAPI)
pip install intel-extension-for-pytorch

# أو قم بتثبيت مجموعة أدوات oneAPI الأساسية الكاملة (أكثر شمولاً)
# التنزيل من: https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html
```

## أمثلة بايثون## أوامر التثبيت

```bash
# تثبيت Intel Extension for PyTorch (موصى به لنظامك)
pip install torch torchvision torchaudio intel-extension-for-pytorch

# تثبيت dpctl للتحكم على مستوى أدنى
pip install dpctl dpnp

# تثبيت scikit-learn المُحسّن من إنتل
pip install scikit-learn-intelex

# التحقق من التثبيت
python -c "import torch; import intel_extension_for_pytorch as ipex; print('XPU available:', torch.xpu.is_available() if hasattr(torch, 'xpu') else False)"
```

## النقاط الرئيسية:

1.  **تسمية الجهاز**: إنتل تستخدم `xpu` بدلاً من `cuda` الخاصة بـ CUDA في PyTorch
2.  **التوافق**: يجب أن تعمل بطاقة Intel UHD Graphics الخاصة بك، ولكن سيكون الأداء محدودًا مقارنة بوحدات معالجة الرسوميات المنفصلة
3.  **التثبيت**: Intel Extension for PyTorch هي أسهل طريقة للبدء

## اختبار سريع:

احفظ هذا الاختبار البسيط:

```python
import torch
import intel_extension_for_pytorch as ipex

print(f"PyTorch version: {torch.__version__}")
print(f"IPEX version: {ipex.__version__}")

if hasattr(torch, 'xpu') and torch.xpu.is_available():
    print(f"✓ Intel GPU available: {torch.xpu.get_device_name(0)}")
    
    # عملية حسابية بسيطة
    x = torch.randn(100, 100, device='xpu')
    y = torch.randn(100, 100, device='xpu')
    z = x @ y
    print(f"✓ Successfully computed on GPU")
else:
    print("✗ Intel GPU not detected")
```

شغّله باستخدام: `python test_intel_gpu.py`

ملاحظة: بطاقة Intel UHD Graphics المدمجة الخاصة بك لديها قدرة حوسبة محدودة مقارنة بوحدات معالجة الرسوميات المنفصلة، لذلك لا تتوقع أداءً بمستوى NVIDIA. لا تزال مفيدة لتعلم ومهام الحوسبة الخفيفة باستخدام وحدة معالجة الرسوميات.