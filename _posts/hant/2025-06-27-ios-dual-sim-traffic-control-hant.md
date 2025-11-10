---
audio: false
generated: true
lang: hant
layout: post
title: iOS 雙SIM卡流量路由管理與防火長城考量
translated: true
type: note
---

iOS 提供了 API，讓你在使用雙卡功能時可以管理和分隔不同流動數據計劃的網絡流量，但存在限制，並且無法原生支援基於中國防火牆（GFW）限制來精確控制特定流量路由到特定 SIM 卡。然而，透過結合 iOS API、手動配置以及潛在的第三方工具，你可以實現某種程度的流量分隔，以區別處理澳門 SIM 卡和中國電信 SIM 卡的流量。以下我將概述相關的 API、配置和注意事項，包括如何應對 GFW 相關的挑戰。

### 用於雙卡和流量管理的關鍵 iOS API 與功能

1. **CoreTelephony 框架**：
   - **目的**：提供存取雙卡裝置的流動網絡相關資訊和配置。
   - **關鍵類別**：
     - `CTCellularPlanProvisioning`：允許你添加或管理流動網絡計劃（例如 eSIM 或實體 SIM 卡）。
     - `CTTelephonyNetworkInfo`：提供可用流動網絡計劃及其屬性的資訊，例如營運商名稱、移動國家代碼（MCC）和移動網絡代碼（MNC）。
     - `CTCellularData`：監控流動數據使用量和網絡狀態（例如流動數據是否啟用）。
   - **限制**：CoreTelephony 允許你查詢和管理流動網絡計劃，但無法直接控制將特定應用程式的流量路由到特定 SIM 卡。你可以偵測哪張 SIM 卡正在使用數據，但無法在 API 層面以程式方式將特定流量（例如特定應用程式或目的地）分配給 SIM 卡。

2. **NetworkExtension 框架**：
   - **目的**：啟用進階網絡配置，例如建立自訂 VPN 或管理網絡流量規則。
   - **關鍵功能**：
     - **NEVPNManager**：允許你配置和管理 VPN 連接，可用於透過特定伺服器路由流量以繞過 GFW 限制。
     - **NEPacketTunnelProvider**：用於建立自訂 VPN 通道，可以配置為透過澳門 SIM 卡路由特定流量以避開 GFW 限制。
   - **GFW 使用案例**：透過在澳門 SIM 卡上設定 VPN（由於澳門網絡獨立，不受 GFW 審查限制），你可以透過中國大陸以外的伺服器路由流量，以存取被封鎖的服務，例如 Google、WhatsApp 或 YouTube。
   - **限制**：VPN 配置通常應用於系統層級，而非按 SIM 卡配置。你需要手動切換使用中的數據 SIM 卡，或使用自訂 VPN 解決方案來選擇性路由流量。

3. **雙卡配置（基於設定）**：
   - iOS 在相容的 iPhone（例如 iPhone XS、XR 或更新型號，在澳門或香港等支援雙卡雙待的區域購買，支援兩張 nano-SIM 卡或 eSIM）上支援雙卡雙待（DSDS）。這允許你：
     - 為流動數據分配預設 SIM 卡（設定 > 流動網絡 > 流動數據）。
     - 啟用「允許流動數據切換」以根據訊號覆蓋或可用性自動在 SIM 卡之間切換（設定 > 流動網絡 > 流動數據 > 允許流動數據切換）。
     - 標記 SIM 卡（例如「澳門 SIM 卡」用於無限制存取，「中國電信」用於本地服務）並手動選擇哪張 SIM 卡處理特定任務的數據。
   - **手動流量分隔**：你可以在設定中手動切換使用中的數據 SIM 卡，將所有流動流量導向澳門 SIM 卡（以繞過 GFW）或中國電信 SIM 卡（用於受 GFW 限制的本地服務）。然而，iOS 未提供 API 來根據應用程式或目的地動態路由流量到特定 SIM 卡，而無需使用者介入。

