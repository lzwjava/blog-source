---
audio: false
generated: true
lang: de
layout: post
title: Dateien in einem Verzeichnis zählen
translated: true
type: note
---

Um die Anzahl der Dateien in einem Verzeichnis zu zählen, können Sie verschiedene Methoden verwenden, abhängig von Ihrem Betriebssystem und Ihren Tools. Hier sind die gängigsten Ansätze:

### **Unter Windows (Eingabeaufforderung)**
```cmd
dir /a-d | find /c /v ""
```
- Listet alle Dateien (keine Verzeichnisse) auf und zählt die Zeilen, außer leeren.

### **Unter Windows (PowerShell)**
```powershell
(Get-ChildItem -File).Count
```
- Ruft nur Dateien ab und zählt sie.

### **Unter Linux/macOS (Terminal)**
```bash
ls -l | grep ^- | wc -l
```
- Listet Dateien auf (`ls -l`), filtert nach regulären Dateien (`grep ^-`) und zählt sie (`wc -l`).

ODER, einfacher:
```bash
find . -maxdepth 1 -type f | wc -l
```
- Findet nur Dateien (`-type f`) im aktuellen Verzeichnis (`-maxdepth 1`) und zählt sie.

### **Mit Python**
```python
import os
file_count = len([f for f in os.listdir('.') if os.path.isfile(f)])
print(file_count)
```
- Listet Verzeichnisinhalte auf, prüft auf Dateien und zählt sie.

Wählen Sie die Methode basierend auf Ihrer Umgebung. Wenn Sie Details für ein bestimmtes Betriebssystem oder Tool benötigen, lassen Sie es mich wissen!