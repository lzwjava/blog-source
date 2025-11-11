---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Google Analytics
translated: true
type: note
---

要使用 Google Analytics，請將其整合到您的前端項目中，並透過應用程式和網站檢查數據，請按照以下步驟操作。本指南假設您的前端項目是網站或移動應用程式，並使用 **Google Analytics 4 (GA4)**（截至 2023 年的現行標準），因為 Universal Analytics 已不再支援新數據收集。

---

### 1. 設定 Google Analytics
在將 Google Analytics 整合到您的項目之前，您需要建立帳戶並進行配置：

- **建立帳戶**：前往 [analytics.google.com](https://analytics.google.com)，如果還沒有 Google 帳戶，請先註冊。
- **建立 GA4 資源**：
  - 點擊左下角的「管理」。
  - 在「資源」下，點擊「建立資源」，填寫您的項目詳細資訊，並選擇 **Google Analytics 4**。
- **添加數據流**：根據您的前端項目類型：
  - **對於網站**：選擇「網站」，輸入您的網站 URL，並為數據流命名（例如「我的網站」）。
  - **對於移動應用程式**：選擇「應用程式」，選擇 iOS 或 Android，並提供您的應用程式詳細資訊（例如套件名稱）。

設定數據流後，您將獲得一個**測量 ID**（例如 `G-XXXXXXXXXX`），用於整合。

---

### 2. 將 Google Analytics 整合到您的前端項目
整合過程取決於您的前端項目是網站還是移動應用程式。

#### 對於網站
- **添加 Google 代碼**：
  - 在您的 GA4 資源中，前往「數據流」，選擇您的網站數據流，並找到「代碼設定說明」。
  - 複製提供的 **Google 代碼** 腳本，如下所示：
    ```html
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_MEASUREMENT_ID"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'YOUR_MEASUREMENT_ID');
    </script>
    ```
  - 將此代碼貼到您網站 HTML 的 `<head>` 部分，並將 `YOUR_MEASUREMENT_ID` 替換為您的實際測量 ID。
- **對於單頁應用程式 (SPA)**（例如 React、Angular、Vue）：
  - 默認腳本僅追蹤初始頁面加載。對於 SPA（頁面在路由更改時不會重新加載），請使用庫來追蹤導航。例如，在 **React** 中：
    1. 安裝 `react-ga4` 庫：
       ```bash
       npm install react-ga4
       ```
    2. 在您的應用程式中初始化（例如在 `index.js` 或 `App.js` 中）：
       ```javascript
       import ReactGA from 'react-ga4';
       ReactGA.initialize('YOUR_MEASUREMENT_ID');
       ```
    3. 在路由更改時追蹤頁面瀏覽（例如使用 React Router）：
       ```javascript
       ReactGA.send({ hitType: "pageview", page: window.location.pathname });
       ```
       在路由更改時調用此代碼，例如在與路由器的位置綁定的 `useEffect` 鉤子中。
  - 其他框架也有類似的庫（例如 Angular 的 `ngx-analytics`、Vue 的 `vue-ga`—請檢查 GA4 兼容性）。
- **可選**：使用 **Google Tag Manager (GTM)** 代替硬編碼代碼，以便更輕鬆地管理追蹤腳本。

#### 對於移動應用程式
- **使用 Firebase（推薦）**：
  - 如果您的應用程式使用 Firebase，請啟用 **Google Analytics for Firebase**：
    1. 在 [console.firebase.google.com](https://console.firebase.google.com) 建立 Firebase 項目。
    2. 將您的應用程式添加到項目中（iOS 或 Android）。
    3. 按照提示下載配置文件（例如 iOS 的 `GoogleService-Info.plist`、Android 的 `google-services.json`）並將其添加到您的應用程式中。
    4. 安裝 Firebase SDK：
       - **iOS**：使用 CocoaPods（`pod 'Firebase/Analytics'`）並在 `AppDelegate` 中初始化。
       - **Android**：在 `build.gradle` 中添加依賴項並在您的應用程式中初始化。
    5. Firebase 會自動連結到您的 GA4 資源並開始收集數據。
- **不使用 Firebase**：
  - 使用獨立的 **Google Analytics SDK** 用於 iOS 或 Android（現在較少見，因為 GA4 與 Firebase 整合）。請參考官方文檔進行設定，因為它因平台而異。

---

### 3. 驗證整合
- **對於網站**：添加追蹤代碼後：
  - 訪問您的網站並在 Google Analytics 中打開**即時**報告（在「報告」>「即時」下）。
  - 如果您看到您的訪問被記錄，則整合正常。
  - 或者，使用瀏覽器工具如 **GA Checker** 或 Chrome DevTools 控制台來確認 `gtag` 調用。
- **對於應用程式**：在安裝 SDK 後啟動您的應用程式後，檢查 Firebase 控制台或 GA4 即時報告。數據可能需要幾分鐘才會顯示。

---

### 4. 使用應用程式和網站檢查數據
一旦 Google Analytics 開始收集數據，您可以透過兩種方式查看：
- **Google Analytics 網站界面**：
  - 登入 [analytics.google.com](https://analytics.google.com)。
  - 選擇您的 GA4 資源。
  - 探索報告，例如：
    - **即時**：查看即時用戶活動。
    - **受眾**：了解用戶人口統計。
    - **客戶開發**：追蹤用戶來源。
    - **行為**：分析用戶互動（例如頁面瀏覽、事件）。
- **Google Analytics 移動應用程式**：
  - 從 App Store (iOS) 或 Google Play Store (Android) 下載官方的 **Google Analytics 應用程式**。
  - 使用您的 Google 帳戶登入並選擇您的資源。
  - 在移動裝置上查看部分報告（例如即時、受眾）。

---

### 補充說明
- **如果您的項目同時包含網站和應用程式**：您可以在同一 GA4 資源下添加多個數據流（例如一個用於網站，一個用於應用程式）。這允許您在同一界面中查看合併或分開的分析數據。
- **追蹤事件**：除了頁面瀏覽外，還可以使用 `gtag('event', ...)` 用於網站或 Firebase 的 `logEvent` 用於應用程式來追蹤自定義事件（例如按鈕點擊）。網站示例：
  ```javascript
  gtag('event', 'click', {
    'event_category': 'Button',
    'event_label': 'Submit'
  });
  ```
- **GA4 與 Universal Analytics**：對於新項目，請使用 GA4，因為 Universal Analytics 在 2023 年 7 月 1 日後已停止處理數據。

通過遵循這些步驟，您將成功將 Google Analytics 整合到您的前端項目中，並能夠使用 Google Analytics 網站和移動應用程式來監控用戶數據。如果您的項目類型（網站或應用程式）需要具體說明，請相應調整整合步驟！