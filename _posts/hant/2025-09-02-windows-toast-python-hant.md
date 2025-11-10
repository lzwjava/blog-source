---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 使用 Python 實現 Windows 彈出通知
translated: true
type: note
---

### 什麼是 win10toast？
win10toast 是一個輕量級的 Python 函式庫，可讓您從 Python 腳本發送 Windows 10 的 Toast 通知（彈出式提示）。它適用於桌面應用程式或腳本中的用戶通知，類似於原生的 Windows Toast。

### 先決條件
- 已安裝 Python 3.x
- Windows 10（它依賴於 Windows 特定的 API）
- 除了 Python 之外，無需其他依賴項

### 安裝
透過 pip（Python 套件安裝工具）安裝此函式庫：

```
pip install win10toast
```

如果您使用虛擬環境，請先啟動它。

### 基本用法
1. 導入模組：
   ```python
   from win10toast import ToastNotifier
   ```

2. 建立一個 `ToastNotifier` 實例並呼叫其 `show_toast` 方法來顯示通知：
   ```python
   toaster = ToastNotifier()
   toaster.show_toast("標題", "訊息", icon_path=None, duration=5)
   ```
   - **標題**：通知標題的字串
   - **訊息**：通知內文的字串
   - **icon_path**：可選的 .ico 或 .png 檔案路徑，用於通知圖示（例如 `"path/to/icon.ico"`）。省略則無圖示
   - **duration**：Toast 顯示的時間（秒），預設為 5；Windows 可能會覆蓋此設定

通知將出現在操作中心並作為彈出式視窗顯示。

### 進階用法
- **自訂圖示**：使用圖片檔案（建議 128x128 像素以獲得最佳品質）
- **處理點擊事件**：傳遞回呼函數（支援有限；主要用於基本點擊行為）
- **多個通知**：實例化 `ToastNotifier` 一次並重複使用以發送多個 Toast
- **錯誤處理**：使用 try-except 包裝以處理潛在的 Windows API 問題，例如通知被禁用時

帶有圖示和錯誤處理的範例：
```python
from win10toast import ToastNotifier
import os

try:
    toaster = ToastNotifier()
    icon = "C:\\path\\to\\icon.ico"  # 替換為實際路徑
    toaster.show_toast("警報！", "您的腳本已完成。", icon_path=icon, duration=10)
except Exception as e:
    print(f"通知失敗：{e}")
```

### 限制與提示
- 通知需要啟用 Windows 10 的操作中心（設定 > 系統 > 通知與動作）
- 對於更複雜的功能（例如操作或圖片），請考慮使用替代方案，如 plyer 或 winrt（現代 Windows SDK 的一部分）
- 如果通知未顯示，請檢查 Windows 的專注輔助設定或嘗試以管理員身份執行腳本

完整文件請查閱 [win10toast GitHub 儲存庫](https://github.com/Charnelx/win10toast)。如果您遇到問題，請提供錯誤詳情以獲得針對性的幫助。