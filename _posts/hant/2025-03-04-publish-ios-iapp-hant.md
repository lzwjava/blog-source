---
audio: false
generated: true
lang: hant
layout: post
title: 將iOS應用程式發佈到App Store
translated: true
type: note
---

要使用 Apple Developer Program 上傳 iOS 應用程式，無論是個人或企業用途，您都需要先註冊該計劃、準備並封裝應用程式、上傳檔案，以及管理更新。以下將逐步解答您的疑問，包括企業用途所需的鄧白氏（D-U-N-S）編號要求、應用程式封裝方式、封存檔上傳流程，以及透過 Apple 網站更新應用程式的方法。

---

### 1. 註冊 Apple Developer Program

#### 個人用途
- **建立 Apple ID**：  
  若尚未擁有 Apple ID，請前往 [appleid.apple.com](https://appleid.apple.com) 使用個人電郵地址註冊。
- **註冊計劃**：  
  - 造訪 [developer.apple.com/programs/](https://developer.apple.com/programs/) 並點擊「註冊」。
  - 使用您的 Apple ID 登入。
  - 同意條款、提供個人法定姓名與地址，並支付每年 99 美元的費用。
- **重要注意事項**：您的個人姓名將顯示為 App Store 中的銷售者。

#### 企業用途
- **取得鄧白氏編號**：  
  - 鄧白氏編號是由鄧白氏公司核發的九位數唯一識別碼，用於驗證組織的合法實體狀態。Apple 要求企業帳戶必須提供此編號。
  - 請至 [dnb.com](https://www.dnb.com) 查詢您的組織是否已有編號。若無，可透過其網站免費申請，處理時間可能長達兩週。
- **註冊計劃**：  
  - 使用與組織關聯的 Apple ID（例如公司電郵）。
  - 前往 [developer.apple.com/programs/](https://developer.apple.com/programs/) 並點擊「註冊」。
  - 選擇「組織」並提供：
    - 法定實體名稱
    - 總部地址
    - 鄧白氏編號
  - 註冊者必須具備法律權限代表組織同意 Apple 的條款。
  - 支付每年 99 美元的費用。
- **重要注意事項**：您的組織名稱將顯示為 App Store 中的銷售者。

---

### 2. 準備與封裝應用程式
- **在 Xcode 中開發應用程式**：  
  - 使用 Apple 官方開發工具 Xcode 建置 iOS 應用程式。
  - 確保應用程式符合 [App Store 審核指南](https://developer.apple.com/app-store/review/guidelines/)。
  - 在專案設定中設定部署目標，並更新應用程式的版本與建置編號。
- **封存應用程式**：  
  - 在 Xcode 中開啟您的專案。
  - 選擇「Generic iOS Device」（或任何模擬器）作為建置目標。
  - 前往選單列中的 **Product** > **Archive**。
  - Xcode 將編譯應用程式並建立封存檔，此為準備分發的封裝版本，包含程式碼、資源與簽署資訊。

---

### 3. 上傳應用程式封存檔
- **使用 Xcode**：  
  - 封存完成後，Xcode 會自動開啟 Organizer 視窗。
  - 選擇您的封存檔並點擊 **Distribute App**。
  - 選擇 **App Store Connect** 作為分發方式。
  - 依照提示驗證並將封存檔上傳至 App Store Connect。
- **使用 Transporter（替代方案）**：  
  - 從 Mac App Store 下載 [Transporter 應用程式](https://apps.apple.com/us/app/transporter/id1450874784)。
  - 使用您的 Apple ID 登入。
  - 新增已封存的應用程式檔案（從 Xcode 匯出的 `.ipa` 檔案）並上傳至 App Store Connect。
  - 此選項適合進階使用者或需要批量上傳的情況。

---

### 4. 透過 Apple 網站更新應用程式（App Store Connect）
- **登入 App Store Connect**：  
  - 前往 [appstoreconnect.apple.com](https://appstoreconnect.apple.com) 並使用 Apple ID 登入。
- **管理應用程式**：  
  - 從儀表板中選擇您的應用程式。
  - 導航至 **App Store** 分頁。
  - 更新詮釋資料（例如應用程式描述、截圖、關鍵字）。
  - 在「Versions」區段選擇您上傳的新建置版本。
- **提交審核**：  
  - 點擊 **Submit for Review** 將更新提交至 Apple 審核團隊。
  - 通過審核後，您可以手動發布或設定自動發布排程。

---

### 補充說明
- **企業專屬細節**：  
  - 請確保鄧白氏編號與組織資訊準確無誤，以避免註冊延誤。
  - 您可透過 App Store Connect 邀請團隊成員（例如開發者、測試人員），並分配「Developer」或「Admin」等角色。
- **常見問題與技巧**：  
  - **程式碼簽署問題**：在 Xcode 的 **Signing & Capabilities** 中檢查憑證與供應設定檔。若不確定，可使用「Automatically manage signing」選項。
  - **應用程式審核遭拒**：徹底測試應用程式以確保符合 Apple 指南，避免延誤。
  - **鄧白氏編號延遲**：若為企業用戶，請提前申請鄧白氏編號，因其為註冊的必要條件。

---

透過以上步驟，無論是個人或企業用戶，您都能成功使用 Apple Developer Program 上傳與更新 iOS 應用程式。更多詳細資訊，請參閱 Apple 官方文件 [developer.apple.com](https://developer.apple.com)。