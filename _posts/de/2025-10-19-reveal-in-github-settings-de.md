---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Einstellungsfenster für Reveal-In-GitHub
translated: true
type: note
---

### Übersicht
Diese XML-Datei ist ein Interface Builder XIB-Dokument (XML Interface Builder) für eine macOS-Anwendung. XIB-Dateien werden in Xcode verwendet, um Benutzeroberflächen deklarativ zu definieren, insbesondere für Fenster, Views und Steuerelemente in Cocoa-Apps. Diese spezifische Datei definiert die Benutzeroberfläche für ein Einstellungsfenster in einer App namens **Reveal-In-GitHub** (wahrscheinlich ein Hilfsprogramm zum schnellen Öffnen von Quellcodedateien oder Repositories in GitHub aus Ihrer IDE oder Ihrem Dateisystem).

Die Datei zielt auf macOS ab (Cocoa-Laufzeitumgebung) und verwendet Auto Layout (`useAutolayout="YES"`). Sie ist um ein Hauptfensterobjekt herum strukturiert, mit Verbindungen zu einer benutzerdefinierten Controller-Klasse (`RIGSettingWindowController`), Outlets für wichtige Views und verschiedenen UI-Subviews wie Buttons, Labels und einem benutzerdefinierten Container.

Wichtige Metadaten:
- **Tools Version**: Xcode 9.0.1 (toolsVersion="9059"), erstellt auf macOS 10.12.6 (systemVersion="14F27").
- **Fensterverhalten**: Betitelt, schließbar, minimierbar und in der Größe veränderbar. Es berechnet die Key View Loop nicht automatisch neu und verwendet Standardanimationen.
- **Anfangsposition/Größe**: Öffnet sich an Bildschirmposition (527, 176) mit den Abmessungen 651x497 Pixel (auf einem 1440x877 Bildschirm).

Der Ursprung der Datei ist ein `<document>`, das `<dependencies>` (für das Cocoa-Plugin) und `<objects>` (die eigentliche UI-Hierarchie) enthält.

### Hauptkomponenten

#### 1. **File's Owner (Benutzerdefinierter Controller)**
   - **Klasse**: `RIGSettingWindowController`
   - Dies fungiert als der Controller für das Fenster und verwaltet Logik wie das Laden/Speichern von Einstellungen.
   - **Outlets** (Verbindungen zu UI-Elementen):
     - `configsView` → Eine benutzerdefinierte View zur Anzeige von Konfigurationsoptionen (ID: `IKd-Ev-B9V`).
     - `mainView` → Die Content View des Fensters (ID: `se5-gp-TjO`).
     - `window` → Das Einstellungsfenster selbst (ID: `F0z-JX-Cv5`).
   - Der `delegate` des Fensters ist ebenfalls mit diesem Controller verbunden.

#### 2. **Standardobjekte**
   - **First Responder** (`-1`): Platzhalter für die Tastaturereignisbehandlung.
   - **Application** (`-3`): Repräsentiert die NSApplication-Instanz (hier nicht direkt verwendet).

