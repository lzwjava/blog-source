---
audio: false
generated: true
lang: de
layout: post
title: iVersion in iOS verwenden
translated: true
---

Um das `iVersion`-Pod in deinem iOS-Projekt zu verwenden, musst du diese Schritte befolgen:

1. **Öffne dein Projekt in Xcode**: Stelle sicher, dass dein Xcode-Projekt geöffnet ist, in dem du das `iVersion`-Pod hinzufügen möchtest.

2. **Initialisiere CocoaPods**: Falls du CocoaPods in deinem Projekt noch nicht initialisiert hast, öffne das Terminal, navigiere zu deinem Projektverzeichnis und führe aus:
   ```bash
   pod init
   ```
   Dies erstellt eine `Podfile` in deinem Projektverzeichnis.

3. **Bearbeite die Podfile**: Öffne die `Podfile` in einem Texteditor oder in Xcode. Füge das `iVersion`-Pod zu deiner `Podfile` hinzu, indem du die folgende Zeile innerhalb des Zielabschnitts einfügst:
   ```ruby
   pod 'iVersion', '1.11.4'
   ```

4. **Installiere das Pod**: Speichere die `Podfile` und kehre zum Terminal zurück. Führe den folgenden Befehl aus, um das `iVersion`-Pod zu installieren:
   ```bash
   pod install
   ```

5. **Öffne die `.xcworkspace`-Datei**: Nach Abschluss der Installation schließe dein Xcode-Projekt, falls es geöffnet ist, und öffne dann die neu erstellte `.xcworkspace`-Datei. Diese Datei befindet sich normalerweise im selben Verzeichnis wie deine ursprüngliche `.xcodeproj`-Datei.

6. **Importiere iVersion**: In deinen Swift- oder Objective-C-Dateien importiere das `iVersion`-Modul, um es zu verwenden:
   ```swift
   import iVersion
   ```

7. **Verwende iVersion in deinem Code**: Jetzt kannst du die `iVersion`-Bibliothek in deinem Projekt verwenden. Zum Beispiel kannst du die App-Version oder die Build-Nummer mit den von `iVersion` bereitgestellten Methoden überprüfen.

Durch das Befolgen dieser Schritte solltest du das `iVersion`-Pod erfolgreich in deinem iOS-Projekt integrieren und verwenden können.