---
audio: false
generated: true
lang: de
layout: post
title: Verwenden von Git Pull und Push mit Flachen Klonen
translated: true
type: note
---

Ja, Sie können `git pull` oder `git push` weiterhin verwenden, nachdem Sie ein Repository mit einer begrenzten Historie mittels `--depth=20` geklont haben. Es sind jedoch einige wichtige Punkte zu beachten:

### 1. **Was `--depth=20` bewirkt**
   - Die Option `--depth=20` erstellt einen *flachen Klon* (shallow clone), der nur die letzten 20 Commits (oder die angegebene Anzahl) vom Standard-Branch (oder dem angegebenen Branch, falls Sie `--branch` verwenden) abruft.
   - Dies reduziert die Menge der heruntergeladenen Historie, macht den Klon schneller und kleiner, aber das Repository enthält nicht die vollständige Commit-Historie.

### 2. **Verwendung von `git pull` mit einem flachen Klon**
   - **Ja, Sie können `git pull` verwenden** in einem flachen Klon, um neue Commits aus dem Remote-Repository abzurufen und zusammenzuführen.
   - Standardmäßig wird `git pull` neue Commits abrufen und die flache Historie aktualisieren, sodass sie mit dem Remote-Branch konsistent bleibt.
   - Wenn dem Remote-Branch neue Commits hinzugefügt werden, wird `git pull` diese abrufen und die Historie in Ihrem lokalen Repository erweitern, wobei der flache Charakter des Klons weiterhin respektiert wird.

   **Hinweis**: Wenn sich die Historie des Branches so ändert, dass Commits betroffen sind, die älter als Ihre flache Historie sind (z.B. ein Force-Push oder Rebase auf dem Remote), können Probleme auftreten. In solchen Fällen müssen Sie möglicherweise die Historie vertiefen (mit `git fetch --deepen=<n>` oder `git fetch --unshallow`, um die vollständige Historie abzurufen), um Konflikte zu lösen oder die Arbeit fortzusetzen.

### 3. **Verwendung von `git push` mit einem flachen Klon**
   - **Ja, Sie können `git push` verwenden**, um Ihre lokalen Commits zum Remote-Repository zu übertragen.
   - Ein flacher Klon schränkt Ihre Fähigkeit nicht ein, neue Commits zu erstellen und sie an das Remote-Repository zu übertragen, solange das Remote Ihre Änderungen akzeptiert.
   - Wenn das Remote-Repository jedoch Operationen erfordert, die von der vollständigen Historie abhängen (z.B. ein Merge oder Rebase, der ältere Commits einbezieht), müssen Sie möglicherweise mehr Historie abrufen, um den Push erfolgreich abzuschließen.

### 4. **Einschränkungen flacher Klone**
   - **Begrenzte Historie**: Einige Git-Operationen wie `git log`, `git blame` oder `git rebase` können eingeschränkt sein, weil ältere Commits lokal nicht verfügbar sind.
   - **Mergen und Rebasen**: Wenn Sie mit Commits außerhalb Ihrer flachen Historie mergen oder rebasen müssen, müssen Sie möglicherweise mehr Historie mit `git fetch --deepen=<n>` oder `git fetch --unshallow` abrufen.
   - **Force-Pushes**: Wenn der Remote-Branch umgeschrieben wird (z.B. mit `git push --force`), könnte Ihr flacher Klon nicht genug Kontext haben, um die Änderungen zu verarbeiten, was Sie zwingt, die Historie zu vertiefen oder erneut zu klonen.

### 5. **So vertiefen Sie einen flachen Klon (falls nötig)**
   Wenn Sie Probleme mit `git pull` oder `git push` aufgrund der begrenzten Historie haben, können Sie zusätzliche Historie abrufen:
   - **Um eine bestimmte Anzahl von Commits vertiefen**:
     ```bash
     git fetch --deepen=20
     ```
     Dies ruft 20 weitere Commits der Historie ab.
   - **Die vollständige Historie abrufen**:
     ```bash
     git fetch --unshallow
     ```
     Dies verwandelt Ihren flachen Klon in einen vollständigen Klon mit der gesamten Historie.

### 6. **Praktischer Ratschlag**
   - Ein flacher Klon mit `--depth=20` ist für die meisten Workflows in der Regel ausreichend, insbesondere wenn Sie nur an recent changes arbeiten oder kleine Updates beisteuern.
   - Wenn Sie erwarten, die vollständige Historie zu benötigen (z.B. für komplexe Merges, Rebases oder Debugging), sollten Sie in Betracht ziehen, das Repository vollständig ohne die `--depth`-Option zu klonen oder die Historie später bei Bedarf zu vertiefen.
   - Stellen Sie immer sicher, dass Sie Schreibzugriff auf das Remote-Repository (z.B. `git@github.com:cisco/ChezScheme.git`) haben, bevor Sie versuchen, zu pushen.

### Beispiel Workflow
```bash
# Klonen mit begrenzter Historie
git clone git@github.com:cisco/ChezScheme.git --depth=20
cd ChezScheme

# Änderungen vornehmen und committen
git commit -m "My changes"

# Neueste Änderungen abrufen
git pull origin main

# Ihre Änderungen übertragen
git push origin main
```

Wenn Sie auf Probleme aufgrund des flachen Klons stoßen, vertiefen Sie die Historie wie oben beschrieben.

### Zusammenfassung
Ja, Sie können `git pull` und `git push` mit einem flachen Klon verwenden, der mit `--depth=20` erstellt wurde. Möglicherweise müssen Sie jedoch für bestimmte Operationen zusätzliche Historie abrufen, wenn die flache Historie nicht ausreicht. Verwenden Sie `git fetch --deepen` oder `git fetch --unshallow`, um etwaige Einschränkungen zu beheben.