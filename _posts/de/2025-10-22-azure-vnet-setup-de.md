---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Azure Virtual Network Einrichtungsleitfaden
translated: true
type: note
---

### Übersicht der Azure Virtual Network-Konfiguration

Um Ihre beschriebene Architektur in Azure einzurichten, verwenden wir der Einfachheit halber ein einzelnes Virtual Network (VNet) mit mehreren Subnetzen, um öffentlich zugängliche Ressourcen (wie Ihren API- und Admin-Dienst) von internen Ressourcen (wie der MQ/Redis-VM) zu trennen. Dies ermöglicht eine sichere interne Kommunikation über private IPs, während der öffentliche Zugriff über Network Security Groups (NSGs) gesteuert wird. Wir konfigurieren auch SSH-Zugriff, der auf die IP-Bereiche Ihres Teams beschränkt ist.

Wichtige Grundsätze:
- **Öffentlicher Zugriff**: Verwenden Sie öffentliche IPs und NSGs, um eingehenden Datenverkehr nur auf bestimmten Ports (443 für API, 80 für Admin) aus dem Internet oder von Team-IPs zu erlauben.
- **Interne Kommunikation**: VMs im selben VNet können frei über private IPs kommunizieren; verwenden Sie NSGs zur Feinabstimmung (z.B. Backend zu MQ auf Port 6379 für Redis erlauben).
- **SSH-Zugriff**: Auf Bastion oder direkten SSH auf Port 22 von Team-IPs beschränken.
- **Admin-Dienst**: Behandeln Sie ihn wie die API, aber auf Port 80 und auf das Team beschränkt.

Dies setzt voraus, dass Sie das Azure Portal oder die CLI verwenden; ich werde allgemeine Schritte mit CLI-Beispielen zur Reproduzierbarkeit bereitstellen. Für VNets, VMs und öffentliche IPs fallen Kosten an.

#### Schritt 1: Erstellen des Virtual Networks und der Subnetze
Erstellen Sie ein VNet mit zwei Subnetzen:
- **Öffentliches Subnetz** (z.B. für API- und Admin-VMs): Erlaubt öffentliche IPs.
- **Privates Subnetz** (z.B. für MQ/Redis-VM): Keine öffentlichen IPs; nur intern.

Verwendung der Azure CLI (zuerst `az login` ausführen):

```bash
# Ressourcengruppe erstellen
az group create --name myResourceGroup --location eastus

# VNet erstellen
az network vnet create \
  --resource-group myResourceGroup \
  --name myVNet \
  --address-prefixes 10.0.0.0/16 \
  --subnet-name PublicSubnet \
  --subnet-prefixes 10.0.1.0/24

# Privates Subnetz hinzufügen
az network vnet subnet create \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PrivateSubnet \
  --address-prefixes 10.0.2.0/24
```

#### Schritt 2: Erstellen von VMs und Zuweisen der Netzwerkkonfiguration
- **Backend-API-VM** (in PublicSubnet): Öffentliche IP für 443-Zugriff.
- **MQ/Redis-VM** (in PrivateSubnet): Nur private IP.
- **Admin-VM** (in PublicSubnet): Öffentliche IP für 80-Zugriff.

CLI-Beispiele:

```bash
# Backend-API-VM
az vm create \
  --resource-group myResourceGroup \
  --name backendVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PublicSubnet \
  --public-ip-sku Standard

# Öffentliche IP für API abrufen
API_PUBLIC_IP=$(az vm show -d -g myResourceGroup -n backendVM --query publicIps -o tsv)

# MQ/Redis-VM (keine öffentliche IP)
az vm create \
  --resource-group myResourceGroup \
  --name mqVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PrivateSubnet

# Private IP für interne Kommunikation abrufen
MQ_PRIVATE_IP=$(az vm show -g myResourceGroup -n mqVM --query privateIps -o tsv)

# Admin-VM
az vm create \
  --resource-group myResourceGroup \
  --name adminVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PublicSubnet \
  --public-ip-sku Standard

# Öffentliche IP für Admin abrufen
ADMIN_PUBLIC_IP=$(az vm show -d -g myResourceGroup -n adminVM --query publicIps -o tsv)
```

Auf den VMs:
- Installieren Sie Ihre API auf backendVM (z.B. Lauschen auf 443 mit SSL).
- Installieren Sie Redis/MQ auf mqVM (Lauschen auf 6379).
- Installieren Sie den Admin-Dienst auf adminVM (Lauschen auf 80).

