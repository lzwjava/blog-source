---
audio: false
generated: true
lang: de
layout: post
title: Netzwerkleistung und -verwaltung Tutorial
translated: true
type: note
---

**Maßgeschneidert für die chinesische Selbststudienprüfung (自考) in Computernetzwerktechnologie**

---

## **1. Wichtige Leistungskennzahlen**  
### **1.1 Latenz (延迟)**  
- **Definition**: Zeit, die Daten benötigen, um von der Quelle zum Ziel zu gelangen (ms).  
- **Komponenten**:  
  - **Ausbreitungsverzögerung**: Entfernung ÷ Geschwindigkeit des Mediums (z.B. Glasfaser ≈ 2/3 Lichtgeschwindigkeit).  
  - **Übertragungsverzögerung**: Paketgröße ÷ Bandbreite.  
  - **Warteschlangenverzögerung**: Zeit, die in Routern/Switches verbracht wird.  
  - **Bearbeitungsverzögerung**: Zeit, die Geräte für die Verarbeitung von Headern benötigen.  
- **Auswirkung**: Kritisch für Echtzeitanwendungen (z.B. Videoanrufe, Gaming).  
- **Beispiel**: Hohe Latenz beim Zugriff auf internationale Websites (z.B. ein chinesischer Benutzer verbindet sich mit einem US-Server).  

### **1.2 Bandbreite (带宽)**  
- **Definition**: Maximale Datenübertragungsrate (Mbps/Gbps).  
- **Bedeutung**: Bestimmt die Netzwerkkapazität.  
- **Beispiel**: 4K-Streaming benötigt ~25 Mbps; unzureichende Bandbreite verursacht Buffering.  

### **1.3 Jitter (抖动)**  
- **Definition**: Schwankung der Latenz zwischen Paketen.  
- **Auswirkung**: Unterbrochene VoIP-Anrufe oder Videokonferenzen.  
- **Lösung**: Verwendung von Jitter-Puffern, um Verzögerungen auszugleichen.  

### **1.4 Paketverlust (丢包率)**  
- **Definition**: Prozentsatz der Pakete, die das Ziel nicht erreichen.  
- **Ursachen**: Netzwerküberlastung, fehlerhafte Hardware, Signalstörungen.  
- **Auswirkung**: Neuübertragungen verlangsamen den Durchsatz (z.B. Lag in Online-Spielen).  

---

## **2. Netzwerk-Fehlerbehebungs-Tools**  
### **2.1 Ping**  
- **Funktion**: Testet die Konnektivität und misst die Latenz mittels ICMP Echo Requests.  
- **Befehl**: `ping www.baidu.com`  
  - **Wichtige Ausgabe**: Round-Trip Time (RTT) und Paketverlust %.  
  - **Dauer-Ping**: `ping -t` (Windows) oder `ping -c 10` (Linux).  

### **2.2 Traceroute**  
- **Funktion**: Zeichnet den Pfad der Pakete nach und identifiziert die Latenz bei jedem Hop.  
- **Befehl**:  
  - Windows: `tracert www.qq.com`  
  - Linux/macOS: `traceroute -I www.qq.com` (verwendet ICMP)  
- **Mechanismus**: Verwendet TTL (Time-to-Live), um Router zu Fehlermeldungen zu zwingen.  

---

## **3. Grundlagen der Netzwerkkonfiguration & -verwaltung**  
### **3.1 IP-Adressierung & Subnetting**  
- **IPv4**: 32-Bit-Adresse (z.B. `192.168.1.1`).  
- **Subnetting**: Unterteilt Netzwerke zur Effizienzsteigerung (z.B. `/24` Subnetz = 256 Adressen).  

### **3.2 DHCP & DNS**  
- **DHCP**: Automatisiert die IP-Zuweisung (z.B. Heimrouter).  
- **DNS**: Übersetzt Domainnamen in IPs (z.B. `www.taobao.com` → `140.205.220.96`).  

### **3.3 Gerätekonfiguration**  
- **Router/Switches**: Verwendung von CLI (z.B. Cisco IOS) oder GUI (z.B. Huawei Web-Oberfläche).  
- **Sicherheit**: Firewalls, ACLs (Access Control Lists).  

---

## **4. Quality of Service (QoS)**  
### **4.1 Warum QoS wichtig ist**  
- Priorisiert kritischen Datenverkehr (z.B. Videokonferenzen gegenüber Datei-Downloads).  

### **4.2 QoS-Mechanismen**  
- **Datenverkehrsklassifizierung**: Markieren von Paketen (z.B. DSCP für VoIP).  
- **Warteschlangenverwaltung**: Prioritätswarteschlangen (z.B. LLQ für Sprachverkehr).  
- **Shaping/Policing**: Bandbreitenbegrenzung für nicht-kritische Anwendungen.  

### **4.3 Modelle**  
- **DiffServ**: Skalierbar, klassenbasiert (z.B. Unternehmensnetzwerke).  
- **IntServ**: Ressourcenreservierung für hochprioritäre Datenflüsse (komplex, weniger verbreitet).  

---

## **5. Prüfungstipps & Praxis**  
### **5.1 Wichtige Formeln**  
- **Gesamtlatenz** = Ausbreitungs- + Übertragungs- + Warteschlangen- + Bearbeitungsverzögerung  
- **Bandbreite-Latenz-Produkt** = Bandbreite × RTT (misst die Netzwerkkapazität).  

### **5.2 Szenariobasierte Fragen**  
- **Beispiel**: Ein Benutzer beschwert sich über ruckelige Zoom-Anrufe. Identifizieren Sie wahrscheinliche Ursachen (Jitter, Paketverlust) und Tools (ping, traceroute).  

### **5.3 Labs für Selbststudium**  
1. Verwenden Sie `ping`, um die Latenz zu `www.baidu.com` vs. `www.amazon.com` zu vergleichen.  
2. Führen Sie `tracert` aus, um die Hops zu einer internationalen Website zu analysieren.  
3. Konfigurieren Sie die QoS-Einstellungen eines Heimrouters, um WeChat Video zu priorisieren.  

---

**Zusammenfassung**: Die Beherrschung dieser Konzepte gewährleistet ein effizientes Netzwerkdesign und eine effektive Fehlerbehebung, was sowohl für reale Anwendungen als auch für Prüfungen unerlässlich ist. Konzentrieren Sie sich auf das Verständnis der Wechselwirkungen zwischen den Kennzahlen (z.B. wie Jitter VoIP beeinflusst) und die praktische Anwendung der Tools.