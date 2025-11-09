---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Überwachung des Router-Netzwerkverkehrs
translated: true
type: note
---

### Überwachung von HTTP-Anfragen und TCP-Verbindungen am 360 Wi-Fi 6 Router T7

Der 360 T7 läuft auf einer angepassten Linux-basierten Firmware (nicht vollständig OpenWrt ab Werk), daher sind die Überwachungsmöglichkeiten im Standard-Setup im Vergleich zu einer vollwertigen Linux-Shell eingeschränkt. Mit Administratorrechten (über die Web-Oberfläche) können Sie auf grundlegende Protokolle zugreifen. Für tiefergehendes "Hacking", wie z.B. die Echtzeit-Protokollierung von HTTP-Anfragen oder die Verfolgung von TCP-Verbindungen, ist der beste ethische Ansatz das Flashen von OpenWrt (das offiziell unterstützt wird), das Aktivieren von SSH und die Verwendung standardmäßiger Linux-Tools. **Warnung: Das Flashen von Custom-Firmware macht die Garantie ungültig und birgt das Risiko, das Gerät zu beschädigen (Brick) – sichern Sie zuerst Ihre Daten und befolgen Sie Anleitungen sorgfältig. Führen Sie dies nur an Ihrem eigenen Gerät durch.**

#### 1. **Administratorrechte auf der Standard-Firmware erhalten**
   - Verbinden Sie sich mit dem WLAN des Routers oder per Ethernet.
   - Öffnen Sie einen Browser und gehen Sie zu `http://ihome.360.cn` oder `http://192.168.0.1` (Standard-IP).
   - Anmeldung: Standardbenutzername `admin`, Passwort steht auf dem Aufkleber am Router (oft `admin` oder ein eindeutiger String wie `360XXXXXX` – prüfen Sie den Aufkleber auf der Unterseite).
   - Navigieren Sie nach der Anmeldung zu **System > Protokoll** oder **Sicherheit > Protokoll** für grundlegende System- und Verkehrsprotokolle. Dies zeigt Firewall-Blocks, Verbindungen und einige HTTP-Aktivitäten an (z.B. blockierte Seiten oder Eindringversuche), aber keine vollständigen HTTP-Anfragedetails.

   **Grundlegende Überwachung über die Web-Oberfläche:**
   - **Systemprotokolle**: Zeigen Sie kürzliche Ereignisse an, einschließlich TCP-Verbindungsversuchen und Fehlern. Exportieren Sie Protokolle (erfordert möglicherweise das Passwort vom Aufkleber zur Entschlüsselung).
   - **Verkehrsstatistiken**: Unter **Status > Netzwerk** oder **Erweitert > Verkehrsmonitor** sehen Sie die Bandbreitennutzung pro Gerät/IP, aber keine detaillierten HTTP/TCP-Daten.
   - Einschränkungen: Keine Echtzeit-Inspektion von HTTP-Paketinhalten; Protokolle sind allgemein gehalten und nicht ohne Authentifizierung exportierbar.

#### 2. **Erweiterte Überwachung: OpenWrt flashen für Shell-Zugriff**
   Der 360 T7 (MT7981B Chipsatz) wird in OpenWrt 23.05+ Snapshots unterstützt. Das Flashen ermöglicht vollen Root-Shell-Zugriff über SSH, wo Sie Tools wie `tcpdump` für Paketaufnahmen und `logread` für Protokolle verwenden können.

   **Schritte zum Flashen von OpenWrt (Überblick; Verwenden Sie die offizielle Anleitung):**
   1. Laden Sie das Factory-Image von den OpenWrt-Downloads herunter (suchen Sie nach "Qihoo 360T7 sysupgrade.bin" oder Factory-Image).
   2. Sichern Sie die Standard-Firmware: Gehen Sie in der Web-Oberfläche zu **System > Backup** und laden Sie die Konfiguration/Firmware herunter.
   3. Hochladen über die Web-Oberfläche: **System > Firmware-Upgrade**, wählen Sie die .bin-Datei aus und wenden Sie sie an (der Router startet neu in OpenWrt).
   4. Nach dem Flashen: Zugriff auf die Web-Oberfläche unter `http://192.168.1.1` (LuCI-Oberfläche), Benutzername `root`, zunächst kein Passwort – setzen Sie sofort eines über SSH oder die Oberfläche.
   5. SSH aktivieren: Es ist standardmäßig auf Port 22 aktiviert. Verbinden Sie sich von Ihrem PC: `ssh root@192.168.1.1` (verwenden Sie PuTTY unter Windows).

   **Risikominderung**: Bei Problemen verwenden Sie die TFTP-Wiederherstellung (Reset-Taste während des Bootens gedrückt halten) oder die serielle Konsole (erfordert UART-Adapter).

