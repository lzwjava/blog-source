---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de configuración de Azure Virtual Network
translated: true
type: note
---

### Resumen de Configuración de Azure Virtual Network

Para configurar la arquitectura descrita en Azure, utilizaremos una única Virtual Network (VNet) por simplicidad, con múltiples subredes para separar los recursos orientados al público (como su API y servicio de administración) de los internos (como la VM de MQ/Redis). Esto permite una comunicación interna segura a través de IPs privadas mientras se controla el acceso público mediante Network Security Groups (NSGs). También configuraremos el acceso SSH restringido a los rangos de IP de su equipo.

Principios clave:
- **Acceso público**: Utilice IPs públicas y NSGs para permitir tráfico entrante solo en puertos específicos (443 para API, 80 para administración) desde internet o las IPs del equipo.
- **Comunicación interna**: Las VMs en la misma VNet pueden comunicarse libremente mediante IPs privadas; use NSGs para ajustes finos (ej., permitir que el backend se comunique con MQ en el puerto 6379 para Redis).
- **Acceso SSH**: Restrinja a bastion o SSH directo en el puerto 22 desde las IPs del equipo.
- **Servicio de administración**: Trátelo como la API pero en el puerto 80, restringido al equipo.

Esto asume que está usando Azure Portal o la CLI; proporcionaré pasos de alto nivel con ejemplos de CLI para reproducibilidad. Aplican costos por VNets, VMs e IPs públicas.

#### Paso 1: Crear la Virtual Network y las Subredes
Cree una VNet con dos subredes:
- **Subred Pública** (ej., para las VMs de API y administración): Permite IPs públicas.
- **Subred Privada** (ej., para la VM de MQ/Redis): Sin IPs públicas; solo interna.

Usando Azure CLI (instalar primero via `az login`):

```bash
# Crear grupo de recursos
az group create --name myResourceGroup --location eastus

# Crear VNet
az network vnet create \
  --resource-group myResourceGroup \
  --name myVNet \
  --address-prefixes 10.0.0.0/16 \
  --subnet-name PublicSubnet \
  --subnet-prefixes 10.0.1.0/24

# Añadir subred privada
az network vnet subnet create \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PrivateSubnet \
  --address-prefixes 10.0.2.0/24
```

#### Paso 2: Crear las VMs y Asignar Redes
- **VM de Backend API** (en PublicSubnet): IP pública para acceso 443.
- **VM de MQ/Redis** (en PrivateSubnet): Solo IP privada.
- **VM de Administración** (en PublicSubnet): IP pública para acceso 80.

Ejemplos de CLI:

```bash
# VM de Backend API
az vm create \
  --resource-group myResourceGroup \
  --name backendVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PublicSubnet \
  --public-ip-sku Standard

# Obtener IP pública para la API
API_PUBLIC_IP=$(az vm show -d -g myResourceGroup -n backendVM --query publicIps -o tsv)

# VM de MQ/Redis (sin IP pública)
az vm create \
  --resource-group myResourceGroup \
  --name mqVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PrivateSubnet

# Obtener IP privada para comunicación interna
MQ_PRIVATE_IP=$(az vm show -g myResourceGroup -n mqVM --query privateIps -o tsv)

# VM de Administración
az vm create \
  --resource-group myResourceGroup \
  --name adminVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PublicSubnet \
  --public-ip-sku Standard

# Obtener IP pública para administración
ADMIN_PUBLIC_IP=$(az vm show -d -g myResourceGroup -n adminVM --query publicIps -o tsv)
```

En las VMs:
- Instale su API en backendVM (ej., escuchando en 443 con SSL).
- Instale Redis/MQ en mqVM (escuchando en 6379).
- Instale el servicio de administración en adminVM (escuchando en 80).

#### Paso 3: Configurar Network Security Groups (NSGs)
Los NSGs actúan como firewalls. Asocie un NSG por subred (o por NIC para un control más fino). Cree reglas para permitir:
- Público: 443 a backendVM, 80 a adminVM.
- Interno: Backend a MQ en 6379.
- SSH: Puerto 22 desde las IPs del equipo (reemplace `TEAM_IPS` con su CIDR, ej., 203.0.113.0/24).

CLI para NSGs:

```bash
# Crear NSG para Subred Pública
az network nsg create \
  --resource-group myResourceGroup \
  --name publicNSG

# Reglas para NSG público
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

# Asociar NSG público a PublicSubnet
az network vnet subnet update \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PublicSubnet \
  --network-security-group publicNSG

# Crear NSG para Subred Privada
az network nsg create \
  --resource-group myResourceGroup \
  --name privateNSG

# Permitir tráfico interno desde el backend a MQ
az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name privateNSG \
  --name AllowFromBackend \
  --priority 100 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefixes '10.0.1.0/24'  # CIDR de PublicSubnet
  --source-port-ranges '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges 6379  # Puerto de Redis

# Permitir SSH a VM privada si es necesario (desde el equipo via bastion o VPN)
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

# Asociar NSG privado
az network vnet subnet update \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PrivateSubnet \
  --network-security-group privateNSG
```

- **Comunicación Interna**: BackendVM (10.0.1.x) ahora puede alcanzar mqVM (10.0.2.x:6379) sin exposición pública.
- **Denegación por Defecto**: Los NSGs deniegan implícitamente todo otro tráfico.

#### Paso 4: Acceso SSH para el Equipo
- SSH directo: Use `ssh azureuser@<VM_PUBLIC_IP> -p 22` desde las IPs del equipo (ya permitido en el NSG).
- Para VM privada: Use Azure Bastion (recomendado por seguridad) en la VNet.
  - Crear Bastion: `az network bastion create --name myBastion --resource-group myResourceGroup --vnet-name myVNet --location eastus --sku Standard --bastion-subnet-address-prefix 10.0.3.0/26` (añada primero una nueva BastionSubnet).
  - Conéctese via Azure Portal > Bastion > Connect a mqVM usando la IP privada.

#### Paso 5: Acceder a los Servicios
- **API Pública**: `https://$API_PUBLIC_IP` (puerto 443).
- **Servicio de Administración**: `http://$ADMIN_PUBLIC_IP` (puerto 80, solo equipo).
- **Prueba Interna**: Desde backendVM, `redis-cli -h $MQ_PRIVATE_IP -p 6379`.

#### Mejores Prácticas Adicionales
- **Load Balancer/Application Gateway**: Para producción, ponga la API/administración detrás de Azure Application Gateway para WAF/terminación SSL.
- **Private Endpoints**: Para Redis, use Azure Private Link para evitar la exposición de la subred.
- **Monitoring**: Habilite Azure Network Watcher para logs de tráfico.
- **Escalado**: Si las VMs crecen, use Availability Sets o Scale Sets.
- **Limpieza**: `az group delete --name myResourceGroup --yes --no-wait`.

Para documentación completa: [Azure VNet Overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview), [NSG Rules](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview). Si necesita plantillas de Terraform/ARM o detalles específicos (ej., IPs exactas del equipo), ¡proporcione más detalles!