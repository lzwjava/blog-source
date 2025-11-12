---
audio: false
generated: true
lang: de
layout: post
title: Traceroute-Optionen
translated: true
type: note
---

Traceroute ist ein leistungsfähiges Werkzeug zur Diagnose von Netzwerkpfaden. Während die grundlegende Verwendung einfach ist, bietet es erweiterte Optionen, um sein Verhalten anzupassen. Im Folgenden werde ich gängige Optionen umreißen und erklären, wie man traceroute auf fortgeschrittene Weise verwendet, mit Fokus auf praktische Beispiele. Die genauen Optionen hängen von Ihrem Betriebssystem ab (z.B. Windows verwendet `tracert`, während Linux/macOS `traceroute` verwenden), aber ich werde die am weitesten verbreiteten behandeln.

### Grundlegende Verwendung
- **Linux/macOS**: `traceroute [Ziel]`
  - Beispiel: `traceroute google.com`
- **Windows**: `tracert [Ziel]`
  - Beispiel: `tracert google.com`

Dies zeigt die Hops (Router) zwischen Ihnen und dem Ziel zusammen mit den Round-Trip-Zeiten (RTT) für jeden Hop.

---

### Häufige Traceroute-Optionen
Hier ist eine Übersicht über wichtige Optionen, primär für den `traceroute`-Befehl auf Unix-ähnlichen Systemen (Linux/macOS). Windows `tracert` hat weniger Optionen, teilt aber einige Konzepte.

1. **`-n` (Keine DNS-Auflösung)**
   - Überspringt die Auflösung von IP-Adressen zu Hostnamen, beschleunigt den Prozess und zeigt rohe IPs.
   - Verwendung: `traceroute -n google.com`
   - Grund: Nützlich, wenn die DNS-Auflösung langsam ist oder Sie nur an den IPs interessiert sind.

2. **`-m [max_hops]` (Maximale Hops setzen)**
   - Begrenzt, wie viele Hops traceroute überprüft, bevor es aufgibt (Standard ist oft 30).
   - Verwendung: `traceroute -m 15 google.com`
   - Grund: Verhindert endlose Läufe, wenn das Ziel unerreichbar oder sehr weit entfernt ist.

3. **`-q [nqueries]` (Anzahl der Abfragen pro Hop)**
   - Legt fest, wie viele Pakete pro Hop gesendet werden (Standard ist 3). Jede Abfrage zeigt einen Latenzwert.
   - Verwendung: `traceroute -q 1 google.com`
   - Grund: Reduziert die Ausgabemenge oder beschleunigt die Ablaufverfolgung; erhöhen Sie sie für zuverlässigere Latenzdaten.

4. **`-w [waittime]` (Wartezeit pro Hop)**
   - Setzt, wie lange (in Sekunden) auf eine Antwort gewartet werden soll, bevor ein Hop als Zeitüberschreitung markiert wird.
   - Verwendung: `traceroute -w 2 google.com`
   - Grund: Passt sich an langsame Netzwerke an oder reduziert Verzögerungen in schnellen.

5. **`-p [port]` (Port angeben, UDP-Modus)**
   - Setzt den Zielport für UDP-basiertes traceroute (Standard ist oft 33434+).
   - Verwendung: `traceroute -p 53 google.com`
   - Grund: Zielt auf bestimmte Dienste ab (z.B. DNS auf Port 53) oder umgeht Filter, die ICMP blockieren.

6. **`-I` (ICMP anstelle von UDP verwenden)**
   - Wechselt von UDP (Standard auf vielen Systemen) zu ICMP Echo Request Paketen.
   - Verwendung: `traceroute -I google.com`
   - Grund: Einige Netzwerke blockieren UDP, erlauben aber ICMP, was die Sichtbarkeit verbessert.

7. **`-T` (TCP-Modus)**
   - Verwendet TCP-Pakete anstelle von UDP oder ICMP, oft mit SYN-Paketen.
   - Verwendung: `traceroute -T -p 80 google.com`
   - Grund: Umgeht Firewalls, die ICMP/UDP blockieren; ideal für die Ablaufverfolgung zu Web-Servern (Port 80 = HTTP).

