---
audio: true
generated: true
lang: de
layout: post
title: Zwei Router verwenden
translated: true
---

Um Ihre beiden TP-Link AX3000 (TL-XDR 3050) Router mit Ihrem Modem in der Konfiguration **Modem → Kabel → Router1 → Wireless → Router2** einzurichten, folgen Sie dieser Schritt-für-Schritt-Anleitung. Ihr Modem verfügt bereits über WiFi-Funktionalität und eine IP-Adresse von `192.168.1.1`. Wir konfigurieren Router1 als Hauptrouter, der über ein Kabel mit dem Modem verbunden ist, und Router2, um das Netzwerk drahtlos zu erweitern.

Hier ist, wie Sie dies erreichen:

---

### **Schritt 1: Verstehen der Einrichtung**
- **Modem**: Bietet Internetzugang und hat sein eigenes WiFi (IP: `192.168.1.1`).
- **Router1**: Wird mit einem Kabel mit dem Modem verbunden und fungiert als primärer Router für Ihr Netzwerk.
- **Router2**: Wird drahtlos mit Router1 verbunden, um die Netzwerkabdeckung zu erweitern.

Sie haben mehrere Modi erwähnt (Wired AP Bridge, Wireless AP Bridge, DHCP, Broadband Connect). Wir werden **DHCP** für Router1 verwenden, um eine Internetverbindung vom Modem zu erhalten, und **Wireless AP Bridge** (oder einen ähnlichen Modus wie WDS/Repeater) für Router2, um sich drahtlos mit Router1 zu verbinden.

---

### **Schritt 2: Einrichtung von Router1**
1. **Verbindung von Router1 mit dem Modem**:
   - Nehmen Sie ein Ethernet-Kabel und stecken Sie ein Ende in einen **LAN-Port** Ihres Modems.
   - Stecken Sie das andere Ende in den **WAN (Internet)-Port** von Router1.

2. **Zugang zur Web-Oberfläche von Router1**:
   - Verbinden Sie einen Computer oder ein Smartphone mit dem Standard-WiFi-Netzwerk von Router1 (überprüfen Sie das Etikett auf dem Router für die Standard-SSID und das Passwort) oder verwenden Sie ein Ethernet-Kabel.
   - Öffnen Sie einen Webbrowser und geben Sie `http://tplinkwifi.net` oder `192.168.0.1` (die Standard-IP für TP-Link-Router) ein.
   - Melden Sie sich mit den Standard-Anmeldeinformationen an (normalerweise `admin` für beide Benutzername und Passwort), es sei denn, Sie haben diese geändert.

3. **Konfiguration von Router1**:
   - **Internetverbindung**:
     - Gehen Sie zu **Quick Setup** oder dem Abschnitt **Internet** der Einstellungen.
     - Wählen Sie **DHCP**-Modus. Dies ermöglicht es Router1, automatisch eine IP-Adresse vom Modem zu erhalten (wahrscheinlich im Bereich `192.168.1.x`).
   - **WiFi-Einstellungen**:
     - Legen Sie eine eindeutige **SSID** (Netzwerkname) und ein starkes **Passwort** für das WiFi von Router1 fest.
     - Speichern Sie diese Details, da Router2 sie benötigen wird, um sich drahtlos zu verbinden.
   - **LAN-Einstellungen**:
     - Stellen Sie sicher, dass die LAN-IP von Router1 sich von der IP des Modems unterscheidet. Standardmäßig ist es wahrscheinlich `192.168.0.1`, was in Ordnung ist, da das Modem `192.168.1.1` ist.
     - Bestätigen Sie, dass **DHCP** auf Router1 aktiviert ist. Dies ermöglicht es Router1, IP-Adressen (z.B. `192.168.0.x`) an Geräte zuzuweisen, die mit ihm verbunden sind, einschließlich Router2.
   - Speichern Sie die Einstellungen und starten Sie Router1 neu, falls dies erforderlich ist.

---

### **Schritt 3: Einrichtung von Router2 als drahtloser Bridge**
1. **Zugang zur Web-Oberfläche von Router2**:
   - Verbinden Sie einen Computer oder ein Smartphone mit dem Standard-WiFi-Netzwerk von Router2 oder über Ethernet.
   - Öffnen Sie einen Webbrowser und geben Sie `http://tplinkwifi.net` oder `192.168.0.1` ein.
   - Melden Sie sich mit den Standard-Anmeldeinformationen (oder Ihren benutzerdefinierten) an.

