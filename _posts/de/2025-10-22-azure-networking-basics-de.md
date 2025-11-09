---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Grundlagen der Azure Virtual Network
translated: true
type: note
---

### Grundlagen der Azure Virtual Network

Azure bietet eine skalierbare und sichere Netzwerkumgebung über seinen **Virtual Network (VNet)**-Dienst, der das Kernäquivalent zu AWS VPC ist. Er erzeugt einen privaten, isolierten Bereich in der Azure-Cloud für Ihre Ressourcen wie VMs, App Services oder Kubernetes-Cluster. Nachfolgend erläutere ich die wichtigsten Komponenten (virtuelles Netzwerk, Gateways, Subnetze usw.) mit Gemeinsamkeiten und Unterschieden zu AWS, strukturiert für einen einfachen Vergleich.

#### Virtuelles Netzwerk (VNet)
- **Was es ist**: Das grundlegende, isolierte Netzwerk in Azure, das sich über eine Region erstreckt und die private Kommunikation zwischen Ressourcen ermöglicht. Sie definieren seinen Adressraum mit CIDR-Blöcken (z. B. 10.0.0.0/16).
- **Wichtige Merkmale**:
  - Standardmäßiger ausgehender Internetzugang für Ressourcen (im Gegensatz zu AWS, wo er optional ist).
  - Unterstützt IPv4 und IPv6; standardmäßig isoliert.
  - Keine Kosten für das VNet selbst – Sie zahlen für angehängte Ressourcen wie Gateways.
- **Vergleichbar mit AWS VPC**: Beide sind private Clouds zur Ressourcenisolierung, Skalierung und Konnektivität. Azure VNets erstrecken sich automatisch über Availability Zones (AZs); AWS VPCs erfordern eine explizite AZ-Einrichtung.
- **Warum verwenden?**: Sichere Kommunikation zwischen Ressourcen, Internetzugang und Verbindungen zum lokalen Standort. Jedes Azure-Abonnement hat Zugriff, aber Sie erstellen benutzerdefinierte VNets für die Kontrolle.
- **Beispiel**: Wie AWS VPC ist es Ihr "privates Anwesen" in der Cloud – Sie setzen die Grenzen, aber Azure handhabt einige Standardeinstellungen wie ausgehenden Internetverkehr.

#### Subnetze
- **Was sie sind**: Unterteilungen des Adressraums eines VNets, in denen Ressourcen bereitgestellt werden. Jedes Subnetz ist auf das VNet beschränkt und kann sich über alle AZs in einer Region erstrecken.
- **Typen**:
  - **Öffentliches Subnetz**: Ressourcen können öffentliche IPs für ein- und ausgehenden Internetverkehr haben (über Azure Load Balancer oder öffentliche Endpunkte).
  - **Privates Subnetz**: Kein direkter öffentlicher Zugriff; ideal für Datenbanken oder interne Apps.
- **Wichtige Merkmale**:
  - CIDR-definiert (z. B. 10.0.1.0/24).
  - Mehrere pro VNet zur Segmentierung; Datenverkehr zwischen ihnen kann gefiltert werden.
- **Vergleichbar mit AWS Subnetzen**: Beide segmentieren Netzwerke für Sicherheit und Organisation. Die automatische AZ-Ausdehnung von Azure vereinfacht Hochverfügbarkeit; AWS bindet Subnetze an bestimmte AZs.
- **Warum verwenden?**: Isoliert Workloads – z. B. Frontends in öffentlichen Subnetzen, Backends in privaten.
- **Beispiel**: Subnetze sind "Bezirke" in Ihrer VNet-Stadt: öffentliche mit Straßenzugang (Internet), private hinter Mauern.

#### Gateways
Gateways in Azure handhaben externe Konnektivität, mit einigen Standardeinstellungen, die sich von AWS unterscheiden.

