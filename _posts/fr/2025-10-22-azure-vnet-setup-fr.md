---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de configuration de réseau virtuel Azure
translated: true
type: note
---

### Présentation de la configuration du réseau virtuel Azure

Pour mettre en place l'architecture décrite dans Azure, nous utiliserons un seul réseau virtuel (VNet) par souci de simplicité, avec plusieurs sous-réseaux pour séparer les ressources exposées publiquement (comme votre API et le service d'administration) de celles qui sont internes (comme la machine virtuelle MQ/Redis). Cela permet une communication interne sécurisée via des adresses IP privées tout en contrôlant l'accès public via les Groupes de sécurité réseau (NSG). Nous configurerons également un accès SSH restreint aux plages d'adresses IP de votre équipe.

Principes clés :
- **Accès public** : Utilisez des adresses IP publiques et des NSG pour autoriser le trafic entrant uniquement sur des ports spécifiques (443 pour l'API, 80 pour l'administration) depuis Internet ou les IPs de l'équipe.
- **Communication interne** : Les machines virtuelles dans le même VNet peuvent communiquer librement via les adresses IP privées ; utilisez les NSG pour un réglage fin (par exemple, autoriser le backend vers MQ sur le port 6379 pour Redis).
- **Accès SSH** : Restreignez-le au bastion ou au SSH direct sur le port 22 depuis les IPs de l'équipe.
- **Service d'administration** : Traitez-le comme l'API mais sur le port 80, restreint à l'équipe.

Ceci suppose que vous utilisez le Portail Azure ou l'interface CLI ; je fournirai des étapes générales avec des exemples CLI pour la reproductibilité. Des coûts s'appliquent pour les VNets, les machines virtuelles et les adresses IP publiques.

#### Étape 1 : Créer le réseau virtuel et les sous-réseaux
Créez un VNet avec deux sous-réseaux :
- **Sous-réseau Public** (par exemple, pour les machines virtuelles d'API et d'administration) : Autorise les adresses IP publiques.
- **Sous-réseau Privé** (par exemple, pour la machine virtuelle MQ/Redis) : Aucune adresse IP publique ; interne uniquement.