2. **Konfiguration von Router2 im Wireless Bridge Modus**:
   - Suchen Sie nach einem Modus wie **Wireless AP Bridge**, **WDS** oder **Repeater** in den Einstellungen (wahrscheinlich unter **Betriebsmodus** oder **Wireless**-Einstellungen).
   - Wählen Sie **Wireless AP Bridge** (oder WDS/Repeater, wenn das verfügbar ist).
   - **Verbindung mit dem WiFi von Router1**:
     - Scannen Sie nach verfügbaren Netzwerken und wählen Sie die SSID von Router1.
     - Geben Sie das WiFi-Passwort von Router1 ein.
     - Stellen Sie sicher, dass Router2 denselben drahtlosen Kanal wie Router1 verwendet (z.B. wenn Router1 auf Kanal 6 ist, setzen Sie Router2 auf Kanal 6).
   - **LAN-IP-Einstellung**:
     - Ändern Sie die LAN-IP von Router2, um Konflikte mit Router1 zu vermeiden. Zum Beispiel können Sie sie auf `192.168.0.2` setzen (da Router1 wahrscheinlich `192.168.0.1` ist).
     - **Deaktivieren Sie DHCP** auf Router2. Router1 wird die IP-Zuweisungen für alle Geräte übernehmen.
   - Speichern Sie die Einstellungen und starten Sie Router2 neu. Er sollte sich nun drahtlos mit Router1 verbinden.

---

### **Schritt 4: Testen der Einrichtung**
1. **Überprüfen Sie die Verbindung von Router2**:
   - Nach dem Neustart überprüfen Sie die Oberfläche von Router2, um sicherzustellen, dass er mit dem WiFi von Router1 verbunden ist.
2. **Verbindung eines Geräts mit Router2**:
   - Verwenden Sie ein Smartphone, Laptop oder ein anderes Gerät, um sich mit dem WiFi von Router2 zu verbinden (es könnte dieselbe SSID wie Router1 verwenden, abhängig vom Modus).
   - Stellen Sie sicher, dass das Gerät eine IP-Adresse von Router1 erhält (z.B. `192.168.0.x`).
   - Testen Sie den Internetzugang, indem Sie eine Website besuchen.

---

### **Abschließende Konfigurationszusammenfassung**
- **Modem**: IP `192.168.1.1`, bietet Internet und WiFi.
- **Router1**:
  - WAN: Mit dem Modem über ein Kabel verbunden, auf **DHCP** eingestellt (erhält IP vom Modem, z.B. `192.168.1.x`).
  - LAN: IP `192.168.0.1`, **DHCP aktiviert**, um IPs an Geräte zuzuweisen.
  - WiFi: Benutzerdefinierte SSID und Passwort.
- **Router2**:
  - Modus: **Wireless AP Bridge** (oder WDS/Repeater), drahtlos mit dem WiFi von Router1 verbunden.
  - LAN-IP: `192.168.0.2`, **DHCP deaktiviert**.

---

### **Fehlerbehebungstipps**
- **Router2 verbindet sich nicht drahtlos**:
  - Überprüfen Sie die SSID, das Passwort und die Kanaleinstellungen von Router1 in der Konfiguration von Router2.
  - Wenn **Wireless AP Bridge** nicht verfügbar ist, versuchen Sie **WDS** oder **Repeater**-Modus. Beziehen Sie sich auf die TP-Link AX3000-Anleitung für unterstützte Modi.
- **Kein Internet auf Router2**:
  - Stellen Sie sicher, dass DHCP auf Router1 funktioniert und DHCP auf Router2 ausgeschaltet ist.
  - Überprüfen Sie, ob Router2 erfolgreich eine Brücke zu Router1 bildet.
- **Doppelte NAT-Bedenken**:
  - Da Ihr Modem WiFi hat und Router1 als Router fungiert, könnten Sie doppelte NAT (Modem und Router1 beide vergeben IPs) haben. Dies ist normalerweise für den grundlegenden Gebrauch in Ordnung, könnte aber einige Anwendungen (z.B. Gaming) beeinträchtigen. Wenn nötig, setzen Sie das Modem in **Bridge-Modus** (konsultieren Sie die Anleitung Ihres Modems), obwohl dies möglicherweise dessen WiFi deaktiviert.

Mit dieser Einrichtung wird Router2 Ihr Netzwerk drahtlos von Router1 erweitern, und Geräte, die mit einem der Router verbunden sind, sollten über das Modem auf das Internet zugreifen. Lassen Sie mich wissen, wenn Sie weitere Hilfe benötigen!

---

