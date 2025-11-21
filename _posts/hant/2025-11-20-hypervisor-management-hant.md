---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Hypervisor 與虛擬機器管理
translated: true
type: note
---

**虛擬機器監視器**（亦稱為**虛擬機器管理程式**或 VMM）是核心軟體（有時是韌體/硬體），用於在實體主機電腦上建立、執行及管理**虛擬機器 (VM)**。它透過抽象化並共享實體硬體資源（CPU、記憶體、儲存、網路等）於多個隔離的虛擬機器之間，從而實現虛擬化技術。

### 兩大主要虛擬機器監視器類型

| 類型 | 描述 | 是否直接運行於硬體？ | 範例 | 優點 | 缺點 |
|------|-------------|-----------------------------|----------|------|------|
| **Type 1（裸機式）** | 直接安裝並運行於實體硬體上，虛擬機器監視器下方無宿主作業系統。 | 是 | VMware ESXi、Microsoft Hyper-V（於虛擬機器監視器模式）、Xen、KVM（用於裸機時）、Proxmox VE、Oracle VM Server | 最佳效能、更高安全性、較低系統負載，常用於生產環境/資料中心 | 對初學者較難管理、內建驅動程式/工具較少 |
| **Type 2（宿主式）** | 作為應用程式運行於傳統作業系統（Windows、macOS、Linux）之上，由宿主作業系統掌控硬體。 | 否（運行於宿主作業系統） | VMware Workstation、VMware Fusion、VirtualBox、Parallels Desktop、QEMU（搭配宿主作業系統使用時） | 易於安裝使用、適合桌面/筆記型電腦、可使用宿主作業系統驅動程式及工具 | 效能略低、因宿主作業系統而存在較大攻擊面 |

### 虛擬機器監視器運作原理（簡化版）

1. **資源抽象化** – 虛擬機器監視器為每個虛擬機器提供虛擬 CPU (vCPU)、虛擬記憶體、虛擬磁碟、虛擬網路卡等資源。
2. **隔離性** – 每個虛擬機器完全隔離；單一虛擬機器當機或遭入侵通常不影響其他虛擬機器。
3. **排程機制** – 虛擬機器監視器排程哪個虛擬機器可在特定時刻使用實體 CPU/記憶體（分時共享）。
4. **陷阱與模擬** – 當虛擬機器嘗試執行特權指令（例如變更分頁表、存取硬體）時，CPU 會陷入虛擬機器監視器，由其安全地模擬或處理請求。
5. **硬體加速** – 現代 CPU 具備虛擬化擴充功能（Intel VT-x、AMD-V），可極速執行陷阱與模擬流程（接近原生效能）。

### 常見應用場景

- 伺服器整合（單一實體伺服器運行數十個虛擬機器）
- 雲端運算（AWS EC2、Azure VM、GCP Compute Engine 底層皆使用虛擬機器監視器）
- 開發/測試環境
- 桌面虛擬化（在 macOS 上運行 Windows 或並行多個 Linux 發行版）
- 安全沙箱與惡意軟體分析

### 現今主流虛擬機器監視器（2025 年）

- **VMware ESXi** – 企業市場主流（現隸屬 Broadcom）
- **Microsoft Hyper-V** – 內建於 Windows Server 及 Windows 10/11 Pro
- **KVM** – Linux 預設虛擬化方案，驅動多數 OpenStack 與公有雲（Google Cloud、AWS Nitro 等）
- **Proxmox VE** – 基於 Debian + KVM + LXC 的開源 Type-1 解決方案
- **Xen** – 被 Oracle Cloud、AWS（舊世代）、XCP-ng 採用
- **VirtualBox** – Oracle 推出的免費 Type-2 方案，個人使用極普及
- **Nutanix AHV** – 適用於超融合基礎架構的 Acropolis Hypervisor（基於 KVM）

簡而言之：虛擬機器監視器如同「樂團指揮」，讓多個作業系統能安全高效地共享同一台實體電腦。Type 1 常見於資料中心與雲端環境；Type 2 則通常由桌面用戶安裝使用。