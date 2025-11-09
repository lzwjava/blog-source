---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Shadowrocket 設定檔案分析
translated: true
type: note
---

這似乎是 Shadowrocket 的設定檔，這是一款基於規則的 iOS 代理工具（類似 Surge 或 Quantumult）。它採用文字型設定檔結構，定義了應用程式如何路由流量、處理 DNS、應用規則以及執行重寫或 MITM（中間人）攔截。檔案標記日期為「2025-10-02 20:25:43」，可能是時間戳記或佔位符。

我將逐節解析，說明每個部分的作用及其配置原因。此設定似乎是為網路受限地區（例如中國）使用者優化，將某些全球/被封鎖的服務透過代理伺服器路由，同時讓本地/國內流量直連以獲得更好速度並避免不必要的轉送。這並非完整設定——您仍需在應用程式中單獨配置代理伺服器（例如透過 Shadowsocks、V2Ray 等），且此設定引用了從 GitHub 自動更新的外部規則集。

### 關鍵假設與注意事項
- **代理設定**：此設定假設您已在 Shadowrocket 中配置可運作的代理伺服器（例如 SOCKS5、HTTP 或加密通訊協定）。若未配置，「PROXY」規則將無法運作。
- **目的**：似乎是為了規避審查（例如中國的防火長城）。AI 服務（如 OpenAI/ChatGPT）透過代理，而中國網域/IP 則直連以避免節流。
- **TUN 模式**：引用「tun」（通道模式）來路由所有裝置流量。
- **外部依賴**：部分規則從 GitHub URL 載入（例如規則清單）。請確保信任這些來源，因它們可能自動更新。
- 若有任何不清楚或需要協助應用，請告知您的設定詳情。

### 章節解析

#### **[General]**
設定全域應用行為、DNS 解析和網路路由。類似 Shadowrocket 的「偏好設定」或「系統設定」。

- `bypass-system = true`：忽略 iOS 系統代理設定。Shadowrocket 自行處理所有代理，不依賴系統全域設定。
  
- `skip-proxy = 192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,localhost,*.local,captive.apple.com,*.ccb.com,*.abchina.com.cn,*.psbc.com,www.baidu.com`：逗號分隔的清單，列出**始終直連**（不經代理）的網域/IP 範圍。包括：
  - 私有網路（例如家用 Wi-Fi IP 如 192.168.x.x）。
  - 本地網域（*.local）和 localhost。
  - Apple 的強制入口Portal檢查。
  - 中國銀行網域（*.ccb.com 為中國建設銀行、*.abchina.com.cn 為中國農業銀行、*.psbc.com 為中國郵政儲蓄銀行）。
  - 百度（www.baidu.com），中國主要搜尋引擎。
  - *原因？* 國內中國網站（尤其是銀行和搜尋）無需代理即可存取，且若經代理路由可能被節流或標記。

- `tun-excluded-routes = 10.0.0.0/8, 100.64.0.0/10, 127.0.0.0/8, 169.254.0.0/16, 172.16.0.0/12, 192.0.0.0/24, 192.0.2.0/24, 192.88.99.0/24, 192.168.0.0/16, 198.51.100.0/24, 203.0.113.0/24, 224.0.0.0/4, 255.255.255.255/32, 239.255.255.250/32`：在通道（TUN）模式下，這些 IP 範圍**排除**在代理通道外。避免干擾本地/路由流量，如回送 IP、組播和測試範圍。

- `dns-server = https://doh.pub/dns-query,https://dns.alidns.com/dns-query,223.5.5.5,119.29.29.29`：代理流量的優先 DNS 解析器清單。這些是 DoH（DNS over HTTPS）伺服器和普通 DNS（騰訊的 119.29.29.29 和阿里雲的 223.5.5.5）。以加密/公開伺服器（doh.pub 和 alidns.com）開頭以確保隱私/安全。

- `fallback-dns-server = system`：若主要 DNS 失敗，則退回使用 iOS 系統 DNS。

- `ipv6 = true`：啟用 IPv6 支援。`prefer-ipv6 = false`：連線時偏好 IPv4 勝於 IPv6（例如為了穩定性或相容性）。

- `dns-direct-system = false`：直連時不使用系統 DNS——改用設定的 DNS。

- `icmp-auto-reply = true`：自動回覆 ICMP（ping）請求。有助於連線檢查。

- `always-reject-url-rewrite = false`：允許觸發 URL 重寫（後續設定中使用）。

- `private-ip-answer = true`：允許 DNS 回應包含私有 IP（例如您的路由器）。

- `dns-direct-fallback-proxy = true`：若直連 DNS 查詢失敗，則透過代理重試。

- `tun-included-routes = `：（空）TUN 模式下未包含自訂路由——使用預設值。

- `always-real-ip = `：（空）未強制暴露真實 IP——標準行為。

- `hijack-dns = 8.8.8.8:53,8.8.4.4:53`：攔截來自 Google 公共 DNS（連接埠 53 的 8.8.8.8/8.8.4.4）的 DNS 流量，並透過代理路由。強制使用您設定的 DNS 而非可能被封鎖或監控的公共 DNS。

