---
audio: false
generated: true
lang: hant
layout: post
title: 在 macOS 上升級至 OpenJDK 21
translated: true
type: note
---

由於您目前已在 macOS 系統上透過 Homebrew 安裝了 OpenJDK 17，以下是在 2025 年 7 月 1 日當下安裝最新長期支援（LTS）版本 OpenJDK 21 的簡明指南。您可以將 OpenJDK 21 與 OpenJDK 17 並存安裝，並根據需要切換使用。最簡便的方法是使用 Homebrew，但我也會提供手動安裝選項。

### 方法一：使用 Homebrew 安裝 OpenJDK 21（推薦）
您的系統已安裝 Homebrew（從您當前的 Java 版本可知），這是最簡單且易於維護的方式。

1. **更新 Homebrew**：
   確保 Homebrew 為最新狀態以獲取最新套件：
   ```bash
   brew update
   ```

2. **安裝 OpenJDK 21**：
   Homebrew 提供專用的 OpenJDK 21 配方。執行以下指令：
   ```bash
   brew install openjdk@21
   ```
   此操作會以 keg-only 方式安裝 OpenJDK 21，意味著它不會被符號連結到 `/usr/local/bin` 以避免與其他 Java 版本衝突。

3. **將 OpenJDK 21 加入路徑**：
   要使用 OpenJDK 21，您需要將其加入系統 PATH。安裝後 Homebrew 會提供指示，通常可臨時或永久連結：
   - **臨時（當前工作階段）**：
     ```bash
     export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"
     ```
   - **永久（加入 shell 設定檔）**：
     開啟您的 shell 設定檔（預設應為 `~/.zshrc`，因 macOS 預設使用 Zsh）：
     ```bash
     nano ~/.zshrc
     ```
     加入以下行：
     ```bash
     export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"
     ```
     儲存並關閉檔案，然後套用變更：
     ```bash
     source ~/.zshrc
     ```

4. **設定 JAVA_HOME**：
   為確保 Java 應用程式能定位 OpenJDK 21，請設定 `JAVA_HOME` 環境變數：
   ```bash
   export JAVA_HOME=$(/usr/libexec/java_home -v 21)
   ```
   要永久生效，請將此加入 `~/.zshrc`：
   ```bash
   echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 21)' >> ~/.zshrc
   source ~/.zshrc
   ```

5. **驗證安裝**：
   檢查 OpenJDK 21 是否已安裝並啟用：
   ```bash
   java -version
   ```
   您應看到類似輸出：
   ```
   openjdk 21.0.1 2023-10-17
   OpenJDK Runtime Environment (build 21.0.1+12)
   OpenJDK 64-Bit Server VM (build 21.0.1+12, mixed mode, sharing)
   ```

6. **切換 Java 版本**：
   由於您已安裝 OpenJDK 17，可使用 `/usr/libexec/java_home` 切換版本。例如：
   - 使用 OpenJDK 17：
     ```bash
     export JAVA_HOME=$(/usr/libexec/java_home -v 17)
     ```
   - 使用 OpenJDK 21：
     ```bash
     export JAVA_HOME=$(/usr/libexec/java_home -v 21)
     ```
   或者，可考慮使用版本管理器如 `jenv`（透過 `brew install jenv` 安裝）來簡化切換：
   ```bash
   jenv add /Library/Java/JavaVirtualMachines/openjdk-21.jdk/Contents/Home
   jenv add /Library/Java/JavaVirtualMachines/openjdk-17.jdk/Contents/Home
   jenv enable-plugin export
   jenv global 21
   ```

### 方法二：手動安裝
若您不想使用 Homebrew，可手動安裝 OpenJDK 21。

1. **下載 OpenJDK 21**：
   - 造訪官方 OpenJDK 網站 (jdk.java.net/21) 或可信供應商如 Oracle、Azul 或 Adoptium。
   - 對於 Apple Silicon (M1/M2)，下載 `macOS/AArch64` tar.gz 檔案；對於 Intel 架構 Mac，選擇 `macOS/x64`。
   - 範例：從 Oracle 的 JDK 21 下載頁面，選擇 ARM64 或 x64 tar.gz 檔案。

2. **驗證下載檔案**：
   使用 SHA256 校驗碼檢查下載檔案的完整性：
   ```bash
   shasum -a 256 openjdk-21.0.1_macos-aarch64_bin.tar.gz
   ```
   將輸出與下載頁面提供的校驗碼比對。

3. **解壓縮檔案**：
   將 tar.gz 檔案解壓至目標目錄，例如您的家目錄：
   ```bash
   tar -xf openjdk-21.0.1_macos-aarch64_bin.tar.gz -C ~/OpenJDK
   ```
   JDK 將被解壓至 `~/OpenJDK/jdk-21.0.1.jdk/Contents/Home`。

4. **移至系統目錄**（可選）：
   為保持一致性，可將 JDK 移至標準的 macOS Java 目錄：
   ```bash
   sudo mv ~/OpenJDK/jdk-21.0.1.jdk /Library/Java/JavaVirtualMachines/
   ```

5. **設定 JAVA_HOME 與 PATH**：
   更新您的 `~/.zshrc` 加入：
   ```bash
   export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-21.0.1.jdk/Contents/Home
   export PATH=$JAVA_HOME/bin:$PATH
   ```
   套用變更：
   ```bash
   source ~/.zshrc
   ```

6. **驗證安裝**：
   確認安裝：
   ```bash
   java -version
   ```
   確保顯示為 OpenJDK 21。

### 注意事項
- **Apple Silicon 相容性**：請確保為 M1/M2 Mac 下載 AArch64 版本以避免效能問題。Homebrew 會自動選擇正確架構。
- **多版本 JDK**：macOS 支援在 `/Library/Java/JavaVirtualMachines/` 中安裝多個 JDK。使用 `/usr/libexec/java_home -v <版本>` 切換版本。
- **Homebrew 優勢**：Homebrew 簡化更新流程（`brew upgrade openjdk@21`）並確保系統相容性。
- **替代供應商**：您亦可使用 Azul Zulu 或 Eclipse Temurin 版本的 OpenJDK 21，可從其官方網站（如 azul.com 或 adoptium.net）取得。

若遇到問題，請告知我以協助排查![](https://www.geeksforgeeks.org/how-to-install-openjdk-in-macos/)[](https://formulae.brew.sh/formula/openjdk%4021)[](https://codetrips.com/2023/10/15/installing-java-jdk-21-macos/)