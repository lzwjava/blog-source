---
audio: false
generated: true
lang: de
layout: post
title: LeanCloud Echtzeit iOS SDK
translated: true
---

Um die `pod 'AVOSCloudIM', '3.1.6.2'` in deinem iOS-Projekt mit CocoaPods zu verwenden, folge diesen Schritten. Es wird vorausgesetzt, dass CocoaPods installiert ist und du mit der grundlegenden iOS-Entwicklung mit Xcode vertraut bist.

---

### Schritt 1: CocoaPods einrichten (falls noch nicht geschehen)
Wenn du CocoaPods noch nicht installiert hast, installiere es über das Terminal:
```bash
sudo gem install cocoapods
```
Überprüfe die Installation:
```bash
pod --version
```

---

### Schritt 2: Xcode-Projekt erstellen oder öffnen
1. Öffne dein bestehendes Xcode-Projekt oder erstelle ein neues in Xcode.
2. Schließe Xcode vorerst (wir öffnen es später mit dem Workspace erneut).

---

### Schritt 3: Podfile initialisieren
1. Öffne dein Terminal und navigiere zu deinem Projektverzeichnis (wo sich die `.xcodeproj`-Datei befindet):
   ```bash
   cd /pfad/zu/deinem/projekt
   ```
2. Wenn du noch kein Podfile hast, erstelle eines, indem du folgendes ausführst:
   ```bash
   pod init
   ```
   Dies erstellt ein grundlegendes `Podfile` in deinem Projektverzeichnis.

---

### Schritt 4: Podfile bearbeiten
1. Öffne das `Podfile` in einem Texteditor (z.B. `nano`, `vim` oder einem Code-Editor wie VS Code):
   ```bash
   open Podfile
   ```
2. Bearbeite das `Podfile`, um das `AVOSCloudIM`-Pod mit der Version `3.1.6.2` zu enthalten. Hier ist ein Beispiel, wie dein `Podfile` aussehen könnte:
   ```ruby
   platform :ios, '9.0'  # Gib die minimale iOS-Version an (nach Bedarf anpassen)
   use_frameworks!       # Optional: Verwende dies, wenn dein Projekt Swift oder Frameworks verwendet

   target 'DeinAppName' do
     pod 'AVOSCloudIM', '3.1.6.2'  # Füge diese Zeile hinzu, um AVOSCloudIM Version 3.1.6.2 zu enthalten
   end
   ```
   - Ersetze `'DeinAppName'` durch den tatsächlichen Namen deines Xcode-Ziels (normalerweise der Name deiner App).
   - Die Zeile `platform :ios, '9.0'` gibt die minimale iOS-Version an; passe sie entsprechend den Anforderungen deines Projekts an.
   - `use_frameworks!` ist erforderlich, wenn dein Projekt Swift verwendet oder wenn das Pod dynamische Frameworks benötigt.

3. Speichere und schließe das `Podfile`.

---

### Schritt 5: Pod installieren
1. Führe im Terminal den folgenden Befehl aus, während du dich im Verzeichnis deines Projekts befindest:
   ```bash
   pod install
   ```
   - Dies lädt die `AVOSCloudIM`-Bibliothek (Version 3.1.6.2) herunter und integriert sie in dein Projekt.
   - Bei Erfolg siehst du eine Ausgabe wie:
     ```
     Pod-Installation abgeschlossen! Es gibt X Abhängigkeiten aus der Podfile und X insgesamt installierte Pods.
     ```