4. **按應用程式 VPN（NetworkExtension）**：
   - iOS 透過 NetworkExtension 框架中的 `NEAppProxyProvider` 或 `NEAppRule` 類別支援按應用程式 VPN 配置，通常用於企業環境（例如受管理的應用程式配置）。
   - **使用案例**：你可以配置按應用程式 VPN，將特定應用程式（例如 YouTube、Google）的流量透過使用澳門 SIM 卡數據連接的 VPN 通道路由，以繞過 GFW 限制，而其他應用程式則使用中國電信 SIM 卡進行本地服務。
   - **要求**：這需要自訂 VPN 應用程式或企業流動裝置管理（MDM）解決方案，對於獨立開發者來說實施較為複雜。此外，當 VPN 使用時，你需要確保澳門 SIM 卡設定為使用中的數據 SIM 卡。

5. **URLSession 和自訂網絡**：
   - `URLSession` API 允許你使用 `allowsCellularAccess` 或透過綁定到特定網絡介面來配置具有特定流動網絡介面的網絡請求。
   - **使用案例**：你可以以程式方式停用某些請求的流動網絡存取（強制使用 Wi-Fi 或其他介面），或使用 VPN 來路由流量。然而，不直接支援將特定請求綁定到特定 SIM 卡的流動網絡介面；你需要依賴系統的使用中數據 SIM 卡設定。
   - **解決方法**：結合 `URLSession` 與配置為使用澳門 SIM 卡數據的 VPN，將流量路由到中國以外的伺服器。

### 使用雙卡處理 GFW 限制

中國防火牆（GFW）在使用中國大陸營運商（如中國電信）時會封鎖許多外國網站和服務（例如 Google、YouTube、WhatsApp），因為它們的流量是透過中國的審查基礎設施路由的。相比之下，澳門 SIM 卡（例如來自 CTM 或 3 Macau）的流量是透過澳門的獨立網絡路由，不受 GFW 審查（除了中國電信澳門，其執行 GFW 限制）。以下是你如何利用澳門 SIM 卡和中國電信 SIM 卡實現此目的：

1. **澳門 SIM 卡用於無限制存取**：
   - 將澳門 SIM 卡用作預設流動數據計劃，用於存取被 GFW 封鎖的應用程式或服務（例如 Google、YouTube）。
   - **配置**：
     - 前往設定 > 流動網絡 > 流動數據，選擇澳門 SIM 卡。
     - 在中國大陸時，確保為澳門 SIM 卡啟用數據漫遊，因為它將透過澳門的網絡路由流量，繞過 GFW。
     - 可選地，配置 VPN（例如使用 `NEVPNManager`）以進一步保護流量，儘管澳門 SIM 卡通常不需要 VPN 來存取被封鎖的服務。
   - **API 支援**：使用 `CTTelephonyNetworkInfo` 確認澳門 SIM 卡正在使用數據（`dataServiceIdentifier` 屬性）並監控其狀態。

2. **中國電信 SIM 卡用於本地服務**：
   - 使用中國電信 SIM 卡進行本地應用程式和服務（例如微信、支付寶），這些服務需要中國手機號碼或針對大陸網絡進行了優化。
   - **配置**：
     - 在存取本地服務時，手動在設定 > 流動網絡 > 流動數據中切換到中國電信 SIM 卡。
     - 注意，此 SIM 卡上的流量將受 GFW 限制，除非使用 VPN，否則許多外國網站將被封鎖。
   - **API 支援**：使用 `CTCellularData` 監控流動數據使用量並確保正確的 SIM 卡處於使用中。你還可以使用 `NEVPNManager` 為特定應用程式配置 VPN，以在中國電信 SIM 卡上繞過 GFW，儘管由於主動封鎖，VPN 在中國的可靠性不穩定。

