---
audio: false
lang: de
layout: post
title: OpenWRT als Wireless-Bridge konfigurieren
translated: true
---

Um Ihre Anfrage zu beantworten, "ist es richtig?" bezüglich der Schritte zur Konfiguration von OpenWRT als drahtlose Brücke und um die richtigen Methoden zur Erreichung dieses Ziels zu bieten, werde ich die von Ihnen bereitgestellten Schritte bewerten und sie basierend auf den Best Practices für OpenWRT verfeinern. Ihr Ziel ist es, Ihren OpenWRT-Router (z. B. Xiaomi Mi Router 4C mit OpenWRT 24.10.0) als drahtlose Brücke einzurichten – drahtlos mit einem bestehenden Wi-Fi-Netzwerk als Client verbunden und die Verbindung über seinen eigenen Wi-Fi-Access-Point (AP) oder Ethernet-Ports teilen, wobei alle Geräte im gleichen Subnetz wie der Hauptrouter verbleiben.

Ihre bereitgestellten Schritte sind größtenteils korrekt, aber es fehlt eine kritische Anpassung, um eine ordnungsgemäße Brückenbildung sicherzustellen und IP-Konflikte zu vermeiden. Im Folgenden werde ich zunächst Ihre Konfiguration bewerten und dann die richtigen, vollständigen Schritte zur Erreichung einer drahtlosen Brücke in OpenWRT unter Verwendung der einfachen Brückenmethode (Client + AP auf derselben Brücke) vorstellen, die mit Ihrer Absicht übereinstimmt. Ich werde auch kurz eine Alternative unter Verwendung von `relayd` für Fälle erwähnen, in denen die einfache Methode fehlschlägt, obwohl Ihre Einrichtung wahrscheinlich die einfachere Methode unterstützt.

---

### **Bewertung Ihrer Bereitgestellten Schritte**

Ihre Schritte zielen darauf ab:
1. Den OpenWRT-Router als Client mit einem bestehenden Wi-Fi-Netzwerk zu verbinden.
2. Einen AP einzurichten, um ein neues Wi-Fi-Netzwerk zu senden.
3. Die Client- und AP-Schnittstellen zu brücken, um das Internet zu teilen.

Hier ist eine schnelle Überprüfung:
- **Schritt 1: Anmeldung bei LuCI** - Richtig, der Zugriff auf die Weboberfläche ist der Ausgangspunkt.
- **Schritt 2: Konfiguration des drahtlosen Clients** - Der Beitritt zum Ziel-Wi-Fi und die Zuweisung zu dem `lan`-Netzwerk ist ein guter Anfang, aber die Standardkonfiguration von `lan` in OpenWRT (statische IP, typischerweise 192.168.1.1) könnte mit dem Hauptrouter in Konflikt geraten, wenn dieser dieselbe IP verwendet. Dies benötigt eine Anpassung.
- **Schritt 3: Konfiguration des drahtlosen AP** - Die Einrichtung eines AP und die Zuweisung zu `lan` ist für die Brückenbildung korrekt, aber es hängt davon ab, dass die `lan`-Schnittstelle ordnungsgemäß konfiguriert ist.
- **Schritt 4: Brücken der Netzwerke** - Die Zuweisung beider Schnittstellen zu `lan` brückt sie theoretisch, aber ohne Deaktivierung des DHCP-Servers oder Anpassung der IP-Einstellungen funktioniert es möglicherweise nicht nahtlos.
- **Schritt 5: Testen der Einrichtung** - Das Testen ist wichtig, aber der Erfolg hängt davon ab, dass die vorherigen Schritte vollständig korrekt sind.

**Was fehlt oder ist falsch?**
- Standardmäßig hat die `lan`-Schnittstelle von OpenWRT eine statische IP (z. B. 192.168.1.1) und führt einen DHCP-Server aus. Wenn der Hauptrouter ebenfalls 192.168.1.1 ist, entsteht ein IP-Konflikt. Sie müssen die `lan`-Schnittstelle in den DHCP-Client-Modus setzen, um eine IP vom Hauptrouter zu erhalten, und den lokalen DHCP-Server deaktivieren, damit der Hauptrouter allen Geräten IPs zuweist.
- Die Zuweisung der Firewall-Zone zu `lan` ist für die Einfachheit in Ordnung, aber die IP-Konfiguration ist entscheidend.

Mit diesem im Hinterkopf sind Ihre Schritte "größtenteils richtig", aber ohne Anpassung der `lan`-Schnittstelleneinstellungen unvollständig. Hier sind die korrigierten Schritte.

---

### **Richtige Schritte zur Konfiguration von OpenWRT als drahtlose Brücke (Einfache Brückenmethode)**

Diese Methode richtet Ihren OpenWRT-Router so ein, dass er sich mit einem bestehenden Wi-Fi-Netzwerk als Client verbindet und diese Verbindung über seinen eigenen AP oder Ethernet-Ports teilt, alles im gleichen Subnetz wie der Hauptrouter (z. B. 192.168.1.x). Hier ist, wie Sie dies über die LuCI-Weboberfläche tun können:

