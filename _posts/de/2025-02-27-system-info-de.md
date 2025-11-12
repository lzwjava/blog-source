---
audio: false
generated: true
lang: de
layout: post
title: Systeminformationen unter macOS
translated: true
type: note
---

Um Systeminformationen auf Ihrem macOS zu erhalten, können Sie verschiedene integrierte Tools und Befehle verwenden. Hier sind einige Methoden, um verschiedene Arten von Systeminformationen abzurufen:

### 1. **Systeminformationen-Dienstprogramm**
Die App "Systeminformationen" bietet einen umfassenden Überblick über die Hardware und Software Ihres Mac.

- Öffnen Sie die **Spotlight-Suche** durch Drücken von `Cmd + Leertaste` und geben Sie "Systeminformationen" ein, dann drücken Sie die Eingabetaste.
- Alternativ können Sie sie über das **Apple-Menü** > **Über diesen Mac** > **Systembericht** öffnen.

### 2. **Über diesen Mac**
Dies bietet einen schnellen Überblick über die Spezifikationen Ihres Mac.

- Klicken Sie auf das **Apple-Menü** in der linken oberen Ecke des Bildschirms.
- Wählen Sie **Über diesen Mac**. Dies zeigt grundlegende Informationen wie die macOS-Version, Prozessor, Speicher und Seriennummer an.

### 3. **Terminal-Befehle**
Sie können das Terminal verwenden, um detaillierte Systeminformationen mit verschiedenen Befehlen zu erhalten.

- Öffnen Sie das **Terminal** unter `Programme` > `Dienstprogramme` > `Terminal` oder indem Sie es in der Spotlight-Suche suchen.

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

#### Datenträgernutzung
```sh
df -h
```

#### Netzwerkinformationen
```sh
ifconfig
```

#### Akku-Informationen (für Laptops)
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

### 4. **Aktivitätsmonitor**
Diese App bietet Echtzeitinformationen über die CPU-, Speicher-, Energie-, Datenträger- und Netzwerknutzung Ihres Mac.

- Öffnen Sie den **Aktivitätsmonitor** unter `Programme` > `Dienstprogramme` > `Aktivitätsmonitor` oder indem Sie ihn in der Spotlight-Suche suchen.

### 5. **Festplatten-Dienstprogramm**
Diese App bietet Informationen über Ihre Speichergeräte.

- Öffnen Sie das **Festplatten-Dienstprogramm** unter `Programme` > `Dienstprogramme` > `Festplatten-Dienstprogramm` oder indem Sie es in der Spotlight-Suche suchen.

### 6. **Tools von Drittanbietern**
Es gibt auch Anwendungen von Drittanbietern wie **iStat Menus** und **CoconutBattery**, die detaillierte Systeminformationen und Überwachungsfunktionen bieten.

Durch die Verwendung dieser Methoden können Sie eine Vielzahl von Systeminformationen auf Ihrem macOS sammeln.