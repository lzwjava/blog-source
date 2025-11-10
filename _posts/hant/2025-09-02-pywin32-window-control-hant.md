---
audio: false
generated: true
image: false
lang: hant
layout: post
title: PyWin32 視窗控制基礎
translated: true
type: note
---

這是一份關於操作 **PyWin32 視窗**的指南——重點介紹其屬性、啟動及底層區域處理方法。

---

## 1. 什麼是 PyWin32 中的視窗？

在 PyWin32 中，「視窗」泛指任何由 Windows API 管理且擁有**控制代碼 (HWND)** 的圖形使用者介面元素。這可以是頂層應用程式視窗、對話方塊，甚至是表單內的控制項。

您通常透過以下方式與視窗互動：

* `win32gui` – 用於視窗控制代碼、屬性和訊息的低階函式。
* `win32con` – 用於 Windows 訊息和樣式的常數。
* `win32api` – 通用的 Windows API 函式。

---

## 2. 常見視窗屬性

視窗有許多可供查詢或修改的屬性：

* **控制代碼 (HWND)**：視窗的唯一識別碼。
* **標題**：顯示在標題列的文字 (`win32gui.GetWindowText(hwnd)`)。
* **類別名稱**：視窗的註冊類別 (`win32gui.GetClassName(hwnd)`)。
* **樣式**：定義視窗的行為與外觀 (使用 `GWL_STYLE` 的 `GetWindowLong`)。
* **位置與大小**：透過 `GetWindowRect(hwnd)` 或 `MoveWindow` 取得的矩形座標。
* **可見性**：視窗是否顯示 (`IsWindowVisible`)。
* **啟用狀態**：是否接受輸入 (`IsWindowEnabled`)。
* **父視窗/擁有者**：視窗的階層關係 (`GetParent(hwnd)`)。

---

## 3. 視窗啟動

要將視窗帶到前景或使其成為活動視窗：

* **SetForegroundWindow(hwnd)** – 使視窗成為活動視窗。
* **SetActiveWindow(hwnd)** – 啟動視窗但不保證置頂。
* **BringWindowToTop(hwnd)** – 將其提升至其他視窗之上。
* **ShowWindow(hwnd, flag)** – 根據 `flag` 參數顯示/隱藏/最小化/最大化視窗（例如 `SW_SHOW`、`SW_MINIMIZE`、`SW_RESTORE`）。

---

## 4. 「底層區域」（Z 軸順序與放置）

視窗以 Z 軸順序層疊排列：

* **頂層** – 始終位於其他視窗之上（使用 `SetWindowPos` 並搭配 `HWND_TOPMOST`）。
* **底層** – 可使用 `SetWindowPos(hwnd, win32con.HWND_BOTTOM, …)` 將視窗推至所有其他視窗之後。
* **非啟動** – 您可以在不啟動視窗的情況下顯示或定位視窗（使用如 `SWP_NOACTIVATE` 的旗標）。

這在您希望背景工具視窗保持開啟但不搶奪焦點時非常實用。

---

## 5. 您將使用的典型函式

以下是一些關鍵的 PyWin32 函式及範例：

```python
import win32gui
import win32con

# 透過標題尋找視窗
hwnd = win32gui.FindWindow(None, "Untitled - Notepad")

# 取得屬性
title = win32gui.GetWindowText(hwnd)
rect = win32gui.GetWindowRect(hwnd)  # (left, top, right, bottom)

# 啟動視窗
win32gui.SetForegroundWindow(hwnd)

# 移至底層（置於其他視窗之後）
win32gui.SetWindowPos(hwnd, win32con.HWND_BOTTOM, 0, 0, 0, 0,
                      win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

# 顯示/還原視窗
win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
```

---

## 6. 事件/訊息處理

您也可以透過以下方式掛鉤視窗事件（啟動、調整大小、關閉）：

* 使用 `SetWindowLong` 進行子類別化。
* 使用 `SendMessage` / `PostMessage` 模擬操作。
* 處理如 `WM_ACTIVATE`、`WM_SIZE` 等訊息。

---

✅ 總結：

* **屬性**：標題、類別、大小、樣式、可見性、啟用狀態。
* **啟動**：使用 `SetForegroundWindow`、`BringWindowToTop`。
* **底層區域**：使用 `SetWindowPos` 和 `HWND_BOTTOM` 管理 Z 軸順序。

您是否需要我提供一個**實用腳本**，該腳本能列出所有頂層視窗及其屬性（標題、位置、Z 軸順序），並允許您互動式地啟動或將其傳送至底層？