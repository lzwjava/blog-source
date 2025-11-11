---
audio: false
generated: true
lang: hant
layout: post
title: 在 IntelliJ IDEA 中處理非信任憑證
translated: true
type: note
---

IntelliJ IDEA 中的「未受信任伺服器憑證」對話框通常會在 IDE 遇到其金鑰儲存庫不信任的 SSL 憑證時出現，例如自簽憑證或自訂企業憑證。既然你已將企業金鑰儲存庫匯入至 `/lib/cacerts` 但仍看到提示，問題可能源自 IntelliJ 未使用該金鑰儲存庫，或其他額外憑證觸發了對話框。以下提供解決方法，可能可停止這些提示：

### 選項 1：設定 IntelliJ 自動接受非信任憑證
啟用此選項會讓 IntelliJ 略過未信任憑證的對話框，但請謹慎使用，因為這會降低安全性，接受所有憑證可能使你暴露於中間人攻擊的風險中。

- **Windows/Linux**：
  1. 前往 `檔案 > 設定 > 工具 > 伺服器憑證`。
  2. 勾選 **「自動接受非信任憑證」** 的核取方塊。
  3. 點擊 **套用** 與 **確定**。
- **macOS**：
  1. 前往 `IntelliJ IDEA > 偏好設定 > 工具 > 伺服器憑證`。
  2. 勾選 **「自動接受非信任憑證」**。
  3. 點擊 **套用** 與 **確定**。

**注意**：除非你處於受信任的隔離網路環境（例如氣隙企業環境），否則不建議啟用此選項，因為這可能使你的 IDE 容易遭受未經驗證的連線風險。

### 選項 2：驗證並修正金鑰儲存庫設定
既然你已將企業金鑰儲存庫匯入至 `/lib/cacerts`，請確保 IntelliJ 正確使用它。問題可能在於 IntelliJ 仍參考其自身的信任儲存庫或錯誤的 cacerts 檔案。

1. **檢查金鑰儲存庫路徑**：
   - IntelliJ 通常使用其自身的信任儲存庫，位於 `~/.IntelliJIdea<version>/system/tasks/cacerts`，或 JetBrains Runtime (JBR) 的信任儲存庫，位於 `<IntelliJ 安裝路徑>/jbr/lib/security/cacerts`。
   - 若你修改了 IntelliJ 目錄中的 `/lib/cacerts`，請確認該路徑適用於你的 IDE 版本。對於透過 JetBrains Toolbox 安裝的情況，路徑可能不同（例如 Windows 上的 `~/AppData/Local/JetBrains/Toolbox/apps/IDEA-U/ch-0/<version>/jbr/lib/security/cacerts`）。
   - 使用 `keytool` 指令驗證憑證是否存在於 cacerts 檔案中：
     ```bash
     keytool -list -keystore <cacerts-路徑> -storepass changeit
     ```
     確保你的企業 CA 憑證列於其中。

2. **設定 IntelliJ 使用自訂金鑰儲存庫**：
   - 若憑證已正確匯入但 IntelliJ 仍顯示提示，可能表示它未使用修改後的 cacerts。可新增自訂 VM 選項指定信任儲存庫：
     1. 前往 `說明 > 編輯自訂 VM 選項`。
     2. 新增：
        ```
        -Djavax.net.ssl.trustStore=<cacerts-路徑>
        -Djavax.net.ssl.trustStorePassword=changeit
        ```
        將 `<cacerts-路徑>` 替換為你修改後的 `cacerts` 檔案的完整路徑。
     3. 重新啟動 IntelliJ IDEA。

3. **重新匯入憑證**：
   - 若憑證匯入不完整或不正確，請重新匯入：
     ```bash
     keytool -import -trustcacerts -file <憑證檔案>.cer -alias <別名> -keystore <cacerts-路徑> -storepass changeit
     ```
     將 `<憑證檔案>.cer` 替換為你的企業 CA 憑證，`<cacerts-路徑>` 替換為正確的 cacerts 檔案路徑。

