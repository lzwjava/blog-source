---
audio: false
generated: true
lang: de
layout: post
title: Verwenden von PopMenu in iOS
translated: true
type: note
---

Um `pod 'PopMenu', '2.4'` in Ihrem iOS-Projekt zu verwenden, integrieren Sie die PopMenu-Bibliothek (Version 2.4) via CocoaPods, einem beliebten Dependency Manager für iOS. Diese Bibliothek bietet ein Pop-up-Animationsmenü, inspiriert von Apps wie Sina Weibo oder NetEase. Im Folgenden finden Sie die Schritte zur Einrichtung und Verwendung in Ihrem Projekt:

---

### Schritt 1: CocoaPods installieren (falls noch nicht geschehen)
Falls Sie CocoaPods noch nicht auf Ihrem System installiert haben, installieren Sie es zuerst:
1. Öffnen Sie Ihr Terminal.
2. Führen Sie diesen Befehl aus:
   ```bash
   sudo gem install cocoapods
   ```
3. Überprüfen Sie die Installation:
   ```bash
   pod --version
   ```

---

### Schritt 2: Ihre Podfile einrichten
1. Navigieren Sie im Terminal zu Ihrem Xcode-Projektverzeichnis:
   ```bash
   cd /pfad/zu/ihrem/projekt
   ```
2. Falls Sie noch keine Podfile haben, erstellen Sie eine mit:
   ```bash
   pod init
   ```
3. Öffnen Sie die `Podfile` in einem Texteditor (z.B. `nano Podfile` oder verwenden Sie Xcode).
4. Fügen Sie die folgenden Zeilen hinzu, um den PopMenu-Pod für Ihr Target anzugeben:
   ```ruby
   platform :ios, '8.0'  # Passen Sie die iOS-Version bei Bedarf an
   target 'IhrAppName' do
     use_frameworks!
     pod 'PopMenu', '2.4'
   end
   ```
   - Ersetzen Sie `IhrAppName` mit dem Namen Ihres Xcode-Targets.
   - Die Zeile `use_frameworks!` ist erforderlich, da PopMenu wahrscheinlich eine Framework-basierte Bibliothek ist.

5. Speichern und schließen Sie die Podfile.

---

### Schritt 3: Den Pod installieren
1. Führen Sie im Terminal aus:
   ```bash
   pod install
   ```
2. Dies lädt PopMenu Version 2.4 herunter und integriert es in Ihr Projekt. Warten Sie, bis Sie eine Meldung wie diese sehen:
   ```
   Pod installation complete! There are X dependencies from the Podfile and X total pods installed.
   ```
3. Schließen Sie Ihr Xcode-Projekt, falls es geöffnet ist, und öffnen Sie dann die neu generierte `.xcworkspace`-Datei (z.B. `IhrAppName.xcworkspace`) anstelle der `.xcodeproj`-Datei.

---

### Schritt 4: Grundlegende Verwendung in Ihrem Code
PopMenu ist in Objective-C geschrieben, daher müssen Sie es entsprechend verwenden. Hier ist ein Beispiel, wie Sie es in Ihrer App implementieren können:

1. **Bibliothek importieren**:
   - In Ihrer Objective-C-Datei (z.B. `ViewController.m`):
     ```objective-c
     #import "PopMenu.h"
     ```
   - Wenn Sie Swift verwenden, erstellen Sie einen Bridging Header:
     - Gehen Sie zu `File > New > File > Header File` (z.B. `IhrAppName-Bridging-Header.h`).
     - Fügen Sie hinzu:
       ```objective-c
       #import "PopMenu.h"
       ```
     - Setzen Sie in Xcode den Bridging Header unter `Build Settings > Swift Compiler - General > Objective-C Bridging Header` auf den Pfad Ihrer Header-Datei (z.B. `IhrAppName/IhrAppName-Bridging-Header.h`).

2. **Menüelemente erstellen**:
   Definieren Sie die Elemente, die im Pop-up-Menü erscheinen sollen. Jedes Element kann einen Titel, ein Icon und eine Leuchtfarbe haben.
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
   Erstellen Sie eine `PopMenu`-Instanz und zeigen Sie sie in Ihrer View an.
   ```objective-c
   PopMenu *popMenu = [[PopMenu alloc] initWithFrame:self.view.bounds items:items];
   popMenu.menuAnimationType = kPopMenuAnimationTypeNetEase; // Optionen: kPopMenuAnimationTypeSina oder kPopMenuAnimationTypeNetEase
   popMenu.perRowItemCount = 2; // Anzahl der Elemente pro Reihe
   [popMenu showMenuAtView:self.view];
   ```

4. **Auswahl behandeln (Optional)**:
   Sie können die Funktionalität durch Subclassing oder Erweiterungen anpassen, um Taps zu erkennen, obwohl die Basisversion von PopMenu (circa 2.4) von Haus aus möglicherweise keinen Delegaten unterstützt. Überprüfen Sie die Dokumentation der Bibliothek auf GitHub (`xhzengAIB/PopMenu`) auf Updates oder Anpassungsmöglichkeiten.

---

### Schritt 5: Ihr Projekt ausführen
Erstellen Sie Ihr Projekt und führen Sie es aus (`Cmd + R`) in Xcode. Stellen Sie sicher, dass die Icons (z.B. `post_type_bubble_flickr`) Teil Ihres Asset-Katalogs sind und Ihrem Projekt hinzugefügt wurden. Falls nicht, müssen Sie sie beschaffen oder erstellen.

---

### Hinweise
- **Versionsspezifität**: `pod 'PopMenu', '2.4'` bindet Sie an Version 2.4. Wenn Sie die neueste Version möchten, verwenden Sie `pod 'PopMenu'` ohne Versionsnummer, aber dies könnte Breaking Changes einführen.
- **Kompatibilität**: Stellen Sie sicher, dass Ihr Deployment Target mindestens iOS 8.0 ist (oder passen Sie die `platform` in der Podfile an).
- **Anpassung**: PopMenu erlaubt Anpassungen des Animationstyps und Layouts (z.B. `perRowItemCount`). Erkunden Sie den Quellcode für weitere Optionen.
- **Fehlerbehebung**: Falls Sie Fehler wie "file not found" erhalten, stellen Sie sicher, dass Ihre Pods korrekt installiert sind und Ihr Workspace verwendet wird.

Das sollte Ihnen den Einstieg in PopMenu 2.4 in Ihrer iOS-App ermöglichen! Lassen Sie es mich wissen, wenn Sie weitere Erklärungen benötigen.