Wenn Sie sich entscheiden, eine feste (statische) IP-Adresse für den ersten Router (Router1) anstelle von DHCP zu verwenden, müssen Sie die WAN-Einstellungen von Router1 manuell konfigurieren, um mit Ihrem Modem zu kommunizieren. Hier sind die Einstellungen, die Sie für die IP-Adresse, DNS, Subnetzmaske und Gateway konfigurieren sollten:

---

### **Annahmen**
- Ihr Modem hat eine IP-Adresse von `192.168.1.1` und verwendet das Subnetz `192.168.1.0/24` (Subnetzmaske `255.255.255.0`).
- Das Modem hat einen DHCP-Bereich (z.B. `192.168.1.2` bis `192.168.1.100`), der IP-Adressen an verbundene Geräte zuweist.

Wenn Ihr Modem eine andere IP oder ein anderes Subnetz verwendet, passen Sie die Werte entsprechend an.

---

### **WAN-Einstellungen für Router1**
Diese Einstellungen konfigurieren, wie Router1 sich mit dem Modem verbindet:

1. **IP-Adresse**
   - Wählen Sie eine statische IP innerhalb des Subnetzes des Modems (`192.168.1.0/24`), aber **außerhalb des DHCP-Bereichs des Modems**, um Konflikte zu vermeiden.
   - Beispiel: Wenn der DHCP-Bereich des Modems `192.168.1.2` bis `192.168.1.100` ist, können Sie `192.168.1.101` verwenden.
   - Dies stellt sicher, dass Router1 eine eindeutige, feste Adresse im Netzwerk des Modems hat.

2. **Subnetzmaske**
   - Setzen Sie dies so, dass es mit der Subnetzmaske des Modems übereinstimmt, die normalerweise `255.255.255.0` ist.
   - Dies definiert den Netzwerkbereich als `192.168.1.0` bis `192.168.1.255`.

3. **Standard-Gateway**
   - Setzen Sie dies auf die IP-Adresse des Modems, die `192.168.1.1` ist.
   - Das Gateway ist das Gerät (Ihr Modem), das Router1 verwendet, um auf das Internet zuzugreifen.

4. **DNS-Server**
   - Sie haben zwei Optionen:
     - Verwenden Sie die IP des Modems: `192.168.1.1`. Dies lässt das Modem DNS-Anfragen verarbeiten.
     - Verwenden Sie öffentliche DNS-Server: `8.8.8.8` (Google) und `8.8.4.4` (Google sekundär). Diese sind zuverlässig und oft schneller.
   - Empfehlung: Beginnen Sie mit `192.168.1.1`. Wenn Sie DNS-Probleme haben, wechseln Sie zu `8.8.8.8` und `8.8.4.4`.

---

### **Beispielkonfiguration**
So könnten Ihre WAN-Einstellungen für Router1 aussehen:

- **IP-Adresse**: `192.168.1.101`
- **Subnetzmaske**: `255.255.255.0`
- **Standard-Gateway**: `192.168.1.1`
- **DNS-Server**: `192.168.1.1` (oder `8.8.8.8` und `8.8.4.4`)

---

### **Zusätzliche Hinweise**
- **Überprüfen Sie die Modem-Einstellungen**: Melden Sie sich bei Ihrem Modem (normalerweise unter `192.168.1.1`) an, um seine IP, Subnetzmaske und den DHCP-Bereich zu bestätigen. Passen Sie die statische IP von Router1 bei Bedarf an.
- **LAN-Einstellungen für Router1**: Um Konflikte zu vermeiden, konfigurieren Sie das LAN-Netzwerk von Router1 auf einem anderen Subnetz, wie `192.168.0.1` mit einer Subnetzmaske von `255.255.255.0`. Aktivieren Sie DHCP auf Router1, um IPs (z.B. `192.168.0.2` bis `192.168.0.254`) an Geräte zuzuweisen, die mit ihm verbunden sind.
- **Testen**: Nach dem Anwenden dieser Einstellungen stellen Sie sicher, dass Router1 auf das Internet zugreifen kann. Wenn nicht, überprüfen Sie die IP (keine Konflikte), das Gateway und die DNS-Werte.

Diese Konfiguration gibt Router1 eine feste IP im Netzwerk des Modems, was eine konsistente Konnektivität gewährleistet. Lassen Sie mich wissen, wenn Sie Hilfe bei zusätzlichen Routern oder spezifischen Modem-Details benötigen!

---

