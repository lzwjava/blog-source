---
audio: false
generated: true
lang: hant
layout: post
title: SSI 社交媒體元標籤
translated: true
type: note
---

您提供的程式碼包含 **Open Graph (OG)** 和 **Twitter Card** 元標籤，用於控制在社交媒體平台（如 Facebook、Twitter（現為 X）及其他支援這些協定的平台）上分享內容時的顯示方式。這些標籤是網站 HTML `<head>` 部分的一部分，提供頁面的元數據，以增強其在社交媒體動態中的呈現效果。

在此案例中，這些元標籤用於 **Safe Superintelligence Inc. (SSI)** 的網站，網址為 `https://ssi.inc`。下面，我將解釋這些標籤是什麼、它們如何工作，並根據提供的資訊提供關於 Safe Superintelligence Inc. 的背景說明。

---

### 什麼是這些元標籤？

**Open Graph (OG) 元標籤**：
- 由 Facebook 開發，Open Graph 標籤允許網站定義其內容在 Facebook、LinkedIn 及其他支援 Open Graph 協定的平台上分享時的外觀。
- 這些標籤指定了頁面的關鍵細節，如標題、描述、圖片和 URL，確保連結分享時具有一致且視覺上吸引人的預覽。

**Twitter Card 元標籤**：
- Twitter Cards 是 Twitter（現為 X）使用的類似概念，用於豐富推文或貼文中的連結預覽。
- 它們提供元數據，以便在平台上分享 URL 時顯示摘要、圖片或其他媒體。

這兩組標籤有助於優化用戶體驗，確保分享的連結看起來專業並提供相關資訊，如標題、描述和圖片。

---

### 元標籤詳解

以下是您提供的程式碼中每個標籤的作用：

#### Open Graph 標籤
1. `<meta property="og:url" content="https://ssi.inc">`
   - 指定要分享頁面的標準 URL。這確保顯示和追蹤正確的 URL，避免重複（例如 `ssi.inc` 與 `www.ssi.inc`）。
   - **值**: `https://ssi.inc`

2. `<meta property="og:type" content="website">`
   - 定義內容類型。在此案例中，`website` 表示一個普通的網頁（其他類型包括 `article`、`video` 等）。
   - **值**: `website`

3. `<meta property="og:title" content="Safe Superintelligence Inc.">`
   - 設定在社交媒體預覽中顯示的標題。這通常是頁面或組織的名稱。
   - **值**: `Safe Superintelligence Inc.`

4. `<meta property="og:description" content="The world's first straight-shot SSI lab, with one goal and one product: a safe superintelligence.">`
   - 提供頁面內容的簡短描述，顯示在預覽中。這總結了 Safe Superintelligence Inc. 的使命。
   - **值**: `The world's first straight-shot SSI lab, with one goal and one product: a safe superintelligence.`

5. `<meta property="og:image" content="https://ssi.inc/public/og-preview.jpg">`
   - 指定在預覽中顯示的圖片。這通常是標誌、橫幅或相關圖形。
   - **值**: `https://ssi.inc/public/og-preview.jpg`

#### Twitter Card 標籤
1. `<meta name="twitter:card" content="summary_large_image">`
   - 定義 Twitter Card 的類型。`summary_large_image` 創建一個帶有大圖片、標題和描述的預覽。
   - **值**: `summary_large_image`

2. `<meta name="twitter:site" content="@ssi">`
   - 指定與網站相關的 Twitter (X) 帳號，連結到組織的官方帳戶。
   - **值**: `@ssi`

3. `<meta property="twitter:domain" content="ssi.inc">`
   - 指示正在分享的網站網域。
   - **值**: `ssi.inc`

4. `<meta property="twitter:url" content="https://ssi.inc">`
   - 指定正在分享的頁面 URL，類似於 `og:url`。
   - **值**: `https://ssi.inc`

5. `<meta name="twitter:title" content="Safe Superintelligence Inc.">`
   - 設定 Twitter Card 的標題，與 Open Graph 標題一致。
   - **值**: `Safe Superintelligence Inc.`

6. `<meta name="twitter:description" content="The world's first straight-shot SSI lab, with one goal and one product: a safe superintelligence.">`
   - 提供 Twitter Card 的描述，與 Open Graph 描述一致。
   - **值**: `The world's first straight-shot SSI lab, with one goal and one product: a safe superintelligence.`

