---
audio: false
generated: true
lang: de
layout: post
title: Streamen von MKV-Dateien auf dem iPad mit VLC Mobile und anderen Apps
translated: true
type: note
---

Um Ihre `.mkv`-Dateien von Ihrem Nginx-Server (z.B. `http://192.168.1.27/movies/`) auf Ihrem iPad zu streamen, ohne sie vollständig herunterzuladen, benötigen Sie eine App, die HTTP-Streaming und `.mkv`-Wiedergabe unterstützt. iPadOS kann `.mkv`-Dateien nicht nativ in Safari oder der Dateien-App gut verarbeiten, daher ist ein Media-Player eines Drittanbieters der richtige Weg. So erreichen Sie diesen "Zauber" auf Ihrem iPad:

### Empfohlene Apps zum Streamen von `.mkv` auf dem iPad
#### 1. VLC for Mobile (Kostenlos, Beste Option)
VLC ist auf iPadOS verfügbar und funktioniert ähnlich wie die Mac-Version, mit Unterstützung für HTTP-Streaming mit Bereichsanfragen (Range Requests).
- **Installation**:
  1. Öffnen Sie den **App Store** auf Ihrem iPad.
  2. Suchen Sie nach **VLC for Mobile**.
  3. Tippen Sie auf **Holen** (oder das Cloud-Symbol, falls Sie es bereits installiert hatten) und authentifizieren Sie sich gegebenenfalls mit Ihrer Apple ID.
- **Streamen**:
  1. Öffnen Sie die **VLC**-App.
  2. Tippen Sie auf den **Netzwerk**-Tab (Kegel-Symbol) unten.
  3. Wählen Sie **Netzwerkstream öffnen**.
  4. Geben Sie `http://192.168.1.27/movies/ihredatei.mkv` ein.
  5. Tippen Sie auf **Netzwerkstream öffnen** (oder das Play-Symbol).
- **Warum es funktioniert**: VLC puffert den Stream, sodass Sie abspielen und suchen können, ohne die gesamte Datei herunterzuladen.

#### 2. nPlayer (Kostenpflichtig, Premium-Option)
nPlayer ist ein leistungsstarker Media-Player mit exzellenter `.mkv`-Unterstützung und Streaming-Fähigkeiten.
- **Installation**:
  1. Öffnen Sie den **App Store**.
  2. Suchen Sie nach **nPlayer** (kostet ca. 8,99 $, es gibt aber auch eine kostenlose Lite-Version mit Werbung).
  3. Tippen Sie auf **Holen** oder **Kaufen** und installieren Sie die App.
- **Streamen**:
  1. Öffnen Sie **nPlayer**.
  2. Tippen Sie auf das **+** Symbol oder die **Netzwerk**-Option.
  3. Wählen Sie **URL hinzufügen** oder **HTTP/HTTPS**.
  4. Geben Sie `http://192.168.1.27/movies/ihredatei.mkv` ein.
  5. Tippen Sie auf **Abspielen**.
- **Warum es funktioniert**: Unterstützt erweiterte Codecs und smooth Streaming; großartige Benutzeroberfläche für das iPad.

#### 3. Infuse (Kostenlos mit In-App-Käufen)
Infuse ist eine weitere beliebte Wahl zum Streamen und Abspielen von `.mkv`-Dateien, mit einer eleganten Oberfläche.
- **Installation**:
  1. Öffnen Sie den **App Store**.
  2. Suchen Sie nach **Infuse**.
  3. Tippen Sie auf **Holen** (die kostenlose Stufe reicht für grundlegendes Streaming; das Pro-Upgrade ist optional).
- **Streamen**:
  1. Öffnen Sie **Infuse**.
  2. Tippen Sie auf **Dateien hinzufügen** > **Über URL**.
  3. Geben Sie `http://192.168.1.27/movies/ihredatei.mkv` ein.
  4. Tippen Sie auf **Hinzufügen** oder **Abspielen**.
- **Warum es funktioniert**: Streamt über HTTP und verarbeitet `.mkv` gut; Pro-Funktionen (wie AirPlay) sind optional.

### Schritte für den Anfang
1. **Verbinden Sie sich mit demselben Netzwerk**:
   - Stellen Sie sicher, dass sich Ihr iPad im selben Wi-Fi-Netzwerk wie Ihr Nginx-Server befindet (z.B. `192.168.1.x`).
   - Testen Sie die Konnektivität: Öffnen Sie Safari auf Ihrem iPad und gehen Sie zu `http://192.168.1.27/movies/`. Sie sollten die Dateiliste sehen (auch wenn Safari `.mkv` nicht abspielen kann).

2. **Wählen Sie eine App**:
   - **VLC** ist kostenlos und zuverlässig – fangen Sie hier an.
   - Installieren Sie es wie beschrieben aus dem App Store.

3. **Geben Sie die URL ein**:
   - Verwenden Sie die exakte URL Ihrer `.mkv`-Datei (z.B. `http://192.168.1.27/movies/ihredatei.mkv`).
   - Sie können den Link aus der Dateiliste in Safari kopieren und in die App einfügen.

4. **Spielen Sie ab und genießen Sie**:
   - Die App streamt das Video. Sie können pausieren, suchen oder die Wiedergabe anpassen, ohne die gesamte Datei herunterzuladen.

### Problembehandlung
- **Verbindung schlägt fehl**: Wenn das iPad `192.168.1.27` nicht erreichen kann, stellen Sie sicher, dass die Firewall des Servers Port 80 erlaubt (`sudo ufw allow 80`) und das iPad im selben LAN ist.
- **Buffering**: Langsames Wi-Fi kann zu Verzögerungen führen – bewegen Sie sich näher an den Router oder überprüfen Sie Ihre Netzwerkgeschwindigkeit.
- **Codec-Probleme**: Wenn die `.mkv`-Datei nicht abgespielt wird, verwendet sie möglicherweise einen nicht unterstützten Codec (z.B. VP9). VLC handelt die meisten ab, aber Sie könnten sie mit HandBrake zu H.264/AAC für breitere Kompatibilität neu enkodieren.
- **URL-Tippfehler**: Überprüfen Sie die IP und den Pfad – `http://192.168.1.27/movies/ihredatei.mkv` muss Ihrer Einrichtung entsprechen.

### Bonus: Durchsuchen und Auswählen
Da `autoindex on;` Ihnen eine Verzeichnisliste gibt:
- Öffnen Sie Safari auf Ihrem iPad, gehen Sie zu `http://192.168.1.27/movies/`, tippen Sie auf einen Dateilink und kopieren Sie dann die URL.
- Fügen Sie sie in VLC/nPlayer/Infuse zum Streamen ein.

Mit **VLC for Mobile** haben Sie diesen "Zauber" auf Ihrem iPad im Handumdrehen – und streamen Ihre `.mkv`-Dateien mühelos! Lassen Sie es mich wissen, wenn Sie Hilfe bei der Einrichtung benötigen.