- **Internet Gateway-Äquivalent**:
  - **Was es ist**: Kein direktes IGW; ausgehender Internetzugang ist für VNet-Ressourcen standardmäßig aktiviert. Für eingehenden Verkehr wird eine öffentliche IP oder ein Load Balancer benötigt.
  - **Wie es funktioniert**: Datenverkehr wird über Azure-Systemrouten geleitet (0.0.0.0/0 zum Internet). Verwenden Sie öffentliche IPs für bidirektionalen Zugriff.
  - **Vergleichbar mit AWS IGW**: Beide ermöglichen öffentlichen Internetzugang, aber Azure ist standardmäßig "immer an" für ausgehenden Verkehr; AWS erfordert explizites Anhängen und Routen.
  - **Warum verwenden?**: Einfache öffentliche Bereitstellung für Web-Apps. Kostenlos für grundlegendes Routing.

- **NAT Gateway**:
  - **Was es ist**: Ein verwalteter Dienst in einem öffentlichen Subnetz für rein ausgehenden Internetzugang aus privaten Subnetzen (z. B. für VM-Updates).
  - **Wie es funktioniert**: Teilt sich eine Elastic IP für die Übersetzung; hochverfügbar über AZs hinweg.
  - **Vergleichbar mit AWS NAT Gateway**: Beide bieten sicheren ausgehenden Zugang ohne eingehende Exposition. Azure's Lösung ist standardmäßig integrierter und skalierbarer.
  - **Warum verwenden?**: Schützt private Ressourcen und erlaubt gleichzeitig Einweg-Zugriff. Kosten ~0,045 $/Stunde + Daten.

- **Andere Gateways**:
  - **VPN Gateway**: Für Site-to-Site- oder Point-to-Site-VPNs zum lokalen Standort (wie AWS VGW).
  - **ExpressRoute Gateway**: Private Hochgeschwindigkeitsverbindungen zum lokalen Standort (wie AWS Direct Connect).

#### Andere verwandte Komponenten ("Etc.")
- **Routingtabellen**: Steuern den Datenfluss im Subnetz (z. B. zum Internet oder zu gepaarten VNets). Systemstandards existieren; benutzerdefinierte Tabellen überschreiben sie für spezifische Routen. Vergleichbar mit AWS-Routingtabellen, aber Azure propagiert BGP-Routen dynamisch vom lokalen Standort.
- **Netzwerksicherheitsgruppen (NSGs)**: Zustandsbehaftete Firewalls für Subnetze oder Ressourcen mit Regeln nach IP/Port/Protokoll. Ähnlich einer Kombination aus AWS Security Groups (Instanzebene, zustandsbehaftet) und NACLs (Subnetzebene, aber Azure's sind zustandsbehaftet). Verwenden Sie Application Security Groups für logische Tagging.
- **VNet-Peering**: Verbindet VNets (gleiche/verschiedene Regionen/Konten) für privaten Datenverkehr, wie AWS VPC Peering.
- **Dienstendpunkte/Private Link**: Sicherer, privater Zugriff auf Azure-Dienste (z. B. Storage) ohne Internet, ähnlich wie AWS VPC Endpoints.
- **Virtuelle Netzwerkgeräte**: VM-basierte Firewalls oder Router im VNet, ähnlich wie AWS Network Firewall.

#### Wie alles zusammenpasst
1. Erstellen Sie ein VNet mit CIDR.
2. Fügen Sie Subnetze (öffentlich/privat) hinzu, die sich über AZs erstrecken.
3. Ressourcen erhalten standardmäßig ausgehenden Internetzugang; fügen Sie öffentliche IPs/Load Balancers für eingehenden Verkehr hinzu.
4. Verwenden Sie NAT Gateway für ausgehenden Verkehr aus privaten Subnetzen.
5. Wenden Sie Routingtabellen und NSGs zur Datenflusskontrolle an.
6. Peeren Sie VNets oder fügen Sie Gateways für Hybrid-Setups hinzu.

Azure's Modell betont Standardeinstellungen (z. B. ausgehender Internetzugang) für einen schnelleren Setup, während AWS mehr granulare Optionen bietet. Beide priorisieren Sicherheit und Resilienz.

Für praktische Erfahrungen probieren Sie den VNet-Assistenten im Azure-Portal aus.

[Azure Virtual Network – Übersicht](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)