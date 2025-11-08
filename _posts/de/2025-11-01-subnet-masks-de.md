---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Grundlagen von Subnetzmasken
translated: true
type: note
---

### Was ist eine Subnetzmaske?

Eine **Subnetzmaske** (oder Netmask) ist eine 32-Bit-Zahl (geschrieben in punktierter Dezimalschreibweise, wie 255.255.255.0), die eine IPv4-Adresse in zwei Teile unterteilt:
- **Netzwerkanteil**: Identifiziert das übergeordnete Netzwerk (oder Subnetz), zu dem ein Gerät gehört.
- **Hostanteil**: Identifiziert das spezifische Gerät (Host) innerhalb dieses Netzwerks.

Sie funktioniert wie ein Filter: Wenn ein Gerät Daten sendet, wird die Subnetzmaske (mittels einer bitweisen UND-Operation) auf die IP-Adresse angewendet, um herauszufinden, ob das Ziel im *lokalen Subnetz* liegt (direkte Kommunikation, kein Router erforderlich) oder in einem *entfernten Netzwerk* (Daten gehen durch das Standardgateway/den Router).

#### Aufschlüsselung von 255.255.255.0
Deine Erklärung ist **genau richtig**—lass sie uns Schritt für Schritt bestätigen und erweitern.

1.  **In Binär (Hier passiert die eigentliche Magie)**:
    - Jedes Oktett (z.B. 255) ist 8 Bit, also ist die vollständige Maske 32 Bit.
    - 255 = `11111111` (alle Bits "an").
    - 0 = `00000000` (alle Bits "aus").
    - Also ist 255.255.255.0 in Binär:  
      `11111111.11111111.11111111.00000000`
    - Das bedeutet:
      - **Erste 24 Bits (drei 255er):** Fest als **Netzwerkpräfix**. Diese können sich für Geräte im selben Subnetz nicht ändern—sie definieren, *in welchem Subnetz* man sich befindet.
      - **Letzte 8 Bits (die 0):** Variabel als **Hostanteil**. Diese *können* sich ändern, um einzelne Geräte zu identifizieren.

2.  **Wie viele Adressen sind in diesem Subnetz?**
    - Der Hostanteil hat 8 Bits, also gibt es \\(2^8 = 256\\) mögliche Kombinationen (von `00000000` bis `11111111`, oder 0 bis 255 dezimal).
    - Beispiel mit einer Basis-IP wie 192.168.1.0:
      - Netzwerkadresse: 192.168.1.0 (alle Host-Bits = 0; dies ist die Subnetz-ID selbst).
      - Verwendbare Hosts: 192.168.1.1 bis 192.168.1.254 (254 Adressen, da .0 für das Netzwerk und .255 für Broadcast reserviert ist).
      - Broadcast: 192.168.1.255 (sendet an alle im Subnetz).
    - Dein Router (z.B. auf 192.168.1.1) vergibt IPs aus diesem Pool via DHCP, wie die von dir erwähnte 192.168.1.100.

3.  **Kommunikation innerhalb des Subnetzes**:
    - Ja! Geräte mit IPs im selben Subnetz (z.B. dein Laptop auf 192.168.1.100 und ein Telefon auf 192.168.1.50) können *direkt* über Ethernet/Wi-Fi kommunizieren—keine Router-Sprünge nötig. Die Subnetzmaske sagt ihnen: "Hey, wir sind Nachbarn—schick die Pakete direkt zur MAC-Adresse."
    - Wenn das Ziel außerhalb liegt (z.B. 192.168.2.50), gehen die Daten zum Standardgateway (deinem Router auf 192.168.1.1), um woanders hingeleitet zu werden.

#### Schnelle Visualisierung: IP-Adresse + Subnetzmaske Beispiel

| IP-Adresse      | Subnetzmaske    | Netzwerkanteil | Hostanteil | Vollständige Netzwerk-ID |
|-----------------|-----------------|----------------|------------|--------------------------|
| 192.168.1.100 | 255.255.255.0 | 192.168.1    | .100      | 192.168.1.0            |

- Zur Berechnung: IP UND Maske = Netzwerk-ID (z.B., 192.168.1.100 UND 255.255.255.0 = 192.168.1.0).

Dies ist ein typisches Heimnetzwerk-Setup (/24-Subnetz, oder CIDR-Notation 192.168.1.0/24). Größere Masken (z.B. 255.255.255.252) bedeuten kleinere Subnetze mit weniger Hosts, aber präziserer Segmentierung.

Wenn du ein spezifisches IP-Setup hast oder etwas berechnen möchtest (z.B. per Code), teile mehr Details mit!