Es scheint, dass Sie Router1 mit einer statischen WAN-IP konfiguriert und dessen LAN mit DHCP eingerichtet haben, aber Ihr Laptop kann sich nicht mit dem Netzwerk verbinden. Lassen Sie uns dies Schritt für Schritt diagnostizieren, um herauszufinden, warum und wie es behoben werden kann.

---

### Schritt 1: Überprüfen Sie die WAN-Verbindung von Router1
Ihre WAN-Einstellungen sind:

- **IP-Adresse**: `192.168.1.101`
- **Subnetzmaske**: `255.255.255.0`
- **Standard-Gateway**: `192.168.1.1`
- **DNS-Server**: `192.168.1.1` (oder `8.8.8.8` und `8.8.4.4`)

Diese Einstellungen deuten darauf hin, dass Router1 mit einem Modem oder einem anderen Router mit einer IP von `192.168.1.1` verbunden ist. Hier ist, was Sie überprüfen sollten:

- **Internetzugang auf Router1**:
  - Melden Sie sich in der Web-Oberfläche von Router1 an (wahrscheinlich unter `192.168.0.1` aus Ihren LAN-Einstellungen unten).
  - Gehen Sie zum Abschnitt **Status** oder **WAN**, um zu sehen, ob Router1 eine aktive Internetverbindung anzeigt. Wenn nicht, könnte das Problem zwischen Router1 und dem Modem liegen.

- **IP-Konflikt**:
  - Stellen Sie sicher, dass kein anderes Gerät im Netzwerk des Modems `192.168.1.101` verwendet. Wenn der DHCP-Bereich des Modems diese IP enthält, könnte dies zu einem Konflikt führen. Melden Sie sich beim Modem (unter `192.168.1.1`) an und überprüfen Sie dessen DHCP-Einstellungen oder die Liste der verbundenen Geräte. Wenn `192.168.1.101` im DHCP-Bereich des Modems liegt, ändern Sie die WAN-IP von Router1 in etwas außerhalb dieses Bereichs (z.B. `192.168.1.200`) oder schließen Sie es aus dem DHCP-Pool des Modems aus.

- **Modem-Konnektivität**:
  - Stellen Sie sicher, dass das Ethernet-Kabel in den **LAN-Port** des Modems und den **WAN-Port** von Router1 gesteckt ist. Wenn dies nicht korrekt eingerichtet ist, wird Router1 keine Internetverbindung haben.

---

### Schritt 2: Überprüfen Sie die LAN- und DHCP-Einstellungen von Router1
Ihre LAN- und DHCP-Einstellungen sind:

- **LAN-IP**: `192.168.0.1`
- **Subnetzmaske**: `255.255.255.0`
- **DHCP aktiviert**: Ja
- **IP-Adressbereich**: `192.168.0.2` bis `192.168.0.254`
- **Gateway**: `192.168.0.1`
- **DNS-Server**: `192.168.0.1`

Diese sehen solide aus, aber lassen Sie uns sicherstellen, dass sie funktionieren:

- **DHCP-Funktionalität**:
  - Mit aktiviertem DHCP sollte Ihr Laptop automatisch eine IP-Adresse zwischen `192.168.0.2` und `192.168.0.254` mit einem Gateway von `192.168.0.1` erhalten. Wenn nicht, funktioniert DHCP möglicherweise nicht richtig.

- **DNS-Konfiguration**:
  - Durch das Setzen des DNS-Servers auf `192.168.0.1` wird Router1 DNS-Anfragen für Ihren Laptop verarbeiten. Stellen Sie sicher, dass Router1 so konfiguriert ist, dass er diese Anfragen an einen übergeordneten DNS-Server (wie `192.168.1.1` oder `8.8.8.8`) weiterleitet. Dies ist normalerweise automatisch, aber überprüfen Sie es in den Einstellungen von Router1. Alternativ könnten Sie den DHCP-DNS direkt auf `8.8.8.8` und `8.8.4.4` setzen, um Router1 für DNS zu umgehen.

---

### Schritt 3: Testen Sie die Verbindung Ihres Laptops
Da Ihr Laptop sich nicht verbindet, lassen Sie uns dies diagnostizieren:

- **Verbindungstyp**:
  - Verwenden Sie WiFi oder Ethernet? Wenn WiFi, stellen Sie sicher, dass Sie sich mit der SSID von Router1 (nicht dem Modem) verbinden. Wenn Ethernet, stellen Sie sicher, dass das Kabel in einen der LAN-Ports von Router1 gesteckt ist.

