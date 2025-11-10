---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 立即安全升級 Open WebUI
translated: true
type: note
---

明白了。以下是安全無虞的 Open WebUI 升級方法。

## 若您使用 `pip` 安裝（您的情況）

```bash
# 1) （推薦）啟用您用於 Open WebUI 的環境
#    例如 conda：
conda activate open-webui
#    或 venv：
# source ~/open-webui-venv/bin/activate

# 2) 升級至最新版本
python3.11 -m pip install -U open-webui

# 3) （可選）若 pip 快取導致問題
python3.11 -m pip cache purge
python3.11 -m pip install --no-cache-dir -U open-webui

# 4) 驗證安裝結果
python3.11 -m pip show open-webui
```

官方文件說明只需執行 `pip install -U open-webui` 即可升級至最新版本。（[Open WebUI][1]）

### 保持資料/設定持久化

啟動伺服器時，可指定資料目錄以確保升級不影響資料：

```bash
# macOS/Linux
DATA_DIR="$HOME/.open-webui" open-webui serve
# Windows (PowerShell)
$env:DATA_DIR="C:\open-webui\data"; open-webui serve
```

此做法符合官方文件指引，設定 `DATA_DIR`（或使用 `uvx … @latest serve` 搭配相同變數）可讓對話記錄與設定獨立於套件安裝。（[Open WebUI][2]）

> 提示：若先前未使用 `DATA_DIR`，請立即開始使用；Open WebUI 後續將持續使用該資料夾。

## 若使用 Docker（供參考）

```bash
# 停止並移除舊容器（資料保存在具名 volume 中）
docker rm -f open-webui

# 拉取最新映像
docker pull ghcr.io/open-webui/open-webui:main

# 使用現有 volume 重新啟動
docker run -d -p 3000:8080 \
  -v open-webui:/app/backend/data \
  --name open-webui \
  ghcr.io/open-webui/open-webui:main
```

此為專案推薦的手動更新流程；您的資料將持續保存在 `open-webui` Docker volume 中。（[Open WebUI][3]）

## 確認「最新版本」狀態

升級前後可從 GitHub Releases 確認最新版本標籤。（[GitHub][4]）

若發生錯誤（例如 Python 版本不符），請確保在 pip 安裝方式中使用 Python 3.11，此為專案明確推薦版本。（[GitHub][5]）

需要我協助檢查當前環境或解讀升級錯誤訊息嗎？請將相關內容貼至此處，我將協助疑難排解。

[1]: https://docs.openwebui.com/getting-started/quick-start/?utm_source=chatgpt.com "️ 快速開始"
[2]: https://docs.openwebui.com/?utm_source=chatgpt.com "Open WebUI：首頁"
[3]: https://docs.openwebui.com/getting-started/updating/?utm_source=chatgpt.com "更新 Open WebUI"
[4]: https://github.com/open-webui/open-webui/releases?utm_source=chatgpt.com "版本發布 · open-webui/open-webui"
[5]: https://github.com/open-webui/open-webui?utm_source=chatgpt.com "open-webui/open-webui：使用者友善的 AI 介面 ..."