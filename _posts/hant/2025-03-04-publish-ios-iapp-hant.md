---
audio: false
generated: true
lang: hant
layout: post
title: 發布 iOS 應用程式至 App Store
translated: true
---

使用 Apple Developer Program 上傳 iOS 應用程式，無論是個人或企業用途，都需要註冊該計劃、準備和打包您的應用程式、上傳它，並管理更新。以下是涵蓋您查詢的所有方面的逐步指南，包括企業用途的 Dun & Bradstreet (D-U-N-S) 編號要求、打包應用程式、上傳存檔和通過 Apple 網站更新應用程式。

---

### 1. 註冊 Apple Developer Program

#### 適用於個人（個人用途）
- **建立 Apple ID**：
  如果您還沒有，請前往 [appleid.apple.com](https://appleid.apple.com) 並使用個人電子郵件地址註冊。
- **註冊計劃**：
  - 訪問 [developer.apple.com/programs/](https://developer.apple.com/programs/) 並點擊「註冊」。
  - 使用您的 Apple ID 登入。
  - 同意條款，提供您的個人法律姓名和地址，並支付每年 99 美元的費用。
- **注意事項**：您的個人姓名將作為 App Store 的賣家顯示。

#### 適用於企業（組織用途）
- **獲取 D-U-N-S 編號**：
  - D-U-N-S 編號是 Dun & Bradstreet 分配的唯一九位數字識別碼，用於驗證您組織的法律實體狀態。Apple 要求企業帳戶使用此編號。
  - 在 [dnb.com](https://www.dnb.com) 查看您的組織是否已經擁有一個。如果沒有，請通過其網站免費申請—處理可能需要兩週。
- **註冊計劃**：
  - 使用與您的組織相關聯的 Apple ID（例如，商業電子郵件）。
  - 訪問 [developer.apple.com/programs/](https://developer.apple.com/programs/) 並點擊「註冊」。
  - 選擇「組織」，並提供：
    - 法律實體名稱
    - 總部地址
    - D-U-N-S 編號
  - 註冊人必須有法律權限代表組織同意 Apple 的條款。
  - 支付每年 99 美元的費用。
- **注意事項**：您的組織名稱將作為 App Store 的賣家顯示。

---

### 2. 準備和打包應用程式
- **在 Xcode 中開發您的應用程式**：
  - 使用 Xcode，Apple 的官方開發工具，構建您的 iOS 應用程式。
  - 確保它符合 [App Store 審查指南](https://developer.apple.com/app-store/review/guidelines/)。
  - 設定部署目標，並在項目設置中更新應用程式的版本和構建號。
- **存檔應用程式**：
  - 在 Xcode 中打開您的項目。
  - 選擇「通用 iOS 設備」（或任何模擬器）作為構建目標。
  - 在菜單欄中選擇 **Product** > **Archive**。
  - Xcode 將編譯您的應用程式並創建一個存檔，這是一個包含代碼、資源和簽名信息的打包版本，準備進行分發。

---

### 3. 上傳應用程式存檔
- **使用 Xcode**：
  - 存檔後，Organizer 窗口會自動在 Xcode 中打開。
  - 選擇您的存檔並點擊 **Distribute App**。
  - 選擇 **App Store Connect** 作為分發方法。
  - 按照提示驗證並將存檔上傳到 App Store Connect。
- **使用 Transporter（替代方案）**：
  - 從 Mac App Store 下載 [Transporter 應用程式](https://apps.apple.com/us/app/transporter/id1450874784)。
  - 使用您的 Apple ID 登入。
  - 添加存檔應用程式文件（從 Xcode 導出為 `.ipa` 文件）並將其上傳到 App Store Connect。
  - 這個選項適用於高級用戶或批量上傳。

---

### 4. 使用 Apple 網站（App Store Connect）更新應用程式
- **訪問 App Store Connect**：
  - 訪問 [appstoreconnect.apple.com](https://appstoreconnect.apple.com) 並使用您的 Apple ID 登入。
- **管理您的應用程式**：
  - 從儀表板中選擇您的應用程式。
  - 導航到 **App Store** 選項卡。
  - 更新元數據（例如，應用程式描述、截圖、關鍵字）。
  - 在「版本」下，選擇您上傳的新構建。
- **提交審查**：
  - 點擊 **Submit for Review** 將更新發送給 Apple 的審查團隊。
  - 經批准後，您可以手動發布或安排自動發布。

---

### 附加說明
- **企業專屬詳細信息**：
  - 確保您的 D-U-N-S 編號和組織信息準確，以避免註冊延誤。
  - 您可以通過 App Store Connect 邀請團隊成員（例如，開發人員、測試人員）並分配角色，如「開發人員」或「管理員」。
- **常見挑戰和建議**：
  - **代碼簽名問題**：在 Xcode 中的 **Signing & Capabilities** 下驗證您的證書和配置文件。如果不確定，請使用「自動管理簽名」選項。
  - **應用程式審查拒絕**：彻底測試您的應用程式，以符合 Apple 的指南並避免延誤。
  - **D-U-N-S 延誤**：如果您是企業，請提前申請 D-U-N-S 編號，因為這是註冊的先決條件。

---

通過這些步驟，您可以成功使用 Apple Developer Program 上傳和更新您的 iOS 應用程式，無論是作為個人還是企業。有關更多詳細信息，請參考 Apple 的官方文檔 [developer.apple.com](https://developer.apple.com)。