---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Behebung von Flutter Xcode Code Signing Fehlern
translated: true
type: note
---

Du hast einen häufigen Flutter/Xcode Code-Signing-Fehler: Xcode/`security` hat keine gültigen Signaturidentitäten gefunden, daher kann `flutter run` die App nicht für ein physisches Gerät signieren. Im Folgenden findest du eine klare, geordnete Liste von Lösungen und Troubleshooting-Befehlen – wähle den gewünschten Ansatz (sofort im Simulator ausführen oder Signierung für ein echtes Gerät einrichten). Ich werde nicht nach weiteren Informationen fragen – ich gehe davon aus, dass du das Problem jetzt beheben möchtest.

---

# Schnelle Optionen (wähle eine)

**A — Im Simulator ausführen (keine Code-Signing erforderlich)**
Wenn du schnell loslegen möchtest, ohne dich mit Zertifikaten zu beschäftigen:

1. Simulator öffnen: `open -a Simulator`
2. Flutter für den Simulator ausführen:
   `flutter run -d "$(xcrun simctl list devices | grep -m1 -o "iPhone.*(Simulator)" | sed 's/ (Simulator)//')"`
   Oder einfacher: `flutter run -d iPhone-14` (ersetze durch einen verfügbaren Simulator-Namen aus `xcrun simctl list`).

**B — Signierung beheben, um auf einem echten Gerät bereitzustellen (empfohlen für Gerätetests)**
Folge den untenstehenden Schritten der Reihe nach.

---

# Schritte zur Behebung der Signierung für Gerätebereitstellung

## 1) Umgebung & grundlegende Checks bestätigen

Führe diese Befehle aus und notiere die Ausgabe:

```bash
flutter doctor -v
xcode-select --print-path
xcodebuild -version
security find-identity -p codesigning -v
xcrun simctl list devices
```

`security find-identity -p codesigning -v` sollte mindestens eine Identität anzeigen. Bei dir wurde `0 valid identities found` angezeigt – deshalb schlägt es fehl.

## 2) Automatische Xcode-Signierung verwenden (am einfachsten)

1. Workspace öffnen:
   `open ios/Runner.xcworkspace`
2. In Xcode: Wähle das `Runner` Projekt → `Runner` Target → **Signing & Capabilities**.
3. Setze **Team** auf deine Apple ID / Apple Developer Account. Wenn deine Apple ID nicht hinzugefügt ist:

   * Xcode → Preferences → Accounts → `+` → Apple ID hinzufügen.
4. Aktiviere **Automatically manage signing**.
5. Stelle sicher, dass die **Bundle Identifier** eindeutig ist (Reverse-DNS-Stil, z.B. `com.deinname.deineapp`).
6. Xcode wird versuchen, ein Entwicklungszertifikat & Provisioning Profile zu erstellen; wenn du Aufforderungen siehst, erlaube Xcode die Verwaltung.

> Hinweis: Für die vollständige Bereitstellung auf einem beliebigen Gerät benötigst du eine Apple Developer Membership ($99/Jahr). Xcode kann eine kostenlose Apple ID für "Free Provisioning" verwenden, aber dies ist eingeschränkt (Geräteanzahl, keine bestimmten Berechtigungen).

## 3) Gerät registrieren (falls erforderlich)

Wenn Xcode dein Gerät nicht automatisch registrieren kann, gehe zum Apple Developer Portal → Certificates, IDs & Profiles → Devices → füge die Geräte-UDID hinzu. Du erhältst die Geräte-UDID, indem du das Gerät verbindest und es im Fenster "Devices and Simulators" von Xcode auswählst.

## 4) Zertifikat manuell generieren/importieren (falls du bereits eine .p12 hast)

Wenn du ein `.p12`-Zertifikat und einen privaten Schlüssel hast:

```bash
security import /pfad/zum/zertifikat.p12 -k ~/Library/Keychains/login.keychain-db -P "P12_PASSWORT" -T /usr/bin/codesign
```