3. **流量分隔的實用工作流程**：
   - **手動切換**：為簡化操作，根據任務在設定中切換使用中的數據 SIM 卡（例如澳門 SIM 卡用於國際應用程式，中國電信 SIM 卡用於本地應用程式）。這是最直接的方法，但需要使用者介入。
   - **中國電信 SIM 卡的 VPN**：如果你需要在中國電信 SIM 卡使用期間存取被封鎖的服務，請使用 `NEVPNManager` 配置 VPN。請注意，許多 VPN（例如 ExpressVPN、NordVPN）在中國可能不可靠，因為 GFW 會封鎖它們，因此請事先測試供應商，例如 Astrill 或自訂解決方案。一些 eSIM 供應商（例如 Holafly、ByteSIM）提供內建 VPN，可以啟動以繞過限制。
   - **按應用程式 VPN**：對於進階使用，開發一個使用 `NEAppProxyProvider` 的自訂應用程式，當中國電信 SIM 卡使用時，將特定應用程式流量透過 VPN 路由，同時允許其他應用程式直接使用澳門 SIM 卡。
   - **自動化限制**：iOS 未提供 API 來根據應用程式或目的地 URL 以程式方式切換使用中的數據 SIM 卡。你需要依賴使用者啟動的 SIM 卡切換或 VPN 來管理流量路由。

### 實施流量分隔的步驟

1. **設定雙卡**：
   - 確保你的 iPhone 支援雙卡（例如 iPhone XS 或更新型號，並運行 iOS 12.1 或更新版本）。
   - 插入澳門 SIM 卡和中國電信 SIM 卡（或為其中一張配置 eSIM）。
   - 前往設定 > 流動網絡，標記計劃（例如「澳門」和「中國電信」），並設定預設數據 SIM 卡（例如澳門用於無限制存取）。

2. **配置流動數據設定**：
   - 停用「允許流動數據切換」以防止自動 SIM 卡切換，讓你可以手動控制哪張 SIM 卡用於數據（設定 > 流動網絡 > 流動數據 > 允許流動數據切換）。
   - 在你的應用程式中使用 `CTTelephonyNetworkInfo` 以程式方式驗證哪張 SIM 卡正在使用數據。

3. **實施 VPN 以繞過 GFW**：
   - 對於中國電信 SIM 卡，使用 `NEVPNManager` 或第三方 VPN 應用程式（例如 Astrill、Holafly 的內建 VPN）配置 VPN 以繞過 GFW 限制。
   - 對於澳門 SIM 卡，可能不需要 VPN，因為其流量是透過中國審查基礎設施以外的路由傳輸的。

4. **監控和管理流量**：
   - 使用 `CTCellularData` 監控流動數據使用量，並確保正確的 SIM 卡正在使用。
   - 對於進階路由，探索使用 `NEPacketTunnelProvider` 建立自訂 VPN，以根據應用程式或目的地選擇性路由流量，儘管這需要大量的開發工作。

5. **測試和優化**：
   - 在中國大陸測試兩張 SIM 卡的連接性，確保澳門 SIM 卡按預期繞過 GFW，並且中國電信 SIM 卡適用於本地服務。
   - 驗證中國電信 SIM 卡上的 VPN 性能，因為 GFW 會主動封鎖許多 VPN 協議。

### 限制與挑戰

- **無動態 SIM 路由的原生 API**：iOS 未提供 API 來根據應用程式、URL 或目的地動態路由流量到特定 SIM 卡。你必須手動切換使用中的數據 SIM 卡或使用 VPN 來管理流量。
- **GFW VPN 封鎖**：GFW 主動封鎖許多 VPN 協議（例如 IPsec、PPTP），即使基於 SSL 的 VPN 在被偵測到時也可能受到速率限制。澳門 SIM 卡通常更可靠，無需 VPN 即可繞過 GFW。
- **中國電信 SIM 卡限制**：中國電信基於 CDMA 的網絡可能與某些外國手機存在相容性問題，儘管其 LTE/5G 網絡更廣泛相容。此外，其流量受 GFW 審查，需要 VPN 才能存取被封鎖的服務。
- **實名登記**：澳門和中國電信 SIM 卡都可能需要實名登記（例如護照資料），這可能使設定複雜化。
- **性能**：在中國大陸使用澳門 SIM 卡漫遊可能導致速度較慢，尤其是在鄉村地區。

