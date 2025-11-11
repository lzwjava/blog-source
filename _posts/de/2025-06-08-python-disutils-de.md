---
audio: false
generated: true
lang: de
layout: post
title: Beheben des Python-distutils-ModuleNotFoundError
translated: true
type: note
---

Der Fehler tritt auf, weil das `distutils`-Modul, das Teil der Python-Standardbibliothek ist, in Ihrer Umgebung fehlt. Dies ist bei minimalen Python-Installationen häufig der Fall. So beheben Sie das Problem:

### Lösung:
1. **Installieren Sie die Python-Entwicklungstools** (enthält `distutils`):
   ```bash
   sudo apt update && sudo apt install python3-distutils python3-dev
   ```

2. **Installieren Sie `setuptools` erneut** (um die ordnungsgemäße Funktionalität sicherzustellen):
   ```bash
   pip install --upgrade --force-reinstall setuptools
   ```

3. **Wiederholen Sie die Installation Ihrer Requirements**:
   ```bash
   pip install -r requirements.local.txt
   ```

### Warum das funktioniert:
- `python3-distutils` stellt das fehlende `distutils`-Modul bereit.
- `python3-dev` enthält die notwendigen Header- und Build-Tools.
- Die Neuinstallation von `setuptools` behebt eventuelle verbleibende Konfigurationsprobleme.

Wenn Sie eine virtuelle Umgebung verwenden, erstellen Sie diese nach der Installation der Systempakete neu, um sicherzustellen, dass die Umgebung Zugriff auf die benötigten Module hat.