---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: Cisco AnyConnect 網絡存取管理器概覽
translated: true
type: note
---

Cisco AnyConnect Secure Mobility Client 是一套軟體模組，提供安全的 VPN 存取、網路安全及基於策略的端點功能。此套件中的可選模組之一為 **Cisco Network Access Manager (NAM)**。

### Cisco AnyConnect NAM 的功能
- **網路連線管理**：NAM 取代 Windows 原生的無線與有線網路管理程式，負責設定、連線及保護有線與無線網路。
- **進階 802.1X 支援**：為有線與無線網路連線提供完整的 **802.1X 認證**（EAP-TLS、PEAP、EAP-FAST 等），常見於需要憑證基礎認證或端點狀態檢查的企業環境。
- **策略強制執行**：管理員可定義策略來規範終端裝置如何連線至網路——優先考量安全需求、定義允許的 SSID 或限制不安全的連線。
- **跨平台一致性行為**：透過集中化控制，使用者在不同電腦上皆能獲得相同的網路存取體驗。

### 重要說明
- **平台支援**：過去 NAM 僅支援 Windows 平台。隨著後期 AnyConnect 版本（自 v4.9 起），Cisco 終止了 NAM 支援，因作業系統原生網路管理程式（Windows Native Wi-Fi、macOS supplicant 等）已趨於成熟。
- **典型應用場景**：主要部署於企業、大學或政府網路，這些環境需要在系統登入前或登入期間，透過憑證基礎認證連線至 Wi-Fi 或有線區域網路。

👉 簡而言之：**Cisco AnyConnect NAM（網路存取管理程式）** 是一款進階網路連線管理工具，可取代 Windows 原生 supplicant 程式，透過 802.1X 認證及企業定義策略來處理安全的有線/無線連線。

---

您是否希望我進一步說明 **NAM 與較常使用的 AnyConnect VPN 模組之間的關聯性**（因現今多數使用者僅熟悉 VPN 功能）？