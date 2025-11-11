---
audio: false
generated: true
lang: hant
layout: post
title: Gemini 代碼輔助
translated: true
type: note
---

要使用 **Gemini Code Assist**（由 Google 開發的 AI 編程助手），您可以將其整合到您的開發環境中，例如 Visual Studio Code (VSCode)，以提升編程體驗。Gemini Code Assist 可協助進行代碼補全、代碼生成、解釋、除錯等功能。以下是在 VSCode 中設定和使用的逐步指南。

---

### 步驟 1：安裝 Gemini Code Assist 擴展
- 開啟 **VSCode**。
- 點擊活動欄中的擴展圖示或按下 `Ctrl+Shift+X`（Windows/Linux）或 `Cmd+Shift+X`（macOS），進入 **擴展** 視圖。
- 在搜尋欄中輸入 **"Gemini Code Assist"**。
- 在市場中找到官方擴展，點擊 **安裝**，如有提示請重啟 VSCode。

---

### 步驟 2：使用您的 Google 帳戶登入
- 安裝完成後，在活動欄（VSCode 左側）找到 **Gemini Code Assist 圖示**。
- 點擊圖示開啟 Gemini 面板。
- 選擇 **"使用 Google 登入"**，並按照驗證提示使用您的 Google 帳戶進行操作。
  - 對於 **免費版本**（Gemini Code Assist 個人版），使用個人 Gmail 帳戶即可。
  - 對於 **標準版或企業版**，您可能需要將其連結到已啟用相關 API 的 Google Cloud 項目。

---

### 步驟 3：開始使用 Gemini Code Assist
登入後，您可以透過以下幾種方式使用其功能：

#### a. 代碼補全
- 當您在編輯器中輸入時，Gemini 會自動建議代碼補全。
- 按下 `Tab` 鍵（或其他設定的按鍵）接受這些建議。

#### b. 透過聊天進行代碼生成與解釋
- 點擊活動欄中的 Gemini 圖示，開啟 **Gemini 面板**。
- 輸入自然語言提示，例如：
  - "解釋這段代碼"
  - "生成一個排序陣列的函數"
  - "協助我除錯這個錯誤"
- 若要參考特定代碼，請在輸入提示前先在編輯器中選取該代碼。
- Gemini 將在聊天面板中回應，您可以將生成的代碼插入檔案中（如有需要）。

#### c. 代碼轉換
- 按下 `Ctrl+I`（Windows/Linux）或 `Cmd+I`（macOS）開啟快速選擇選單。
- 輸入指令，例如 `/generate function to create a Cloud Storage bucket`。
- 在差異視圖中檢視建議的更改，並按需應用。

#### d. 內聯建議
- 編程時，Gemini 可能會提供內聯建議，以補全代碼行或代碼塊。
- 這些建議會在您輸入時出現，並可透過按鍵接受。

---

### 額外提示
- **逐步教學**：首次使用時，您可能會看到在 VSCode 中啟動逐步教學的選項。這個互動式指南介紹了擴展的功能。
- **支援的語言**：Gemini Code Assist 適用於所有公開的編程語言，例如 Python、JavaScript 和 Java。
- **驗證建議**：請務必檢視 AI 生成的代碼，因為它偶爾可能看似合理但不正確。
- **私隱**：您可以在擴展內調整數據使用設定，以符合您的偏好。

---

### 潛在注意事項
- **網絡**：如果您位於代理伺服器後，請相應配置 VSCode 的網絡設定。
- **使用限制**：免費版本每天提供最多 6,000 次代碼相關請求和 240 次聊天請求，對大多數用戶來說已足夠。
- **GitHub 整合**：若要在 GitHub 上使用 AI 驅動的代碼審查，需要進行額外設定，但這與核心 IDE 功能是分開的。

---

按照這些步驟，您可以在 VSCode 中有效使用 Gemini Code Assist 來簡化編程任務。如需更多詳細資訊，請參閱 Google 的官方文件。