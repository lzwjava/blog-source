---
audio: false
generated: true
lang: hant
layout: post
title: 像Python腳本般運行Java
translated: true
type: note
---

若要直接執行 `MultiMark.java` 檔案，類似執行 Python 腳本的方式，您有幾種選擇。由於您使用的是類 Unix 系統（如 `~/projects` 路徑和 `ls` 命令所示），我將提供步驟讓執行 Java 程式盡可能無縫接軌。以下是兩種主要方法：

---

### **選項 1：直接使用 `java` 命令執行 `MultiMark.java`（Java 11+）**
自 Java 11 起，您可以直接執行單一 Java 原始碼檔案，無需先明確編譯，這讓操作體驗更接近執行 Python 腳本。

1. **確保已安裝 Java**
   檢查是否已安裝 Java 11 或更新版本：
   ```bash
   java --version
   ```
   若未安裝 Java 或版本過舊，請安裝相容版本（例如 OpenJDK）：
   ```bash
   sudo apt update
   sudo apt install openjdk-17-jdk
   ```

2. **直接執行 Java 檔案**
   導航至包含 `MultiMark.java` 的目錄：
   ```bash
   cd ~/projects/lzwjava.github.io/scripts/benchmark
   ```
   使用以下指令直接執行 Java 檔案：
   ```bash
   java MultiMark.java
   ```
   此命令會一步完成編譯並執行 `MultiMark.java` 檔案。終端機將顯示輸出結果（例如 CPU 核心數、執行緒數量和時間）。

---

### **選項 2：建立 Shell 腳本方便使用**
若要讓執行 `MultiMark.java` 更像執行 Python 腳本（例如 `./multimark`），您可以建立 Shell 腳本包裝器。

1. **建立 Shell 腳本**
   在 `scripts/benchmark` 目錄中建立名為 `multimark` 的檔案（無副檔名）：
   ```bash
   nano ~/projects/lzwjava.github.io/scripts/benchmark/multimark
   ```
   加入以下內容：
   ```bash
   #!/bin/bash
   java MultiMark.java
   ```
   儲存並離開（在 nano 中使用 `Ctrl+O`、`Enter`、`Ctrl+X`）。

2. **設定腳本為可執行**
   設定執行權限：
   ```bash
   chmod +x multimark
   ```

3. **執行腳本**
   現在您可以像執行 Python 腳本般執行程式：
   ```bash
   ./multimark
   ```
   這將在後台執行 `java MultiMark.java`。

---

### **選項 3：分開編譯與執行（傳統方法）**
若您偏好或需要明確編譯 Java 檔案（例如適用舊版 Java 或檢查編譯錯誤），請遵循以下步驟：

1. **編譯 Java 檔案**
   導航至目錄：
   ```bash
   cd ~/projects/lzwjava.github.io/scripts/benchmark
   ```
   編譯 Java 原始碼檔案：
   ```bash
   javac MultiMark.java
   ```
   這將生成 `MultiMark.class` 檔案。

2. **執行編譯後的程式**
   執行已編譯的類別：
   ```bash
   java MultiMark
   ```
   注意：使用 `MultiMark`（不含 `.java`），因為您正在執行編譯後的類別檔案。

---

### **實現 Python 式操作體驗**
要讓操作體驗最接近執行 Python 腳本，**選項 1**（直接執行 `java MultiMark.java`）最為簡便，因為它跳過了手動編譯步驟。**選項 2**（Shell 腳本）則最理想，若您希望像執行 `./script.py` 般使用單一指令 `./multimark`。

### **注意事項**
- **Java 版本**：此程式碼使用標準 Java 函式庫（`java.util.*` 和 `System.nanoTime`），因此應可在 Java 8 或更新版本運作。直接執行功能（`java MultiMark.java`）需要 Java 11+。
- **效能表現**：`MultiMark.java` 程式會對多執行緒排序進行效能測試。無論直接執行或透過腳本執行，皆不影響其效能表現，但請確保系統具備足夠資源（CPU/記憶體）以應付測試的執行緒數量（最高 64 執行緒）。
- **目錄上下文**：由於您顯示了 `ls scripts/benchmark/`，我假設 `MultiMark.java` 位於該目錄中。若檔案位於其他位置，請調整路徑。
- **錯誤處理**：若遇到錯誤（例如 `java: command not found`），請確保已安裝 Java 並加入 `PATH` 環境變數。若程式執行失敗（例如因記憶體或執行緒限制），請檢查堆疊追蹤以獲取詳細資訊。

若您希望將此程式整合至 Python 腳本工作流程（`executormark.py`、`multimark.py`、`threadmark.py`），請告知，我可建議整合方式（例如從 Python 呼叫 Java 程式）。