---
audio: false
generated: true
lang: de
layout: post
title: Divergente Git-Branches
translated: true
type: note
---

Wenn sich Ihr lokaler `main`-Branch und der Remote-Branch `origin/main` in Git verzweigt haben – mit 74 bzw. 70 unterschiedlichen Commits – bedeutet dies, dass sie einen gemeinsamen Vorfahren teilen, aber seitdem eigene Commits entwickelt haben. Ihr Ziel ist es, Ihren lokalen `main`-Branch an `origin/main` anzugleichen, indem Sie Ihren lokalen Branch auf den gemeinsamen Vorfahren (den "Eltern-Branch beider") zurücksetzen und dann `git pull` verwenden, um die Remote-Änderungen zu übernehmen. Dadurch werden Ihre lokalen, abweichenden Commits effektiv zugunsten der Remote-Commits verworfen. Nachfolgend sind die Schritte aufgeführt, um dies zu erreichen.

### Schritte zur Behebung der Verzweigung

1. **Holen Sie die neuesten Remote-Änderungen ab**  
   Stellen Sie zunächst sicher, dass Ihr lokales Repository die neuesten Informationen vom Remote-Repository hat. Dies aktualisiert Ihre Referenz auf `origin/main`, ohne Ihren lokalen `main`-Branch vorerst zu verändern.

   ```bash
   git fetch origin
   ```

2. **Finden Sie den gemeinsamen Vorfahren-Commit**  
   Verwenden Sie `git merge-base`, um den gemeinsamen Vorfahren-Commit zwischen Ihrem lokalen `main` und `origin/main` zu identifizieren. Dies ist der Punkt, an dem sich die Branches verzweigt haben.

   ```bash
   ancestor=$(git merge-base main origin/main)
   ```

   Dieser Befehl speichert den Commit-Hash des gemeinsamen Vorfahren in der Variable `ancestor`.

3. **Setzen Sie den lokalen `main` auf den gemeinsamen Vorfahren zurück**  
   Setzen Sie Ihren lokalen `main`-Branch auf den gemeinsamen Vorfahren-Commit zurück. Die Option `--hard` stellt sicher, dass sowohl der Branch-Zeiger als auch Ihr Arbeitsverzeichnis aktualisiert werden, wodurch alle lokalen Commits und Änderungen, die nach diesem Punkt vorgenommen wurden, verworfen werden.

   ```bash
   git reset --hard $ancestor
   ```

   **Achtung**: Dieser Schritt verwirft alle uncommitteten Änderungen in Ihrem Arbeitsverzeichnis und Ihrer Staging-Area sowie die 74 Commits, die nur in Ihrem lokalen `main` vorhanden sind. Wenn Sie diese bewahren müssen, sollten Sie zuerst einen Backup-Branch erstellen (siehe "Optionale Sicherung" unten).

4. **Pullen Sie die Remote-Änderungen**  
   Holen Sie nun die Änderungen von `origin/main` ab. Da sich Ihr lokaler `main` jetzt auf dem gemeinsamen Vorfahren befindet und `origin/main` um 70 Commits voraus ist, wird Ihr lokaler `main` durch einen Fast-Forward auf `origin/main` aktualisiert.

   ```bash
   git pull origin main
   ```

   Danach ist Ihr lokaler `main`-Branch identisch mit `origin/main`, und alle lokalen, abweichenden Commits wurden verworfen.

### Vollständige Befehlssequenz

Hier ist die vollständige Sequenz der auszuführenden Befehle:

```bash
git fetch origin
ancestor=$(git merge-base main origin/main)
git reset --hard $ancestor
git pull origin main
```

### Was passiert?
- **Nach Schritt 1**: Ihr lokales Repository kennt den neuesten Zustand von `origin/main`.
- **Nach Schritt 2**: Sie haben den gemeinsamen Vorfahren-Commit identifiziert (z.B. einen Hash wie `abc123`).
- **Nach Schritt 3**: Ihr lokaler `main` wurde auf `abc123` zurückgesetzt, wodurch die 74 eindeutigen lokalen Commits verloren gehen.
- **Nach Schritt 4**: `git pull` führt einen Fast-Forward von `main` auf `origin/main` durch und übernimmt die 70 Commits vom Remote-Branch.

Das Ergebnis ist, dass Ihr lokaler `main` exakt mit `origin/main` übereinstimmt, was Ihr Ziel erfüllt, den Remote-Branch zu verwenden.

### Optionale Sicherung
Wenn Sie unsicher sind, ob Sie Ihre lokalen Commits verwerfen möchten, und sie für später bewahren wollen, erstellen Sie vor dem Zurücksetzen einen Backup-Branch:

```bash
git branch backup-main
```

Führen Sie diesen Befehl vor dem `git reset`-Befehl aus. Ihre 74 lokalen Commits verbleiben auf `backup-main`, und Sie können sie später bei Bedarf erneut einsehen.

### Wichtige Hinweise
- **Uncommittete Änderungen**: Wenn Sie uncommittete Änderungen (in Ihrem Arbeitsverzeichnis oder Ihrer Staging-Area) haben, die Sie behalten möchten, stashen Sie sie vor dem Zurücksetzen:
  ```bash
  git stash
  ```
  Nach Abschluss des Vorgangs können Sie sie mit `git stash pop` wiederherstellen.
- **Warum dies funktioniert**: Das Zurücksetzen auf den gemeinsamen Vorfahren und anschließende Pullen ermöglicht einen sauberen Fast-Forward auf `origin/main` und vermeidet Merge-Konflikte, die durch direktes Pullen bei verzweigten Branches entstehen könnten.

Indem Sie diese Schritte befolgen, setzen Sie Ihren lokalen `main`-Branch erfolgreich zurück, um wie gewünscht mit `origin/main` übereinzustimmen.