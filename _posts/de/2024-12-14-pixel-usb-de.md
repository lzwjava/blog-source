---
audio: false
generated: false
image: true
lang: de
layout: post
title: Pixel USB, iOS Entwicklertools, Wischtippen
translated: true
type: post
---

### Inhaltsverzeichnis

1. [USB-Optionen des Pixel](#pixels-usb-options)
   - Pixel als Webcam verwenden
   - Entwicklermodus in den Einstellungen aktivieren
   - USB-Debugging für die Verbindung aktivieren
   - Verbindung mit ADB-Befehl überprüfen

2. [Entwicklermodus von iOS und ideviceinstaller](#developer-mode-of-ios-and-ideviceinstaller)
   - Installierte Apps über Xcode anzeigen
   - Xcode für Screenshots und Protokolle verwenden
   - Apps mit dem xcrun-Befehl auflisten
   - ideviceinstaller-Tool installieren und verwenden

3. [Schnelles Wisch-Tippen](#quick-swipe-typing)
   - Wörter durch Wischen über die Buchstaben eingeben
   - Versehentlich entdeckte Funktion
   - Linie erscheint bei schneller Berührung


## USB-Optionen des Pixel

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/pixel/pixel.jpg" alt="Pixel" width="50%" />  
</div>

Pixel bietet verschiedene USB-Optionen, und eine besonders interessante Funktion ist die Möglichkeit, als Webcam zu fungieren. Unter macOS kann QuickTime auf die Android-Webcam als Videoquelle zugreifen, was eine einfache und effektive Lösung darstellt.

So richten Sie dies ein:  

1. Navigieren Sie zu den Einstellungen unter "Über das Telefon" und tippen Sie siebenmal auf die Build-Nummer, um den Entwicklermodus zu aktivieren.  
2. Öffnen Sie die Entwickleroptionen und aktivieren Sie USB-Debugging.  
3. Verbinden Sie Ihr Pixel über USB mit Ihrem Computer und führen Sie den folgenden Befehl in einem Terminal aus, um die Verbindung zu überprüfen:  
   ```bash
   adb devices
   ```

---

## Entwicklermodus von iOS und ideviceinstaller

*2024.12.03*

## Entwicklermodus

Ich war eine Zeit lang iOS-Entwickler. Aber mein beruflicher Schwerpunkt hat sich auf andere Technologien verlagert. Es ist jedoch immer noch sehr nützlich, iOS-Entwicklungswissen anzuwenden, auch wenn ich jetzt kein professioneller iOS-Entwickler bin.

Kürzlich wollte ich meine installierten Apps teilen. Aber wenn ich Screenshots aller Apps vom Startbildschirm oder aus der App-Liste in den Einstellungen gemacht hätte, wäre das ein Chaos gewesen. Also musste ich einen Weg finden, alle installierten Apps anzuzeigen.

Hier sind die Schritte, um alle installierten Apps mit Xcode anzuzeigen:

1. Verbinden Sie Ihr iPhone über USB mit Ihrem Mac
2. Öffnen Sie Xcode
3. Gehen Sie zu Fenster → Geräte und Simulatoren (oder drücken Sie Umschalt + Befehl + 2)
4. Wählen Sie Ihr iPhone in der linken Seitenleiste aus
5. Scrollen Sie im Hauptbereich zum Abschnitt "Installierte Apps"

Es hat weitere nützliche Funktionen:

1. Screenshots machen
2. Neueste Protokolle öffnen
3. Die Konsole öffnen

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

## Schnelles Wisch-Tippen

*2024.12.01*

Wenn Sie "threads" in iOS eingeben möchten, müssen Sie nur schnell eine Linie ziehen, um die Positionen der Buchstaben "threads" abzudecken, um das Ergebnis zu erhalten. Sehen wir uns an, wie es funktioniert.

<video width="50%" controls>
  <source src="/assets/images/input/in.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

Ich habe dies zufällig entdeckt. Wenn mein Finger schnell den Eingabebereich berührt, wird eine Linie angezeigt. Ich weiß nicht, was das bedeutet. Nach einigen Experimenten habe ich die obige Entdeckung gemacht.