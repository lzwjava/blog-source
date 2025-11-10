---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Überblick und Verwendung von Git Cherry-Pick
translated: true
type: note
---

### Was ist Git Cherry-Pick?

Git cherry-pick ist ein Befehl, der es ermöglicht, die Änderungen eines bestimmten Commits (oder einer Gruppe von Commits) auf Ihren aktuellen Branch anzuwenden und dabei einen neuen Commit mit diesen Änderungen zu erstellen. Es ist nützlich, wenn Sie eine bestimmte Fehlerbehebung oder ein Feature aus einem Branch übernehmen möchten, ohne den gesamten Branch zu mergen. Im Gegensatz zu einem Merge, der die gesamte Historie integriert, kopiert cherry-pick Änderungen selektiv.

### Wie Git Cherry-Pick intern funktioniert

1.  **Commit auswählen**: Sie geben einen Commit-Hash an (z. B. via `git log`, um ihn zu finden), der die gewünschten Änderungen enthält.
2.  **Änderungen anwenden**: Git nimmt das Diff (die tatsächlichen Code-Änderungen) aus diesem Commit und versucht, es im Arbeitsverzeichnis Ihres aktuellen Branches anzuwenden, wobei nach Möglichkeit die Drei-Wege-Merge-Logik von Git verwendet wird.
3.  **Neuen Commit erstellen**: Wenn erfolgreich, wird ein neuer Commit in Ihrem Branch erstellt mit:
    *   Den gleichen Änderungen wie der ursprüngliche Commit.
    *   Einem neuen Commit-Hash (da es ein neuer Commit ist).
    *   Einer Commit-Message, die auf das Original verweist (z. B. über das Flag `-x`, um "cherry picked from commit <hash>" anzuhängen).

    Wenn Merge-Konflikte auftreten (z. B. der Ziel-Branch inkompatible Änderungen enthält), hält Git an und lässt Sie diese manuell beheben, bevor der Commit erstellt wird.

Der Prozess verändert nicht die Historie des ursprünglichen Commits – er kopiert nur die Änderungen. Dies macht cherry-pick ideal für das Backporting von Bugfixes oder das selektive Anwenden von Features.

### Grundlegende Verwendungsschritte

1.  Stellen Sie sicher, dass Sie sich auf dem Ziel-Branch befinden (wechseln mit `git checkout <branch>`).
2.  Finden Sie den gewünschten Commit-Hash (z. B. `git log --oneline`).
3.  Führen Sie aus: `git cherry-pick <commit-hash>`
    *   Für mehrere: `git cherry-pick <hash1> <hash2>`
    *   Mit Optionen wie `-n` (kein Commit, für die Staging-Area) oder `-x` (verweist auf das Original).
4.  Bei Konflikten bearbeiten Sie die Dateien, staggen sie mit `git add` und führen dann `git cherry-pick --continue` aus.
5.  Um den Vorgang abzubrechen: `git cherry-pick --abort`.

### Beispielszenario

Angenommen, Sie haben einen Feature-Branch mit den Commits A -> B -> C, und Sie möchten den Commit B auf den main-Branch cherry-picken.

*   Auf main: `git checkout main`
*   `git cherry-pick B` (ersetzen Sie B mit dem tatsächlichen Hash)

Dies fügt die Änderungen aus B als neuen Commit D auf main hinzu, ohne A oder C zu übernehmen. Das originale B verbleibt im Feature-Branch.

### Einschränkungen und Tipps

*   Vermeiden Sie das Cherry-Picken von Merge-Commits (Commits mit mehreren Parents), da dies zu Problemen führen kann – verwenden Sie `git cherry-pick -m 1 <merge-commit>`, um einen Parent anzugeben.
*   Es bewahrt nicht die Metadaten des Commits wie das Autor-Datum, aber `git cherry-pick --edit` ermöglicht es Ihnen, die Nachricht zu ändern.
*   Für aufeinanderfolgende Änderungen sollten Sie mehrere Commits in der richtigen Reihenfolge cherry-picken, um Abhängigkeitsprobleme zu vermeiden.
*   Testen Sie immer nach einem Cherry-Pick, da dies Bugs verursachen kann, wenn sich die Kontexte unterscheiden.

Weitere Details finden Sie in der offiziellen Git-Dokumentation: https://git-scm.com/docs/git-cherry-pick. Wenn Sie auf spezifische Probleme stoßen, teilen Sie Ihre Git-Log-Ausgabe!