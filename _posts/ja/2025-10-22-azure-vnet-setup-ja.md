---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Azure仮想ネットワークセットアップガイド
translated: true
type: note
---

### Azure Virtual Network 構成の概要

Azureで説明されたアーキテクチャを設定するには、シンプルにするために単一のVirtual Network (VNet) を使用し、パブリック向けリソース（APIや管理サービスなど）と内部リソース（MQ/Redis VMなど）を分離するために複数のサブネットを設けます。これにより、プライベートIPを介した安全な内部通信を可能にしつつ、Network Security Groups (NSG) を通じてパブリックアクセスを制御できます。また、チームのIP範囲に制限したSSHアクセスも設定します。

基本原則:
- **パブリックアクセス**: パブリックIPとNSGを使用し、特定のポート（API用443、管理用80）へのインターネットまたはチームIPからのインバウンドトラフィックのみを許可します。
- **内部通信**: 同じVNet内のVMはプライベートIPで自由に通信可能。NSGを使用して微調整（例: バックエンドからMQへのRedisポート6379を許可）。
- **SSHアクセス**: チームIPからのポート22へのバスチオンまたは直接SSHを制限。
- **管理サービス**: APIと同様に扱いますが、ポート80を使用し、チームに制限。

これはAzure PortalまたはCLIを使用していることを想定しています。再現性のためにCLI例を用いた大まかな手順を提供します。VNet、VM、パブリックIPにはコストがかかります。

#### ステップ 1: Virtual Networkとサブネットの作成
2つのサブネットを持つVNetを作成:
- **パブリックサブネット** (例: APIおよび管理VM用): パブリックIPを許可。
- **プライベートサブネット** (例: MQ/Redis VM用): パブリックIPなし。内部のみ。

Azure CLIを使用（最初に `az login` でインストール）:

```bash
# リソースグループの作成
az group create --name myResourceGroup --location eastus

# VNetの作成
az network vnet create \
  --resource-group myResourceGroup \
  --name myVNet \
  --address-prefixes 10.0.0.0/16 \
  --subnet-name PublicSubnet \
  --subnet-prefixes 10.0.1.0/24

# プライベートサブネットの追加
az network vnet subnet create \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PrivateSubnet \
  --address-prefixes 10.0.2.0/24
```

#### ステップ 2: VMの作成とネットワーク割り当て
- **バックエンドAPI VM** (PublicSubnet内): 443アクセス用のパブリックIP。
- **MQ/Redis VM** (PrivateSubnet内): プライベートIPのみ。
- **管理VM** (PublicSubnet内): 80アクセス用のパブリックIP。

CLI例:

```bash
# バックエンドAPI VM
az vm create \
  --resource-group myResourceGroup \
  --name backendVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PublicSubnet \
  --public-ip-sku Standard

# APIのパブリックIP取得
API_PUBLIC_IP=$(az vm show -d -g myResourceGroup -n backendVM --query publicIps -o tsv)

# MQ/Redis VM (パブリックIPなし)
az vm create \
  --resource-group myResourceGroup \
  --name mqVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PrivateSubnet

# 内部通信用プライベートIP取得
MQ_PRIVATE_IP=$(az vm show -g myResourceGroup -n mqVM --query privateIps -o tsv)

# 管理VM
az vm create \
  --resource-group myResourceGroup \
  --name adminVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --admin-password <strong-password> \
  --vnet-name myVNet \
  --subnet PublicSubnet \
  --public-ip-sku Standard

# 管理用パブリックIP取得
ADMIN_PUBLIC_IP=$(az vm show -d -g myResourceGroup -n adminVM --query publicIps -o tsv)
```

VM上で:
- backendVMにAPIをインストール（例: SSLで443をリッスン）。
- mqVMにRedis/MQをインストール（6379をリッスン）。
- adminVMに管理サービスをインストール（80をリッスン）。

#### ステップ 3: Network Security Groups (NSG) の設定
NSGはファイアウォールとして機能します。サブネットごと（またはより細かい制御のためにNICごと）にNSGを関連付けます。以下の許可ルールを作成:
- パブリック: backendVMへの443、adminVMへの80。
- 内部: バックエンドからMQへの6379。
- SSH: チームIPからのポート22（`TEAM_IPS` をCIDR、例: 203.0.113.0/24 に置き換え）。

NSG用CLI:

```bash
# パブリックサブネット用NSG作成
az network nsg create \
  --resource-group myResourceGroup \
  --name publicNSG

# パブリックNSGのルール
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

# パブリックNSGをPublicSubnetに関連付け
az network vnet subnet update \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PublicSubnet \
  --network-security-group publicNSG

# プライベートサブネット用NSG作成
az network nsg create \
  --resource-group myResourceGroup \
  --name privateNSG

# バックエンドからMQへの内部トラフィック許可
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
  --destination-port-ranges 6379  # Redisポート

# 必要に応じてプライベートVMへのSSH許可（チームからバスチオンまたはVPN経由）
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

# プライベートNSGの関連付け
az network vnet subnet update \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name PrivateSubnet \
  --network-security-group privateNSG
```

- **内部通信**: BackendVM (10.0.1.x) はパブリック公開なしで mqVM (10.0.2.x:6379) に到達可能。
- **デフォルト拒否**: NSGは他のすべてのトラフィックを暗黙的に拒否。

#### ステップ 4: チームのSSHアクセス
- 直接SSH: チームIPから `ssh azureuser@<VM_PUBLIC_IP> -p 22` を使用（NSGですでに許可）。
- プライベートVM用: VNet内でAzure Bastion（セキュリティのために推奨）を使用。
  - Bastion作成: `az network bastion create --name myBastion --resource-group myResourceGroup --vnet-name myVNet --location eastus --sku Standard --bastion-subnet-address-prefix 10.0.3.0/26`（最初に新しいBastionSubnetを追加）。
  - Azure Portal > Bastion > Connect からプライベートIPを使用して mqVM に接続。

#### ステップ 5: サービスへのアクセス
- **パブリックAPI**: `https://$API_PUBLIC_IP` (ポート443)。
- **管理サービス**: `http://$ADMIN_PUBLIC_IP` (ポート80、チームのみ)。
- **内部テスト**: backendVMから `redis-cli -h $MQ_PRIVATE_IP -p 6379`。

#### 追加のベストプラクティス
- **ロードバランサー/Application Gateway**: 本番環境では、API/管理の前にAzure Application Gatewayを配置してWAF/SSL終端。
- **プライベートエンドポイント**: RedisにはAzure Private Linkを使用してサブネット公開を回避。
- **監視**: トラフィックログのためにAzure Network Watcherを有効化。
- **スケーリング**: VMが増加する場合、Availability SetsまたはScale Setsを使用。
- **クリーンアップ**: `az group delete --name myResourceGroup --yes --no-wait`。

完全なドキュメント: [Azure VNet Overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview), [NSG Rules](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)。Terraform/ARMテンプレートや詳細（例: 正確なチームIP）が必要な場合は、詳細を提供してください！