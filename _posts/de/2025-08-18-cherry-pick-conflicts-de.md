---
audio: false
generated: true
image: false
lang: de
layout: post
title: Konfliktfreie Cherry-Picking-Lösungen
translated: true
type: note
---

Git **cherry-pick** ist ein Befehl, der es ermöglicht, einen Commit von einem Branch zu nehmen und auf einen anderen Branch anzuwenden, ohne die gesamte Branch-Historie zu mergen.

---

### So funktioniert es

* Wenn Sie `git cherry-pick <commit-hash>` ausführen, macht Git Folgendes:

  1. Findet die Änderungen, die durch diesen Commit eingeführt wurden (ein Diff gegenüber seinem Parent-Commit).
  2. Wendet diese Änderungen erneut auf Ihren aktuellen Branch an und erstellt dabei einen neuen Commit mit einer neuen Hash-Adresse.
  3. Das bedeutet, der Commit-Inhalt wird wiederverwendet, aber die Abstammung des ursprünglichen Commits wird nicht beibehalten.

Man kann es sich so vorstellen:
*"Nimm einfach den Patch dieses einen Commits und füge ihn dort ein, wo ich mich gerade befinde."*

---

### Warum Konflikte auftreten

Konflikte entstehen, weil cherry-pick Änderungen **aus ihrem ursprünglichen Kontext heraus** anwendet. Einige häufige Gründe:

1. **Code-Drift**
   Wenn sich der Ziel-Branch in denselben Codebereichen seit dem ursprünglichen Commit geändert hat, kann Git den Patch nicht sauber anwenden. Zum Beispiel:

   * Der ursprüngliche Commit hat eine Funktion in `fileA` hinzugefügt.
   * Im Ziel-Branch hat jemand diese Funktion umbenannt oder entfernt.
     → Konflikt beim Cherry-Picken.

2. **Fehlende abhängige Commits**
   Manchmal hängt ein Commit von früheren Commits ab (z.B. Refactorings, Umbenennungen von Variablen). Wenn Sie ihn ohne diese Commits cherry-picken, ist der Kontext ein anderer und es treten Konflikte auf.

3. **Überlappende Änderungen**
   Wenn beide Branches die gleichen Codezeilen bearbeitet haben (selbst aus unterschiedlichen Gründen), kann Git nicht automatisch entscheiden und hält für eine manuelle Auflösung an.

---

### Beispielszenario

* `feature-branch` hat die Commits A → B → C.
* Sie möchten Commit B in `main` haben.
* Sie führen `git checkout main && git cherry-pick B` aus.
* Wenn `main` bereits dieselbe Datei/dieselben Zeilen wie B bearbeitet hat, meldet Git einen Konflikt. Sie müssen die Datei öffnen, die Unterschiede auflösen, `git add` ausführen und dann `git cherry-pick --continue`.

---

👉 Kurz gesagt: **Cherry-pick spielt einen Patch in einem neuen Kontext ab. Konflikte treten auf, wenn sich dieser Kontext zu stark vom ursprünglichen unterscheidet.**

Möchten Sie, dass ich Ihnen auch **Best Practices zur Reduzierung von Cherry-Pick-Konflikten** durchgehe (wie das Sortieren von Commits, die Verwendung von `-x` oder vorheriges Rebasen)?