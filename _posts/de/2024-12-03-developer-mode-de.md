---
audio: false
generated: false
lang: de
layout: post
title: Entwicklermodus von iOS und ideviceinstaller
translated: true
---

## Entwicklermodus

Ich war eine Zeit lang iOS-Entwickler. Aber mein Karriereschwerpunkt hat sich auf andere Technologien verlagert. Dennoch ist es sehr nützlich, das Wissen über iOS-Entwicklung anzuwenden, auch wenn ich jetzt kein professioneller iOS-Entwickler mehr bin.

Kürzlich wollte ich meine installierten Apps teilen. Aber wenn ich Screenshots aller Apps vom Home-Bildschirm oder aus der App-Liste in den Einstellungen machen würde, wäre das ein Chaos. Also musste ich einen Weg finden, um alle installierten Apps anzuzeigen.

Hier sind die Schritte, um alle installierten Apps mit Xcode anzuzeigen:

1. Verbinde dein iPhone über USB mit deinem Mac
2. Öffne Xcode
3. Gehe zu Window → Devices and Simulators (oder drücke Shift + Cmd + 2)
4. Wähle dein iPhone aus der linken Seitenleiste aus
5. Scrolle im Hauptbereich nach unten zum Abschnitt "Installed Apps"

Es verfügt über weitere nützliche Funktionen:

1. Screenshots erstellen
2. Kürzliche Protokolle öffnen
3. Die Konsole öffnen

## xcrun

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
Verwende ausführliche Protokollierung.
2024-12-03 16:24:18.579+0800  Aktiviere Developer-Disk-Image-Dienste.
2024-12-03 16:24:18.637+0800  Nutzungsbestätigung erworben.
Installierte Apps:
  - 0 Elemente
```

Befehl abgeschlossen, dauerte 0,120 Sekunden
```

## ideviceinstaller

```bash
brew install ideviceinstaller
ideviceinstaller -l
```

```bash
(base) lzwjava@192 Downloads % ideviceinstaller -l
CFBundleIdentifier, CFBundleVersion, CFBundleDisplayName
com.huawei.smarthome-ios, "14.1.1.325", "HUAWEI AI Life"
com.sf-express.waybillcn, "9.70.0.1", "顺丰速运"
com.roblox.robloxmobile, "2.652.762", "Roblox"
co.alphaexploration.clubhouse, "3273", "Clubhouse"
com.dbs.mbanking.cn, "11", "DBS digibank"
global.longbridge.ios, "59579", "Longbridge"
imgurmobile, "416", "Imgur"
com.creditkarma.mobile, "17316145", "Credit Karma"
...
```