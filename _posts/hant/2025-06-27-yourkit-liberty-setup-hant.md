---
audio: false
generated: true
lang: hant
layout: post
title: 在 Windows 上整合 YourKit Profiler 與 WebSphere Liberty
translated: true
type: note
---

在 Windows 系統上使用 YourKit Java Profiler 與 WebSphere Liberty Server 涉及將 YourKit 代理程式整合到 WebSphere Liberty JVM 中，並進行效能分析配置。以下是根據現有資訊以及 YourKit 與 WebSphere Liberty 整合的最佳實踐所整理的設定步驟：

### 先決條件
- **YourKit Java Profiler**：已安裝在您的 Windows 機器上。請從 [YourKit 官方網站](https://www.yourkit.com/) 下載，並確保您擁有有效的授權或試用金鑰。
- **WebSphere Liberty**：已安裝並在您的 Windows 系統上運行。確保您擁有伺服器配置檔案的系統管理員存取權限。
- **Java JDK**：WebSphere Liberty 使用 Java 運行環境（IBM JDK 或 OpenJDK）。請確認 JDK 版本與 YourKit 相容（YourKit 支援 Java 5 及更高版本，但請驗證與您特定版本的相容性）。
- **系統管理員權限**：需要修改 WebSphere Liberty 配置檔案。

### 逐步指南

1. **安裝 YourKit Java Profiler**
   - 從 [YourKit 網站](https://www.yourkit.com/download) 下載並安裝 YourKit Java Profiler for Windows。
   - 記下安裝目錄，因為您將需要 YourKit 代理程式庫（`yjpagent.dll`）的路徑。

2. **找到 YourKit 代理程式**
   - YourKit 代理程式在 Windows 上的通常位置為：
     ```
     C:\Program Files\YourKit-Java-Profiler-<version>\bin\win64\yjpagent.dll
     ```
     （如果運行 32 位元 JVM，請使用 `win32` 代替 `win64`。）
   - 確保代理程式與 WebSphere Liberty 使用的 JVM 架構（32 位元或 64 位元）相符。

3. **配置 WebSphere Liberty 使用 YourKit 代理程式**
   - **找到 `jvm.options` 檔案**：
     - 導航至您的 WebSphere Liberty 伺服器配置目錄，通常為：
       ```
       <LIBERTY_INSTALL_DIR>\usr\servers\<server_name>\jvm.options
       ```
       將 `<LIBERTY_INSTALL_DIR>` 替換為您的 WebSphere Liberty 安裝路徑（例如 `C:\wlp`），並將 `<server_name>` 替換為您的伺服器名稱（例如 `defaultServer`）。
     - 如果 `jvm.options` 檔案不存在，請在伺服器目錄中創建它。
   - **添加 YourKit 代理程式路徑**：
     - 使用系統管理員權限在文字編輯器中打開 `jvm.options`。
     - 添加以下行以包含 YourKit 代理程式：
       ```
       -agentpath:C:\Program Files\YourKit-Java-Profiler-<version>\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
       ```
       - 將 `<version>` 替換為您的 YourKit 版本（例如 `2023.9`）。
       - 這些選項（`disablestacktelemetry`、`disableexceptiontelemetry`、`probe_disable=*`）通過停用不必要的遙測來減少負載。`delay=10000` 確保代理程式在伺服器初始化後啟動，而 `sessionname=WebSphereLiberty` 用於識別效能分析工作階段。
       - 範例：
         ```
         -agentpath:C:\Program Files\YourKit-Java-Profiler-2023.9\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
         ```
   - **儲存檔案**：確保您對 `jvm.options` 檔案擁有寫入權限。

4. **驗證 JVM 相容性**
   - WebSphere Liberty 通常使用 IBM JDK 或 OpenJDK。YourKit 與兩者都相容，但如果您遇到問題（例如某些 IBM JDK 案例中出現的 `NoSuchMethodError`），請在代理程式路徑中添加 `probe_disable=*` 以停用可能與 IBM JDK 衝突的探針。[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=8042)
   - 檢查 Liberty 使用的 Java 版本：
     ```
     <LIBERTY_INSTALL_DIR>\java\bin\java -version
     ```
     確保它受 YourKit 支援（舊版本支援 Java 5 或更高版本；現代版本支援 Java 8+）。

5. **啟動 WebSphere Liberty**
   - 照常啟動您的 WebSphere Liberty 伺服器：
     ```
     <LIBERTY_INSTALL_DIR>\bin\server start <server_name>
     ```
     範例：
     ```
     C:\wlp\bin\server start defaultServer
     ```
   - 檢查伺服器日誌（`<LIBERTY_INSTALL_DIR>\usr\servers\<server_name>\logs\console.log` 或 `messages.log`）以查找與 YourKit 代理程式相關的任何錯誤。
   - 在以下位置查找 YourKit 代理程式日誌：
     ```
     %USERPROFILE%\.yjp\log\<session_name>-<pid>.log
     ```
     範例：
     ```
     C:\Users\<YourUsername>\.yjp\log\WebSphereLiberty-<pid>.log
     ```
     日誌應顯示代理程式已加載並正在監聽某個端口（預設：10001）：
     ```
     Profiler agent is listening on port 10001
     ```

6. **連接 YourKit Profiler UI**
   - 在您的 Windows 機器上啟動 YourKit Java Profiler UI。
   - 在 YourKit UI 中，選擇 **Profile | Profile Local Java Server or Application** 或 **Profile | Profile Remote Java Server or Application**。
     - 對於本地效能分析（因為 YourKit 和 Liberty 在同一台機器上），選擇 **Profile Local Java Server or Application**。
     - UI 應檢測到 WebSphere Liberty 進程（由 `sessionname=WebSphereLiberty` 識別）。
   - 如果未自動檢測到，請使用 **Profile Remote Java Server or Application**，選擇 **Direct Connect**，並輸入：
     - **Host**：`localhost`
     - **Port**：`10001`（或代理程式日誌中指定的端口）。
   - 連接到伺服器。UI 將顯示 CPU、記憶體和線程遙測數據。

7. **對應用程式進行效能分析**
   - 使用 YourKit UI 進行以下操作：
     - **CPU 效能分析**：啟用 CPU 取樣或追蹤以識別效能瓶頸。對於高負載系統，避免啟用 "Profile J2EE" 以最小化負載。[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)
     - **記憶體效能分析**：通過按 Web 應用程式分組物件來分析堆使用情況並檢測記憶體泄漏（對於 Liberty 託管的應用程式非常有用）。[](https://www.yourkit.com/docs/java-profiler/latest/help/webapps.jsp)
     - **線程分析**：在 Threads 標籤頁中檢查死鎖或凍結的線程。[](https://www.yourkit.com/changes/)
   - 如果需要，可以拍攝快照以供離線分析（File | Save Snapshot）。
   - 監控記憶體使用情況，因為效能分析可能會增加記憶體消耗。避免在沒有監控的情況下進行長時間的效能分析工作階段。[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

8. **疑難排解**
   - **伺服器啟動失敗或變得無法訪問**：
     - 檢查日誌（`console.log`、`messages.log` 和 YourKit 代理程式日誌）以查找錯誤，例如 `OutOfMemoryError` 或 `NoSuchMethodError`。[](https://www.yourkit.com/forum/viewtopic.php?t=328)[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
     - 確保 `-agentpath` 已添加到正確的 `jvm.options` 檔案中，並且與用於啟動 Liberty 的腳本相符。[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
     - 如果使用 IBM JDK，請嘗試在代理程式路徑中添加 `probe_disable=*` 以避免衝突。[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=8042)
   - **ClassNotFoundException**：
     - 如果您看到類似 `java.lang.ClassNotFoundException` 的錯誤（例如對於 `java.util.ServiceLoader`），請確保 YourKit 代理程式版本與您的 JDK 相容。對於舊版 IBM JDK（例如 Java 5），請使用 YourKit 8.0 或更早版本。[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=7149)
   - **沒有效能分析數據**：
     - 驗證 YourKit 代理程式和 UI 版本是否匹配。版本不匹配可能導致連接問題。[](https://www.yourkit.com/forum/viewtopic.php?t=328)
     - 確保可以通過瀏覽器訪問伺服器（例如，如果使用 SSL，則為 `https://localhost:9443`）。如果不能，請檢查防火牆設置或 SSL 配置。[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
   - **日誌檔案問題**：
     - 如果在 `~/.yjp/log/` 中沒有創建 YourKit 日誌，請確保進程對用戶的家目錄擁有寫入權限。[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=3219)
   - **效能影響**：
     - 效能分析可能會影響效能。在類似生產環境中，請使用最小設置（例如，停用堆疊遙測）。[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

9. **可選：使用 YourKit 整合精靈**
   - YourKit 提供了一個 Java Server Integration Wizard 來簡化配置：
     - 啟動 YourKit UI 並選擇 **Profile | Profile Local Java Server or Application**。
     - 從支援的伺服器列表中選擇 **WebSphere Liberty**（如果 Liberty 未列出，則選擇 "Other Java application"）。
     - 按照精靈生成必要的 `-agentpath` 設置並更新 `jvm.options`。確保您對配置檔案擁有寫入權限。[](https://www.yourkit.com/docs/java-profiler/latest/help/java-server-integration-wizard.jsp)
   - 這對於確保正確的路徑和設置特別有用。

10. **停止效能分析**
    - 要停用效能分析，請移除或註釋掉 `jvm.options` 中的 `-agentpath` 行，然後重新啟動伺服器。
    - 或者，停止伺服器：
      ```
      <LIBERTY_INSTALL_DIR>\bin\server stop <server_name>
      ```

### 補充說明
- **授權**：伺服器上的 YourKit 代理程式不需要授權金鑰；授權在 YourKit UI 中應用。如果從另一台 Windows 機器進行遠端效能分析，請確保 UI 擁有有效的授權。[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=11385)[](https://www.yourkit.com/forum/viewtopic.php?t=11385)
- **遠端效能分析**：如果從不同的機器進行效能分析，請確保網絡連接到代理程式端口（預設：10001），並使用 **Profile Remote Java Server or Application** 選項，輸入伺服器的主機名/IP。
- **效能考量**：效能分析可能會增加記憶體和 CPU 使用量。對於生產系統，請從最小效能分析選項（例如 CPU 取樣）開始，並監控伺服器健康狀態。[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)
- **相容性**：如果使用舊版 WebSphere Liberty 與 IBM JDK 1.4.2 或 1.5，您可能需要舊版 YourKit（例如，對於 Java 5 使用 8.0 版）。[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=7149)[](https://stackoverflow.com/questions/61795/java-profiler-for-ibm-jvm-1-4-2-websphere-6-0-2)
- **文件**：請參考 YourKit 官方文件以獲取詳細的效能分析選項：[YourKit Java Profiler Help](https://www.yourkit.com/docs/java/help/)。[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

### 配置範例
以下是一個範例 `jvm.options` 檔案：
```
-Xmx4G
-Xms4G
-agentpath:C:\Program Files\YourKit-Java-Profiler-2023.9\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
```

### 測試設定
- 啟動伺服器後，訪問您的應用程式（例如 `https://localhost:9443`）以確保其正在運行。
- 在 YourKit UI 中，驗證是否顯示了遙測數據（CPU、記憶體、線程）。
- 如果出現問題，請檢查 YourKit 代理程式日誌和 Liberty 日誌以查找錯誤。

如果您遇到特定錯誤或需要某個步驟的進一步幫助，請告訴我，我可以提供更多協助！