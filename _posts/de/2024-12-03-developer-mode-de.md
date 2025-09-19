---
audio: false
generated: false
image: false
lang: de
layout: post
title: Entwicklermodus von iOS und ideviceinstaller
translated: true
---

## Entwicklermodus

Ich war früher für einige Zeit iOS-Entwickler. Mein Karrierefokus hat sich jedoch auf andere Technologien verlagert. Dennoch ist es immer noch sehr nützlich, iOS-Entwicklungskenntnisse anzuwenden, auch wenn ich kein professioneller iOS-Entwickler mehr bin.

Kürzlich wollte ich meine installierten Apps teilen. Wenn ich jedoch Screenshots aller Apps vom Home-Bildschirm oder aus der App-Liste in den Einstellungen gemacht hätte, wäre das unübersichtlich geworden. Also musste ich einen Weg finden, alle installierten Apps anzuzeigen.

Hier sind die Schritte, um alle installierten Apps mit Xcode anzuzeigen:

1. Verbinde dein iPhone über USB mit deinem Mac
2. Öffne Xcode
3. Gehe zu Fenster → Geräte und Simulatoren (oder drücke Shift + Cmd + 2)
4. Wähle dein iPhone aus der linken Seitenleiste
5. Scrolle im Hauptfenster nach unten zum Abschnitt „Installierte Apps“

Es gibt noch weitere nützliche Funktionen:

1. Screenshots erstellen
2. Letzte Logs öffnen
3. Konsole öffnen

## xcrun

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
Using verbose logging.
2024-12-03 16:24:18.579+0800  Enabling developer disk image services.
2024-12-03 16:24:18.637+0800  Acquired usage assertion.
Apps installed:
  - 0 elements

Command Completed, took 0.120 seconds
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

---

## Schnellwisch-Eingabe

*2024.12.01*

Wenn du in iOS „threads“ eingeben möchtest, musst du einfach schnell eine Linie ziehen, die die Positionen der Buchstaben von „threads“ abdeckt, um das Ergebnis zu erhalten. Lass uns sehen, wie das funktioniert.

<video width="50%" controls>
  <source src="/assets/images/input/in.mp4" type="video/mp4">
  Dein Browser unterstützt das Video-Tag nicht.
</video>

Ich habe das zufällig entdeckt. Wenn mein Finger schnell den Eingabebereich berührt, erscheint eine Linie. Ich wusste nicht, was das bedeutet. Nach einigen Experimenten habe ich die obige Entdeckung gemacht.