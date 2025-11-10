---
audio: false
generated: true
lang: fr
layout: post
title: Compter les fichiers dans un répertoire
translated: true
type: note
---

Pour compter le nombre de fichiers dans un répertoire, vous pouvez utiliser différentes méthodes selon votre système d'exploitation et vos outils. Voici les approches les plus courantes :

### **Sur Windows (Invite de commande)**
```cmd
dir /a-d | find /c /v ""
```
- Liste tous les fichiers (pas les répertoires) et compte les lignes, en excluant les vides.

### **Sur Windows (PowerShell)**
```powershell
(Get-ChildItem -File).Count
```
- Récupère uniquement les fichiers et les compte.

### **Sur Linux/macOS (Terminal)**
```bash
ls -l | grep ^- | wc -l
```
- Liste les fichiers (`ls -l`), filtre les fichiers réguliers (`grep ^-`), et les compte (`wc -l`).

OU, plus simplement :
```bash
find . -maxdepth 1 -type f | wc -l
```
- Trouve uniquement les fichiers (`-type f`) dans le répertoire courant (`-maxdepth 1`) et les compte.

### **Avec Python**
```python
import os
file_count = len([f for f in os.listdir('.') if os.path.isfile(f)])
print(file_count)
```
- Liste le contenu du répertoire, vérifie les fichiers et les compte.

Choisissez la méthode en fonction de votre environnement. Si vous avez besoin de détails pour un système ou un outil spécifique, faites-le moi savoir !