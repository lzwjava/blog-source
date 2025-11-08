---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Netzwerkadressübersetzung kurz erklärt
translated: true
type: note
---

### Was ist NAT (Network Address Translation)?

NAT ist eine Netzwerktechnik, die verwendet wird, um IP-Adressen (und manchmal auch Portnummern) in den Headern von Paketen zu ändern, während sie einen Router oder eine Firewall passieren. Ihr Hauptzweck ist es, mehreren Geräten in einem privaten (lokalen) Netzwerk zu ermöglichen, eine einzige öffentliche IP-Adresse zu teilen, wenn sie eine Verbindung zum Internet herstellen. Dies hilft, öffentliche IP-Adressen zu sparen, verbessert die Sicherheit, indem interne Netzwerkdetails verborgen werden, und ermöglicht es privaten Netzwerken, mit dem öffentlichen Internet zu kommunizieren.

Es gibt einige gängige Arten von NAT:
- **Source NAT (SNAT)**: Übersetzt die Quell-IP ausgehender Pakete (z.B. von einer privaten zu einer öffentlichen IP).
- **Destination NAT (DNAT)**: Übersetzt die Ziel-IP eingehender Pakete (z.B. um Datenverkehr an einen bestimmten internen Server weiterzuleiten).
- **Port Address Translation (PAT)**: Eine Variante von SNAT, die auch Ports neu zuordnet, sodass viele private Geräte eine öffentliche IP-Adresse teilen können.

NAT wird typischerweise auf Routern, Firewalls oder Gateways implementiert.

### Übersetzt NAT lokale Adressen (z.B. 192.168.0.x) in ein anderes Subnetz?

Ja, genau – das ist eine seiner Kernfunktionen. Private IP-Bereiche wie 192.168.0.x (oder 10.0.0.x, 172.16-31.x.x) sind im öffentlichen Internet nicht routbar (gemäß RFC 1918). Wenn ein Gerät in Ihrem Heim-/Büro-LAN (z.B. 192.168.0.10) ausgehenden Datenverkehr sendet:

1.  Das NAT-Gerät (wie Ihr Router) ändert die Quell-IP von der privaten Adresse (192.168.0.10) zu seiner eigenen öffentlichen IP (z.B. so etwas wie 203.0.113.5 in einem anderen Subnetz).
2.  Es verfolgt auch die ursprüngliche IP/Port-Kombination, um eingehende Antworten korrekt zurückzuschreiben.
3.  Diese "Übersetzung" geschieht dynamisch für ausgehenden Datenverkehr, sodass es so aussieht, als ob alle Ihre Geräte von einer öffentlichen Adresse kommen.

Für eingehenden Datenverkehr (z.B. das Hosten eines Servers) benötigen Sie eine zusätzliche Einrichtung wie Portweiterleitung (eine Form von DNAT), um die öffentliche IP wieder auf eine bestimmte private IP abzubilden.

### NAT in Windows XP

Sie liegen genau richtig – Windows XP enthielt eine integrierte NAT-Unterstützung via **Internet Connection Sharing (ICS)**. Dies erlaubte es, eine Internetverbindung von einem PC (der als Gateway fungiert) mit anderen in einem lokalen Netzwerk zu teilen. ICS verwendete NAT, um private IPs (z.B. aus dem geteilten Netzwerk) in die öffentliche IP des Host-PCs zu übersetzen. Es war eine einfache Möglichkeit, ein Mini-Heimnetzwerk einzurichten, bevor Consumer-Router allgegenwärtig wurden. Man konnte es in den Netzwerkverbindungseinstellungen aktivieren, und es vergab sogar automatisch DHCP-IPs wie 192.168.0.x.

### Das "Huasheng Ke" Programm in China (Das Exponieren lokaler Server)

Ich glaube, Sie meinen **花生壳 (Huāshēngké)**, allgemein bekannt als **Peanut Shell** – einen beliebten dynamischen DNS (DDNS)-Dienst in China (und weltweit). Es ist nicht NAT selbst, aber es funktioniert *mit* NAT, um das von Ihnen angesprochene Problem "lokalen Computer als Server exponierten" zu lösen.

-   Hinter NAT (z.B. auf einem Heimrouter) ist Ihr lokaler Server (sagen wir, ein Webserver auf 192.168.0.50:80) nicht direkt vom Internet aus erreichbar, weil er eine private IP hat.
-   Peanut Shell stellt einen Domainnamen bereit (z.B. yourserver.peanuthull.com), der dynamisch aktualisiert wird, um auf Ihre öffentliche IP zu zeigen. Kombiniert mit Portweiterleitung auf Ihrem Router "bohrt es sich durch" NAT, um Ihren lokalen Rechner als öffentlichen Server fungieren zu lassen (für Websites, Spiele, Dateifreigabe usw.).
-   Es ist besonders nützlich in Regionen mit dynamischen öffentlichen IPs oder strikten NAT-Einstellungen und existiert seit den frühen 2000er Jahren, ähnlich wie Dienste von No-IP oder DynDNS.

Falls das nicht das exakte Programm ist, das Sie meinten, können Sie gerne näher erläutern!

### NAT in AWS

AWS verwendet NAT intensiv für Cloud-Netzwerke:
-   **NAT Gateway**: Ein verwalteter Service in einem öffentlichen Subnetz, der Instanzen in privaten Subnetzen (z.B. mit privaten IPs wie 10.0.1.x) erlaubt, ausgehenden Internetzugang zu initiieren (z.B. für Software-Updates), ohne sie direkt zu exponieren. Er übersetzt private Quell-IPs in die öffentliche Elastic IP des Gateways.
-   **NAT Instance**: Eine DIY-Alternative, die eine EC2-Instanz als NAT-Router verwendet (heute weniger verbreitet).
-   Dies hält Ihre privaten Ressourcen sicher, während gleichzeitig unidirektionaler ausgehender Datenverkehr ermöglicht wird – perfekt für VPCs (Virtual Private Clouds).

Kurz gesagt, NAT ist überall in modernen Netzwerken zu finden, um private und öffentliche Welten effizient zu verbinden. Wenn Sie ein bestimmtes Setup oder Szenario im Kopf haben (z.B. Fehlerbehebung), kann ich genauer darauf eingehen!