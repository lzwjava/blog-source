---
audio: false
generated: true
lang: hant
layout: post
title: 修復 VisualVM 中的「不支援的 OpenJDK」錯誤
translated: true
type: note
---

在執行 VisualVM 時出現「OpenJDK 版本不受支援，請使用 default-jdk」的錯誤訊息，表示當前使用的 Java 開發工具包（JDK）版本與 VisualVM 不相容。此問題通常發生在 VisualVM 找不到受支援的 JDK，或已安裝的 JDK 未正確配置時。以下根據您的環境設定（YourKit Java Profiler 2025.3 及 VisualVM，疑似在 Linux 系統上運行）提供解決步驟。

### 解決問題的步驟

1. **檢查當前 Java 版本**
   執行以下指令確認已安裝的 Java 版本：
   ```bash
   java -version
   ```
   此指令將顯示 OpenJDK 版本，例如：
   ```
   openjdk version "17.0.9" 2023-10-17
   OpenJDK Runtime Environment (build 17.0.9+9-Ubuntu-122.04)
   OpenJDK 64-Bit Server VM (build 17.0.9+9-Ubuntu-122.04, mixed mode, sharing)
   ```
   VisualVM 通常需要 JDK（不僅是 JRE）並支援 Oracle JDK 8+ 或相容的 OpenJDK 版本。請確保已安裝受支援的 JDK。[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)[](https://visualvm.github.io/troubleshooting.html)

2. **安裝預設 JDK**
   錯誤訊息建議使用 `default-jdk`。在 Ubuntu/Debian 系統上可透過以下指令安裝：
   ```bash
   sudo apt update
   sudo apt install default-jdk
   ```
   此操作通常會安裝穩定且受支援的 OpenJDK 版本（例如 OpenJDK 11 或 17）。安裝完成後，請再次使用 `java -version` 確認版本。[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)[](https://askubuntu.com/questions/1504020/visualvm-version-of-openjdk-is-not-supported)

3. **設定 JAVA_HOME 環境變數**
   VisualVM 依賴 `JAVA_HOME` 環境變數來定位 JDK。檢查是否已設定：
   ```bash
   echo $JAVA_HOME
   ```
   若未設定或指向不受支援的 JDK，請將其設定至正確的 JDK 路徑。例如若 `default-jdk` 安裝了 OpenJDK 17，路徑可能為 `/usr/lib/jvm/java-17-openjdk-amd64`。設定指令如下：
   ```bash
   export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
   ```
   若要永久生效，請將此行加入 `~/.bashrc` 或 `~/.zshrc`：
   ```bash
   echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
   source ~/.bashrc
   ```
   請將路徑替換為您系統上的實際 JDK 路徑（可使用 `update-alternatives --list java` 查詢）。[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)[](https://github.com/oracle/visualvm/issues/558)

4. **為 VisualVM 指定 JDK 路徑**
   若設定 `JAVA_HOME` 仍無法解決問題，可在啟動 VisualVM 時明確指定 JDK 路徑：
   ```bash
   ~/bin/YourKit-JavaProfiler-2025.3/bin/visualvm --jdkhome /usr/lib/jvm/java-17-openjdk-amd64
   ```
   請將 `/usr/lib/jvm/java-17-openjdk-amd64` 替換為您的 JDK 路徑。此操作可確保 VisualVM 使用指定的 JDK。[](https://visualvm.github.io/download.html)[](https://notepad.onghu.com/2021/solve-visualvm-does-not-start-on-windows-openjdk/)

5. **安裝相容的 JDK**
   若 `default-jdk` 仍不相容，請考慮安裝已知與 VisualVM 相容的特定 JDK 版本，例如 OpenJDK 11 或 Oracle JDK 8+：
   ```bash
   sudo apt install openjdk-11-jdk
   ```
   接著按照前述方法更新 `JAVA_HOME` 或使用 `--jdkhome` 選項。[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)

6. **檢查 VisualVM 安裝狀態**
   請確認 VisualVM 是否正確安裝。錯誤訊息顯示您正從 YourKit Java Profiler 目錄（`~/bin/YourKit-JavaProfiler-2025.3/bin`）執行 VisualVM，這並不常見，因為 VisualVM 通常是獨立工具或與 JDK 捆綁發行。請確認 VisualVM 未損毀：
   - 從 `visualvm.github.io/download.html` 下載最新版 VisualVM（例如 2025 年 4 月 22 日發佈的 VisualVM 2.2 支援 JDK 24）。[](https://visualvm.github.io/relnotes.html)[](https://visualvm.github.io/)
   - 解壓縮至新目錄並執行：
     ```bash
     unzip visualvm_22.zip
     cd visualvm_22/bin
     ./visualvm --jdkhome /usr/lib/jvm/java-17-openjdk-amd64
     ```
   請避免覆蓋現有的 VisualVM 安裝，否則可能引發問題。[](https://visualvm.github.io/troubleshooting.html)

7. **檢查多重 Java 安裝**
   多重 Java 版本可能導致衝突。列出所有已安裝的 Java 版本：
   ```bash
   update-alternatives --list java
   ```
   若列出多個版本，請將所需版本設為預設：
   ```bash
   sudo update-alternatives --config java
   ```
   選擇對應相容 JDK 的編號（例如 OpenJDK 11 或 17）。[](https://askubuntu.com/questions/1504020/visualvm-version-of-openjdk-is-not-supported)

8. **確認 VisualVM 依賴項目**
   VisualVM 需要 `libnb-platform18-java` 與 `libvisualvm-jni`。請確保已安裝這些套件：
   ```bash
   sudo apt install libnb-platform18-java libvisualvm-jni
   ```
   若您透過 `apt` 安裝 VisualVM，此步驟尤其重要。[](https://askubuntu.com/questions/1504020/visualvm-version-of-openjdk-is-not-supported)

9. **繞過 OpenJDK 限制（可選）**
   若您使用不受支援的 OpenJDK 建構版本（例如 IcedTea 或 AdoptOpenJDK），分析功能可能受限。可透過加入命令列參數繞過部分限制：
   ```bash
   ./visualvm --jdkhome /usr/lib/jvm/java-17-openjdk-amd64 -J-Dorg.graalvm.visualvm.profiler.SupportAllVMs=true
   ```
   此操作可啟用對不受支援 JVM 的分析功能，但無法保證完全正常運作。[](https://github.com/oracle/visualvm/issues/143)

10. **檢查 YourKit 與 VisualVM 相容性**
    由於您從 YourKit Java Profiler 目錄執行 VisualVM，請確認 YourKit 的環境未造成干擾。YourKit Java Profiler 2025.3 可能捆綁特定 VisualVM 版本或配置。請查閱 YourKit 說明文件或聯絡 `support@yourkit.com` 以確認與您 JDK 的相容性。或者，可嘗試獨立執行 VisualVM（單獨下載）以隔離問題。[](https://www.yourkit.com/changes/)

### 補充說明
- **YourKit 背景**：此錯誤與 YourKit Java Profiler 無直接關聯，但從 YourKit 目錄執行 VisualVM 暗示整合關係。YourKit 支援 Java 7–15 及後續版本的 EAP 建構，因此若需同時使用兩款工具，請確保您的 JDK 與兩者皆相容。[](https://www.yourkit.com/forum/viewtopic.php?t=41723)[](https://www.yourkit.com/forum/viewtopic.php?t=40299)
- **記錄檔案**：檢查 VisualVM 記錄以獲取詳細資訊。記錄通常位於 `~/.visualvm/<version>/var/log`。對於 YourKit，請檢查 `~/.yjp/log/` 中的分析器代理記錄。若問題持續存在，請將記錄傳送至 `support@yourkit.com`。[](https://stackoverflow.com/questions/70211315/java-17-and-yourkit-2021-11)[](https://www.yourkit.com/forum/viewtopic.php?t=40299)
- **替代方案**：若 VisualVM 持續失效，可考慮使用 YourKit 內建的分析工具或其他分析器（例如 JProfiler 或 Async Profiler），這些工具可能與您的環境有更好的相容性。[](https://digma.ai/9-best-java-profilers-to-use-in-2024/)[](https://bell-sw.com/blog/a-guide-to-java-profiling-tools-techniques-best-practices/)

### 若問題仍未解決
若以上方法皆無效，請提供：
- `java -version` 與 `echo $JAVA_HOME` 的輸出結果
- `update-alternatives --list java` 的輸出結果
- 確切的 VisualVM 版本（透過 `visualvm --help` 或下載頁面查詢）
- 您使用的是 YourKit 捆綁版還是獨立安裝的 VisualVM

這些資訊將有助於進一步定位問題。您亦可將問題回報至 VisualVM GitHub 頁面（`https://github.com/oracle/visualvm`）或聯絡 YourKit 技術支援以獲得具體指引。[](https://github.com/oracle/visualvm/issues/558)