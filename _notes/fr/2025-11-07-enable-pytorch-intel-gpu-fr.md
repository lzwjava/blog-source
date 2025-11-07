---
audio: false
generated: true
image: false
lang: fr
layout: post
model: anthropic/claude-4.5-sonnet
title: Activer la prise en charge du GPU Intel pour PyTorch
translated: true
---

Bonne progression ! PyTorch et IPEX fonctionnent maintenant ensemble. Cependant, votre système n'a pas le support GPU Intel activé. Laissez-moi vous aider à comprendre ce qui se passe et comment le résoudre :

## État actuel
- ✓ PyTorch + IPEX installés correctement
- ✗ Support GPU Intel (XPU) non disponible
- ✗ Packages optionnels manquants (`dpctl`, `scikit-learn-intelex`)

## Pour activer le support GPU Intel

### 1. **Vérifiez si vous avez un GPU Intel**
```bash
# Vérifiez votre matériel GPU
lspci | grep -i vga
# ou
lspci | grep -i display
```

### 2. **Installez les pilotes GPU Intel** (si vous avez des graphiques Intel Arc/Iris/UHD)

Pour Ubuntu/Debian :
```bash
# Ajoutez le dépôt GPU Intel
wget -qO - https://repositories.intel.com/gpu/intel-graphics.key | \
  sudo gpg --dearmor --output /usr/share/keyrings/intel-graphics.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/intel-graphics.gpg] https://repositories.intel.com/gpu/ubuntu jammy client" | \
  sudo tee /etc/apt/sources.list.d/intel-gpu-jammy.list

sudo apt update

# Installez les runtimes Level Zero et OpenCL
sudo apt install -y \
  intel-opencl-icd \
  intel-level-zero-gpu \
  level-zero \
  level-zero-dev
```

### 3. **Installez les packages Python supplémentaires**
```bash
# Installez dpctl pour la gestion des périphériques GPU Intel
pip install dpctl

# Installez scikit-learn avec les optimisations Intel
pip install scikit-learn-intelex
```

### 4. **Installez PyTorch avec le support XPU**
```bash
# Désinstallez PyTorch version CPU uniquement
pip uninstall torch torchvision torchaudio

# Installez PyTorch avec le support Intel XPU
pip install torch==2.8.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/xpu

# Assurez-vous qu'IPEX correspond
pip install intel-extension-for-pytorch==2.8.0
```

### 5. **Vérifiez l'installation**
```bash
python -c "import torch; import intel_extension_for_pytorch as ipex; print('XPU disponible:', torch.xpu.is_available()); print('Nombre de périphériques XPU:', torch.xpu.device_count() if torch.xpu.is_available() else 0)"
```

## À propos de l'erreur d'entraînement

L'erreur `"The optimizer should be given for training mode"` est un bogue dans votre script. Vous devez passer un optimiseur en mode entraînement. Vérifiez votre `try_intel_gpu.py` et assurez-vous que la fonction d'entraînement inclut un paramètre d'optimiseur.

**Quel matériel GPU Intel avez-vous ?** Exécutez `lspci | grep -i vga` pour vérifier, et je pourrai vous donner des instructions plus spécifiques.