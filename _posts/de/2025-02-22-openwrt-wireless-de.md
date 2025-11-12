---
audio: false
generated: true
image: false
lang: de
layout: post
title: Konfiguration von OpenWRT als drahtlose Brücke
translated: true
type: note
---

Mit Hilfe von Grok versuche ich immer noch, an Folgendem zu arbeiten.

---

Um Ihre Frage "ist das richtig?" bezüglich der Schritte zur Konfiguration von OpenWRT als Wireless Bridge zu beantworten und die korrekten Methoden dafür bereitzustellen, werde ich die von Ihnen bereitgestellten Schritte auswerten und basierend auf den Best Practices für OpenWRT verfeinern. Ihr Ziel ist es, Ihren OpenWRT-Router (z.B. Xiaomi Mi Router 4C mit OpenWRT 24.10.0) als Wireless Bridge einzurichten – also ihn drahtlos als Client mit einem bestehenden WLAN-Netzwerk zu verbinden und diese Verbindung über seinen eigenen WLAN-Zugangspunkt (AP) oder seine Ethernet-Ports zu teilen, wobei alle Geräte im selben Subnetz wie der Hauptrouter bleiben.

Ihre bereitgestellten Schritte sind größtenteils korrekt, übersehen jedoch eine kritische Anpassung, um ein ordnungsgemäßes Bridging sicherzustellen und IP-Konflikte zu vermeiden. Nachfolgend werde ich zunächst Ihre Konfiguration bewerten und dann die korrekten, vollständigen Schritte vorstellen, um eine Wireless Bridge in OpenWRT mit der einfachen Bridge-Methode (Client + AP auf derselben Bridge) einzurichten, was Ihrer Absicht entspricht. Ich werde auch kurz eine Alternative mit `relayd` erwähnen, für den Fall, dass die einfache Methode scheitert, obwohl Ihr Setup wahrscheinlich den einfacheren Ansatz unterstützt.

---

### **Bewertung Ihrer bereitgestellten Schritte**

Ihre Schritte zielen darauf ab:
1. Den OpenWRT-Router als Client mit einem bestehenden WLAN-Netzwerk zu verbinden.
2. Einen AP einzurichten, der ein neues WLAN-Netzwerk ausstrahlt.
3. Die Client- und AP-Schnittstellen zu bridgen, um das Internet zu teilen.

Hier ist eine kurze Überprüfung:
- **Schritt 1: Bei LuCI anmelden** - Korrekt, der Zugriff auf die Weboberfläche ist der Anfang.
- **Schritt 2: Den Wireless Client konfigurieren** - Das Verbinden mit dem Ziel-WLAN und das Zuweisen zum `lan`-Netzwerk ist ein guter Anfang, aber die Standard-`lan`-Konfiguration in OpenWRT (statische IP, typischerweise 192.168.1.1) könnte mit dem Hauptrouter kollidieren, wenn dieser die gleiche IP verwendet. Dies muss angepasst werden.
- **Schritt 3: Den Wireless Access Point konfigurieren** - Das Einrichten eines AP und das Zuweisen zum `lan` ist korrekt für Bridging, setzt jedoch voraus, dass die `lan`-Schnittstelle korrekt konfiguriert ist.
- **Schritt 4: Die Netzwerke bridgen** - Das Zuweisen beider Schnittstellen zu `lan` überbrückt sie theoretisch, aber ohne das Abschalten des DHCP-Servers oder die Anpassung der IP-Einstellungen funktioniert es möglicherweise nicht nahtlos.
- **Schritt 5: Das Setup testen** - Tests sind essenziell, aber der Erfolg hängt davon ab, dass die vorherigen Schritte vollständig korrekt sind.

**Was fehlt oder ist falsch?**
- Standardmäßig hat die `lan`-Schnittstelle in OpenWRT eine statische IP (z.B. 192.168.1.1) und betreibt einen DHCP-Server. Wenn der Hauptrouter ebenfalls 192.168.1.1 verwendet, führt dies zu einem IP-Konflikt. Sie müssen die `lan`-Schnittstelle auf den DHCP-Client-Modus setzen, um eine IP vom Hauptrouter zu erhalten, und den lokalen DHCP-Server deaktivieren, damit der Hauptrouter allen Geräten IPs zuweist.
- Die Firewall-Zonen-Zuweisung zu `lan` ist der Einfachheit halber in Ordnung, aber die IP-Konfiguration ist entscheidend.

Vor diesem Hintergrund sind Ihre Schritte "größtenteils richtig", aber ohne die Anpassung der `lan`-Schnittstelleneinstellungen unvollständig. Nachfolgend finden Sie die korrigierten Schritte.

---

### **Korrekte Schritte zur Konfiguration von OpenWRT als Wireless Bridge (Einfache Bridge-Methode)**

