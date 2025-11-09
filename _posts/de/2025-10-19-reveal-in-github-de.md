---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Enthüllen in GitHub Xcode-Plugin
translated: true
type: note
---

### Was ist Reveal-In-GitHub?

Reveal-In-GitHub ist ein Xcode-Plugin, mit dem Sie schnell von Ihrem Xcode-Arbeitsbereich zu wichtigen GitHub-Funktionen für Ihr aktuelles Repository navigieren können. Es wurde für Entwickler konzipiert, die an GitHub-gehosteten Git-Projekten arbeiten, und ermöglicht den Zugriff mit einem Klick (oder Tastenkombination) auf Dinge wie Commit-Verlauf, Blame-Ansichten, Pull Requests, Issues und Benachrichtigungen – ohne Xcode zu verlassen oder URLs manuell einzugeben.

### Voraussetzungen
- Xcode muss installiert sein (auf neueren Versionen getestet; keine spezifische Mindestversion genannt).
- Ihr Projekt muss ein Git-Repository sein, das auf GitHub gehostet wird (das Plugin erkennt die Repo-URL und Dateipfade automatisch).
- Wenn Ihr Projekt mehrere Git-Remotes hat, werden Sie bei der ersten Verwendung aufgefordert, ein Standard-Repo auszuwählen.

### Installation
Es gibt zwei Hauptwege zur Installation:

#### Option 1: Verwendung von Alcatraz (Empfohlen)
1. Installieren Sie Alcatraz, falls noch nicht geschehen (ein Paketmanager für Xcode-Plugins). Sie können Setup-Anleitungen online finden, wie z.B. [diese hier](http://blog.devtang.com/blog/2014/03/05/use-alcatraz-to-manage-xcode-plugins/), wenn Sie Anweisungen auf Chinesisch bevorzugen.
2. Öffnen Sie Alcatraz in Xcode (über das Menü: `Window > Package Manager`).
3. Suchen Sie nach "Reveal In GitHub".
4. Klicken Sie auf **Install**.
5. Starten Sie Xcode neu.

#### Option 2: Manuelle Installation
1. Klonen Sie das Repository:  
   ```
   git clone https://github.com/lzwjava/Reveal-In-GitHub.git
   ```
2. Öffnen Sie die Datei `Reveal-In-GitHub.xcodeproj` in Xcode.
3. Bauen Sie das Projekt (Product > Build oder ⌘B). Dadurch wird die Datei `Reveal-In-GitHub.xcplugin` erzeugt.
4. Verschieben Sie das Plugin in den Ordner:  
   `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins/`
5. Starten Sie Xcode neu.

Nach der Installation sollte das Plugin in der Xcode-Menüleiste unter **Editor > Reveal In GitHub** erscheinen.

### Verwendung
Sobald es installiert ist und Xcode neu gestartet wurde:
1. Öffnen Sie ein GitHub-gehostetes Projekt in Xcode und bearbeiten Sie eine Quelldatei (navigieren Sie z.B. zu einer bestimmten Zeile).
2. Verwenden Sie eine der Tastenkombinationen oder Menüpunkte unter **Editor > Reveal In GitHub**, um zu GitHub zu springen. Das Plugin erkennt automatisch Ihr Repo, die aktuelle Datei, die Zeilennummer und den letzten Commit-Hash.

Hier ist eine Kurzreferenz für die integrierten Menüpunkte und Tastenkombinationen (die Tastenkombinationen folgen dem Muster ⌃⇧⌘ + erster Buchstabe des Titels):

| Menüpunkt      | Tastenkombination | Funktion | Beispiel-GitHub-URL (für Datei LZAlbumManager.m in Zeile 40 im Repo lzwjava/LZAlbum bei Commit fd7224) |
|----------------|-------------|--------------|-----------------------------------------------------------------------------------------------|
| **Setting**    | ⌃⇧⌘S      | Öffnet den Anpassungsbereich | N/A |
| **Repo**       | ⌃⇧⌘R      | Öffnet die Haupt-Repo-Seite | https://github.com/lzwjava/LZAlbum |
| **Issues**     | ⌃⇧⌘I      | Öffnet die Issues-Liste | https://github.com/lzwjava/LZAlbum/issues |
| **PRs**        | ⌃⇧⌘P      | Öffnet die Pull-Requests-Liste | https://github.com/lzwjava/LZAlbum/pulls |
| **Quick File** | ⌃⇧⌘Q      | Öffnet die Dateiansicht in der aktuellen Zeile | https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40 |
| **List History**| ⌃⇧⌘L     | Öffnet den Commit-Verlauf für die Datei | https://github.com/lzwjava/LZAlbum/commits/fd7224/LZAlbum/manager/LZAlbumManager.m |
| **Blame**      | ⌃⇧⌘B      | Öffnet die Blame-Ansicht für die aktuelle Zeile | https://github.com/lzwjava/LZAlbum/blame/fd7224/LZAlbum/manager/LZAlbumManager.m#L40 |
| **Notifications**| ⌃⇧⌘N   | Öffnet die Repo-Benachrichtigungen | https://github.com/lzwjava/LZAlbum/notifications?all=1 |

- **Tipps**: 
  - Die Tastenkombinationen stehen nicht in Konflikt mit den Xcode-Standards.
  - Wenn ein Textbereich ausgewählt ist, werden einige Aktionen (wie Blame) an diesen Bereich verankert (z.B. #L40-L43).
  - Testen Sie es: Öffnen Sie ein Projekt, gehen Sie zu einer Zeile und drücken Sie ⌃⇧⌘B – es sollte die Blame-Seite in Ihrem Browser öffnen.

### Anpassung
Um Menüpunkte anzupassen oder hinzuzufügen:
1. Drücken Sie ⌃⇧⌘S oder gehen Sie zu **Editor > Reveal In GitHub > Setting**.
2. Im Anpassungsbereich:
   - Fügen Sie neue Elemente hinzu, indem Sie auf die "+"-Schaltfläche klicken: Geben Sie einen Titel (z.B. "Wiki"), eine Tastenkombination und ein URL-Muster ein.
   - URL-Muster verwenden Platzhalter wie:
     - `{git_remote_url}`: Vollständige Repo-URL (z.B. https://github.com/user/repo).
     - `{commit}`: Hash des letzten Commits des aktuellen Branches.
     - `{file_path}`: Relativer Pfad zur Datei.
     - `#{selection}`: Aktuelle Zeile oder Auswahl (z.B. #L40).
   - Beispiel: Für einen Wiki-Link setzen Sie das Muster auf `{git_remote_url}/wiki`.
3. Wenn Sie mehrere Remotes haben, verwenden Sie die Schaltfläche "Clear Default Repos", um die Auswahl zurückzusetzen.

Das Plugin ist inspiriert von [ShowInGitHub](https://github.com/larsxschneider/ShowInGitHub) und unter der MIT-Lizenz lizenziert.

[Reveal-In-GitHub GitHub Repository](https://github.com/lzwjava/Reveal-In-GitHub)