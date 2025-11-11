---
audio: false
generated: true
lang: de
layout: post
title: VS Code Quellcodeverwaltung Leitfaden
translated: true
type: note
---

Visual Studio Code (VS Code) bietet eine umfassende integrierte Unterstützung für Source Control, die es Entwicklern ermöglicht, Versionskontrollsysteme (VCS) wie Git, Mercurial und andere direkt im Editor zu verwalten. Diese Anleitung bietet einen umfassenden Überblick über die Verwendung von Source Control in VS Code, konzentriert sich auf Git, da es das am häufigsten verwendete VCS ist, und behandelt Einrichtung, Schlüsselfunktionen, Workflows und erweiterte Nutzung.

### Überblick über Source Control in VS Code
Die Source Control-Ansicht von VS Code bietet eine intuitive Oberfläche zur Interaktion mit Versionskontrollsystemen. Sie integriert sich standardmäßig mit Git und unterstützt Erweiterungen für andere VCS. Die Source Control-Ansicht zeigt Änderungen an, ermöglicht Staging, Commits, Branching, Merging und mehr, alles ohne den Editor zu verlassen. Nachfolgend finden Sie eine Schritt-für-Schritt-Anleitung zur effektiven Nutzung von Source Control.

### 1. **Source Control in VS Code einrichten**
Um Source Control zu verwenden, benötigen Sie eine installierte Git-Installation und ein initialisiertes Repository. So richten Sie es ein:

