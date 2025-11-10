---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 全面理解完整網域名稱
translated: true
type: note
---

### 什麼是 FQDN？

完整網域名稱（Fully Qualified Domain Name，FQDN）是指網際網路或區域網路中特定裝置或服務的完整絕對位址。它在域名系統（DNS）中能唯一識別主機（如電腦或伺服器），DNS 會將人類可讀的名稱轉譯為 IP 位址。

#### 關鍵組成部分
FQDN 包含域名層級結構中的所有部分，以點號分隔並按層級順序排列（從最特定到最通用）：
- **主機/主機名稱**：機器的特定名稱（例如「www」或「mail」）
- **子網域**：頂級網域下的可選層級（例如「www.google.com」中的「google」）
- **網域名稱**：主要部分（例如「google」）
- **頂級網域（TLD）**：最高層級，如「.com」、「.org」或國家代碼如「.uk」

與相對網域名稱（例如僅「google.com」）不同，FQDN 總是以句點（.）結尾以表示其完整性，但在日常使用中末尾的句點通常會被省略。

#### 為何使用 FQDN？
- **唯一性**：確保沒有歧義，能精確定位在 DNS 樹狀結構中的位置
- **DNS 解析**：有助於正確路由傳輸流量，特別是在子網域或私有網路等複雜設定中
- **範例**：
  - `"www.example.com."` — 完整格式（注意末尾的句點）
  - `"mail.google.com"` — 在 URL 中通常省略句點
  - 在區域網路中，可能是 `"server.dept.company.local."` 以指定部門中的伺服器

此概念由網際網路工程任務組（IETF）在 RFC 1035 等標準中規範，這些標準定義了 DNS。FQDN 能防止衝突、提升設定安全性，且對於電子郵件伺服器（如 SMTP）和網頁瀏覽器等工具至關重要。如果您有特定應用場景（例如網路架構或虛擬主機），我可以進一步延伸說明！