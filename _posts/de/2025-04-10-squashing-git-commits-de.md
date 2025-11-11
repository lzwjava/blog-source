---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Git-Commit-Nach-Autor-Zusammenführen
translated: true
type: note
---

### Das Ziel verstehen
Git verfügt nicht über einen integrierten "squash by author"-Befehl, aber Sie können dies mit einem interaktiven Rebase erreichen, um Commits manuell zu gruppieren und zu squashen. Die Idee ist, die letzten 10 Commits (angenommen, sie stammen von 3 verschiedenen Autoren) zu nehmen und die Commits jedes Autors in einen einzelnen Commit pro Autor zusammenzuführen, sodass am Ende insgesamt 3 Commits übrig bleiben.

Dies setzt voraus:
- Sie befinden sich auf dem Branch mit diesen Commits (z.B. main oder Feature-Branch).
- Die Commits sind linear (keine Merges).
- Sie kennen die Autoren im Voraus.

Wenn die Commits nicht-linear oder komplex sind, kann dies eine sorgfältige Behandlung erfordern, um Konflikte zu vermeiden.

### Schritte zum Squashen von Commits nach Autor
1. **Die letzten 10 Commits prüfen**  
   Führen Sie `git log --oneline -10` aus, um die letzten 10 Commits einschließlich ihrer Hashes, Autoren und Nachrichten zu sehen. Identifizieren Sie die Autoren (z.B. mit `git log --format="%an" -10 | sort | uniq`, um eindeutige Autoren aufzulisten).

2. **Einen interaktiven Rebase starten**  
   Identifizieren Sie den Commit vor dem 10. Commit. Wenn sich Ihr neuester Commit bei HEAD befindet und es 10 Commits gibt, ist die Basis `HEAD~10`. Führen Sie aus:  
   ```
   git rebase -i HEAD~10
   ```  
   Dies öffnet einen Editor (standardmäßig vim) mit einer Liste der letzten 10 Commits. Es sieht so aus:  
   ```
   pick abc123 Erster Commit von Autor A  
   pick def456 Zweiter Commit von Autor A  
   pick ghi789 Commit von Autor B  
   pick jkl012 Commit von Autor C  
   ... (weitere Commits)
   ```  
   - Jede Zeile beginnt mit `pick`.

3. **Commits zum Squashen nach Autor markieren**  
   Ändern Sie für jeden Autor `pick` in `s` (squash) bei allen seinen Commits, außer bei dem ersten, den Sie für diesen Autor behalten möchten. Legen Sie fest:
   - Einen "Keep"-Commit pro Autor (wählen Sie den frühesten oder relevantesten als Basis).
   - Ändern Sie den Rest dieses Autors in `s`, um sie in den Basis-Commit zu squashen.  
   Beispiel (für 3 Autoren):  
   ```
   pick abc123 Erster Commit von Autor A (diesen behalten)  
   s    def456 Zweiter Commit von Autor A (in den obigen squashen)  
   pick ghi789 Commit von Autor B (diesen behalten)  
   pick jkl012 Erster Commit von Autor C (diesen behalten)  
   s    mno345 Zweiter Commit von Autor C (in den obigen squashen)  
   ```  
   Speichern Sie und verlassen Sie den Editor. Dadurch wird der Rebase gestartet.

4. **Commit-Nachrichten während des Rebases bearbeiten**  
   Bei jedem Squash-Vorgang hält Git an und lässt Sie die Commit-Nachricht bearbeiten (die der gesquashten Commits kombiniert). Aktualisieren Sie sie auf etwas wie "Squashed commits by Author A: description". Speichern Sie und fahren Sie fort.  
   Wenn es weitere Squashes gibt, wiederholen Sie dies für jeden Autor. Führen Sie nach jeder Bearbeitung `git rebase --continue` aus.  
   Wenn Konflikte auftreten (selten bei einfachem Squash), lösen Sie sie mit `git add <Datei>` und dann `git rebase --continue`.

5. **Verifizieren und Pushen**  
   Nach Abschluss des Rebases prüfen Sie das Log: `git log --oneline -10`. Sie sollten 3 Commits sehen, jeweils von einem Autor.  
   Force-push, wenn Sie auf einen gemeinsamen Branch pushen (destruktiver Rebase): `git push --force-with-lease origin Branch-Name`.  
   **Warnung:** Führen Sie einen Force-Push nur durch, wenn Sie sicher sind, dass die alten Commits nicht anderweitig benötigt werden, da dies die History überschreibt.

### Tipps und Hinweise
- Wenn Autoren viele Commits haben, gruppieren Sie sie effizient in der Rebase-Liste (alle von Autor A zusammen, usw.).
- Für die Automatisierung können Tools wie `git-interactive-rebase-tool` oder Skripte helfen, aber ein manueller Rebase ist unkompliziert.
- Wenn Sie nach exaktem Autor filtern müssen, verwenden Sie vorher `git log --author="Autor Name"` zur Bestätigung.
- Testen Sie zuerst auf einem Backup-Branch, um Datenverlust zu vermeiden.

Für mehr zu Rebase: `git help rebase`. Wenn dies nicht genau auf Ihr Szenario zutrifft, geben Sie weitere Details zur Commit-Struktur an.