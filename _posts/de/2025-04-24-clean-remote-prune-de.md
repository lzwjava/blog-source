---
audio: false
generated: true
image: false
lang: de
layout: post
title: Entfernen Sie nicht mehr vorhandene Remote-Branches mit Prune
translated: true
type: note
---

`git fetch --prune` ist eine Möglichkeit, Ihre lokalen Verweise auf Remote-Branches sauber und aktuell zu halten.

### Was es bewirkt

* **`git fetch`** aktualisiert normalerweise Ihre lokale Kopie der Remote-Branches (wie `origin/main`, `origin/feature-x`), ohne Ihre eigenen lokalen Branches anzufassen.
* Mit der Zeit könnte das Remote-Repository einige Branches löschen oder umbenennen. Ohne Bereinigung würde Ihr lokales Repository diese alten Remote-Tracking-Branches (z.B. `origin/feature-old`) weiterhin anzeigen.
* **Die Option `--prune`** weist Git an: *"Wenn der Remote ein Branch nicht mehr vorhanden ist, lösche meinen entsprechenden Remote-Tracking-Verweis."*

Nach dem Ausführen von `git fetch --prune` stimmt Ihre lokale Liste der Remote-Branches also exakt mit dem überein, was der Remote aktuell hat.

### Beispiel

1. Remote hat die Branches: `main`, `feature-a`.
2. Sie führen `git fetch` aus → Sie haben jetzt `origin/main`, `origin/feature-a`.
3. Jemand löscht `feature-a` auf dem Remote.
4. Wenn Sie `git fetch` ausführen, sehen Sie `origin/feature-a` lokal immer noch (veralteter Verweis).
5. Wenn Sie `git fetch --prune` ausführen, stellt Git fest, dass `feature-a` weg ist und entfernt `origin/feature-a` aus Ihrem lokalen Repository.

### Warum es nützlich ist

* Hält `git branch -r` (die Liste der Remote-Branches) sauber.
* Vermeidet Verwirrung beim Wechseln oder Mergen in Branches, die upstream nicht mehr existieren.
* Wird oft mit Aliassen verwendet (z.B. `git fetch -p`) oder kann als Standard festgelegt werden mit:

  ```bash
  git config fetch.prune true
  ```

Auf diese Weise prunt jeder `git fetch` automatisch veraltete Branches.

---

Möchten Sie, dass ich auch erkläre, wie **Pruning mit Tags interagiert** (da `git fetch --prune` standardmäßig nur Branches behandelt, Tags sich jedoch anders verhalten)?