7. `<meta name="twitter:image" content="https://ssi.inc/public/og-preview.jpg">`
   - 指定 Twitter Card 的圖片，與 Open Graph 圖片一致。
   - **值**: `https://ssi.inc/public/og-preview.jpg`

---

### 這些元標籤如何工作？

1. **目的**：
   - 當有人在 Facebook 或 Twitter (X) 等平台上分享 URL `https://ssi.inc` 時，平台的網路爬蟲（例如 Facebook 的爬蟲或 Twitter 的機器人）會從頁面的 HTML 讀取這些元標籤。
   - 爬蟲提取標題、描述、圖片和其他元數據以生成豐富的預覽卡。例如：
     - 在 **Facebook** 上，分享的連結將顯示一張卡片，標題為 "Safe Superintelligence Inc."，描述為 "The world's first straight-shot SSI lab…"，並顯示位於 `https://ssi.inc/public/og-preview.jpg` 的圖片。
     - 在 **Twitter (X)** 上，將出現類似的卡片，帶有大圖片、相同的標題和描述，以及用於歸屬的 `@ssi` 帳號。

2. **機制**：
   - **爬取**：當 URL 被分享時，社交媒體平台向網站的伺服器發送請求以獲取 HTML 並解析元標籤。
   - **渲染**：平台使用標籤值創建預覽卡。例如，Twitter 上的 `summary_large_image` 確保帶有下方文字的突出圖片。
   - **快取**：平台可能會快取元數據以減少伺服器負載。如果標籤更新，像 Facebook 這樣的平台提供工具（例如 Sharing Debugger）來刷新快取。
   - **驗證**：平台可能會驗證圖片（例如確保其可訪問且符合尺寸要求），並在標籤缺失或無效時回退到預設文字或圖片。

3. **影響**：
   - 這些標籤通過使分享的連結在視覺上更具吸引力且資訊豐富，來提高用戶參與度。
   - 它們通過允許網站所有者控制標題、描述和圖片來確保品牌一致性。
   - 通過提供引人入勝的預覽，它們可以為網站帶來流量。

---

### 關於 Safe Superintelligence Inc. (SSI)

根據元標籤及所提供搜尋結果的額外背景資訊，以下是我們對 Safe Superintelligence Inc. 的了解：

- **概述**：
  - Safe Superintelligence Inc. (SSI) 是一家美國人工智慧公司，由 Ilya Sutskever（OpenAI 前首席科學家）、Daniel Gross（Apple AI 前負責人）和 Daniel Levy（AI 研究員和投資者）於 2024 年 6 月創立。
  - 其使命是開發一個**安全的超級智慧**，定義為一個超越人類智慧同時優先考慮安全以防止傷害的 AI 系統。

- **使命與方法**：
  - SSI 的唯一重點是創建一個安全的超級智慧系統，這既是其使命也是其唯一的產品。與其他 AI 公司不同，SSI 避免商業產品週期，專注於長期安全和技術突破。
  - 該公司將安全和 AI 能力視為相互交織的技術挑戰，旨在快速推進能力的同時確保安全至關重要。
  - SSI 強調一種使其免受短期商業壓力影響的商業模式，允許其專注於安全、保障和進步。

- **營運**：
  - SSI 在**加利福尼亞州帕洛阿爾托**和**以色列特拉維夫**設有辦事處，以招募頂尖技術人才。
  - 截至 2024 年 9 月，SSI 擁有約 20 名員工，但正在積極招聘研究員和工程師，重點關注「良好品格」和非凡能力，而不僅僅是資歷。

- **融資與估值**：
  - 2024 年 9 月，SSI 以**50 億美元的估值**籌集了**10 億美元**，投資者包括 Andreessen Horowitz、Sequoia Capital、DST Global 和 SV Angel。
  - 到 2025 年 3 月，SSI 在由 Greenoaks Capital 領投的一輪融資中達到**300 億美元的估值**，並在 2025 年 4 月再籌集**20 億美元**，使總融資額達到**30 億美元**，估值為**320 億美元**。
  - 資金正用於獲取計算能力（例如通過與 Google Cloud 合作獲取 TPU）和招聘頂尖人才。

