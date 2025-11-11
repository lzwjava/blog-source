---
audio: false
generated: true
lang: de
layout: post
title: Streamen von MKV-Dateien von Nginx mit VLC
translated: true
type: note
---

Da Sie einen Nginx-Server haben, der `.mkv`-Dateien bereitstellt (z. B. unter `http://192.168.1.27/movies/`) und diese von einem Mac aus ansehen möchten, ohne die gesamte Datei herunterzuladen, möchten Sie die Videos **streamen**. Nginx kann Dateien so bereitstellen, dass HTTP-Range-Anfragen unterstützt werden (was standardmäßig der Fall ist), sodass Media Player streamen können, anstatt die Dateien vollständig herunterzuladen. So geht's, zusammen mit geeigneten Tools für macOS.

### Voraussetzungen
- Ihre Nginx-Konfiguration (z. B. `alias /var/www/movies/; autoindex on;`) funktioniert und `http://192.168.1.27/movies/` listet Dateien auf.
- Die `.mkv`-Dateien sind über das Netzwerk erreichbar (von einem anderen Rechner getestet).

### Tools zum Streamen von `.mkv`-Dateien auf macOS
Sie benötigen einen Media Player, der das Streamen über HTTP unterstützt und `.mkv`-Dateien gut verarbeitet. Hier sind die besten Optionen:

