---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von iVersion in iOS
translated: true
type: note
---

Um den `iVersion` Pod in Ihrem iOS-Projekt zu verwenden, müssen Sie folgende Schritte befolgen:

1. **Öffnen Sie Ihr Projekt in Xcode**: Stellen Sie sicher, dass Ihr Xcode-Projekt geöffnet ist, in das Sie den `iVersion` Pod hinzufügen möchten.

2. **Initialisieren Sie CocoaPods**: Falls Sie CocoaPods noch nicht in Ihrem Projekt initialisiert haben, öffnen Sie das Terminal, navigieren Sie zu Ihrem Projektverzeichnis und führen Sie aus:
   ```bash
   pod init
   ```
   Dies erstellt eine `Podfile` in Ihrem Projektverzeichnis.

3. **Bearbeiten Sie die Podfile**: Öffnen Sie die `Podfile` in einem Texteditor oder in Xcode. Fügen Sie den `iVersion` Pod zu Ihrer `Podfile` hinzu, indem Sie die folgende Zeile innerhalb des Target-Abschnitts einfügen:
   ```ruby
   pod 'iVersion', '1.11.4'
   ```

4. **Installieren Sie den Pod**: Speichern Sie die `Podfile` und gehen Sie zurück zum Terminal. Führen Sie den folgenden Befehl aus, um den `iVersion` Pod zu installieren:
   ```bash
   pod install
   ```

5. **Öffnen Sie die `.xcworkspace`-Datei**: Schließen Sie nach Abschluss der Installation Ihr Xcode-Projekt, falls es geöffnet ist, und öffnen Sie dann die neu erstellte `.xcworkspace`-Datei. Diese Datei befindet sich normalerweise im selben Verzeichnis wie Ihre ursprüngliche `.xcodeproj`-Datei.

6. **Importieren Sie iVersion**: Importieren Sie in Ihren Swift- oder Objective-C-Dateien das `iVersion` Modul, um es zu verwenden:
   ```swift
   import iVersion
   ```

7. **Verwenden Sie iVersion in Ihrem Code**: Jetzt können Sie die `iVersion`-Bibliothek in Ihrem Projekt verwenden. Sie können beispielsweise die App-Version oder die Build-Nummer mit den von `iVersion` bereitgestellten Methoden überprüfen.

Wenn Sie diese Schritte befolgen, sollten Sie den `iVersion` Pod erfolgreich in Ihr iOS-Projekt integrieren und verwenden können.