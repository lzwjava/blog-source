---
audio: false
generated: true
lang: de
layout: post
title: LeanCloud Echtzeit iOS SDK
translated: true
type: note
---

Um `pod 'AVOSCloudIM', '3.1.6.2'` in Ihrem iOS-Projekt mit CocoaPods zu verwenden, befolgen Sie diese Schritte. Dies setzt voraus, dass Sie CocoaPods installiert haben und mit der grundlegenden iOS-Entwicklung unter Xcode vertraut sind.

---

### Schritt 1: CocoaPods einrichten (falls noch nicht geschehen)
Falls Sie CocoaPods noch nicht installiert haben, installieren Sie es über das Terminal:
```bash
sudo gem install cocoapods
```
Überprüfen Sie die Installation:
```bash
pod --version
```

---

### Schritt 2: Erstellen oder öffnen Sie Ihr Xcode-Projekt
1. Öffnen Sie Ihr bestehendes Xcode-Projekt oder erstellen Sie ein neues in Xcode.
2. Schließen Sie Xcode vorerst (wir werden es später mit dem Workspace wieder öffnen).

---

### Schritt 3: Eine Podfile initialisieren
1. Öffnen Sie Ihr Terminal und navigieren Sie zum Stammverzeichnis Ihres Projekts (wo sich die `.xcodeproj`-Datei befindet):
   ```bash
   cd /pfad/zu/ihrem/projekt
   ```
2. Wenn Sie noch keine Podfile haben, erstellen Sie eine, indem Sie ausführen:
   ```bash
   pod init
   ```
   Dies erzeugt eine grundlegende `Podfile` in Ihrem Projektverzeichnis.

---

### Schritt 4: Die Podfile bearbeiten
1. Öffnen Sie die `Podfile` in einem Texteditor (z.B. `nano`, `vim` oder einem Code-Editor wie VS Code):
   ```bash
   open Podfile
   ```
2. Modifizieren Sie die `Podfile`, um den `AVOSCloudIM`-Pod mit der Version `3.1.6.2` einzubinden. Hier ist ein Beispiel, wie Ihre `Podfile` aussehen könnte:
   ```ruby
   platform :ios, '9.0'  # Legen Sie die minimale iOS-Version fest (passen Sie sie bei Bedarf an)
   use_frameworks!       # Optional: Verwenden Sie dies, wenn Ihr Projekt Swift oder Frameworks nutzt

   target 'IhrAppName' do
     pod 'AVOSCloudIM', '3.1.6.2'  # Fügen Sie diese Zeile hinzu, um AVOSCloudIM Version 3.1.6.2 einzubinden
   end
   ```
   - Ersetzen Sie `'IhrAppName'` mit dem tatsächlichen Namen Ihres Xcode-Targets (üblicherweise der Name Ihrer App).
   - Die Zeile `platform :ios, '9.0'` spezifiziert die minimale iOS-Version; passen Sie sie basierend auf den Anforderungen Ihres Projekts an.
   - `use_frameworks!` wird benötigt, wenn Ihr Projekt Swift verwendet oder wenn der Pod dynamische Frameworks erfordert.

3. Speichern und schließen Sie die `Podfile`.

---

### Schritt 5: Den Pod installieren
1. Führen Sie im Terminal den folgenden Befehl aus dem Stammverzeichnis Ihres Projekts aus:
   ```bash
   pod install
   ```
   - Dies lädt die `AVOSCloudIM`-Bibliothek (Version 3.1.6.2) herunter und integriert sie in Ihr Projekt.
   - Wenn erfolgreich, sehen Sie eine Ausgabe wie:
     ```
     Pod installation complete! There are X dependencies from the Podfile and X total pods installed.
     ```

