---
audio: false
generated: true
lang: de
layout: post
title: Anschluss des iPad an einen HDMI-Monitor
translated: true
type: note
---

Um dein iPad über HDMI mit einem Monitor zu verbinden und damit Filme anzuschauen (z. B. gestreamt von deinem Nginx-Server auf dem Ubuntu-Laptop mit einer App wie Infuse), benötigst du den richtigen Adapter und ein einfaches Setup. iPads haben keinen nativen HDMI-Anschluss, aber Apple bietet offizielle Adapter an, und es gibt auch Drittanbieter-Optionen. Hier ist eine Schritt-für-Schritt-Anleitung, die auf dein Ziel zugeschnitten ist, Filme ohne Probleme auf deinem Monitor anzuschauen.

### Was du benötigst
1. **iPad mit Lightning- oder USB-C-Anschluss**
   - Überprüfe dein iPad-Modell: Ältere iPads (z. B. iPad Air 2, iPad Mini 4) verwenden Lightning-Anschlüsse, während neuere (z. B. iPad Pro 2018+, iPad Air 4. Gen+) USB-C verwenden.
   - Du hast dein iPad-Modell nicht angegeben, daher gehe ich auf beide Möglichkeiten ein.

2. **HDMI-Adapter**
   - Für **Lightning-iPads**: Apples **Lightning auf HDMI Adapter** (offiziell "Lightning Digital AV Adapter", ~49 USD).
   - Für **USB-C-iPads**: Apples **USB-C Digital AV Multiport Adapter** (~69 USD) oder einen USB-C auf HDMI Adapter eines Drittanbieters (stelle sicher, dass er Videoausgabe unterstützt, ~15-30 USD).
   - Adapter von Drittanbietern funktionieren, unterstützen aber möglicherweise nicht alle Funktionen (z. B. HDR oder hohe Bildwiederholraten); Apple-Adapter sind zuverlässiger für Plug-and-Play.

3. **HDMI-Kabel**
   - Ein beliebiges Standard-HDMI-Kabel (z. B. HDMI 2.0 für 4K, falls dein Monitor und iPad dies unterstützen). Die Länge hängt von deinem Setup ab – 5-10 Fuß sind typisch für Verbindungen in der Nähe.

4. **Monitor mit HDMI-Eingang**
   - Diesen hast du bereits, stelle also sicher, dass er eingeschaltet und auf den korrekten HDMI-Eingang eingestellt ist.

5. **Optional: Stromquelle**
   - Apples Adapter haben oft einen zusätzlichen Anschluss (Lightning oder USB-C) zum Laden. Wenn du lange Filme schaust, schließe dein iPad-Netzteil an, um es mit Strom zu versorgen.

### Schritte zum Verbinden deines iPads mit dem Monitor
1. **Besorge den richtigen Adapter**
   - Lightning-iPad: Stecke den Lightning Digital AV Adapter in den Lightning-Anschluss deines iPads.
   - USB-C-iPad: Stecke den USB-C Digital AV Multiport Adapter (oder einen USB-C auf HDMI Adapter) in den USB-C-Anschluss deines iPads.

2. **Schließe das HDMI-Kabel an**
   - Stecke ein Ende des HDMI-Kabels in den HDMI-Anschluss des Adapters.
   - Stecke das andere Ende in den HDMI-Eingangsanschluss deines Monitors.

3. **Stromversorgung anschließen (Optional)**
   - Für lange Sitzungen schließe dein iPad-Netzteil an den zusätzlichen Anschluss des Adapters (Lightning oder USB-C) an und stecke es in eine Steckdose. Dies verhindert das Entladen des Akkus.

4. **Monitor einschalten**
   - Schalte deinen Monitor ein und verwende seine Eingangs-/Quelltaste, um den HDMI-Port auszuwählen, den du verwendet hast (z. B. HDMI 1 oder HDMI 2).

5. **Bildschirmspiegelung des iPads**
   - Sobald verbunden, sollte der Bildschirm deines iPads automatisch auf den Monitor gespiegelt werden. Du siehst den Home-Bildschirm des iPads auf dem Monitor.
   - Wenn es nicht automatisch spiegelt:
     - Wische von der oberen rechten Ecke (auf iPads mit Face ID) oder von unten nach oben (auf älteren iPads mit Home-Taste), um die **Control Center** zu öffnen.
     - Tippe auf das **Bildschirmspiegelung**-Symbol (zwei überlappende Rechtecke).
     - Wähle den Adapter aus (er erscheint möglicherweise als "Apple AV Adapter" oder ähnlich). Die Spiegelung sollte beginnen.

