---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von MBProgressHUD in iOS
translated: true
---

Es sieht so aus, als ob du dich erkundigst, wie man die `MBProgressHUD`-Bibliothek in einem iOS-Projekt, speziell Version `0.9.1`, über eine Podfile in CocoaPods verwendet. Lasse mich dich Schritt für Schritt durch den Prozess führen.

### Was ist MBProgressHUD?
`MBProgressHUD` ist eine beliebte Drittanbieter-Bibliothek für iOS, die eine einfache Möglichkeit bietet, ein HUD (Heads-Up Display) mit Aktivitätsanzeigen, Fortschrittsbalken oder benutzerdefinierten Ansichten anzuzeigen, die typischerweise verwendet werden, um Ladezustände oder kurze Nachrichten anzuzeigen.

### Schritte zur Verwendung von `pod 'MBProgressHUD', '0.9.1'`

#### 1. **Installieren von CocoaPods (falls noch nicht installiert)**
CocoaPods ist ein Abhängigkeitsmanager für iOS-Projekte. Wenn du es noch nicht installiert hast, führe diesen Befehl in deinem Terminal aus:
```bash
sudo gem install cocoapods
```

#### 2. **Einrichten einer Podfile**
- Navigiere in deinem Terminal zu deinem Xcode-Projektverzeichnis:
  ```bash
  cd /path/to/your/project
  ```
- Wenn du noch keine Podfile hast, erstelle eine, indem du folgendes ausführst:
  ```bash
  pod init
  ```
- Öffne die `Podfile` in einem Texteditor (z. B. `nano Podfile` oder `open Podfile`).

#### 3. **MBProgressHUD zur Podfile hinzufügen**
In deiner `Podfile` füge die Zeile für `MBProgressHUD` Version `0.9.1` innerhalb des Zielblocks für deine App hinzu. Es sollte in etwa so aussehen:
```ruby
platform :ios, '9.0'  # Gib dein Deployment-Ziel an

target 'YourAppName' do
  use_frameworks!
  pod 'MBProgressHUD', '0.9.1'
end
```
- Ersetze `'YourAppName'` durch den tatsächlichen Namen deines Xcode-Ziels.
- Die Zeile `platform :ios, '9.0'` setzt die minimale iOS-Version fest; passe sie entsprechend den Anforderungen deines Projekts an.

#### 4. **Installieren des Pods**
- Speichere die `Podfile` und führe diesen Befehl im Terminal aus:
  ```bash
  pod install
  ```
- Dies lädt `MBProgressHUD` Version `0.9.1` herunter und integriert es in dein Projekt. Bei Erfolg siehst du eine Bestätigungsausgabe.

#### 5. **Öffnen des Workspaces**
- Nach der Installation schließe dein Xcode-Projekt (falls geöffnet) und öffne die neu erstellte `.xcworkspace`-Datei (z. B. `YourAppName.xcworkspace`) anstelle der `.xcodeproj`-Datei. CocoaPods erstellt diesen Workspace, um Abhängigkeiten zu verwalten.

#### 6. **Verwenden von MBProgressHUD in deinem Code**
- **Swift**: Importiere das Modul und verwende es in deinem Code:
  ```swift
  import MBProgressHUD

  class ViewController: UIViewController {
      override func viewDidLoad() {
          super.viewDidLoad()

          // Zeige ein einfaches HUD mit einer Ladeanzeige an
          let hud = MBProgressHUD.showAdded(to: self.view, animated: true)
          hud.label.text = "Loading..."

          // Verstecke es nach einiger Zeit (z. B. 2 Sekunden)
          DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
              hud.hide(animated: true)
          }
      }
  }
  ```

- **Objective-C**: Importiere die Header-Datei und verwende sie:
  ```objc
  #import <MBProgressHUD/MBProgressHUD.h>

  @interface ViewController ()
  @end

  @implementation ViewController
  - (void)viewDidLoad {
      [super viewDidLoad];

      // Zeige ein einfaches HUD mit einer Ladeanzeige an
      MBProgressHUD *hud = [MBProgressHUD showHUDAddedTo:self.view animated:YES];
      hud.label.text = @"Loading...";

      // Verstecke es nach einiger Zeit (z. B. 2 Sekunden)
      dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 2 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
          [hud hideAnimated:YES];
      });
  }
  @end
  ```

#### 7. **Gängige MBProgressHUD-Funktionen**
- **Grundlegendes HUD**: Wie oben gezeigt, eine drehende Anzeige mit optionalem Text anzeigen.
- **Nur benutzerdefinierter Text**:
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .text
  hud.label.text = "Done!"
  hud.hide(animated: true, afterDelay: 1.5)
  ```
- **Fortschrittsbalken**:
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .determinate
  hud.progress = 0.5 // 50% Fortschritt
  ```

#### Hinweise
- **Version 0.9.1**: Dies ist eine ältere Version (veröffentlicht um 2015). Die neueste Version bis März 2025 ist viel neuer (z. B. 1.2.0 oder höher). Um die neueste zu verwenden, schreibe einfach `pod 'MBProgressHUD'` ohne Versionsnummer. Überlege, ob du auf die neueste Version aktualisierst, es sei denn, du benötigst 0.9.1 aus Kompatibilitätsgründen.
- **Dokumentation**: Besuche die [MBProgressHUD GitHub-Seite](https://github.com/jdg/MBProgressHUD) für weitere Optionen und Beispiele. Version 0.9.1 könnte weniger Funktionen als moderne Veröffentlichungen haben.

Lass mich wissen, wenn du Hilfe beim Fehlersuchen oder spezifischere Beispiele benötigst!