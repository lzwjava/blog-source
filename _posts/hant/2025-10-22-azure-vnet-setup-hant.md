---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Azure 虛擬網絡設定指南
translated: true
type: note
---

### Azure 虛擬網絡配置概覽

為了在 Azure 中設置您描述的架構，我們將使用單一虛擬網絡（VNet）以簡化操作，並透過多個子網段來分隔面向公眾的資源（如您的 API 和管理服務）與內部資源（如 MQ/Redis 虛擬機器）。這允許透過私有 IP 進行安全的內部通訊，同時透過網絡安全組（NSGs）控制公眾存取。我們還將配置僅限您團隊 IP 範圍的 SSH 存取。

關鍵原則：
- **公眾存取**：使用公共 IP 和 NSGs，僅允許來自網際網路或團隊 IP 的特定端口（API 使用 443，管理服務使用 80）的入站流量。
- **內部通訊**：同一 VNet 中的虛擬機器可以透過私有 IP 自由通訊；使用 NSGs 進行微調（例如，允許後端在端口 6379 上存取 MQ 以用於 Redis）。
- **SSH 存取**：僅限從團隊 IP 透過堡壘主機或直接 SSH 在端口 22 上進行。
- **管理服務**：將其視為 API，但使用端口 80，並僅限團隊存取。

這假設您使用 Azure 入口網站或 CLI；我將提供帶有 CLI 示例的高階步驟以確保可重現性。VNet、虛擬機器和公共 IP 均會產生費用。

#### 步驟 1：建立虛擬網絡和子網段
建立一個包含兩個子網段的 VNet：
- **公共子網段**（例如，用於 API 和管理虛擬機器）：允許公共 IP。
- **私有子網段**（例如，用於 MQ/Redis 虛擬機器）：無公共 IP；僅限內部存取。

使用 Azure CLI（請先透過 `az login` 安裝）：

```bash
# 建立資源群組
az group create --name myResourceGroup --location eastus

# 建立 VNet
az network vnet create \
  --resource-group myResourceGroup \
  --name myVNet \
  --address-prefixes 10.0.0.0/16 \
  --subnet-name PublicSubnet \
  --subnet-prefixes 10.0.1.0/24

# 新增私有子網段
az network vnet subnet create \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PrivateSubnet \
  --address-prefixes 10.0.2.0/24
```

#### 步驟 2：建立虛擬機器並分配網絡配置
- **後端 API 虛擬機器**（位於 PublicSubnet）：公共 IP 用於 443 存取。
- **MQ/Redis 虛擬機器**（位於 PrivateSubnet）：僅私有 IP。
- **管理虛擬機器**（位於 PublicSubnet）：公共 IP 用於 80 存取。

CLI 示例：

```bash
# 後端 API 虛擬機器
az vm create \
  --resource-group myResourceGroup \
  --name backendVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PublicSubnet \
  --public-ip-sku Standard

# 取得 API 的公共 IP
API_PUBLIC_IP=$(az vm show -d -g myResourceGroup -n backendVM --query publicIps -o tsv)

# MQ/Redis 虛擬機器（無公共 IP）
az vm create \
  --resource-group myResourceGroup \
  --name mqVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PrivateSubnet

# 取得內部通訊的私有 IP
MQ_PRIVATE_IP=$(az vm show -g myResourceGroup -n mqVM --query privateIps -o tsv)

# 管理虛擬機器
az vm create \
  --resource-group myResourceGroup \
  --name adminVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PublicSubnet \
  --public-ip-sku Standard

# 取得管理服務的公共 IP
ADMIN_PUBLIC_IP=$(az vm show -d -g myResourceGroup -n adminVM --query publicIps -o tsv)
```

在虛擬機器上：
- 在 backendVM 上安裝您的 API（例如，在 443 端口上監聽並使用 SSL）。
- 在 mqVM 上安裝 Redis/MQ（在 6379 端口上監聽）。
- 在 adminVM 上安裝管理服務（在 80 端口上監聽）。

#### 步驟 3：配置網絡安全組（NSGs）
NSGs 充當防火牆。為每個子網段（或每個網絡介面卡以進行更精細的控制）關聯一個 NSG。建立規則以允許：
- 公眾：443 到 backendVM，80 到 adminVM。
- 內部：後端到 MQ 在 6379 端口。
- SSH：從團隊 IP 的端口 22（將 `TEAM_IPS` 替換為您的 CIDR，例如 203.0.113.0/24）。

NSGs 的 CLI：

```bash
# 為公共子網段建立 NSG
az network nsg create \
  --resource-group myResourceGroup \
  --name publicNSG

# 公共 NSG 的規則
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

# 將公共 NSG 關聯到 PublicSubnet
az network vnet subnet update \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PublicSubnet \
  --network-security-group publicNSG

# 為私有子網段建立 NSG
az network nsg create \
  --resource-group myResourceGroup \
  --name privateNSG

# 允許從後端到 MQ 的內部流量
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
  --destination-port-ranges 6379  # Redis 端口

# 如果需要，允許 SSH 到私有虛擬機器（從團隊透過堡壘主機或 VPN）
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

# 關聯私有 NSG
az network vnet subnet update \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PrivateSubnet \
  --network-security-group privateNSG
```

- **內部通訊**：BackendVM (10.0.1.x) 現在可以無需公共暴露即可連接到 mqVM (10.0.2.x:6379)。
- **預設拒絕**：NSGs 隱含拒絕所有其他流量。

#### 步驟 4：團隊的 SSH 存取
- 直接 SSH：從團隊 IP 使用 `ssh azureuser@<VM_PUBLIC_IP> -p 22`（已在 NSG 中允許）。
- 對於私有虛擬機器：使用 VNet 中的 Azure Bastion（建議為了安全）。
  - 建立 Bastion：`az network bastion create --name myBastion --resource-group myResourceGroup --vnet-name myVNet --location eastus --sku Standard --bastion-subnet-address-prefix 10.0.3.0/26`（請先新增 BastionSubnet）。
  - 透過 Azure 入口網站 > Bastion > 使用私有 IP 連接到 mqVM。

#### 步驟 5：存取服務
- **公共 API**：`https://$API_PUBLIC_IP`（端口 443）。
- **管理服務**：`http://$ADMIN_PUBLIC_IP`（端口 80，僅限團隊）。
- **測試內部**：從 backendVM，使用 `redis-cli -h $MQ_PRIVATE_IP -p 6379`。

#### 其他最佳實踐
- **負載平衡器/應用程式閘道**：在生產環境中，使用 Azure 應用程式閘道來前置 API/管理服務，以實現 WAF/SSL 終止。
- **私有端點**：對於 Redis，使用 Azure Private Link 以避免子網段暴露。
- **監控**：啟用 Azure Network Watcher 以獲取流量日誌。
- **擴展**：如果虛擬機器增加，請使用可用性設定組或擴展集。
- **清理**：`az group delete --name myResourceGroup --yes --no-wait`。

完整文件：[Azure VNet 概覽](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)、[NSG 規則](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)。如果您需要 Terraform/ARM 模板或具體細節（例如確切的團隊 IP），請提供更多詳細資訊！