---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: DNS Einfach Erklärt
translated: true
type: note
---

### Was bedeutet DNS?

DNS steht für **Domain Name System**. Es ist im Wesentlichen das "Telefonbuch" des Internets (und lokaler Netzwerke). Es übersetzt für Menschen lesbare Domainnamen (wie `www.example.com` oder `google.com`) in maschinenlesbare IP-Adressen (wie `192.0.2.1` oder `8.8.8.8`). Ohne DNS müssten Sie sich rohe IP-Adressen merken und eingeben, um Websites zu besuchen, was unpraktisch wäre.

DNS funktioniert hierarchisch: Ihr Gerät fragt einen DNS-Server ab (ein spezieller Server, der diese Nachschlagevorgänge bearbeitet), der entweder die Antwort kennt oder die Anfrage die Kette hinauf zu autoritativen Servern weiterleitet, bis der Name in eine IP-Adresse aufgelöst ist.

### DNS unter macOS oder Windows konfigurieren

Wenn Sie die Netzwerkeinstellungen unter macOS (in Systemeinstellungen > Netzwerk) oder Windows (in Einstellungen > Netzwerk & Internet > Ethernet/WLAN > Eigenschaften) konfigurieren, können Sie im Abschnitt **DNS** DNS-Server manuell angeben oder die von Ihrem Netzwerk bereitgestellten Standardwerte verwenden. Häufige Standardwerte sind:
- Die DNS-Server Ihres Internetanbieters.
- Öffentliche Server wie die von Google (`8.8.8.8` und `8.8.4.4`) oder Cloudflare (`1.1.1.1`).

Wenn Sie die Einstellung auf "Automatisch" belassen (oft über DHCP, wie Sie erwähnt haben), stellt Ihr Router oder Netzwerk diese DNS-Server für Sie bereit.

Die anderen von Ihnen aufgeführten Details:
- **192.168.1.1**: Dies ist typischerweise die lokale IP-Adresse Ihres Routers (das "Standardgateway"). Es ist die Tür zum externen Internet von Ihrem Heimnetzwerk aus.
- **IPv4 Use DHCP**: DHCP (Dynamic Host Configuration Protocol) ist ein Dienst, der automatisch IP-Adressen und andere Netzwerkinformationen an Geräte in Ihrem Netzwerk vergibt. "Use DHCP" bedeutet, dass Ihr Computer keine statische IP-Adresse wählt, sondern den DHCP-Server (normalerweise Ihren Router) dynamisch um eine bittet.

### Wie Ihr Computer eine Verbindung zum Netzwerk herstellt und IP-/Host-Anfragen bearbeitet

Lassen Sie uns den Prozess Schritt für Schritt aufschlüsseln, wenn Ihr Computer "das Netzwerk besucht" (d.h. eine Verbindung zu WLAN oder Ethernet herstellt):

1. **Erstverbindung und DHCP-Handshake**:
    - Wenn Sie eine Verbindung herstellen, sendet Ihr Computer eine DHCP-"Discover"-Anfrage als Broadcast: "Hallo, hat jemand eine verfügbare IP-Adresse für mich?"
    - Ihr **Router** (der als DHCP-Server fungiert) antwortet mit einem "Offer": "Sicher, hier ist eine IP für Sie (z.B. 192.168.1.100), plus Ihrer Subnetzmaske (z.B. 255.255.255.0), Ihrem Standardgateway (192.168.1.1) und den DNS-Server-IPs (z.B. 8.8.8.8)."
    - Ihr Computer akzeptiert ("Request") und bestätigt ("Acknowledge"). Jetzt hat er alles, um im lokalen Netzwerk zu kommunizieren.
    - Dies beinhaltet noch kein DNS – es dient nur der eigenen IP-Adresse Ihres Geräts und dem grundlegenden Routing. Ihr "Host" (Hostname, wie der Name Ihres Computers) kann lokal auf Ihrem Gerät festgelegt oder beim Router für die lokale Namensauflösung registriert sein, aber das ist separat.

2. **Hostnamen auflösen (Hier kommt DNS ins Spiel)**:
    - Sobald die Verbindung besteht und Sie versuchen, `www.google.com` zu besuchen, kennt Ihr Computer die IP-Adresse noch nicht. Er sendet eine **DNS-Abfrage** an den/die vom DHCP bereitgestellten DNS-Server (könnte die Router-IP oder eine externe sein).
    - **Geht sie zum Router?** Oft ja, indirekt:
        - Wenn Ihr Router als DNS-Proxy/-Weiterleitung konfiguriert ist (üblich in Heimroutern wie von TP-Link, Netgear oder Apple Airport), fragt Ihr Computer zuerst den Router ab (z.B. über 192.168.1.1 als DNS-Server).
        - Der Router prüft seinen lokalen Cache (für Geschwindigkeit). Wenn er die Antwort hat (von einer vorherigen Abfrage), antwortet er direkt. Wenn nicht, leitet er die Abfrage an einen vorgelagerten Upstream-DNS-Server weiter (wie den Ihres ISP oder einen öffentlichen, den Sie festgelegt haben).
    - Der vorgelagerte DNS-Server löst sie auf (z.B. `www.google.com` → `142.250.190.14`) und sendet die IP-Adresse über die Kette zurück zu Ihrem Computer.
    - Ihr Computer verwendet dann diese IP-Adresse, um eine Verbindung zur Website herzustellen.

3. **Wie der Router mit diesen Abfragen umgeht**:
    - **DHCP-Abfragen**: Der Router verwaltet einen Pool verfügbarer IP-Adressen (z.B. 192.168.1.50 bis 192.168.1.150). Wenn Sie eine anfordern, vergibt er sie für eine festgelegte Zeit (z.B. 24 Stunden) an Sie, verfolgt sie in seiner Tabelle und verlängert sie bei Bedarf. Er verwaltet auch Ihren Hostnamen, falls Sie einen festgelegt haben (z.B. für lokalen Zugriff wie `ping mylaptop.local`).
    - **DNS-Abfragen**: Der Router "besitzt" keine DNS-Einträge – er ist ein Mittelsmann. Er:
        - Speichert Antworten im Cache, um wiederholte Upstream-Abfragen zu vermeiden (verbessert Geschwindigkeit und reduziert Bandbreite).
        - Leitet ungelöste Abfragen an konfigurierte Upstream-Server weiter.
        - Wendet möglicherweise Kindersicherungen, Werbeblockierung (über benutzerdefinierte DNS wie Pi-hole) oder Protokollierung an.
        - Wenn die Abfrage für ein lokales Gerät bestimmt ist (z.B. einen anderen Computer in Ihrem Netzwerk), löst er sie möglicherweise über seine lokale Hosts-Datei oder mDNS (Multicast DNS, verwendet von Bonjour auf macOS/Apple-Geräten) auf.
    - Fehler? Wenn DNS fehlschlägt (z.B. falsche Server-IP), können Namen nicht aufgelöst werden – Websites laden nicht, aber das direkte Anpingen von IPs könnte funktionieren.

Kurz gesagt: DHCP besorgt Ihrem Computer seine "Adresse und Wegbeschreibung" vom Router. DNS verwendet dann diese Wegbeschreibung, um zu fragen "Wo ist diese Website?" – oft geleitet über den Router zu externen Resolvern.

Wenn Sie eine bestimmte Konfiguration problembeheben, teilen Sie weitere Details wie Ihr Routermodel oder die genaue Fehlermeldung mit!