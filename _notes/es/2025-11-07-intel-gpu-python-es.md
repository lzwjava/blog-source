---
audio: false
generated: true
image: false
lang: es
layout: post
model: anthropic/claude-4.5-sonnet
title: Computación con GPU de Intel en Python
translated: true
type: note
---

Aquí te mostramos cómo configurar y usar Intel oneAPI con Python para computación GPU:

## Instalación

```bash
# Instalar Intel Extension for PyTorch (incluye el runtime de oneAPI)
pip install intel-extension-for-pytorch

# O instalar el kit de herramientas base oneAPI completo (más integral)
# Descargar desde: https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html
```

## Ejemplos en Python

## Comandos de Instalación

```bash
# Instalar Intel Extension for PyTorch (recomendado para tu sistema)
pip install torch torchvision torchaudio intel-extension-for-pytorch

# Instalar dpctl para control de bajo nivel
pip install dpctl dpnp

# Instalar scikit-learn optimizado para Intel
pip install scikit-learn-intelex

# Verificar la instalación
python -c "import torch; import intel_extension_for_pytorch as ipex; print('XPU disponible:', torch.xpu.is_available() if hasattr(torch, 'xpu') else False)"
```

## Puntos Clave:

1.  **Nomenclatura del dispositivo**: Intel usa `xpu` en lugar del `cuda` de CUDA en PyTorch
2.  **Compatibilidad**: Tu Intel UHD Graphics debería funcionar, pero el rendimiento será limitado comparado con GPUs discretas
3.  **Instalación**: Intel Extension for PyTorch es la forma más fácil de comenzar

## Prueba Rápida:

Guarda esta prueba simple:

```python
import torch
import intel_extension_for_pytorch as ipex

print(f"Versión de PyTorch: {torch.__version__}")
print(f"Versión de IPEX: {ipex.__version__}")

if hasattr(torch, 'xpu') and torch.xpu.is_available():
    print(f"✓ GPU Intel disponible: {torch.xpu.get_device_name(0)}")
    
    # Cálculo simple
    x = torch.randn(100, 100, device='xpu')
    y = torch.randn(100, 100, device='xpu')
    z = x @ y
    print(f"✓ Cálculo en GPU exitoso")
else:
    print("✗ GPU Intel no detectada")
```

Ejecuta con: `python test_intel_gpu.py`

Nota: Tu Intel UHD Graphics integrada tiene capacidad de cómputo limitada comparada con las GPUs discretas, así que no esperes un rendimiento al nivel de NVIDIA. Sigue siendo útil para aprender y para tareas ligeras de computación GPU.