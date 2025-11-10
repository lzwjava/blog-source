---
audio: false
generated: true
image: false
lang: de
layout: post
title: Anpassen von Suchausschlüssen in VS Code
translated: true
type: note
---

In VS Code berücksichtigt die globale Dateisuche die konfigurierten **Suchausschlüsse**. Sie können den Editor so einstellen, dass bestimmte Dateien oder Ordner ignoriert werden, damit sie nicht in den Suchergebnissen erscheinen.

Hier sind die wichtigsten Methoden:

---

### 1. `search.exclude` in **settings.json** verwenden

Öffnen Sie Ihre Einstellungen (`⌘,` / `Strg+,` → oben rechts „Einstellungen öffnen (JSON)“) und fügen Sie hinzu:

```json
"search.exclude": {
  "**/node_modules": true,
  "**/dist": true,
  "**/*.log": true
}
```

* Die Schlüssel sind [Glob Patterns](https://code.visualstudio.com/docs/editor/codebasics#_advanced-search-options).
* `true` bedeutet „von der Suche ausschließen“.
* Beispiele:

  * `**/node_modules` → alle node\_modules-Ordner
  * `**/*.log` → alle `.log`-Dateien, egal wo
  * `**/build/**` → alles innerhalb von build-Ordnern

---

### 2. `.gitignore` verwenden

Wenn Ihr Projekt eine `.gitignore`-Datei hat, können Sie VS Code anweisen, diese bei der Suche zu berücksichtigen:

```json
"search.useIgnoreFiles": true
```

Auf diese Weise erscheint alles, was von Git ignoriert wird, nicht in den Suchergebnissen.

---

### 3. `.ignore` verwenden

Sie können auch eine `.ignore`-Datei im Projektstammverzeichnis erstellen (gleiches Format wie `.gitignore`), die speziell für Editor-Tools gedacht ist. VS Code berücksichtigt sie, wenn `search.useIgnoreFiles` aktiviert ist.

---

### 4. Schnellausschluss in der Such-UI

Wenn Sie suchen, fahren Sie mit der Maus über eine Datei/einen Ordner in den Ergebnissen und klicken Sie auf **„Exclude“**. Dies fügt diesen Pfad temporär zu `search.exclude` in den Einstellungen hinzu.

---

👉 Die gängigste Einrichtung ist also:

* Allgemeine, projektweite Ausschlüsse in `.gitignore` hinzufügen.
* Editorspezifische Ausschlüsse (wie `dist`, `.vscode`) in `search.exclude` hinzufügen.

---

Möchten Sie, dass ich Ihnen zeige, wie Sie Dateien **nur während der Suche ausschließen** können, sie aber dennoch im Explorer behalten, oder wie Sie sie auch aus der Explorer-Seitenleiste ausblenden?