---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Google Analytics
translated: true
---

要使用 Google Analytics，將其整合到您的前端項目中，並使用應用程式和網站檢查數據，請按照以下步驟進行。本指南假設您的前端項目是網站或行動應用程式，並使用 **Google Analytics 4 (GA4)**，這是截至 2023 年的當前標準，因為 Universal Analytics 不再支持新的數據收集。

---

### 1. 設定 Google Analytics
在將 Google Analytics 整合到您的項目之前，您需要創建一個帳戶並進行配置：

- **創建帳戶**：前往 [analytics.google.com](https://analytics.google.com) 並使用您的 Google 帳戶註冊，如果您還沒有帳戶的話。
- **創建 GA4 屬性**：
  - 點擊左下角的「管理」。
  - 在「屬性」下，點擊「創建屬性」，填寫您的項目詳細資料，並選擇 **Google Analytics 4**。
- **添加數據流**：根據您的前端項目類型：
  - **網站**：選擇「網站」，輸入您的網站 URL，並為流命名（例如，「我的網站」）。
  - **行動應用程式**：選擇「應用程式」，選擇 iOS 或 Android，並提供您的應用程式詳細資料（例如，套件名稱）。

設置數據流後，您將獲得一個 **測量 ID**（例如，`G-XXXXXXXXXX`），您將用於整合。

---

### 2. 將 Google Analytics 整合到您的前端項目
整合過程取決於您的前端項目是網站還是行動應用程式。

#### 網站
- **添加 Google 標籤**：
  - 在您的 GA4 屬性中，前往「數據流」，選擇您的網站流，並找到「標籤指示」。
  - 複製提供的 **Google 標籤** 腳本，內容如下：
    ```html
    <!-- Google 標籤 (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_MEASUREMENT_ID"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'YOUR_MEASUREMENT_ID');
    </script>
    ```
  - 將此代碼粘貼到您的網站 HTML 的 `<head>` 部分，將 `YOUR_MEASUREMENT_ID` 替換為您的實際測量 ID。
- **單頁應用程式 (SPAs)**（例如，React、Angular、Vue）：
  - 默認腳本僅追蹤初始頁面加載。對於 SPAs，頁面在路由變更時不會重新加載，請使用庫來追蹤導航。例如，在 **React**：
    1. 安裝 `react-ga4` 庫：
       ```bash
       npm install react-ga4
       ```
    2. 在應用程式中初始化它（例如，在 `index.js` 或 `App.js` 中）：
       ```javascript
       import ReactGA from 'react-ga4';
       ReactGA.initialize('YOUR_MEASUREMENT_ID');
       ```
    3. 在路由變更時追蹤頁面查看（例如，使用 React Router）：
       ```javascript
       ReactGA.send({ hitType: "pageview", page: window.location.pathname });
       ```
       每當路由變更時呼叫此函數，例如在與路由器位置相關聯的 `useEffect` 鉤子中。
  - 其他框架也有類似的庫（例如，`ngx-analytics` 適用於 Angular，`vue-ga` 適用於 Vue—請檢查 GA4 兼容性）。
- **可選**：使用 **Google 標籤管理器 (GTM)** 而不是硬編碼標籤，以更輕鬆地管理追蹤腳本。

#### 行動應用程式
- **使用 Firebase（推薦）**：
  - 如果您的應用程式使用 Firebase，啟用 **Firebase 的 Google Analytics**：
    1. 在 [console.firebase.google.com](https://console.firebase.google.com) 創建一個 Firebase 項目。
    2. 將應用程式添加到項目中（iOS 或 Android）。
    3. 按照提示下載配置文件（例如，iOS 的 `GoogleService-Info.plist`，Android 的 `google-services.json`），並將其添加到您的應用程式中。
    4. 安裝 Firebase SDK：
       - **iOS**：使用 CocoaPods (`pod 'Firebase/Analytics'`) 並在 `AppDelegate` 中初始化。
       - **Android**：在 `build.gradle` 中添加依賴項並在應用程式中初始化。
    5. Firebase 會自動鏈接到您的 GA4 屬性並開始收集數據。
- **不使用 Firebase**：
  - 使用獨立的 **Google Analytics SDK** 適用於 iOS 或 Android（現在 GA4 的 Firebase 整合後不太常見）。請參考官方文檔進行設置，因為它會根據平台有所不同。

---

### 3. 驗證整合
- **網站**：添加追蹤代碼後：
  - 訪問您的網站並打開 Google Analytics 中的 **即時** 報告（在「報告」>「即時」下）。
  - 如果您看到訪問記錄，則整合成功。
  - 或者，使用瀏覽器工具（例如 **GA Checker** 或 Chrome DevTools 控制台）確認 `gtag` 請求。
- **應用程式**：在安裝 SDK 後啟動應用程式，檢查 Firebase 控制台或 GA4 即時報告。數據可能需要幾分鐘才會顯示。

---

### 4. 使用應用程式和網站檢查數據
一旦 Google Analytics 開始收集數據，您可以通過兩種方式查看它：
- **Google Analytics 網頁介面**：
  - 登錄 [analytics.google.com](https://analytics.google.com)。
  - 選擇您的 GA4 屬性。
  - 探索報告，例如：
    - **即時**：查看即時用戶活動。
    - **受眾**：了解用戶人口統計。
    - **獲取**：追蹤用戶來源。
    - **行為**：分析用戶互動（例如，頁面查看、事件）。
- **Google Analytics 行動應用程式**：
  - 從 App Store（iOS）或 Google Play Store（Android）下載官方 **Google Analytics** 應用程式。
  - 使用您的 Google 帳戶登錄並選擇您的屬性。
  - 在移動中查看報告子集（例如，即時、受眾）。

---

### 附加說明
- **如果您的項目包括網站和應用程式**：您可以在同一個 GA4 屬性下添加多個數據流（例如，一個用於網站，一個用於應用程式）。這使您可以在同一個介面中查看合併或單獨的分析。
- **追蹤事件**：除了頁面查看，還可以使用 `gtag('event', ...)` 追蹤自定義事件（例如，按鈕點擊）適用於網站或 Firebase 的 `logEvent` 適用於應用程式。網站的示例：
  ```javascript
  gtag('event', 'click', {
    'event_category': '按鈕',
    'event_label': '提交'
  });
  ```
- **GA4 與 Universal Analytics**：對於新項目，請使用 GA4，因為 Universal Analytics 在 2023 年 7 月 1 日後停止處理數據。

按照這些步驟，您將成功將 Google Analytics 整合到您的前端項目中，並能夠使用 Google Analytics 網站和行動應用程式監控用戶數據。如果您的項目類型（網站或應用程式）需要具體說明，請相應地調整整合步驟！