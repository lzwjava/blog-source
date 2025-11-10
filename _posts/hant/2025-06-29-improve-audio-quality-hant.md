---
audio: false
generated: true
lang: hant
layout: post
title: 提升 yt-dlp 音訊品質
translated: true
type: note
---

針對您使用 `yt-dlp` 下載 YouTube 影片時音質未如預期的問題，我將指導您如何修改腳本，確保**無論選擇何種影片解析度（720p 或 480p）都能下載最佳音質**。讓我們逐步分析並提供清晰的解決方案。

### 了解當前腳本
您的腳本使用 `yt-dlp` 下載 YouTube 影片，並允許指定解析度（720p 或 480p）。格式選擇由 `format_str` 變數控制，並傳遞給 `yt-dlp` 的 `-f` 選項。當前設定如下：

- **720p**：`format_str = 'bestvideo[height<=720]+bestaudio/best[height<=720]'`
- **480p**：`format_str = 'bestvideo[height<=480]+bestaudio/best[height<=720]'`

在 `yt-dlp` 中：
- `bestvideo[height<=720]` 選擇高度不超過 720 像素的最佳影片串流。
- `bestaudio` 選擇最佳純音訊串流，通常是位元速率最高的。
- `+` 運算子指示 `yt-dlp` 分別下載影片和音訊串流，並合併為單一檔案。
- `/` 運算子提供後備方案：如果前面的組合（例如 `bestvideo[height<=720]+bestaudio`）不可用，則使用後面的格式（例如 `best[height<=720]`），即不超過 720p 且包含影片和音訊的最佳單一格式。

由於已包含 `bestaudio`，腳本理應選擇最佳可用音質。但您注意到音質「未如理想」，讓我們探究原因及解決方法。

### 音質未如理想的可能原因
即使使用了 `bestaudio`，仍可能存在問題：
- 後備選項（`best[height<=720]`）可能在極少數情況下觸發，即當指定的影片和音訊串流無法合併時。此後備選項會選擇結合影片與音訊的格式，其音質可能較低（例如 128kbps，而非獨立的 256kbps 音訊串流）。
- 對於 480p 的情況，後備設定為 `best[height<=720]` 不一致——當您要求 480p 時，它可能下載 720p 影片，且該結合格式的音質可能非最佳。

由於 YouTube 通常提供獨立的影片和音訊串流，`bestvideo + bestaudio` 組合幾乎總是可行。但為保證最佳音質並避免後備至可能較低音質的結合格式，我們可以優化腳本。

### 解決方案：確保最佳音質
為確保 `yt-dlp` 始終下載最佳音質：
1. **使用 `bestaudio` 且不設後備**：強制 `yt-dlp` 下載最佳可用音訊串流，連同所選解析度的最佳影片串流。若此組合不可行，它將報錯而非妥協音質，這可以接受，因為 YouTube 影片幾乎總有獨立串流。
2. **修正 480p 的後備不一致問題**：若保留後備，應與要求解析度一致，但移除後備更簡單且符合您的目標。

以下是修改腳本的方法：

#### 修改後的程式碼
更新腳本中的 `format_str` 定義如下：

```python
import argparse
import subprocess
import os

def main():
    parser = argparse.ArgumentParser(description="Download YouTube videos at specified resolution.")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument(
        "--resolution",
        choices=["720p", "480p"],
        default="720p",
        help="Video resolution to download (default: 720p)"
    )
    args = parser.parse_args()

    output_dir = "test"
    os.makedirs(output_dir, exist_ok=True)

    # 更新格式字串以確保最佳音質
    if args.resolution == "720p":
        format_str = 'bestvideo[height<=720]+bestaudio'
    else:  # 480p
        format_str = 'bestvideo[height<=480]+bestaudio'

    command = [
        "yt-dlp",
        "--cookies-from-browser", "firefox",
        "-f", format_str,
        "-P", output_dir,
        args.url
    ]

    subprocess.run(command)

if __name__ == "__main__":
    main()
```

#### 修改說明
- **720p**：從 `'bestvideo[height<=720]+bestaudio/best[height<=720]'` 改為 `'bestvideo[height<=720]+bestaudio'`。
- **480p**：從 `'bestvideo[height<=480]+bestaudio/best[height<=720]'` 改為 `'bestvideo[height<=480]+bestaudio'`。
- **移除後備（`/best[height<=...]`）**：確保 `yt-dlp` 始終使用最佳音訊串流（`bestaudio`），而非可能後備至音質較低的結合格式。

### 為何此修改有效
- **`bestaudio`**：選擇最高位元速率的可用音訊串流（例如 160kbps 的 Opus 或 256kbps 的 AAC，視影片而定），確保最佳音質。
- **無後備**：透過移除 `/best[height<=720]`，防止 `yt-dlp` 下載音質較差的結合格式。由於 YouTube 影片通常有獨立串流，`bestvideo + bestaudio` 應總是成功。
- **解析度尊重**：影片解析度維持在您選擇的範圍內（720p 或 480p），同時音質最大化。

### 驗證結果
為確認您獲得最佳音質：
1. **檢查可用格式**：執行 `yt-dlp --list-formats <youtube_url>` 查看特定影片的可用影片和音訊串流。尋找純音訊格式（例如 `m4a`、`webm`）及其位元速率。
2. **監控下載過程**：運行腳本時，`yt-dlp` 將輸出它正在下載的格式（例如「下載影片串流（代碼）」和「下載音訊串流（代碼）」）。確保它選擇了高位元速率的獨立音訊串流。
3. **測試播放**：播放下載的檔案並驗證音質。若仍不理想，可能是影片的最佳可用音質受上傳者限制，非腳本問題。

### 若失敗怎麼辦？
如果 `yt-dlp` 因 `bestvideo[height<=720]+bestaudio` 不可用而報錯（對 YouTube 極不可能），您可以：
- 重新加入後備如 `/best[height<=720]'`，但這可能妥協音質，應避免。
- 使用 `--list-formats` 調查特定影片，並針對該情況調整腳本，但這很少需要。

### 總結
您的腳本現已設定為始終下載最佳可用音質，透過使用 `bestaudio` 且不設後備，並配合您選擇的影片解析度。修改後的 `format_str` 值為：

- 720p：`'bestvideo[height<=720]+bestaudio'`
- 480p：`'bestvideo[height<=480]+bestaudio'`

此修改應解決您的問題，確保在您偏好的解析度範圍內獲得最高音質。若音質仍感不足，可能是影片原始上傳品質所致，超出腳本控制範圍。請嘗試並告知效果！