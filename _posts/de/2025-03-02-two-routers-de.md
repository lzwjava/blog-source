---
audio: false
lang: de
layout: post
title: Zwei Router verwenden
translated: true
---

Um Ihre beiden TP-Link AX3000 (TL-XDR 3050) Router mit Ihrem Modem in der Konfiguration **Modem → Kabel → Router1 → Wireless → Router2** einzurichten, folgen Sie dieser Schritt-für-Schritt-Anleitung. Ihr Modem hat bereits WiFi-Funktionalität und eine IP-Adresse von `192.168.1.1`. Wir konfigurieren Router1 als Hauptrouter, der über ein Kabel mit dem Modem verbunden ist, und Router2, um das Netzwerk drahtlos zu erweitern.

Hier ist, wie Sie dies erreichen:

---

### **Schritt 1: Setup verstehen**
- **Modem**: Bietet Internetzugang und hat eigenes WiFi (IP: `192.168.1.1`).
- **Router1**: Wird über ein Kabel mit dem Modem verbunden und dient als primärer Router für Ihr Netzwerk.
- **Router2**: Wird drahtlos mit Router1 verbunden, um die Netzwerkabdeckung zu erweitern.

Sie haben mehrere Modi erwähnt (Wired AP Bridge, Wireless AP Bridge, DHCP, Broadband Connect). Wir werden **DHCP** für Router1 verwenden, um eine Internetverbindung vom Modem zu erhalten, und **Wireless AP Bridge** (oder einen ähnlichen Modus wie WDS/Repeater) für Router2, um sich drahtlos mit Router1 zu verbinden.

---

### **Schritt 2: Router1 einrichten**
1. **Router1 mit dem Modem verbinden**:
   - Nehmen Sie ein Ethernet-Kabel und stecken Sie ein Ende in einen **LAN-Port** Ihres Modems.
   - Stecken Sie das andere Ende in den **WAN (Internet)-Port** von Router1.

2. **Auf die Web-Oberfläche von Router1 zugreifen**:
   - Verbinden Sie einen Computer oder ein Smartphone mit dem Standard-WiFi-Netzwerk von Router1 (überprüfen Sie das Etikett auf dem Router für die Standard-SSID und das Passwort) oder verwenden Sie ein Ethernet-Kabel.
   - Öffnen Sie einen Webbrowser und geben Sie `http://tplinkwifi.net` oder `192.168.0.1` (die Standard-IP für TP-Link-Router) ein.
   - Melden Sie sich mit den Standard-Anmeldeinformationen an (normalerweise `admin` für beide Benutzername und Passwort), es sei denn, Sie haben diese geändert.

3. **Router1 konfigurieren**:
   - **Internetverbindung**:
     - Gehen Sie zu **Quick Setup** oder dem Abschnitt **Internet** Einstellungen.
     - Wählen Sie den **DHCP**-Modus aus. Dies ermöglicht es Router1, automatisch eine IP-Adresse vom Modem zu erhalten (wahrscheinlich im Bereich `192.168.1.x`).
   - **WiFi-Einstellungen**:
     - Legen Sie eine eindeutige **SSID** (Netzwerkname) und ein starkes **Passwort** für das WiFi von Router1 fest.
     - Speichern Sie diese Details, da Router2 sie benötigt, um sich drahtlos zu verbinden.
   - **LAN-Einstellungen**:
     - Stellen Sie sicher, dass die LAN-IP von Router1 sich von der IP des Modems unterscheidet. Standardmäßig ist es wahrscheinlich `192.168.0.1`, was in Ordnung ist, da das Modem `192.168.1.1` ist.
     - Stellen Sie sicher, dass **DHCP** auf Router1 aktiviert ist. Dies ermöglicht es Router1, IP-Adressen (z.B. `192.168.0.x`) an Geräte zuzuweisen, die mit ihm verbunden sind, einschließlich Router2.
   - Speichern Sie die Einstellungen und starten Sie Router1 neu, falls dies angefordert wird.

