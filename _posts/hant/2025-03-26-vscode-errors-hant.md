---
audio: false
generated: true
lang: hant
layout: post
title: 在 VSCode 中隱藏專案的錯誤紅線
translated: true
type: note
---

對於先前的誤解，我深感抱歉。看來我之前的方法未能正確解決您希望在 Visual Studio Code (VSCode) 中針對使用 Gradle 的 Java Spring 專案停用錯誤指示器（紅色底線）的需求，特別是針對「找不到符號」的錯誤。讓我提供修正後的完整解決方案，以有效隱藏這些錯誤指示器。

由於您希望停用編輯器中的紅色底線，且錯誤與 Java 相關（可能由 VSCode 中的 Java 語言伺服器偵測到），我將專注於直接控制錯誤顯示的解決方案，而不依賴可能不適用的假設。以下是實現此目標的步驟：

---

### **解決方案 1：調整工作區設定中的 Java 錯誤嚴重性等級**
「找不到符號」錯誤通常源自於類別路徑問題或未解析的參考，這些問題會被 VSCode 中的 Java Extension Pack 標記為紅色底線。您可以設定 Java 擴充功能來忽略這些特定錯誤。

1. **開啟工作區設定：**
   - 在您的專案資料夾中，導覽至 `.vscode` 目錄。如果該目錄不存在，請建立它。
   - 在 `.vscode` 內，開啟或建立一個名為 `settings.json` 的檔案。

2. **加入以下設定：**
   ```json
   {
       "java.errors.incompleteClasspath.severity": "ignore"
   }
   ```
   - 此設定告訴 Java 語言伺服器忽略與不完整類別路徑相關的錯誤，這是在 Gradle 專案中導致「找不到符號」問題的常見原因。

3. **重新載入 VSCode：**
   - 儲存 `settings.json` 檔案。
   - 按下 `Ctrl + R` (Windows/Linux) 或 `Cmd + R` (macOS) 重新載入 VSCode，或使用指令選擇區 (`Ctrl + Shift + P` 或 `Cmd + Shift + P`) 並選擇「Developer: Reload Window」。

4. **檢查結果：**
   - 重新載入後，如果「找不到符號」錯誤是由於類別路徑問題所致，紅色底線應該會消失。

---

### **解決方案 2：全域停用 Java 診斷功能（進階）**
如果解決方案 1 未能完全移除紅色底線，或者錯誤源自更廣泛的 Java 語言伺服器診斷功能，您可以停用更多錯誤檢查功能。

1. **編輯工作區設定：**
   - 如上所述，開啟 `.vscode/settings.json`。

2. **加入更廣泛的設定：**
   ```json
   {
       "java.errors.incompleteClasspath.severity": "ignore",
       "java.validate.references": false
   }
   ```
   - `"java.validate.references": false` 設定可能會停用參考驗證，從而可能減少額外的「找不到符號」錯誤。請注意，此設定的可用性取決於您的 Java 擴充功能版本，因此屬於實驗性設定。

3. **重新載入 VSCode：**
   - 如解決方案 1 所述，儲存並重新載入。

---

### **解決方案 3：停用 Java 檔案的所有編輯器診斷功能**
如果上述解決方案效果不彰，您可以完全停用 VSCode 在 Java 檔案中的行內錯誤底線，同時保留其他 Java 功能。

1. **開啟工作區設定：**
   - 前往 `.vscode/settings.json`。

2. **加入以下內容：**
   ```json
   {
       "[java]": {
           "editor.showLinting": false,
           "editor.diagnostics": false
       }
   }
   ```
   - 此設定僅針對 Java 檔案 (`[java]`)，並停用 Linting 和診斷功能，從而移除編輯器中的紅色底線。

3. **重新載入 VSCode：**
   - 儲存並重新載入視窗。

**注意：** 此方法在舊版 VSCode 中可能無法使用，因為 `"editor.diagnostics"` 並非標準設定。如果無效，請繼續進行解決方案 4。

