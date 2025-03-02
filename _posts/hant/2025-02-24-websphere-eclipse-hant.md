---
audio: false
generated: true
lang: hant
layout: post
title: 使用 WebSphere Liberty 與 Eclipse
translated: true
---

要在 Eclipse 中使用 WebSphere 插件工具並與 WebSphere Liberty 集成，您可以選擇兩個主要選項：**IBM Liberty Developer Tools** 和 **Liberty Tools**。兩者均可通過 Eclipse Marketplace 獲取，並提供構建、部署和管理 WebSphere Liberty 上的應用程序的功能，WebSphere Liberty 是一個輕量級、可生產的 Java EE 和雲原生應用程序伺服器。以下是如何使用和集成這些工具的詳細指南。

---

### **工具概述**
- **IBM Liberty Developer Tools**：IBM 提供的傳統插件，用於在 Eclipse 中管理 Liberty 伺服器。它允許您創建和管理 Liberty 伺服器，部署應用程序，並直接從 IDE 中進行調試。這個工具適合伺服器中心工作流或不使用 Maven 或 Gradle 的項目。
- **Liberty Tools**：專注於 Maven 和 Gradle 項目的下一代開源替代方案。它提供了更緊密的構建工具集成、自動檢測 Liberty 項目和對 Liberty 的開發模式（開發模式）的支持。這個工具更適合現代、構建工具中心的工作流。

兩個工具都簡化了 WebSphere Liberty 的開發，但它們在方法上有所不同。選擇最適合您的項目類型和開發偏好的工具。

---

### **安裝**
1. **安裝 Eclipse**：
   - 使用兼容版本，例如 **Eclipse for Enterprise Java and Web Developers**。
   - 確保您的 Eclipse 版本支持您選擇的插件（在市場列表中檢查兼容性）。

2. **安裝插件**：
   - 打開 Eclipse 並前往 **Help > Eclipse Marketplace**。
   - 搜索：
     - "IBM Liberty Developer Tools" 以獲取傳統 IBM 工具集，或
     - "Liberty Tools" 以獲取開源替代方案。
   - 按照提示安裝所需的插件。

---

