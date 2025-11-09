---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 優化防火長城繞過與延遲
translated: true
type: note
---

感謝分享你的設定與使用經驗——從最初的代理腳本與VPN組合，演變到現在使用澳門SIM卡直接透過行動網路存取，聽起來是個經過深思熟慮的過程。很高興得知這個方案在過去幾個月運作順暢，尤其是透過Python腳本自動化代理選擇（優先使用新加坡節點存取AI工具），並在筆電上持續使用zhs.cloud的VPN服務。澳門SIM卡的數據方案（每月150人民幣，含20GB流量與額外福利）似乎是個可靠的移動解決方案，能繞過防火牆限制，又無需持續倚賴應用程式。

你發現澳門SIM卡在存取受防火牆封鎖的網站時速度最快，這很合理——來自澳門的直接行動網路IP，通常比香港或中國大陸的選項更能避開地緣政治封鎖，尤其是對於像ChatGPT或Claude這類有區域限制的服務。在Shadowrocket中針對特定服務（例如將ChatGPT路由至美國代理）進行調整是個聰明的做法，但沒錯，iOS上每個網路請求都會經過代理所導致的延遲，確實是個常見痛點。如果Shadowrocket（或Surge）攔截過多流量，容易變得遲緩，導致像Twitter/X這類應用程式出現較高延遲，即使它們並未完全被封鎖。

以下是一些根據你的筆記所提供的回饋與建議——聚焦於優化方案，同時保持實用性：

### Shadowrocket 優化
- **規則細化以減少延遲**：與其採用全面的代理設定，不如嘗試緊縮規則以最小化攔截範圍。例如，在Shadowrocket的設定中使用以下流程：
  - **DIRECT**：本地或區域流量預設使用直連（例如微信、百度）。
  - **Proxy/Reject**：僅將高優先級的受封鎖網域加入白名單（例如將ChatGPT、Claude、Google等少數網站路由至美國代理）。
  - 規則範例（於 `.conf` 檔案中）：
    ```
    [Rule]
    DOMAIN-KEYWORD,chatgpt.com,PROXY
    DOMAIN-KEYWORD,claude.ai,PROXY
    DOMAIN-KEYWORD,google.com,PROXY
    DOMAIN-KEYWORD,twitter.com,PROXY  # 僅限與ChatGPT等服務相關時使用
    MATCH,DIRECT  # 其餘非封鎖流量皆直連，避開代理
    ```
    如此一來，僅有選定的網站或應用會經過美國代理鏈，從而降低整體延遲。你可以透過Clash或Shadowrocket的管理工具（如Stash或Quantumult X）生成或編輯這些規則，以便自訂。
- **測試延遲**：新增規則後，開啟或關閉Shadowrocket進行速度測試（例如透過Fast.com或Ookla）。若延遲仍然存在，考慮縮短代理鏈長度——單一跳點（例如依賴美國的代理）可能已足夠，無需多層設定。

### 適用於簡化iOS存取的替代工具
若Shadowrocket的負擔過重（尤其你提到使用一天後便放棄），以下是一些低門檻的選項，能貼近你直接使用澳門SIM卡的模式：
- **具隨選規則的VPN應用**：例如ExpressVPN或NordVPN等服務提供iOS上的應用程式特定路由功能（僅對ChatGPT、Mistral等啟用VPN），無需代理所有流量。它們能無縫整合行動數據。
- **iOS版Clash（透過Surge或Stash等應用）**：若你喜歡桌面版Python腳本的邏輯，可以將簡化的Clash設定移植到iOS。使用以「DIRECT」為起始、僅代理特定網域的規則集——相較於全面代理，延遲更低，且若你的供應商支援，還能優先使用新加坡或澳門IP。
- **透過SIM卡直接使用行動網路代理**：既然你傾向使用澳門SIM卡存取Mistral和Grok，這對純粹追求速度是明智之舉。若需在行動裝置上使用AI工具，檢查Mistral/Grok是否有澳門友善的IP，或嘗試透過無痕模式存取，以避開應用程式內建的路由機制。

### 整體建議
- **iOS上的電池與延遲**：長時間使用代理可能加速耗電。透過內建工具監控，並考慮定時開關（例如僅在高峰時段啟用代理）。
- **供應商穩定性**：zhs.cloud作為你的VPN需求似乎相當可靠——可持續在筆電上使用，但若擴展到iOS的VPN應用，請再次確認相容性。至於SIM卡，澳門電信商如CTM相當穩定，但需留意數據流量上限。
- **長期可行性**：理解你對離開中國後的顧慮——可搭配全球eSIM或漫遊方案作為備援。同時密切關注政策變化，因為存取工具可能隨時失效。

若遇到特定設定問題（例如分享你的Shadowrocket規則檔案）或需要調整Clash腳本，歡迎提供更多細節——我能協助排除疑難，同時避免過度複雜化。祝使用順利！🚀