### 選項 3：透過 IntelliJ 的伺服器憑證設定新增憑證
無需手動修改 cacerts 檔案，你可透過 IntelliJ 的使用者介面新增憑證，這些憑證將儲存於其內部信任儲存庫：

1. 前往 `檔案 > 設定 > 工具 > 伺服器憑證`（macOS 為 `IntelliJ IDEA > 偏好設定`）。
2. 點擊 **「+」** 按鈕以新增憑證。
3. 瀏覽至你的企業 CA 憑證檔案（格式為 `.cer` 或 `.pem`）並匯入。
4. 重新啟動 IntelliJ 以確保憑證被識別。

### 選項 4：檢查代理伺服器或防毒軟體干擾
企業環境常使用代理伺服器或防毒軟體（例如 Zscaler、Forcepoint）進行中間人 SSL 檢查，動態產生新憑證。若這些憑證頻繁變更（例如 McAfee Endpoint Security 的每日更新），可能導致重複出現提示。

- **匯入代理伺服器/防毒軟體的 CA 憑證**：
  - 從你的代理伺服器或防毒軟體取得根 CA 憑證（請洽詢 IT 部門）。
  - 透過 `設定 > 工具 > 伺服器憑證` 將其匯入 IntelliJ 的信任儲存庫，或使用上述 `keytool` 指令匯入至 cacerts 檔案。
- **停用 SSL 檢查（若可行）**：
  - 若你的代理伺服器允許，可設定其略過 IntelliJ 相關網域（例如 `plugins.jetbrains.com`、`repo.maven.apache.org`）的 SSL 檢查。

### 選項 5：偵錯並識別問題憑證
若問題持續存在，請識別是哪個伺服器或憑證導致提示：

1. 啟用詳細 SSL 記錄：
   - 前往 `說明 > 編輯自訂 VM 選項` 並新增：
     ```
     -Djavax.net.debug=ssl:handshake:verbose
     ```
   - 重新啟動 IntelliJ 並檢查 `idea.log` 檔案（位於 `~/.IntelliJIdea<version>/system/log/`）中的 SSL 錯誤，例如 `PKIX path building failed`。這將顯示有問題的伺服器或憑證。

2. 檢查特定外掛或整合功能：
   - 如 Maven、Gradle 或版本控制系統（例如 Git、SVN）等外掛可能連線至使用不同憑證的伺服器。可暫時停用外掛以隔離問題。
   - 對於 Maven，請確保在 `檔案 > 設定 > 建置、執行、部署 > 建置工具 > Maven > Runner` 中設定的 JDK 使用已更新的 cacerts。

### 補充說明
- **安全性警告**：自動接受非信任憑證雖方便，但在非隔離網路中存在風險。請僅在受信任環境中使用此選項。
- **系統時間同步**：請確保系統時鐘已同步，因為時間不符可能導致憑證驗證問題。
- **JetBrains Runtime (JBR)**：IntelliJ 運行於其自身的 JBR，可能不會使用系統的 Java 信任儲存庫。對系統 `$JAVA_HOME/lib/security/cacerts` 的修改不會影響 IntelliJ，除非明確設定。
- **持續性提示**：若匯入憑證後提示仍持續出現，可能是由於某個外掛或服務（例如 JFrog、SonarQube）使用了不同的信任儲存庫。請檢查外掛設定或聯絡 IT 部門以取得完整的憑證鏈。

### 建議處理方式
1. 優先嘗試 **選項 3**（透過 IntelliJ 使用者介面新增憑證），這是最安全且最直接的方法。
2. 若無效，請透過 **選項 2** 驗證金鑰儲存庫路徑與設定。
3. 僅在受信任環境中，將 **選項 1**（自動接受）作為最後手段。
4. 若問題涉及代理伺服器或防毒軟體，請與 IT 團隊合作取得並匯入正確的 CA 憑證。

若你仍遇到問題，請提供憑證相關細節（例如簽發者、網域）或 `idea.log` 檔案中的任何錯誤訊息，我將協助進一步釐清問題。