---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 遠程 JMX 端口 9001 指南
translated: true
type: note
---

**JMX 遠端代理**是 Java 管理擴充功能（JMX）的一部分。它讓你能夠遠端監控和管理執行中的 Java 應用程式。當你啟用 JMX 遠端管理時，JVM 會啟動一個代理程式，透過 TCP 連接埠公開 MBean（受管 Bean）。像 **jconsole**、**VisualVM** 或自訂監控軟體等工具，可以連接到該連接埠來檢查記憶體使用情況、執行緒狀態、GC 活動，甚至呼叫操作。

關於 **9001 連接埠**：

* 實際的連接埠號碼取決於應用程式的配置。通常你會看到 9001、9090、9091 等。
* 如果你看到有程式在 `9001` 上監聽，且它是 **JMX 遠端代理**，這表示某個 Java 程序啟動時設定了以下系統屬性：

  ```bash
  -Dcom.sun.management.jmxremote
  -Dcom.sun.management.jmxremote.port=9001
  -Dcom.sun.management.jmxremote.authenticate=false
  -Dcom.sun.management.jmxremote.ssl=false
  ```

這會在連接埠 `9001` 上開啟 JMX，且無需驗證/SSL（通常僅供內部或開發使用，因為若公開暴露會存在安全風險）。

---

### 如何在 Windows 上檢查哪個程式使用 JMX 連接埠 9001

1. 開啟**命令提示字元（以系統管理員身分執行）**。
2. 執行：

   ```cmd
   netstat -ano | findstr :9001
   ```

   這會顯示綁定該連接埠的 PID（程序識別碼）。
3. 要識別程式：

   ```cmd
   tasklist /FI "PID eq <PID>"
   ```

   將 `<PID>` 替換為步驟 2 中的數字。

---

### 如何停止 / 終止它

* 如果你確認這是一個你不想要的 Java 程序，可以用以下指令終止它：

  ```cmd
   taskkill /PID <PID> /F
   ```
* 但如果它是你的應用程式伺服器（如 Tomcat、WebSphere、Spring Boot 應用程式等）的一部分，最好透過其服務/控制台來停止它，而不是直接終止程序，這樣可以讓它正常關閉。

---

👉 你是否還需要我示範如何在 Java 應用程式中**停用 JMX 遠端代理**，讓它完全不開啟 9001 連接埠？