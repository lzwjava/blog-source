---
audio: false
generated: true
lang: de
layout: post
title: LeanCloud iOS SDK
translated: true
---

Um die `pod 'AVOSCloud', '3.1.6.2'` in einem iOS-Projekt zu verwenden, beziehen Sie sich auf die Integration des AVOSCloud SDK (wahrscheinlich das LeanCloud SDK für Cloud-Dienste) über CocoaPods, einen Abhängigkeitsmanager für iOS-Projekte. Hier ist eine Schritt-für-Schritt-Anleitung zur Einrichtung:

---

### Voraussetzungen
1. **CocoaPods installieren**: Wenn Sie CocoaPods noch nicht installiert haben, installieren Sie es zuerst, indem Sie diesen Befehl in Ihrem Terminal ausführen:
   ```bash
   sudo gem install cocoapods
   ```
2. **Xcode-Projekt**: Stellen Sie sicher, dass Sie ein bestehendes iOS-Projekt in Xcode haben.

---

### Schritte zur Verwendung von `pod 'AVOSCloud', '3.1.6.2'`

1. **Navigieren Sie zu Ihrem Projektverzeichnis**:
   Öffnen Sie Ihr Terminal und gehen Sie zum Verzeichnis, das Ihre `.xcodeproj`-Datei enthält:
   ```bash
   cd /pfad/zu/ihrem/projekt
   ```

2. **Podfile initialisieren** (falls Sie noch keines haben):
   Führen Sie den folgenden Befehl aus, um eine `Podfile`-Datei zu erstellen:
   ```bash
   pod init
   ```

3. **Podfile bearbeiten**:
   Öffnen Sie die `Podfile` in einem Texteditor (z.B. `nano Podfile` oder `open Podfile`) und fügen Sie das `AVOSCloud`-Pod mit der spezifischen Version `3.1.6.2` hinzu. Ihre `Podfile` sollte in etwa so aussehen:
   ```ruby
   platform :ios, '9.0'  # Geben Sie die minimale iOS-Version an (nach Bedarf anpassen)

   target 'IhrAppName' do
     use_frameworks!
     pod 'AVOSCloud', '3.1.6.2'  # Fügen Sie diese Zeile für das AVOSCloud SDK hinzu
   end
   ```
   - Ersetzen Sie `'IhrAppName'` durch den tatsächlichen Namen Ihres Xcode-Ziels.
   - `use_frameworks!` ist erforderlich, wenn Sie Swift oder dynamische Frameworks verwenden.

4. **Pod installieren**:
   Speichern Sie die `Podfile` und führen Sie dann diesen Befehl im Terminal aus, um die angegebene Version von AVOSCloud zu installieren:
   ```bash
   pod install
   ```
   - Dies wird die Version `3.1.6.2` des AVOSCloud SDK herunterladen und Ihr Projekt mit einer `.xcworkspace`-Datei einrichten.

5. **Workspace öffnen**:
   Nach der Installation schließen Sie Ihre `.xcodeproj`, falls sie geöffnet ist, und öffnen Sie die neu erstellte `.xcworkspace`-Datei:
   ```bash
   open IhrAppName.xcworkspace
   ```

6. **AVOSCloud in Ihrem Code importieren und verwenden**:
   - In Objective-C:
     ```objc
     #import <AVOSCloud/AVOSCloud.h>

     - (void)beispiel {
         [AVOSCloud setApplicationId:@"your_app_id" clientKey:@"your_client_key"];
         AVObject *testObject = [AVObject objectWithClassName:@"TestObject"];
         [testObject setObject:@"Hello" forKey:@"message"];
         [testObject save];
     }
     ```
   - In Swift:
     ```swift
     import AVOSCloud

     func beispiel() {
         AVOSCloud.setApplicationId("your_app_id", clientKey: "your_client_key")
         let testObject = AVObject(className: "TestObject")
         testObject["message"] = "Hello"
         try? testObject.save()
     }
     ```
   - Ersetzen Sie `"your_app_id"` und `"your_client_key"` durch Ihre LeanCloud-App-Anmeldeinformationen aus deren Dashboard.

7. **App-Anmeldeinformationen konfigurieren**:
   - Registrieren Sie sich bei [LeanCloud](https://leancloud.app) (oder dem relevanten AVOSCloud-Dienstleister).
   - Holen Sie sich Ihre `App ID` und `Client Key` aus den Einstellungen Ihrer App und setzen Sie sie in Ihrem Code (wie oben gezeigt).

8. **Bauen und Ausführen**:
   Bauen Sie Ihr Projekt in Xcode (`Cmd + B`), um sicherzustellen, dass alles korrekt eingerichtet ist. Wenn Fehler auftreten, überprüfen Sie die Syntax Ihrer Podfile oder Ihre Netzwerkverbindung.

---

### Hinweise
- **Versionsspezifisch**: Durch die Angabe von `'3.1.6.2'` sperren Sie das SDK auf diese genaue Version. Dies könnte ab dem 03. März 2025 veraltet sein. Um die neueste Version zu verwenden, schreiben Sie einfach `pod 'AVOSCloud'` ohne Versionsnummer.
- **Kompatibilität**: Stellen Sie sicher, dass die Version `3.1.6.2` Ihr iOS-Deployment-Ziel unterstützt (z.B. iOS 9.0 oder höher). Überprüfen Sie die [LeanCloud-Dokumentation](https://leancloud.app/docs) für Details.
- **Pod-Aktualisierung**: Wenn Sie CocoaPods aktualisieren oder Probleme beheben müssen, führen Sie aus:
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