#### Voraussetzungen
- **Git installieren**: Laden Sie Git von [git-scm.com](https://git-scm.com/) herunter und installieren Sie es. Überprüfen Sie die Installation, indem Sie `git --version` in einem Terminal ausführen.
- **Git konfigurieren**:
  ```bash
  git config --global user.name "Ihr Name"
  git config --global user.email "ihre.email@beispiel.com"
  ```
- **VS Code installieren**: Stellen Sie sicher, dass Sie die neueste Version von VS Code von [code.visualstudio.com](https://code.visualstudio.com/) installiert haben.

#### Ein Git-Repository initialisieren
1. Öffnen Sie einen Projektordner in VS Code.
2. Öffnen Sie das Terminal (Ctrl+` oder Cmd+` unter macOS) und führen Sie aus:
   ```bash
   git init
   ```
   Dies erstellt einen `.git`-Ordner in Ihrem Projekt und initialisiert es als Git-Repository.
3. Alternativ können Sie ein bestehendes Repository klonen:
   ```bash
   git clone <repository-url>
   ```
   Öffnen Sie anschließend den geklonten Ordner in VS Code.

#### Source Control-Ansicht aktivieren
- Öffnen Sie die Source Control-Ansicht, indem Sie auf das Source Control-Symbol in der Aktivitätsleiste klicken (drittes Symbol von oben, ähnelt einem Branch) oder `Ctrl+Shift+G` (Windows/Linux) bzw. `Cmd+Shift+G` (macOS) drücken.
- Wenn ein Git-Repository erkannt wird, zeigt VS Code die Source Control-Ansicht mit Optionen zur Verwaltung von Änderungen an.

### 2. **Verwendung der Source Control-Ansicht**
Die Source Control-Ansicht ist das zentrale Hub für Versionskontrollaufgaben. Sie zeigt:
- **Changes**: Dateien, die seit dem letzten Commit geändert, hinzugefügt oder gelöscht wurden.
- **Staged Changes**: Dateien, die für den Commit bereit sind.
- **Commit Message Box**: Hier geben Sie Commit-Nachrichten ein.
- **Actions**: Schaltflächen für Commit, Aktualisieren und mehr.

#### Allgemeiner Workflow
1. **Änderungen vornehmen**: Bearbeiten Sie Dateien in Ihrem Projekt. VS Code erkennt Änderungen automatisch und listet sie unter "Changes" in der Source Control-Ansicht auf.
2. **Änderungen stagen**:
   - Klicken Sie auf das `+`-Symbol neben einer Datei, um sie zu stagen, oder verwenden Sie die Option "Stage All Changes" (Drei-Punkte-Menü > Stage All Changes).
   - Staging bereitet Änderungen für den nächsten Commit vor.
3. **Eine Commit-Nachricht schreiben**:
   - Geben Sie eine beschreibende Nachricht in das Textfeld oben in der Source Control-Ansicht ein.
   - Beispiel: `Add user authentication feature`.
4. **Änderungen committen**:
   - Klicken Sie auf das Häkchensymbol oder drücken Sie `Ctrl+Enter` (Windows/Linux) bzw. `Cmd+Enter` (macOS), um die gestagten Änderungen zu committen.
   - Verwenden Sie das Drei-Punkte-Menü, um zwischen "Commit All", "Commit Staged" oder "Commit All and Push" zu wählen.
5. **Zum Remote-Repository pushen**:
   - Wenn Sie mit einem Remote-Repository (z.B. GitHub) verbunden sind, pushen Sie Änderungen mit der Option "Push" im Drei-Punkte-Menü oder führen Sie `git push` im Terminal aus.

### 3. **Schlüsselfunktionen von Source Control in VS Code**
VS Code bietet mehrere Funktionen zur Optimierung der Versionskontrolle:

#### Diff-Ansicht
- Klicken Sie auf eine Datei unter "Changes", um eine Side-by-Side-Diff-Ansicht zu öffnen, die die Modifikationen im Vergleich zum letzten Commit anzeigt.
- Verwenden Sie Inline-Aktionen, um bestimmte Zeilen zu stagen oder zu verwerfen.

#### Branch-Management
- Branches wechseln: Klicken Sie auf den Branch-Namen in der Statusleiste unten links oder verwenden Sie das Branch-Menü in der Source Control-Ansicht (Drei-Punkte-Menü > Branch > Checkout to...).
- Einen neuen Branch erstellen: Wählen Sie "Create Branch" aus dem Branch-Menü, geben Sie einen Namen ein und bestätigen Sie.
- Branches mergen: Verwenden Sie "Branch > Merge Branch" und wählen Sie den Branch aus, der in den aktuellen Branch gemergt werden soll.

#### Pull und Fetch
- **Pull**: Synchronisieren Sie Änderungen vom Remote-Repository mit der Option "Pull" im Drei-Punkte-Menü.
- **Fetch**: Rufen Sie Remote-Änderungen ohne Merge mit "Fetch" ab.

#### Konflikte lösen
- Beim Mergen oder Pullen können Konflikte auftreten. VS Code hebt Konflikte in Dateien hervor und bietet eine Inline-Oberfläche zur Konfliktlösung:
  - Wählen Sie "Accept Current Change", "Accept Incoming Change", "Accept Both Changes" oder bearbeiten Sie die Datei manuell.
  - Stagen und committen Sie die aufgelöste Datei.

#### Git Lens Extension
Für erweiterte Git-Funktionen installieren Sie die **GitLens**-Erweiterung:
- Zeigen Sie Commit-Historie, Blame-Annotationen und Dateiänderungen an.
- Greifen Sie auf Repository-Einblicke wie letzte Commits und Stashes zu.
- Installieren Sie sie über die Extensions-Ansicht (`Ctrl+Shift+X` oder `Cmd+Shift+X`).

### 4. **Erweiterte Nutzung**
#### Stashing von Änderungen
- Speichern Sie uncommittete Änderungen temporär:
  - Gehen Sie zum Drei-Punkte-Menü > Stash > Stash.
  - Wenden Sie Stashes später über das gleiche Menü an oder "pop" Sie sie.
- Nützlich, um Branches zu wechseln, ohne unvollständige Arbeit zu committen.

#### Git-Befehle im Terminal
- Für Aufgaben, die nicht direkt in der UI unterstützt werden, verwenden Sie das integrierte Terminal:
  ```bash
  git rebase <branch>
  git cherry-pick <commit>
  git log --oneline
  ```

#### Anpassung von Source Control
- **Einstellungen**: Passen Sie das Source Control-Verhalten in den VS Code-Einstellungen an (`Ctrl+,` oder `Cmd+,`):
  - `git.autoRepositoryDetection`: Automatische Git-Repository-Erkennung aktivieren/deaktivieren.
  - `git.enableSmartCommit`: Alle Änderungen committen, wenn keine Dateien gestagt sind.
- **SCM-Provider**: Installieren Sie Erweiterungen für andere VCS wie Mercurial oder SVN.

#### GitHub-Integration
- Verwenden Sie die **GitHub Pull Requests and Issues**-Erweiterung, um PRs und Issues direkt in VS Code zu verwalten.
- Authentifizieren Sie sich bei GitHub über das Accounts-Menü (unten links), um von/zu GitHub-Repositories zu pushen/pullen.

### 5. **Beispiel-Workflow: Erstellen und Pushen eines Feature-Branches**
Hier ein praktisches Beispiel für einen gängigen Git-Workflow in VS Code:

# Beispiel-Git-Workflow in VS Code

## Schritte zum Erstellen und Pushen eines Feature-Branches

1. **Einen neuen Branch erstellen**:
   - Klicken Sie in der Source Control-Ansicht auf den Branch-Namen in der Statusleiste oder verwenden Sie das Drei-Punkte-Menü > Branch > Create Branch.
   - Benennen Sie den Branch, z.B. `feature/add-login`.
   - VS Code wechselt zum neuen Branch.

2. **Änderungen vornehmen und stagen**:
   - Bearbeiten Sie Dateien (z.B. fügen Sie eine Login-Komponente zu `src/Login.js` hinzu).
   - In der Source Control-Ansicht erscheinen Dateien unter "Changes".
   - Klicken Sie auf das `+`-Symbol, um Änderungen zu stagen, oder wählen Sie "Stage All Changes".

3. **Änderungen committen**:
   - Geben Sie eine Commit-Nachricht ein, z.B. `Add login component`.
   - Klicken Sie auf das Häkchensymbol oder drücken Sie `Ctrl+Enter` (Windows/Linux) bzw. `Cmd+Enter` (macOS), um zu committen.

4. **Den Branch pushen**:
   - Wenn kein Remote existiert, fügen Sie einen hinzu:
     ```bash
     git remote add origin <repository-url>
     ```
   - Pushen Sie den Branch: Drei-Punkte-Menü > Push, oder führen Sie aus:
     ```bash
     git push -u origin feature/add-login
     ```

5. **Einen Pull Request erstellen**:
   - Wenn Sie GitHub verwenden, öffnen Sie das Repository in einem Browser oder verwenden Sie die GitHub Pull Requests-Erweiterung, um einen PR zu erstellen.
   - Verlinken Sie den PR mit dem `feature/add-login`-Branch.

## Tipps
- Ziehen Sie regelmäßig Updates aus dem Main-Branch, um Konflikte zu vermeiden.
- Verwenden Sie beschreibende Commit-Nachrichten für eine bessere Zusammenarbeit.
- Installieren Sie GitLens für erweiterte Commit-Historie und Blame-Ansichten.

### 6. **Behebung häufiger Probleme**
- **Git wird nicht erkannt**: Stellen Sie sicher, dass Git installiert und in Ihrem System-PATH vorhanden ist. Starten Sie VS Code nach der Installation neu.
- **Authentifizierungsfehler**: Konfigurieren Sie SSH-Keys oder verwenden Sie ein Personal Access Token für GitHub/GitLab. Authentifizieren Sie sich über das Accounts-Menü.
- **Merge-Konflikte**: Verwenden Sie die Inline-Konfliktlösungstools oder bearbeiten Sie Dateien manuell, stagen und committen Sie sie dann.
- **Langsame Leistung**: Deaktivieren Sie `git.autoRepositoryDetection` für große Projekte oder verwenden Sie GitLens für optimierte Git-Operationen.

### 7. **Best Practices**
- **Oft committen**: Machen Sie kleine, logische Commits, um den Fortschritt zu verfolgen.
- **Beschreibende Nachrichten verwenden**: Folgen Sie einer Konvention wie `<type>(<scope>): <description>` (z.B. `feat(auth): add login endpoint`).
- **Regelmäßig pullen**: Bleiben Sie mit dem Remote-Repository synchron, um Konflikte zu minimieren.
- **Stashes sichern**: Stellen Sie vor dem Anwenden von Stashes sicher, dass sie keine wichtigen Änderungen überschreiben.
- **Erweiterungen nutzen**: Verwenden Sie GitLens, Git History oder Git Graph für erweiterte Funktionalität.

### 8. **Zusätzliche Ressourcen**
- **VS Code-Dokumentation**: [Version Control in VS Code](https://code.visualstudio.com/docs/editor/versioncontrol)
- **Git-Dokumentation**: [git-scm.com/doc](https://git-scm.com/doc)
- **GitLens-Erweiterung**: Verfügbar im VS Code Marketplace.
- **GitHub Pull Requests-Erweiterung**: Zum Verwalten von PRs und Issues.

Diese Anleitung behandelt die Grundlagen und erweiterten Funktionen von Source Control in VS Code mit einem Fokus auf Git. Indem Sie diese Schritte und Best Practices befolgen, können Sie Versionskontroll-Workflows effizient direkt im Editor verwalten.