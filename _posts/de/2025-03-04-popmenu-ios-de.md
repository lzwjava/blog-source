---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von PopMenu in iOS
translated: true
---

Um `pod 'PopMenu', '2.4'` in deinem iOS-Projekt zu verwenden, integrierst du die PopMenu-Bibliothek (Version 2.4) über CocoaPods, einen beliebten Abhängigkeitsmanager für iOS. Diese Bibliothek bietet ein Pop-up-Menü mit Animationsfunktion, das von Apps wie Sina Weibo oder NetEase inspiriert ist. Hier sind die Schritte zur Einrichtung und Verwendung in deinem Projekt:

---

### Schritt 1: CocoaPods installieren (falls noch nicht installiert)
Wenn du CocoaPods noch nicht auf deinem System installiert hast, installiere es zuerst:
1. Öffne dein Terminal.
2. Führe diesen Befehl aus:
   ```bash
   sudo gem install cocoapods
   ```
3. Überprüfe die Installation:
   ```bash
   pod --version
   ```

---

### Schritt 2: Deine Podfile einrichten
1. Navigiere in deinem Terminal zu deinem Xcode-Projektverzeichnis:
   ```bash
   cd /pfad/zu/deinem/projekt
   ```
2. Wenn du noch keine Podfile hast, erstelle eine mit:
   ```bash
   pod init
   ```
3. Öffne die `Podfile` in einem Texteditor (z.B. `nano Podfile` oder mit Xcode).
4. Füge die folgenden Zeilen hinzu, um das PopMenu-Pod für dein Ziel zu spezifizieren:
   ```ruby
   platform :ios, '8.0'  # Passe die iOS-Version bei Bedarf an
   target 'DeinAppName' do
     use_frameworks!
     pod 'PopMenu', '2.4'
   end
   ```
   - Ersetze `DeinAppName` durch den Namen deines Xcode-Ziels.
   - Die Zeile `use_frameworks!` ist erforderlich, da PopMenu wahrscheinlich eine frameworkbasierte Bibliothek ist.

5. Speichere und schließe die Podfile.

---

### Schritt 3: Das Pod installieren
1. Führe im Terminal aus:
   ```bash
   pod install
   ```
2. Dies lädt und integriert PopMenu Version 2.4 in dein Projekt. Warte, bis du eine Nachricht wie diese siehst:
   ```
   Pod-Installation abgeschlossen! Es gibt X Abhängigkeiten aus der Podfile und X insgesamt installierte Pods.
   ```
3. Schließe dein Xcode-Projekt, falls es geöffnet ist, und öffne dann die neu generierte `.xcworkspace`-Datei (z.B. `DeinAppName.xcworkspace`) anstelle der `.xcodeproj`-Datei.

---

### Schritt 4: Grundlegende Verwendung in deinem Code
PopMenu ist in Objective-C geschrieben, daher musst du es entsprechend verwenden. Hier ist ein Beispiel, wie du es in deiner App implementieren kannst:

1. **Bibliothek importieren**:
   - In deiner Objective-C-Datei (z.B. `ViewController.m`):
     ```objective-c
     #import "PopMenu.h"
     ```
   - Wenn du Swift verwendest, erstelle eine Brückenheader-Datei:
     - Gehe zu `Datei > Neu > Datei > Header-Datei` (z.B. `DeinAppName-Bridging-Header.h`).
     - Füge hinzu:
       ```objective-c
       #import "PopMenu.h"
       ```
     - Setze in Xcode den Brückenheader unter `Build Settings > Swift Compiler - General > Objective-C Bridging Header` auf den Pfad deiner Header-Datei (z.B. `DeinAppName/DeinAppName-Bridging-Header.h`).

2. **Menüelemente erstellen**:
   Definiere die Elemente, die du im Pop-up-Menü haben möchtest. Jedes Element kann einen Titel, ein Icon und eine Glow-Farbe haben.
   ```objective-c
   NSMutableArray *items = [[NSMutableArray alloc] init];

   MenuItem *menuItem1 = [[MenuItem alloc] initWithTitle:@"Flickr"
                                               iconName:@"post_type_bubble_flickr"
                                              glowColor:[UIColor grayColor]
                                                  index:0];
   [items addObject:menuItem1];

   MenuItem *menuItem2 = [[MenuItem alloc] initWithTitle:@"Twitter"
                                               iconName:@"post_type_bubble_twitter"
                                              glowColor:[UIColor blueColor]
                                                  index:1];
   [items addObject:menuItem2];
   ```

3. **Menü initialisieren und anzeigen**:
   Erstelle eine `PopMenu`-Instanz und zeige sie in deiner Ansicht an.
   ```objective-c
   PopMenu *popMenu = [[PopMenu alloc] initWithFrame:self.view.bounds items:items];
   popMenu.menuAnimationType = kPopMenuAnimationTypeNetEase; // Optionen: kPopMenuAnimationTypeSina oder kPopMenuAnimationTypeNetEase
   popMenu.perRowItemCount = 2; // Anzahl der Elemente pro Zeile
   [popMenu showMenuAtView:self.view];
   ```

4. **Auswahl verarbeiten (optional)**:
   Du kannst eine Unterklasse erstellen oder die Funktionalität erweitern, um Berührungen zu erkennen, obwohl die grundlegende Version von PopMenu (circa 2.4) möglicherweise kein Delegat aus der Box unterstützt. Überprüfe die Dokumentation der Bibliothek auf GitHub (`xhzengAIB/PopMenu`) auf Aktualisierungen oder Anpassungen.

---

### Schritt 5: Dein Projekt ausführen
Bau und führe dein Projekt (`Cmd + R`) in Xcode aus. Wenn die Icons (z.B. `post_type_bubble_flickr`) Teil deines Asset-Katalogs sind, stelle sicher, dass sie zu deinem Projekt hinzugefügt sind. Wenn nicht, musst du sie beschaffen oder erstellen.

---

### Hinweise
- **Versionsspezifität**: `pod 'PopMenu', '2.4'` sperrt dich auf Version 2.4. Wenn du die neueste Version möchtest, verwende `pod 'PopMenu'` ohne Versionsnummer, aber dies könnte zu Änderungen führen, die nicht kompatibel sind.
- **Kompatibilität**: Stelle sicher, dass das Deployment-Ziel deines Projekts mindestens iOS 8.0 ist (oder passe die `platform` in der Podfile an).
- **Anpassung**: PopMenu ermöglicht Anpassungen der Animationsart und des Layouts (z.B. `perRowItemCount`). Erkunde den Quellcode für mehr Optionen.
- **Fehlerbehebung**: Wenn du Fehler wie „Datei nicht gefunden“ bekommst, stelle sicher, dass deine Pods korrekt installiert sind und deine Arbeitsmappe verwendet wird.

Das sollte dir den Einstieg mit PopMenu 2.4 in deiner iOS-App ermöglichen! Lass es mich wissen, wenn du weitere Klarstellungen benötigst.