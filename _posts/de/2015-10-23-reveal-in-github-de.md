---
audio: false
generated: false
lang: de
layout: post
title: 'Ein Xcode-Plugin: Reveal-In-GitHub'
translated: true
---

Dies ist die README.md von einem GitHub-Projekt: [https://github.com/lzwjava/Reveal-In-GitHub](https://github.com/lzwjava/Reveal-In-GitHub).

---

# Reveal-In-GitHub

Ein Xcode-Plugin, das für eine nahtlose Navigation zu wichtigen GitHub-Funktionen innerhalb Ihres aktuellen Repositories entwickelt wurde. Mit einem Klick können Sie mühelos auf den GitHub-Verlauf, die Verursacheransicht, Pull-Requests, Issues und Benachrichtigungen zugreifen – alles in wenigen Sekunden.

![plugin](https://cloud.githubusercontent.com/assets/5022872/10867703/96e980be-80ab-11e5-9aaa-a06ef476b7f7.gif)

Unser Unternehmen arbeitet auf GitHub. Ich öffne GitHub oft. Manchmal bearbeite ich in Xcode etwas und verstehe den Code nicht, also gehe ich zu GitHub, um ihn zu veröffentlichen. Manchmal finde ich die letzten Commits für eine Datei, um herauszufinden, wie sich der Code entwickelt hat. Daher fragte ich mich, ob es ein Tool gibt, das mir hilft, schnell von Xcode aus zu GitHub zu wechseln. Daher schrieb ich dieses Plugin. Wenn du eine Quelldatei in Xcode bearbeitest, ist es einfach zu wissen, in welchem GitHub-Repository du arbeitest und welche Datei du bearbeitest. Daher macht es Sinn, schnell zur Datei auf GitHub zu springen, schnell zur Verursacheransicht der aktuellen bearbeiteten Zeile auf GitHub zu springen, schnell zu den Issues oder PRs des aktuellen Repositories zu springen, an dem du in Xcode arbeitest.

## Menüpunkte

<img width="700" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864813/5df3f05e-8034-11e5-9f3e-03ae3fbc3cfc.png">

Es gibt sechs Menüpunkte:

 Menü-Titel     | Taschenrechner               | GitHub-URL-Muster (wenn ich LZAlbumManager.m Zeile 40 bearbeite)                |
----------------|--------------------------|----------------------------------
 Einstellungen	    |⌃⇧⌘S |
 Repository      |⌃⇧⌘R | https://github.com/lzwjava/LZAlbum
 Issues          |⌃⇧⌘I | https://github.com/lzwjava/LZAlbum/issues
 PRs             |⌃⇧⌘P | https://github.com/lzwjava/LZAlbum/pulls
 Schnelldatei    |⌃⇧⌘Q | https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 Historie auflisten |⌃⇧⌘L | https://github.com/lzwjava/LZAlbum/commits/fd7224/LZAlbum/manager/LZAlbumManager.m
 Verursacheransicht       |⌃⇧⌘B | https://github.com/lzwjava/LZAlbum/blame/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 Benachrichtigungen |⌃⇧⌘N | https://github.com/leancloud/LZAlbum/notifications?all=1

Die Tastenkombinationen sind sorgfältig gestaltet. Sie werden nicht mit den Standardtastenkombinationen von Xcode in Konflikt geraten. Das Tastenkombinationsmuster ist ⌃⇧⌘ (Ctrl+Shift+Command), plus das erste Zeichen des Menü-Titels.

## Anpassen

Manchmal möchten Sie möglicherweise schnell zur Wiki springen. Hier ist die Vorgehensweise, öffnen Sie die Einstellungen:

<img width="500" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864939/fa83f286-8037-11e5-97d7-e9549485b11d.png">

Zum Beispiel,

Schnelldatei, das Muster und die tatsächliche URL:

```
           {git_remote_url}       /blob/{commit}/          {file_path}         #{selection}
https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40-L43
```

Der {commit} ist der aktuelle Commit-Hash des aktuellen Branches. Es ist besser, ihn zu verwenden, anstatt den Branch, weil der HEAD des Branches sich ändern kann. Daher kann auch der Code in #L40-L43 geändert werden.

Wenn Sie also eine Tastenkombination für die Wiki des aktuellen Repositories hinzufügen möchten, fügen Sie einfach einen Menüpunkt hinzu und legen Sie das Muster auf `{git_remote_url}/wiki` fest.

In den Einstellungen bedeutet `Clear Default Repos`, wenn Sie mehrere Git-Remotes haben, wird es Sie beim ersten Mal auffordern, eines von ihnen auszuwählen:

<img width="400" src="https://cloud.githubusercontent.com/assets/5022872/10865120/5794994a-803c-11e5-9527-965f7e617e8f.png">

Das Plugin merkt sich dann, welches Sie wählen. Daher wird beim nächsten Auslösen des Menüs dieses Remote-Repository als Standard geöffnet. Der Knopf `Clear Default Repos` löscht diese Einstellung und fordert Sie erneut zur Auswahl auf.

## Installieren

Empfohlen zur Installation mit [Alcatraz](http://alcatraz.io/),

![qq20151101-1 2x](https://cloud.githubusercontent.com/assets/5022872/10867743/0ce351c6-80ae-11e5-82e2-f740887153f7.jpg)

Oder

1. Klonen Sie dieses Repository.
2. Öffnen Sie `Reveal-In-GitHub.xcodeproj` und bauen Sie es.
3. Reveal-In-GitHub.xcplugin sollte sich in `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins` befinden
4. XCode neu starten
5. Öffnen Sie ein beliebiges GitHub-Projekt und drücken Sie ⌃⇧⌘B (Ctrl+Shift+Command+B), um den Code zu veröffentlichen.

## 安装

Empfohlen zur Installation mit [Alcatraz](http://alcatraz.io/), siehe auch den Blog von Devtang [Blog](http://blog.devtang.com/blog/2014/03/05/use-alcatraz-to-manage-xcode-plugins/). Nach der Installation, suchen Sie nach `Reveal In GitHub` und klicken Sie auf `Install`.

Wenn Sie dieses Tool nicht verwenden, erfolgen drei Schritte:

* Klonen Sie dieses Projekt auf Ihren lokalen Rechner.
* Öffnen Sie xcodeproj, klicken Sie auf Build zum Bauen. Dies wird in der Verzeichnis `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins` Reveal-In-GitHub.xcplugin Datei generieren.
* Starten Sie Xcode neu und öffnen Sie ein beliebiges Projekt auf GitHub. Drücken Sie `Ctrl+Shift+Command+B`, um den Code zu veröffentlichen.

## Credit

Während der Entwicklung stellte sich heraus, dass ein weiteres Plugin [ShowInGitHub](https://github.com/larsxschneider/ShowInGitHub) eine ähnliche Aufgabe durchführt. Ich lernte einige Techniken davon. Vielen Dank dafür.

## Lizenz

MIT