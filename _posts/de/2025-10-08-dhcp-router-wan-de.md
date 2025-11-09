---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: DHCP-Protokolle für die Router-WAN-Schnittstelle
translated: true
type: note
---

### Verständnis der DHCP-Protokolleinträge im 360 Wi-Fi Router T7

Dieser Protokollausschnitt von Ihrem 360 T7 Router (wahrscheinlich aus dem Bereich **System > Protokoll** in der Web-Oberfläche extrahiert) zeigt, wie die WAN-Schnittstelle des Routers als DHCP-Client agiert, um seine öffentliche IP-Adresse vom DHCP-Server Ihres ISP zu beziehen und zu erneuern. DHCP (Dynamic Host Configuration Protocol) ist das Standardprotokoll zur automatischen Zuweisung von IP-Adressen in Netzwerken. Der Router fordert periodisch eine IP-Adresse an oder erneuert die Lease, um die Internetverbindung aufrechtzuerhalten – typischerweise alle 12-24 Stunden, abhängig von der Lease-Time Ihres ISP.

Diese Einträge sind **normal und weisen auf einen ordnungsgemäßen Betrieb hin**, es handelt sich nicht um einen Fehler. Sie repräsentieren den standardmäßigen DORA-Prozess (Discover, Offer, Request, ACK) für die anfängliche IP-Zuweisung, gefolgt von Lease-Verlängerungen. Hier ist eine Aufschlüsselung jeder Zeile in chronologischer Reihenfolge (Hinweis: Die Zeitstempel sind in Ihrem Protokoll in umgekehrter Reihenfolge, ich habe sie der Übersichtlichkeit halber neu geordnet; die Datumsangaben folgen dem Format JJJJ/MM/TT-HH:MM:SS):

| Log-ID | Zeitstempel         | Nachricht                | Erklärung |
|--------|--------------------|--------------------------|-------------|
| 148   | 2025/09/19-03:44:57 | Sending DHCP discover   | Der Router sendet eine **DHCP Discover**-Nachricht als Broadcast auf der WAN-Seite, um einen verfügbaren DHCP-Server (Ihres ISP) zu finden. Dies ist der erste Schritt, wenn die Lease abläuft oder der Router neu startet. (Er wiederholt dies schnell in der nächsten Zeile.) |
| 147   | 2025/09/19-03:45:00 | Sending DHCP discover   | Ein erneuter Versuch der Discover-Nachricht (üblich, wenn keine sofortige Antwort kommt; Router senden 2-4 Wiederholungsversuche mit exponentiellem Backoff). |
| 146   | 2025/09/19-03:45:02 | DHCP offer Received     | Der DHCP-Server des ISP antwortet mit einem **DHCP Offer**, der eine verfügbare IP-Adresse, Subnetzmaske, Gateway, DNS-Server und Lease-Dauer (z.B. 24 Stunden) vorschlägt. |
| 145   | 2025/09/19-03:45:02 | Sending DHCP request    | Der Router sendet eine **DHCP Request**-Nachricht, um die angebotene IP zu akzeptieren und den Server formell um deren Zuweisung zu bitten (Broadcast, damit andere Server ihre Angebote zurückziehen können, falls vorhanden). |
| 144   | 2025/09/19-03:45:02 | DHCP ACK received       | Der Server sendet eine **DHCP ACK** (Acknowledge/Bestätigung), die die IP-Zuweisung bestätigt. Der Router hat nun eine gültige WAN-IP und kann eine Verbindung zum Internet herstellen. Dies schließt die anfängliche Lease-Beantragung ab (hier insgesamt ~5 Sekunden). |
| 143   | 2025/09/19-15:45:02 | Sending DHCP renew      | ~12 Stunden später (die Hälfte einer typischen 24-Stunden-Lease) sendet der Router proaktiv eine **DHCP Renew**-Nachricht (ein Unicast-Request an den bekannten Server), um die Lease ohne vollständige Neuentdeckung zu verlängern. |
| 142   | 2025/09/19-15:45:02 | DHCP ACK received       | Der Server bestätigt die Verlängerung – die Lease wurde nahtlos verlängert. |
| 141   | 2025/09/20-03:45:02 | Sending DHCP renew      | Eine weitere Verlängerung ~12 Stunden später (nun am nächsten Tag). Wenn keine ACK folgt (hier nicht gezeigt), könnte es zu einem vollständigen Rebind oder einer Neuentdeckung eskalieren. |

#### Warum dies geschieht
- **Lease-Zyklus**: ISPs setzen Lease-Zeiten (z.B. 24 Stunden). Nach Ablauf von 50% der Zeit erneuert der Client die Lease, um Ausfallzeiten zu vermeiden. Wenn die Erneuerung bei 87,5% fehlschlägt, erfolgt ein Rebind (Broadcast-Request); bei 100% startet der vollständige DORA-Prozess neu.
- **Im Kontext des 360 T7**: Dies wird unter WAN-Verbindungsereignissen protokolliert. Der T7 verwendet einen schlanken DHCP-Client (wahrscheinlich udhcpc-basiert) in seiner Firmware, der diese genauen Meldungen generiert. Keine Probleme, es sei denn, Sie sehen Fehler wie "DHCP NAK received" (IP abgelehnt) oder wiederholte Discovers ohne ACKs (könnte auf ISP-Probleme oder Kabelprobleme hindeuten).
- **Troubleshooting-Tipps**:
  - Wenn die Internetverbindung zu diesen Zeiten abbricht, überprüfen Sie den WAN-Status in der Oberfläche (**Status > WAN**) auf IP-Änderungen oder Fehler.
  - Exportieren Sie vollständige Protokolle über die Oberfläche, um Muster zu erkennen.
  - Um eine Erneuerung zu erzwingen: Führen Sie eine WAN-Freigabe/Erneuerung unter **Netzwerk > WAN** durch oder starten Sie den Router neu.

Dies ist Routineverhalten – Ihr Router hält lediglich sein "Internet-Ticket" gültig.

[Understanding DHCP Basics (Microsoft)](https://learn.microsoft.com/en-us/windows-server/troubleshoot/dynamic-host-configuration-protocol-basics)  
[DHCP Process Overview (Netmanias)](https://www.netmanias.com/en/post/techdocs/5998/dhcp-network-protocol/understanding-the-basic-operations-of-dhcp)