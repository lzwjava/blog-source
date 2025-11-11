---
audio: false
generated: true
lang: fr
layout: post
title: PortAudio et PyAudio
translated: true
type: note
---

L'erreur se produit car **pyaudio** nécessite les en-têtes de développement PortAudio pour compiler, qui sont manquants sur votre système. Voici comment la résoudre :

### Solution étape par étape :

1. **Installer les en-têtes de développement PortAudio** (requis pour pyaudio) :
```bash
sudo apt update && sudo apt install portaudio19-dev
```

2. **Installer les outils de développement Python** (s'ils ne sont pas déjà installés) :
```bash
sudo apt install python3-dev
```

3. **Réessayer l'installation** :
```bash
pip install -r requirements.local.txt
```

### Si vous rencontrez toujours des problèmes avec pycrypto :
Le package pycrypto est obsolète et peut avoir des problèmes de compatibilité. Remplacez-le par **pycryptodome** en modifiant votre `requirements.local.txt` :

1. Ouvrez le fichier requirements :
```bash
nano requirements.local.txt
```

2. Remplacez `pycrypto` par :
```
pycryptodome
```

3. Sauvegardez et relancez l'installation :
```bash
pip install -r requirements.local.txt
```

### Pourquoi cela fonctionne :
- `portaudio19-dev` fournit les en-têtes PortAudio manquants nécessaires pour compiler pyaudio
- `python3-dev` inclut les en-têtes de développement Python nécessaires
- `pycryptodome` est un remplacement maintenu et compatible pour l'obsolète pycrypto

### Alternative pour pycrypto (si vous devez le conserver) :
Si vous avez spécifiquement besoin de pycrypto, installez d'abord les dépendances de compilation :
```bash
sudo apt install build-essential libgmp-dev
pip install pycrypto
```
Mais notez que pycrypto a des problèmes de compatibilité avec les nouvelles versions de Python.

Après ces étapes, tous les packages devraient s'installer correctement. Les avertissements de DÉPRÉCIATION concernant les builds legacy sont informatifs et n'empêcheront pas l'installation - ils indiquent que les packages devront migrer vers des builds PEP 517 dans le futur.