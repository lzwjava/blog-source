---
audio: false
generated: true
lang: hant
layout: post
title: Git 提交前執行 Maven 編譯
translated: true
type: note
---

是的，你可以在執行 `git commit` 前，先在本地的 Git 儲存庫中運行 `mvn compile`。以下是簡要說明與步驟：

1. **確保 Maven 已安裝**：確認系統已安裝並配置好 Maven（可執行 `mvn -version` 驗證）。

2. **導航至 Git 儲存庫**：使用 `cd 路徑/至/你的/儲存庫` 進入包含 Maven 專案（具有 `pom.xml` 檔案）的本地 Git 儲存庫。

3. **執行 Maven 編譯**：運行 `mvn compile` 來編譯你的 Java 程式碼。這將：
   - 編譯 `src/main/java` 中的原始碼
   - 將編譯後的類別檔案置於 `target/classes`
   - 回報任何編譯錯誤

4. **檢查編譯狀態**：
   - 若 `mvn compile` 成功（結尾顯示 `BUILD SUCCESS`），即可繼續進行 Git 操作
   - 若失敗（例如因語法錯誤），請先修正程式碼再提交

5. **Git 工作流程**：
   - 暫存變更：`git add .`（或指定檔案）
   - 提交變更：`git commit -m "你的提交訊息"`

### 可選：使用 Git Hooks 自動化
若要確保每次 `git commit` 前都執行 `mvn compile`，可使用 Git pre-commit hook：
1. 導航至儲存庫中的 `.git/hooks` 目錄
2. 建立或編輯 `pre-commit` 檔案（無副檔名）
3. 加入如下腳本：
   ```bash
   #!/bin/sh
   mvn compile
   if [ $? -ne 0 ]; then
       echo "編譯失敗，提交中止。"
       exit 1
   fi
   ```
4. 設定可執行權限：`chmod +x .git/hooks/pre-commit`
   - 現在唯有當 `mvn compile` 成功時，`git commit` 才會繼續執行

### 注意事項
- **相依性**：請確保 `pom.xml` 配置正確，且相依套件已下載（如有需要可執行 `mvn dependency:resolve`）
- **效能**：每次提交前都運行 `mvn compile` 可確保程式碼品質，但在大型專案中可能降低工作流程速度
- **替代指令**：若需包含測試，請改用 `mvn test` 來編譯並執行單元測試

此方法能確保你的程式碼在提交至 Git 儲存庫前已成功編譯。