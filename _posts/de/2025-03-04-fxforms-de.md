---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von FXForms in iOS
translated: true
type: note
---

Es sieht so aus, als ob Sie sich auf die Integration der `FXForms`-Bibliothek in ein iOS-Projekt mit CocoaPods beziehen, einem beliebten Abhängigkeitsmanager für Swift- und Objective-C-Projekte. Hier ist eine Schritt-für-Schritt-Anleitung, die Ihnen hilft, `pod 'FXForms', '1.2.13'` in Ihrem Projekt zu verwenden:

---

### Voraussetzungen
1. **CocoaPods installieren**: Wenn Sie CocoaPods noch nicht auf Ihrem Rechner installiert haben, installieren Sie es zuerst, indem Sie diesen Befehl in Ihrem Terminal ausführen:
   ```bash
   sudo gem install cocoapods
   ```
2. **Xcode-Projekt**: Stellen Sie sicher, dass Sie ein vorhandenes Xcode-Projekt haben, in das Sie `FXForms` integrieren möchten.

---

### Schritte zur Verwendung von `pod 'FXForms', '1.2.13'`

#### 1. **Zum Projektverzeichnis navigieren**
Öffnen Sie Ihr Terminal und wechseln Sie in das Verzeichnis, das Ihre Xcode-Projektdatei (`.xcodeproj`) enthält:
```bash
cd /pfad/zu/ihrem/projekt
```

#### 2. **Podfile initialisieren (falls noch nicht vorhanden)**
Wenn Sie noch keine `Podfile` in Ihrem Projektverzeichnis haben, erstellen Sie eine, indem Sie folgenden Befehl ausführen:
```bash
pod init
```
Dies erzeugt eine `Podfile` in Ihrem Projektverzeichnis.

#### 3. **Podfile bearbeiten**
Öffnen Sie die `Podfile` in einem Texteditor (z.B. `nano`, `vim` oder einem Code-Editor wie VS Code) und fügen Sie den `FXForms`-Pod mit der spezifischen Version `1.2.13` hinzu. Ihre `Podfile` sollte in etwa so aussehen:

```ruby
platform :ios, '9.0'  # Gibt die minimale iOS-Version an (bei Bedarf anpassen)
use_frameworks!       # Optional, einbinden wenn Sie Swift oder Frameworks verwenden

target 'IhrProjektName' do
  # Pods für IhrProjektName
  pod 'FXForms', '1.2.13'
end
```

- Ersetzen Sie `'IhrProjektName'` mit dem tatsächlichen Namen Ihres Xcode-Targets (diesen finden Sie in Xcode unter Ihren Projekteinstellungen).
- Die Zeile `pod 'FXForms', '1.2.13'` gibt an, dass Sie Version `1.2.13` der `FXForms`-Bibliothek verwenden möchten.

#### 4. **Pod installieren**
Speichern Sie die `Podfile` und führen Sie dann den folgenden Befehl in Ihrem Terminal aus, um die angegebene Version von `FXForms` zu installieren:
```bash
pod install
```
Dies lädt `FXForms` Version `1.2.13` herunter und integriert es in Ihr Projekt. Bei Erfolg sehen Sie eine Ausgabe, die anzeigt, dass die Pods installiert wurden.

#### 5. **Workspace öffnen**
Nach dem Ausführen von `pod install` wird eine `.xcworkspace`-Datei in Ihrem Projektverzeichnis erstellt. Öffnen Sie diese Datei (nicht die `.xcodeproj`) in Xcode:
```bash
open IhrProjektName.xcworkspace
```

#### 6. **FXForms im Code