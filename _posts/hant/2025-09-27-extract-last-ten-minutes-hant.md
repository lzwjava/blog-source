---
audio: false
generated: true
image: false
lang: hant
layout: post
model: google/gemini-2.5-flash
title: 提取最後十分鐘音頻
translated: true
type: note
---

要擷取音訊檔案 `lobby-zh.ogg` 的最後 10 分鐘內容，你需要使用以下資訊：

1.  **總時長：** 輸入檔案的時長為 `00:33:34.40`。
2.  **所需片段長度：** 10 分鐘（即 600 秒）。
3.  **開始時間計算：** 你需要計算檔案結束前 10 分鐘的時間點。

### 計算方式

*   總時長（秒）：
    $$(33 \times 60) + 34.40 = 1980 + 34.40 = 2014.40 \text{ 秒}$$
*   開始時間（秒）：
    $$2014.40 \text{ 秒} - 600 \text{ 秒} = 1414.40 \text{ 秒}$$

以 `HH:MM:SS.sss` 格式表示：
$$1414.40 \text{ 秒} = 23 \text{ 分鐘 } 34.40 \text{ 秒} \quad (1414.40 / 60 = 23.5733\dots)$$
$$\text{開始時間} = 00:23:34.40$$

### FFmpeg 指令

你將使用 `-ss`（跳轉至指定位置）輸入選項，並結合 `-t`（時長）選項。

1.  `-ss 00:23:34.40`：設定擷取的起始位置。
2.  `-t 00:10:00`：設定輸出片段的時長為正好 10 分鐘。

```bash
ffmpeg -i lobby-zh.ogg -ss 00:23:34.40 -t 00:10:00 last_10_minutes.ogg
```

**注意：** 若希望輸出檔案使用原始位元率/編解碼器設定，可加入 `-c copy` 以加速處理：

```bash
ffmpeg -i lobby-zh.ogg -ss 00:23:34.40 -t 00:10:00 -c copy last_10_minutes_copy.ogg
```