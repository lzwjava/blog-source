---
audio: false
generated: false
image: false
lang: de
layout: post
title: Einrichtung eines Live-Streams mit OBS, SRS und FFmpeg
translated: true
---

*Dieser Blogbeitrag wurde mit Unterstützung von ChatGPT-4o verfasst.*

---

Livestreaming ist zu einem wesentlichen Bestandteil der Online-Kommunikation geworden, mit breiten Anwendungsmöglichkeiten von professionellen Sendungen bis hin zu persönlichen Video-Blogs. Die Einrichtung einer robusten Livestreaming-Lösung erfordert ein Verständnis verschiedener Tools und Protokolle. Diese Anleitung führt Sie Schritt für Schritt durch die Einrichtung eines Livestreams mit OBS, SRS und FFmpeg.

### Schlüsselkomponenten eines Livestreams

**1. OBS（Open Broadcaster Software）**
OBS ist eine leistungsstarke Open-Source-Software für Videoaufnahmen und Live-Streaming. Es bietet Funktionen wie Echtzeit-Quellen- und Geräteerfassung, Szenenzusammensetzung, Kodierung, Aufnahme und Übertragung.

**2. SRS（Simple Realtime Server）**
SRS ist ein leistungsstarker RTMP-, HLS- und HTTP-FLV-Streaming-Server. Es unterstützt eine große Anzahl gleichzeitiger Verbindungen und ist hochgradig konfigurierbar.

**3. FFmpeg**
FFmpeg ist ein umfassendes Multimedia-Framework, das in der Lage ist, nahezu alles, was von Menschen und Maschinen erstellt wurde, zu decodieren, encodieren, transkodieren, multiplexen, demultiplexen, streamen, filtern und abzuspielen. Es wird in Streaming-Setups weit verbreitet eingesetzt und wird aufgrund seiner Vielseitigkeit und Zuverlässigkeit hoch geschätzt.

### Einrichten Ihrer Live-Streaming-Umgebung

#### OBS-Konfiguration

1. **Installieren Sie OBS**: Laden Sie OBS von der offiziellen Website herunter und installieren Sie es.
2. **Konfigurieren Sie die Einstellungen**: Öffnen Sie OBS und gehen Sie zu `Einstellungen > Stream`. Konfigurieren Sie den Stream-Typ als `Benutzerdefiniert...`. Geben Sie Ihre Streaming-Server-URL ein (z.B. `rtmp://your_server_ip/live`).
3. **Quellen hinzufügen**: Fügen Sie in OBS Video- und Audioquellen hinzu, um eine Szene zu erstellen. Dies kann Bildschirmaufnahme, Kamera, Bilder, Text usw. umfassen.

#### SRS Server-Einrichtung

1. **Installation von SRS**: Klonen Sie das SRS-Repository von GitHub und kompilieren Sie es, um SSL zu unterstützen.
    ```sh
    git clone https://github.com/ossrs/srs.git
    cd srs/trunk
    ./configure --disable-all --with-ssl
    make
    ```
2. **Konfiguration von SRS**: Bearbeiten Sie die Datei `conf/rtmp.conf`, um Ihre RTMP-Einstellungen zu konfigurieren.
    ```sh
    listen 1935;
    max_connections 1000;
    vhost __defaultVhost__ { }
    ```
3. **Starten von SRS**: Führen Sie den SRS-Server mit Ihrer Konfigurationsdatei aus.
    ```sh
    ./objs/srs -c conf/rtmp.conf
    ```

#### Streaming mit FFmpeg

1. **Installation von FFmpeg**: Installieren Sie FFmpeg von der offiziellen Website oder über einen Paketmanager.
2. **Verwendung von FFmpeg für das Streaming**: Verwenden Sie FFmpeg, um den Video-Stream an Ihren SRS-Server zu senden.
    ```sh
    ffmpeg -re -i input_video.flv -vcodec copy -acodec copy -f flv rtmp://your_server_ip/live/stream_key
    ```
3. **Automatisierung des Streamings**: Erstellen Sie ein Skript, um Video-Dateien kontinuierlich zu streamen.
    ```sh
    for ((;;)); do 
        ffmpeg -re -i input_video.flv -vcodec copy -acodec copy -f flv rtmp://your_server_ip/live/stream_key;
        sleep 1;
    done
    ```

### Protokolle und Formate

**RTMP (Real-Time Messaging Protocol)**
- RTMP wird aufgrund seiner geringen Latenz und zuverlässigen Übertragung häufig für Live-Streaming verwendet.
- Es verwendet TCP, kann dauerhafte Verbindungen aufrechterhalten und sorgt so für einen reibungslosen Streaming-Vorgang.

**HLS (HTTP Live Streaming)**
- HLS unterteilt den Video-Stream in kleine, auf HTTP basierende Dateisegmente, was die Übertragung über Standard-Webserver erleichtert.
- Obwohl es eine gewisse Latenz einführt, ist es hochgradig kompatibel mit verschiedenen Geräten und Plattformen.

**HTTP-FLV**
- Kombiniert das FLV-Format mit der HTTP-Übertragung für die Streaming-Übertragung mit geringer Latenz.
- Geeignet für browserbasiertes Streaming, da es die bestehende HTTP-Infrastruktur nutzt.

### Praktische Anwendungen

**iOS- und Android-Streaming**
- Implementierung von RTMP-Streaming auf mobilen Geräten mithilfe von Bibliotheken wie VideoCore und Ijkplayer.
- Integration von FFmpeg für Kodierungs- und Dekodierungsaufgaben, um Kompatibilität und Leistung zu verbessern.

**Web-basiertes Streaming**
- Implementierung der Videowiedergabe auf Webseiten mithilfe des HTML5-Videoelements, unterstützt HLS oder HTTP-FLV.
- Nutzung von WebRTC für Echtzeitkommunikation und Interaktion mit geringer Latenz.

### Werkzeuge und Ressourcen

- **VLC**: Ein vielseitiger Medienplayer, der Streaming-Protokolle wie RTMP und HLS unterstützt.
- **SRS Player**: Ein Online-Player zum Testen von SRS-Streams.
- **FFmpeg-Dokumentation**: Bietet detaillierte Dokumentation für verschiedene Multimedia-Aufgaben.

### Fazit

Ein zuverlässiges Live-Streaming-System zu erstellen, erfordert das Verständnis und die Konfiguration verschiedener Tools und Protokolle. OBS, SRS und FFmpeg sind leistungsstarke Komponenten, die in Kombination eine robuste Streaming-Infrastruktur bilden können. Egal, ob für iOS, Android oder das Web, diese Tools bieten die Flexibilität und Leistung, die für hochwertige Live-Streams erforderlich sind.

Weitere detaillierte Informationen und erweiterte Konfigurationen finden Sie in der offiziellen Dokumentation jedes Tools. Entdecken Sie außerdem weitere Tipps und Unterstützung in den Community-Foren. Viel Erfolg bei Ihrem Live-Streaming!