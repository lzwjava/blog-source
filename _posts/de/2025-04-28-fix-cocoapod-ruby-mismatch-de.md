---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Beheben von CocoaPod-Ruby-Versionskonflikten unter macOS
translated: true
type: note
---

Ich sehe, was passiert: Dein System-Ruby- und Gems-Setup ist etwas vermischt, weshalb der Befehl `pod deintegrate` CocoaPods nicht finden kann. Lass uns das Schritt für Schritt durchgehen:

---

### Problem
- Du bist auf macOS (wahrscheinlich `arm64`, M1/M2).
- Du hast Ruby aktualisiert (auf 3.4.1 via Homebrew).
- Deine `pod`-Executable gehört zum älteren Ruby (3.3.0 Gem-Pfad: `/opt/homebrew/lib/ruby/gems/3.3.0/bin/pod`).
- Aber jetzt ist Ruby 3.4.1 aktiv, daher kann es die `cocoapods`-Gems am richtigen Ort nicht finden.

Diese Fehlanpassung ist der Grund für den Fehler.

---

### Lösungen

#### 1. CocoaPods mit dem Ruby neu installieren, das du tatsächlich ausführst
```bash
gem install cocoapods
```

Dann überprüfen mit:
```bash
which pod
pod --version
```

---

#### 2. Wenn du das Ruby von `brew` verwendest, ist es am besten, CocoaPods auch via Homebrew zu installieren
```bash
brew install cocoapods
```

Dies vermeidet Ruby-Versionskonflikte komplett.

---

#### 3. Wenn du `rbenv` oder `rvm` verwendest, stelle sicher, dass du dich in der korrekten Ruby-Versionsumgebung befindest
Zum Beispiel mit `rbenv`:
```bash
rbenv global 3.4.1
gem install cocoapods
```

---

#### 4. Alte Pod-Binary-Symlinks bereinigen
Überprüfe, wo der verwaiste `pod`-Befehl herkommt:
```bash
which pod
```
Wenn er auf `/opt/homebrew/lib/ruby/gems/3.3.0/bin/pod` verweist, entferne diesen oder aktualisiere deinen `PATH`, damit der korrekte verwendet wird.

---

✅ Empfohlen (einfach & stabil): Führe einfach   
```bash
brew install cocoapods
```
aus und versuche es dann erneut:
```bash
pod deintegrate
```

---

Möchtest du, dass ich dir helfe, **den PATH so zu reparieren, dass er immer die richtige Pod-Binary auswählt**, oder nur den schnellsten Neuinstallations-Fix?