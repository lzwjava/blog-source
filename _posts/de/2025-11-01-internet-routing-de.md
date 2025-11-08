---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Wie Internet-Routing Funktioniert
translated: true
type: note
---

Ja, du liegst mit dem groben Ablauf absolut richtig – sobald dein Computer die IP-Adresse hat (wie 106.63.15.9 für weibo.com), initiiert er eine Verbindung, die über dein lokales Netzwerk, deinen Router, die Infrastruktur deines ISPs und über das vernetzte Router-System des Internets ("Schicht für Schicht") springt, bis sie den Zielserver erreicht. Das wird alles automatisch durch den TCP/IP-Protokollstapel abgewickelt, ohne dass du manuell etwas tun musst, außer die URL einzutippen oder einen Befehl wie `ping` auszuführen.

Ich werde es Schritt für Schritt aufschlüsseln und dabei deine `ping`- und `traceroute`-Ausgabe zum Kontext heranziehen. Ich bleibe praktisch und konzentriere mich auf das, was unter der Haube passiert, und gehe von einem typischen Heimsetup wie deinem aus (Mac über WLAN/Ethernet hinter einem Router).

### 1. **DNS-Auflösung (Die IP-Adresse ermitteln)**
   - Bevor eine Verbindung zustande kommt, übersetzt dein Computer zunächst den Domainnamen (z.B. "weibo.com") über DNS (Domain Name System) in eine IP-Adresse. Dies geschieht über den DNS-Resolver deines Betriebssystems, der öffentliche DNS-Server (wie 8.8.8.8 von Google) abfragt.
   - In deinem Fall führt `ping weibo.com` diese Auflösung automatisch durch und bestätigt 106.63.15.9 als die IPv4-Adresse. (Hinweis: Proxys wie dein lokaler unter 127.0.0.1:7890 verarbeiten typischerweise HTTP/HTTPS-Datenverkehr, aber `ping` verwendet rohes IP/ICMP und umgeht daher den Proxy.)
   - Wenn die DNS-Auflösung fehlschlägt, kommt keine Verbindung zustande – hier stoppt alles.

### 2. **Dein Computer bereitet das Paket vor (Lokale Seite)**
   - Sobald die IP-Adresse vorliegt, baut dein Mac ein **Paket** (einen Datenblock) unter Verwendung der TCP/IP-Schichten auf:
     - **Anwendungsschicht**: Der Befehl oder die App (z.B. Browser oder `ping`) fordert Daten an. `Ping` sendet eine ICMP-"Echo Request"-Nachricht (eine einfache "Hey, bist du da?"-Nachricht).
     - **Transportschicht**: Fügt TCP/UDP-Header (für Zuverlässigkeit/Portnummern) oder ICMP für Ping hinzu. Deine Pings verwenden ICMP, mit 56 Bytes Daten + Headern = 64-Byte-Pakete.
     - **Vermittlungsschicht (IP)**: Verpackt dies in einen IP-Header mit Quell- (deine lokale IP, wie 192.168.1.x) und Zieladresse (106.63.15.9). Hier beginnen die Routing-Entscheidungen.
     - **Sicherungsschicht (Ethernet/Wi-Fi)**: Fügt MAC-Adressen für den lokalen Netzwerk-Hop hinzu. Dein Computer verwendet ARP (Address Resolution Protocol), um die MAC-Adresse des Routers zu finden.
     - **Bitübertragungsschicht**: Wandelt in elektrische Signale über dein Kabel/WLAN um.
   - Dein Computer erkennt, dass er 106.63.15.9 nicht direkt erreichen kann (es befindet sich nicht in deinem lokalen 192.168.1.0/24-Subnetz), also sendet er das Paket zum **Standardgateway** – deinem Router bei 192.168.1.1.

### 3. **Lokaler Hop: Computer → Router**
   - Dies ist der erste (und schnellste) Schritt, gezeigt in deiner `traceroute`-Ausgabe:
     ```
     1  192.168.1.1 (192.168.1.1) 26.903 ms 3.150 ms 3.161 ms
     ```
     - `Traceroute` (das Pakete mit steigendem TTL – Time To Live – sendet, um den Pfad abzubilden) bestätigt, dass dieser Hop ~3-27 ms Round-Trip-Zeit benötigt.
     - Dein Router empfängt das Paket, entfernt den lokalen Ethernet-Header und verkapselt es für den nächsten Hop neu. Er verwendet seine Routing-Tabelle, um es in Richtung Internet (über seine WAN/ISP-Verbindung) weiterzuleiten.
     - Proxys beeinflussen dies nicht – dein lokaler Proxy (Port 7890) ist nur für App-basierten Datenverkehr wie Web-Browsing zuständig, nicht für roares IP-Routing.