### **設置 Liberty 運行時**
- **下載 Liberty**：
  - 如果還沒有，請從 [官方 IBM 網站](https://www.ibm.com/docs/en/was-liberty) 下載 WebSphere Liberty 運行時。
  - 確保 Liberty 版本與您安裝的插件兼容。

- **在 Eclipse 中配置運行時**：
  - 針對 **IBM Liberty Developer Tools**：
    - 前往 **Window > Preferences > Server > Runtime Environments**。
    - 點擊 "Add"，選擇 "Liberty Server"，並指定到您的 Liberty 安裝目錄的路徑。
  - 針對 **Liberty Tools**：
    - 不需要顯式運行時配置。Liberty Tools 通過 Maven 或 Gradle 配置檢測 Liberty 項目，因此請確保您的項目已正確設置（見下文）。

---

### **與您的項目集成**
兩個工具的集成過程略有不同。根據您安裝的工具，請按照以下步驟操作。

#### **針對 IBM Liberty Developer Tools**
1. **創建 Liberty 伺服器**：
   - 打開 **Servers** 視圖 (**Window > Show View > Servers**)。
   - 在 Servers 視圖中右鍵點擊並選擇 **New > Server**。
   - 從列表中選擇 "Liberty Server"，並按照向導配置伺服器，包括指定到您的 Liberty 安裝的路徑。

2. **添加您的項目**：
   - 在 Servers 視圖中右鍵點擊伺服器並選擇 **Add and Remove...**。
   - 選擇您的項目並將其移動到 "Configured" 邊。

3. **啟動伺服器**：
   - 右鍵點擊伺服器並選擇 **Start** 或 **Debug** 以運行您的應用程序。
   - 在指定的 URL（默認：`http://localhost:9080/<context-root>`）訪問您的應用程序。

#### **針對 Liberty Tools (Maven/Gradle 項目)**
1. **確保項目配置**：
   - 您的項目必須包含必要的 Liberty 插件：
     - 針對 Maven：在 `pom.xml` 中添加 `liberty-maven-plugin`。
     - 針對 Gradle：在 `build.gradle` 中添加 `liberty-gradle-plugin`。
   - `server.xml` 配置文件應位於標準位置：
     - 針對 Maven：`src/main/liberty/config`。
     - 針對 Gradle：根據您的項目結構進行調整。

2. **使用 Liberty 儀表板**：
   - 點擊 Eclipse 工具欄中的 Liberty 圖標以打開 **Liberty 儀表板**。
   - Liberty Tools 會自動檢測並在儀表板中列出您的 Liberty 項目。
   - 在儀表板中右鍵點擊您的項目以訪問命令，例如：
     - "在開發模式下啟動"（自動重新部署更改而不重新啟動伺服器）。
     - "運行測試"。
     - "查看測試報告"。

3. **訪問您的應用程序**：
   - 伺服器運行後，在指定的 URL（默認：`http://localhost:9080/<context-root>`）訪問您的應用程序。
   - 在開發模式下，對代碼進行更改，Liberty 會自動重新部署它們。

---

### **關鍵功能**
兩個工具都提供強大的功能來提高生產力：

- **伺服器管理**：
  - 直接從 Eclipse 啟動、停止和調試 Liberty 伺服器。
- **應用程序部署**：
  - 方便地部署和重新部署應用程序。
- **配置協助**：
  - 兩個工具都提供代碼補全、驗證和懸停描述，用於 Liberty 配置文件（例如 `server.xml`）。
- **開發模式**：
  - 自動檢測和重新部署代碼更改而不重新啟動伺服器（特別是使用 Liberty Tools 的開發模式）。
- **調試**：
  - 將 Eclipse 调試器附加到 Liberty 伺服器以進行故障排除。

---

### **考慮事項和潛在問題**
- **版本兼容性**：
  - 確保您的 Eclipse、插件和 Liberty 運行時版本兼容。檢查文檔以獲取具體要求。
- **項目配置**：
  - 針對 Liberty Tools，您的項目必須是正確配置的 Maven 或 Gradle 項目，並包含 Liberty 插件。
  - 確保 `server.xml` 位於工具預期的位置，以便工具識別您的項目。
- **網絡設置**：
  - 確保默認 Liberty 端口（例如 9080 供 HTTP，9443 供 HTTPS）開放且未被防火牆阻擋。
- **Java 兼容性**：
  - Liberty 是基於 Java 的伺服器，因此請確保已安裝與您的 Liberty 運行時兼容的 Java 版本。

---

### **快速開始使用 Liberty Tools (Maven/Gradle)**
如果您使用 Maven 或 Gradle，Liberty Tools 提供了簡化的體驗。以下是逐步指南：

1. 安裝 **Eclipse for Enterprise Java and Web Developers**。
2. 前往 **Help > Eclipse Marketplace**，搜索 "Liberty Tools"，並安裝插件。
3. 創建或導入配置為 Liberty 的 Maven/Gradle 項目：
   - 您可以使用 [Open Liberty Starter](https://openliberty.io/start/) 生成示例項目。
4. 確保您的項目配置了 `liberty-maven-plugin`（針對 Maven）或 `liberty-gradle-plugin`（針對 Gradle）。
5. 通過點擊工具欄中的 Liberty 圖標打開 **Liberty 儀表板**。
6. 您的項目應該出現在儀表板中。右鍵點擊它並選擇 "在開發模式下啟動"。
7. 在指定的 URL（默認：`http://localhost:9080/<context-root>`）訪問您的應用程序。
8. 對代碼進行更改；Liberty 開發模式會自動重新部署它們。
9. 使用儀表板運行測試或查看測試報告。

---

### **選擇工具**
- **IBM Liberty Developer Tools**：
  - 適合傳統伺服器管理方法或不使用 Maven 或 Gradle 的項目。
  - 提供 Servers 視圖以顯式管理 Liberty 伺服器。
- **Liberty Tools**：
  - 更適合 Maven 或 Gradle 項目，與這些構建系統更緊密集成。
  - 提供 Liberty 儀表板進行項目中心管理和開發模式支持。
  - 開源，允許社區貢獻和更新。

兩個工具均可從 Eclipse Marketplace 获取，因此您可以嘗試兩者並選擇最適合您工作流的工具。

---

總結來說，在 Eclipse 中使用 WebSphere 插件工具涉及安裝適當的插件、設置 Liberty 運行時並配置您的項目以與 Liberty 協同工作。無論您選擇 IBM Liberty Developer Tools 還是 Liberty Tools，兩者都提供強大的功能來簡化 Eclipse IDE 中的 WebSphere Liberty 開發。