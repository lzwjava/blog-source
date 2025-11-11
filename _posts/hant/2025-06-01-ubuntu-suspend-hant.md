---
audio: false
generated: true
lang: hant
layout: post
title: Ubuntu 休眠指南
translated: true
type: note
---

在 Ubuntu 系統中，您可以透過多種方式讓系統進入睡眠或休眠模式：

## 圖形介面方法：
- **右上角**：點擊頂部面板的電源/設定圖示，然後選擇「暫停」（睡眠）或「休眠」（如果可用）
- **活動選單**：按下 Super 鍵，輸入「power」或「suspend」，然後選擇電源選項

## 指令行方法：
```bash
# 進入暫停（睡眠）模式
systemctl suspend

# 進入休眠模式
systemctl hibernate

# 進入混合睡眠模式（結合兩種模式）
systemctl hybrid-sleep
```

## 鍵盤快捷鍵：
- 多數 Ubuntu 系統預設使用 **Fn + Sleep 鍵** 或 **Ctrl + Alt + End**
- 您可以在「設定 > 鍵盤 > 快捷鍵」中自訂這些設定

## 重要注意事項：
- **睡眠/暫停模式**：保持記憶體供電，喚醒速度快但會消耗部分電池電量
- **休眠模式**：將所有資料儲存到硬碟後關機，喚醒速度較慢但完全不消耗電力
- 由於可能與某些硬體存在相容性問題，較新版本的 Ubuntu 可能預設未啟用休眠功能

若休眠功能無法運作，您可能需要先配置交換空間並編輯系統設定來啟用該功能。睡眠/暫停模式在多數系統上應可直接使用。