---

### **解決方案 4：停用此工作區的 Java 擴充功能**
若想以更徹底但保證有效的方式移除所有 Java 相關的錯誤指示器：

1. **開啟擴充功能檢視：**
   - 按下 `Ctrl + Shift + X` (Windows/Linux) 或 `Cmd + Shift + X` (macOS)。

2. **找到 "Language Support for Java(TM) by Red Hat"：**
   - 這是提供 Java 支援和錯誤檢查的主要擴充功能。

3. **停用於工作區：**
   - 點擊擴充功能旁的齒輪圖示。
   - 選擇「Disable (Workspace)」。

4. **重新載入 VSCode：**
   - 重新載入視窗以套用變更。

**取捨：** 這會停用所有 Java 功能（例如程式碼自動完成、偵錯），而不僅僅是錯誤指示器。僅在您在此專案中不需要 Java 特定支援時使用此方法。

---

### **推薦方法**
- **從解決方案 1 開始**：這是最精確的方法，針對 Gradle 專案中常見的類別路徑相關錯誤。
- **如有需要，嘗試解決方案 2 或 3**：這些方法提供對診斷功能的更廣泛控制。
- **將解決方案 4 作為最後手段**：僅在您願意放棄所有 Java 功能時使用。

---

### **重要注意事項**
- **隱藏 vs. 修復**：這些解決方案會隱藏紅色底線，但不會解決根本的「找不到符號」問題。對於 Gradle 專案，在終端機中執行 `gradle build` 或 `gradle clean build` 可能透過確保依賴項正確解析來修復根本原因。
- **Spring 特定情境**：由於這是 Java Spring 專案，請確保您的 `build.gradle` 檔案包含所有必要的依賴項（例如 `spring-boot-starter`）。如果建置設定不完整，未解析的符號可能仍然存在，但這些解決方案仍會按照您的要求隱藏指示器。
- **還原變更**：若要復原，請從 `settings.json` 中移除新增的行，或重新啟用擴充功能。

請先嘗試解決方案 1，並讓我知道紅色底線是否仍然存在。如果需要進一步調整答案，我隨時在此提供協助！

---

聽起來您在 VSCode 中仍然看到紅色底線錯誤，特別是「Nullable cannot resolve to a type」，即使已經套用了一些設定。讓我們以清晰且實用的方式逐步解決這個問題。

---

### 為什麼會發生此錯誤
「Nullable cannot resolve to a type」錯誤表示 VSCode 的 Java 語言伺服器在您的專案中找不到 `Nullable` 註解或類別。這可能是由於：
- 專案中缺少依賴項（例如，未包含提供 `Nullable` 的程式庫）。
- 程式碼中的 import 語句不正確或缺失。
- Gradle 或 VSCode 設定問題，導致類別路徑設定不正確。

既然您已經嘗試了一些修復方法，我們將專注於驗證基本要素，然後調整 VSCode 以消除這些紅色底線。

---

### 步驟 1：修正程式碼和依賴項
讓我們確保您的程式碼和專案設定是正確的。

#### **檢查您的 Import 語句**
在您的 Java 檔案中，確保您從正確的套件匯入 `Nullable`。以下是兩個最常見的選項：
- **對於 Spring 專案**：
  ```java
  import org.springframework.lang.Nullable;
  ```
- **對於一般用途**（例如 JSR-305 註解）：
  ```java
  import javax.annotation.Nullable;
  ```

如果您不確定需要哪一個，請檢查您的專案框架或詢問您的團隊。如果完全沒有 import 語句，請加入適當的語句。

#### **在 Gradle 中加入依賴項**
如果 import 正確但錯誤仍然存在，可能是程式庫不在您的專案中。開啟您的 `build.gradle` 檔案並加入必要的依賴項：
- **對於 Spring**（如果您使用 Spring Boot 或 Spring Framework）：
  ```groovy
  implementation 'org.springframework:spring-context:5.3.10'  // 請根據您的專案調整版本
  ```