8. **`-f [first_ttl]` (Bei spezifischem TTL starten)**
   - Setzt den anfänglichen TTL-Wert und überspringt frühere Hops.
   - Verwendung: `traceroute -f 5 google.com`
   - Grund: Konzentriert sich auf einen bestimmten Teil des Pfades, z.B. jenseits Ihres lokalen Netzwerks.

9. **`-g [gateway]` (Loose Source Routing)**
   - Zwingt Pakete, ein bestimmtes Gateway zu passieren (wenn vom Netzwerk unterstützt).
   - Verwendung: `traceroute -g 192.168.1.1 google.com`
   - Grund: Testet bestimmte Routen oder umgeht Standard-Routing.

10. **`-4` oder `-6` (IPv4 oder IPv6 erzwingen)**
    - Beschränkt traceroute auf IPv4 oder IPv6.
    - Verwendung: `traceroute -6 google.com`
    - Grund: Stellt sicher, dass Sie ein bestimmtes Protokoll testen, nützlich für Dual-Stack-Netzwerke.

---

### Windows `tracert` Optionen
Windows hat weniger Optionen, aber hier sind die wichtigsten:
- **`-d`**: Keine DNS-Auflösung (wie `-n`).
- **`-h [max_hops]`**: Maximale Hops (wie `-m`).
- **`-w [timeout]`**: Wartezeit in Millisekunden (wie `-w`).
- Beispiel: `tracert -d -h 20 google.com`

---

### Beispiele für erweiterte Verwendung
Hier ist, wie man Optionen für bestimmte Zwecke kombiniert:

1. **Langsame Verbindung diagnostizieren**
   - Ziel: Herausfinden, wo Latenzspitzen auftreten.
   - Befehl: `traceroute -I -q 5 -w 1 google.com`
   - Grund: ICMP für Zuverlässigkeit, 5 Abfragen für bessere Latenzstatistiken, 1-Sekunden-Timeout für schnelles Vorankommen.

2. **Firewall-Beschränkungen umgehen**
   - Ziel: Zu einem Webserver verfolgen, der durch ICMP-Filter blockiert ist.
   - Befehl: `traceroute -T -p 443 google.com`
   - Grund: TCP auf Port 443 (HTTPS) imitiert legitimen Datenverkehr, der oft durch Firewalls erlaubt wird.

3. **Jenseits Ihres ISPs testen**
   - Ziel: Lokale Hops überspringen, um sich auf externes Routing zu konzentrieren.
   - Befehl: `traceroute -f 3 -m 10 google.com`
   - Grund: Beginnt bei Hop 3 (nach Ihrem Router/ISP), begrenzt auf insgesamt 10 Hops.

4. **IPv4- vs. IPv6-Pfade vergleichen**
   - Ziel: Sehen, ob die Protokollwahl das Routing beeinflusst.
   - Befehle:
     - `traceroute -4 google.com`
     - `traceroute -6 google.com`
   - Grund: Identifiziert Unterschiede in Netzwerkpfaden oder Leistung.

5. **Stille, schnelle Ablaufverfolgung für Skripting**
   - Ziel: Schnelle Ausgabe für Automatisierung.
   - Befehl: `traceroute -n -q 1 -w 1 google.com > output.txt`
   - Grund: Kein DNS, eine Abfrage, kurzes Timeout, Ausgabe in eine Datei umgeleitet.

---

### Tipps für die erweiterte Verwendung
- **Kombinieren mit anderen Tools**: Kombinieren Sie traceroute mit `ping` (für Latenz) oder `mtr` (Echtzeit-traceroute) für tiefere Einblicke.
- **Netzwerkkontext verstehen**: Firewalls, NAT oder VPNs können Hops verschleiern (zeigen Sternchen `*`) – passen Sie Protokolle (ICMP/TCP) an.
- **Root-Rechte**: Auf Unix-Systemen erfordern einige Optionen (z.B. TCP-Modus) möglicherweise `sudo` für Raw-Socket-Zugriff: `sudo traceroute -T google.com`.

Die Stärke von traceroute liegt in seiner Flexibilität. Durch das Anpassen von Optionen können Sie es anpassen, um spezifische Netzwerkprobleme zu beheben, Beschränkungen zu umgehen oder Routing-Verhalten im Detail zu analysieren. Lassen Sie mich wissen, wenn Sie tiefer in ein bestimmtes Szenario eintauchen möchten!