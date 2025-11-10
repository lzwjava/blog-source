---
audio: false
generated: true
image: false
lang: de
layout: post
title: GitHub-Code-Suche-Tipps JSON
translated: true
type: note
---

Sie können eine GitHub-Code-Suchabfrage wie folgt schreiben:

```
"deepseek/deepseek-chat-v3.1" language:JSON
```

### Hinweise:

* Die Anführungszeichen stellen sicher, dass GitHub exakt nach der Zeichenkette `deepseek/deepseek-chat-v3.1` sucht.
* `language:JSON` (oder `lang:json`, beide funktionieren) schränkt die Ergebnisse auf JSON-Dateien ein.
* Wenn Sie JSON-ähnliche Konfigurationen einschließen möchten, die nicht in `.json`-Dateien vorliegen (wie `.ipynb` oder `.eslintrc`), können Sie den `lang:`-Filter weglassen.

Beispiele:

* Nur JSON-Dateien durchsuchen:

  ```
  "deepseek/deepseek-chat-v3.1" lang:json
  ```

* Alle Dateitypen durchsuchen, aber JSON-Ergebnisse hervorheben:

  ```
  "deepseek/deepseek-chat-v3.1"
  ```

Möchten Sie, dass ich Ihnen auch zeige, wie Sie dies weiter verfeinern können – zum Beispiel die Suche innerhalb von Repositories, Issues oder Code?