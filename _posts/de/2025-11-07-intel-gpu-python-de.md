---
audio: false
generated: true
image: false
lang: de
layout: post
model: anthropic/claude-4.5-sonnet
title: Intel GPU-Computing mit Python
translated: true
type: note
---

Hier erfahren Sie, wie Sie Intel oneAPI mit Python für GPU-Computing einrichten und verwenden:

## Installation

```bash
# Installieren Sie die Intel Extension for PyTorch (enthält die oneAPI-Laufzeitumgebung)
pip install intel-extension-for-pytorch

# Oder installieren Sie das vollständige oneAPI Base Toolkit (umfassender)
# Download von: https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html
```

## Python-Beispiele
## Installationsbefehle

```bash
# Installieren Sie die Intel Extension for PyTorch (für Ihr System empfohlen)
pip install torch torchvision torchaudio intel-extension-for-pytorch

# Installieren Sie dpctl für Low-Level-Kontrolle
pip install dpctl dpnp

# Installieren Sie Intel-optimiertes scikit-learn
pip install scikit-learn-intelex

# Überprüfen Sie die Installation
python -c "import torch; import intel_extension_for_pytorch as ipex; print('XPU available:', torch.xpu.is_available() if hasattr(torch, 'xpu') else False)"
```

## Wichtige Punkte:

1.  **Gerätenamen**: Intel verwendet `xpu` anstelle von CUDAs `cuda` in PyTorch
2.  **Kompatibilität**: Ihre Intel UHD Graphics sollte funktionieren, aber die Leistung ist im Vergleich zu diskreten GPUs begrenzt
3.  **Installation**: Die Intel Extension for PyTorch ist der einfachste Einstieg

## Schnelltest:

Speichern Sie diesen einfachen Test:

```python
import torch
import intel_extension_for_pytorch as ipex

print(f"PyTorch version: {torch.__version__}")
print(f"IPEX version: {ipex.__version__}")

if hasattr(torch, 'xpu') and torch.xpu.is_available():
    print(f"✓ Intel GPU verfügbar: {torch.xpu.get_device_name(0)}")
    
    # Einfache Berechnung
    x = torch.randn(100, 100, device='xpu')
    y = torch.randn(100, 100, device='xpu')
    z = x @ y
    print(f"✓ Erfolgreich auf der GPU berechnet")
else:
    print("✗ Intel GPU nicht erkannt")
```

Ausführen mit: `python test_intel_gpu.py`

Hinweis: Ihre integrierte Intel UHD Graphics hat eine begrenzte Rechenleistung im Vergleich zu diskreten GPUs, erwarten Sie also keine NVIDIA-ähnliche Leistung. Sie ist dennoch nützlich zum Lernen und für leichte GPU-Computing-Aufgaben.