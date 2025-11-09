---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Verstehen der Ghostty-Konfigurationsdatei
translated: true
type: note
---

### Wie die Ghostty-Konfigurationsdatei funktioniert

Die Konfigurationsdatei von Ghostty verwendet ein einfaches, textbasiertes Format mit Schlüssel-Wert-Paaren im Stil von `key = value`. Sie ist so konzipiert, dass sie unkompliziert ist und es Ihnen ermöglicht, nur die Standardwerte zu überschreiben, die Sie ändern möchten – Ghostty liefert für alles andere sinnvolle Standardvorgaben mit, sodass auch eine minimale oder sogar leere Konfigurationsdatei problemlos funktioniert.

#### Kurze Syntax-Übersicht
- **Schlüssel und Werte**: Schlüssel sind immer kleingeschrieben und unterscheiden zwischen Groß- und Kleinschreibung (z. B. `font-family = JetBrains Mono`). Werte können ohne Anführungszeichen geschrieben werden, es sei denn, sie enthalten Leerzeichen oder Sonderzeichen (z. B. `font-family = "JetBrains Mono Nerd Font"`). Leerzeichen um das `=` spielen keine Rolle.
- **Kommentare**: Beginnen Sie eine Zeile mit `#` für Notizen (z. B. `# Mein benutzerdefiniertes Theme`). Inline-Kommentare nach Werten sind nicht möglich, da sie als Teil des Werts geparst werden.
- **Auf Standard zurücksetzen**: Verwenden Sie einen leeren Wert wie `key =`, um eine Einstellung auf den integrierten Standardwert von Ghostty zurückzusetzen.
- **Spezielle Werte**: Einige Optionen haben einzigartige Formate, wie Zeitangaben (z. B. `resize-overlay-duration = 4s 200ms`) – Details finden Sie in der Dokumentation.
- **Dateiladung**: Ghostty sucht nach der Konfiguration unter `~/.config/ghostty/config` (Linux/Windows) oder `~/Library/Application Support/com.mitchellh.ghostty/config` (macOS). Sie können mit `config-file = pfad/zur/anderen.conf` andere Dateien für modulare Setups einbinden.
- **CLI-Überschreibungen**: Jede Einstellung kann auch über Befehlszeilenflags gesetzt werden (z. B. `ghostty --font-family="Fira Code"`), die Vorrang vor der Datei haben.

Änderungen werden sofort wirksam, wenn Sie mit der Standard-Tastenkombination (Cmd+Shift+, unter macOS oder Ctrl+Shift+, unter Linux/Windows) neu laden oder `ghostty +reload-config` ausführen.

Um alle Optionen und Standardwerte zu sehen, führen Sie `ghostty +show-config --default --docs` in Ihrem Terminal aus.

### Was ist eine normale Konfiguration?
Eine "normale" Konfiguration ist oft minimal – es werden nur wenige Dinge wie Schriftart, Farben oder Abstände für den Komfort angepasst. Die Standardwerte von Ghostty umfassen JetBrains Mono als Schriftartfamilie (mit integrierter Nerd Font-Unterstützung), ein klares Hintergrund-/Vordergrundschema und keinen zusätzlichen Abstand.

Hier ist ein einfaches, typisches Beispiel für ein Dark-Theme mit einer beliebten Schriftart, etwas Abstand und grundlegenden Tastenkombinationen. Speichern Sie dies als Ihre `config`-Datei:

```
# Einfaches Dark-Theme mit Abstand und benutzerdefinierter Schriftart
background = 1e1e1e
foreground = f8f8f2
font-family = "JetBrains Mono Nerd Font"
font-size = 14

# Etwas Freiraum um den Text hinzufügen
window-padding-x = 8
window-padding-y = 8

# Benutzerdefinierte Tastenkombinationen (überschreibt Standardwerte bei Bedarf)
keybind = cmd+t=new_tab
keybind = cmd+w=close_tab
keybind = cmd+d=new_split:right
```

Dies hält die Konfiguration schlank, während die wesentlichen Elemente angepasst werden. Sie können sie mit weiteren Farben (z. B. Paletteinträgen wie `color0 = 282a36`) oder Themes aus der Dokumentation erweitern.

[Ghostty-Konfigurationsdokumentation](https://ghostty.org/docs/config)