Diese Methode richtet Ihren OpenWRT-Router so ein, dass er sich als Client mit einem bestehenden WLAN-Netzwerk verbindet und diese Verbindung über seinen eigenen AP oder seine Ethernet-Ports teilt, alles im selben Subnetz wie der Hauptrouter (z.B. 192.168.1.x). So geht es über die LuCI-Weboberfläche:

#### **Voraussetzungen**
- OpenWRT ist installiert (z.B. Version 24.10.0 auf Xiaomi Mi Router 4C).
- Sie haben die SSID, das Passwort und den Verschlüsselungstyp (z.B. WPA2-PSK) des Haupt-WLAN-Netzwerks.
- Zugriff auf LuCI unter `http://192.168.1.1` (oder der aktuellen IP) und Ihre Admin-Zugangsdaten.

#### **Schritt 1: Bei LuCI anmelden**
- Öffnen Sie einen Browser und navigieren Sie zu `http://192.168.1.1`.
- Melden Sie sich mit Ihrem OpenWRT-Benutzernamen (Standard: `root`) und Passwort (während der Installation festgelegt) an.

#### **Schritt 2: Den Wireless Client konfigurieren**
- **Zu den Wireless-Einstellungen navigieren:**
  - Gehen Sie zu **Network > Wireless**.
- **Nach Netzwerken scannen:**
  - Suchen Sie Ihr Radio (z.B. `radio0` für 2,4 GHz auf dem Mi Router 4C).
  - Klicken Sie auf **Scan**, um verfügbare WLAN-Netzwerke aufzulisten.
- **Dem Haupt-WLAN-Netzwerk beitreten:**
  - Finden Sie die SSID des WLANs Ihres Hauptrouters.
  - Klicken Sie auf **Join Network**.
- **Client-Einstellungen konfigurieren:**
  - **Wi-Fi Key:** Geben Sie das Passwort für das Haupt-WLAN ein.
  - **Network:** Wählen Sie `lan` aus oder setzen Sie es auf `lan` (dies fügt die Client-Schnittstelle zur `br-lan`-Bridge hinzu).
  - **Firewall Zone:** Weisen Sie `lan` zu (dies vereinfacht die Verkehrsregeln für das Bridging).
  - **Interface Name:** LuCI schlägt möglicherweise `wwan` vor; Sie können dies belassen oder zur besseren Übersicht in `client` umbenennen, stellen Sie jedoch sicher, dass es an `lan` gebunden ist.
- **Speichern & Anwenden:**
  - Klicken Sie auf **Save & Apply**, um eine Verbindung zum Haupt-WLAN herzustellen.

#### **Schritt 3: Die LAN-Schnittstelle auf DHCP Client umstellen**
- **Zu Interfaces gehen:**
  - Navigieren Sie zu **Network > Interfaces**.
- **Die LAN-Schnittstelle bearbeiten:**
  - Klicken Sie auf **Edit** neben der `lan`-Schnittstelle.
- **Protokoll auf DHCP Client setzen:**
  - Wählen Sie im Dropdown-Menü **Protocol** die Option **DHCP client** aus.
  - Dies ermöglicht es der `br-lan`-Bridge (die nun den Wireless Client enthält), eine IP-Adresse vom DHCP-Server des Hauptrouters (z.B. 192.168.1.x) zu erhalten.
- **DHCP-Server deaktivieren:**
  - Da `lan` nun ein DHCP-Client ist, wird der lokale DHCP-Server automatisch deaktiviert. Überprüfen Sie dies unter **Advanced Settings** oder **DHCP and DNS** – stellen Sie sicher, dass "Ignore interface" aktiviert ist, falls die Option erscheint.
- **Speichern & Anwenden:**
  - Klicken Sie auf **Save & Apply**. Der Router fordert nun eine IP vom Hauptrouter an.

#### **Schritt 4: Den Wireless Access Point konfigurieren**
- **Ein neues Wireless-Netzwerk hinzufügen:**
  - Gehen Sie zurück zu **Network > Wireless**.
  - Klicken Sie unter demselben Radio (z.B. `radio0`) auf **Add**, um eine neue Wireless-Schnittstelle zu erstellen.
- **Den AP einrichten:**
  - **ESSID:** Wählen Sie einen Namen für Ihr WLAN (z.B. `OpenWRT_AP`).
  - **Mode:** Setzen Sie auf **Access Point (AP)**.
  - **Network:** Weisen Sie `lan` zu (dies bridget sie mit der Client-Schnittstelle und den Ethernet-Ports).
- **Sicherheit konfigurieren:**
  - Gehen Sie zum Tab **Wireless Security**.
  - **Encryption:** Wählen Sie **WPA2-PSK** (empfohlen).
  - **Key:** Legen Sie ein starkes Passwort für Ihren AP fest.
- **Speichern & Anwenden:**
  - Klicken Sie auf **Save & Apply**. Ihr Router strahlt nun sein eigenes WLAN aus.

