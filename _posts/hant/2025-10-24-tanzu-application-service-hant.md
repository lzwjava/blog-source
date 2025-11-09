---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: VMware Tanzu 應用服務概覽
translated: true
type: note
---

## VMware Tanzu Application Service for VMs（TAS for VMs）簡介

VMware Tanzu Application Service for VMs（TAS for VMs）是基於開源專案 Cloud Foundry 構建的商業平台即服務（PaaS）。它旨在簡化雲原生應用的部署、擴展和管理，讓開發者能專注於編寫代碼，而無需處理基礎架構問題。TAS for VMs 支援在各種環境中快速部署應用，包括本地環境（如 vSphere）或公有雲（AWS、Azure、GCP、OpenStack），並同時支援自主管理設置和經認證的商業供應商。

### 主要功能
- **開源基礎**：利用 Cloud Foundry 的可擴展性避免供應商鎖定，支援多種語言、框架和服務
- **自動化部署**：使用熟悉工具（如 CLI）推送應用而無需修改代碼；應用程式將打包成「droplets」（預編譯套件）以實現快速部署和運行
- **可擴展性與韌性**：使用 Diego 在虛擬機間進行智能負載分配，具備自動擴展和容錯能力，可處理流量激增或故障情況
- **用戶管理**：通過 UAA（用戶帳戶與身份驗證）伺服器將團隊組織為「組織」和「空間」，並提供基於角色的存取權限（如管理員、開發者）
- **服務整合**：通過 Service Brokers 輕鬆將應用與數據庫或 API 等服務綁定，無需修改應用程式代碼
- **監控與日誌記錄**：通過 Loggregator 將日誌和指標匯總到「Firehose」流中，實現即時分析、警報和工具整合
- **精簡版本選項**：僅需 4 個虛擬機即可運行的輕量版本（標準版需 13+ 個），適合小型團隊或測試環境，但存在擴展限制
- **靈活基礎架構**：通過 BOSH（自動化工具）部署，並使用 Tanzu Operations Manager 進行統一配置管理

### 優勢
TAS for VMs 能讓應用在數分鐘內上線，具備自動擴展和全球存取能力，從而加速產品上市時間。它透過分隔的工作空間降低基礎架構開銷、增強安全性，並促進可移植性——應用在不同環境中保持一致性運行。通過抽象化虛擬機管理，它降低了成本與複雜度，同時 Cloud Foundry 社群確保了持續創新與支援。

### 運作原理
TAS for VMs 的核心是多租戶 PaaS：
1. **部署**：使用 Tanzu Operations Manager 在 BOSH 管理的虛擬機上配置和部署平台
2. **應用生命週期**：開發者通過 CLI 推送代碼；Cloud Controller 使用 buildpacks（用於語言特定設置）將其組裝成 droplets，隨後 Diego 在主機虛擬機間進行實例競價和運行
3. **路由與存取**：Gorouter 處理傳入流量，外部進行負載平衡；UAA 進行用戶身份驗證
4. **運維**：內部組件通過 NATS 消息傳遞和 BOSH DNS 進行通訊；blob 和配置等資源存儲在 GitHub、blobstores 或 MySQL 中

TAS for VMs 在開源 Cloud Foundry 基礎上擴展了 VMware 的企業級功能、支援和認證，使其成為生產工作負載的穩健選擇。

詳細資訊請查閱官方文件：[TAS for VMs 概述](https://techdocs.broadcom.com/us/en/vmware-tanzu/platform/tanzu-platform-for-cloud-foundry/6-0/tpcf/concepts-overview.html)