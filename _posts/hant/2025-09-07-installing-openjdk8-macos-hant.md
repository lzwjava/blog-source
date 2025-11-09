---
audio: false
date: 2025-09-07
generated: true
image: false
lang: hant
layout: post
title: 在 macOS 上安裝 OpenJDK 8
translated: true
type: note
---

以下是如何在 **2025 年**於 macOS 上安裝 **OpenJDK 8**（Java SE 8）的方法，涵蓋了 Homebrew、SDKMAN、手動安裝程式以及 MacPorts。無需表格——只有清晰簡易的流程：

---

## 1. 使用 Homebrew (`openjdk@8`)

這仍然是在 macOS 上安裝 OpenJDK 8 最簡單的方法之一。

### 步驟：

1. 開啟 Terminal。

2. 執行：

   ```bash
   brew install openjdk@8
   ```

   ([Homebrew Formulae][1])

3. 安裝完成後，連結 JDK 以便 macOS 工具能偵測到它：

   ```bash
   sudo ln -sfn $(brew --prefix)/opt/openjdk@8/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-8.jdk
   ```

   ([Homebrew Formulae][1])

4. 可選地，在你的 shell 設定檔（例如 `.zshrc`）中將 OpenJDK 8 加入 PATH：

   ```bash
   export PATH="$(brew --prefix openjdk@8)/bin:$PATH"
   ```

**給 Apple Silicon（M 系列）用戶的注意事項：**
如果你遇到架構問題，可能需要透過 Rosetta 2 執行 Homebrew：

```bash
env /usr/bin/arch -x86_64 /bin/zsh --login
brew install openjdk@8
```

然後繼續進行符號連結和 PATH 設定 ([Stack Overflow][2])。

---

## 2. 透過 SDKMAN（Java 版本管理工具）

SDKMAN 是一個靈活的工具，用於安裝和切換多個 Java 版本。

### 快速安裝：

```bash
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk list java
sdk install java 8.xxx-tem
```

將 `8.xxx-tem` 替換為 `sdk list java` 中顯示的識別碼。([Stack Overflow][2])

---

## 3. 手動安裝（Oracle / Adoptium / AdoptOpenJDK）

### 選項 A：Oracle 的 .dmg / .pkg 安裝程式

1. 從 Oracle 的 Java SE 8 下載頁面下載適合你架構的安裝程式。
2. 開啟 `.dmg`，執行 `.pkg` 安裝程式，並按照提示操作。([Oracle Documentation][3])
3. 安裝完成後，使用如 `java_home` 的工具來選擇版本：

   ```bash
   /usr/libexec/java_home -v 1.8 --exec java -version
   ```

### 選項 B：AdoptOpenJDK 或類似版本

AdoptOpenJDK（現由 Eclipse Adoptium 管理）提供版本——包括安裝程式和封存檔選項。

* 例如，Salesforce 在 2025 年 8 月的文件建議使用 AdoptOpenJDK 網站，選擇 OpenJDK 8（LTS）與 HotSpot JVM，並透過其安裝程式進行安裝。([Salesforce][4])

安裝完成後，設定你的 JAVA\_HOME，例如：

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
export PATH=$JAVA_HOME/bin:$PATH
```

---

## 4. MacPorts

如果你使用 MacPorts 而非 Homebrew，安裝 OpenJDK 8 非常直接：

```bash
sudo port install openjdk8
```

若要查看安裝內容：

```bash
port contents openjdk8
```

之後若要更新：

```bash
sudo port selfupdate && sudo port upgrade openjdk8
```

([MacPorts][5])

---

## 選擇適合你的方法

| 意圖                                               | 最佳方法                                        |
| -------------------------------------------------- | ----------------------------------------------- |
| 快速安裝且易於維護                                 | **Homebrew (`brew install openjdk@8`)**         |
| 管理多個並行的 Java 版本                           | **SDKMAN**                                      |
| 完全控制與官方安裝程式（適合圖形介面使用者）       | **手動 `.dmg` 或 `.pkg`** 透過 Oracle/Adoptium |
| 偏好 MacPorts 生態系統                             | **MacPorts**                                    |

---

## 驗證安裝

安裝完成後，使用以下指令檢查：

```bash
java -version
```

預期會看到類似 `"1.8.0_xxx"` 的輸出，以確認 Java 8 已啟用。若要精確控制：

```bash
/usr/libexec/java_home -v 1.8 --exec javac -version
```

---

## 最後總結

總而言之：

* **Homebrew** 是 2025 年最受歡迎的首選——只需 `brew install openjdk@8`，然後連結並設定 PATH。
* **SDKMAN** 在你需要頻繁切換 Java 版本時提供靈活性。
* **手動安裝程式**（Oracle、Adoptium）仍然是可靠的、基於圖形介面的備選方案。
* **MacPorts** 適用於偏好該套件管理器的用戶。

如果你需要協助設定 shell 環境、切換 Java 版本或任何其他相關事項，請隨時告訴我！

[1]: https://formulae.brew.sh/formula/openjdk%408?utm_source=chatgpt.com "openjdk@8"
[2]: https://stackoverflow.com/questions/24342886/how-to-install-java-8-on-mac?utm_source=chatgpt.com "How to install Java 8 on Mac"
[3]: https://docs.oracle.com/javase/8/docs/technotes/guides/install/mac_jdk.html?utm_source=chatgpt.com "JDK 8 Installation for macOS"
[4]: https://help.salesforce.com/s/articleView?id=001117155&language=en_US&type=1&utm_source=chatgpt.com "How to Install OpenJDK 8 on macOS to Work with Anypoint ..."
[5]: https://ports.macports.org/port/openjdk8/?utm_source=chatgpt.com "Install openjdk8 on macOS with MacPorts"