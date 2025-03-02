---
audio: true
generated: true
lang: de
layout: post
title: Windows-Netzwerkbefehle
translated: true
---

Lass uns einige nützliche Windows-Netzwerkbefehle durchgehen, die du im Eingabeaufforderungsfenster (CMD) ausführen kannst, um Probleme zu beheben, Informationen zu sammeln oder dein Netzwerk zu verwalten. Ich werde einige beliebte Befehle wie `getmac` erklären und einige andere hinzufügen, die nützlich sein könnten. Du musst kein Tech-Experte sein – diese sind ziemlich einfach, sobald du den Dreh raushast.

Zuerst, um diese Befehle zu verwenden, öffne das Eingabeaufforderungsfenster: Drücke `Windows-Taste + R`, gib `cmd` ein und drücke Enter. Einfach genug, oder?

### 1. `getmac` - Finde deine MAC-Adresse
Der `getmac`-Befehl zeigt die Media Access Control (MAC)-Adresse deiner Netzwerkadapter – diese eindeutigen Kennungen für dein Gerät in einem Netzwerk. Hier ist, wie es funktioniert:

- Gib `getmac` ein und drücke Enter.
- Du siehst eine Liste von MAC-Adressen für jeden Netzwerkadapter (wie Ethernet oder Wi-Fi).
- Füge den `-v`-Schalter hinzu (`getmac -v`) für den ausführlichen Modus, der zusätzliche Details wie den Adapternamen und den Transporttyp (z.B. Ethernet oder Wireless) liefert.

Ein Beispielausgabe könnte so aussehen:
```
Physikalische Adresse    Transportname
=================== ==========================================================
00-14-22-01-23-45   \Device\Tcpip_{12345678-ABCD-1234-EF56-7890ABCDEF12}
```
Die „Physikalische Adresse“ ist deine MAC. Nützlich für die Netzwerkfehlerbehebung oder das Einrichten von MAC-Filterung auf einem Router.

### 2. `ipconfig` - Überprüfe deine IP-Konfiguration
Dies ist ein Standardbefehl für Netzwerkinformationen:
- Gib `ipconfig` ein und drücke Enter, um grundlegende Details wie deine IP-Adresse, Subnetzmaske und Standardgateway zu sehen.
- Verwende `ipconfig /all` für eine vollständige Aufschlüsselung, einschließlich DNS-Server, DHCP-Status und – ja – deine MAC-Adresse noch einmal.

Es ist großartig, um herauszufinden, ob dein Gerät ordnungsgemäß verbunden ist oder ob es einen IP-Konflikt gibt.

### 3. `ping` - Teste die Verbindungsfähigkeit
Möchtest du überprüfen, ob du ein anderes Gerät oder eine Website erreichen kannst?
- Gib `ping [Adresse]` ein (z.B. `ping google.com` oder `ping 8.8.8.8`).
- Es sendet einige Pakete und sagt dir, ob sie zurückkommen, plus wie lange es dauert (in Millisekunden).

Wenn du „Anfrage abgelaufen“ erhältst, blockiert etwas die Verbindung – könnte ein Firewall, ein toter Server oder dein eigenes Netzwerk sein.

### 4. `tracert` - Verfolge den Weg
Kurz für "trace route", zeigt dies den Weg, den deine Daten zu einem Ziel nehmen:
- Gib `tracert [Adresse]` ein (z.B. `tracert google.com`).
- Es listet jeden Hop (Router oder Server) entlang des Weges mit Antwortzeiten auf.

Nützlich, um herauszufinden, wo eine Verbindung verlangsamt oder ausfällt.

### 5. `netstat` - Sieh dir die Netzwerkaktivität an
Dieser Befehl dient dazu, herauszufinden, was gerade in deinem Netzwerk passiert:
- Gib `netstat -a` ein, um alle aktiven Verbindungen und lauschenden Ports zu sehen.
- Füge `-n` hinzu (`netstat -an`), um IP-Adressen anstelle von Hostnamen anzuzeigen – schneller und roher.

Es ist wie ein Fenster, das zeigt, mit wem dein Computer spricht – nützlich, um verdächtige Aktivitäten zu erkennen.

### 6. `nslookup` - DNS-Details
Wenn Websites nicht geladen werden, überprüft dies die Domain Name System (DNS)-Auflösung:
- Gib `nslookup [Domain]` ein (z.B. `nslookup google.com`).
- Es gibt die IP-Adresse zurück, die mit dieser Domain verbunden ist, und zeigt, ob dein DNS funktioniert.

### Tipps für einen reibungslosen Ablauf
- Führe CMD als Administrator aus (mit der rechten Maustaste auf Eingabeaufforderung > „Als Administrator ausführen“), wenn ein Befehl höhere Berechtigungen benötigt.
- Kombiniere Befehle mit `|` (Pipe) zum Filtern – z.B. `getmac | find "00-14"`, um nach einer bestimmten MAC zu suchen.
- Wenn du feststeckst, gib `[Befehl] /?` ein (z.B. `ipconfig /?`), um Hilfe zu diesem Befehl zu erhalten.

Das sind deine grundlegenden Werkzeuge zum Herumstöbern in einem Windows-Netzwerk. Möchtest du dich auf einen konzentrieren – wie `getmac` – oder etwas Spezielles ausprobieren? Lass mich wissen, was du vorhast!