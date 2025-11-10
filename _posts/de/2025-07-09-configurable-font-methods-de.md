---
audio: false
generated: true
lang: de
layout: post
title: Konfigurierbare Schriftarten in LaTeX
translated: true
type: note
---

Sie können die Schriftart konfigurierbar gestalten, indem Sie Variablen am Anfang Ihres LaTeX-Dokuments erstellen. Hier sind einige Ansätze:

## Methode 1: Einfache Variablen (Empfohlen)

## Methode 2: Verwendung von Konditionalen für verschiedene Systeme

Lassen Sie mich eine anspruchsvollere Version mit automatischer Betriebssystemerkennung erstellen:

## Methode 3: Verwendung einer separaten Konfigurationsdatei

Sie können auch eine separate Datei für die Schriftartkonfiguration erstellen:

Und dann in Ihrem Hauptdokument:

## Gängige Linux-Schriftartalternativen

Hier sind einige gute Schriftartalternativen für Linux-Systeme:

**Für chinesische/CJK-Schriftarten:**
- `Noto Sans CJK SC` (empfohlen)
- `Source Han Sans SC`
- `WenQuanYi Micro Hei`
- `Droid Sans Fallback`

**Für englische Schriftarten:**
- `Liberation Serif` (Times New Roman Alternative)
- `DejaVu Serif`
- `Linux Libertine`
- `TeX Gyre Termes`

## Verwendung

1. **Methode 1** ist die einfachste - kommentieren Sie einfach die Linux-Schriftartzeilen bei Bedarf aus
2. **Methode 2** ermöglicht es Ihnen, nur eine Variable (`\fontsystem`) zu ändern, um zwischen verschiedenen Systemen zu wechseln
3. **Methode 3** hält die Schriftartkonfiguration getrennt, was die Pflege verschiedener Versionen erleichtert

Wählen Sie die Methode, die am besten zu Ihrem Workflow passt!