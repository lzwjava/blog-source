---
audio: false
generated: true
lang: hant
layout: post
title: 修正 Java 類別路徑錯誤
translated: true
type: note
---

您遇到的錯誤（`Could not find or load main class scripts.benchmark.MultiMark`）是因為您嘗試從專案根目錄（`~/projects/lzwjava.github.io`）使用完整類別名稱（`scripts.benchmark.MultiMark`）執行 Java 程式，但 Java 執行時期期望從套件結構開始的目錄執行類別，或者您需要正確指定類別路徑。當您切換到 `scripts/benchmark` 目錄並執行 `java MultiMark` 時，它正常運作是因為類別相對於指令處於正確目錄中。

要從專案根目錄（`~/projects/lzwjava.github.io`）執行 `MultiMark.java` 或 `MultiMark.class` 而無需切換目錄，您可以使用 `-cp`（類別路徑）選項搭配 `java` 指令，告訴 Java 在哪裡找到編譯後的類別檔案。以下是兩種實現方法，讓您保持在根目錄：

---

### **選項 1：使用類別路徑執行編譯後的類別**
如果 `MultiMark.class` 已存在於 `scripts/benchmark/` 中（如您的 `ls` 輸出所示），您可以透過指定類別路徑從根目錄執行它。

1. **保持在根目錄**
   確保您位於 `~/projects/lzwjava.github.io`。

2. **執行程式**
   使用 `-cp` 選項指向包含類別檔案的目錄：
   ```bash
   java -cp scripts/benchmark MultiMark
   ```
   - `-cp scripts/benchmark` 告訴 Java 在 `scripts/benchmark` 目錄中尋找類別。
   - `MultiMark` 是類別名稱（無需 `.class` 或套件前綴，因為 `MultiMark.java` 沒有 `package` 宣告）。

   這應該會產生如下輸出：
   ```
   CPU cores: 32
   ...
   ```

3. **注意**：如果 `MultiMark.class` 已過時或遺失，請先從根目錄編譯原始碼檔案：
   ```bash
   javac scripts/benchmark/MultiMark.java
   ```
   然後執行上述指令。

---

### **選項 2：直接使用類別路徑執行原始檔（Java 11+）**
如果您偏好直接執行原始檔（類似 `python script.py`），您可以使用 `java` 指令搭配原始檔路徑，並指定類別路徑。

1. **保持在根目錄**
   確保您位於 `~/projects/lzwjava.github.io`。

2. **執行原始檔**
   使用：
   ```bash
   java -cp scripts/benchmark scripts/benchmark/MultiMark.java
   ```
   - `-cp scripts/benchmark` 將類別路徑設定為包含原始檔的目錄。
   - `scripts/benchmark/MultiMark.java` 指定要編譯和執行的原始檔。

   這會一步完成編譯和執行 `MultiMark.java`，產生與之前相同的輸出。

---

### **選項 3：在根目錄建立 Shell 腳本**
為了更方便（例如從根目錄執行 `./multimark`），您可以在根目錄（`~/projects/lzwjava.github.io`）建立一個 shell 腳本。

1. **建立 Shell 腳本**
   在根目錄建立名為 `multimark` 的檔案：
   ```bash
   nano multimark
   ```
   加入：
   ```bash
   #!/bin/bash
   java -cp scripts/benchmark MultiMark
   ```
   儲存並離開。

2. **使其可執行**
   ```bash
   chmod +x multimark
   ```

3. **執行腳本**
   從根目錄：
   ```bash
   ./multimark
   ```
   這會執行程式而無需切換目錄。

4. **可選：在腳本中編譯**
   如果您希望腳本能處理編譯（例如原始檔變更時），修改腳本：
   ```bash
   #!/bin/bash
   javac scripts/benchmark/MultiMark.java
   java -cp scripts/benchmark MultiMark
   ```

---

### **關鍵注意事項**
- **類別路徑（`-cp`）**：`-cp` 選項告訴 Java 在哪裡尋找類別或原始檔。由於 `MultiMark.java` 沒有 `package` 宣告，類別名稱僅為 `MultiMark`，而非 `scripts.benchmark.MultiMark`。如果它有 `package scripts.benchmark;` 這行，您需要從根目錄使用 `java -cp . scripts.benchmark.MultiMark`。
- **Java 版本**：原始檔執行（`java scripts/benchmark/MultiMark.java`）需要 Java 11 或更新版本。您的系統似乎已安裝 Java，因為從 `scripts/benchmark` 目錄執行時正常運作。
- **目錄**：這些解決方案讓您保持在根目錄（`~/projects/lzwjava.github.io`），符合您的偏好。
- **自動化**：Shell 腳本（選項 3）最接近 Python 的使用體驗，因為您可以像執行 Python 腳本一樣執行 `./multimark`。您也可以將其加入 `PATH` 以便全域存取，但這是可選的。
- **錯誤處理**：如果遇到 `NoClassDefFoundError` 等錯誤，請確保 `MultiMark.class` 存在於 `scripts/benchmark/` 中或重新編譯。如果找不到 Java，請驗證安裝（`java --version`）。

如果您希望將此與 Python 腳本整合或需要特定工作流程（例如同時執行 `multimark.py` 和 `MultiMark.java`），請告訴我！