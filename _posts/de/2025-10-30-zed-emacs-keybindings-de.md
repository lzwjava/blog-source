---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Konfiguration von Zed mit Emacs-Tastenkombinationen
translated: true
type: note
---

### Konfigurieren des Zed-Editors mit Emacs-Tastenkombinationen

Es sieht so aus, als ob du **Zed** meinen könntest (den leistungsstarken Code-Editor), da "Zig-Editor" nicht auf ein Standard-Tool verweist – Zig ist eine Programmiersprache ohne einen integrierten Editor. Falls das nicht deine Absicht war, kläre es gerne! Wenn wir von Zed ausgehen, hat dieser integrierte Unterstützung für Emacs-Tastenkombinationen (bezeichnet als "Emacs (Beta)"). Dies deckt viele Grundfunktionen sofort ab, wie Bewegung (`Strg-b/f/n/p`) und Bearbeitung (`Strg-d` zum Löschen von Zeichen, `Strg-k` zum Ausschneiden bis zum Zeilenende). Du kannst es einfach aktivieren und bei Bedarf weiter anpassen.

#### Schritt 1: Integrierte Emacs-Tastenzuordnung aktivieren
Zeds Emacs-Modus ist vordefiniert und erfordert für die Grundfunktionen kein manuelles Einrichten von Tastenbindungen. So wechselst du zu ihm:

1. Öffne die Zed-Einstellungen:
   - macOS: `Cmd-,`
   - Windows/Linux: `Strg-,`

2. Suche in der Einstellungs-UI nach "base keymap" und setze sie auf **Emacs**.

   *Oder bearbeite sie direkt in der `settings.json`* (öffnen via `Cmd-Alt-,` auf macOS oder `Strg-Alt-,` auf Windows/Linux):
   ```json
   {
     "base_keymap": "Emacs"
   }
   ```

   Speichere und lade Zed neu (`Cmd-R` oder `Strg-R`). Das war's – die Beta-Emacs-Tastenzuordnung wird sofort aktiviert.

   Alternativ verwende die Befehlspalette (`Cmd-Umsch-P` oder `Strg-Umsch-P`), tippe "toggle base keymap" ein und wähle Emacs.

Dies gibt dir die grundlegende Emacs-Bedienung ohne zusätzliche Arbeit. Für eine vollständige Liste der integrierten Bindungen, sieh dir Zeds Standard-Keymap-Dateien im Quellcode an (z.B. via GitHub), aber die Grundlagen beinhalten:
- **Bewegung**: `Strg-b` (Zeichen links), `Strg-f` (Zeichen rechts), `Strg-p` (Zeile hoch), `Strg-n` (Zeile runter), `Alt-b/f` (vorheriges/nächstes Wort).
- **Bearbeitung**: `Strg-d` (Zeichen löschen), `Strg-k` (bis Zeilenende ausschneiden), `Strg-y` (Einfügen/Yank), `Strg-@` (Marke für Region setzen), `Strg-w` (Region ausschneiden).
- **Sonstiges**: `Strg-x Strg-s` (Speichern), `Strg-g` (Abbrechen), `Strg-/` (Rückgängig).

#### Schritt 2: Grundlegende Tastenbindungen hinzufügen oder anpassen (falls nötig)
Für Anpassungen oder mehr Emacs-ähnliches Verhalten (z.B. besseres Home/End oder Absatznavigation), bearbeite `keymap.json`:
- Öffne sie via Befehlspalette: Tippe "open keymap file" ein.
- Pfad: `~/.config/zed/keymap.json` (macOS/Linux) oder `~\AppData\Roaming\Zed\keymap.json` (Windows).

Füge Bindungen als JSON-Array unter Kontexten wie "Editor" hinzu. Hier ist ein **minimales Beispiel** für grundlegende Bewegung und Bearbeitung (füge es in das Array ein; es basiert auf Community-Konfigurationen für Kompatibilität):

```json
[
  {
    "context": "Editor",
    "bindings": {
      // Grundlegende Bewegung
      "ctrl-a": "editor::MoveToBeginningOfLine",
      "ctrl-e": "editor::MoveToEndOfLine",
      "ctrl-b": "editor::MoveLeft",
      "ctrl-f": "editor::MoveRight",
      "ctrl-p": "editor::MoveLineUp",
      "ctrl-n": "editor::MoveLineDown",
      "alt-b": "editor::MoveToPreviousWordStart",
      "alt-f": "editor::MoveToNextWordEnd",

      // Grundlegende Bearbeitung
      "ctrl-d": "editor::DeleteRight",
      "ctrl-k": "editor::CutToEndOfLine",
      "ctrl-y": "editor::Paste",
      "ctrl-w": "editor::Cut",
      "ctrl-@": ["editor::SetSelectionAnchor", { "selection_id": 0 }],  // Marke setzen
      "ctrl-x ctrl-x": "editor::FlipSelectionAnchor",  // Punkt/Marke austauschen

      // Navigation Extras
      "ctrl-home": "editor::MoveToBeginning",
      "ctrl-end": "editor::MoveToEnd",
      "ctrl-g": "editor::Cancel"
    }
  }
]
```

- Speichere und lade Zed neu. Diese überschreiben oder ergänzen die Basis-Emacs-Zuordnung.
- Teste in einem Editor-Puffer. Für Auswahlen, verwende `Strg-Leertaste` (oder `Strg-@`), um die Marke zu setzen, und bewege dann die Cursorposition, um eine Region auszuwählen.
- Pro-Tipp: Kombiniere es mit `vim_mode: false` in der settings.json, um Konflikte zu vermeiden.

#### Tipps
- **Beta-Status**: Der Emacs-Modus wird verbessert (verfolge den Fortschritt [hier](https://github.com/zed-industries/zed/issues/4856)). Melde Probleme auf Zeds GitHub.
- **Vollständige benutzerdefinierte Setups**: Für erweiterte Funktionen (z.B. Fensterwechsel mit `Strg-x o`), siehe Community-Beispiele in der Diskussion unten.
- Falls du Vim/Helix-Modi parallel verwenden möchtest, setze `vim_mode: true` oder `helix_mode: true` in den Einstellungen – sie werden zusätzlich geladen.

Dies sollte dir 80% des grundlegenden Emacs-Gefühls vermitteln. Beginne mit der integrierten Lösung und passe sie dann schrittweise an!

[Key Bindings Docs](https://zed.dev/docs/key-bindings)
[Configuring Zed](https://zed.dev/docs/configuring-zed)
[Emacs Keymap Discussion](https://github.com/zed-industries/zed/discussions/6572)
[Emacs Compatibility Issue](https://github.com/zed-industries/zed/issues/4856)