---
audio: false
generated: true
image: false
lang: es
layout: post
model: anthropic/claude-4.5-sonnet
title: Habilitar la compatibilidad con GPU Intel para PyTorch
translated: true
type: note
---

¡Buen progreso! PyTorch e IPEX ahora funcionan juntos. Sin embargo, tu sistema no tiene habilitado el soporte para GPU Intel. Permíteme ayudarte a entender qué está pasando y cómo solucionarlo:

## Estado Actual
- ✓ PyTorch + IPEX instalados correctamente
- ✗ Soporte para GPU Intel (XPU) no disponible
- ✗ Paquetes opcionales faltantes (`dpctl`, `scikit-learn-intelex`)

## Para Habilitar el Soporte para GPU Intel

### 1. **Verifica si tienes una GPU Intel**
```bash
# Verifica tu hardware de GPU
lspci | grep -i vga
# o
lspci | grep -i display
```

### 2. **Instala los controladores de GPU Intel** (si tienes gráficos Intel Arc/Iris/UHD)

Para Ubuntu/Debian:
```bash
# Añade el repositorio de GPU Intel
wget -qO - https://repositories.intel.com/gpu/intel-graphics.key | \
  sudo gpg --dearmor --output /usr/share/keyrings/intel-graphics.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/intel-graphics.gpg] https://repositories.intel.com/gpu/ubuntu jammy client" | \
  sudo tee /etc/apt/sources.list.d/intel-gpu-jammy.list

sudo apt update

# Instala los runtimes Level Zero y OpenCL
sudo apt install -y \
  intel-opencl-icd \
  intel-level-zero-gpu \
  level-zero \
  level-zero-dev
```

### 3. **Instala paquetes adicionales de Python**
```bash
# Instala dpctl para la gestión de dispositivos de GPU Intel
pip install dpctl

# Instala scikit-learn con optimizaciones de Intel
pip install scikit-learn-intelex
```

### 4. **Instala PyTorch con soporte XPU**
```bash
# Desinstala PyTorch solo para CPU
pip uninstall torch torchvision torchaudio

# Instala PyTorch con soporte Intel XPU
pip install torch==2.8.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/xpu

# Asegúrate de que IPEX coincida
pip install intel-extension-for-pytorch==2.8.0
```

### 5. **Verifica la instalación**
```bash
python -c "import torch; import intel_extension_for_pytorch as ipex; print('XPU disponible:', torch.xpu.is_available()); print('Número de dispositivos XPU:', torch.xpu.device_count() if torch.xpu.is_available() else 0)"
```

## Sobre el Error de Entrenamiento

El error `"The optimizer should be given for training mode"` es un bug en tu script. Necesitas pasar un optimizador cuando estés entrenando. Revisa tu `try_intel_gpu.py` y asegúrate de que la función de entrenamiento incluya un parámetro de optimizador.

**¿Qué hardware de GPU Intel tienes?** Ejecuta `lspci | grep -i vga` para verificar, y puedo darte instrucciones más específicas.