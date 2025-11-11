---
audio: false
generated: true
lang: de
layout: post
title: TortoiseGit
translated: true
type: note
---

TortoiseGit ist eine Windows-Shell-Erweiterung, die eine benutzerfreundliche Oberfläche für Git, das beliebte Versionskontrollsystem, bereitstellt. Es integriert sich direkt in den Windows Explorer und ermöglicht es Ihnen, Git-Operationen über Kontextmenüs durchzuführen. Diese Anleitung behandelt die Installation, Konfiguration und Verwendung von TortoiseGit unter Windows sowie häufige Aufgaben und Best Practices.

### Überblick über TortoiseGit
TortoiseGit basiert auf msysGit (Git für Windows) und bietet eine grafische Oberfläche für Git-Befehle. Es ist ideal für Benutzer, die eine GUI gegenüber Git-Befehlen auf der Kommandozeile bevorzugen. Wichtige Funktionen sind:
- Integration von Kontextmenüs im Windows Explorer.
- Visuelle Diff- und Merge-Tools.
- Unterstützung für gängige Git-Workflows (Commit, Push, Pull, Branch, Merge usw.).
- Integration mit beliebten Issue-Trackern und externen Tools.

### Voraussetzungen
Stellen Sie vor der Installation von TortoiseGit sicher, dass Sie Folgendes haben:
- Ein Windows-Betriebssystem (Windows 10 oder höher wird empfohlen).
- Git für Windows installiert (TortoiseGit setzt darauf auf).
- Grundlegendes Verständnis von Git-Konzepten (Repositories, Commits, Branches usw.).

