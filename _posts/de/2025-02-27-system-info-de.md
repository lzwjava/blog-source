---
audio: true
generated: false
lang: de
layout: post
title: Systeminformationen auf macOS
translated: true
---

Um Systeminformationen auf Ihrem macOS zu erhalten, können Sie mehrere integrierte Tools und Befehle verwenden. Hier sind einige Methoden, um verschiedene Arten von Systeminformationen abzurufen:

### 1. **Systeminformationen-App**
Die Systeminformationen-App bietet eine umfassende Übersicht über die Hardware und Software Ihres Mac.

- Öffnen Sie die **Spotlight-Suche** durch Drücken von `Cmd + Space` und geben Sie "Systeminformationen" ein, dann drücken Sie Enter.
- Alternativ können Sie sie über das **Apple-Menü** > **Über diesen Mac** > **Systembericht** öffnen.

### 2. **Über diesen Mac**
Dies bietet eine schnelle Übersicht über die Spezifikationen Ihres Mac.

- Klicken Sie auf das **Apple-Menü** in der oberen linken Ecke des Bildschirms.
- Wählen Sie **Über diesen Mac**. Dies zeigt grundlegende Informationen wie die macOS-Version, den Prozessor, den Speicher und die Seriennummer an.

### 3. **Terminal-Befehle**
Sie können das Terminal verwenden, um detaillierte Systeminformationen mit verschiedenen Befehlen zu erhalten.

- Öffnen Sie **Terminal** über `Programme` > `Dienstprogramme` > `Terminal` oder indem Sie danach in Spotlight suchen.

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

#### Speicherinformationen
```sh
sysctl hw.memsize
```

#### Festplattenbelegung
```sh
df -h
```

#### Netzwerkinformationen
```sh
ifconfig
```

#### Batterieinformationen (für Laptops)
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

#### Liste der laufenden Prozesse
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
Diese App bietet Echtzeitinformationen über die CPU, den Speicher, die Energie, die Festplatte und die Netzwerkauslastung Ihres Mac.

- Öffnen Sie die **Aktivitätsanzeige** über `Programme` > `Dienstprogramme` > `Aktivitätsanzeige` oder indem Sie danach in Spotlight suchen.

### 5. **Festplattendienstprogramm**
Diese App bietet Informationen über Ihre Speichergeräte.

- Öffnen Sie das **Festplattendienstprogramm** über `Programme` > `Dienstprogramme` > `Festplattendienstprogramm` oder indem Sie danach in Spotlight suchen.

### 6. **Drittanbieter-Tools**
Es gibt auch Drittanbieter-Anwendungen wie **iStat Menüs** und **CoconutBattery**, die detaillierte Systeminformationen und Überwachungsfunktionen bieten.

Mit diesen Methoden können Sie eine breite Palette von Systeminformationen auf Ihrem macOS sammeln.