---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von zwei Routern
translated: true
type: note
---

Um Ihre beiden TP-Link AX3000 (TL-XDR 3050) Router mit Ihrem Modem in der Konfiguration **Modem → Kabel → Router1 → Drahtlos → Router2** einzurichten, folgen Sie dieser Schritt-für-Schritt-Anleitung. Ihr Modem verfügt bereits über WLAN-Funktionalität und eine IP-Adresse von `192.168.1.1`. Wir konfigurieren Router1 als Hauptrouter, der per Kabel mit dem Modem verbunden ist, und Router2, um das Netzwerk drahtlos zu erweitern.

So gehen Sie vor:

---

### **Schritt 1: Verstehen Sie den Aufbau**
- **Modem**: Bietet Internetzugang und hat ein eigenes WLAN (IP: `192.168.1.1`).
- **Router1**: Wird per Kabel mit dem Modem verbunden und fungiert als primärer Router für Ihr Netzwerk.
- **Router2**: Wird drahtlos mit Router1 verbunden, um die Netzwerkabdeckung zu erweitern.

Sie haben mehrere Modi erwähnt (Wired AP Bridge, Wireless AP Bridge, DHCP, Broadband Connect). Wir verwenden **DHCP** für Router1, um eine Internetverbindung vom Modem zu erhalten, und **Wireless AP Bridge** (oder einen ähnlichen Modus wie WDS/Repeater) für Router2, um sich drahtlos mit Router1 zu verbinden.

---

### **Schritt 2: Richten Sie Router1 ein**
1. **Verbinden Sie Router1 mit dem Modem**:
   - Nehmen Sie ein Ethernet-Kabel und stecken Sie ein Ende in einen **LAN-Port** Ihres Modems.
   - Stecken Sie das andere Ende in den **WAN (Internet)-Port** an Router1.

2. **Greifen Sie auf die Web-Oberfläche von Router1 zu**:
   - Verbinden Sie einen Computer oder ein Smartphone mit dem Standard-WLAN-Netzwerk von Router1 (überprüfen Sie das Etikett am Router für die Standard-SSID und das Passwort) oder verwenden Sie ein Ethernet-Kabel.
   - Öffnen Sie einen Webbrowser und geben Sie `http://tplinkwifi.net` oder `192.168.0.1` ein (die Standard-IP für TP-Link Router).
   - Melden Sie sich mit den Standard-Anmeldedaten an (normalerweise `admin` für Benutzername und Passwort), es sei denn, Sie haben diese geändert.

3. **Konfigurieren Sie Router1**:
   - **Internetverbindung**:
     - Gehen Sie zu **Quick Setup** oder den **Internet**-Einstellungen.
     - Wählen Sie den **DHCP**-Modus. Dies ermöglicht es Router1, automatisch eine IP-Adresse vom Modem zu beziehen (wahrscheinlich im Bereich `192.168.1.x`).
   - **WLAN-Einstellungen**:
     - Vergeben Sie eine eindeutige **SSID** (Netzwerkname) und ein starkes **Passwort** für das WLAN von Router1.
     - Speichern Sie diese Daten, da Router2 sie für die drahtlose Verbindung benötigt.
   - **LAN-Einstellungen**:
     - Stellen Sie sicher, dass die LAN-IP von Router1 sich von der IP des Modems unterscheidet. Standardmäßig ist sie wahrscheinlich `192.168.0.1`, was in Ordnung ist, da das Modem `192.168.1.1` verwendet.
     - Bestätigen Sie, dass **DHCP** auf Router1 aktiviert ist. Dies ermöglicht es Router1, IP-Adressen (z.B. `192.168.0.x`) an verbundene Geräte, einschließlich Router2, zu vergeben.
   - Speichern Sie die Einstellungen und starten Sie Router1 bei Aufforderung neu.

---

### **Schritt 3: Richten Sie Router2 als Wireless Bridge ein**
1. **Greifen Sie auf die Web-Oberfläche von Router2 zu**:
   - Verbinden Sie einen Computer oder ein Smartphone mit dem Standard-WLAN-Netzwerk von Router2 oder per Ethernet.
   - Öffnen Sie einen Webbrowser und geben Sie `http://tplinkwifi.net` oder `192.168.0.1` ein.
   - Melden Sie sich mit den Standard-Anmeldedaten (oder Ihren benutzerdefinierten) an.

