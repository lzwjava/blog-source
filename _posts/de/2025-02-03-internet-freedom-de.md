---
audio: false
generated: false
image: false
lang: de
layout: post
title: Der Weg zur Verfolgung der Internetfreiheit
translated: true
---

### Inhaltsverzeichnis

1. [Proxy-Lösungen in China](#proxy-lösungen-in-china)
   - Macao-SIM-Karten-Lösungen (Beste Option)
   - Proxy-Server-Empfehlungen
   - App-Konfiguration und Einrichtung
   - Zahlung und regionale Einstellungen

2. [Der Weg zur Internetfreiheit](#der-weg-zur-internetfreiheit)
   - Zeitstrahl der Proxy-Methoden (2010–2025)
   - Vergleich: Internetfreiheit vs. Kurzsichtigkeitslösungen
   - Aktuelle Einrichtung und Leistung
   - Wiederherstellungsmethoden und gelernte Lektionen

3. [Macao-SIM-Karten](#macao-sim-karten)
   - Details zur China Telecom Easy+ SIM-Karte
   - Blue Macau SIM-Karten-Optionen
   - Preise und Datentarife
   - Gerätekompatibilität

4. [Shadowsocks-Proxy-Probleme](#shadowsocks-proxy-probleme)
   - Netzwerkspezifische Verbindungsprobleme
   - Leistungsunterschiede zwischen 5G und 4G
   - Fehlerbehebung und Lösungen
   - Auswirkungen der Richtlinien von ISPs und Mobilfunkanbietern

---

## Proxy-Lösungen in China

*29.12.2024*

* Die beste Methode ist der Kauf einer **China-Macao-SIM-Karte**, um bei Bedarf direkt mobiles Internet zu nutzen. Besuche [https://www.1888.com.mo](https://www.1888.com.mo). Die Kosten betragen etwa **80 CNY für 10 GB mobiles Datenvolumen** – schnell und unkompliziert.

* **China Telecom Macao-SIM-Karten** gibt es in zwei Varianten: **rot** und **blau**.
  - **Rote Karten** bieten Tagespläne (z. B. 2, 3 oder 5 Macao-Patacas pro Tag).
  - **Blaue Karten** bieten Datentarife (z. B. **10 GB für 98 MOP** oder **20 GB für 198 MOP**) ohne monatliche Grundgebühr.

* Falls du mehr Datenvolumen benötigst oder häufig einen Laptop nutzt, empfehlt sich [zhs.cloud](https://zhs.cloud). Für **30 CNY/Monat** erhältst du Zugang zu etwa **15 globalen Proxy-Servern**.

* **Auf iOS**: Nutze **Shadowrocket** mit Shadowsocks-Regeln:
  [https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever).
  Konfiguriere **globales Routing**, um den Datenverkehr zwischen China und dem Ausland zu trennen.

* **Auf Android**: Nutze **V2Ray**.
  **Auf Fire TV**: V2Ray-App.
  **Auf Apple TV**: Shadowrocket-App.
  **Auf Mac**: **ShadowsocksX-NG** oder **ClashX**.

* **Nicht empfohlen**: Eigenen Proxy-Server einrichten. Protokolle wie **Shadowsocks, VMess oder Trojan** werden leicht blockiert – unabhängig vom Server.

* **App Store auf USA-Regional umstellen**:
  Aktiviere einen **globalen Proxy (USA)**, dann erscheint die Zahlungsoption *„Keine“* und du kannst die Region wechseln.

* **Guthaben aufladen**: Nutze eine **Visa-Karte**, um Amazon-Geschenkkarten zu kaufen, oder lade dein App Store-Konto über das **Apple-Geschenkkarten-Portal** auf.

---

## Der Weg zur Internetfreiheit

*03.02.2025, Letzte Aktualisierung: August 2025.*

### Meine Reise

- **2010–2013**: Nutzte **Goagent** und das Proxy-Tool **SwitchyOmega**, um die GFW zu umgehen.
- **2014–2015**: Setzte **Qujing (曲径)** ein und folgte dessen Autor auf Twitter (der heute in Japan lebt).
- **Juni 2016 – Juli 2018**: Hostete meinen **Shadowsocks-Proxy-Server** bei **Digital Ocean**.
- **Ab 2019**: Wechsel zu [zhs.cloud](https://zhs.cloud).
- **März 2023**: Nutzte eine **Macao-SIM-Karte** im Handy für **Internet ohne Proxy/VPN** (Kosten: ~150 CNY/Monat für 20 GB). Diese Methode nutzte ich etwa ein Jahr.
- **2024**: Rückkehr zu **Outline Manager** mit eigenem Shadowsocks-Server und Tests verschiedener Cloud-Anbieter.
- **Februar 2025**: Aktuelle Einrichtung:
  - **Outline Manager** mit **Aliyun-Hongkong-Server** für den täglichen Gebrauch.
  - **Nicht-Hongkong-Server** (z. B. Singapur oder Japan) für KI-Tools.
  - Gleiche Proxy-Regeln wie in **Shadowrocket/Clash**.
- **Ab Juni 2025**:
  - **Python-Skript** auf dem Laptop, das alle **10 Minuten** automatisch den schnellsten Proxy-Server auswählt (basierend auf Speedtests).
  - **Priorisierung**: Singapur-Server für KI-Tools vor Hongkong-Servern.
  - Details: [Automatisierung der Clash-Proxy-Verwaltung](/clash-en).
  - **Cloud-Anbieter**: Nach wie vor [zhs.cloud](https://zhs.cloud).
  - **Auf iOS**: Rückkehr zur **Macao-SIM-Karte** (150 CNY/Monat für 20 GB + 3x 5 GB Nachkauf à 20 MOP → **35 GB für ~200 CNY**).

Die letzten **2 Monate** lief alles reibungslos. Ich hoffe, diese Methode bis zu meinem Auslandsaufenthalt nutzen zu können.

---

### Unterschied zum Rückgang der Kurzsichtigkeit

- **GFW**: Ein vom Menschen gemachtes Hindernis.
- **Kurzsichtigkeit**: Betrifft die **Funktionsweise der Augenmuskeln**.

**Messbarkeit**:
- Proxy-Lösungen lassen sich **sofort** auf Effektivität prüfen.
- Bei Kurzsichtigkeit dauert es **Monate/Jahre**, um Veränderungen der Augapfelform zu erkennen.

---
### Gemeinsamkeiten mit der Korrektur von Kurzsichtigkeit

- **Beide Lösungen funktionieren oft gut**:
  - Proxy für **Internetzugriff**, Brille mit **200 Dioptrien weniger** für bessere Sicht.
- **Grundprinzip**:
  - Versteht man, **wie die GFW funktioniert**, lässt sie sich umgehen.
  - Versteht man die **Ursachen von Kurzsichtigkeit**, lässt sie sich korrigieren.

---
### Reflexionen und Nuancen

Ich verstehe die GFW **immer noch nicht vollständig**. Wenn mein Proxy-Server blockiert wird, habe ich heute mehr Möglichkeiten, die Ursache zu analysieren:

- **Netzwerktest**: Funktioniert die Blockade nur im **mobilen Netz** oder auch im **Heimnetz**?
- **5G vs. 4G**: Falls mobil, liegt es an **5G oder 4G**?
- **Kurzsichtigkeit**: Wenn nach 6–12 Monaten keine Besserung eintritt, muss ich prüfen:
  - Gibt es **Unterschiede zwischen beiden Augen**?
  - Habe ich die meiste Zeit nur **„gerade so scharf“** gesehen, ohne die Augen zu entspannen?

---
### Aktueller Status

- **Proxy-Server läuft stabil**:
  - **Download**: 80 Mbit/s, **Upload**: 50 Mbit/s (bei Verbindung zum Hongkong-Server).
  - Gleiche Leistung auf **Handy und Laptop**.
- **Konfiguration**:
  - **Proxy für ausländische Seiten**, **Nicht-HK-Server für KI-Tools**.

---
### Wiederherstellung bei Problemen

Falls etwas nicht funktioniert:
1. **Elastische IP** des **Aliyun-Hongkong-Servers** ändern.
2. Neue Proxy-URL in die **Cloud speichern**.
3. **Zwei Skripte ausführen** (~1 Minute) → **Laptop/Handy aktualisieren die Serveradresse automatisch**.

---
### Bedauern

- **Zu viel Zeit** mit dem Kampf gegen die GFW verbracht.
- **Viele Protokolle** ausprobiert, obwohl klar war, dass die GFW sie blockieren würde.
- **Ohne zuverlässigen Proxy-Server** ist die Einrichtung auf einem **OpenWrt-Router** schwierig.

**Was ich bereue**:
1. **Techniken von Proxy-Anbietern** wie [zhs.cloud](https://zhs.cloud) **nicht früher gelernt** zu haben.
2. **Oberflächliches Denken**: Bei einer Sperre einfach einen neuen Server aufgesetzt, statt die **Ursache** zu analysieren.

---
### Metriken

- **Speedtest hätte ich früher nutzen sollen**:
  - **5G**: Leicht über **100 Mbit/s**.
  - **Heimnetz**: Selten über **100 Mbit/s**.
- **Kurzsichtigkeit**:
  - **C-förmige Sehtafel** und **Standard-Sehtest** gekauft.
  - **„Keine Messung, keine Verbesserung.“**

---
### Es ist noch früh

- **Wird die GFW in den nächsten Jahren fallen?** Ungewiss.
- **Kurzsichtigkeit**:
  - Nach 2 Jahren sagte ich einem Freund, meine Methode müsse verbessert werden (von **150 auf 200 Dioptrien weniger**).
  - Seine Antwort: *„Kein Problem, es ist nicht verschwendete Zeit – es ist noch früh.“*
  - **Grundlegende Dinge** brauchen Zeit.
  - **Todd Becker** teilte seine Erkenntnisse **2014 auf YouTube** (über 1 Mio. Aufrufe). **2025** wissen **weniger als 10.000 Menschen** weltweit davon.

---

## Macau-SIM-Karten

*20.04.2023*

### Meine Erfahrungen mit Macau-SIM-Karten

Bei einem Wochenendbesuch in Macau **2023** kaufte ich eine **China Telecom Easy+ SIM-Karte**. Zurück in **Guangzhou** funktionierte sie einwandfrei – ich konnte **Englisch lernen** und **ausländische Apps herunterladen**, als wäre ich noch in Macau. **Absolut empfehlenswert!** Später testete ich die **Blue Macau SIM-Karte**, die ebenfalls gut war. Hier ein kurzer Überblick:

---
### **China Telecom Easy+ SIM-Karte**

**Jederzeit einfach nutzbar!**

#### Wichtige Punkte
- **Keine Kaution**, automatische Aktivierung für **Festlandchina, Macau und Hongkong**.
- **Kein Vertrag**, keine Kündigungsgebühr – sofort einsatzbereit.
- **Macao-Nummer inklusive**; optional **Festlandchina-Nummer** für Dual-SIM-Nutzung.
- **Online-Aufladung** oder per Wertkarte möglich.

#### Tagesgebühren
- **2 MOP/Tag**: 4 GB Hochgeschwindigkeitsvolumen, danach unbegrenzt (gedrosselt) + 5.000 Minuten lokale Gespräche.
- **3 MOP/Tag**: 10 GB Hochgeschwindigkeitsvolumen, danach unbegrenzt (gedrosselt) + 5.000 Minuten.
- **5 MOP/Tag**: 20 GB Hochgeschwindigkeitsvolumen, danach unbegrenzt (gedrosselt) + 5.000 Minuten.

#### Extras
- **Datenverbrauch in Hongkong**: 0,1 MOP/MB.
- **Tarifwechsel** jederzeit per SMS möglich.

---
### **Blue Macau SIM-Karte**

#### Wichtige Punkte
- **Keine monatliche Grundgebühr** – nutze, was du brauchst.
- **Lokale Gespräche**: 0,39 MOP/Minute; **Internet**: 0,1 MOP/MB; **SMS**: 1 MOP/Nachricht.
- **Optionale Datenpakete (ohne Ablauf)**:
  - 10 GB für **98 MOP**
  - 20 GB für **188 MOP**
  - 40 GB für **288 MOP**
- **Alle 180 Tage aufladen**, um die Karte aktiv zu halten.

---
### **Kompatible Geräte**
- **4G-Vollnetz-Unterstützung** oder **China Telecom-kompatibles Handy** erforderlich.

Mehr Infos: [China Telecom Macau](https://www.1888.com.mo/).

---
**Auf Taobao erhältlich:**

<div align="center"><img src="/assets/images/macao/easy.jpg" width="300px" /><img/></div>

---

## Shadowsocks-Proxy-Probleme

*03.01.2025*

**Zhiwei:**
Ich war mit einem Freund grillieren und nutzte **Shadowsocks mit einem Singapur-Server**, um die GFW zu umgehen. **Auf 5G draußen** funktionierte die Verbindung nicht (Timeout bei YouTube), aber **zu Hause auf 4G oder im China-Telecom-Heimnetz** lief alles einwandfrei. Warum?

**Mistral:**
Das klingt nach **netzwerkspezifischen Verbindungsproblemen**. Mögliche Ursachen:

1. **Unterschiede in der Netzwerkkonfiguration**:
   - **5G-Netz**: Strengere Firewall-Regeln oder andere Routing-Pfade als 4G.
   - **4G-Netz**: Weniger Restriktionen, bessere Kompatibilität mit Shadowsocks.

2. **ISP-Beschränkungen**:
   - **Mobilfunkanbieter-Politik**: Manche Anbieter blockieren/begrenzen VPN-Proxy-Verkehr auf 5G.
   - **Heimnetz (China Telecom)**: Weniger Filterung → Shadowsocks funktioniert.

3. **Signalstärke und Stabilität**:
   - **5G-Signal**: Outdoor oft instabil, führt zu Timeouts.
   - **4G-Signal**: Stabiler, zuverlässigere Verbindung für Shadowsocks.

4. **Server-Standort (Singapur)**:
   - **Latenz**: 5G könnte höhere Latenz zum Singapur-Server haben als 4G/Heimnetz.
   - **Routing**: Suboptimale Pfade auf 5G.

5. **Geräteeinstellungen**:
   - **Konfiguration**: Prüfe, ob Shadowsocks für 5G/4G korrekt eingerichtet ist.
   - **App-Berechtigungen**: Stelle sicher, dass die App auf allen Netzen funktioniert.

---
### **Fehlerbehebungsschritte**:

1. **Netzwerkeinstellungen prüfen**:
   - Shadowsocks-Konfiguration für **5G/4G** überprüfen.
   - Gibt es **spezifische 5G-Blockaden**?

2. **Andere Server testen**:
   - Wechsel zu einem **Hongkong- oder Japan-Server**, um zu prüfen, ob das Problem nur bei Singapur auftritt.
   - **Latenz und Stabilität** messen (z. B. mit Ping).

3. **Mobilfunkanbieter kontaktieren**:
   - Nachfragen, ob **5G spezielle VPN-Beschränkungen** hat.

4. **Software aktualisieren**:
   - Shadowsocks-App und **Betriebssystem** auf dem neuesten Stand?

5. **Alternative Proxys/VPNs nutzen**:
   - Testweise **V2Ray oder WireGuard** ausprobieren, falls Shadowsocks auf 5G blockiert wird.

---
**Aktualisierung:**

Interessanterweise nutze ich zu Hause **China Mobile (IP: 120.235.8.xx)**. Hier zeigt sich ein **inkonsistentes Muster**:
- **Proxy funktioniert** auf **mobilen Daten und China Telecom**.
- **Manchmal blockiert** er jedoch im **Heim-WLAN (China Mobile)**.

**Fazit**: Systematische Tests helfen, die Ursache (ISP, Protokoll, Serverstandort) einzugrenzen.