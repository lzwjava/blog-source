---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 安納普爾納實驗室：AWS 客製化晶片
translated: true
type: note
---

### 什麼是 Annapurna Labs？

**Annapurna Labs** 是一家以色列半導體公司，專注於為雲端運算、網絡、儲存及 AI 工作負載設計**高效能、低功耗處理器**。該公司於 **2015 年 1 月被亞馬遜以約 3.5–3.7 億美元收購**，現為 **Amazon Web Services (AWS)** 全資子公司。

Annapurna Labs 設計的**客製化晶片**驅動了 AWS 大部分基礎設施，使亞馬遜能在特定工作負載上減少對 Intel、Broadcom 及 NVIDIA 等第三方晶片供應商的依賴。

---

### Annapurna Labs 設計的關鍵晶片（用於 AWS）

| 晶片系列 | 類型 | 關鍵特性 | 主要 AWS 應用場景 |
|-------------|------|--------------|-----------------------|
| **Alpine** | 基於 ARM 的 SoC | 多核 ARMv8 CPU、低功耗、整合網絡/儲存功能 | 早期 EC2 實例、儲存控制器 |
| **Graviton** | 基於 ARM 的 CPU | 64 位元 ARM Neoverse 核心（AWS 自主設計）、高核心數、DDR5、PCIe Gen4/5 | **EC2 Graviton 實例**（通用運算） |
| **Nitro** | 智能網卡／卸載晶片 | ARM CPU + 客製化加速器，用於虛擬化、安全、儲存、網絡功能卸載 | **EC2 Nitro 系統**、EBS、VPC、安全卸載 |
| **Inferentia** | AI 推論晶片 | 高吞吐量張量處理、低延遲、神經元核心 | **EC2 Inf1/Inf2 實例**用於機器學習推論 |
| **Trainium** | AI 訓練晶片 | 可擴展至大型語言模型、高記憶體頻寬、NeuronLink 互連技術 | **EC2 Trn1/Trn2 實例**用於訓練 LLM |

---

### 旗艦晶片系列（截至 2025 年現行）

#### 1. **AWS Graviton（CPU）**
- **架構**：客製化 ARM Neoverse 核心（非現成方案）
- **世代演進**：
  - **Graviton1**（2018）：16 核 ARMv8，用於 A1 實例
  - **Graviton2**（2020）：64 核 Neoverse N1，性價比較 x86 提升約 40%
  - **Graviton3**（2022）：Neoverse V1，支援 DDR5、bfloat16，較 Graviton2 提升最高 60%
  - **Graviton4**（2024）：Neoverse V2，96 核心，每瓦效能為 Graviton3 的 2.7 倍
- **應用**：驅動 **AWS EC2 約 30–40% 工作負載**（尤其容器、微服務、資料庫）

#### 2. **AWS Inferentia（AI 推論）**
- **Inferentia2**（2023）：效能為 Inferentia1 的 4 倍，支援 FP16/BF16/INT8
- 針對**即時推論**優化（推薦系統、語音、影像識別）
- 用於 **SageMaker**、**EC2 Inf2**

#### 3. **AWS Trainium（AI 訓練）**
- **Trainium2**（2024 年發布，2025 年上市）：訓練效能為 Trainium1 的 4 倍
- 設計目標為在 LLM 訓練領域與 **NVIDIA H100** 競爭
- 支援**萬億參數模型**及高頻寬記憶體（HBM）

#### 4. **Nitro 系統（智能網卡／DPU）**
- 搭載硬體加速器的客製化 ARM SoC
- 卸載虛擬化、網絡、儲存、加密運算
- 實現**虛擬化環境中的裸機效能**

---

### Annapurna 的重要性

- **成本與效率**：AWS 宣稱其性價比較 x86 **最高提升 40%**
- **垂直整合**：亞馬遜掌握晶片設計 → 加速創新、降低成本
- **AI 佈局**：Trainium/Inferentia 直接挑戰 NVIDIA 在雲端 AI 的主導地位
- **供應鏈韌性**：降低對 Intel/TSMC 獨家供應的依賴

---

### 總結

> **Annapurna Labs = AWS 的秘密晶片武器**  
> 他們打造 **基於 ARM 的 Graviton CPU**、**Inferentia（推論）**、**Trainium（訓練）** 及 **Nitro 卸載晶片**——全部為雲端環境優化。  
> 這些技術驅動著**更經濟、快速、環保**的 AWS 服務，也是 AWS 能在價格上壓制競爭對手並擴展 AI 規模的關鍵原因。

如需深入了解特定晶片（例如 Graviton4 對比 Apple M4、Trainium2 對比 H100），歡迎隨時提出。