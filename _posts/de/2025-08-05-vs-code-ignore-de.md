---
audio: false
generated: true
image: false
lang: de
layout: post
title: Ausgenommene Dateien in VS Code ausblenden
translated: true
type: note
---

Sie können „Go to File“ (Schnellöffnen, Strg + P) so anpassen, dass es Dateien einschließt, die in Ihrer `.gitignore` stehen, indem Sie drei Einstellungen in Ihrer `settings.json` ändern:

1. **Der Suche mitteilen, die Regeln Ihrer `.gitignore` zu ignorieren**

   ```jsonc
   "search.useIgnoreFiles": false,      // .gitignore nicht beachten
   "search.useGlobalIgnoreFiles": false // globale gitignore nicht beachten
   ```
2. **Sicherstellen, dass Ihre Ausschluss-Globs diese Dateien nicht verstecken**
   Standardmäßig übernimmt VS Code alle Muster aus `files.exclude` in `search.exclude`. Wenn Sie `.gitignore`-Verzeichnisse dort manuell ausgeschlossen haben, aktivieren Sie sie wieder:

   ```jsonc
   "search.exclude": {
     "**/.git": false,          // .git indizieren (falls gewünscht)
     "**/.gitignore": false     // Ihre .gitignore-Datei selbst definitiv nicht ausblenden
     // …alle anderen Muster, die Sie überschreiben möchten
   }
   ```
3. **Das Fenster neu laden**
   Nachdem Sie Ihre Benutzer- oder Arbeitsbereichseinstellungen gespeichert haben, führen Sie **Developer: Reload Window** (⇧ ⌘ P → „Reload Window“) aus, damit der Datei-Indexierer die Änderung erfasst.

Wenn Sie nun Strg + P drücken, sehen Sie *alle* Dateien nach Namen – unabhängig davon, ob sie ignoriert werden oder nicht. ([stackoverflow.com][1])

[1]: https://stackoverflow.com/questions/62855190/how-do-you-include-git-ignored-files-in-vscode-quick-search?utm_source=chatgpt.com "How do you include git ignored files in VSCode quick search"