- **背景與領導層**：
  - Ilya Sutskever 是 OpenAI 的聯合創始人，也是 ChatGPT 和 AlexNet 背後的關鍵人物，在涉及安全擔憂和 Sam Altman 被罷免的爭執後，於 2024 年 5 月離開 OpenAI。SSI 反映了他認為 OpenAI 將重點轉向商業化而非安全的信念。
  - SSI 對**存在安全**（例如防止 AI 造成災難性傷害）的關注使其有別於「信任與安全」工作（如內容審核）。
  - 該公司因其高知名度的團隊和使命而備受關注，Meta 曾試圖收購 SSI，並在 2025 年聘請了其 CEO Daniel Gross。

- **現狀**：
  - SSI 處於**隱形模式**，截至 2025 年 7 月，沒有公開產品或收入。其網站極簡，僅包含一個帶有使命聲明和聯絡資訊的頁面。
  - 該公司正專注於進行多年的研發，然後才發布其第一個產品，即一個安全的超級智慧。

---

### Safe Superintelligence Inc. 如何運作？

雖然 SSI 的技術細節因其隱形模式而未公開，但可以從現有資訊推斷其營運模式：

1. **研究與開發**：
   - SSI 進行 AI 安全、倫理、安全和治理的基礎研究，以識別風險並開發可驗證的保障措施。
   - 該公司旨在創建一個與人類價值觀一致並保持控制下的超級智慧 AI 系統，類似於確保極端條件下核反應爐的安全。

2. **安全優先方法**：
   - 與 OpenAI 等開發 ChatGPT 等商業產品的公司不同，SSI 專注於單獨構建一個安全的超級智慧系統，避免產品週期的「競爭性競賽」。
   - 安全被整合到能力開發中，通過創新工程將兩者都作為技術問題來解決。

3. **團隊與人才**：
   - SSI 正在帕洛阿爾托和特拉維夫建立一個精幹、高技能的工程師和研究員團隊，優先考慮那些致力於其安全使命的人。
   - 該公司花費大量時間審查候選人，以確保其與公司文化和使命的一致性。

4. **基礎設施**：
   - SSI 與 Google Cloud 等雲端供應商合作，以獲取 TPU（Tensor Processing Units）來支持其 AI 訓練的計算需求。
   - 該公司計劃與晶片公司合作以獲取額外的計算資源。

5. **教育與協作**：
   - 除了開發，SSI 旨在教育研究員、開發人員、政策制定者和公眾關於安全 AI 實踐，培養一種優先考慮安全而非商業化的全球思維模式。
   - 它尋求建立一個協作生態系統，以確立安全 AI 開發的全球規範和最佳實踐。

---

### 這些元標籤對 SSI 的重要性

這些元標籤反映了 SSI 的品牌和使命：
- 一致的標題和描述（"Safe Superintelligence Inc." 和 "The world's first straight-shot SSI lab…"）強調了其對安全超級智慧的單一關注，與其公開訊息一致。
- Twitter 帳號 `@ssi` 將網站連接到其官方 X 帳戶，公司成立的公告等更新曾在此發布。
- 圖片 (`og-preview.jpg`) 很可能是一個品牌圖形或標誌，儘管其內容未公開描述。它確保網站分享時的視覺一致性。

這些標籤對 SSI 至關重要，作為一個處於隱形模式、公開形象極少的初創公司，它們有助於控制其在社交媒體上的敘事，特別是考慮到其高知名度的創始人和重大的投資者興趣。

---

### 限制與注意事項
- **缺乏公開細節**：SSI 的網站和公開資訊稀少，反映了其早期階段和隱形狀態。元標籤提供了對其品牌的一瞥，但未揭示其技術方法。
- **推測性質**：關於 SSI 估值和融資的主張基於報導，但確切細節（例如產品路線圖）仍未公開。
- **X 貼文作為情緒指標**：X 上的貼文暗示了對 SSI 潛力的興奮，但這不是事實證據，可能包含推測。

如果您希望我根據現有數據更深入地探討 SSI 的技術方法、分析相關的 X 貼文以了解情緒，或進一步解釋元標籤，請告訴我！