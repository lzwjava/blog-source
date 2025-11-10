---
audio: false
generated: true
image: false
lang: hant
layout: post
title: JMX 遠端代理端口指南
translated: true
type: note
---

**JMX 遠端代理**是 Java 管理擴展（JMX）技術的一部分。它允許管理員或監控工具從 JVM 進程外部（通常透過 TCP/IP）連接到運作中的 Java 應用程式。這通常用於生產環境中 Java 應用程式的監控、診斷和管理。

以下詳細說明：

### 1. 什麼是 JMX 遠端代理

* 它將 JVM 內部狀態（記憶體使用量、執行緒活動、垃圾回收、類別載入等）公開為 *受管 Bean（MBeans）*。
* 它允許您遠端連接（例如透過 **jconsole**、**VisualVM** 或像 Prometheus exporters 這類監控工具）。
* 通常透過 JVM 啟動參數啟用，例如：

  ```bash
  -Dcom.sun.management.jmxremote
  -Dcom.sun.management.jmxremote.port=9091
  -Dcom.sun.management.jmxremote.authenticate=false
  -Dcom.sun.management.jmxremote.ssl=false
  ```
* 啟用後，JVM 會執行一個綁定到指定連接埠的 RMI（遠端方法呼叫）連接器伺服器。

### 2. 關於連接埠 9091

* 數字 **9091** 本身並無特殊意義；它只是一個您為 JMX 連接設定的 TCP 連接埠。
* 管理員通常會選擇 9091（或 9010、9999 等）以方便起見，並避免與標準連接埠衝突。
* 當在 `9091` 上監聽時，JVM 將接受該連接埠上的遠端 JMX 連接。
* 如果未啟用安全保護（`authenticate=false, ssl=false`），任何具有網路存取權限的人都能控制或觀察您的 JVM — 這存在重大的安全風險。

### 3. 典型用途

* 使用 **JConsole** 進行監控：

  ```bash
  jconsole host:9091
  ```
* 與監控系統整合（例如 Prometheus JMX Exporter）。
* 在疑難排解期間進行遠端管理（例如檢查堆積轉儲、執行緒、GC 行為）。

### 4. 安全考量

* 務必透過以下方式保護 JMX 連接埠：

  * 網路防火牆（限制存取）。
  * 身份驗證（`password` 和 `access` 檔案）。
  * 如有需要，啟用 SSL。
* 否則，在 9091 連接埠上不加保護地暴露它，等同於將您 JVM 的遠端 shell 層級控制權交給他人。

---

✅ 總之：**在連接埠 9091 上的 JMX 遠端代理**意味著您的 JVM 正透過 TCP 連接埠 9091 公開一個管理和監控介面，該介面可供 JConsole 或 Prometheus 等工具使用，但必須確保其安全性。

您是否需要我示範啟用密碼身份驗證（而非非安全模式）的**確切 JVM 參數**？