#### **Voraussetzungen**
- OpenWRT ist installiert (z. B. Version 24.10.0 auf Xiaomi Mi Router 4C).
- Sie haben die SSID, das Passwort und den Verschlüsselungstyp (z. B. WPA2-PSK) des Haupt-Wi-Fi-Netzwerks.
- Zugriff auf LuCI unter `http://192.168.1.1` (oder die aktuelle IP) und Ihre Admin-Anmeldeinformationen.

#### **Schritt 1: Anmeldung bei LuCI**
- Öffnen Sie einen Browser und navigieren Sie zu `http://192.168.1.1`.
- Melden Sie sich mit Ihrem OpenWRT-Benutzernamen (Standard: `root`) und Passwort (während der Installation festgelegt) an.

#### **Schritt 2: Konfiguration des drahtlosen Clients**
- **Navigieren Sie zu den drahtlosen Einstellungen:**
  - Gehen Sie zu **Netzwerk > Drahtlos**.
- **Netzwerke scannen:**
  - Finden Sie Ihr Funkgerät (z. B. `radio0` für 2,4 GHz auf dem Mi Router 4C).
  - Klicken Sie auf **Scannen**, um verfügbare Wi-Fi-Netzwerke aufzulisten.
- **Beitreten Sie dem Haupt-Wi-Fi-Netzwerk:**
  - Finden Sie die SSID Ihres Hauptrouter-Wi-Fi.
  - Klicken Sie auf **Netzwerk beitreten**.
- **Konfigurieren Sie die Client-Einstellungen:**
  - **Wi-Fi-Schlüssel:** Geben Sie das Passwort für das Haupt-Wi-Fi ein.
  - **Netzwerk:** Wählen Sie oder setzen Sie auf `lan` (dies fügt die Client-Schnittstelle zur `br-lan`-Brücke hinzu).
  - **Firewall-Zone:** Zuweisen zu `lan` (dies vereinfacht die Verkehrsregeln für die Brückenbildung).
  - **Schnittstellenname:** LuCI könnte `wwan` vorschlagen; Sie können es belassen oder in `client` umbenennen, um Klarheit zu schaffen, aber stellen Sie sicher, dass es mit `lan` verbunden ist.
- **Speichern & Anwenden:**
  - Klicken Sie auf **Speichern & Anwenden**, um sich mit dem Haupt-Wi-Fi zu verbinden.

#### **Schritt 3: Anpassen der LAN-Schnittstelle auf DHCP-Client**
- **Gehen Sie zu Schnittstellen:**
  - Navigieren Sie zu **Netzwerk > Schnittstellen**.
- **Bearbeiten Sie die LAN-Schnittstelle:**
  - Klicken Sie auf **Bearbeiten** neben der `lan`-Schnittstelle.
- **Setzen Sie das Protokoll auf DHCP-Client:**
  - Im **Protokoll**-Dropdown wählen Sie **DHCP-Client**.
  - Dies ermöglicht es der `br-lan`-Brücke (die nun die drahtlose Client-Schnittstelle enthält), eine IP-Adresse vom DHCP-Server des Hauptrouters (z. B. 192.168.1.x) zu erhalten.
- **Deaktivieren Sie den DHCP-Server:**
  - Da `lan` nun ein DHCP-Client ist, wird der lokale DHCP-Server automatisch deaktiviert. Überprüfen Sie dies unter **Erweiterte Einstellungen** oder **DHCP und DNS** – stellen Sie sicher, dass "Schnittstelle ignorieren" aktiviert ist, wenn die Option erscheint.
- **Speichern & Anwenden:**
  - Klicken Sie auf **Speichern & Anwenden**. Der Router wird nun eine IP vom Hauptrouter anfordern.

#### **Schritt 4: Konfiguration des drahtlosen Access Points**
- **Fügen Sie ein neues drahtloses Netzwerk hinzu:**
  - Gehen Sie zurück zu **Netzwerk > Drahtlos**.
  - Klicken Sie auf **Hinzufügen** unter demselben Funkgerät (z. B. `radio0`), um eine neue drahtlose Schnittstelle zu erstellen.
- **Richten Sie den AP ein:**
  - **ESSID:** Wählen Sie einen Namen für Ihr Wi-Fi (z. B. `OpenWRT_AP`).
  - **Modus:** Setzen Sie auf **Access Point (AP)**.
  - **Netzwerk:** Zuweisen zu `lan` (dies brückt es mit der Client-Schnittstelle und Ethernet-Ports).
- **Konfigurieren Sie die Sicherheit:**
  - Gehen Sie zur Registerkarte **Drahtlose Sicherheit**.
  - **Verschlüsselung:** Wählen Sie **WPA2-PSK** (empfohlen).
  - **Schlüssel:** Legen Sie ein starkes Passwort für Ihren AP fest.
- **Speichern & Anwenden:**
  - Klicken Sie auf **Speichern & Anwenden**. Ihr Router wird nun sein eigenes Wi-Fi senden.

