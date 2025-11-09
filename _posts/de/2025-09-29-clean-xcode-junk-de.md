---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Xcode-Datenmüll bereinigen und Festplattenspeicher freigeben
translated: true
type: note
---

Gute Frage 👍 Xcode (und der iOS Simulator) können mit der Zeit eine *Menge* Datenmüll ansammeln – Build-Cache, Derived Data, Simulator-Geräte, Device-Support-Dateien, Logs usw. Das Bereinigen davon befreit Gigabytes an Speicherplatz. Hier ist ein strukturierter Ansatz:

---

### 1. Derived Data löschen (Build-Cache)

Dies entfernt alte Build-Produkte, Zwischendateien und Indizes.

* Über die **Xcode-Oberfläche**:
  `Xcode → Einstellungen → Locations → Derived Data → Pfeil anklicken → Ordner löschen.`
* Über das **Terminal**:

  ```bash
  rm -rf ~/Library/Developer/Xcode/DerivedData/*
  ```

---

### 2. Simulator-Daten bereinigen

* Simulator-Inhalte zurücksetzen oder löschen:

  ```bash
  xcrun simctl erase all
  ```

  (löscht Apps & Daten, behält aber Gerätedefinitionen)

* Um alle unbenutzten Simulator-Geräte zu entfernen (wenn sich alte iOS-Versionen angesammelt haben):

  ```bash
  xcrun simctl delete unavailable
  ```

* Um alle Simulator-Geräte zu löschen (Vorsicht, entfernt alles):

  ```bash
  xcrun simctl delete all
  ```

* Schwere Verzeichnisse manuell löschen:

  ```bash
  rm -rf ~/Library/Developer/CoreSimulator/Devices/*
  ```

---

### 3. Alte Device Support Files entfernen

Wenn Sie echte Geräte verbinden, lädt Xcode Debugging-Symbole für jede iOS-Version herunter. Diese häufen sich an.

```bash
rm -rf ~/Library/Developer/Xcode/iOS\ DeviceSupport/*
```

---

### 4. Archives bereinigen

App-Archives von "Product → Archive" verbrauchen viel Speicher.

* Über den Organizer in Xcode → Archives → alte Einträge löschen.
* Oder via Terminal:

  ```bash
  rm -rf ~/Library/Developer/Xcode/Archives/*
  ```

---

### 5. Logs bereinigen

```bash
rm -rf ~/Library/Developer/Xcode/DocumentationCache/*
rm -rf ~/Library/Developer/Xcode/ios device logs/*
rm -rf ~/Library/Logs/CoreSimulator/*
```

---

### 6. Abgeleitete Indizes & Module Cache bereinigen

```bash
rm -rf ~/Library/Developer/Xcode/DerivedDataModuleCache/*
```

---

### 7. Optional: Vollständiger Reset

Wenn Sie Xcode-bezogene Caches komplett zurücksetzen möchten:

```bash
rm -rf ~/Library/Developer/Xcode/*
rm -rf ~/Library/Developer/CoreSimulator/*
```

(Dies entfernt alles: Simulatoren, Archives, Derived Data, etc. Der nächste Start von Xcode fühlt sich an wie eine "frische Installation".)

---

⚠️ **Tipps**

* Beenden Sie Xcode und den Simulator immer, bevor Sie diese Befehle ausführen.
* Verwenden Sie `du -sh ~/Library/Developer/*`, um zu sehen, welche Ordner am meisten Speicher belegen.
* Manchmal reicht `Clean Build Folder` (`⇧⌘K`) in Xcode aus, aber eine gründliche Reinigung spart mehr Platz.

---

Möchtest du, dass ich dir ein **einziges Script** gebe, mit dem du den gesamten üblichen Datenmüll auf einmal bereinigen kannst (mit optionalen Flags)?