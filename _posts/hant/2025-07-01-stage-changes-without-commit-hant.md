---
audio: false
generated: true
lang: hant
layout: post
title: 預提交掛鉤中的階段變更
translated: true
type: note
---

為了在 pre-commit hook 期間將 `update_notes_link.py` 腳本的更改整合到當前提交中（而非建立獨立提交），你需要修改 hook 以暫存更新後的檔案而不單獨提交。這樣，Python 腳本所做的更改將包含在使用者的提交中。以下提供實現此目的的修訂版 pre-commit hook 腳本。

### 主要變更
- **無獨立提交**：腳本僅暫存更新後的檔案（`git add`），使其包含在使用者的提交中，而不在 hook 中執行 `git commit`。
- **保留使用者提交訊息**：Hook 不會建立新提交，確保使用者的原始提交訊息被使用。
- **錯誤處理**：若 Python 腳本執行失敗，hook 將以非零狀態退出以阻止提交。

### Pre-Commit Hook 腳本

以下是更新後的 pre-commit hook 腳本，它會暫存變更而不建立獨立提交：

```x-shellscript
#!/bin/bash

# 執行 update_notes_link.py 腳本並捕獲其輸出
OUTPUT=$(python scripts/generate/update_notes_link.py 2>&1)
EXIT_CODE=$?

# 檢查 Python 腳本是否成功執行
if [ $EXIT_CODE -ne 0 ]; then
    echo "錯誤：update_notes_link.py 執行失敗，退出碼為 $EXIT_CODE"
    echo "$OUTPUT"
    exit 1
fi

# 檢查特定檔案是否被更新
if echo "$OUTPUT" | grep -q "Updated original/2025-01-11-notes-en.md"; then
    echo "筆記連結已更新，正在為當前提交暫存變更。"

    # 暫存相關檔案
    git add original/2025-01-11-notes-en.md
    git add _posts/en/*.md

    # 驗證檔案是否已暫存
    if ! git diff --cached --quiet; then
        echo "變更已成功暫存。"
    else
        echo "無需暫存的變更。"
    fi
else
    echo "original/2025-01-11-notes-en.md 無更新，未暫存其他檔案。"
fi

# 成功退出以允許提交繼續進行
exit 0
```

### 腳本說明

- **Shebang (`#!/bin/bash`)**：確保腳本在 Bash shell 中執行。
- **執行 Python 腳本**：執行 `python scripts/generate/update_notes_link.py` 並捕獲其輸出和退出碼。
- **錯誤處理**：檢查 Python 腳本的退出碼（`$EXIT_CODE`）。若為非零值，hook 將失敗、顯示錯誤並停止提交。
- **檢查輸出**：使用 `grep` 檢查輸出是否顯示 `original/2025-01-11-notes-en.md` 已被更新。
- **暫存檔案**：對指定檔案（`original/2025-01-11-notes-en.md` 和 `_posts/en/*.md`）執行 `git add`，將其包含在使用者的提交中。
- **無提交操作**：跳過 `git commit`，讓使用者的 `git commit` 指令能以其原始提交訊息包含已暫存的變更。
- **回饋訊息**：顯示訊息告知使用者變更是否已暫存。
- **退出碼**：以 `0` 退出，允許提交繼續進行，除非 Python 腳本執行失敗。

### 設定 Hook

1. **建立 Hook**：
   - 將腳本放置於你的儲存庫中的 `.git/hooks/pre-commit`。

2. **設定可執行權限**：
   ```bash
   chmod +x .git/hooks/pre-commit
   ```

3. **測試 Hook**：
   - 修改檔案或確保 Python 腳本會更新 `original/2025-01-11-notes-en.md`。
   - 執行 `git commit -m "你的提交訊息"`。
   - 透過在提交前檢查 `git diff --cached` 或提交後檢查 `git show`，確認更新後的檔案已包含在提交中。

### 使用 `pre-commit` 框架（可選）

若你偏好使用 `pre-commit` 框架，可以在 `.pre-commit-config.yaml` 檔案中定義相同邏輯。此方法更具可攜性，並允許你指定觸發 hook 的檔案。

1. **安裝 pre-commit**：
   ```bash
   pip install pre-commit
   ```

2. **建立 `.pre-commit-config.yaml`**：

```yaml
repos:
- repo: local
  hooks:
  - id: update-notes-links
    name: Update Notes Links
    entry: bash -c '
      OUTPUT=$(python scripts/generate/update_notes_link.py 2>&1);
      EXIT_CODE=$?;
      if [ $EXIT_CODE -ne 0 ]; then
        echo "Error: update_notes_link.py failed with exit code $EXIT_CODE";
        echo "$OUTPUT";
        exit 1;
      fi;
      if echo "$OUTPUT" | grep -q "Updated original/2025-01-11-notes-en.md"; then
        echo "Notes links updated, staging changes for the current commit.";
        git add original/2025-01-11-notes-en.md;
        git add _posts/en/*.md;
        if ! git diff --cached --quiet; then
          echo "Changes staged successfully.";
        else
          echo "No changes to stage.";
        fi;
      else
        echo "No updates to original/2025-01-11-notes-en.md, no additional files staged.";
      fi'
    language: script
    files: ^(original/2025-01-11-notes-en\.md|_posts/en/.*\.md)$
    stages: [commit]
```

3. **安裝 Hook**：
   ```bash
   pre-commit install
   ```

4. **測試 Hook**：
   - 提交符合 `files` 正則表達式的檔案變更（例如 `original/2025-01-11-notes-en.md` 或 `_posts/en/*.md`）。
   - 確認 hook 執行、在適用情況下暫存變更，並將其包含在你的提交中。

### 與原始 GitHub Actions 的主要差異

- **無獨立提交**：與 GitHub Actions 工作流程會建立新提交不同，此 hook 僅為使用者的當前提交暫存變更。
- **無推送操作**：Hook 不會推送變更，因為 pre-commit hook 在提交完成前於本地端執行。使用者必須手動執行 `git push`。
- **錯誤處理**：Hook 檢查 Python 腳本的退出碼，確保不會無聲失敗。
- **無 Git 使用者設定**：腳本省略了 `git config user.name` 和 `user.email`，因為提交將使用使用者的 Git 設定。

### 注意事項

- **Python 腳本**：確保 `scripts/generate/update_notes_link.py` 存在且可在本地執行。若其依賴環境變數或套件，請確保它們可用。
- **檔案路徑**：確認路徑 `original/2025-01-11-notes-en.md` 和 `_posts/en/*.md` 符合你的儲存庫結構。
- **Hook 失敗**：若 Python 腳本失敗，hook 將阻止提交，確保不會暫存部分更新。
- **測試**：使用 `git commit` 測試，確認變更被暫存並包含在提交中，且未建立額外提交。使用 `git show` 檢查提交內容。

### 驗證

驗證步驟：
1. 修改檔案或確保 Python 腳本更新 `original/2025-01-11-notes-en.md`。
2. 執行 `git commit -m "測試提交"`。
3. 檢查 `git show` 確認更新後的檔案已包含在提交中，且使用你的原始訊息。
4. 確保未建立額外提交（例如無 `chore(notes): Update notes links` 提交）。

若需要進一步調整，例如處理特定錯誤情況或添加更多需暫存的檔案，請告知！