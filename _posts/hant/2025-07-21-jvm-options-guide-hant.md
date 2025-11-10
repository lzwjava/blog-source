---
audio: false
generated: true
image: false
lang: hant
layout: post
title: JVM 選項分類速查指南
translated: true
type: note
---

在 JVM 領域中，有**許多選項**可供配置，具體取決於 JVM 的實現（HotSpot、OpenJ9、GraalVM 等）及版本。總體而言，JVM 選項可分為以下幾類：

---

## 1. 標準選項

這些是穩定且跨版本的選項，有官方文件記錄並保證可用。例如：

* `-classpath` / `-cp` → 指定類別路徑。
* `-Dproperty=value` → 設定系統屬性。
* `-version` → 顯示 JVM 版本。
* `-Xms` / `-Xmx` → 初始與最大堆積大小。
* `-ea` → 啟用斷言。

---

## 2. 非標準選項 (`-X`)

這些是 JVM 特定的選項，不保證長期穩定。範例（HotSpot）：

* `-Xint` → 僅解釋執行（無 JIT）。
* `-Xcomp` → 首次使用時編譯所有方法。
* `-Xbatch` → 停用背景編譯。
* `-Xss512k` → 設定執行緒堆疊大小。

---

## 3. 進階選項 (`-XX`)

這些選項提供 GC、JIT 及執行時行為的細緻調校。範例：

* `-XX:+UseG1GC` → 啟用 G1 垃圾收集器。
* `-XX:+PrintGCDetails` → 記錄 GC 活動。
* `-XX:MaxMetaspaceSize=256m` → 設定元空間上限。
* `-XX:+HeapDumpOnOutOfMemoryError` → 發生 OOM 時傾印堆積。
* `-XX:+UnlockExperimentalVMOptions` → 允許實驗性旗標。
* `-XX:+UseStringDeduplication` → 透過字串去重複化減少記憶體使用。

---

## 4. 診斷與實驗性選項

部分旗標需解鎖才能使用：

* `-XX:+UnlockDiagnosticVMOptions` → 啟用診斷旗標。
* `-XX:+UnlockExperimentalVMOptions` → 允許實驗性調校。

之後可使用以下選項：

* `-XX:+PrintFlagsFinal` → 列出所有 JVM 選項及其數值。
* `-XX:+LogCompilation` → 記錄 JIT 編譯器活動。

---

## 5. 處理 JVM 選項的工具

* **`java -X`** → 列出當前 JVM 版本的非標準選項。
* **`java -XX:+PrintFlagsFinal`** → 顯示所有已識別選項的預設值與當前數值。
* **`jcmd <pid> VM.flags`** → 顯示運行中行程的 JVM 旗標。
* **`jcmd <pid> VM.uptime`**、`jcmd <pid> VM.system_properties` → 執行時檢視。
* **`jps` + `jinfo`** → 列出 Java 行程並顯示 JVM 選項。
* **VisualVM / JConsole** → 監控堆積、GC 及執行時參數。

---

👉 實用的環境探索方式是執行：

```bash
java -XX:+PrintFlagsFinal | grep GC
```

以查看所有 GC 相關選項，或直接執行：

```bash
java -X
```

以檢查可用的非標準旗標。

---

是否需要我為您提供**最實用 JVM 選項的分類速查表**（GC、記憶體、除錯、效能調校），讓您無需解析冗長的 `PrintFlagsFinal` 清單？