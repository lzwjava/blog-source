---
audio: false
generated: true
image: false
lang: de
layout: post
title: PyCharm Dateien sicher und intelligent umbenennen
translated: true
type: note
---

Ja — wenn Sie die **Refactoring-Funktion von PyCharm** verwenden (Rechtsklick auf die Datei → Refactor → Rename, oder drücken Sie `Umschalt+F6` auf den Dateinamen), wird nicht nur der Dateiname auf der Festplatte geändert, sondern auch **alle Referenzen und Import-Statements** aktualisiert, die darauf verweisen, sofern sie innerhalb des Projekts auflösbar sind.

Einige wichtige Details, die Sie beachten sollten:

* **Umfang des Refactorings**: PyCharm analysiert Ihr gesamtes Projekt, daher werden Importe in anderen Python-Dateien innerhalb des Projekts automatisch aktualisiert.
* **Unaufgelöste / dynamische Importe**: Wenn einige Importe dynamisch erstellt werden (zum Beispiel mit `__import__`, `importlib` oder zeichenbasierten Modulpfaden), erkennt PyCharm diese nicht, daher werden sie nicht aktualisiert.
* **Mehrere Roots / externe Skripte**: Wenn andere Skripte sich außerhalb des PyCharm-Projekts befinden oder nicht indiziert sind (z.B. nicht in Ihren Projekt-Quell-Roots), erfasst PyCharm diese ebenfalls nicht.
* **Tests und relative Importe**: Wenn Sie relative Importe verwenden (`from . import something`) und die Ordnerstruktur sich ändert, müssen Sie dies möglicherweise separat überprüfen.

Für normale `import mymodule.something`-Fälle innerhalb Ihres Projekts hält das Umbenennen mit PyCharm Refactoring also alles konsistent.

Möchten Sie, dass ich auch erkläre, **wie Sie nach dem Umbenennen sicher testen können**, um sicherzugehen, dass nichts kaputt gegangen ist?