---

### **Schritt 3: Router2 als drahtlosen Bridge einrichten**
1. **Auf die Web-Oberfläche von Router2 zugreifen**:
   - Verbinden Sie einen Computer oder ein Smartphone mit dem Standard-WiFi-Netzwerk von Router2 oder über Ethernet.
   - Öffnen Sie einen Webbrowser und geben Sie `http://tplinkwifi.net` oder `192.168.0.1` ein.
   - Melden Sie sich mit den Standard-Anmeldeinformationen (oder Ihren benutzerdefinierten) an.

2. **Router2 im Wireless Bridge Modus konfigurieren**:
   - Suchen Sie nach einem Modus wie **Wireless AP Bridge**, **WDS** oder **Repeater** in den Einstellungen (wahrscheinlich unter **Operation Mode** oder **Wireless** Einstellungen).
   - Wählen Sie **Wireless AP Bridge** (oder WDS/Repeater, falls verfügbar).
   - **Mit Router1s WiFi verbinden**:
     - Scannen Sie nach verfügbaren Netzwerken und wählen Sie die SSID von Router1 aus.
     - Geben Sie das WiFi-Passwort von Router1 ein.
     - Stellen Sie sicher, dass Router2 denselben drahtlosen Kanal wie Router1 verwendet (z.B. wenn Router1 auf Kanal 6 ist, setzen Sie Router2 auf Kanal 6).
   - **LAN-IP-Einstellung**:
     - Ändern Sie die LAN-IP von Router2, um Konflikte mit Router1 zu vermeiden. Zum Beispiel auf `192.168.0.2` (da Router1 wahrscheinlich `192.168.0.1` ist).
     - **Deaktivieren Sie DHCP** auf Router2. Router1 wird die IP-Zuweisungen für alle Geräte übernehmen.
   - Speichern Sie die Einstellungen und starten Sie Router2 neu. Er sollte sich nun drahtlos mit Router1 verbinden.

---

### **Schritt 4: Setup testen**
1. **Router2-Verbindung überprüfen**:
   - Nach dem Neustart überprüfen Sie die Oberfläche von Router2, um sicherzustellen, dass er mit dem WiFi von Router1 verbunden ist.
2. **Gerät mit Router2 verbinden**:
   - Verwenden Sie ein Smartphone, Laptop oder ein anderes Gerät, um sich mit dem WiFi von Router2 zu verbinden (es könnte dieselbe SSID wie Router1 verwenden, abhängig vom Modus).
   - Stellen Sie sicher, dass das Gerät eine IP-Adresse von Router1 erhält (z.B. `192.168.0.x`).
   - Testen Sie den Internetzugang, indem Sie eine Website aufrufen.

---

### **Abschließende Konfigurationszusammenfassung**
- **Modem**: IP `192.168.1.1`, bietet Internet und WiFi.
- **Router1**:
  - WAN: Mit dem Modem über Kabel verbunden, auf **DHCP** gesetzt (erhält IP vom Modem, z.B. `192.168.1.x`).
  - LAN: IP `192.168.0.1`, **DHCP aktiviert** zur IP-Zuweisung an Geräte.
  - WiFi: Benutzerdefinierte SSID und Passwort.
- **Router2**:
  - Modus: **Wireless AP Bridge** (oder WDS/Repeater), drahtlos mit Router1s WiFi verbunden.
  - LAN-IP: `192.168.0.2`, **DHCP deaktiviert**.

---

### **Fehlerbehebungstipps**
- **Router2 verbindet sich nicht drahtlos**:
  - Überprüfen Sie doppelt die SSID, das Passwort und die Kanaleinstellungen von Router1 in der Konfiguration von Router2.
  - Wenn **Wireless AP Bridge** nicht verfügbar ist, versuchen Sie **WDS** oder **Repeater** Modus. Beziehen Sie sich auf die TP-Link AX3000 Anleitung für unterstützte Modi.
