---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: Jekyll 構建缺乏自動清理功能
translated: true
type: note
---

Jekyll 本身並沒有 `--replace` 或 `--refresh` 參數。每次執行 `jekyll build` 時，它會將生成的檔案寫入（或覆寫）到你指定的 `--destination` 資料夾，但**不會自動刪除來源中已不存在的舊檔案**。這意味著殘留檔案可能會繼續存在。

若想要乾淨的建置輸出，你需要在執行 `jekyll build` 前自行清空目標目錄。有兩種常見做法：

**1. 在腳本中手動清理**
在呼叫 `jekyll build` 前清除目標目錄：

```python
import shutil

def run_jekyll(destination: str, extra_args: list[str]) -> int:
    # 移除舊檔案
    dest_path = Path(destination)
    if dest_path.exists():
        shutil.rmtree(dest_path)

    command = [
        "jekyll",
        "build",
        "--destination",
        destination,
        *extra_args,
    ]
    completed = subprocess.run(command, check=False)
    return completed.returncode
```

**2. 使用 Jekyll 預設的 `_site` 目錄**
如果你讓 Jekyll 使用專案根目錄下的預設 `_site` 目錄（而非自訂的 `--destination`），則可透過 `jekyll clean` 在重建前清除輸出：

```bash
jekyll clean && jekyll build
```

但需注意 `jekyll clean` 僅識別 `_site` 目錄，不適用於自訂資料夾。

---

總結：

* Jekyll 沒有內建的 `--replace` 參數
* 若使用自訂目標路徑（如你的腳本所示），且需要全新輸出時，應在建置前明確刪除該目錄

需要我為你的腳本添加類似 `jekyll clean` 的 `--clean` 選項，讓它在建置前自動清空目標目錄嗎？