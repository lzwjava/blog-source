---
audio: false
generated: true
lang: es
layout: post
title: Contar Archivos en un Directorio
translated: true
type: note
---

Para contar el número de archivos en un directorio, puedes usar varios métodos dependiendo de tu sistema operativo y herramientas. Estos son los enfoques más comunes:

### **En Windows (Símbolo del sistema)**
```cmd
dir /a-d | find /c /v ""
```
- Lista todos los archivos (no directorios) y cuenta las líneas, excluyendo las vacías.

### **En Windows (PowerShell)**
```powershell
(Get-ChildItem -File).Count
```
- Recupera solo archivos y los cuenta.

### **En Linux/macOS (Terminal)**
```bash
ls -l | grep ^- | wc -l
```
- Lista archivos (`ls -l`), filtra por archivos regulares (`grep ^-`), y los cuenta (`wc -l`).

O, más simple:
```bash
find . -maxdepth 1 -type f | wc -l
```
- Encuentra solo archivos (`-type f`) en el directorio actual (`-maxdepth 1`) y los cuenta.

### **Usando Python**
```python
import os
file_count = len([f for f in os.listdir('.') if os.path.isfile(f)])
print(file_count)
```
- Lista el contenido del directorio, verifica qué elementos son archivos y los cuenta.

Elige el método basándote en tu entorno. Si necesitas detalles para un sistema operativo o herramienta específica, ¡avísame!