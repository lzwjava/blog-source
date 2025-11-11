---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Excel-Dateien mit Pandas lesen
translated: true
type: note
---

### Voraussetzungen
Um Excel-Dateien in Python zu lesen, benötigen Sie die `pandas`-Bibliothek und eine Excel-Engine. Installieren Sie pandas, falls noch nicht geschehen:
```
pip install pandas
```
Für moderne Excel-Formate (.xlsx) installieren Sie `openpyxl`:
```
pip install openpyxl
```
Für .xls-Dateien verwenden Sie `xl