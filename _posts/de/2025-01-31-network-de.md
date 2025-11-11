---
audio: false
generated: false
lang: de
layout: post
title: Computernetzwerktechnologie
translated: true
type: note
---

Nachfolgend finden Sie eine Liste von 100 Kernpunkten, die den Umfang eines Kurses oder Selbststudienplans zum Thema "Computer Network Technology" grob abdecken und grundlegende Konzepte, Protokolle und praktische Anwendungen behandeln.

1.  **Definition eines Computernetzwerks:** Ein System miteinander verbundener Geräte, die Ressourcen und Daten gemeinsam nutzen.
2.  **Primäre Funktionen von Netzwerken:** Ressourcenfreigabe, Kommunikation, Datenübertragung und Zusammenarbeit.
3.  **Evolution von Netzwerken:** Von ARPANET und frühen LANs zum heutigen globalen Internet.
4.  **Häufige Netzwerktypen:** LAN (Local Area Network), MAN (Metropolitan Area Network), WAN (Wide Area Network).
5.  **Topologiestrukturen:** Bus, Stern, Ring, Masche und Hybrid.
6.  **Intranet vs. Extranet vs. Internet:** Unterschiede im Umfang und typische Anwendungsfälle.
7.  **Standardisierungsorganisationen:** IEEE, IETF, ISO – definieren und pflegen Netzwerkstandards und -protokolle.
8.  **OSI-Referenzmodell:** Ein siebenschichtiges konzeptionelles Framework zum Verständnis von Netzwerkfunktionen.
9.  **TCP/IP-Modell:** Ein pragmatisches vier- (oder manchmal fünf-) schichtiges Modell, das dem Internet zugrunde liegt.
10. **Vergleich von OSI und TCP/IP:** Gemeinsamkeiten (schichtenbasierter Ansatz) und Unterschiede (Anzahl der Schichten und Abstraktion).