#### 1. VLC Media Player (Kostenlos, Empfohlen)
VLC ist ein vielseitiger, quelloffener Player, der das Streamen von `.mkv`-Dateien über HTTP unterstützt, ohne die gesamte Datei herunterzuladen (er verwendet Range-Anfragen).
- **Installation**:
  - Laden Sie ihn von [videolan.org](https://www.videolan.org/vlc/) herunter.
  - Installieren Sie ihn auf Ihrem Mac.
- **Streamen**:
  1. Öffnen Sie VLC.
  2. Drücken Sie `Cmd + N` (oder gehen Sie zu `Datei > Netzwerk öffnen`).
  3. Geben Sie die URL ein, z. B. `http://192.168.1.27/movies/ihredatei.mkv`.
  4. Klicken Sie auf `Öffnen`.
- **Warum es funktioniert**: VLC puffert nur das, was benötigt wird, und ermöglicht es Ihnen, vor- und zurückzuspulen, ohne die gesamte Datei herunterzuladen.

#### 2. IINA (Kostenlos, macOS-Nativ)
IINA ist ein moderner, macOS-spezifischer Player mit exzellenter `.mkv`-Unterstützung und Streaming-Fähigkeiten.
- **Installation**:
  - Laden Sie ihn von [iina.io](https://iina.io/) herunter oder verwenden Sie `brew install iina` (mit Homebrew).
- **Streamen**:
  1. Öffnen Sie IINA.
  2. Drücken Sie `Cmd + U` (oder `Datei > URL öffnen`).
  3. Geben Sie `http://192.168.1.27/movies/ihredatei.mkv` ein.
  4. Klicken Sie auf `OK`.
- **Warum es funktioniert**: Leichtgewichtig, unterstützt HTTP-Streaming und integriert sich gut mit macOS.

#### 3. QuickTime Player (Integriert, Eingeschränkt)
Der Standard-QuickTime Player von macOS kann einige Formate streamen, aber die `.mkv`-Unterstützung ist ohne zusätzliche Codecs lückenhaft.
- **Versuch**:
  1. Öffnen Sie QuickTime Player.
  2. Drücken Sie `Cmd + U` (oder `Datei > Ort öffnen`).
  3. Geben Sie `http://192.168.1.27/movies/ihredatei.mkv` ein.
  4. Klicken Sie auf `Öffnen`.
- **Einschränkung**: Wenn es nicht funktioniert, installieren Sie Perian (ein alter Codec-Pack) oder verwenden Sie stattdessen VLC/IINA.

#### 4. Browser (Safari/Chrome, Einfachste Methode)
Moderne Browser können `.mkv`-Dateien direkt streamen, wenn sie mit unterstützten Codecs kodiert sind (z. B. H.264-Video, AAC-Audio).
- **Vorgehen**:
  1. Öffnen Sie Safari oder Chrome auf Ihrem Mac.
  2. Gehen Sie zu `http://192.168.1.27/movies/`.
  3. Klicken Sie auf `ihredatei.mkv`.
- **Warum es funktioniert**: Browser verwenden HTML5-Video-Tags und Range-Anfragen zum Streamen.
- **Einschränkung**: Wenn die `.mkv` nicht unterstützte Codecs verwendet (z. B. VP9, Opus), wird sie nicht abgespielt – wechseln Sie zu VLC oder IINA.

### Sicherstellen, dass Nginx Streaming unterstützt
Nginx verarbeitet Range-Anfragen standardmäßig, was das Streaming ermöglicht. Zur Bestätigung:
- Stellen Sie sicher, dass Ihre Konfiguration dies nicht deaktiviert (z. B. kein `limit_rate` oder benutzerdefinierte Header, die Range-Anfragen blockieren).
- Testen Sie mit VLC oder IINA – wenn Sie suchen können (z. B. zu 5 Minuten springen), funktioniert das Streaming.

### Empfohlener Arbeitsablauf
1. **Verwenden Sie VLC** (am zuverlässigsten):
   - Installieren Sie VLC.
   - Öffnen Sie `http://192.168.1.27/movies/ihredatei.mkv` über `Cmd + N`.
   - Spielen Sie ab, pausieren Sie oder suchen Sie wie benötigt.
2. **Verzeichnis-Durchsuchen**:
   - Besuchen Sie `http://192.168.1.27/movies/` in Safari/Chrome, um die Dateiliste zu sehen (dank `autoindex on;`).
   - Kopieren Sie die URL von `ihredatei.mkv` und fügen Sie sie in VLC oder IINA ein.

### Fehlerbehebung
- **Pufferungsprobleme**: Ein langsames Netzwerk oder große `.mkv`-Dateien können zu Verzögerungen führen – stellen Sie sicher, dass Ihr LAN stabil ist (z. B. dass die Wi-Fi-Verbindung nicht abbricht).
- **Codec-Fehler**: Wenn VLC "nicht unterstütztes Format" meldet, verwendet die `.mkv` möglicherweise seltene Codecs – versuchen Sie, sie mit HandBrake in H.264/AAC neu zu kodieren.
- **Verbindung abgelehnt**: Überprüfen Sie die Firewall-Einstellungen auf dem Server (`sudo ufw allow 80` oder Äquivalent).

Mit VLC oder IINA streamen Sie Ihre `.mkv`-Dateien im Handumdrehen von Ihrem Mac, ohne sie vollständig herunterzuladen. Lassen Sie es mich wissen, wenn Sie auf Probleme stoßen!

---

Die Installation von VLC auf einem Mac ist unkompliziert. Hier ist eine kurze Anleitung, um ihn einzurichten, damit Sie Ihre `.mkv`-Dateien von Ihrem Nginx-Server streamen können:

### Methode 1: Download von der offiziellen Website
1. **Besuchen Sie die VLC-Website**:
   - Öffnen Sie Ihren Browser (z. B. Safari oder Chrome).
   - Gehen Sie zu [https://www.videolan.org/vlc/](https://www.videolan.org/vlc/).

2. **VLC herunterladen**:
   - Klicken Sie auf den Button **Download VLC**. Er sollte Ihr macOS automatisch erkennen und die richtige Version anbieten (z. B. VLC 3.0.20 zum jetzigen Zeitpunkt).
   - Sie erhalten eine `.dmg`-Datei (z. B. `vlc-3.0.20.dmg`).

3. **VLC installieren**:
   - Öffnen Sie die heruntergeladene `.dmg`-Datei (normalerweise in Ihrem `Downloads`-Ordner).
   - Ziehen Sie das VLC-Symbol wie im Fenster angezeigt in den Ordner **Programme**.
   - Schließen Sie das `.dmg`-Fenster und hängen Sie es aus (Rechtsklick auf das Laufwerkssymbol auf Ihrem Desktop oder im Finder und "Auswerfen" wählen).

4. **VLC ausführen**:
   - Gehen Sie zu Ihrem Ordner **Programme** (z. B. über Finder oder Spotlight mit `Cmd + Leertaste`, dann "Programme" eingeben).
   - Doppelklicken Sie auf **VLC**.
   - Falls macOS es blockiert ("nicht identifizierter Entwickler"), machen Sie einen Rechtsklick auf VLC, wählen Sie **Öffnen** und klicken Sie dann im Dialogfeld auf **Öffnen**.

5. **Ihre Datei streamen**:
   - Öffnen Sie VLC.
   - Drücken Sie `Cmd + N` (oder `Datei > Netzwerk öffnen`).
   - Geben Sie `http://192.168.1.27/movies/ihredatei.mkv` ein.
   - Klicken Sie auf **Öffnen**.

### Methode 2: Installation über Homebrew (Terminal)
Wenn Sie die Kommandozeile bevorzugen und Homebrew installiert haben:
1. **Homebrew installieren** (falls noch nicht geschehen):
   - Öffnen Sie Terminal.
   - Führen Sie aus:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Folgen Sie den Anweisungen.

2. **VLC installieren**:
   - Im Terminal:
     ```bash
     brew install vlc
     ```

3. **VLC ausführen**:
   - Starten Sie ihn vom Terminal mit:
     ```bash
     open -a VLC
     ```
   - Oder finden Sie ihn in **Programme** als `VLC.app`.

4. **Streamen**:
   - Wie oben: `Cmd + N`, geben Sie Ihre URL ein und spielen Sie ab.

### Installation überprüfen
- Sobald installiert, sollte VLC in Ihrem Ordner **Programme** erscheinen.
- Testen Sie ihn zuerst mit einer lokalen Datei (ziehen Sie eine `.mkv` in VLC), um sicherzustellen, dass er funktioniert, und versuchen Sie dann, `http://192.168.1.27/movies/ihredatei.mkv` zu streamen.

### Fehlerbehebung
- **Download schlägt fehl**: Verwenden Sie einen Mirror-Link von der VLC-Website, falls der Hauptdownload langsam ist.
- **Sicherheitsabfrage**: Falls macOS es blockiert, gehen Sie zu `Systemeinstellungen > Sicherheit & Datenschutz > Allgemein` und klicken Sie auf **Trotzdem öffnen**.
- **Spielt nicht ab**: Stellen Sie sicher, dass die URL korrekt ist und Ihr Server erreichbar ist (`ping 192.168.1.27` im Terminal).

Das war's! VLC sollte jetzt auf Ihrem Mac bereit sein, um Ihre `.mkv`-Dateien zu streamen. Lassen Sie es mich wissen, wenn Sie Hilfe mit dem nächsten Schritt benötigen!