2. **Konfigurieren Sie Router2 im Wireless Bridge-Modus**:
   - Suchen Sie nach einem Modus wie **Wireless AP Bridge**, **WDS** oder **Repeater** in den Einstellungen (wahrscheinlich unter **Operation Mode** oder **Wireless**-Einstellungen).
   - Wählen Sie **Wireless AP Bridge** (oder WDS/Repeater, falls verfügbar).
   - **Verbinden Sie sich mit dem WLAN von Router1**:
     - Scannen Sie nach verfügbaren Netzwerken und wählen Sie die SSID von Router1 aus.
     - Geben Sie das WLAN-Passwort von Router1 ein.
     - Stellen Sie sicher, dass Router2 den gleichen WLAN-Kanal wie Router1 für Kompatibilität verwendet (z.B. wenn Router1 auf Kanal 6 ist, setzen Sie Router2 auch auf Kanal 6).
   - **LAN-IP-Einstellung**:
     - Ändern Sie die LAN-IP von Router2, um Konflikte mit Router1 zu vermeiden. Setzen Sie sie z.B. auf `192.168.0.2` (da Router1 wahrscheinlich `192.168.0.1` ist).
     - **Deaktivieren Sie DHCP** auf Router2. Router1 übernimmt die IP-Vergabe für alle Geräte.
   - Speichern Sie die Einstellungen und starten Sie Router2 neu. Er sollte sich nun drahtlos mit Router1 verbinden.

---

### **Schritt 4: Testen Sie das Setup**
1. **Überprüfen Sie die Verbindung von Router2**:
   - Überprüfen Sie nach dem Neustart die Oberfläche von Router2, um zu bestätigen, dass er mit dem WLAN von Router1 verbunden ist.
2. **Verbinden Sie ein Gerät mit Router2**:
   - Verwenden Sie ein Smartphone, Laptop oder anderes Gerät, um sich mit dem WLAN von Router2 zu verbinden (je nach Modus kann es die gleiche SSID wie Router1 verwenden).
   - Überprüfen Sie, ob das Gerät eine IP-Adresse von Router1 erhält (z.B. `192.168.0.x`).
   - Testen Sie den Internetzugang, indem Sie eine Website aufrufen.

---

### **Zusammenfassung der endgültigen Konfiguration**
- **Modem**: IP `192.168.1.1`, stellt Internet und WLAN bereit.
- **Router1**:
  - WAN: Verbunden mit Modem per Kabel, auf **DHCP** gesetzt (erhält IP vom Modem, z.B. `192.168.1.x`).
  - LAN: IP `192.168.0.1`, **DHCP aktiviert**, um IPs an Geräte zu vergeben.
  - WLAN: Benutzerdefinierte SSID und Passwort.
- **Router2**:
  - Modus: **Wireless AP Bridge** (oder WDS/Repeater), drahtlos verbunden mit dem WLAN von Router1.
  - LAN-IP: `192.168.0.2`, **DHCP deaktiviert**.

---

### **Tipps zur Fehlerbehebung**
- **Router2 verbindet sich nicht drahtlos**:
  - Überprüfen Sie nochmals die SSID, das Passwort und die Kanaleinstellungen von Router1 in der Konfiguration von Router2.
  - Wenn **Wireless AP Bridge** nicht verfügbar ist, versuchen Sie es mit **WDS** oder **Repeater**-Modus. Konsultieren Sie das Handbuch des TP-Link AX3000 für unterstützte Modi.
- **Kein Internet auf Router2**:
  - Stellen Sie sicher, dass das DHCP von Router1 funktioniert und das DHCP von Router2 ausgeschaltet ist.
  - Verifizieren Sie, dass Router2 erfolgreich eine Bridge zu Router1 herstellt.
- **Bedenken bezüglich Double NAT**:
  - Da Ihr Modem WLAN hat und Router1 als Router fungiert, könnten Sie Double NAT haben (Modem und Router1 vergeben beide IPs). Dies ist für die grundlegende Nutzung normalerweise in Ordnung, könnte aber einige Anwendungen beeinflussen (z.B. Gaming). Stellen Sie bei Bedarf das Modem auf **Bridge-Modus** (konsultieren Sie das Handbuch Ihres Modems), dies könnte jedoch sein WLAN deaktivieren.

