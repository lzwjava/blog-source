---
audio: false
generated: true
lang: hant
layout: post
title: 在 VSCode 中配置 Gradle 代理設定
translated: true
type: note
---

要為 Visual Studio Code (VSCode) 中的 Gradle 配置代理，使其能透過代理下載依賴項，您需要在 Gradle 的配置中設定代理設定。Gradle 使用屬性檔案來管理此類設定，而 VSCode 的 Gradle 專案則依賴 Gradle 的建置系統。以下是具體步驟：

### 在 VSCode 中配置 Gradle 代理的步驟

1. **尋找或建立 Gradle 屬性檔案**
   - Gradle 使用名為 `gradle.properties` 的檔案來儲存全域配置設定。
   - 該檔案通常位於 Gradle 用戶主目錄中：
     - Windows：`C:\Users\<您的用戶名>\.gradle\gradle.properties`
     - macOS/Linux：`~/.gradle/gradle.properties`
   - 如果檔案不存在，請在以上位置建立。

2. **將代理設定加入 `gradle.properties`**
   - 在文字編輯器中開啟 `gradle.properties` 檔案。
   - 加入以下行，並將佔位符（`<proxyHost>`、`<proxyPort>`、`<username>`、`<password>`）替換為您的實際代理詳細資訊：
     ```
     systemProp.http.proxyHost=<proxyHost>
     systemProp.http.proxyPort=<proxyPort>
     systemProp.http.proxyUser=<username>
     systemProp.http.proxyPassword=<password>
     systemProp.https.proxyHost=<proxyHost>
     systemProp.https.proxyPort=<proxyPort>
     systemProp.https.proxyUser=<username>
     systemProp.https.proxyPassword=<password>
     ```
   - 實際數值範例：
     ```
     systemProp.http.proxyHost=proxy.example.com
     systemProp.http.proxyPort=8080
     systemProp.http.proxyUser=myuser
     systemProp.http.proxyPassword=mypassword
     systemProp.https.proxyHost=proxy.example.com
     systemProp.https.proxyPort=8080
     systemProp.https.proxyUser=myuser
     systemProp.https.proxyPassword=mypassword
     ```
   - 如果您的代理不需要驗證（用戶名/密碼），可以省略 `proxyUser` 和 `proxyPassword` 行。

3. **可選：按專案配置代理**
   - 如果您希望代理設定僅應用於特定專案（而非全域），您可以將 `gradle.properties` 檔案加入專案的根目錄（例如 `<project-root>/gradle.properties`），內容與上述相同。

4. **驗證 Gradle 使用代理**
   - 在 VSCode 中開啟您的 Gradle 專案。
   - 透過 VSCode 終端機或 Gradle 擴充功能執行建置任務（例如 `gradle build`）。
   - Gradle 現在應透過指定的代理路由其下載（例如從官方網站下載依賴項）。

5. **VSCode 特定注意事項**
   - 確保 VSCode 中已安裝 **Java Extension Pack** 和 **Gradle for Java** 擴充功能，因為它們增強了 Gradle 專案支援。
   - 如果 VSCode 仍有問題，請檢查您的 Java 運行時環境（由 Gradle 使用）是否也尊重代理設定。您可能需要設定 JVM 代理參數：
     - 在 VSCode 中，前往 `檔案 > 偏好設定 > 設定`。
     - 搜尋 `java.gradle.build.jvmArguments`。
     - 加入類似以下內容：
       ```
       -Dhttp.proxyHost=<proxyHost> -Dhttp.proxyPort=<proxyPort> -Dhttps.proxyHost=<proxyHost> -Dhttps.proxyPort=<proxyPort>
       ```

6. **測試配置**
   - 在 VSCode 中重新載入專案（例如關閉並重新開啟，或使用 Gradle 側邊欄中的「重新整理」按鈕）。
   - 執行 Gradle 任務（例如 `gradle build` 或 `gradle dependencies`）以確認其透過代理下載檔案。

### 疑難排解
- **檢查代理詳細資訊**：確保您的代理主機、端口和憑證正確無誤。
- **防火牆或網路**：如果仍然失敗，您的代理或網路可能封鎖了特定的 Gradle URL（例如 `https://services.gradle.org`）。請使用 `curl` 等指令進行測試，或諮詢您的網路管理員。
- **詳細輸出**：在 VSCode 終端機中執行 Gradle 時加上 `--debug` 或 `--info`（例如 `gradle build --debug`）以查看有關網路請求的詳細日誌。

此設定應能讓 VSCode 中的 Gradle 成功透過您的代理下載依賴項。如果您遇到任何問題，請告知！