---
audio: false
generated: true
lang: zh
layout: post
title: 使用 Google Analytics
translated: true
---

要使用 Google Analytics，将其集成到前端项目中，并通过应用程序和网站检查数据，请按照以下步骤进行操作。本指南假设您的前端项目是网站或移动应用程序，并使用 **Google Analytics 4 (GA4)**，这是截至 2023 年的当前标准，因为通用分析不再支持新的数据收集。

---

### 1. 设置 Google Analytics
在将 Google Analytics 集成到项目中之前，您需要创建一个帐户并进行配置：

- **创建帐户**：转到 [analytics.google.com](https://analytics.google.com) 并使用您的 Google 帐户注册，如果您还没有帐户的话。
- **创建 GA4 属性**：
  - 点击左下角的“管理”。
  - 在“属性”下，点击“创建属性”，填写您的项目详细信息，并选择 **Google Analytics 4**。
- **添加数据流**：根据您的前端项目类型：
  - **对于网站**：选择“网站”，输入您的网站的 URL，并为流命名（例如，“我的网站”）。
  - **对于移动应用**：选择“应用”，选择 iOS 或 Android，并提供您的应用详细信息（例如，包名）。

设置数据流后，您将获得一个 **测量 ID**（例如，`G-XXXXXXXXXX`），您将用于集成。

---

### 2. 将 Google Analytics 集成到前端项目中
集成过程取决于您的前端项目是网站还是移动应用程序。

#### 对于网站
- **添加 Google 标签**：
  - 在您的 GA4 属性中，转到“数据流”，选择您的网络流，并找到“标记说明”。
  - 复制提供的 **Google 标签** 脚本，如下所示：
    ```html
    <!-- Google 标签 (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_MEASUREMENT_ID"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'YOUR_MEASUREMENT_ID');
    </script>
    ```
  - 将此代码粘贴到网站的 HTML 的 `<head>` 部分，将 `YOUR_MEASUREMENT_ID` 替换为您的实际测量 ID。
- **对于单页应用程序（SPAs）**（例如，React、Angular、Vue）：
  - 默认脚本仅跟踪初始页面加载。对于 SPAs，页面在路由更改时不会重新加载，因此使用库来跟踪导航。例如，在 **React**：
    1. 安装 `react-ga4` 库：
       ```bash
       npm install react-ga4
       ```
    2. 在应用程序中初始化它（例如，在 `index.js` 或 `App.js` 中）：
       ```javascript
       import ReactGA from 'react-ga4';
       ReactGA.initialize('YOUR_MEASUREMENT_ID');
       ```
    3. 在路由更改时跟踪页面视图（例如，使用 React Router）：
       ```javascript
       ReactGA.send({ hitType: "pageview", page: window.location.pathname });
       ```
       每当路由更改时调用此方法，例如在与路由器位置绑定的 `useEffect` 钩子中。
  - 其他框架也有类似的库（例如，`ngx-analytics` 适用于 Angular，`vue-ga` 适用于 Vue—请检查 GA4 兼容性）。
- **可选**：使用 **Google 标签管理器（GTM）** 而不是硬编码标签，以便更轻松地管理跟踪脚本。

#### 对于移动应用
- **使用 Firebase（推荐）**：
  - 如果您的应用使用 Firebase，请启用 **Firebase 的 Google Analytics**：
    1. 在 [console.firebase.google.com](https://console.firebase.google.com) 创建一个 Firebase 项目。
    2. 将应用添加到项目中（iOS 或 Android）。
    3. 按照提示下载配置文件（例如，iOS 的 `GoogleService-Info.plist`，Android 的 `google-services.json`）并将其添加到应用中。
    4. 安装 Firebase SDK：
       - **iOS**：使用 CocoaPods（`pod 'Firebase/Analytics'`）并在 `AppDelegate` 中初始化。
       - **Android**：在 `build.gradle` 中添加依赖项并在应用中初始化。
    5. Firebase 会自动链接到您的 GA4 属性并开始收集数据。
- **不使用 Firebase**：
  - 使用独立的 **Google Analytics SDK** 适用于 iOS 或 Android（现在 GA4 的 Firebase 集成较少）。请参考官方文档进行设置，因为它因平台而异。

---

### 3. 验证集成
- **对于网站**：添加跟踪代码后：
  - 访问您的网站并打开 Google Analytics 中的 **实时** 报告（在“报告” > “实时”下）。
  - 如果您看到访问记录，则集成正常工作。
  - 或者，使用浏览器工具（例如，GA 检查器）或 Chrome DevTools 控制台确认 `gtag` 调用。
- **对于应用**：在安装 SDK 并启动应用后，检查 Firebase 控制台或 GA4 实时报告。数据可能需要几分钟才会出现。

---

### 4. 使用应用程序和网站检查数据
一旦 Google Analytics 开始收集数据，您可以通过两种方式查看它：
- **Google Analytics 网络界面**：
  - 登录到 [analytics.google.com](https://analytics.google.com)。
  - 选择您的 GA4 属性。
  - 浏览报告，例如：
    - **实时**：查看实时用户活动。
    - **受众**：了解用户人口统计。
    - **获取**：跟踪用户来源。
    - **行为**：分析用户交互（例如，页面视图、事件）。
- **Google Analytics 移动应用**：
  - 从 App Store（iOS）或 Google Play Store（Android）下载官方 **Google Analytics** 应用。
  - 使用您的 Google 帐户登录并选择您的属性。
  - 在移动设备上查看报告子集（例如，实时、受众）。

---

### 附加说明
- **如果您的项目包括网站和应用**：您可以在同一 GA4 属性下添加多个数据流（例如，一个用于网站，一个用于应用）。这允许您在同一界面中查看组合或单独的分析。
- **跟踪事件**：除了页面视图，还可以使用 `gtag('event', ...)` 为网站或 Firebase 的 `logEvent` 为应用跟踪自定义事件。例如，对于网站：
  ```javascript
  gtag('event', 'click', {
    'event_category': 'Button',
    'event_label': 'Submit'
  });
  ```
- **GA4 与通用分析**：对于新项目，请使用 GA4，因为通用分析在 2023 年 7 月 1 日之后停止处理数据。

通过遵循这些步骤，您将成功将 Google Analytics 集成到前端项目中，并能够使用 Google Analytics 网站和移动应用监控用户数据。如果您的项目类型（网站或应用）需要特定的说明，请相应地调整集成步骤！