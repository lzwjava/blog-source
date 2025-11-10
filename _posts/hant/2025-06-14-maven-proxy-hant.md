---
audio: false
generated: true
lang: hant
layout: post
title: Maven 代理設定
translated: true
type: note
---

根據你的 `checkproxy` 指令輸出，你的 HTTP 和 HTTPS 代理均設定為 `http://127.0.0.1:7890`。以下是更新後的 Maven `settings.xml` 配置片段，用於設定 Maven 使用這些代理設定。

### 更新後的 `settings.xml` 代理配置片段

在你的 Maven `settings.xml` 檔案（位於 `~/.m2/settings.xml` 或 `/usr/share/maven/conf/settings.xml`）中，新增或更新 `<proxies>` 區段為以下內容：

```xml
<settings>
  <proxies>
    <proxy>
      <id>http-proxy</id>
      <active>true</active>
      <protocol>http</protocol>
      <host>127.0.0.1</host>
      <port>7890</port>
      <nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>
    </proxy>
    <proxy>
      <id>https-proxy</id>
      <active>true</active>
      <protocol>https</protocol>
      <host>127.0.0.1</host>
      <port>7890</port>
      <nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>
    </proxy>
  </proxies>
</settings>
```

### 片段說明
- **`<id>`**：每個代理設定的唯一識別符（`http-proxy` 和 `https-proxy`）。
- **`<active>true</active>`**：啟用代理。
- **`<protocol>`**：HTTP 代理設定為 `http`，HTTPS 代理設定為 `https`，與你的 `checkproxy` 輸出相符。
- **`<host>127.0.0.1</host>`**：代理伺服器的 IP 地址，如你的代理設定所示。
- **`<port>7890</port>`**：兩個代理的端口號，如指定所示。
- **`<nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>`**：排除 `localhost` 和 `127.0.0.1` 不使用代理，這是避免本地服務問題的標準做法。
- **沒有 `<username>` 或 `<password>`**：由於你的代理輸出未顯示需要驗證，因此省略這些欄位。如果需要驗證，請新增你的憑證。

### 應用步驟
1. **開啟 `settings.xml`**：
   - 如果 `~/.m2/settings.xml` 存在，請編輯它（例如 `nano ~/.m2/settings.xml`）。
   - 如果不存在，請建立它或編輯全域檔案 `/usr/share/maven/conf/settings.xml`（需要 `sudo`）。

2. **插入或更新 `<proxies>` 區段**：
   - 如果 `<proxies>` 已存在，請使用上面的片段替換或合併 `<proxy>` 項目。
   - 如果 `<settings>` 是空的或內容很少，你可以將整個片段用作檔案的內容。

3. **儲存並關閉**檔案。

### 驗證配置
執行一個需要網路連線的 Maven 指令來確認代理是否生效：
```bash
cd ~/Projects/blog-server
mvn -X clean checkstyle:check
```

在除錯輸出（`-X`）中，尋找顯示 Maven 正在使用代理的行（例如連線到 `127.0.0.1:7890`）。如果指令成功下載依賴或完成而沒有網路錯誤，則代理運作正常。

### 疑難排解
- **代理無法運作**：
  - 確保 `127.0.0.1:7890` 上的代理伺服器正在執行（例如使用 `curl -x http://127.0.0.1:7890 https://repo.maven.apache.org` 測試）。
  - 檢查 `settings.xml` 檔案是否有拼寫錯誤。
- **設定檔案被忽略**：
  - 透過檢查除錯輸出中的檔案路徑，確認 Maven 正在讀取 `~/.m2/settings.xml`。
  - 如果使用全域檔案，請確保你正確編輯了 `/usr/share/maven/conf/settings.xml`。
- **需要驗證**：
  - 如果你的代理需要使用者名稱和密碼，請在每個 `<proxy>` 區塊中新增：
    ```xml
    <username>你的使用者名稱</username>
    <password>你的密碼</password>
    ```

### 關於先前內容的說明
你在 `blog-server` 專案中遇到的 `checkstyle:check` 問題（與 `checks.xml` 和 `SuppressWithNearbyTextFilter` 相關）應透過單獨更新 `pom.xml` 來解決，如先前建議（使用 `maven-checkstyle-plugin:3.3.1` 搭配 Checkstyle `10.17.0` 和 `<configLocation>${project.basedir}/checks.xml</configLocation>`）。上述代理設定將確保 Maven 能夠下載該修復所需的任何工件。

如果你遇到問題或需要有關更新 `pom.xml` 或進一步代理除錯的幫助，請告訴我！