2. Wenn Sie Fehler erhalten (z.B. Pod nicht gefunden), stellen Sie sicher, dass die Version `3.1.6.2` noch im CocoaPods-Repository verfügbar ist. Ältere Versionen werden möglicherweise nicht mehr unterstützt. Sie können die neueste Version auf [CocoaPods.org](https://cocoapods.org) unter `AVOSCloudIM` prüfen oder auf eine neuere Version aktualisieren (z.B. `pod 'AVOSCloudIM', '~> 12.3'`).

---

### Schritt 6: Den Workspace öffnen
1. Nach der Installation wird eine `.xcworkspace`-Datei in Ihrem Projektverzeichnis erstellt (z.B. `IhrAppName.xcworkspace`).
2. Öffnen Sie diese Datei in Xcode:
   ```bash
   open IhrAppName.xcworkspace
   ```
   - Verwenden Sie von nun an immer die `.xcworkspace`-Datei anstelle der `.xcodeproj`-Datei, um an Ihrem Projekt zu arbeiten.

---

### Schritt 7: AVOSCloudIM in Ihrem Code importieren und verwenden
1. Importieren Sie in Ihren Swift- oder Objective-C-Dateien das `AVOSCloudIM`-Modul:
   - **Swift**:
     ```swift
     import AVOSCloudIM
     ```
   - **Objective-C**:
     ```objc
     #import <AVOSCloudIM/AVOSCloudIM.h>
     ```
2. Beginnen Sie, die Funktionen der Bibliothek zu nutzen. `AVOSCloudIM` ist Teil des LeanCloud SDK, typischerweise verwendet für Echtzeit-Nachrichten. Konsultieren Sie die [LeanCloud-Dokumentation](https://leancloud.app/docs/) für spezifische Verwendungsbeispiele, wie das Einrichten eines Chat-Clients:
   - Beispiel (Swift):
     ```swift
     let client = AVIMClient(clientId: "yourClientID")
     client.open { (succeeded, error) in
         if succeeded {
             print("Connected to LeanCloud IM!")
         } else {
             print("Error: \\(error?.localizedDescription ?? "Unknown")")
         }
     }
     ```

---

### Schritt 8: Konfigurieren Sie Ihr Projekt (falls nötig)
- **App Key und Initialisierung**: LeanCloud SDKs erfordern oft eine App-ID und einen Schlüssel. Fügen Sie diesen Initialisierungscode hinzu (z.B. in `AppDelegate`):
  - **Swift**:
    ```swift
    import AVOSCloud
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        AVOSCloud.setApplicationId("yourAppID", clientKey: "yourAppKey")
        return true
    }
    ```
  - Ersetzen Sie `"yourAppID"` und `"yourAppKey"` mit den Zugangsdaten aus Ihrem LeanCloud-Account.
- **Berechtigungen**: Stellen Sie sicher, dass Ihre App die notwendigen Berechtigungen hat (z.B. Internetzugriff) in `Info.plist`:
  ```xml
  <key>NSAppTransportSecurity</key>
  <dict>
      <key>NSAllowsArbitraryLoads</key>
      <true/>
  </dict>
  ```

---

### Hinweise
- **Versionsspezifität**: Die Verwendung von `pod 'AVOSCloudIM', '3.1.6.2'` bindet Sie an diese exakte Version. Wenn Sie Flexibilität für kleinere Updates wünschen, verwenden Sie `~>` (z.B. erlaubt `pod 'AVOSCloudIM', '~> 3.1.6'` Updates wie 3.1.6.1, aber nicht 3.2).
- **Fehlerbehebung**: Wenn `pod install` fehlschlägt, versuchen Sie:
  - CocoaPods zu aktualisieren: `sudo gem install cocoapods`
  - Den Cache zu leeren: `pod cache clean --all`
  - `pod repo update` auszuführen, um das lokale CocoaPods-Spec-Repository zu aktualisieren.
- **LeanCloud SDK**: Da `AVOSCloudIM` Teil von LeanCloud ist, stellen Sie sicher, dass Sie deren Setup-Anleitung für zusätzliche Konfiguration befolgen (z.B. Registrierung auf deren Plattform).

---

Das war's! Sie haben nun `AVOSCloudIM` Version 3.1.6.2 in Ihr iOS-Projekt integriert. Bauen Sie Ihre App in Xcode und führen Sie sie aus, um sie zu testen. Lassen Sie mich wissen, wenn Sie Hilfe mit spezifischen LeanCloud-Funktionen benötigen!