En utilisant Azure CLI (installez-le via `az login` d'abord) :

```bash
# Créer un groupe de ressources
az group create --name myResourceGroup --location eastus

# Créer un VNet
az network vnet create \
  --resource-group myResourceGroup \
  --name myVNet \
  --address-prefixes 10.0.0.0/16 \
  --subnet-name PublicSubnet \
  --subnet-prefixes 10.0.1.0/24

# Ajouter un sous-réseau privé
az network vnet subnet create \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PrivateSubnet \
  --address-prefixes 10.0.2.0/24
```

#### Étape 2 : Créer les machines virtuelles et assigner la mise en réseau
- **Machine virtuelle Backend API** (dans PublicSubnet) : Adresse IP publique pour l'accès sur le port 443.
- **Machine virtuelle MQ/Redis** (dans PrivateSubnet) : Adresse IP privée uniquement.
- **Machine virtuelle d'Administration** (dans PublicSubnet) : Adresse IP publique pour l'accès sur le port 80.

Exemples CLI :

```bash
# Machine virtuelle Backend API
az vm create \
  --resource-group myResourceGroup \
  --name backendVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PublicSubnet \
  --public-ip-sku Standard

# Obtenir l'adresse IP publique pour l'API
API_PUBLIC_IP=$(az vm show -d -g myResourceGroup -n backendVM --query publicIps -o tsv)

# Machine virtuelle MQ/Redis (sans adresse IP publique)
az vm create \
  --resource-group myResourceGroup \
  --name mqVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PrivateSubnet

# Obtenir l'adresse IP privée pour la communication interne
MQ_PRIVATE_IP=$(az vm show -g myResourceGroup -n mqVM --query privateIps -o tsv)

# Machine virtuelle d'Administration
az vm create \
  --resource-group myResourceGroup \
  --name adminVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PublicSubnet \
  --public-ip-sku Standard

# Obtenir l'adresse IP publique pour l'administration
ADMIN_PUBLIC_IP=$(az vm show -d -g myResourceGroup -n adminVM --query publicIps -o tsv)
```

Sur les machines virtuelles :
- Installez votre API sur backendVM (par exemple, écoute sur le port 443 avec SSL).
- Installez Redis/MQ sur mqVM (écoute sur le port 6379).
- Installez le service d'administration sur adminVM (écoute sur le port 80).

#### Étape 3 : Configurer les Groupes de sécurité réseau (NSG)
Les NSG agissent comme des pare-feux. Associez un NSG par sous-réseau (ou par carte réseau pour un contrôle plus fin). Créez des règles pour autoriser :
- Public : 443 vers backendVM, 80 vers adminVM.
- Interne : Backend vers MQ sur le port 6379.
- SSH : Port 22 depuis les IPs de l'équipe (remplacez `TEAM_IPS` par votre CIDR, par exemple 203.0.113.0/24).

CLI pour les NSG :

```bash
# Créer un NSG pour le Sous-réseau Public
az network nsg create \
  --resource-group myResourceGroup \
  --name publicNSG

# Règles pour le NSG public
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

# Associer le NSG public au PublicSubnet
az network vnet subnet update \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PublicSubnet \
  --network-security-group publicNSG

# Créer un NSG pour le Sous-réseau Privé
az network nsg create \
  --resource-group myResourceGroup \
  --name privateNSG

# Autoriser le trafic interne du backend vers MQ
az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name privateNSG \
  --name AllowFromBackend \
  --priority 100 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefixes '10.0.1.0/24'  # CIDR du PublicSubnet
  --source-port-ranges '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges 6379  # Port Redis

# Autoriser le SSH vers la machine virtuelle privée si nécessaire (depuis l'équipe via bastion ou VPN)
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

# Associer le NSG privé
az network vnet subnet update \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PrivateSubnet \
  --network-security-group privateNSG
```

- **Communication Interne** : BackendVM (10.0.1.x) peut maintenant atteindre mqVM (10.0.2.x:6379) sans exposition publique.
- **Refus par défaut** : Les NSG refusent implicitement tout autre trafic.

#### Étape 4 : Accès SSH pour l'équipe
- SSH direct : Utilisez `ssh azureuser@<VM_PUBLIC_IP> -p 22` depuis les IPs de l'équipe (déjà autorisé dans le NSG).
- Pour la machine virtuelle privée : Utilisez Azure Bastion (recommandé pour la sécurité) dans le VNet.
  - Créer Bastion : `az network bastion create --name myBastion --resource-group myResourceGroup --vnet-name myVNet --location eastus --sku Standard --bastion-subnet-address-prefix 10.0.3.0/26` (ajoutez d'abord un nouveau BastionSubnet).
  - Connectez-vous via Portail Azure > Bastion > Connectez-vous à mqVM en utilisant l'adresse IP privée.

#### Étape 5 : Accéder aux services
- **API Publique** : `https://$API_PUBLIC_IP` (port 443).
- **Service d'Administration** : `http://$ADMIN_PUBLIC_IP` (port 80, réservé à l'équipe).
- **Test Interne** : Depuis backendVM, `redis-cli -h $MQ_PRIVATE_IP -p 6379`.

#### Bonnes pratiques supplémentaires
- **Load Balancer/Application Gateway** : Pour la production, placez l'API/l'administration derrière Azure Application Gateway pour le WAF/la terminaison SSL.
- **Private Endpoints** : Pour Redis, utilisez Azure Private Link pour éviter l'exposition du sous-réseau.
- **Monitoring** : Activez Azure Network Watcher pour les logs de trafic.
- **Mise à l'échelle** : Si les machines virtuelles augmentent, utilisez des Availability Sets ou des Scale Sets.
- **Nettoyage** : `az group delete --name myResourceGroup --yes --no-wait`.

Pour la documentation complète : [Vue d'ensemble du réseau virtuel Azure](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview), [Règles NSG](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview). Si vous avez besoin de modèles Terraform/ARM ou de détails spécifiques (par exemple, les IPs exactes de l'équipe), fournissez plus de détails !