### Installation
1. **Git für Windows installieren**:
   - Laden Sie die neueste Version von [Git for Windows](https://gitforwindows.org/) oder [Git SCM](https://git-scm.com/downloads) herunter.
   - Führen Sie das Installationsprogramm aus und folgen Sie den Anweisungen. Empfohlene Einstellungen:
     - Verwenden Sie den Standard-Editor (z.B. Notepad) oder wählen Sie einen wie VS Code.
     - Wählen Sie „Use Git from the Windows Command Prompt“ für die Zugänglichkeit.
     - Wählen Sie „OpenSSL“ für HTTPS-Transport.
     - Wählen Sie „Checkout as-is, commit as-is“ für Zeilenenden (es sei denn, Sie arbeiten in plattformübergreifenden Teams).
   - Schließen Sie die Installation ab.

2. **TortoiseGit installieren**:
   - Laden Sie die neueste Version von der [offiziellen TortoiseGit-Website](https://tortoisegit.org/download/) herunter.
   - Führen Sie das Installationsprogramm aus:
     - Wählen Sie die Standardsprache und Komponenten.
     - Stellen Sie sicher, dass Git für Windows erkannt wird (TortoiseGit fordert Sie ggf. auf, falls es fehlt).
     - Installieren Sie TortoiseGitPlink (empfohlen für SSH), falls benötigt.
   - Starten Sie Ihren Computer bei Aufforderung neu.

3. **Installation überprüfen**:
   - Klicken Sie mit der rechten Maustaste in einen beliebigen Ordner im Windows Explorer. Sie sollten TortoiseGit-Optionen wie „Git Clone“, „Git Create Repository here“ usw. sehen.

### Erste Konfiguration
Konfigurieren Sie nach der Installation TortoiseGit für Ihre Benutzerdaten und Präferenzen:
1. **Benutzerinformationen festlegen**:
   - Klicken Sie mit der rechten Maustaste in einen Ordner und wählen Sie **TortoiseGit > Einstellungen**.
   - Navigieren Sie im Einstellungsfenster zu **Git > Config**.
   - Geben Sie Ihren Namen und Ihre E-Mail-Adresse ein (dieselben wie bei GitHub, GitLab usw. verwendet):
     ```
     Name: Ihr Name
     Email: ihre.email@beispiel.com
     ```
   - Klicken Sie auf **Übernehmen** und **OK**.

2. **SSH konfigurieren (Optional)**:
   - Wenn Sie SSH für Remote-Repositories verwenden, richten Sie einen SSH-Schlüssel ein:
     - Öffnen Sie **PuTTYgen** (mit TortoiseGit installiert).
     - Generieren Sie ein neues SSH-Schlüsselpaar, speichern Sie den privaten Schlüssel und kopieren Sie den öffentlichen Schlüssel.
     - Fügen Sie den öffentlichen Schlüssel zu Ihrem Git-Hosting-Dienst hinzu (z.B. GitHub, GitLab).
     - Wählen Sie in den TortoiseGit-Einstellungen unter **Git > Remote** TortoiseGitPlink als SSH-Client aus.

3. **Diff- und Merge-Tools festlegen**:
   - Wählen Sie unter **TortoiseGit > Einstellungen > Diff Viewer** ein Tool wie TortoiseGitMerge (Standard) oder ein externes Tool wie Beyond Compare.
   - Konfigurieren Sie für das Zusammenführen unter **Merge Tool** (TortoiseGitMerge wird für Anfänger empfohlen).

### Grundlegende Verwendung
Im Folgenden finden Sie häufige TortoiseGit-Operationen, die über Kontextmenüs im Windows Explorer zugänglich sind.

#### 1. **Repository klonen**
   - Klicken Sie mit der rechten Maustaste in einen Ordner und wählen Sie **Git Clone**.
   - Geben Sie im Dialogfeld:
     - Die Repository-URL ein (z.B. `https://github.com/benutzername/repo.git`).
     - Geben Sie das lokale Verzeichnis für das Repository an.
     - Wählen Sie optional einen Branch aus oder laden Sie SSH-Schlüssel.
   - Klicken Sie auf **OK**, um das Repository zu klonen.

#### 2. **Neues Repository erstellen**
   - Navigieren Sie zu einem Ordner, klicken Sie mit der rechten Maustaste und wählen Sie **Git Create Repository here**.
   - Aktivieren Sie „Make it Bare“, wenn Sie ein serverseitiges Repository erstellen (selten für lokale Verwendung).
   - Klicken Sie auf **OK**. Ein `.git`-Ordner wird erstellt, der das Repository initialisiert.

#### 3. **Änderungen committen**
   - Fügen Sie Dateien zu Ihrem Repository-Ordner hinzu.
   - Klicken Sie mit der rechten Maustaste auf den Ordner oder ausgewählte Dateien und wählen Sie dann **Git Commit -> "main"** (oder aktuellen Branch).
   - Geben Sie im Commit-Dialog:
     - Eine Commit-Nachricht ein, die die Änderungen beschreibt.
     - Wählen Sie die zu staggenden Dateien aus (Kontrollkästchen).
     - Klicken Sie auf **OK** oder **Commit & Push**, um Änderungen in das Remote-Repository zu übertragen.

#### 4. **Änderungen pushen**
   - Nach dem Committen klicken Sie mit der rechten Maustaste und wählen Sie **TortoiseGit > Push**.
   - Wählen Sie das Remote-Repository und den Branch aus.
   - Authentifizieren Sie sich bei Aufforderung (Benutzername/Passwort für HTTPS oder SSH-Schlüssel).
   - Klicken Sie auf **OK**, um zu pushen.

#### 5. **Änderungen pullen**
   - Um Ihr lokales Repository mit Remote-Änderungen zu aktualisieren, klicken Sie mit der rechten Maustaste und wählen Sie **TortoiseGit > Pull**.
   - Wählen Sie den Remote-Branch aus und klicken Sie auf **OK**.
   - Lösen Sie Konflikte bei Aufforderung (verwenden Sie das Merge-Tool).

#### 6. **Branches erstellen und wechseln**
   - Klicken Sie mit der rechten Maustaste und wählen Sie **TortoiseGit > Create Branch**.
   - Geben Sie einen Branch-Namen ein und klicken Sie auf **OK**.
   - Um Branches zu wechseln, klicken Sie mit der rechten Maustaste und wählen Sie **TortoiseGit > Switch/Checkout**, dann wählen Sie den Branch.

#### 7. **Verlauf anzeigen**
   - Klicken Sie mit der rechten Maustaste und wählen Sie **TortoiseGit > Show Log**.
   - Sehen Sie sich den Commit-Verlauf an, einschließlich Autor, Datum und Nachrichten.
   - Klicken Sie mit der rechten Maustaste auf einen Commit, um Änderungen anzuzeigen, rückgängig zu machen oder auszuwählen.

#### 8. **Merge-Konflikte lösen**
   - Während eines Pulls oder Merges, falls Konflikte auftreten, wird TortoiseGit Sie benachrichtigen.
   - Klicken Sie mit der rechten Maustaste auf konfliktierende Dateien und wählen Sie **TortoiseGit > Resolve**.
   - Verwenden Sie das Merge-Tool, um Konflikte manuell zu bearbeiten, und markieren Sie sie dann als gelöst.
   - Committen Sie die gelösten Änderungen.

### Erweiterte Funktionen
1. **Änderungen stashen**:
   - Um uncommittete Änderungen temporär zu speichern, klicken Sie mit der rechten Maustaste und wählen Sie **TortoiseGit > Stash Save**.
   - Um gestashte Änderungen abzurufen, wählen Sie **TortoiseGit > Stash Pop**.

2. **Rebasing**:
   - Klicken Sie mit der rechten Maustaste und wählen Sie **TortoiseGit > Rebase**.
   - Wählen Sie den Branch aus, auf den rebased werden soll, und folgen Sie den Anweisungen, um Commits neu anzuordnen oder zu squashen.

3. **Submodule**:
   - Um Submodule zu verwalten, klicken Sie mit der rechten Maustaste und wählen Sie **TortoiseGit > Submodule Update** oder **Add**.
   - Konfigurieren Sie Submodule-Einstellungen in den TortoiseGit-Einstellungen.

4. **Bisecting**:
   - Um einen fehlerhaften Commit zu finden, verwenden Sie **TortoiseGit > Bisect Start**.
   - Markieren Sie Commits als „good“ oder „bad“, um den problematischen Commit einzugrenzen.

### Best Practices
- **Oft committen**: Machen Sie kleine, häufige Commits mit klaren Nachrichten.
- **Regelmäßig pullen**: Halten Sie Ihr lokales Repository aktualisiert, um Konflikte zu vermeiden.
- **Branches verwenden**: Erstellen Sie Feature-Branches für neue Arbeiten, um den Hauptbranch stabil zu halten.
- **SSH-Schlüssel sichern**: Speichern Sie SSH-Schlüssel sicher und sichern Sie sie.
- **Änderungen überprüfen**: Verwenden Sie den Diff-Viewer, um Änderungen vor dem Committen zu überprüfen.

### Fehlerbehebung
- **Authentifizierungsprobleme**: Stellen Sie sicher, dass SSH-Schlüssel oder Anmeldeinformationen in Ihrem Git-Hosting-Dienst korrekt konfiguriert sind.
- **Merge-Konflikte**: Verwenden Sie TortoiseGitMerge, um Konflikte visuell zu lösen. Sichern Sie Dateien vor dem Mergen.
- **Fehlendes Kontextmenü**: Überprüfen Sie, ob TortoiseGit korrekt installiert ist und die Explorer-Integration in den Einstellungen aktiviert ist.
- **Langsame Leistung**: Deaktivieren Sie unnötige Overlays unter **TortoiseGit > Einstellungen > Icon Overlays**.

### Beispiel-Workflow
Im Folgenden finden Sie einen Beispiel-Workflow für die Mitwirkung an einem Projekt:

# Beispiel-TortoiseGit-Workflow

## 1. Repository klonen
- Klicken Sie mit der rechten Maustaste in einen Ordner, wählen Sie **Git Clone**.
- Geben Sie die Repository-URL und das lokale Verzeichnis ein.
- Klicken Sie auf **OK**.

## 2. Feature-Branch erstellen
- Klicken Sie mit der rechten Maustaste, wählen Sie **TortoiseGit > Create Branch**.
- Benennen Sie den Branch (z.B. `feature/add-login`).
- Klicken Sie auf **OK** und wechseln Sie zum neuen Branch.

## 3. Änderungen vornehmen
- Bearbeiten Sie Dateien im Repository-Ordner.
- Klicken Sie mit der rechten Maustaste, wählen Sie **Git Commit -> "feature/add-login"**.
- Schreiben Sie eine Commit-Nachricht und stagen Sie Dateien.
- Klicken Sie auf **Commit**.

## 4. Änderungen pushen
- Klicken Sie mit der rechten Maustaste, wählen Sie **TortoiseGit > Push**.
- Wählen Sie den Remote-Branch (z.B. `origin/feature/add-login`).
- Klicken Sie auf **OK**.

## 5. Pull Request erstellen
- Erstellen Sie auf Ihrem Git-Hosting-Dienst (z.B. GitHub) einen Pull Request von Ihrem Branch zum Hauptbranch.
- Warten Sie auf Überprüfung und Merge.

## 6. Lokales Repository aktualisieren
- Wechseln Sie zum Hauptbranch (**TortoiseGit > Switch/Checkout**).
- Pullen Sie Updates (**TortoiseGit > Pull**).

### Ressourcen
- **Offizielle Dokumentation**: [TortoiseGit Dokumentation](https://tortoisegit.org/docs/)
- **Git für Windows**: [Git SCM](https://git-scm.com/)
- **Tutorials**: Suchen Sie auf YouTube oder Tech-Blogs nach „TortoiseGit tutorial“ für visuelle Anleitungen.

TortoiseGit vereinfacht Git-Operationen mit seiner intuitiven Oberfläche und macht Versionskontrolle für Windows-Benutzer zugänglich. Wenn Sie Hilfe bei bestimmten Aufgaben oder erweiterten Konfigurationen benötigen, lassen Sie es mich wissen!