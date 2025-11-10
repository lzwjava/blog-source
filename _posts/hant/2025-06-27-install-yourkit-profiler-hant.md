---
audio: false
generated: true
lang: hant
layout: post
title: 在Ubuntu上安裝YourKit Java Profiler
translated: true
type: note
---

要在 Ubuntu 上安裝 YourKit Java Profiler，請根據 YourKit 網站提供的資訊遵循以下步驟：

1. **下載分析器**：
   - 造訪 YourKit Java Profiler 下載頁面：[https://www.yourkit.com/java/profiler/download/](https://www.yourkit.com/java/profiler/download/)
   - 選擇支援 Java 8 至 Java 24 的 YourKit Java Profiler 2025.3 Linux 版本，該版本相容於 Linux（包括 Ubuntu）並支援 arm32、arm64、ppc64le、x64 及 x86 架構。請確保系統符合[系統需求](https://www.yourkit.com/docs/java/system-requirements/)以保證相容性。

2. **下載壓縮檔**：
   - 下載適用於 Linux 的 `.zip` 壓縮檔（例如 `YourKit-JavaProfiler-2025.3-<build>.zip`）。下載連結可在 YourKit 下載頁面找到。

3. **解壓縮檔案**：
   - 開啟終端機並導航至下載檔案所在目錄（例如 `~/Downloads`）。
   - 使用以下指令解壓縮：
     ```bash
     unzip YourKit-JavaProfiler-2025.3-<build>.zip -d /opt/yourkit
     ```
     請將 `<build>` 替換為下載檔案的實際建置編號。此指令會將分析器解壓至 `/opt/yourkit`。您亦可選擇其他目錄。

4. **執行分析器**：
   - 導航至解壓後的目錄：
     ```bash
     cd /opt/yourkit
     ```
   - 使用提供的指令碼執行分析器：
     ```bash
     ./bin/profiler.sh
     ```
     這將啟動 YourKit Java Profiler 使用者介面。

5. **可選：使用授權金鑰進行自動化安裝**：
   - 若您擁有授權金鑰並希望自動化安裝流程，可使用命令列選項接受 EULA 並套用授權金鑰。例如：
     ```bash
     ./bin/profiler.sh -accept-eula -license-key=<key>
     ```
     請將 `<key>` 替換為實際授權金鑰。此方式適用於自動化或腳本設定。

6. **整合開發環境（可選）**：
   - 若您使用 Eclipse、IntelliJ IDEA 或 NetBeans 等 IDE，YourKit 提供外掛程式以實現無縫整合。以 Eclipse 為例：
     - 開啟 Eclipse 並前往 **Help > Install New Software**。
     - 新增 YourKit 外掛程式儲存庫：`https://www.yourkit.com/download/yjp2025_3_for_eclipse/`。
     - 選擇 YourKit Java Profiler 外掛程式，依循安裝提示操作，並在需要時重新啟動 Eclipse。
     - 或可使用離線壓縮檔：`<Profiler Installation Directory>/lib/eclipse-plugin/yjp2025_3_for_eclipse.zip`。
   - 安裝完成後，Eclipse 的工具列、主選單或右鍵選單中將出現「Profile」操作選項，方便進行效能分析。

7. **驗證安裝**：
   - 當分析器啟動後，歡迎畫面將允許您監控本機執行的 Java 應用程式、連接遠端應用程式或開啟現有快照。您亦可載入示範應用程式以探索分析器功能。

8. **補充說明**：
   - 若遇到問題，請確保系統已安裝 Java（版本 8 或更高），因為 YourKit Java Profiler 需要相容的 JVM。您可透過以下指令檢查 Java 版本：
     ```bash
     java -version
     ```
   - 如需遠端分析，請確保已配置 SSH 存取權限（若需分析遠端伺服器上的應用程式）。
   - YourKit 提供 15 天免費試用，因此初期無需授權金鑰。若為非商業開源專案，可聯繫 YourKit 銷售部門申請免費授權。
   - 若分析器啟動失敗（例如因安裝路徑包含空格），請將解壓後的資料夾移至不含空格的路徑，例如 `/opt/yourkit`。

如需進一步協助，請參閱 [YourKit 說明文件](https://www.yourkit.com/docs/java/)或透過 [YourKit 網站](https://www.yourkit.com/support/)聯繫技術支援。

如有任何特定步驟需要協助，請隨時告知！