### 建議

- **主要策略**：使用澳門 SIM 卡作為預設流動數據計劃，以存取被封鎖的服務，因為它透過澳門未經審查的網絡自然繞過 GFW。切換到中國電信 SIM 卡用於需要中國號碼或針對大陸網絡優化的本地應用程式，例如微信或支付寶。
- **VPN 作為備份**：對於中國電信 SIM 卡，使用可靠的 VPN 供應商（例如 Astrill，或具有內建 VPN 的 eSIM，如 Holafly 或 ByteSIM）以存取被封鎖的服務。在進入中國前預先安裝並測試 VPN，因為在中國下載 VPN 應用程式可能受到限制。
- **開發工作**：如果你正在建立應用程式，使用 `NetworkExtension` 實施自訂 VPN 以進行選擇性流量路由，但請注意這很複雜，並且可能需要企業級權限。對於大多數使用者，手動 SIM 卡切換結合 VPN 已足夠。
- **出行前設定**：在抵達中國前購買並啟動兩張 SIM 卡（或 eSIM），因為當地政策可能限制在中國大陸購買 eSIM。例如，Nomad 或 Holafly 等供應商允許預先購買和啟動具有內建 GFW 繞過功能的 eSIM。

### 程式碼範例片段

以下是使用 `CTTelephonyNetworkInfo` 檢查使用中流動網絡計劃和使用 `NEVPNManager` 為中國電信 SIM 卡配置 VPN 的基本範例：

```swift
import CoreTelephony
import NetworkExtension

// 檢查使用中的流動網絡計劃
func checkActiveCellularPlan() {
    let networkInfo = CTTelephonyNetworkInfo()
    if let dataService = networkInfo.serviceCurrentRadioAccessTechnology {
        for (serviceIdentifier, rat) in dataService {
            print("服務: \(serviceIdentifier), 無線接入技術: \(rat)")
            // 識別哪張 SIM 卡正在使用（例如澳門或中國電信）
        }
    }
}

// 為中國電信 SIM 卡配置 VPN
func setupVPN() {
    let vpnManager = NEVPNManager.shared()
    vpnManager.loadFromPreferences { error in
        if let error = error {
            print("載入 VPN 偏好設定失敗: \(error)")
            return
        }
        
        let vpnProtocol = NEVPNProtocolIKEv2()
        vpnProtocol.serverAddress = "vpn.example.com" // 替換為你的 VPN 伺服器
        vpnProtocol.remoteIdentifier = "vpn.example.com"
        vpnProtocol.authenticationMethod = .certificate // 根據需要配置
        
        vpnManager.protocolConfiguration = vpnProtocol
        vpnManager.isEnabled = true
        
        vpnManager.saveToPreferences { error in
            if let error = error {
                print("儲存 VPN 偏好設定失敗: \(error)")
            } else {
                print("VPN 配置成功")
            }
        }
    }
}
```

### 結論

雖然 iOS 未提供原生 API 來根據應用程式或目的地動態路由流量到特定 SIM 卡，但你可以透過以下方式實現流量分隔：
1. 使用澳門 SIM 卡進行無限制存取，無需 VPN 即可繞過 GFW。
2. 使用中國電信 SIM 卡進行本地服務，並搭配 VPN（透過 `NEVPNManager` 或第三方應用程式配置）以存取被封鎖的服務。
3. 在設定中手動切換使用中的數據 SIM 卡以進行不同任務。
4. 可選地，使用 `NetworkExtension` 開發自訂 VPN 解決方案以進行按應用程式流量路由，儘管這很複雜。

對於最簡單的方法，依賴澳門 SIM 卡進行 GFW 封鎖的服務，並切換到中國電信 SIM 卡以滿足本地需求，並為後者預先安裝可靠的 VPN。在前往中國前始終測試配置，因為 GFW 政策和 VPN 可靠性可能迅速變化。

如果你需要進一步澄清或協助具體的 API 實施，請告訴我！