Dann führe `security find-identity -p codesigning -v` erneut aus, um zu bestätigen, dass es erscheint.

## 5) Wenn du bevorzugst, dass Xcode Zertifikate für dich erstellt

In Xcode → Accounts → Wähle deine Apple ID → Manage Certificates → `+` → füge **iOS Development** hinzu. Dies erstellt ein Zertifikat in deinem Keychain und es wird in `security find-identity` angezeigt.

## 6) Sicherstellen, dass Command Line Tools gesetzt sind

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

Dann Lizenz akzeptieren, falls nötig:

```bash
sudo xcodebuild -license accept
```

## 7) Nachdem die Signierung eingerichtet ist, von Terminal ausführen

Aus dem Projektverzeichnis:

```bash
flutter clean
flutter pub get
flutter run
```

Bei mehreren Geräten, gib `-d <Geräte-ID>` an.

---

# Troubleshooting-Tipps & häufige Fallstricke

* **"0 valid identities found" besteht fort** – bestätige, dass der private Schlüssel des Zertifikats im Login-Keychain ist (öffne Keychain Access → login). Wenn du das Zertifikat, aber nicht den privaten Schlüssel importiert hast, schlägt die Signierung fehl.
* **Bundle ID stimmt nicht überein** – die App ID im Developer Portal muss exakt mit der Bundle Identifier in Xcode übereinstimmen (Wildcards sind in manchen Fällen erlaubt).
* **Team nicht ausgewählt** – Xcode zeigt "No account" an – füge Apple ID in Xcode Preferences → Accounts hinzu.
* **Provisioning Profile abgelaufen** – überprüfe das Developer Portal und regeneriere das Provisioning Profile.
* **Einschränkungen bei kostenloser Bereitstellung** – wenn du eine kostenlose Apple ID verwendest, musst du möglicherweise alle 7 Tage erneuern und hast limitierte Geräte.
* **CI / Automatisierung** – verwende `fastlane match` oder App Store Connect APIs, um Zertifikate und Profile zentral zu verwalten.
* **Codesign-Berechtigungsfehler** – stelle sicher, dass der Keychain-Eintrag Codesign-Zugriff gewährt; manchmal musst du `/usr/bin/codesign` manuell erlauben, auf den privaten Schlüssel im Keychain zuzugreifen.
* **Wenn `flutter run` weiterhin fehlschlägt**, führe den Xcode-Build aus, um einen detaillierteren Fehler zu sehen: öffne den Workspace und klicke auf Run in Xcode; überprüfe Signing & Capabilities Fehler in der UI.

---

# Nützliche Befehle zum Kopieren

Codesigning-Identitäten auflisten:

```bash
security find-identity -p codesigning -v
```

`.p12` importieren:

```bash
security import /pfad/zum/deinzertifikat.p12 -k ~/Library/Keychains/login.keychain-db -P "P12PASSWORT" -T /usr/bin/codesign
```

Xcode Command Line Tools setzen:

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

iOS Workspace öffnen:

```bash
open ios/Runner.xcworkspace
```

---

# Wenn du möchtest, kann ich

* dir die exakte Abfolge der Xcode-Klicks geben, um Schritt-für-Schritt Zertifikat/Profil zu erstellen (die Kernschritte habe ich bereits eingefügt), oder
* `fastlane`/`match` Beispielbefehle bereitstellen, wenn du Automatisierung für mehrere Maschinen/CI möchtest, oder
* helfen, jegliche neue Fehlerausgabe zu interpretieren, nachdem du den Weg der automatischen Xcode-Signierung versucht hast.

Sag mir, welchen Weg du gewählt hast (Simulator jetzt / Xcode automatisch / manueller p12 Import / CI) und füge alle neuen Fehler ein, falls es weiterhin fehlschlägt – ich gebe dir die nächsten Schritte.