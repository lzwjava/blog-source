---
audio: false
generated: true
lang: hant
layout: post
title: 建立 Git 預加入掛鉤替代方案
translated: true
type: note
---

Git 本身沒有內建的 `pre-add` 鉤子，但你可以透過以下幾種方式實現類似功能：

### 1. **Git 別名（推薦做法）**
你可以建立一個 Git 別名，在呼叫 `git add` 前先執行檢查腳本：

```bash
git config --global alias.safe-add '!your-pre-add-script.sh && git add'
```

之後改用 `git safe-add` 指令代替 `git add`。

### 2. **封裝腳本**
在 PATH 路徑中建立名為 `git-pre-add` 的腳本，該腳本會：
1. 執行 pre-add 檢查
2. 檢查通過後才呼叫 `git add`

```bash
#!/bin/bash
# 在此處加入你的 pre-add 驗證邏輯
if [ 某項條件 ]; then
  git add "$@"
else
  echo "Pre-add 檢查失敗"
  exit 1
fi
```

### 3. **使用現有鉤子**
你可以創造性地利用現有鉤子：
- **pre-commit**：雖然此鉤子在 add 之後、commit 之前執行，但你可以在這裡檢查已暫存的檔案
- **prepare-commit-msg**：與 pre-commit 類似但執行時機更早

### 4. **檔案系統監控**
針對進階需求，你可以使用：
- **inotifywait**（Linux）監控工作目錄
- **fswatch**（Mac）實現類似功能

### Pre-Add 檢查腳本範例
以下是一個防止新增含有多餘空白字元檔案的簡單範例：

```bash
#!/bin/bash
# .git/hooks/pre-commit（但可對已暫存檔案生效）

# 檢查空白字元錯誤
if git diff --cached --check; then
  exit 0
else
  echo "在已暫存檔案中發現空白字元錯誤"
  exit 1
fi
```

請記得將所有鉤子腳本設為可執行權限（`chmod +x script.sh`）。

需要我針對你的使用情境詳細說明任何特定做法嗎？