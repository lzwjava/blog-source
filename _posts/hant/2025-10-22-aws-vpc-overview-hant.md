---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: AWS 虛擬私有雲概覽
translated: true
type: note
---

### 什麼是 AWS 中的 VPC？

Amazon Virtual Private Cloud（VPC）是一項基礎性的 AWS 服務，可讓您在 AWS 雲端中建立邏輯隔離的區域，用於啟動和管理您的 AWS 資源，例如 EC2 執行個體、資料庫和負載平衡器。它本質上為您在 AWS 內提供了一個私有、可自訂的虛擬網路環境，類似於您設置傳統資料中心網路的方式，但具備雲端的可擴展性和安全性。

#### 關鍵組件與功能
- **子網路**：將您的 VPC 劃分為更小的區段（公共或私有），以組織資源並控制存取。
- **隔離性**：您的 VPC 專屬於您的 AWS 帳戶，並與其他 VPC 隔離，確保安全性和合規性。
- **IP 位址分配**：您可以定義自己的 IP 位址範圍（CIDR 區塊），並可使用 IPv4、IPv6 或兩者兼用。
- **路由與閘道**：包括路由表、網際網路閘道（用於公共存取）、NAT 閘道（用於私有輸出流量）以及 VPC 對等連接（用於連接多個 VPC）。
- **安全性**：內建工具如安全群組（執行個體層級防火牆）和網路 ACL（子網路層級防火牆），用於控制輸入/輸出流量。

#### 為何使用 VPC？
預設情況下，所有 AWS 資源都會啟動到 VPC 中（您無法再選擇退出）。它提供了對網路控制的權限，通過保持資源私有來增強安全性，並支援混合設置（例如，通過 VPN 或 Direct Connect 連接到本地資料中心）。對於生產工作負載來說，避免將資源直接暴露於網際網路是至關重要的。

如需實際設置，請查看 AWS Management Console 或 CLI 來建立您的第一個 VPC。

#### 參考資料
- [什麼是 Amazon VPC？](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [Amazon VPC 概述](https://aws.amazon.com/vpc/)
- [Amazon VPC 運作原理](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html)
- [Amazon VPC 簡介](https://www.geeksforgeeks.org/devops/amazon-vpc-introduction-to-amazon-virtual-cloud/)