Mit diesem Setup erweitert Router2 Ihr Netzwerk drahtlos von Router1 aus, und Geräte, die mit einem der Router verbunden sind, sollten über das Modem auf das Internet zugreifen können. Lassen Sie mich wissen, wenn Sie weitere Hilfe benötigen!

---

Wenn Sie sich entscheiden, für den ersten Router (Router1) eine feste (statische) IP-Adresse zu verwenden, anstatt sich auf DHCP zu verlassen, müssen Sie seine WAN-Einstellungen manuell konfigurieren, um mit Ihrem Modem zu kommunizieren. Hier ist, was Sie für die IP-Adresse, DNS, Subnetzmaske und Gateway konfigurieren sollten:

---

### **Annahmen**
- Ihr Modem hat eine IP-Adresse von `192.168.1.1` und verwendet das Subnetz `192.168.1.0/24` (Subnetzmaske `255.255.255.0`).
- Das Modem hat einen DHCP-Bereich (z.B. `192.168.1.2` bis `192.168.1.100`), der IP-Adressen an verbundene Geräte vergibt.

Wenn Ihr Modem eine andere IP oder ein anderes Subnetz verwendet, passen Sie die Werte entsprechend an.

---

### **WAN-Einstellungen für Router1**
Diese Einstellungen konfigurieren, wie Router1 eine Verbindung zum Modem herstellt:

1. **IP-Adresse**
   - Wählen Sie eine statische IP innerhalb des Subnetzes des Modems (`192.168.1.0/24`), aber **außerhalb des DHCP-Bereichs des Modems**, um Konflikte zu vermeiden.
   - Beispiel: Wenn der DHCP-Bereich des Modems `192.168.1.2` bis `192.168.1.100` ist, können Sie **`192.168.1.101`** verwenden.
   - Dies stellt sicher, dass Router1 eine eindeutige, feste Adresse im Netzwerk des Modems hat.

2. **Subnetzmaske**
   - Setzen Sie diese so, dass sie mit der Subnetzmaske des Modems übereinstimmt, typischerweise **`255.255.255.0`**.
   - Dies definiert den Netzwerkbereich als `192.168.1.0` bis `192.168.1.255`.

3. **Standard-Gateway**
   - Setzen Sie dies auf die IP-Adresse des Modems, also **`192.168.1.1`**.
   - Das Gateway ist das Gerät (Ihr Modem), das Router1 für den Internetzugang verwendet.

4. **DNS-Server**
   - Sie haben zwei Möglichkeiten:
     - Verwenden Sie die IP des Modems: **`192.168.1.1`**. Dies ermöglicht es dem Modem, DNS-Anfragen zu bearbeiten.
     - Verwenden Sie öffentliche DNS-Server: **`8.8.8.8`** (Google) und **`8.8.4.4`** (Google sekundär). Diese sind zuverlässig und oft schneller.
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
- **Überprüfen Sie die Modem-Einstellungen**: Melden Sie sich bei Ihrem Modem an (normalerweise unter `192.168.1.1`), um dessen IP, Subnetzmaske und DHCP-Bereich zu bestätigen. Passen Sie die statische IP von Router1 bei Bedarf an.
- **LAN-Einstellungen für Router1**: Um Konflikte zu vermeiden, konfigurieren Sie das LAN-Netzwerk von Router1 auf einem anderen Subnetz, z.B. `192.168.0.1` mit einer Subnetzmaske von `255.255.255.0`. Aktivieren Sie DHCP auf Router1, um IPs (z.B. `192.168.0.2` bis `192.168.0.254`) an verbundene Geräte zu vergeben.
- **Testen**: Stellen Sie nach dem Anwenden dieser Einstellungen sicher, dass Router1 auf das Internet zugreifen kann. Wenn nicht, überprüfen Sie nochmals die IP (keine Konflikte), das Gateway und die DNS-Werte.

Diese Konfiguration gibt Router1 eine feste IP im Netzwerk des Modems und gewährleistet eine konsistente Konnektivität. Lassen Sie mich wissen, wenn Sie Hilfe mit zusätzlichen Routern oder spezifischen Modem-Details benötigen!

