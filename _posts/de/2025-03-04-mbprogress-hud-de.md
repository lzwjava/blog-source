---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von MBProgressHUD in iOS
translated: true
type: note
---

Es sieht so aus, als ob Sie nach der Verwendung der `MBProgressHUD`-Bibliothek in einem iOS-Projekt fragen, speziell Version `0.9.1`, über eine Podfile in CocoaPods. Lassen Sie mich Sie Schritt für Schritt durch den Prozess führen.

### Was ist MBProgressHUD?
`MBProgressHUD` ist eine beliebte Drittanbieter-Bibliothek für iOS, die eine einfache Möglichkeit bietet, ein HUD (Heads-Up Display) mit Aktivitätsindikatoren, Fortschrittsbalken oder benutzerdefinierten Ansichten anzuzeigen. Typischerweise wird es verwendet, um Ladezustände oder kurze Nachrichten anzuzeigen.

### Schritte zur Verwendung von `pod 'MBProgressHUD', '0.9.1'`

#### 1. **CocoaPods installieren (falls noch nicht geschehen)**
CocoaPods ist ein Dependency-Manager für iOS-Projekte. Wenn Sie es nicht installiert haben, führen Sie diesen Befehl in Ihrem Terminal aus:
```bash
sudo gem install cocoapods
```

#### 2. **Eine Podfile einrichten**
- Navigieren Sie in Ihrem Terminal zu Ihrem Xcode-Projektverzeichnis:
  ```bash
  cd /pfad/zu/ihrem/projekt
  ```
- Wenn Sie noch keine Podfile haben, erstellen Sie eine, indem Sie ausführen:
  ```bash
  pod init
  ```
- Öffnen Sie die `Podfile` in einem Texteditor (z.B. `nano Podfile` oder `open Podfile`).

#### 3. **MBProgressHUD zu Ihrer Podfile hinzufügen**
Fügen Sie in Ihrer `Podfile` die Zeile für `MBProgressHUD` Version `0.9.1` innerhalb des Target-Blocks für Ihre App hinzu. Es sollte ungefähr so aussehen:
```ruby
platform :ios, '9.0'  # Geben Sie Ihr Deployment Target an

target 'IhrAppName' do
  use_frameworks!
  pod 'MBProgressHUD', '0.9.1'
end
```
- Ersetzen Sie `'IhrAppName'` mit dem tatsächlichen Namen Ihres Xcode-Targets.
- Die Zeile `platform :ios, '9.0'` setzt die minimale iOS-Version; passen Sie sie basierend auf den Anforderungen Ihres Projekts an.

#### 4. **Das Pod installieren**
- Speichern Sie die `Podfile` und führen Sie diesen Befehl im Terminal aus:
  ```bash
  pod install
  ```
- Dies lädt `MBProgressHUD` Version `0.9.1` herunter und integriert es in Ihr Projekt. Bei Erfolg sehen Sie eine Ausgabe, die die Installation bestätigt.

#### 5. **Den Workspace öffnen**
- Schließen Sie nach der Installation Ihr Xcode-Projekt (falls geöffnet) und öffnen Sie die neu erstellte `.xcworkspace`-Datei (z.B. `IhrAppName.xcworkspace`) anstelle der `.xcodeproj`-Datei. CocoaPods generiert diesen Workspace, um Abhängigkeiten zu verwalten.

#### 6. **MBProgressHUD in Ihrem Code verwenden**
- **Swift**: Importieren Sie das Modul und verwenden Sie es in Ihrem Code:
  ```swift
  import MBProgressHUD

  class ViewController: UIViewController {
      override func viewDidLoad() {
          super.viewDidLoad()
          
          // Ein einfaches HUD mit einem Ladeindikator anzeigen
          let hud = MBProgressHUD.showAdded(to: self.view, animated: true)
          hud.label.text = "Lädt..."
          
          // Nach einiger Zeit ausblenden (z.B. 2 Sekunden)
          DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
              hud.hide(animated: true)
          }
      }
  }
  ```

- **Objective-C**: Importieren Sie den Header und verwenden Sie ihn:
  ```objc
  #import <MBProgressHUD/MBProgressHUD.h>

  @interface ViewController ()
  @end

  @implementation ViewController
  - (void)viewDidLoad {
      [super viewDidLoad];
      
      // Ein einfaches HUD mit einem Ladeindikator anzeigen
      MBProgressHUD *hud = [MBProgressHUD showHUDAddedTo:self.view animated:YES];
      hud.label.text = @"Lädt...";
      
      // Nach einiger Zeit ausblenden (z.B. 2 Sekunden)
      dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 2 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
          [hud hideAnimated:YES];
      });
  }
  @end
  ```

#### 7. **Häufige MBProgressHUD-Funktionen**
- **Einfaches HUD**: Wie oben gezeigt, einen drehenden Indikator mit optionalem Text anzeigen.
- **Nur benutzerdefinierter Text**:
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .text
  hud.label.text = "Erledigt!"
  hud.hide(animated: true, afterDelay: 1.5)
  ```
- **Fortschrittsbalken**:
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .determinate
  hud.progress = 0.5 // 50% Fortschritt
  ```

#### Hinweise
- **Version 0.9.1**: Dies ist eine ältere Version (veröffentlicht um 2015). Die neueste Version Stand März 2025 ist viel neuer (z.B. 1.2.0 oder höher). Um die neueste zu verwenden, schreiben Sie einfach `pod 'MBProgressHUD'` ohne Versionsnummer. Erwägen Sie ein Update, es sei denn, Sie benötigen speziell 0.9.1 aus Kompatibilitätsgründen.
- **Dokumentation**: Schauen Sie auf der [MBProgressHUD GitHub-Seite](https://github.com/jdg/MBProgressHUD) für weitere Optionen und Beispiele. Version 0.9.1 könnte weniger Funktionen haben als moderne Versionen.

Lassen Sie mich wissen, wenn Sie Hilfe bei der Fehlerbehebung oder spezifischere Beispiele benötigen!