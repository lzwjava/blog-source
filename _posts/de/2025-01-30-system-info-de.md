---
audio: false
lang: de
layout: post
title: Systeminformation auf macOS
translated: true
---

Um Systeminformationen auf Ihrem macOS zu erhalten, können Sie mehrere integrierte Tools und Befehle verwenden. Hier sind einige Methoden, um verschiedene Arten von Systeminformationen abzurufen:

### 1. **Systeminformationen-App**
Die App „Systeminformationen“ bietet eine umfassende Übersicht über die Hardware und Software Ihres Mac.

- Öffnen Sie **Spotlight-Suche** durch Drücken von `Cmd + Leertaste` und geben Sie "Systeminformationen" ein, dann drücken Sie Enter.
- Alternativ können Sie es über das **Apple-Menü** > **Über diesen Mac** > **Systembericht** öffnen.

### 2. **Über diesen Mac**
Dies bietet einen schnellen Überblick über die Spezifikationen Ihres Mac.

- Klicken Sie auf das **Apple-Menü** in der linken oberen Ecke des Bildschirms.
- Wählen Sie **Über diesen Mac**. Dies zeigt grundlegende Informationen wie die macOS-Version, den Prozessor, den Arbeitsspeicher und die Seriennummer an.

### 3. **Terminal-Befehle**
Sie können das Terminal verwenden, um detaillierte Systeminformationen mit verschiedenen Befehlen abzurufen.

- Öffnen Sie **Terminal** über `Anwendungen` > `Dienstprogramme` > `Terminal` oder durch Suchen in Spotlight.

#### Grundlegende Systeminformationen
```sh
system_profiler SPHardwareDataType
```

#### Detaillierte Systeminformationen
```sh
system_profiler
```

#### CPU-Informationen
```sh
sysctl -n machdep.cpu.brand_string
```

#### Arbeitsspeicherinformationen
```sh
sysctl hw.memsize
```

#### Datenspeicherverwendung
```sh
df -h
```

#### Netzwerkinformationen
```sh
ifconfig
```

#### Akkuinformationen (für Laptops)
```sh
pmset -g batt
```

#### Liste der installierten Software
```sh
ls /Applications
```

#### macOS-Version
```sh
sw_vers
```

#### Benutzerinformationen
```sh
id
```

#### Liste der ausgeführten Prozesse
```sh
ps aux
```

#### Liste der installierten Brew-Pakete
```sh
brew list
```

#### Liste der installierten Pip-Pakete
```sh
pip list
```

#### Liste der installierten Gem-Pakete
```sh
gem list
```

### 4. **Aktivitätsanzeige**
Diese App bietet Echtzeitinformationen über die CPU, den Arbeitsspeicher, den Energieverbrauch, die Datenspeicher- und Netzwerknutzung Ihres Mac.

- Öffnen Sie **Aktivitätsanzeige** über `Anwendungen` > `Dienstprogramme` > `Aktivitätsanzeige` oder durch Suchen in Spotlight.

### 5. **Festplattendienstprogramm**
Diese App bietet Informationen über Ihre Speichergeräte.

- Öffnen Sie **Festplattendienstprogramm** über `Anwendungen` > `Dienstprogramme` > `Festplattendienstprogramm` oder durch Suchen in Spotlight.

### 6. **Dritte Tools**
Es gibt auch Dritthersteller-Anwendungen wie **iStat Menus** und **CoconutBattery**, die detaillierte Systeminformationen und Überwachungsmöglichkeiten bieten.

Mit diesen Methoden können Sie eine Vielzahl von Systeminformationen auf Ihrem macOS abrufen.