---
audio: false
generated: true
lang: de
layout: post
title: Git Stash
translated: true
type: note
---

Hier erfährst du, wie du `git stash` effektiv nutzen und häufig zwischen Branches oder Tags wechseln kannst, ohne uncommittete Änderungen zu verlieren:

## Verwendung von `git stash`

`git stash` ist ein mächtiger Befehl, der es dir ermöglicht, deine uncommitteten Änderungen (sowohl staged als auch unstaged) temporär zu speichern und dein Arbeitsverzeichnis auf den letzten Commit zurückzusetzen. Dies ist nützlich, wenn du zwischen Branches wechseln oder an etwas anderem arbeiten musst, ohne deine aktuellen, unfertigen Arbeiten zu committen.

Hier ist eine Übersicht über häufige `git stash`-Operationen:

**1. Aktuelle Änderungen stashen:**

```bash
git stash
```

Dieser Befehl nimmt deine uncommitteten Änderungen, speichert sie als neuen Stash und bereinigt dein Arbeitsverzeichnis. Du siehst eine Nachricht wie:

```
Saved working directory and index state WIP on <your_branch>: <commit_hash> <commit_message>
```

**2. Stashen mit einer Nachricht:**

Es ist hilfreich, deinen Stashes eine beschreibende Nachricht hinzuzufügen, besonders wenn du mehrere hast:

```bash
git stash save "deine beschreibende Nachricht"
# oder
git stash push -m "deine beschreibende Nachricht"
```

**3. Deine Stashes auflisten:**

Um eine Liste aller gespeicherten Stashes zu sehen, verwende:

```bash
git stash list
```

Dies zeigt eine Liste von Stashes an, normalerweise im Format:

```
stash@{0}: On <branch_name>: <commit_hash> <stash_message>
stash@{1}: WIP on <another_branch>: ...
```

`stash@{0}` ist der neueste Stash.

**4. Einen Stash anwenden:**

Um die Änderungen aus einem Stash zurückzuholen, kannst du `git stash apply` verwenden. Dies wendet die Änderungen an, behält den Stash aber in der Liste. Standardmäßig wird der neueste Stash (`stash@{0}`) angewendet.

```bash
git stash apply
# oder um einen spezifischen Stash anzuwenden:
git stash apply stash@{1}
```

**5. Einen Stash anwenden und entfernen:**

Wenn du die Änderungen anwenden und den Stash sofort aus der Liste entfernen möchtest, verwende `git stash pop`. Auch dies bezieht sich standardmäßig auf den neuesten Stash.

```bash
git stash pop
# oder um einen spezifischen Stash zu poppen:
git stash pop stash@{1}
```

**6. Stash-Details anzeigen:**

Du kannst eine Zusammenfassung der Änderungen in einem Stash mit folgendem Befehl sehen:

```bash
git stash show
# oder für einen spezifischen Stash:
git stash show stash@{2}
```

Um das vollständige Diff eines Stashes zu sehen, füge das `-p` oder `--patch` Flag hinzu:

```bash
git stash show -p stash@{0}
```

**7. Ungetrackte Dateien stashen:**

Standardmäßig stasht `git stash` nur Änderungen an getrackten Dateien. Um ungetrackte Dateien einzubeziehen, verwende die Option `-u` oder `--include-untracked`:

```bash
git stash -u
git stash save -u "stash mit ungetrackten Dateien"
```

**8. Auch ignorierte Dateien stashen:**

Um sowohl ungetrackte als auch ignorierte Dateien einzubeziehen, verwende die Option `-a` oder `--all`:

```bash
git stash -a
git stash save -a "stash mit allen Dateien"
```

**9. Einen Branch aus einem Stash erstellen:**

Wenn du einige Änderungen gestasht hast und jetzt an ihnen in einem neuen Branch arbeiten möchtest, kannst du direkt aus dem Stash einen Branch erstellen:

```bash
git stash branch <new_branch_name> stash@{0}
# oder für den neuesten Stash:
git stash branch <new_branch_name>
```

Dieser Befehl erstellt einen neuen Branch basierend auf dem Commit, in dem der Stash erstellt wurde, wendet die gestashten Änderungen auf den neuen Branch an und verwirft dann den Stash.

**10. Stashes entfernen:**

* Um einen spezifischen Stash zu entfernen:
    ```bash
    git stash drop stash@{1}
    ```
* Um alle Stashes zu entfernen:
    ```bash
    git stash clear
    ```

