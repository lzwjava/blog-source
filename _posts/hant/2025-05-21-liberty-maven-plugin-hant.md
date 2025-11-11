---
audio: false
generated: true
lang: hant
layout: post
title: Liberty Maven 插件
translated: true
type: note
---

為了在 Windows 系統的 IntelliJ IDEA 中實現快速管理 Liberty 伺服器並構建程式的目標，同時確保在替換 EAR 檔案前停止伺服器，我建議使用 **Liberty Maven Plugin**。這種方法簡單直接，能與您的 Maven 構建流程良好整合，並避免您遇到的指令格式和批次檔問題。

以下是設定步驟：

---

### 解決方案：使用 Liberty Maven Plugin

#### 步驟 1：將 Liberty Maven Plugin 加入您的 `pom.xml`
Liberty Maven Plugin 讓您可以直接透過 Maven 控制 Liberty 伺服器（啟動、停止、部署等），從而無需複雜的指令碼或批次檔。

- 開啟專案的 `pom.xml` 檔案。
- 在 `<build>` 區段內加入以下插件配置：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>io.openliberty.tools</groupId>
            <artifactId>liberty-maven-plugin</artifactId>
            <version>3.3.4</version>
            <configuration>
                <serverName>default</serverName>
                <installDirectory>C:\path\to\liberty</installDirectory>
            </configuration>
        </plugin>
    </plugins>
</build>
```

- **請替換** `C:\path\to\liberty` 為您 Liberty 安裝目錄的實際路徑（例如 `C:\Program Files\IBM\WebSphere\Liberty`）。
- `<serverName>default</serverName>` 與您在 `server start default` 和 `server stop default` 指令中使用的 `default` 相符。

#### 步驟 2：在 IntelliJ IDEA 中建立 Maven 執行配置
您可以配置 IntelliJ IDEA 來執行一系列 Maven 目標，以停止伺服器、構建專案並重新啟動伺服器，而無需使用指令碼或批次檔。

- 在 IntelliJ IDEA 中，前往 **Run > Edit Configurations...**。
- 點擊 **+** 按鈕並從清單中選擇 **Maven**。
- 配置執行設定：
  - **名稱：** 給予一個有意義的名稱，例如 `Run Liberty`。
  - **工作目錄：** 確保設定為您的專案目錄（通常會自動偵測）。
  - **指令列：** 輸入以下 Maven 目標序列：
    ```
    liberty:stop package liberty:start
    ```
- 點擊 **Apply**，然後 **OK**。

#### 步驟 3：執行配置
- 使用 IntelliJ IDEA 中的 **Run** 按鈕（綠色三角形）來執行此配置。
- 這將：
  1. **停止 Liberty 伺服器** (`liberty:stop`)：確保在替換 EAR 檔案時伺服器未運行。
  2. **構建您的專案** (`package`)：執行 `mvn package` 以生成 EAR 檔案。
  3. **啟動 Liberty 伺服器** (`liberty:start`)：使用更新後的 EAR 檔案重新啟動伺服器。

---

### 為何此方案適合您
- **修正指令格式問題：** 您提到在執行配置中使用 "Script text" 會將 `server start default` 拆分為單獨的參數（`server`、`start`、`default`）。Maven 方法透過使用明確定義的插件目標完全避免了此問題。
- **避免批次檔複雜性：** 您發現很難讓 `.bat` 檔案正確工作（例如由於路徑或環境設定）。Liberty Maven Plugin 內部處理伺服器管理，因此您無需除錯批次檔指令或路徑。
- **符合您的需求：** 您需要在替換 EAR 檔案時停止伺服器以避免啟動問題。此解決方案明確在構建前停止伺服器並在之後啟動它，確保了乾淨的流程。

---

### 替代方案：使用批次檔（如果偏好）
如果您仍希望使用批次檔，以下是一個可工作的範例，但由於您遇到的問題，較不推薦：

1. 在您的專案目錄中建立一個名為 `runLiberty.bat` 的檔案，內容如下：

```bat
@echo off
set LIBERTY_BIN=C:\path\to\liberty\bin
set MAVEN_HOME=C:\path\to\maven
set PATH=%PATH%;%LIBERTY_BIN%;%MAVEN_HOME%\bin

"%LIBERTY_BIN%\server" stop default
mvn package
"%LIBERTY_BIN%\server" start default
```

- 將 `C:\path\to\liberty` 和 `C:\path\to\maven` 替換為您 Liberty 和 Maven 安裝的實際路徑。

2. 在 IntelliJ IDEA 中：
   - 前往 **Run > Edit Configurations...**。
   - 點擊 **+** 並選擇 **Batch file**。
   - 將 **Path to batch file** 設定為 `runLiberty.bat` 的位置。
   - 將 **Working directory** 設定為您的專案目錄。
   - 點擊 **Apply** 和 **OK**。

3. 使用 **Run** 按鈕執行。

然而，此方法需要您手動確保路徑和環境變數正確，這正是您覺得困難的地方。Maven 插件方法更簡單可靠。

---

### 建議
使用上述 **Liberty Maven Plugin** 方法。它：
- **整合性強：** 與您現有的 Maven 構建流程緊密結合。
- **簡單易用：** 無需處理批次檔語法或路徑問題。
- **可靠穩定：** 正確處理伺服器的停止和啟動，避免 EAR 替換問題。

此設定將讓您在 IntelliJ IDEA 中快速且一致地在 Liberty 伺服器上運行程式！