#### **Schritt 5: Überprüfen der Brücke**
- **Überprüfen Sie die Schnittstellen:**
  - Gehen Sie zu **Netzwerk > Schnittstellen**.
  - Stellen Sie sicher, dass die `lan`-Schnittstelle sowohl den drahtlosen Client (z. B. `wlan0`) als auch den AP (z. B. `wlan0-1`) unter der `br-lan`-Brücke auflistet.
- **Überprüfen Sie die IP-Zuweisung:**
  - Gehen Sie zu **Status > Übersicht**.
  - Notieren Sie sich die IP-Adresse, die der `lan`-Schnittstelle vom Hauptrouter zugewiesen wurde (z. B. `192.168.1.100`).

#### **Schritt 6: Testen der Einrichtung**
- **Testen Sie Wi-Fi:**
  - Verbinden Sie ein Gerät mit dem `OpenWRT_AP`-Wi-Fi.
  - Stellen Sie sicher, dass es eine IP vom Hauptrouter (z. B. `192.168.1.x`) erhält und Internetzugang hat.
- **Testen Sie Ethernet (falls zutreffend):**
  - Stecken Sie ein Gerät in einen der LAN-Ports des Routers.
  - Bestätigen Sie, dass es eine IP vom Hauptrouter erhält und sich mit dem Internet verbindet.
- **Zugreifen auf LuCI:**
  - Verwenden Sie die neue IP-Adresse (z. B. `http://192.168.1.100`), um auf die OpenWRT-Oberfläche zuzugreifen.

---

### **Warum das funktioniert**
- Die Zuweisung sowohl der Client- als auch der AP-Schnittstellen zum `lan`-Netzwerk fügt sie zur `br-lan`-Brücke hinzu, sodass Layer-2-Verkehr zwischen ihnen und dem Hauptrouter fließen kann.
- Das Setzen von `lan` auf DHCP-Client stellt sicher, dass der OpenWRT-Router eine eindeutige IP vom Hauptrouter erhält, wodurch Konflikte (z. B. mit `192.168.1.1`) vermieden werden, und deaktiviert den lokalen DHCP-Server, sodass der Hauptrouter alle IP-Zuweisungen verwaltet.
- Geräte, die mit dem AP oder Ethernet-Ports verbunden sind, befinden sich im gleichen Subnetz wie das Hauptnetzwerk (z. B. `192.168.1.x`), was die Anforderung an die drahtlose Brücke erfüllt.

---

### **Alternative Methode: Verwendung von relayd (Pseudo-Brücke)**
Wenn die einfache Brückenmethode fehlschlägt (z. B. aufgrund von Einschränkungen des drahtlosen Treibers), können Sie das `relayd`-Paket für eine Pseudo-Brücke verwenden. Dies erstellt eine geroutete Einrichtung, bei der die Clients des OpenWRT-Routers in einem anderen Subnetz sind, aber auf einigen Hardwarekonfigurationen zuverlässiger ist. Hier ist eine kurze Übersicht:

1. **Installieren Sie relayd:**
   - Gehen Sie zu **System > Software**, suchen Sie nach `relayd` und installieren Sie es.
2. **Konfigurieren Sie den drahtlosen Client:**
   - Treten Sie dem Haupt-Wi-Fi bei, aber weisen Sie es einer neuen Schnittstelle (z. B. `wwan`) zu, die auf DHCP-Client gesetzt ist.
3. **Konfigurieren Sie LAN:**
   - Setzen Sie `lan` auf eine statische IP (z. B. `192.168.2.1`) mit eigenem DHCP-Server.
4. **Richten Sie relayd ein:**
   - Konfigurieren Sie `relayd` über SSH oder LuCI (unter **Netzwerk > Hostnamen**), um zwischen `wwan` und `lan` zu relayen.
5. **Konfigurieren Sie AP:**
   - Setzen Sie den AP auf das `lan`-Netzwerk.
6. **Testen:**
   - Geräte auf `OpenWRT_AP` werden sich im `192.168.2.x`-Subnetz befinden, mit Internet, das vom Hauptrouter relayed wird.

**Hinweis:** Dies ist keine echte Brücke (unterschiedliche Subnetze), also verwenden Sie es nur, wenn die einfache Methode nicht funktioniert. Für Ihren Xiaomi Mi Router 4C mit OpenWRT 24.10.0 sollte die einfache Brücke ausreichen.

---

### **Schlussfolgerung**
Ihre ursprünglichen Schritte sind **größtenteils korrekt**, aber ohne das Setzen der `lan`-Schnittstelle auf DHCP-Client-Modus, um IP-Konflikte zu vermeiden und eine ordnungsgemäße Brückenbildung sicherzustellen, sind sie unvollständig. Die korrigierten Schritte oben bieten eine zuverlässige Möglichkeit, OpenWRT als drahtlose Brücke zu konfigurieren. Wenn Sie ihnen folgen, wird Ihr Router sich mit dem Haupt-Wi-Fi verbinden und diese Verbindung nahtlos über seinen AP oder Ethernet-Ports teilen, alles im gleichen Subnetz. Testen Sie die Einrichtung, und wenn Probleme auftreten (selten mit modernem OpenWRT), überlegen Sie sich die `relayd`-Alternative.