#### **Schritt 5: Die Bridge überprüfen**
- **Schnittstellen prüfen:**
  - Gehen Sie zu **Network > Interfaces**.
  - Stellen Sie sicher, dass die `lan`-Schnittstelle sowohl den Wireless Client (z.B. `wlan0`) als auch den AP (z.B. `wlan0-1`) unter der `br-lan`-Bridge auflistet.
- **IP-Zuweisung prüfen:**
  - Gehen Sie zu **Status > Overview**.
  - Notieren Sie die IP-Adresse, die der `lan`-Schnittstelle vom Hauptrouter zugewiesen wurde (z.B. `192.168.1.100`).

#### **Schritt 6: Das Setup testen**
- **WLAN testen:**
  - Verbinden Sie ein Gerät mit dem `OpenWRT_AP`-WLAN.
  - Stellen Sie sicher, dass es eine IP vom Hauptrouter erhält (z.B. `192.168.1.x`) und Internetzugang hat.
- **Ethernet testen (falls zutreffend):**
  - Schließen Sie ein Gerät an einen der LAN-Ports des Routers an.
  - Bestätigen Sie, dass es eine IP vom Hauptrouter erhält und eine Verbindung zum Internet herstellt.
- **Auf LuCI zugreifen:**
  - Verwenden Sie die neue IP-Adresse (z.B. `http://192.168.1.100`), um auf die OpenWRT-Oberfläche zuzugreifen.

---

### **Warum das funktioniert**
- Das Zuweisen sowohl der Client- als auch der AP-Schnittstellen zum `lan`-Netzwerk fügt sie der `br-lan`-Bridge hinzu, was Layer-2-Datenverkehr zwischen ihnen und dem Hauptrouter ermöglicht.
- Das Setzen von `lan` auf DHCP Client stellt sicher, dass der OpenWRT-Router eine eindeutige IP vom Hauptrouter erhält und Konflikte (z.B. mit `192.168.1.1`) vermieden werden, und deaktiviert den lokalen DHCP-Server, sodass der Hauptrouter alle IP-Zuweisungen verwaltet.
- Geräte, die mit dem AP oder den Ethernet-Ports verbunden sind, erscheinen im selben Subnetz wie das Hauptnetzwerk (z.B. `192.168.1.x`), was die Anforderung der Wireless Bridge erfüllt.

---

### **Alternative Methode: Verwendung von relayd (Pseudo-Bridge)**
Falls die einfache Bridge-Methode fehlschlägt (z.B. aufgrund von Treibereinschränkungen), können Sie das `relayd`-Paket für eine Pseudo-Bridge verwenden. Dies erstellt ein geroutetes Setup, bei dem die Clients des OpenWRT-Routers in einem anderen Subnetz sind, aber es ist auf einiger Hardware zuverlässiger. Hier ist ein kurzer Überblick:

1. **relayd installieren:**
   - Gehen Sie zu **System > Software**, suchen Sie nach `relayd` und installieren Sie es.
2. **Wireless Client konfigurieren:**
   - Treten Sie dem Haupt-WLAN bei, weisen Sie es jedoch einer neuen Schnittstelle (z.B. `wwan`) zu, die auf DHCP Client gesetzt ist.
3. **LAN konfigurieren:**
   - Setzen Sie `lan` auf eine statische IP (z.B. `192.168.2.1`) mit einem eigenen DHCP-Server.
4. **relayd einrichten:**
   - Konfigurieren Sie `relayd` per SSH oder LuCI (unter **Network > Hostnames**), um zwischen `wwan` und `lan` zu relayen.
5. **AP konfigurieren:**
   - Richten Sie den AP im `lan`-Netzwerk ein.
6. **Testen:**
   - Geräte im `OpenWRT_AP`-Netzwerk befinden sich im Subnetz `192.168.2.x`, wobei das Internet vom Hauptrouter gerelayed wird.

**Hinweis:** Dies ist keine echte Bridge (unterschiedliche Subnetze), verwenden Sie sie daher nur, wenn die einfache Methode nicht funktioniert. Für Ihren Xiaomi Mi Router 4C mit OpenWRT 24.10.0 sollte die einfache Bridge ausreichen.

---

### **Schlussfolgerung**
Ihre ursprünglichen Schritte sind **größtenteils korrekt**, aber ohne das Setzen der `lan`-Schnittstelle auf den DHCP-Client-Modus unvollständig, um IP-Konflikte zu vermeiden und ein ordnungsgemäßes Bridging sicherzustellen. Die korrigierten Schritte oben bieten eine zuverlässige Methode zur Konfiguration von OpenWRT als Wireless Bridge. Wenn Sie ihnen folgen, verbindet sich Ihr Router mit dem Haupt-WLAN und teilt diese Verbindung nahtlos über seinen AP oder seine Ethernet-Ports, alles im selben Subnetz. Testen Sie das Setup, und falls Probleme auftreten (selten bei modernem OpenWRT), ziehen Sie die `relayd`-Alternative in Betracht.