#### 3. **Überwachung auf OpenWrt (über SSH-Shell)**
   Sobald Sie per SSH als root angemeldet sind, verhält sich der Router wie ein minimales Linux-System. Installieren Sie bei Bedarf Pakete über `opkg update && opkg install tcpdump` (der eingebaute Speicher beträgt 128MB, halten Sie es also leicht).

   - **Alle aktuellen TCP-Verbindungen auflisten (Statische Ansicht):**
     ```
     ss -tunap
     ```
     - Zeigt etablierte/lauschende TCP-Sockets, Ports, Prozesse (z.B. `tcp ESTAB 0 0 192.168.1.1:80 192.168.1.100:54321 users:(("uhttpd",pid=1234,fd=3))`).
     - Für Echtzeit: `watch -n 1 'ss -tunap'`.

   - **Echtzeit-TCP-Verkehrsaufnahme:**
     Installieren Sie falls nötig: `opkg update && opkg install tcpdump`.
     ```
     tcpdump -i any tcp -n -v
     ```
     - `-i any`: Alle Schnittstellen (br-lan für LAN, eth0.2 für WAN).
     - HTTP filtern: `tcpdump -i any tcp port 80 -n -v -A` (`-A` zeigt ASCII-Payload für HTTP-Header/Anfragen).
     - In Datei speichern: `tcpdump -i any tcp -w /tmp/capture.pcap` (herunterladen via SCP: `scp root@192.168.1.1:/tmp/capture.pcap .`).
     - Für HTTPS (Port 443) sind die Nutzdaten verschlüsselt – verwenden Sie Wireshark offline zur Analyse.

   - **HTTP-Anfrageprotokolle überwachen:**
     - Systemprotokolle (beinhaltet Web-Server, falls uhttpd verwendet wird): `logread | grep uhttpd` oder `logread -f` für Echtzeit.
     - Detaillierte HTTP-Protokollierung aktivieren: Bearbeiten Sie `/etc/config/uhttpd` (Web-Server-Konfiguration), fügen Sie `option log_file '/var/log/uhttpd.log'` hinzu, dann `/etc/init.d/uhttpd restart`. Anzeige des Endes: `tail -f /var/log/uhttpd.log` (zeigt GET/POST-Anfragen, IPs, URLs).
     - Für gesamten HTTP-Netzwerkverkehr: Verwenden Sie `tcpdump` wie oben, oder installieren Sie `ngrep` (`opkg install ngrep`): `ngrep -d any 'GET|POST|HTTP' -O /tmp/http.pcap`.

   - **Firewall-/Verbindungsprotokolle:**
     - Protokollierung für Regeln aktivieren: `uci set firewall.@rule[0].log='1'; uci commit; /etc/init.d/firewall restart`.
     - Anzeigen: `logread | grep fw` (zeigt abgewiesene/akzeptierte TCP-Verbindungen).

#### Tipps für ethisches "Hacking"
- **Sicherheit**: Ändern Sie nach dem Setup das Root-Passwort (`passwd`), deaktivieren Sie die Passwort-Authentifizierung in `/etc/ssh/sshd_config` für Schlüssel-only, und beschränken Sie die Firewall für SSH auf das LAN.
- **Leistung**: Der T7 hat 256MB RAM – vermeiden Sie langfristig umfangreiche Aufnahmen, um Speichermangel (OOM) zu verhindern.
- **Zurück zur Standard-Firmware**: Laden Sie die offizielle Firmware von der 360-Website herunter, laden Sie sie über das OpenWrt-Sysupgrade hoch (mit `--force` falls nötig).
- Testen Sie in einer sicheren Umgebung; für GUI-Analysen übertragen Sie die .pcap-Datei per SCP auf den PC und öffnen sie in Wireshark.

Dies bietet umfassende Transparenz. Wenn die Standard-UI für die Grundfunktionen ausreicht, bleiben Sie dort, um das Flashen zu vermeiden.

[OpenWrt Techdata: Qihoo 360T7](https://openwrt.org/toh/hwdata/qihoohardware/qihoohardware_360t7)  
[360 T7U Handbuch (Protokoll-Abschnitt)](https://ipc-pr-cdn.jia.360.cn/ipc-pr/luyouqiT7U.pdf)  
[OpenWrt Protokollierungsanleitung](https://openwrt.org/docs/guide-user/base-system/log.essentials)  
[360 Forum: Protokoll-Export](https://bbs.360.cn/forum-7007-1.html)