11. **Zweck der Bitübertragungsschicht:** Befasst sich mit der Übertragung roher Bits über ein physisches Medium.
12. **Häufige Übertragungsmedien:** Twisted-Pair-Kabel, Koaxialkabel, Glasfaser und drahtlos.
13. **Bandbreite vs. Durchsatz:** Theoretische maximale Rate vs. tatsächliche Datenübertragungsrate.
14. **Signalcodierung:** Methoden (z.B. Manchester-Codierung) zur Darstellung von Datenbits für die Übertragung.
15. **Modulationstechniken:** AM, FM, PM, verwendet bei Analog-Digital- oder Digital-Analog-Umwandlungen.
16. **Geräte der Bitübertragungsschicht:** Hubs, Repeater – hauptsächlich Wiederholung von Signalen ohne Prüfung.
17. **Zweck der Sicherungsschicht:** Behandelt Framing, Adressierung, Fehlererkennung/-korrektur und Flusskontrolle.
18. **Framing:** Einkapseln von Paketen in Sicherungsschicht-Headern und Trailern.
19. **MAC-Adresse (Media Access Control):** Eine eindeutige Hardwarekennung für Netzwerkschnittstellenkarten.
20. **Fehlererkennungsmechanismen:** Paritätsprüfung, CRC (Cyclic Redundancy Check), Prüfsummen.
21. **Ethernet-Grundlagen:** Die gebräuchlichste LAN-Technologie; verwendet eine Rahmenstruktur mit Quell-/Ziel-MAC.
22. **Ethernet-Rahmenformat:** Präambel, Ziel-MAC, Quell-MAC, Typ/Länge, Nutzlast, CRC.
23. **Switching:** Weiterleiten von Frames mithilfe von MAC-Adresstabellen in einem LAN.
24. **Lernprozess in Switches:** Aufbau einer Tabelle von MAC-Adressen, während Geräte kommunizieren.
25. **VLAN (Virtual LAN):** Logische Segmentierung eines physischen LANs in mehrere virtuelle Netzwerke.
26. **Zweck der Vermittlungsschicht:** Routing, logische Adressierung (IP) und Wegfindung.
27. **IPv4-Adressformat:** 32-Bit-Adresse, typischerweise in punktierter Dezimalschreibweise dargestellt.
28. **IPv4-Klassen (veraltet):** Klasse A, B, C, D, E (historischer Kontext, ersetzt durch CIDR).
29. **CIDR (Classless Inter-Domain Routing):** Moderner Ansatz für flexiblere IP-Adressenvergabe.
30. **IPv4 vs. IPv6:** Wichtige Unterschiede (128-Bit-Adressierung, erweitertes Header-Format, Autokonfiguration).
31. **Subnetting:** Unterteilung eines großen Netzwerks in kleinere Teilnetze für eine effiziente Adressnutzung.
32. **NAT (Network Address Translation):** Abbildung privater IP-Adressen auf eine öffentliche IP zur Schonung von IPv4-Adressen.
33. **ARP (Address Resolution Protocol):** Auflösung von IP-Adressen zu MAC-Adressen innerhalb eines LANs.
34. **ICMP (Internet Control Message Protocol):** Diagnosewerkzeug – wird von ping, traceroute verwendet.
35. **Routing vs. Switching:** Routing erfolgt auf IP-Ebene (Schicht 3), Switching auf MAC-Ebene (Schicht 2).
36. **Statisches Routing:** Manuelles Konfigurieren von Routen in einer Routing-Tabelle eines Routers.
37. **Dynamische Routingprotokolle:** RIP (Routing Information Protocol), OSPF (Open Shortest Path First), BGP (Border Gateway Protocol).
38. **Router-Grundlagen:** Bestimmt den nächsten Netzwerksprung für ein Paket basierend auf IP-Adressen.
39. **Zweck der Transportschicht:** Ende-zu-Ende-Datenlieferung, Zuverlässigkeit und Flusskontrolle.
40. **TCP (Transmission Control Protocol):** Verbindungsorientiertes Protokoll, das zuverlässige Datenübertragung bietet.
41. **TCP-Segmentstruktur:** Quellport, Zielport, Sequenznummer, Bestätigungsnummer usw.
42. **TCP Dreiwege-Handshake:** SYN, SYN-ACK, ACK Prozess für den Verbindungsaufbau.
43. **TCP-Vierwege-Abbau:** FIN, FIN-ACK, ACK Sequenz zum Schließen einer Verbindung.
44. **TCP-Flusskontrolle:** Mechanismen wie gleitendes Fenster zur Steuerung der Datenübertragungsrate.
45. **TCP-Überlastkontrolle:** Algorithmen (Slow Start, Congestion Avoidance, Fast Recovery, Fast Retransmit).
46. **UDP (User Datagram Protocol):** Verbindungslos, minimaler Overhead, keine Zustellgarantie.
47. **UDP-Segmentstruktur:** Quellport, Zielport, Länge, Prüfsumme, Daten.
48. **Portnummern:** Bezeichner für Dienste (z.B. 80 für HTTP, 443 für HTTPS, 53 für DNS).
49. **Socket:** Kombination aus einer IP-Adresse und einem Port zur Identifizierung eines Endpunkts.
50. **Zweck der Anwendungsschicht:** Bietet Netzwerkdienste für Anwendungen des Benutzers.
51. **HTTP (Hypertext Transfer Protocol):** Die Grundlage der Datenkommunikation im Web.
52. **HTTP-Methoden:** GET, POST, PUT, DELETE, HEAD usw.
53. **HTTPS:** Verschlüsseltes HTTP mit TLS/SSL für sichere Webkommunikation.
54. **DNS (Domain Name System):** Ordnet Domainnamen (z.B. example.com) IP-Adressen zu.
55. **DNS-Auflösungsprozess:** Rekursive und iterative Abfragen, Root-Server, TLD-Server, autoritative Server.
56. **FTP (File Transfer Protocol):** Legacy-Protokoll für Dateiübertragungen über TCP (Ports 20/21).
57. **E-Mail-Protokolle:** SMTP (Senden), POP3 und IMAP (Abrufen).
58. **DHCP (Dynamic Host Configuration Protocol):** Weist Geräten automatisch IP-Adressen zu.
59. **Telnet vs. SSH:** Remote-Zugriffsprotokolle – SSH ist verschlüsselt, Telnet nicht.
60. **Client-Server-Modell:** Eine gängige Architektur, bei der ein Client Dienste von einem Server anfordert.
61. **P2P-Modell (Peer-to-Peer):** Jeder Knoten kann sowohl Dienste anfordern als auch bereitstellen.
62. **Web-Technologien:** URLs, URIs, Cookies, Sessions, grundlegende Webanwendungsstruktur.
63. **Netzwerksicherheitsprinzipien:** Vertraulichkeit, Integrität, Verfügbarkeit (CIA-Triade).
64. **Häufige Sicherheitsbedrohungen:** Malware (Viren, Würmer, Trojaner), DDoS-Angriffe, Phishing, SQL-Injection.
65. **Firewalls:** Filtert Datenverkehr basierend auf Regeln, an Netzwerkgrenzen platziert.
66. **IDS/IPS (Intrusion Detection/Prevention Systems):** Überwacht den Datenverkehr auf verdächtige Aktivitäten.
67. **VPN (Virtual Private Network):** Verschlüsselter Tunnel über ein öffentliches Netzwerk, sichert Remote-Verbindungen.
68. **TLS/SSL (Transport Layer Security / Secure Sockets Layer):** Verschlüsselung für sichere Datenübertragung.
69. **Grundlagen der Kryptographie:** Symmetrische vs. asymmetrische Verschlüsselung, Schlüsselaustausch, digitale Signaturen.
70. **Digitale Zertifikate:** Werden von CAs (Certificate Authorities) bereitgestellt, um Identität zu validieren und HTTPS zu ermöglichen.
71. **Netzwerksicherheitsrichtlinien:** Richtlinien für die sichere Netzwerknutzung, Zugangskontrollen und Auditing.
72. **DMZ (Demilitarized Zone):** Ein Teilnetz, das extern zugängliche Dienste der Öffentlichkeit exponiert.
73. **WLAN-Sicherheit:** Drahtlose Netzwerke (Wi-Fi), gesichert durch WPA2, WPA3 usw.
74. **Physische Sicherheit:** Sicherstellung, dass die Netzwerkinfrastruktur (Server, Kabel, Router) sicher untergebracht ist.
75. **Social Engineering:** Nicht-technische Eindringtaktiken – Phishing, Pretexting, Baiting.
76. **OSI-Schicht-Angriffe:** Verschiedene Bedrohungen/Abwehrmaßnahmen auf jeder Schicht (z.B. ARP-Spoofing auf der Sicherungsschicht).
77. **Netzwerkverwaltungstools:** ping, traceroute, netstat, nslookup, dig.
78. **Packet Sniffer:** Tools wie Wireshark oder tcpdump zur Analyse des Datenverkehrs auf Paketebene.
79. **Netzwerkmanagementprotokolle:** SNMP (Simple Network Management Protocol).
80. **Protokollierung und Monitoring:** Syslog, Ereignisprotokolle, SIEM-Lösungen für die Echtzeiterkennung.

