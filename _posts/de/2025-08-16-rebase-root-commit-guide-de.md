---
audio: false
generated: true
image: false
lang: de
layout: post
title: Wichtige Anleitung zum Neubasieren des Root-Commit
translated: true
type: note
---

`git rebase --root` ist eine spezielle Form von Rebase, mit der du den **allerersten Commit** deines Repositorys umschreiben kannst. Normalerweise benötigt `git rebase` einen Parent-Commit, auf den rebased wird, aber die Option `--root` behandelt den Root-Commit (den ersten Commit ohne Parent) so, als würde er ebenfalls rebased werden.

So funktioniert es in der Praxis:

### 1. Standard-Rebase vs. Root-Rebase

*   **Normaler `git rebase`**: Du wendest Commits erneut auf einen anderen Branch oder Commit an und änderst so die Historie nach einer gewählten Basis.
*   **`git rebase --root`**: Anstatt nach dem Root zu beginnen, überschreibt es den Root selbst. Du kannst ihn aufteilen, mit nachfolgenden Commits zusammenführen (squash) oder ihn sogar vollständig ersetzen.

### 2. Typische Anwendungsfälle

*   **Die erste Commit-Nachricht bearbeiten**
    Wenn du die allererste Commit-Nachricht deines Projekts umschreiben möchtest, kannst du Folgendes ausführen:

    ```bash
    git rebase --root -i
    ```

    und `pick` für den ersten Commit in `reword` ändern.

*   **Den Root-Commit mit späteren Commits zusammenführen**
    Wenn dein erster Commit zum Beispiel nur Gerüstbau war (wie eine `README`), kannst du ihn mit dem nächsten Commit zusammenführen, um die Historie zu bereinigen.

*   **Den Root-Commit aufteilen**
    Wenn dein erster Commit zu viel enthielt (z. B. ein gesamter Projekt-Code-Dump), kannst du ihn während eines interaktiven Rebases in mehrere logische Commits aufteilen.

### 3. Was intern passiert

*   Git erstellt einen temporären "gefakten" Parent-Commit für den Root-Commit, damit es Rebase-Operationen von Grund an anwenden kann.
*   Jeder Commit wird neu abgespielt (rebased), als ob das Repository anders begonnen hätte.
*   Du schreibst im Wesentlichen die Grundlage der Historie deines Repos um.

### 4. Beispiel-Workflow

```bash
git rebase --root -i
```

Du erhältst einen Editor wie diesen:

```
pick a1b2c3d Initial commit
pick d4e5f6g Add feature A
pick h7i8j9k Add feature B
```

Von hier aus kannst du:

*   `pick` in `reword` für den Root-Commit ändern → seine Nachricht ändern.
*   `pick` in `squash` ändern → Root mit dem nächsten Commit zusammenführen.
*   Bei Bedarf die Reihenfolge ändern oder aufteilen.

### ⚠️ Wichtiger Hinweis

`git rebase --root` **schreibt die Historie um**. Daher sollte es nur auf Branches durchgeführt werden, die noch nicht gepusht/geteilt wurden, oder du musst anschließend einen Force-Push durchführen. Auf gemeinsamen Branches kann es bei Mitwirkenden zu Verwirrung und Konflikten führen.

---

Möchtest du, dass ich dir auch ein konkretes **Vorher-Nachher-Historiebeispiel** (mit Commit-Hashes) zeige, damit du genau sehen kannst, wie `git rebase --root` das Log ändert?