- **Kein Internet auf Router2**:
  - Stellen Sie sicher, dass DHCP auf Router1 funktioniert und DHCP auf Router2 deaktiviert ist.
  - Überprüfen Sie, ob Router2 erfolgreich eine Brücke zu Router1 bildet.
- **Doppelte NAT-Bedenken**:
  - Da Ihr Modem WiFi hat und Router1 als Router fungiert, könnten Sie doppelte NAT haben (Modem und Router1 beide vergeben IPs). Dies ist normalerweise für den grundlegenden Gebrauch in Ordnung, könnte aber einige Anwendungen (z.B. Gaming) beeinträchtigen. Wenn nötig, setzen Sie das Modem in **Bridge-Modus** (konsultieren Sie die Anleitung Ihres Modems), dies könnte jedoch dessen WiFi deaktivieren.

Mit dieser Einrichtung wird Router2 das Netzwerk drahtlos von Router1 erweitern und Geräte, die mit einem der Router verbunden sind, sollten über das Modem Internetzugang haben. Lassen Sie mich wissen, wenn Sie weitere Hilfe benötigen!

---

Wenn Sie sich entscheiden, eine feste (statische) IP-Adresse für den ersten Router (Router1) anstatt DHCP zu verwenden, müssen Sie die WAN-Einstellungen von Router1 manuell konfigurieren, um mit Ihrem Modem zu kommunizieren. Hier sind die Einstellungen, die Sie für die IP-Adresse, DNS, Subnetzmaske und Gateway konfigurieren sollten:

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
   - Beispiel: Wenn der DHCP-Bereich des Modems `192.168.1.2` bis `192.168.1.100` ist, können Sie **`192.168.1.101`** verwenden.
   - Dies stellt sicher, dass Router1 eine eindeutige, feste Adresse im Netzwerk des Modems hat.

2. **Subnetzmaske**
   - Setzen Sie dies auf die Subnetzmaske des Modems, die normalerweise **`255.255.255.0`** ist.
   - Dies definiert den Netzwerkbereich als `192.168.1.0` bis `192.168.1.255`.

3. **Standard-Gateway**
   - Setzen Sie dies auf die IP-Adresse des Modems, die **`192.168.1.1`** ist.
   - Das Gateway ist das Gerät (Ihr Modem), das Router1 verwendet, um auf das Internet zuzugreifen.

4. **DNS-Server**
   - Sie haben zwei Optionen:
     - Verwenden Sie die IP des Modems: **`192.168.1.1`**. Dies lässt das Modem DNS-Anfragen verarbeiten.
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
- **Modem-Einstellungen überprüfen**: Melden Sie sich bei Ihrem Modem an (normalerweise bei `192.168.1.1`), um seine IP, Subnetzmaske und den DHCP-Bereich zu bestätigen. Passen Sie die statische IP von Router1 bei Bedarf an.
- **LAN-Einstellungen für Router1**: Um Konflikte zu vermeiden, konfigurieren Sie das LAN-Netzwerk von Router1 auf einem anderen Subnetz, wie `192.168.0.1` mit einer Subnetzmaske von `255.255.255.0`. Aktivieren Sie DHCP auf Router1, um IPs (z.B. `192.168.0.2` bis `192.168.0.254`) an verbundene Geräte zuzuweisen.
- **Testen**: Nach dem Anwenden dieser Einstellungen stellen Sie sicher, dass Router1 Internetzugang hat. Wenn nicht, überprüfen Sie doppelt die IP (keine Konflikte), das Gateway und die DNS-Werte.

Diese Konfiguration gibt Router1 eine feste IP im Netzwerk des Modems, was eine konsistente Konnektivität gewährleistet. Lassen Sie mich wissen, wenn Sie Hilfe bei zusätzlichen Routern oder spezifischen Modemdetails benötigen!