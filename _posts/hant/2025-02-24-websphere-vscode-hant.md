---
audio: false
generated: true
lang: hant
layout: post
title: 使用 WebSphere Liberty 伺服器在 VSCode
translated: true
---

要在 Visual Studio Code (VSCode) 中使用 WebSphere Liberty 伺服器，可以利用 **Liberty Tools** 擴展，該擴展支持 Open Liberty 和 WebSphere Liberty。這個擴展允許你在 VSCode 中管理你的 Liberty 伺服器、部署應用程式並進行調試，從而簡化你的開發工作流程。

### 在 VSCode 中使用 WebSphere Liberty 的步驟

#### 1. **安裝 Liberty Tools 擴展**
   - 打開 VSCode 並通過點擊活動欄中的擴展圖標或按 `Ctrl+Shift+X` 導航到擴展視圖。
   - 在擴展市場中搜索 "Liberty Tools"。
   - 點擊 "安裝" 將擴展添加到 VSCode。
   - 如果提示，請重新加載 VSCode 以啟用擴展。

#### 2. **設置先決條件**
   - **Java**：確保已安裝兼容版本的 Java（建議使用 Java 8 或更高版本）。Liberty 是基於 Java 的伺服器，因此 Java 是運行它的必要條件。
   - **WebSphere Liberty**：如果尚未安裝，請下載並安裝 WebSphere Liberty 運行時。你可以從 [IBM 官方網站](https://www.ibm.com/docs/en/was-liberty) 获取它。請注意安裝目錄，因為你需要它來配置擴展。

#### 3. **配置 Liberty Tools 擴展**
   - 安裝擴展後，將其配置為指向你的 Liberty 安裝。
   - 通過按 `Ctrl+Shift+P` 打開 VSCode 的命令面板。
   - 鍵入 "Liberty: Add Liberty Runtime" 並選擇命令。
   - 提供你的 Liberty 安裝目錄的路徑（例如，`/opt/ibm/wlp`）。
   - 擴展將檢測到 Liberty 運行時並使其在 VSCode 中可用。

#### 4. **管理你的 Liberty 伺服器**
   - 配置後，可以直接在 VSCode 中管理你的 Liberty 伺服器。
   - **Liberty 儀表板**：在資源管理器窗格或通過命令面板訪問 Liberty 儀表板視圖。這個儀表板列出了你的 Liberty 專案和伺服器。
   - **啟動/停止伺服器**：在儀表板中右鍵點擊你的伺服器以啟動、停止或重啟它。
   - **部署應用程式**：對於 Liberty 專案（例如，具有 Liberty 插件的 Maven 或 Gradle 專案），右鍵點擊專案並選擇 "Deploy to Liberty" 以部署應用程式。
   - **開發模式（Dev 模式）**：對於 Maven 或 Gradle 專案，以 dev 模式啟動伺服器，它會自動檢測代碼變更、重新編譯並重新部署應用程式而不重啟伺服器。這對於迭代開發非常理想。

#### 5. **調試和測試**
   - **調試**：直接從 VSCode 將調試器附加到運行中的 Liberty 伺服器。使用 Liberty 儀表板中的 "Debug" 選項或在 VSCode 的運行和調試視圖中設置調試配置。
   - **運行測試**：如果你的專案包含測試，可以從儀表板運行它們並在 VSCode 中查看結果。

#### 6. **其他功能**
   - **配置協助**：擴展為 Liberty 配置文件（例如 `server.xml`）提供代碼補全、驗證和懸停描述，簡化伺服器配置。
   - **語言支持**：它支持 Java、MicroProfile 和 Jakarta EE API，增強你的開發體驗。

### 主要優點
- **無縫整合**：在不離開 VSCode 的情況下管理你的 Liberty 伺服器，提高效率。
- **自動部署**：在 dev 模式下，代碼變更會自動檢測並部署，節省開發時間。
- **調試支持**：輕鬆將調試器附加到你的伺服器以進行故障排除。
- **輕量且高效**：Liberty Tools 設計輕量，與 Liberty 專注於速度和效率相一致。

### 其他資源
- 詳細指南，請參考 [Open Liberty 文檔](https://openliberty.io/docs/) 和 [Liberty Tools VSCode 文檔](https://openliberty.io/docs/latest/develop/liberty-tools.html)。
- 如果遇到問題，請檢查擴展的故障排除部分或在 Stack Overflow 等平台上尋求社區幫助。

通過遵循這些步驟，你可以在 VSCode 中有效地使用 WebSphere Liberty，利用其功能來增強你的開發過程。