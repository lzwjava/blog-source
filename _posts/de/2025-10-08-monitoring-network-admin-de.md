---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Überwachung der Netzwerkaktivität mit Administratorrechten
translated: true
type: note
---

### Überwachung von HTTP-Anfragen und TCP-Verbindungen mit Admin-Rechten

Angenommen, Sie arbeiten auf einem Linux/Unix-ähnlichen System (z.B. Ubuntu, CentOS) mit Root-/Admin-Rechten, können Sie Netzwerkaktivitäten ethisch für Fehlerbehebung, Sicherheitsaudits oder Pentesting überwachen. **Wichtig: Tun Sie dies nur auf Systemen, die Ihnen gehören oder für die Sie ausdrückliche Erlaubnis haben – unbefugte Überwachung ist illegal.** Ich konzentriere mich auf Befehlszeilen-Tools, die leichtgewichtig sind und keine GUI benötigen.

#### 1. **Alle TCP-Verbindungen überwachen**
   Verwenden Sie integrierte Tools wie `ss` (moderner Ersatz für `netstat`) oder `tcpdump` für die Echtzeiterfassung. Diese zeigen aktive Verbindungen, Ports und Prozesse an.

   - **Alle aktuellen TCP-Verbindungen auflisten (statische Ansicht):**
     ```
     sudo ss -tunap
     ```
     - `-t`: Nur TCP.
     - `-u`: UDP falls benötigt (aber Sie fragten nach TCP).
     - `-n`: Numerische Ports (keine DNS-Auflösung).
     - `-a`: Alle Zustände (established, listening, etc.).
     - `-p`: Zeige zugehörige Prozesse.
     Beispielausgabe:
     ```
     tcp   ESTAB  0      0      192.168.1.10:80     10.0.0.5:54321    users:(("nginx",pid=1234,fd=5))
     ```
     Nur für lauschende Sockets: `sudo ss -tlnp`.

   - **Echtzeit-Überwachung mit watch:**
     ```
     watch -n 1 'sudo ss -tunap'
     ```
     Aktualisiert jede Sekunde.

   - **Live-TCP-Datenverkehr erfassen (Paketebene):**
     Installieren Sie `tcpdump`, falls nicht vorhanden: `sudo apt update && sudo apt install tcpdump` (Debian/Ubuntu) oder `sudo yum install tcpdump` (RHEL/CentOS).
     ```
     sudo tcpdump -i any tcp -n -v
     ```
     - `-i any`: Alle Schnittstellen.
     - `-n`: Keine Namensauflösung.
     - `-v`: Ausführlich.
     Fügen Sie `port 80 or port 443` hinzu, um HTTP/HTTPS zu filtern: `sudo tcpdump -i any tcp port 80 or tcp port 443 -n -v -A` (`-A` für ASCII-Payload, um HTTP-Header zu sehen).

     Speichern Sie in einer Datei für spätere Analyse: `sudo tcpdump -i any tcp -w capture.pcap`.

#### 2. **HTTP-Anfrageprotokolle überwachen**
   HTTP-Protokolle hängen von Ihrem Webserver ab (Apache, Nginx, etc.). Wenn kein Webserver läuft, verwenden Sie Netzwerkerfassung (siehe oben), um HTTP-Datenverkehr zu inspizieren. Für serverspezifische Protokolle:

   - **Apache (httpd):**
     Protokolle befinden sich typischerweise in `/var/log/apache2/access.log` (Ubuntu) oder `/var/log/httpd/access_log` (CentOS).
     ```
     sudo tail -f /var/log/apache2/access.log
     ```
     - Zeigt Anfragen in Echtzeit: IP, Zeitstempel, Methode (GET/POST), URL, Statuscode.
     Beispielzeile: `192.168.1.100 - - [08/Oct/2025:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1234`.

     Für alle Protokolle: `sudo grep "GET\|POST" /var/log/apache2/access.log | less`.

   - **Nginx:**
     Protokolle in `/var/log/nginx/access.log`.
     ```
     sudo tail -f /var/log/nginx/access.log
     ```
     Ähnliches Format wie Apache.

   - **Wenn kein Webserver (allgemeine HTTP-Abfangung):**
     Verwenden Sie `tcpdump` wie oben mit `-A`, um HTTP-Payloads auszugeben, oder installieren Sie `ngrep` für Regex-Matching:
     ```
     sudo apt install ngrep  # Installieren falls benötigt
     sudo ngrep -d any 'GET|POST|HTTP' -O http_capture.pcap
     ```
     Dies filtert und protokolliert HTTP-Methoden.

   - **Fortgeschritten: Richten Sie einen transparenten Proxy für vollständige Protokollierung ein.**
     Installieren Sie Squid-Proxy: `sudo apt install squid`.
     Konfigurieren Sie `/etc/squid/squid.conf`, um alles HTTP zu protokollieren (fügen Sie `access_log /var/log/squid/access.log squid` hinzu).
     Leiten Sie Datenverkehr über iptables um: `sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 3128`.
     Dann tailen Sie das Squid-Protokoll: `sudo tail -f /var/log/squid/access.log`.

#### Tipps für "Hacking" (Ethisches Pentesting)
- **Kombinieren Sie Tools:** Leiten Sie `tcpdump` zu `grep` für spezifische Muster um, z.B. `sudo tcpdump -i any tcp port 80 -A | grep "User-Agent"`.
- **Visualisieren mit Wireshark:** Für GUI-Analyse installieren Sie Wireshark (`sudo apt install wireshark`), führen es als Root aus und öffnen Ihre `.pcap`-Datei.
- **Sicherheitshärtung:** Nach der Überwachung, löschen Sie Protokolle, falls sensibel: `sudo truncate -s 0 /var/log/access.log`.
- **Cross-Platform-Hinweis:** Unter Windows (mit Admin) verwenden Sie `netstat -anob` für TCP und Event Viewer für Protokolle. Unter macOS `netstat -an` und `tcpdump`.

Dieser Setup gibt Ihnen umfassende Einblicke ohne externe Tools. Testen Sie zuerst in einer VM.

[Linux ss Command Man Page](https://man7.org/linux/man-pages/man8/ss.8.html)  
[Tcpdump Tutorial](https://www.tcpdump.org/manpages/tcpdump.1.html)  
[Apache Access Log Format](https://httpd.apache.org/docs/2.4/logs.html)