---
audio: false
generated: true
lang: de
layout: post
title: Windows Netzwerkbefehle
translated: true
type: note
---

Lassen Sie uns einige nützliche Windows-Netzwerkbefehle erkunden, die Sie in der Eingabeuforderung (CMD) ausführen können, um Probleme zu beheben, Informationen zu sammeln oder Ihr Netzwerk zu verwalten. Ich werde einige beliebte Befehle wie `getmac` erklären und andere hinzufügen, die nützlich sein könnten. Sie müssen kein Technik-Experte sein – diese Befehle sind recht einfach, sobald man den Dreh raus hat.

Zuerst müssen Sie die Eingabeaufforderung öffnen, um diese Befehle zu verwenden: Drücken Sie `Windows-Taste + R`, geben Sie `cmd` ein und drücken Sie die Eingabetaste. Einfach, oder?

### 1. `getmac` - Finden Sie Ihre MAC-Adresse
Der `getmac`-Befehl zeigt die Media Access Control (MAC)-Adresse Ihrer Netzwerkadapter an – diese eindeutigen Identifikatoren für Ihr Gerät in einem Netzwerk. So funktioniert es:

- Geben Sie `getmac` ein und drücken Sie die Eingabetaste.
- Sie sehen eine Liste der MAC-Adressen für jeden Netzwerkadapter (wie Ethernet oder Wi-Fi).
- Fügen Sie den Schalter `-v` hinzu (`getmac -v`) für den ausführlichen Modus, der zusätzliche Details wie den Adapternamen und den Transporttyp (z.B. Ethernet oder Wireless) liefert.

Eine Beispielausgabe könnte so aussehen:
```
Physical Address    Transport Name
=================== ==========================================================
00-14-22-01-23-45   \Device\Tcpip_{12345678-ABCD-1234-EF56-7890ABCDEF12}
```
Die "Physical Address" ist Ihre MAC-Adresse. Nützlich für die Netzwerkfehlerbehebung oder die Einrichtung von MAC-Filtering auf einem Router.

### 2. `ipconfig` - Überprüfen Sie Ihre IP-Konfiguration
Dies ist ein Standardbefehl für Netzwerkinformationen:
- Geben Sie `ipconfig` ein und drücken Sie die Eingabetaste, um grundlegende Details wie Ihre IP-Adresse, Subnetzmaske und das Standardgateway zu sehen.
- Verwenden Sie `ipconfig /all` für eine vollständige Aufschlüsselung, einschließlich DNS-Server, DHCP-Status und – ja – auch Ihrer MAC-Adresse.

Er ist ideal, um herauszufinden, ob Ihr Gerät ordnungsgemäß verbunden ist oder ob ein IP-Konflikt vorliegt.

### 3. `ping` - Verbindung testen
Möchten Sie prüfen, ob Sie ein anderes Gerät oder eine Website erreichen können?
- Geben Sie `ping [Adresse]` ein (z.B. `ping google.com` oder `ping 8.8.8.8`).
- Er sendet einige Pakete und teilt Ihnen mit, ob sie zurückkommen und wie lange es dauert (in Millisekunden).

Wenn Sie "Request timed out" erhalten, blockiert etwas die Verbindung – das könnte eine Firewall, ein ausgefallener Server oder Ihr eigenes Netzwerk sein.

### 4. `tracert` - Route verfolgen
Kurz für "Trace Route", zeigt dieser Befehl den Weg, den Ihre Daten zu einem Ziel nehmen:
- Geben Sie `tracert [Adresse]` ein (z.B. `tracert google.com`).
- Er listet jeden Hop (Router oder Server) auf dem Weg zusammen mit den Antwortzeiten auf.

Praktisch, um festzustellen, wo eine Verbindung langsamer wird oder fehlschlägt.

### 5. `netstat` - Netzwerkaktivität anzeigen
Dieser Befehl zeigt, was gerade in Ihrem Netzwerk passiert:
- Geben Sie `netstat -a` ein, um alle aktiven Verbindungen und abhörenden Ports zu sehen.
- Fügen Sie `-n` hinzu (`netstat -an`), um IP-Adressen anstelle von Hostnamen anzuzeigen – schneller und unverarbeitet.

Es ist wie ein Fenster, das zeigt, mit wem Ihr Computer spricht – nützlich, um verdächtige Aktivitäten zu erkennen.

### 6. `nslookup` - DNS überprüfen
Wenn Webseiten nicht laden, überprüft dieser Befehl die Domain Name System (DNS)-Auflösung:
- Geben Sie `nslookup [Domain]` ein (z.B. `nslookup google.com`).
- Er gibt die mit dieser Domain verknüpfte IP-Adresse zurück und zeigt, ob Ihr DNS funktioniert.

### Tipps für einen reibungslosen Ablauf
- Führen Sie CMD als Administrator aus (Rechtsklick auf Eingabeaufforderung > "Als Administrator ausführen"), wenn ein Befehl höhere Berechtigungen benötigt.
- Kombinieren Sie Befehle mit `|` (Pipe) zum Filtern – z.B. `getmac | find "00-14"`, um nach einer bestimmten MAC-Adresse zu suchen.
- Wenn Sie nicht weiterkommen, geben Sie `[Befehl] /?` ein (z.B. `ipconfig /?`), um die Hilfe zu diesem Befehl aufzurufen.

Dies sind Ihre grundlegenden Werkzeuge, um sich in einem Windows-Netzwerk umzusehen. Möchten Sie sich auf einen Befehl konzentrieren – wie `getmac` – oder etwas Bestimmtes ausprobieren? Lassen Sie mich wissen, was Sie vorhaben!