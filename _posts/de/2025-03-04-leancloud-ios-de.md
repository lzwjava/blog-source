---
audio: false
generated: true
lang: de
layout: post
title: LeanCloud iOS SDK
translated: true
type: note
---

Um `pod 'AVOSCloud', '3.1.6.2'` in einem iOS-Projekt zu verwenden, bezieht sich dies auf die Integration des AVOSCloud SDK (wahrscheinlich das LeanCloud SDK für Cloud-Dienste) über CocoaPods, einen Abhängigkeitsmanager für iOS-Projekte. Hier ist eine Schritt-für-Schritt-Anleitung zur Einrichtung:

---

### Voraussetzungen
1. **CocoaPods installieren**: Wenn Sie CocoaPods nicht installiert haben, installieren Sie es zuerst, indem Sie dies in Ihrem Terminal ausführen:
   ```bash
   sudo gem install cocoapods
   ```
2. **Xcode-Projekt**: Stellen Sie sicher, dass Sie ein vorhandenes iOS-Projekt in Xcode haben.

---

### Schritte zur Verwendung von `pod 'AVOSCloud', '3.1.6.2'`

1. **Navigieren Sie zu Ihrem Projektverzeichnis**:
   Öffnen Sie Ihr Terminal und wechseln Sie in das Verzeichnis, das Ihre `.xcodeproj`-Datei enthält:
   ```bash
   cd /pfad/zu/ihrem/projekt
   ```

2. **Eine Podfile initialisieren** (falls Sie noch keine haben):
   Führen Sie den folgenden Befehl aus, um eine `Podfile` zu erstellen:
   ```bash
   pod init
   ```

3. **Die Podfile bearbeiten**:
   Öffnen Sie die `Podfile` in einem Texteditor (z.B. `nano Podfile` oder `open Podfile`) und fügen Sie den `AVOSCloud`-Pod mit der spezifischen Version `3.1.6.2` hinzu. Ihre `Podfile` sollte in etwa so aussehen:
   ```ruby
   platform :ios, '9.0'  # Gibt die minimale iOS-Version an (bei Bedarf anpassen)

   target 'IhrAppName' do
     use_frameworks!
     pod 'AVOSCloud', '3.1.6.2'  # Fügen Sie diese Zeile für das AVOSCloud SDK hinzu
   end
   ```
   - Ersetzen Sie `'IhrAppName'` mit dem tatsächlichen Namen Ihres Xcode-Targets.
   - `use_frameworks!` ist erforderlich, wenn Sie Swift oder dynamische Frameworks verwenden.

4. **Den Pod installieren**:
   Speichern Sie die `Podfile` und führen Sie dann diesen Befehl im Terminal aus, um die angegebene Version von AVOSCloud zu installieren:
   ```bash
   pod install
   ```
   - Dies lädt die Version `3.1.6.2` des AVOSCloud SDK herunter und richtet Ihr Projekt mit einer `.xcworkspace`-Datei ein.

5. **Den Workspace öffnen**:
   Schließen Sie nach der Installation Ihre `.xcodeproj`, falls sie geöffnet ist, und öffnen Sie die neu erstellte `.xcworkspace`-Datei:
   ```bash
   open IhrAppName.xcworkspace
   ```

6. **AVOSCloud in Ihrem Code importieren und verwenden**:
   - In Objective-C:
     ```objc
     #import <AVOSCloud/AVOSCloud.h>

     - (void)example {
         [AVOSCloud setApplicationId:@"ihre_app_id" clientKey:@"ihre_client_key"];
         AVObject *testObject = [AVObject objectWithClassName:@"TestObject"];
         [testObject setObject:@"Hallo" forKey:@"message"];
         [testObject save];
     }
     ```
   - In Swift:
     ```swift
     import AVOSCloud

     func example() {
         AVOSCloud.setApplicationId("ihre_app_id", clientKey: "ihre_client_key")
         let testObject = AVObject(className: "TestObject")
         testObject["message"] = "Hallo"
         try? testObject.save()
     }
     ```
   - Ersetzen Sie `"ihre_app_id"` und `"ihre_client_key"` mit Ihren LeanCloud-App-Anmeldedaten aus deren Dashboard.

7. **App-Anmeldedaten konfigurieren**:
   - Registrieren Sie sich bei [LeanCloud](https://leancloud.app) (oder dem entsprechenden AVOSCloud-Dienstanbieter).
   - Holen Sie sich Ihre `App ID` und `Client Key` aus den Einstellungen Ihrer App und setzen Sie sie in Ihrem Code (wie oben gezeigt).

8. **Erstellen und Ausführen**:
   Bauen Sie Ihr Projekt in Xcode (`Cmd + B`), um sicherzustellen, dass alles korrekt eingerichtet ist. Falls Fehler auftreten, überprüfen Sie die Syntax Ihrer Podfile oder Ihre Netzwerkverbindung.

---

### Hinweise
- **Versionsspezifisch**: Durch die Angabe von `'3.1.6.2'` binden Sie das SDK an diese exakte Version. Diese könnte ab dem 03. März 2025 veraltet sein. Um die neueste Version zu verwenden, schreiben Sie einfach `pod 'AVOSCloud'` ohne Versionsnummer.
- **Kompatibilität**: Stellen Sie sicher, dass die Version `3.1.6.2` Ihr iOS Deployment Target (z.B. iOS 9.0 oder höher) unterstützt. Weitere Details finden Sie in der [LeanCloud-Dokumentation](https://leancloud.app/docs).
- **Pod Update**: Wenn Sie CocoaPods aktualisieren oder Probleme beheben müssen, führen Sie aus:
  ```bash
  pod update
  ```
- **Fehlerbehebung**: Wenn `pod install` fehlschlägt, versuchen Sie:
  ```bash
  pod repo update
  pod install --verbose
  ```

---

Lassen Sie mich wissen, wenn Sie Hilfe bei einem bestimmten Teil benötigen, wie z.B. der Integration eines Features (z.B. Push-Benachrichtigungen, Echtzeit-Nachrichten) von AVOSCloud!