#### 3. **Das Einstellungsfenster**
   - **ID**: `F0z-JX-Cv5`
   - **Titel**: "Reveal-In-GitHub Settings"
   - **Content View** (ID: `se5-gp-TjO`): Eine View in voller Größe (651x497), die sich automatisch mit dem Fenster anpasst. Sie enthält alle Subviews, positioniert mit festen Frames (obwohl Auto Layout aktiviert ist, was darauf hindeutet, dass Constraints möglicherweise programmatisch oder in einer begleitenden .storyboard-Datei hinzugefügt werden).

   **Subviews-Layout** (alle verwenden feste Frames für die Positionierung; y-Koordinaten nehmen von oben nach unten zu):

   | Element | Typ | Position (x, y) | Größe (w x h) | Beschreibung |
   |---------|------|-----------------|--------------|-------------|
   | **Save Button** | `NSButton` (ID: `EuN-9g-Vcg`) | (14, 13) | 137x32 | "Save"-Button unten links (abgerundeter Bezel). Löst die `saveButtonClcked:`-Aktion auf dem Controller aus. Verwendet kleine Systemfont (13pt). |
   | **Reset Default Menus Button** | `NSButton` (ID: `KvN-fn-w7m`) | (151, 12) | 169x32 | Benachbarter "Reset Default Menus"-Button. Löst die `resetMenusButtonClicked:`-Aktion aus. Kleine Systemfont (13pt). |
   | **Config View** | `NSView` (Benutzerdefiniert, ID: `IKd-Ev-B9V`) | (20, 54) | 611x330 | Große, zentrale benutzerdefinierte View mit der Bezeichnung "Config View". Wahrscheinlich ein Container für dynamische Inhalte wie Tabellen, Listen oder Schalter für GitHub-Repo-Konfigurationen (z.B. Repo-Pfade, Auth-Tokens). Diese ist mit dem `configsView`-Outlet verbunden. |
   | **Custom Menu Items Label** | `NSTextField` (ID: `G1C-Td-n9Y`) | (18, 425) | 187x17 | Statisches Label "Custom Menu Items" nahe dem unteren Rand. Helvetica Neue (17pt), Label-Farbe. |
   | **Clear Default Repos Button** | `NSButton` (ID: `KvN-fn-w7m`) | (14, 449) | 164x32 | "Clear Default Repos"-Button unten links. Löst die `clearButtonClicked:`-Aktion aus. Kleine Systemfont (13pt). |
   | **Menu Title Label** | `NSTextField` (ID: `UUf-Cr-5zs`) | (20, 392) | 77x18 | Statisches Label "Menu Title". Helvetica Neue (14pt), Label-Farbe. |
   | **Keyboard Shortcut Label** | `NSTextField` (ID: `rMv-by-SKS`) | (112, 391) | 63x19 | Statisches Label "⌃⇧⌘ +" (Control+Shift+Command +). Lucida Grande UI (15pt), Label-Farbe. Zeigt einen anpassbaren globalen Shortcut für das App-Menü an. |
   | **URL Pattern Label** | `NSTextField` (ID: `zW4-cw-Rhb`) | (410, 392) | 94x18 | Statisches Label "URL Pattern ". Systemfont (15pt), Label-Farbe. Wahrscheinlich für die Konfiguration von GitHub-URL-Vorlagen (z.B. für Deep-Linking zu Dateien/Blame-Views). |

   - **Layout-Hinweise**:
     - Elemente sind meist linksbündig (x=14-20) für ein kompaktes, formularähnliches Design.
     - Oben: Aktionsbuttons (Save/Reset).
     - Mitte: Große Config View (Hauptbereich für die Repo-/Einstellungsverwaltung).
     - Unten: Labels für die Menüanpassung und ein Clear-Button.
     - Alle Textfelder sind nicht editierbar (statische Labels), was darauf hindeutet, dass die Benutzereingabe innerhalb der Config View oder über separate, hier nicht definierte Felder erfolgt.
     - Farben: Systemstandard (Label/Control-Farben für Barrierefreiheit).
     - Fonts: Mix aus System, Helvetica Neue und Lucida Grande für ein natives macOS-Gefühl.

### Zweck und Funktionalität
Dieses Einstellungsfenster ermöglicht Benutzern:
- **Repos/Konfigurationen verwalten**: Über die zentrale "Config View" (z.B. Standard-GitHub-Repos hinzufügen/entfernen).
- **Menüs anpassen**: Einen Menütitel, einen globalen Tastaturkurzbefehl (⌃⇧⌘+) und URL-Muster für das Aufrufen von Dateien in GitHub festlegen.
- **Änderungen speichern**: Einstellungen speichern oder Standardwerte zurücksetzen/löschen mit dedizierten Buttons.

Der Controller (`RIGSettingWindowController`) behandelt die Button-Aktionen:
- `saveButtonClcked:` – Speichert Benutzeränderungen (z.B. in UserDefaults oder einer plist).
- `resetMenusButtonClicked:` – Stellt die Werkseinstellungen für die Menüs wieder her.
- `clearButtonClicked:` – Entfernt Standard-Repo-Einträge.

Dieses XIB wird wahrscheinlich programmatisch im App-Code geladen (z.B. `NSNib(nibNamed: "Settings", bundle: nil)`), wobei die benutzerdefinierte View dynamisch gefüllt wird (z.B. mit einer NSTableView für Repo-Listen).

Wenn Sie diese App erstellen oder modifizieren, können Sie das XIB in Xcodes Interface Builder öffnen, um das Layout visuell darzustellen/zu bearbeiten. Für die Code-Integration sollten Sie nach IBAction-Methoden in der Controller-Klasse suchen, die den Aktions-Selektoren entsprechen.