- **Überprüfen Sie die IP-Adresse Ihres Laptops**:
  - Öffnen Sie eine **Eingabeaufforderung** (Windows) oder **Terminal** (macOS/Linux):
    - Windows: Geben Sie `ipconfig` ein und drücken Sie die Eingabetaste.
    - macOS/Linux: Geben Sie `ifconfig` oder `ip addr` ein und drücken Sie die Eingabetaste.
  - Suchen Sie nach der IP-Adresse Ihres Netzwerkadapters. Sie sollte etwas wie `192.168.0.x` (wobei `x` zwischen 2 und 254 liegt) mit einer Subnetzmaske von `255.255.255.0` und einem Gateway von `192.168.0.1` sein.
  - **Wenn keine IP-Adresse**:
    - Ihr Laptop könnte keine IP von DHCP erhalten. Stellen Sie sicher, dass die Netzwerkeinstellungen Ihres Laptops auf „IP-Adresse automatisch erhalten“ gesetzt sind. Versuchen Sie, die IP neu zuzuweisen:
      - Windows: Führen Sie `ipconfig /release` und dann `ipconfig /renew` aus.
    - Wenn es weiterhin fehlschlägt, könnte DHCP auf Router1 oder die Verbindung zu ihm das Problem sein.

- **Ping Router1**:
  - Von Ihrem Laptop aus führen Sie `ping 192.168.0.1` aus. Wenn Sie Antworten erhalten, ist Ihr Laptop mit Router1 verbunden, hat aber möglicherweise keinen Internetzugang. Wenn es zeitlich abgelaufen ist, erreicht Ihr Laptop Router1 nicht.

---

### Schritt 4: Häufige Probleme und Lösungen
Hier sind einige wahrscheinlich Ursachen:

- **Kabelprobleme**:
  - Wenn Sie Ethernet verwenden, versuchen Sie ein anderes Kabel oder einen anderen LAN-Port auf Router1. Ein defektes Kabel oder ein defekter Port könnte die Konnektivität verhindern.

- **WiFi-Probleme**:
  - Wenn Sie WiFi verwenden, überprüfen Sie das Passwort und stellen Sie sicher, dass das WiFi von Router1 aktiviert ist. Signalstörungen oder eine falsch konfigurierte SSID könnten ebenfalls das Problem sein.

- **Verbindung Router1-Modem**:
  - Wenn Router1 keine Internetverbindung hat, könnte das Modem spezifische Einstellungen (z.B. MAC-Adressklonung) erfordern. Überprüfen Sie die Anleitung oder Einstellungen Ihres Modems dafür.

- **Doppelte NAT**:
  - Ihre Einrichtung hat das Modem (bei `192.168.1.1`) und Router1 (bei `192.168.0.1`), die beide als Router fungieren. Dies sollte die grundlegende Konnektivität nicht blockieren, aber das Setzen des Modems in **Bridge-Modus** (falls möglich) könnte die Dinge vereinfachen.

- **Firewall**:
  - Die Firewall von Router1 könnte Ihren Laptop blockieren. Deaktivieren Sie vorübergehend alle benutzerdefinierten Firewall-Regeln, um dies zu testen.

---

### Schritt 5: Zurücksetzen, falls erforderlich
Wenn nichts funktioniert, setzen Sie Router1 zurück und konfigurieren Sie ihn neu:

- **Werkseinstellungen**:
  - Drücken Sie die Reset-Taste von Router1 für 10 Sekunden und konfigurieren Sie dann die WAN- und DHCP-Einstellungen erneut, wie Sie sie angegeben haben.

- **Versuchen Sie dynamische WAN**:
  - Anstelle einer statischen WAN-IP setzen Sie Router1s WAN auf **DHCP**, um zu sehen, ob er eine IP vom Modem automatisch erhalten kann. Wenn dies funktioniert, könnte die statische IP (`192.168.1.101`) das Problem sein.

---

### Abschlusshinweise
- **DHCP-Bereich des Modems**: Stellen Sie sicher, dass `192.168.1.101` außerhalb des DHCP-Bereichs des Modems liegt, um Konflikte zu vermeiden.
- **Firmware**: Überprüfen Sie die Web-Oberfläche von Router1 auf ein Firmware-Update.
- **Laptop-Treiber**: Stellen Sie sicher, dass die Treiber Ihres Laptop-Netzwerkadapters auf dem neuesten Stand sind.

Folgen Sie diesen Schritten, und Sie sollten herausfinden, warum Ihr Laptop sich nicht verbindet. Wenn Sie immer noch feststecken, lassen Sie mich wissen, was Sie bei jedem Schritt finden – ich werde Ihnen helfen, es weiter einzuschränken!