---

Es klingt so, als hätten Sie Router1 mit einer statischen WAN-IP eingerichtet und sein LAN mit DHCP konfiguriert, aber Ihr Laptop kann immer noch keine Verbindung zum Netzwerk herstellen. Lassen Sie uns das Schritt für Schritt zur Fehlerbehebung angehen, um herauszufinden, warum und wie es zu beheben ist.

---

### Schritt 1: Überprüfen Sie die WAN-Verbindung von Router1
Ihre WAN-Einstellungen sind:

- **IP-Adresse**: `192.168.1.101`
- **Subnetzmaske**: `255.255.255.0`
- **Standard-Gateway**: `192.168.1.1`
- **DNS-Server**: `192.168.1.1` (oder `8.8.8.8` und `8.8.4.4`)

Diese Einstellungen deuten darauf hin, dass Router1 mit einem Modem oder einem anderen Router mit der IP `192.168.1.1` verbunden ist. Hier ist, was zu überprüfen ist:

- **Internetzugang auf Router1**:
  - Melden Sie sich bei der Web-Oberfläche von Router1 an (wahrscheinlich unter `192.168.0.1` gemäß Ihren LAN-Einstellungen unten).
  - Gehen Sie zum **Status** oder **WAN**-Bereich, um zu sehen, ob Router1 eine aktive Internetverbindung anzeigt. Wenn nicht, könnte das Problem zwischen Router1 und dem Modem liegen.

- **IP-Konflikt**:
  - Stellen Sie sicher, dass kein anderes Gerät im Netzwerk des Modems `192.168.1.101` verwendet. Wenn der DHCP-Bereich des Modems diese IP enthält, könnte dies einen Konflikt verursachen. Melden Sie sich beim Modem an (unter `192.168.1.1`) und überprüfen Sie dessen DHCP-Einstellungen oder die Liste der verbundenen Geräte. Wenn `192.168.1.101` innerhalb des DHCP-Bereichs des Modems liegt, ändern Sie entweder die WAN-IP von Router1 auf etwas außerhalb dieses Bereichs (z.B. `192.168.1.200`) oder schließen Sie sie aus dem DHCP-Pool des Modems aus.

- **Modem-Konnektivität**:
  - Bestätigen Sie, dass das Ethernet-Kabel in den **LAN-Port** des Modems und den **WAN-Port** von Router1 eingesteckt ist. Wenn dies nicht korrekt eingerichtet ist, kann Router1 keine Verbindung zum Internet herstellen.

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
  - Wenn der DNS-Server auf `192.168.0.1` gesetzt ist, bedeutet dies, dass Router1 DNS-Anfragen für Ihren Laptop bearbeitet. Stellen Sie sicher, dass Router1 konfiguriert ist, diese Anfragen an einen Upstream-DNS-Server (wie `192.168.1.1` oder `8.8.8.8`) weiterzuleiten. Dies ist normalerweise automatisch, aber überprüfen Sie es dennoch in den Einstellungen von Router1. Alternativ könnten Sie den DHCP-DNS direkt auf `8.8.8.8` und `8.8.4.4` setzen, um Router1 für DNS zu umgehen.

---

### Schritt 3: Testen Sie die Verbindung Ihres Laptops
Da Ihr Laptop keine Verbindung herstellt, diagnostizieren wir das:

- **Verbindungstyp**:
  - Verwenden Sie WLAN oder Ethernet? Wenn WLAN, stellen Sie sicher, dass Sie sich mit der SSID von Router1 verbinden (nicht mit der des Modems). Wenn Ethernet, bestätigen Sie, dass das Kabel in einen der LAN-Ports von Router1 eingesteckt ist.