2. Wenn Fehler auftreten (z.B. Pod nicht gefunden), stelle sicher, dass die Version `3.1.6.2` noch im CocoaPods-Repository verfügbar ist. Ältere Versionen könnten nicht mehr unterstützt werden. Du kannst die neueste Version auf [CocoaPods.org](https://cocoapods.org) unter `AVOSCloudIM` überprüfen oder auf eine neuere Version aktualisieren (z.B. `pod 'AVOSCloudIM', '~> 12.3'`).

---

### Schritt 6: Workspace öffnen
1. Nach der Installation wird eine `.xcworkspace`-Datei in deinem Projektverzeichnis erstellt (z.B. `DeinAppName.xcworkspace`).
2. Öffne diese Datei in Xcode:
   ```bash
   open DeinAppName.xcworkspace
   ```
   - Von nun an solltest du immer die `.xcworkspace`-Datei anstelle der `.xcodeproj`-Datei verwenden, um mit deinem Projekt zu arbeiten.

---

### Schritt 7: AVOSCloudIM in deinem Code importieren und verwenden
1. In deinen Swift- oder Objective-C-Dateien importiere das `AVOSCloudIM`-Modul:
   - **Swift**:
     ```swift
     import AVOSCloudIM
     ```
   - **Objective-C**:
     ```objc
     #import <AVOSCloudIM/AVOSCloudIM.h>
     ```
2. Beginne, die Funktionen der Bibliothek zu verwenden. `AVOSCloudIM` ist Teil des LeanCloud SDK, das typischerweise für Echtzeit-Nachrichten verwendet wird. Verweise auf die [LeanCloud-Dokumentation](https://leancloud.app/docs/) für spezifische Verwendungsbeispiele, wie das Einrichten eines Chat-Clients:
   - Beispiel (Swift):
     ```swift
     let client = AVIMClient(clientId: "deinClientID")
     client.open { (succeeded, error) in
         if succeeded {
             print("Verbunden mit LeanCloud IM!")
         } else {
             print("Fehler: \(error?.localizedDescription ?? "Unbekannt")")
         }
     }
     ```

---

### Schritt 8: Projekt konfigurieren (falls erforderlich)
- **App Key und Initialisierung**: LeanCloud SDKs benötigen oft eine App-ID und einen Schlüssel. Füge diesen Initialisierungscode hinzu (z.B. in `AppDelegate`):
  - **Swift**:
    ```swift
    import AVOSCloud
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        AVOSCloud.setApplicationId("deineAppID", clientKey: "deinAppKey")
        return true
    }
    ```
  - Ersetze `"deineAppID"` und `"deinAppKey"` durch die Anmeldeinformationen von deinem LeanCloud-Konto.
- **Berechtigungen**: Stelle sicher, dass deine App die erforderlichen Berechtigungen (z.B. Internetzugriff) in `Info.plist` hat:
  ```xml
  <key>NSAppTransportSecurity</key>
  <dict>
      <key>NSAllowsArbitraryLoads</key>
      <true/>
  </dict>
  ```

---

### Hinweise
- **Versionsspezifität**: Die Verwendung von `pod 'AVOSCloudIM', '3.1.6.2'` sperrt dich auf diese genaue Version. Wenn du Flexibilität für kleinere Updates möchtest, verwende `~>` (z.B. `pod 'AVOSCloudIM', '~> 3.1.6'` erlaubt Updates wie 3.1.6.1, aber nicht 3.2).
- **Fehlerbehebung**: Wenn `pod install` fehlschlägt, versuche:
  - CocoaPods aktualisieren: `sudo gem install cocoapods`
  - Cache leeren: `pod cache clean --all`
  - `pod repo update` ausführen, um das lokale CocoaPods-Spezifikationsrepository zu aktualisieren.
- **LeanCloud SDK**: Da `AVOSCloudIM` Teil von LeanCloud ist, stelle sicher, dass du deren Einrichtungsanleitung für zusätzliche Konfigurationen (z.B. Registrierung auf ihrer Plattform) folgst.

---

Das war's! Du hast nun `AVOSCloudIM` Version 3.1.6.2 in dein iOS-Projekt integriert. Baue und führe deine App in Xcode aus, um sie zu testen. Lass mich wissen, wenn du Hilfe bei spezifischen LeanCloud-Funktionen benötigst!