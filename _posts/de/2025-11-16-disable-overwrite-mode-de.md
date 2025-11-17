---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Deaktivieren des VS Code Überschreibmodus
translated: true
type: note
---

In Visual Studio Code ist das Standardverhalten **Insert-Modus** (Tippen fügt Text ein und schiebt vorhandenen Text nach vorne).
Der **Replace-Modus** (Tippen überschreibt vorhandenen Text) wird aktiviert, wenn Sie die **Einfg**-Taste auf Ihrer Tastatur drücken – dies schaltet zwischen Einfüge- und Ersetzungs-/Überschreibmodus um.

### So schalten Sie vom Replace- (Überschreib-) zurück in den Insert-Modus

1.  Drücken Sie einfach einmal die **Einfg**-Taste auf Ihrer Tastatur.
    → Die Statusleiste unten rechts ändert sich von **OVR** (Overwrite/Überschreiben) zu **INS** (Insert/Einfügen).

### Wenn Sie nie wieder versehentlich in den Überschreibmodus gelangen möchten

Sie können die Einfg-Taste als Umschaltung komplett deaktivieren:

#### Methode 1: Tastenkombination (empfohlen)
Drücken Sie `Strg + Umschalt + P` → geben Sie **"Toggle Insert/Overwrite"** ein → Sie sehen den Befehl `Preferences: Toggle Insert on Paste and Overtype` oder ähnlich.
Zuverlässiger ist diese direkte Einstellung:

#### Methode 2: Fügen Sie dies Ihrer `settings.json` hinzu
```json
// Deaktiviert die Einfg-Taste zum Umschalten des Überschreibmodus
"editor.occurencesHighlight": true,
"editor.overtypeMode": false,

// Dies ist die entscheidende Einstellung:
"keyboard.dispatch": "keyCode"
```

Eigentlich die beste und gebräuchlichste Lösung:

```json
// Deaktiviert die Einfg-Taste in VS Code komplett
{
    "key": "insert",
    "command": "-editor.action.toggleOverwrite",
    "when": "editorTextFocus"
}
```

Oder schalten Sie Überschreiben global aus:

```json
"editor.occurrencesHighlight": true,
"editor.overwriteMode": false   // keine echte Einstellung, ignorieren

// Echte Einstellung zum Deaktivieren der Überschreib-Umschaltung:
"editor.insertSpaces": true,  // nicht relevant

// Korrekte Methode:
{
    "key": "insert",
    "command": "noop"   // oder entfernen Sie die Standard-Tastenbindung
}
```

#### Einfachste dauerhafte Lösung (die die meisten verwenden):
1.  Öffnen Sie die Einstellungen (`Strg + ,`)
2.  Suchen Sie nach **"overwrite"**
3.  Deaktivieren Sie **Editor: Overtype** (falls vorhanden) oder besser:
4.  Fügen Sie diese Zeile zu Ihrer `settings.json` hinzu (Strg + Umschalt + P → "Preferences: Open Settings (JSON)"):

```json
// Deaktiviert die Einfg-Taste zum Umschalten des Überschreibmodus komplett
{
    "key": "insert",
    "command": "-editor.action.toggleOverwrite"
}
```

Nachdem Sie das hinzugefügt haben, wird die Einfg-Taste in VS Code nichts mehr bewirken und Sie bleiben immer im Insert-Modus.

Das ist die gebräuchlichste und zuverlässigste Lösung, die von Entwicklern verwendet wird, die versehentlich auf Einfg drücken (besonders auf Laptops mit kleinen Tastaten in Taiwan/Asien, wo die Einfg-Taste leicht zu treffen ist).

Lassen Sie es mich wissen, wenn Sie macOS verwenden (verwendet eine andere Taste) oder eine Lösung per Klick in die Statusleiste möchten!