#### Schritt 3: Konfigurieren der Network Security Groups (NSGs)
NSGs fungieren als Firewalls. Weisen Sie jedem Subnetz eine NSG zu (oder jeder NIC für feinere Kontrolle). Erstellen Sie Regeln, um zu erlauben:
- Öffentlich: 443 zu backendVM, 80 zu adminVM.
- Intern: Backend zu MQ auf 6379.
- SSH: Port 22 von Team-IPs (ersetzen Sie `TEAM_IPS` durch Ihr CIDR, z.B. 203.0.113.0/24).

CLI für NSGs:

```bash
# NSG für öffentliches Subnetz erstellen
az network nsg create \
  --resource-group myResourceGroup \
  --name publicNSG

# Regeln für öffentliche NSG
az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name publicNSG \
  --name AllowHTTPS \
  --priority 100 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefixes '*' \
  --source-port-ranges '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges 443

az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name publicNSG \
  --name AllowHTTPAdmin \
  --priority 101 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefixes 'TEAM_IPS' \
  --source-port-ranges '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges 80

az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name publicNSG \
  --name AllowSSH \
  --priority 102 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefixes 'TEAM_IPS' \
  --source-port-ranges '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges 22

# Öffentliche NSG dem PublicSubnet zuweisen
az network vnet subnet update \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PublicSubnet \
  --network-security-group publicNSG

# NSG für privates Subnetz erstellen
az network nsg create \
  --resource-group myResourceGroup \
  --name privateNSG

# Internen Datenverkehr vom Backend zu MQ erlauben
az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name privateNSG \
  --name AllowFromBackend \
  --priority 100 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefixes '10.0.1.0/24'  # PublicSubnet CIDR
  --source-port-ranges '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges 6379  # Redis-Port

# SSH zu privater VM erlauben, falls benötigt (vom Team über Bastion oder VPN)
az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name privateNSG \
  --name AllowSSHPrivate \
  --priority 101 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefixes 'TEAM_IPS' \
  --source-port-ranges '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges 22

# Private NSG zuweisen
az network vnet subnet update \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PrivateSubnet \
  --network-security-group privateNSG
```

- **Interne Kommunikation**: BackendVM (10.0.1.x) kann jetzt mqVM (10.0.2.x:6379) ohne öffentliche Exposition erreichen.
- **Standardverweigerung**: NSGs verweigern implizit allen anderen Datenverkehr.

#### Schritt 4: SSH-Zugriff für das Team
- Direkter SSH: Verwenden Sie `ssh azureuser@<VM_PUBLIC_IP> -p 22` von Team-IPs (bereits in NSG erlaubt).
- Für private VM: Verwenden Sie Azure Bastion (aus Sicherheitsgründen empfohlen) im VNet.
  - Bastion erstellen: `az network bastion create --name myBastion --resource-group myResourceGroup --vnet-name myVNet --location eastus --sku Standard --bastion-subnet-address-prefix 10.0.3.0/26` (zuerst ein neues BastionSubnet hinzufügen).
  - Verbinden über Azure Portal > Bastion > Verbindung zu mqVM mit privater IP.

#### Schritt 5: Auf die Dienste zugreifen
- **Öffentliche API**: `https://$API_PUBLIC_IP` (Port 443).
- **Admin-Dienst**: `http://$ADMIN_PUBLIC_IP` (Port 80, nur Team).
- **Intern testen**: Von backendVM, `redis-cli -h $MQ_PRIVATE_IP -p 6379`.

#### Zusätzliche Best Practices
- **Load Balancer/Application Gateway**: Für Produktion, setzen Sie die API/Admin hinter Azure Application Gateway für WAF/SSL-Terminierung.
- **Private Endpoints**: Für Redis, verwenden Sie Azure Private Link, um Subnetz-Exposition zu vermeiden.
- **Monitoring**: Aktivieren Sie Azure Network Watcher für Verkehrsprotokolle.
- **Skalierung**: Wenn VMs wachsen, verwenden Sie Availability Sets oder Scale Sets.
- **Bereinigung**: `az group delete --name myResourceGroup --yes --no-wait`.

Für vollständige Dokumentation: [Azure VNet Overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview), [NSG Rules](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview). Wenn Sie Terraform/ARM-Vorlagen oder Details (z.B. genaue Team-IPs) benötigen, geben Sie weitere Details an!