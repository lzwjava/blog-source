---
audio: false
generated: true
image: false
lang: fr
layout: post
model: anthropic/claude-4.5-sonnet
title: Calcul GPU Intel avec Python
translated: true
type: note
---

Voici comment configurer et utiliser Intel oneAPI avec Python pour le calcul GPU :

## Installation

```bash
# Installer Intel Extension for PyTorch (inclut le runtime oneAPI)
pip install intel-extension-for-pytorch

# Ou installer le kit d'outils de base oneAPI complet (plus exhaustif)
# Télécharger depuis : https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html
```

## Exemples Python

## Commandes d'installation

```bash
# Installer Intel Extension for PyTorch (recommandé pour votre système)
pip install torch torchvision torchaudio intel-extension-for-pytorch

# Installer dpctl pour un contrôle de bas niveau
pip install dpctl dpnp

# Installer scikit-learn optimisé par Intel
pip install scikit-learn-intelex

# Vérifier l'installation
python -c "import torch; import intel_extension_for_pytorch as ipex; print('XPU disponible:', torch.xpu.is_available() if hasattr(torch, 'xpu') else False)"
```

## Points clés :

1. **Nommage des périphériques** : Intel utilise `xpu` au lieu de `cuda` de CUDA dans PyTorch
2. **Compatibilité** : Votre Intel UHD Graphics devrait fonctionner, mais les performances seront limitées comparé aux GPU discrets
3. **Installation** : Intel Extension for PyTorch est la façon la plus simple de commencer

## Test rapide :

Enregistrez ce test simple :

```python
import torch
import intel_extension_for_pytorch as ipex

print(f"Version de PyTorch : {torch.__version__}")
print(f"Version d'IPEX : {ipex.__version__}")

if hasattr(torch, 'xpu') and torch.xpu.is_available():
    print(f"✓ GPU Intel disponible : {torch.xpu.get_device_name(0)}")
    
    # Calcul simple
    x = torch.randn(100, 100, device='xpu')
    y = torch.randn(100, 100, device='xpu')
    z = x @ y
    print(f"✓ Calcul réussi sur le GPU")
else:
    print("✗ GPU Intel non détecté")
```

Exécutez avec : `python test_intel_gpu.py`

Note : Votre Intel UHD Graphics intégré a des capacités de calcul limitées comparé aux GPU discrets, n'attendez donc pas des performances équivalentes à NVIDIA. Il reste utile pour l'apprentissage et les tâches légères de calcul GPU.