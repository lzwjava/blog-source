---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: PyGetWindow 快速入門指南
translated: true
type: note
---

### 安裝
PyGetWindow 是一個用於操作和查詢多平台（Windows、macOS 和 Linux）視窗的 Python 函式庫。透過 pip 安裝：

```bash
pip install pygetwindow
```

### 導入模組
首先在您的 Python 腳本中導入模組：

```python
import pygetwindow as gw
```

### 取得視窗物件
PyGetWindow 將視窗表示為 `Window` 物件。您可以透過標題、程序或其他屬性來檢索視窗。

- **取得所有視窗物件**：  
  使用 `gw.getAllWindows()` 返回所有開啟視窗的清單。

- **透過標題取得視窗**：  
  使用 `gw.getWindowsWithTitle(title)` 或 `gw.getFirstWindowWithTitle(title)` 進行部分或完全匹配。

- **取得目前使用中的視窗**：  
  使用 `gw.getActiveWindow()` 取得當前焦點所在的視窗。

範例：
```python
windows = gw.getAllWindows()
active = gw.getActiveWindow()
notepad = gw.getWindowsWithTitle('Notepad')  # 包含 'Notepad' 標題的視窗清單
```

### Window 物件的常用方法
一旦您擁有 `Window` 物件，就可以存取屬性和方法，例如：

- **屬性**：`title`、`left`、`top`、`width`、`height`、`isMinimized`、`isMaximized`、`isActive`。
- **方法**： 
  - `activate()`：將視窗移至最前並使其成為使用中狀態。
  - `maximize()` / `minimize()` / `restore()` / `close()`：控制視窗狀態。
  - `resize() / move()`：調整大小和位置。

範例：
```python
if notepad:
    win = notepad[0]
    print(win.title)  # 輸出：例如 'Untitled - Notepad'
    win.activate()
    win.maximize()
    win.move(100, 100)  # 移動至位置 (100, 100)
    win.resize(800, 600)  # 調整大小為 800x600
```

### 處理多平台
- 在 Windows 和 macOS 上，它使用原生 API。
- 在 Linux 上，它依賴 X11 或 Wayland 支援；請確保您的系統已安裝相關套件（例如 Ubuntu 上的 `x11-utils`）。
- 如果某個方法在您的作業系統上不受支援，可能會引發 `NotImplementedError`。

### 範例
以下是一些實用程式碼片段：

1. **列印所有視窗標題**：
   ```python
   for win in gw.getAllWindows():
       print(win.title)
   ```

2. **關閉特定視窗**：
   ```python
   firefox_wins = gw.getWindowsWithTitle('Mozilla Firefox')
   if firefox_wins:
       firefox_wins[0].close()
   ```

3. **移動和調整多個視窗大小**：
   ```python
   windows = gw.getAllWindows()
   for i, win in enumerate(windows[:3]):  # 前 3 個視窗
       win.move(50 * i, 50 * i)
       win.resize(400, 400)
   ```

如需進階用法，請參閱[官方文件](https://pygetwindow.readthedocs.io/)。如果遇到平台特定問題，請檢查系統權限或依賴項，例如 Linux 上的 `xdotool`。