- `udp-policy-not-supported-behaviour = REJECT`：若政策不支援 UDP 流量，則拒絕而非允許。

- `include = `：（空）未包含其他設定檔。

- `update-url = `：（空）未從 URL 自動更新設定。

#### **[Rule]**
定義流量路由規則，按順序處理。類似 ACL（存取控制清單），告訴 Shadowrocket 根據網域、關鍵字、GEOIP 等決定哪些流量代理、哪些直連。若無規則匹配，則退回 `FINAL,DIRECT`。

- `DOMAIN-SUFFIX,anthropic.com,PROXY`：將 anthropic.com 的所有子網域透過代理路由（例如 api.anthropic.com）。Anthropic 是 AI 公司——可能為了繞過封鎖。

- `DOMAIN-SUFFIX,chatgpt.com,PROXY`：將 ChatGPT 網域透過代理路由。ChatGPT 在某些地區常受限制。

- `DOMAIN-SUFFIX,openai.com,PROXY`：將 OpenAI 網域透過代理路由（類似原因）。

- `DOMAIN-SUFFIX,googleapis.com,PROXY`：將 Google 的 API 服務透過代理路由（可能用於間接存取 Google 服務）。

- `DOMAIN-SUFFIX,zhs.futbol,DIRECT`：將此特定網域（可能為西班牙文/中文的運動網站）直連。

- `RULE-SET,https://github.com/lzwjava/lzwjava.github.io/raw/refs/heads/main/scripts/auto-ss-config/AI.list,PROXY`：從 GitHub 載入外部規則集（AI 相關網域清單）並代理它們。此規則會自動更新並擴展 AI 代理規則。

- `RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Lan/Lan.list,DIRECT`：載入本地網路（LAN）網域規則集並直連。避免代理家庭/內部流量。

- `DOMAIN-KEYWORD,cn,DIRECT`：任何包含關鍵字「cn」的網域（例如 anything.cn）直連。對中國網站有用。

- `GEOIP,CN,DIRECT`：任何地理位置為中國（CN）的 IP 直連。避免代理國內流量，因其快速且無限制。

- `FINAL,DIRECT`：預設動作——若無規則匹配，則直連。保持多數流量不經代理以提高效率。

*整體效果*：此為「代理被封鎖全球網站」的設定。AI/ChatGPT/OpenAI 流量強制透過 VPN/代理以繞過區域限制，而中國/本地內容保持直連。

#### **[Host]**
手動主機映射（類似本地 hosts 檔案）。

- `localhost = 127.0.0.1`：將「localhost」映射至回送 IP。標準設定——確保應用可連線至本地服務。

#### **[URL Rewrite]**
在發出請求前重寫傳入 URL。使用正規表示式匹配。

- `^https?://(www.)?g.cn https://www.google.com 302`：將任何 g.cn（或 www.g.cn）的 HTTP/HTTPS URL 重寫為重新導向至 google.com，狀態碼 302（暫時重新導向）。g.cn 是 Google 的中國網域——此舉可繞過它。

- `^https?://(www.)?google.cn https://www.google.com 302`：對 google.cn 至 google.com 執行相同操作。中國常封鎖或重新導向 google.com，因此此設定強制執行乾淨重新導向。

*原因？* 在審查地區，google.cn 可能提供篡改/被封鎖的結果。此設定確保您直接存取全球 Google 網站。

#### **[MITM]**
用於攔截和修改 HTTPS 流量的中間人設定（需在 Shadowrocket 中安裝根 CA 憑證）。

- `hostname = *.google.cn`：攔截任何 google.cn 子網域的流量。結合 URL 重寫，可能用於解密/重新導向 Google CN 網域流量。

*原因？* 可能用於強制執行重寫或處理中國的憑證釘選問題，因 google.cn 使用不同憑證。

### 如何使用此設定
1. **匯入**：在 Shadowrocket 中將此作為設定檔匯入。
2. **代理伺服器**：在「Servers」部分新增您的實際代理伺服器（例如 Shadowsocks 伺服器）——「PROXY」等規則依賴於此。
3. **啟用**：切換至此設定並在需要時啟用通道模式（VPN）。
4. **CA 憑證**：對於 MITM，若尚未完成，請安裝並信任 Shadowrocket 的 CA。
5. **測試**：檢查如 whatismyipaddress.com 等網站，確認 IP/路由是否如預期運作。監控中國網站是否變慢。
6. **疑難排解**：若規則集載入失敗，可能因速率限制或變更。IPv6 偏好設定可能需要切換以確保連線。

### 潛在問題/安全注意事項
- **隱私**：公開的規則集（GitHub 連結）可能洩漏您的路由內容。MITM 可攔截敏感流量——僅使用受信任的 CA。
- **更新**：規則集自動載入；若 GitHub 被封鎖，請使用代理存取它們。
- **未來日期**：設定標記為 2025 年 10 月——可能是筆誤或未來證明，但無功能依賴於此。
- **合法性**：為規避審查而使用代理在某些地方無妨，但在其他地區受限制——請自行承擔風險。
- 若您分享錯誤日誌或目標，我可提供更精確建議！