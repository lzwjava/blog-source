---
audio: false
generated: true
lang: hant
layout: post
title: VisualVM 全面指南：Java 效能分析與監控
translated: true
type: note
---

# VisualVM 完整指南

VisualVM 是一款功能強大的開源 Java 效能分析與監控工具，提供圖形化介面來分析 Java 應用程式的效能。它隨 Java 開發工具包 (JDK) 一起提供，特別適用於診斷效能問題、記憶體洩漏和執行緒相關問題。本指南涵蓋 VisualVM 的功能、設定、使用方法以及為開發人員和系統管理員提供的最佳實踐。

## 目錄
1. [什麼是 VisualVM？](#什麼是-visualvm)
2. [VisualVM 主要功能](#visualvm-主要功能)
3. [系統需求](#系統需求)
4. [安裝 VisualVM](#安裝-visualvm)
5. [啟動 VisualVM](#啟動-visualvm)
6. [連接到 Java 應用程式](#連接到-java-應用程式)
7. [使用 VisualVM 進行監控和分析](#使用-visualvm-進行監控和分析)
   - [概覽標籤頁](#概覽標籤頁)
   - [監視器標籤頁](#監視器標籤頁)
   - [執行緒標籤頁](#執行緒標籤頁)
   - [取樣器](#取樣器)
   - [分析器](#分析器)
   - [堆積傾印分析](#堆積傾印分析)
   - [執行緒傾印分析](#執行緒傾印分析)
   - [MBeans](#mbeans)
8. [遠端監控](#遠端監控)
9. [使用外掛擴展 VisualVM](#使用外掛擴展-visualvm)
10. [最佳實踐](#最佳實踐)
11. [常見問題疑難排解](#常見問題疑難排解)
12. [其他資源](#其他資源)

## 什麼是 VisualVM？

VisualVM 是一款基於 Java 的工具，將多個 JDK 實用程式（如 `jstack`、`jmap` 和 `jconsole`）整合到一個易於使用的單一介面中。它允許開發人員即時監控 Java 應用程式、分析 CPU 和記憶體使用情況、分析堆積傾印以及管理執行緒。VisualVM 對於識別本機和遠端 Java 應用程式中的效能瓶頸、記憶體洩漏和執行緒問題特別有價值。

VisualVM 最初由 Sun Microsystems 開發，現已成為 Oracle JDK 的一部分，並作為開源專案積極維護。它支援在 JDK 6 及更高版本上運行的 Java 應用程式。

## VisualVM 主要功能

- **即時監控**：追蹤 CPU 使用率、記憶體消耗、執行緒活動和垃圾回收。
- **效能分析**：提供 CPU 和記憶體分析，以識別效能瓶頸和記憶體分配模式。
- **堆積傾印分析**：允許檢查記憶體內容以診斷記憶體洩漏。
- **執行緒傾印分析**：幫助分析執行緒狀態並檢測死結。
- **MBean 管理**：提供對 Java 管理擴展 (JMX) 的存取，用於監控和管理應用程式。
- **遠端監控**：支援監控在遠端機器上運行的 Java 應用程式。
- **可擴展性**：支援外掛以擴展功能，例如與特定框架整合或附加分析工具。
- **輕量級且易於使用**：設定簡單，具有直觀的圖形介面。

## 系統需求

使用 VisualVM 需確保以下條件：
- **作業系統**：Windows、macOS、Linux 或任何支援 JVM 的作業系統。
- **Java 版本**：JDK 6 或更高版本（VisualVM 隨 JDK 8 及更高版本捆綁提供）。
- **記憶體**：至少 512 MB 可用 RAM 用於輕量級監控；1 GB 或更多用於堆積傾印分析。
- **磁碟空間**：約 50 MB 用於 VisualVM 安裝。
- **權限**：某些功能可能需要管理員權限（例如，存取系統程序）。

## 安裝 VisualVM

VisualVM 包含在 Oracle JDK 8 及更高版本中，位於 JDK 安裝的 `bin` 目錄中（`jvisualvm` 可執行檔）。或者，您可以將其作為獨立應用程式下載：

1. **從 JDK 安裝**：
   - 如果您安裝了 JDK 8 或更高版本，VisualVM 已存在於 `JAVA_HOME/bin` 目錄中，名為 `jvisualvm`。
   - 運行 `jvisualvm` 可執行檔以啟動工具。

2. **獨立下載**：
   - 訪問 [VisualVM 網站](https://visualvm.github.io/) 下載最新的獨立版本。
   - 將 ZIP 檔案解壓縮到您選擇的目錄。
   - 運行 `visualvm` 可執行檔（例如，Windows 上的 `visualvm.exe`）。

3. **驗證安裝**：
   - 確保 `JRE_HOME` 或 `JAVA_HOME` 環境變數指向相容的 JDK/JRE。
   - 通過啟動 VisualVM 進行測試。

## 啟動 VisualVM

要啟動 VisualVM：
- **在 Windows 上**：雙擊 JDK 的 `bin` 資料夾或獨立安裝目錄中的 `jvisualvm.exe`。
- **在 macOS/Linux 上**：在終端機中運行 `bin` 目錄中的 `./jvisualvm`。
- VisualVM 介面將打開，在左側面板顯示本機 Java 應用程式列表。

## 連接到 Java 應用程式

VisualVM 可以監控本機和遠端 Java 應用程式。

### 本機應用程式
- 啟動後，VisualVM 會自動檢測本機機器上運行的 Java 應用程式。
- 雙擊左側面板中的應用程式以打開其監控儀表板。
- 如果應用程式未列出，請確保它在相容的 JVM 下運行。

### 遠端應用程式
要監控遠端 Java 應用程式：
1. 通過添加 JVM 參數（例如 `-Dcom.sun.management.jmxremote`）在遠端應用程式上啟用 JMX。
2. 在 VisualVM 中，前往 **檔案 > 添加 JMX 連接**。
3. 輸入遠端主機的 IP 地址和端口（例如 `hostname:port`）。
4. 如果啟用了身份驗證，請提供憑據。
5. 連接並監控應用程式。

**注意**：對於安全連接，請根據需要配置 SSL 和身份驗證（參見[遠端監控](#遠端監控)）。

## 使用 VisualVM 進行監控和分析

VisualVM 提供了多個標籤頁和工具來分析 Java 應用程式。以下是每個功能的詳細說明。

### 概覽標籤頁
- 顯示有關應用程式的一般資訊，包括：
  - JVM 參數
  - 系統屬性
  - 應用程式類別路徑
  - PID（程序識別碼）
- 用於驗證應用程式的配置。

### 監視器標籤頁
- 提供即時圖表，用於：
  - **CPU 使用率**：追蹤應用程式和系統 CPU 使用率。
  - **堆積記憶體**：監控堆積使用情況（Eden、Old Gen、PermGen/Metaspace）和垃圾回收活動。
  - **類別**：顯示已載入類別的數量。
  - **執行緒**：顯示存活和後台執行緒的數量。
- 允許手動觸發垃圾回收或堆積傾印。

### 執行緒標籤頁
- 可視化執行緒狀態（運行中、休眠中、等待中等）隨時間的變化。
- 提供執行緒傾印功能以捕獲所有執行緒的當前狀態。
- 有助於識別死結、阻塞的執行緒或過度的執行緒使用。

### 取樣器
- 提供輕量級的 CPU 和記憶體取樣以進行效能分析。
- **CPU 取樣**：
  - 捕獲方法級別的執行時間。
  - 識別消耗最多 CPU 時間的熱點方法。
- **記憶體取樣**：
  - 追蹤物件分配和記憶體使用情況。
  - 幫助識別消耗過多記憶體的物件。
- 取樣比分析器的開銷更低，但提供的資料詳細程度較低。

### 分析器
- 提供深入的 CPU 和記憶體分析。
- **CPU 分析**：
  - 測量方法的執行時間。
  - 在方法級別識別效能瓶頸。
- **記憶體分析**：
  - 追蹤物件分配和引用。
  - 通過識別意外持續存在的物件來幫助檢測記憶體洩漏。
- **注意**：分析比取樣的開銷更高，可能會減慢應用程式速度。

### 堆積傾印分析
- 堆積傾印是應用程式記憶體的快照。
- 要生成堆積傾印：
  1. 前往 **監視器** 標籤頁。
  2. 點擊 **堆積傾印**。
  3. 將傾印儲存為 `.hprof` 檔案或在 VisualVM 中直接分析。
- 功能：
  - 查看類別實例、大小和引用。
  - 識別記憶體使用量高的物件。
  - 通過分析物件保留路徑來檢測記憶體洩漏。
- 使用 **OQL（物件查詢語言）** 控制台進行高級堆積查詢。

### 執行緒傾印分析
- 捕獲特定時刻所有執行緒的狀態。
- 要生成執行緒傾印：
  1. 前往 **執行緒** 標籤頁。
  2. 點擊 **執行緒傾印**。
  3. 在 VisualVM 中分析傾印或將其匯出以供外部工具使用。
- 有助於診斷：
  - 死結
  - 阻塞的執行緒
  - 執行緒競爭問題

### MBeans
- 存取 JMX MBeans 以管理和監控應用程式。
- 功能：
  - 查看和修改 MBean 屬性。
  - 調用 MBean 操作。
  - 監控 MBean 通知。
- 對於具有自定義 JMX 檢測的應用程式非常有用。

## 遠端監控

要監控遠端 Java 應用程式：
1. **配置遠端 JVM**：
   - 將以下 JVM 參數添加到遠端應用程式：
     ```bash
     -Dcom.sun.management.jmxremote
     -Dcom.sun.management.jmxremote.port=<port>
     -Dcom.sun.management.jmxremote.ssl=false
     -Dcom.sun.management.jmxremote.authenticate=false
     ```
   - 對於安全連接，啟用 SSL 和身份驗證：
     ```bash
     -Dcom.sun.management.jmxremote.ssl=true
     -Dcom.sun.management.jmxremote.authenticate=true
     -Dcom.sun.management.jmxremote.password.file=<password_file>
     ```
2. **設定 VisualVM**：
   - 使用遠端主機的 IP 和端口在 VisualVM 中添加 JMX 連接。
   - 如果需要，請提供憑據。
3. **防火牆配置**：
   - 確保 JMX 端口在遠端主機上開放。
   - 如果需要，使用 SSH 隧道進行安全的遠端存取：
     ```bash
     ssh -L <local_port>:<remote_host>:<remote_port> user@remote_host
     ```

## 使用外掛擴展 VisualVM

VisualVM 支援外掛以增強其功能：
1. **安裝外掛**：
   - 前往 **工具 > 外掛**。
   - 在外掛中心瀏覽可用的外掛（例如，Visual GC、BTrace、JConsole 外掛）。
   - 安裝並重新啟動 VisualVM。
2. **熱門外掛**：
   - **Visual GC**：可視化垃圾回收活動。
   - **BTrace**：為 Java 應用程式提供動態追蹤。
   - **JConsole 外掛**：添加 JConsole 相容功能。
3. **自訂外掛**：
   - 從 VisualVM 網站或第三方來源下載外掛。
   - 將外掛檔案放入 `plugins` 目錄並重新啟動 VisualVM。

## 最佳實踐

- **從取樣開始**：在分析之前使用取樣以最小化效能影響。
- **限制分析範圍**：分析特定的套件或類別以減少開銷。
- **定期堆積傾印**：為長時間運行的應用程式安排定期堆積傾印以追蹤記憶體趨勢。
- **監控垃圾回收**：使用 Visual GC 外掛分析 GC 效能。
- **保護遠端連接**：始終對遠端監控使用 SSL 和身份驗證。
- **儲存快照**：儲存堆積和執行緒傾印以供後續分析或協作。
- **使用 OQL 進行高級分析**：學習 OQL 以進行高效的堆積傾印查詢。
- **監控資源使用情況**：確保 VisualVM 有足夠的記憶體用於大型堆積傾印。

## 常見問題疑難排解

- **應用程式未檢測到**：
  - 確保應用程式在相容的 JVM 上運行。
  - 檢查 JVM 是否配置為允許 JMX 連接。
- **分析期間開銷過高**：
  - 切換到取樣以降低開銷。
  - 分析特定的類別或方法。
- **遠端監控連接問題**：
  - 驗證 JMX 端口和防火牆設定。
  - 使用 `telnet <host> <port>` 測試連接性。
- **VisualVM 中的 OutOfMemoryError**：
  - 通過編輯 `visualvm.conf` 檔案增加 VisualVM 的堆積大小：
    ```bash
    -J-Xmx<memory_size>m
    ```
- **堆積傾印分析緩慢**：
  - 使用具有更多 RAM 的機器。
  - 過濾類別以縮小分析範圍。

## 其他資源

- **官方網站**：[visualvm.github.io](https://visualvm.github.io/)
- **文件**：[VisualVM 文件](https://visualvm.github.io/documentation.html)
- **教學**：
  - Oracle 的 [VisualVM 指南](https://www.oracle.com/java/technologies/visualvm.html)
  - [使用 VisualVM 進行 Java 效能調優](https://www.baeldung.com/java-visualvm)
- **社群**：
  - [VisualVM GitHub Issues](https://github.com/visualvm/visualvm.github.io/issues)
  - [Stack Overflow VisualVM 標籤](https://stackoverflow.com/questions/tagged/visualvm)