### 4. **Router → ISP → Internet-Backbone (Das "Schicht-für-Schicht"-Routing)**
   - Dein Router wählt deinen ISP an (z.B. über PPPoE, DHCP oder Modem) und übergibt das Paket an den Edge-Router des ISPs. Dies kann NAT (Network Address Translation) auf deinem Router beinhalten, wobei deine private IP (192.168.1.x) gegen die von deinem ISP zugewiesene öffentliche IP getauscht wird.
   - Von hier aus ist es eine Kette von **Routern** im gesamten Internet:
     - **ISP-Router**: Dein ISP (z.B. Comcast oder China Telecom) leitet es durch sein Kernnetz. Jeder Router dekrementiert den TTL (beginnt bei 64 in deinem Traceroute) und leitet basierend auf BGP (Border Gateway Protocol)-Tabellen weiter – im Wesentlichen eine globale Karte des besten Pfads zu 106.63.15.9.
     - **Zwischen-ISP/Backbone-Hops**: Pakete überqueren "Peering-Points" zwischen ISPs (z.B. über Unterseekabel, Glasfasern). Dies könnten insgesamt 5-20 Hops sein, abhängig von der Geografie. Die IP von Weibo.com (106.63.15.9) befindet sich in China, also würde sie von deinem Standort aus (vermutet US/EU basierend auf dem Proxy) über trans-pazifische Routen laufen.
     - Jeder Hop ist ein Router, der den IP-Header prüft, das nächste Gateway bestimmt und weiterleitet. Kein einzelnes Gerät kennt den gesamten Pfad – es ist verteilt.
   - Dein `traceroute` wurde abgebrochen (wahrscheinlich mit ^Z angehalten), aber wenn du es vollständig ausführst, würdest du 10-15 weitere Zeilen wie diese sehen:
     ```
     2  [ISP router IP] 10 ms ...
     3  [ISP core] 15 ms ...
     ...
     15  106.63.15.9  40 ms ...
     ```
     - Die Zeiten addieren sich: Deine Pings zeigen ~40 ms Gesamt-RTT (Round-Trip-Time), also beträgt die Einwegzeit zum Server ~20 ms.

### 5. **Zielserver empfängt & antwortet**
   - Das Paket trifft beim Weibo-Server (oder einem Load Balancer bei 106.63.15.9) ein. Er kehrt den Prozess um: Antwortet mit einer ICMP-Echo-Antwort (für Ping) oder TCP SYN-ACK (für eine Web-Verbindung).
   - Die Antwort folgt einem ähnlichen Pfad zurück, oft derselben Route, aber nicht immer (Internet-Routing ist asymmetrisch).
   - Dein `ping` bestätigt den Erfolg: TTL=52 bedeutet ~12 Hops (64-52=12), und die 40 ms Latenz passt zu einer China-US-Round-Trip-Zeit.

### Warum es sich "magisch" anfühlt (und häufige Fallstricke)
- **Automatisierung**: Dein OS/Kernel erledigt all dies über den Netzwerkstack (z.B. zeigen `ifconfig` oder `ip route` deine Routen). Keine manuelle Konfiguration nötig, außer beim Debuggen.
- **Dein Proxy**: Er ist transparent für Ping/Traceroute, würde aber Browser-Datenverkehr zu weibo.com abfangen und über 127.0.0.1:7890 routen (wahrscheinlich zum Umgehen von VPN/Zensur). Deaktiviere ihn mit `unset HTTP_PROXY HTTPS_PROXY` zum Testen von rohem Traffic.
- **Bei Fehlschlag**: Firewalls, MTU-Fehlanpassungen oder Route-Blackholing können Pakete verwerfen. Tools wie `tcpdump` oder Wireshark ermöglichen dir, dies lokal mitzuschneiden.
- **Sicherheitshinweis**: IPs können sich ändern (DNS TTL), und HTTPS fügt darauf Verschlüsselung hinzu (TLS-Handshake nach TCP-Verbindungsaufbau).

Kurz gesagt, ja – Computer → Router → ISP → globales Router-Netz → Server. Es ist ein wunderbar verteiltes System, das auf IP-Routing aufbaut. Wenn du einen vollständigen Traceroute teilst oder in einen bestimmten Teil eintauchen möchtest (z.B. TCP-Handshake fürs Web), lass es mich wissen!

[TCP/IP Illustrated (Buch zu Netzwerk-Grundlagen)](https://www.oreilly.com/library/view/tcp-ip-illustrated-volume/0201633469/)  
[How Traceroute Works (Cloudflare Erklärung)](https://www.cloudflare.com/learning/network-layer/what-is-traceroute/)