81. **Grundlegender LAN-Aufbau:** Bestimmung von IP-Bereichen, Subnetzmasken, Gateway, DNS-Servern.
82. **Kabeltypen:** CAT5, CAT5e, CAT6, Glasfaser, wann welches typischerweise verwendet wird.
83. **Strukturierte Verkabelung:** Standards für professionelle Netzwerkinstallationen in großem Maßstab.
84. **Switch-Konfiguration:** Erstellen von VLANs, Trunk-Ports und Spanning-Tree-Protokollen.
85. **Router-Konfiguration:** Einrichten von Routen (statisch/dynamisch), NAT, ACL (Access Control Lists).
86. **Grundlegende Firewall-Regeln:** Alle eingehenden Verbindungen verweigern, außer erforderlichen; alle ausgehenden erlauben oder nach Bedarf einschränken.
87. **Netzadressierungspläne:** Effiziente Vergabe von IP-Adressen basierend auf Abteilung oder Subnetzen.
88. **Redundanz und Failover:** Verwendung von Backup-Links, Lastverteilung oder VRRP/HSRP für hohe Verfügbarkeit.
89. **QoS (Quality of Service):** Priorisierung bestimmten Datenverkehrs (z.B. VoIP) zur Leistungssicherung.
90. **Cloud-Networking-Grundlagen:** Virtuelle Netzwerke, Security Groups, Load Balancer in Cloud-Umgebungen.
91. **SDN (Software-Defined Networking):** Trennung der Control Plane von der Data Plane für zentralisiertes Management.
92. **Virtualisierung:** Verwendung von Hypervisoren (VMware, Hyper-V, KVM) zur Erstellung virtueller Server/Netzwerke.
93. **Container und Microservices:** Docker-Netzwerke, Kubernetes-Networking-Konzepte.
94. **IPv6-Bereitstellung:** Dual Stack (IPv4/IPv6), IPv6-Autokonfiguration (SLAAC), IPv6-Tunnel.
95. **DNS-Lastverteilung:** Verteilung des Datenverkehrs über mehrere Server mittels DNS-Round Robin.
96. **Edge Computing:** Verarbeitung am Netzwerkrand zur Reduzierung der Latenz für IoT und Echtzeitanwendungen.
97. **5G und die Entwicklung der Funktechnologie:** Höhere Datenraten, geringere Latenz, Einsatz im IoT und mobilen Breitband.
98. **Schritte zur Netzwerkfehlerbehebung:** Problem identifizieren, isolieren, Hypothesen testen, beheben, überprüfen.
99. **Dokumentation:** Bedeutung der Führung genauer Netzwerkdiagramme und Gerätekonfigurationen.
100. **Kontinuierliches Lernen:** Netzwerktechnik entwickelt sich ständig weiter und erfordert fortlaufendes Studium neuer Protokolle und Best Practices.

Diese 100 Punkte fassen die wesentlichen Themen in Computernetzwerken zusammen, die grundlegende Theorie, Protokolle, Hardware, Adressierung, Sicherheit und moderne Trends umfassen. Sie sollten Ihre Überprüfung und Ihr Studium für Prüfungen oder das praktische Verständnis von Computernetzwerken leiten.