- **Überprüfen Sie die IP-Adresse des Laptops**:
  - Öffnen Sie auf Ihrem Laptop eine **Eingabeaufforderung** (Windows) oder ein **Terminal** (macOS/Linux):
    - Windows: Geben Sie `ipconfig` ein und drücken Sie Enter.
    - macOS/Linux: Geben Sie `ifconfig` oder `ip addr` ein und drücken Sie Enter.
  - Suchen Sie nach der IP-Adresse Ihres Netzwerkadapters. Es sollte etwas wie `192.168.0.x` sein (wobei `x` zwischen 2 und 254 liegt), mit einer Subnetzmaske von `255.255.255.0` und einem Gateway `192.168.0.1`.
  - **Wenn keine IP-Adresse**:
    - Ihr Laptop erhält möglicherweise keine IP von DHCP. Stellen Sie sicher, dass seine Netzwerkeinstellungen auf "IP-Adresse automatisch beziehen" eingestellt sind. Versuchen Sie, die IP zu erneuern:
      - Windows: Führen Sie `ipconfig /release` und dann `ipconfig /renew` aus.
    - Wenn es weiterhin fehlschlägt, könnte das DHCP auf Router1 oder die Verbindung zu ihm das Problem sein.

- **Pingen Sie Router1**:
  - Führen Sie von Ihrem Laptop `ping 192.168.0.1` aus. Wenn Sie Antworten erhalten, ist Ihr Laptop mit Router1 verbunden, hat aber möglicherweise keinen Internetzugang. Wenn es timeouts gibt, erreicht der Laptop Router1 nicht.

---

### Schritt 4: Häufige Probleme und Lösungen
Hier sind einige wahrscheinliche Ursachen:

- **Kabelprobleme**:
  - Wenn Sie Ethernet verwenden, versuchen Sie ein anderes Kabel oder einen anderen LAN-Port an Router1. Ein defektes Kabel oder ein defekter Port könnte die Konnektivität verhindern.

- **WLAN-Probleme**:
  - Wenn Sie WLAN verwenden, überprüfen Sie nochmals das Passwort und stellen Sie sicher, dass das WLAN von Router1 aktiviert ist. Signalstörungen oder eine falsch konfigurierte SSID könnten ebenfalls das Problem sein.

- **Router1-Modem-Verbindung**:
  - Wenn Router1 keine Internetverbindung erhält, könnte das Modem bestimmte Einstellungen erfordern (z.B. MAC-Adressen-Cloning). Überprüfen Sie das Handbuch oder die Einstellungen des Modems hierfür.

- **Double NAT**:
  - Ihr Setup hat das Modem (bei `192.168.1.1`) und Router1 (bei `192.168.0.1`), die beide als Router fungieren. Dies sollte die grundlegende Konnektivität nicht blockieren, aber das Setzen des Modems auf **Bridge-Modus** (falls möglich) könnte die Dinge vereinfachen.

- **Firewall**:
  - Die Firewall von Router1 könnte Ihren Laptop blockieren. Deaktivieren Sie temporär alle benutzerdefinierten Firewall-Regeln zum Testen.

---

### Schritt 5: Setzen Sie bei Bedarf zurück
Wenn nichts funktioniert, setzen Sie Router1 zurück und konfigurieren Sie ihn neu:

- **Werksreset**:
  - Drücken und halten Sie die Reset-Taste von Router1 für 10 Sekunden, dann richten Sie die WAN- und DHCP-Einstellungen erneut ein, wie Sie sie aufgelistet haben.

- **Versuchen Sie dynamisches WAN**:
  - Verwenden Sie anstelle einer statischen WAN-IP **DHCP** für Router1s WAN, um zu sehen, ob es automatisch eine IP vom Modem beziehen kann. Wenn dies funktioniert, könnte die statische IP (`192.168.1.101`) das Problem sein.

---

### Abschließende Tipps
- **Modem DHCP-Bereich**: Bestätigen Sie, dass `192.168.1.101` außerhalb des DHCP-Bereichs des Modems liegt, um Konflikte zu vermeiden.
- **Firmware**: Überprüfen Sie die Web-Oberfläche von Router1 auf ein Firmware-Update.
- **Laptop-Treiber**: Stellen Sie sicher, dass die Treiber des Netzwerkadapters Ihres Laptops auf dem neuesten Stand sind.

Befolgen Sie diese Schritte, und Sie sollten den Grund eingrenzen, warum Ihr Laptop keine Verbindung herstellt. Wenn Sie immer noch nicht weiterkommen, lassen Sie mich wissen, was Sie in jedem Schritt feststellen – ich helfe Ihnen, es weiter einzugrenzen!