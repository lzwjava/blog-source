---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: AWS-Grundlagen für virtuelles Netzwerken
translated: true
type: note
---

### Grundlagen der virtuellen AWS-Netzwerke

AWS bietet eine flexible, isolierte Netzwerkumgebung über seinen **Virtual Private Cloud (VPC)**-Service. Dieser fungiert als Ihr eigenes logisch isoliertes Segment der AWS-Cloud, in dem Sie Ressourcen wie EC2-Instanzen, RDS-Datenbanken und mehr starten können. Im Folgenden werde ich die von Ihnen erwähnten Schlüsselkomponenten (virtuelles Netzwerk, Gateway, Subnetze) und einige verwandte ("etc.") in einfachen Worten erklären und zeigen, wie sie zusammenpassen.

#### Virtuelles Netzwerk (VPC - Virtual Private Cloud)
- **Was es ist**: Die Grundlage der AWS-Netzwerke. Eine VPC ist ein virtuelles Netzwerk, das Ihrem AWS-Konto zugeordnet ist, ähnlich einem traditionellen Rechenzentrumsnetzwerk, aber in der Cloud. Es erstreckt sich über eine oder mehrere Availability Zones (AZs) in einer Region.
- **Hauptmerkmale**:
  - Sie definieren seinen IP-Adressbereich über CIDR-Blöcke (z.B. 10.0.0.0/16, was ~65.000 IP-Adressen erlaubt).
  - Es ist standardmäßig isoliert – kein Datenverkehr ein- oder ausgehend, es sei denn, Sie konfigurieren es.
  - Unterstützt IPv4 und IPv6.
- **Warum verwenden?**: Kontrolliert Zugriff, Sicherheit und Konnektivität für Ihre Ressourcen. Jedes AWS-Konto erhält eine Standard-VPC, aber Sie können benutzerdefinierte für Produktionsumgebungen erstellen.
- **Beispiel**: Stellen Sie sich eine VPC als Ihren privaten Hinterhof in der AWS-"Nachbarschaft" vor – Sie entscheiden über Zäune, Tore und Wege darin.

#### Subnetze
- **Was sie sind**: Unterteilungen des IP-Adressbereichs einer VPC. Jedes Subnetz ist an eine einzelne Availability Zone gebunden und fungiert wie eine segmentierte Zone innerhalb Ihres Netzwerks.
- **Typen**:
  - **Öffentliches Subnetz**: Ressourcen hier können direkt auf das Internet zugreifen (über ein Internet Gateway).
  - **Privates Subnetz**: Isoliert vom direkten Internetzugang; wird für sensible Ressourcen wie Datenbanken verwendet.
- **Hauptmerkmale**:
  - Größe wird durch CIDR definiert (z.B. 10.0.1.0/24 für ~250 IPs).
  - Sie können mehrere Subnetze pro AZ für hohe Verfügbarkeit haben.
  - Ressourcen (z.B. EC2-Instanzen) werden in einem Subnetz gestartet.
- **Warum verwenden?**: Erhöht die Sicherheit und Fehlertoleranz – z.B. Webserver in öffentliche Subnetze und App-Server in private Subnetze stellen.
- **Beispiel**: Wenn Ihre VPC eine Stadt ist, sind Subnetze Stadtteile: öffentliche in der Nähe der Autobahn (Internet), private in abgeschlossenen Wohnanlagen.

#### Gateways
Gateways verbinden Ihre VPC mit der Außenwelt oder anderen Netzwerken. Es gibt einige Typen:

- **Internet Gateway (IGW)**:
  - **Was es ist**: Eine hochverfügbare Komponente, die an Ihre VPC angehängt wird und bidirektionale Kommunikation mit dem öffentlichen Internet ermöglicht.
  - **Wie es funktioniert**: Leitet Datenverkehr von öffentlichen Subnetzen ins Internet (und umgekehrt). Erfordert Aktualisierungen der Routingtabelle, um Datenverkehr zu lenken (z.B. 0.0.0.0/0 → igw-xxxx).
  - **Warum verwenden?**: Für öffentlich zugängliche Apps wie Websites. Es ist kostenlos und skaliert automatisch.
  - **Beispiel**: Die Haustür zum Internet – hängen Sie es an, aktualisieren Sie die Routen, und Ihre öffentlichen Ressourcen können surfen oder angesurft werden.

- **NAT Gateway (Network Address Translation)**:
  - **Was es ist**: Befindet sich in einem öffentlichen Subnetz und erlaubt es Ressourcen in privaten Subnetzen, ausgehenden Internetverkehr zu initiieren (z.B. für Software-Updates), ohne sie für eingehenden Verkehr freizulegen.
  - **Wie es funktioniert**: Übersetzt private IPs in eine öffentliche Elastic IP. Zuverlässiger als NAT-Instanzen.
  - **Warum verwenden?**: Sichere ausgehende Zugriffe für private Ressourcen. Kosten ~0,045 $/Stunde + Datentransfer.
  - **Beispiel**: Ein Einwegventil – private Server können "nach außen telefonieren" für Pakete, aber niemand kann ungeladen klopfen.

- **Andere Gateways** (kurz):
  - **Virtual Private Gateway (VGW)**: Für VPN-Verbindungen zu Ihrem On-Premises-Netzwerk.
  - **Transit Gateway**: Verbindet mehrere VPCs und On-Premises-Netzwerke wie ein Hub.

#### Andere verwandte Komponenten ("Etc.")
- **Routingtabellen**: Definieren, wie Datenverkehr innerhalb Ihrer VPC geroutet wird (z.B. zu IGW, NAT oder Peering-Verbindungen). Jedes Subnetz hat eine zugeordnete Routingtabelle – stellen Sie es sich als Verkehrskarte vor.
- **Network ACLs (Access Control Lists)**: Zustandslose Firewalls auf Subnetzebene, die ein- und ausgehenden Datenverkehr nach IP/Protokoll kontrollieren (z.B. Port 80 erlauben).
- **Security Groups**: Zustandsbehaftete Firewalls auf Instanzebene, die wie persönliche Türsteher für EC2/RDS fungieren (z.B. SSH von Ihrer IP erlauben).
- **VPC Peering**: Verbindet zwei VPCs (sogar in verschiedenen Konten/Regionen) für private Kommunikation, wie ein direkter Tunnel.
- **Elastic Network Interfaces (ENIs)**: Virtuelle Netzwerkkarten für Instanzen, die mehrere IPs oder Anhänge erlauben.

#### Wie alles zusammenpasst
1. Erstellen Sie eine VPC mit einem CIDR-Block.
2. Fügen Sie Subnetze (öffentlich/privat) über AZs hinzu.
3. Hängen Sie ein Internet Gateway für öffentlichen Zugang an.
4. Konfigurieren Sie Routingtabellen, um Datenverkehr zu lenken (z.B. öffentliche Subnetze routen zum IGW).
5. Starten Sie Ressourcen in Subnetzen und sichern Sie sie mit Security Groups/NACLs.
6. Für ausgehenden privaten Verkehr fügen Sie ein NAT Gateway hinzu.

Dieser Aufbau gewährleistet Skalierbarkeit, Sicherheit und Resilienz. Für praktische Erfahrungen beginnen Sie mit dem AWS VPC-Assistenten in der Konsole – er konfiguriert automatisch einen grundlegenden Aufbau.

Wenn Sie Diagramme, Codebeispiele oder Details zu einem bestimmten Teil (z.B. Peering) benötigen, lassen Sie es mich wissen!

**Referenzen**:
- [AWS VPC-Dokumentation](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [AWS Subnetze-Guide](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)
- [AWS Gateways-Überblick](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)