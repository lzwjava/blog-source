---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 在 macOS 上安裝 Apache Tomcat
translated: true
type: note
---

以下是在 **macOS 上安裝和執行 Apache Tomcat** 的逐步指南：

---

### 1. 檢查 Java

Tomcat 需要 Java。請確認您已安裝：

```bash
java -version
```

如果您沒有看到 Java 版本（例如 `1.8` 或 `11` 或更高版本），請安裝一個。在 macOS 上最簡單的方法是透過 [Homebrew](https://brew.sh)：

```bash
brew install openjdk@11
```

然後連結它：

```bash
brew link --force --overwrite openjdk@11
```

---

### 2. 安裝 Tomcat（選項 A：Homebrew – 最簡單）

使用 Homebrew 可以快速安裝 Tomcat：

```bash
brew install tomcat
```

這通常會安裝最新版本（例如 Tomcat 10）。

您可以在以下位置找到它：

```
/usr/local/Cellar/tomcat/<version>/libexec
```

或者如果使用 Apple Silicon：

```
/opt/homebrew/Cellar/tomcat/<version>/libexec
```

執行它：

```bash
catalina run
```

---

### 3. 安裝 Tomcat（選項 B：手動下載 – 官方方式）

1. 前往 [Apache Tomcat 網站](https://tomcat.apache.org/download-10.cgi) 並下載最新的穩定版本（選擇 `.tar.gz` 檔案）。

2. 將其解壓縮到一個目錄，例如：

   ```bash
   tar xvf apache-tomcat-10.*.tar.gz
   mv apache-tomcat-10.* ~/tomcat
   ```

3. 啟動 Tomcat：

   ```bash
   cd ~/tomcat/bin
   ./startup.sh
   ```

4. 停止它：

   ```bash
   ./shutdown.sh
   ```

---

### 4. 驗證安裝

打開您的瀏覽器並前往：

```
http://localhost:8080
```

您應該會看到 Tomcat 的歡迎頁面。

---

### 5. （可選）添加到 PATH

這樣您就可以從任何地方執行 `startup.sh`，將以下內容添加到您的 `~/.zshrc` 或 `~/.bashrc`：

```bash
export CATALINA_HOME=~/tomcat
export PATH=$CATALINA_HOME/bin:$PATH
```

重新載入：

```bash
source ~/.zshrc
```

---

👉 就是這樣。現在您已經在 macOS 上本地執行了 Tomcat。

您是否希望我在設定完成後，也向您展示 **如何在 macOS 上將 WAR 檔案部署到 Tomcat**？