---
audio: false
generated: true
lang: hant
layout: post
title: 使用UF2檔案為Flash Pico進行燒錄
translated: true
type: note
---

要將 `RPI_PICO-20250415-v1.25.0.uf2` 檔案燒錄至掛載在 `/media/lzw/RPI-RP2` 的 Raspberry Pi Pico，請使用以下指令：

```bash
cp ~/Downloads/RPI_PICO-20250415-v1.25.0.uf2 /media/lzw/RPI-RP2/
```

### 說明
- `cp`：複製檔案
- `~/Downloads/RPI_PICO-20250415-v1.25.0.uf2`：Downloads 目錄中 `.uf2` 檔案的路徑
- `/media/lzw/RPI-RP2/`：Pico 裝置 `RPI-RP2` 驅動器的掛載點，如輸出所示

### 執行指令後
- `.uf2` 檔案將被複製到 Pico，裝置會自動燒錄韌體
- 燒錄完成後，`RPI-RP2` 驅動器會解除掛載（消失），表示燒錄成功
- 若驅動器重新出現，可能表示燒錄失敗。請確認 `.uf2` 檔案有效，或嘗試更換 USB 線材/連接埠

如遇到問題或需要進一步協助，請告訴我！