## Häufiges Wechseln zwischen Branches oder Tags mit uncommitteten Änderungen

Hier erfährst du, wie du `git stash` nutzen kannst, um häufiges Wechseln zwischen Branches oder Tags zu erleichtern, wenn du uncommittete Änderungen hast:

**Szenario 1: Zu einem anderen Branch wechseln**

1.  **Stashe deine aktuellen Änderungen:**
    ```bash
    git stash save "WIP auf aktuellem Branch"
    ```
2.  **Wechsle zum Ziel-Branch:**
    ```bash
    git checkout <target_branch_name>
    # oder mit dem neueren `git switch` Befehl:
    git switch <target_branch_name>
    ```
3.  **Führe deine Arbeit auf dem Ziel-Branch aus.**
4.  **Wenn du zu deinem ursprünglichen Branch zurückkehren musst:**
    ```bash
    git checkout <original_branch_name>
    # oder
    git switch <original_branch_name>
    ```
5.  **Wende deine gestashten Änderungen wieder an:**
    ```bash
    git stash pop  # Wenn du den Stash anwenden und entfernen möchtest
    # oder
    git stash apply # Wenn du den Stash anwenden aber behalten möchtest
    ```
6.  **Löse eventuelle Merge-Konflikte**, die auftreten könnten, wenn sich der ursprüngliche Branch seit dem Stashen signifikant verändert hat.

**Szenario 2: Zu einem Tag wechseln**

Das direkte Wechseln zu einem Tag versetzt dich in einen "detached HEAD"-Zustand, was generell nicht zum Erstellen von Commits empfohlen wird. Wenn du nur den Code zu einem bestimmten Tag inspizieren möchtest:

1.  **Stashe deine aktuellen Änderungen:**
    ```bash
    git stash save "WIP vor Tag-Inspektion"
    ```
2.  **Wechsle zum Tag:**
    ```bash
    git checkout <tag_name>
    ```
3.  **Inspiziere den Code.**
4.  **Um zu deinem Branch zurückzukehren:**
    ```bash
    git checkout <your_branch_name>
    # oder
    git switch <your_branch_name>
    ```
5.  **Wende deine gestashten Änderungen wieder an:**
    ```bash
    git stash pop
    # oder
    git stash apply
    ```

**Szenario 3: Einen neuen Branch von einem Tag mit deinen gestashten Änderungen erstellen**

Wenn du an einem neuen Feature oder Fix basierend auf einem spezifischen Tag arbeiten möchtest und du gestashte Änderungen aus einem vorherigen Kontext hast:

1.  **Stashe deine aktuellen Änderungen (falls noch nicht geschehen):**
    ```bash
    git stash save "WIP"
    ```
2.  **Erstelle einen neuen Branch vom Tag:**
    ```bash
    git checkout -b <new_branch_name> <tag_name>
    # oder
    git switch -c <new_branch_name> <tag_name>
    ```
3.  **Wende deine gestashten Änderungen auf den neuen Branch an:**
    ```bash
    git stash pop # oder git stash apply
    ```
4.  **Löse eventuelle Merge-Konflikte.**

**Wichtige Überlegungen:**

* **Halte deine Stashes organisiert:** Verwende beschreibende Nachrichten, um deine Stashes leicht identifizieren zu können.
* **Stash ist lokal:** Stashes werden lokal in deinem Repository gespeichert und nicht zu Remote-Repositories gepusht.
* **Potenzial für Konflikte:** Wenn du einen Stash erneut anwendest, besteht die Möglichkeit von Merge-Konflikten, wenn sich der Branch, auf dem du anwendest, seit der Erstellung des Stashes signifikant verändert hat. Diese Konflikte musst du manuell lösen.
* **Erwäge die Erstellung temporärer Branches:** Für längerfristige Arbeiten, die du noch nicht committen möchtest, könnte das Erstellen eines temporären Branches ein besserer Ansatz sein als die starke Abhängigkeit von Stashes. Du kannst leicht zwischen Branches wechseln und deinen Fortschritt committen.

Indem du `git stash` effektiv nutzt, kannst du nahtlos zwischen Branches und Tags wechseln, selbst wenn du uncommittete Änderungen hast, was einen flexibleren und effizienteren Workflow ermöglicht. Denke daran, deine Stashes zu verwalten und sei darauf vorbereitet, potenzielle Merge-Konflikte zu behandeln.