- **對於 JSR-305**（`javax.annotation.Nullable` 的常見來源）：
  ```groovy
  implementation 'com.google.code.findbugs:jsr305:3.0.2'
  ```

加入依賴項後：
1. 在 VSCode 中開啟終端機。
2. 執行：
   ```
   gradle clean build
   ```
   這可確保 Gradle 下載依賴項並更新專案的類別路徑。
3. 重新載入 VSCode：
   - 按下 `Ctrl + Shift + P`（或在 Mac 上按 `Cmd + Shift + P`）。
   - 輸入「Developer: Reload Window」並選擇它。

---

### 步驟 2：減少 VSCode 中的錯誤指示器
如果修正程式碼和依賴項後紅色底線仍然出現，可能是 VSCode 設定問題。讓我們調整一些設定。

#### **忽略類別路徑錯誤**
有時，即使建置正常運作，VSCode 仍會因不完整的類別路徑偵測而標記錯誤。將以下內容加入您的 `.vscode/settings.json` 檔案：
1. 開啟該檔案（如果不存在，請在 `.vscode` 資料夾中建立它）。
2. 加入：
   ```json
   {
       "java.errors.incompleteClasspath.severity": "ignore"
   }
   ```
3. 儲存檔案並等待 VSCode 重新整理（或再次重新載入視窗）。

這會告訴 VSCode 停止顯示與類別路徑相關問題（如缺少類型）的紅色底線。

#### **停用過於嚴格的驗證**
如果錯誤仍然顯示，我們可以降低 VSCode 檢查參考的嚴格程度。將以下內容加入 `.vscode/settings.json`：
```json
{
    "java.validate.references": false
}
```
**注意**：此設定是實驗性的，可能無法在所有版本的 Java 擴充功能中運作。如果無效，請跳至下一步。

---

### 步驟 3：在不破壞功能的情況下隱藏紅色底線
如果上述步驟未能完全移除紅色底線，您可以調整 VSCode 的編輯器來隱藏它們，同時保留 Java 功能。

#### **關閉行內診斷**
將以下內容加入 `.vscode/settings.json`：
```json
{
    "editor.inlayHints.enabled": false,
    "editor.codeActionsOnSave": {
        "source.fixAll": false
    }
}
```
這會減少視覺錯誤指示器，而不完全停用 Java 語言伺服器。

#### **Java 專用的編輯器調整**
僅針對 Java 檔案，您可以最小化干擾：
```json
{
    "[java]": {
        "editor.codeLens": false,
        "editor.renderWhitespace": "none"
    }
}
```

---

### 步驟 4：最後手段 – 停用 Java 語言伺服器
如果其他方法都無效，而您只想讓紅色底線消失（即使意味著失去 Java 功能如自動完成），您可以停用此工作區的 Java 擴充功能：
1. 開啟擴充功能檢視 (`Ctrl + Shift + X` 或 `Cmd + Shift + X`)。
2. 找到「Language Support for Java(TM) by Red Hat」。
3. 點擊齒輪圖示並選擇「Disable (Workspace)」。
4. 重新載入 VSCode。

**警告**：這會移除所有 Java 支援，因此僅在您不需要這些功能時使用此方法。

---

### 最終建議
- **先嘗試此方法**：加入正確的 import 和依賴項（步驟 1），然後執行 `gradle clean build` 並重新載入 VSCode。這應該能修復根本原因。
- **如果紅色底線仍然存在**：使用步驟 2 中的 `.vscode/settings.json` 調整來忽略類別路徑錯誤。
- **仍然卡住？**：請告訴我您的 `build.gradle` 內容或您使用的框架，我將進一步量身定制解決方案！

希望這能消除那些煩人的「Nullable cannot resolve to a type」紅色底線！