6. **Anzeigeeinstellungen anpassen (Optional)**
   - Gehe auf deinem iPad zu **Einstellungen > Display & Helligkeit**.
     - Wenn der Monitor höhere Auflösungen unterstützt (z. B. 1080p oder 4K), passt das iPad dies automatisch an, aber du kannst hier Zoom oder Helligkeit anpassen.
     - Die meisten Inhalte (wie Filme) skalieren automatisch, um das Seitenverhältnis des Monitors zu füllen.

7. **Spiele deine Filme ab**
   - Öffne eine App wie **Infuse** (oder einen beliebigen Video-Player) auf deinem iPad.
   - Wenn du Infuse verwendest, um von deinem Ubuntu Nginx-Server zu streamen:
     - Konfiguriere Infuse so, dass es eine Verbindung zu deinem Server herstellt (z. B. `http://<laptop-ip>:80/movies`, wobei `<laptop-ip>` die IP deiner Ubuntu-Maschine ist, wie `192.168.1.100`).
     - Wähle einen Film aus, tippe auf Play, und er wird im Vollbildmodus auf dem Monitor angezeigt.
   - Drehe dein iPad in den Landscape-Modus oder tippe auf das Vollbild-Symbol in der App für die beste Betrachtungserfahrung.

### Überlegungen zur Audioausgabe
- **Monitor mit Lautsprechern**: Audio sollte über die Lautsprecher des Monitors via HDMI abgespielt werden (falls unterstützt).
- **Keine Monitor-Lautsprecher**: Verwende die Lautsprecher des iPads oder schließe kabelgebone Kopfhörer an den Lightning-/USB-C-Anschluss des Adapters an (möglicherweise ist ein Adapter für 3,5-mm-Klinkenstecker erforderlich) oder koppele Bluetooth-Kopfhörer mit dem iPad.

### Tipps für dein Setup
- **Unterstützte Auflösung**: Lightning-Adapter unterstützen bis zu 1080p; USB-C-Adapter unterstützen bis zu 4K (abhängig von deinem iPad und Monitor). Überprüfe die maximale Auflösung deines Monitors und die Qualität der Filmdateien.
- **Steuerung**: Du steuerst die Wiedergabe direkt auf dem Touchscreen des iPads. Da Infuse, wie bereits erwähnt, keine Fernsteuerung über das Netzwerk bietet, musst du mit dem iPad selbst interagieren – behalte es in der Nähe oder verwende einen Ständer.
- **Zugriff auf den Nginx-Server**: Stelle sicher, dass sich dein Ubuntu-Laptop und dein iPad im selben Wi-Fi-Netzwerk befinden. Teste den Nginx-Server, indem du auf dem iPad einen Browser öffnest und zu `http://<laptop-ip>` navigierst – du solltest deine Filmdateien sehen, wenn alles korrekt konfiguriert ist.

### Problembehebung
- **Kein Video**: Stelle sicher, dass alle Verbindungen sicher sind, der Monitor auf den richtigen Eingang eingestellt ist und der Adapter kompatibel ist (einige billige Adapter von Drittanbietern funktionieren nicht).
- **Ruckeln oder Stocken**: Wenn du von Nginx streamst, überprüfe die Stärke deines Wi-Fi-Signals oder die Größe der Filmdatei – große 4K-Dateien benötigen möglicherweise eine stärkere Verbindung.
- **Schwarze Balken**: Wenn der Film den Bildschirm nicht ausfüllt, liegt das an Unterschieden im Seitenverhältnis (z. B. 16:9 Film auf einem 4:3 Monitor). Verwende die Zoom-Optionen in Infuse, um dies anzupassen.

### Abschließende Gedanken
Dieses Setup ermöglicht es deinem iPad, als Wiedergabegerät zu fungieren, das von deinem Ubuntu-Laptop streamt und über HDMI auf den Monitor ausgibt. Es ist einfach, sobald alles verbunden ist – stecke es einfach ein, wähle deinen Film in Infuse aus und schaue zu. Da du minimalen Aufwand und keine zusätzlichen Geräte wie einen Fire TV Stick wolltest, nutzt dies dein vorhandenes iPad und deinen Monitor effektiv. Wenn dein iPad älter ist oder nicht genug Speicher für die Metadaten von Infuse hat, hält das direkte Streamen von Nginx alles schlank. Viel Spaß mit deinen Filmen!