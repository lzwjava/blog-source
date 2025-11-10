---
audio: false
generated: true
image: false
lang: de
layout: post
title: Git-Müllabfuhr erklärt
translated: true
type: note
---

`git gc` steht für **Git garbage collection**. Es ist ein Haushaltsbefehl, der Ihr lokales Repository bereinigt und optimiert.

### Was es bewirkt

* **Komprimiert den Dateiverlauf**: Git speichert Objekte (Commits, Trees, Blobs) in einer Datenbank. Mit der Zeit sammeln sich viele lose Objekte an. `git gc` packt sie zu einer kompakten Binärdatei zusammen und spart so Speicherplatz.
* **Entfernt unerreichbare Objekte**: Wenn Sie Branches gelöscht oder Rebases durchgeführt haben, sind einige Commits möglicherweise nicht mehr von einer Referenz erreichbar. Git bewahrt sie aus Sicherheitsgründen eine Weile auf, aber `git gc` räumt sie schließlich weg.
* **Optimiert Referenzen**: Es schreibt Refs wie Tags und Branches neu und packt sie zusammen, um Suchvorgänge zu beschleunigen.
* **Bereinigt Reflogs**: Alte Reflog-Einträge (Aufzeichnungen von HEAD-Änderungen), die die Aufbewahrungsfrist überschritten haben, werden entfernt.

### Warum es manchmal automatisch passiert

* Git führt einen **automatischen Hintergrund-`gc`** aus, wenn die Anzahl loser Objekte oder Pack-Dateien einen Schwellenwert überschreitet. Zum Beispiel kann Git ihn auslösen, wenn Sie viele Commits, Rebases oder Merges durchgeführt haben.
* Viele Git-Befehle (wie `git fetch`, `git merge` oder `git rebase`) prüfen, ob ein `gc` ratsam ist, und führen ihn bei Bedarf automatisch aus.
* Dies hilft, die Leistungsfähigkeit Ihres Repositories aufrechtzuerhalten, ohne dass Sie daran denken müssen.

### Wann man es manuell ausführen sollte

* Wenn sich Ihr Repository **langsam** oder **aufgebläht** anfühlt (z.B. großer `.git`-Ordner).
* Nach einer **größeren Bereinigung** (wie dem Löschen von Branches oder dem Entfernen großer Dateien aus dem Verlauf).
* Wenn Sie eine sofortige Bereinigung erzwingen möchten:

  ```bash
  git gc --prune=now --aggressive
  ```

  *(Vorsicht: `--aggressive` kann sehr lange dauern, besonders bei großen Repositories)*

---

Möchten Sie, dass ich auch erkläre, wie Sie **prüfen können, wann Git `gc` zuletzt automatisch ausgeführt hat** und welche Schwellenwerte es auslösen?