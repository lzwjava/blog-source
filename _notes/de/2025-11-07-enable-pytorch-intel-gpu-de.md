---
audio: false
generated: true
image: false
lang: de
layout: post
model: anthropic/claude-4.5-sonnet
title: Aktivieren der Intel-GPU-Unterstützung für PyTorch
translated: true
---

Guter Fortschritt! PyTorch und IPEX arbeiten jetzt zusammen. Allerdings ist die Intel GPU-Unterstützung auf Ihrem System nicht aktiviert. Lassen Sie mich erklären, was passiert und wie Sie das Problem beheben können:

## Aktueller Status
- ✓ PyTorch + IPEX korrekt installiert
- ✗ Intel GPU (XPU)-Unterstützung nicht verfügbar
- ✗ Fehlende optionale Pakete (`dpctl`, `scikit-learn-intelex`)

## So aktivieren Sie Intel GPU-Unterstützung

### 1. **Überprüfen Sie, ob Sie eine Intel GPU haben**
```bash
# Überprüfen Sie Ihre GPU-Hardware
lspci | grep -i vga
# oder
lspci | grep -i display
```

### 2. **Installieren Sie Intel GPU-Treiber** (falls Sie Intel Arc/Iris/UHD-Grafik haben)

Für Ubuntu/Debian:
```bash
# Intel GPU-Repository hinzufügen
wget -qO - https://repositories.intel.com/gpu/intel-graphics.key | \
  sudo gpg --dearmor --output /usr/share/keyrings/intel-graphics.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/intel-graphics.gpg] https://repositories.intel.com/gpu/ubuntu jammy client" | \
  sudo tee /etc/apt/sources.list.d/intel-gpu-jammy.list

sudo apt update

# Installieren Sie Level Zero und OpenCL-Runtimes
sudo apt install -y \
  intel-opencl-icd \
  intel-level-zero-gpu \
  level-zero \
  level-zero-dev
```

### 3. **Installieren Sie zusätzliche Python-Pakete**
```bash
# Installieren Sie dpctl für Intel GPU-Geräteverwaltung
pip install dpctl

# Installieren Sie scikit-learn mit Intel-Optimierungen
pip install scikit-learn-intelex
```

### 4. **Installieren Sie PyTorch mit XPU-Unterstützung**
```bash
# Deinstallieren Sie CPU-only PyTorch
pip uninstall torch torchvision torchaudio

# Installieren Sie PyTorch mit Intel XPU-Unterstützung
pip install torch==2.8.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/xpu

# Stellen Sie sicher, dass IPEX übereinstimmt
pip install intel-extension-for-pytorch==2.8.0
```

### 5. **Überprüfen Sie die Installation**
```bash
python -c "import torch; import intel_extension_for_pytorch as ipex; print('XPU verfügbar:', torch.xpu.is_available()); print('Anzahl XPU-Geräte:', torch.xpu.device_count() if torch.xpu.is_available() else 0)"
```

## Zum Trainingsfehler

Der Fehler `"The optimizer should be given for training mode"` ist ein Bug in Ihrem Skript. Sie müssen einen Optimizer übergeben, wenn Sie trainieren. Überprüfen Sie Ihr `try_intel_gpu.py` und stellen Sie sicher, dass die Trainingsfunktion einen Optimizer-Parameter enthält.

**Welche Intel GPU-Hardware haben Sie?** Führen Sie `lspci | grep -i vga` aus, um es zu überprüfen, und ich kann Ihnen spezifischere Anweisungen geben.