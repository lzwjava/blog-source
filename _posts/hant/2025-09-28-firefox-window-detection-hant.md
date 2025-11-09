---
audio: false
generated: true
image: false
lang: hant
layout: post
model: anthropic/claude-sonnet-4
title: Linux 版 Firefox 視窗偵測工具
translated: true
type: note
---

除了 `xdotool` 之外，在 Linux 上還有幾種替代工具和方法可以獲取有關活動 Firefox 視窗的資訊：

## 替代工具

### 1. **wmctrl**
一個比 xdotool 更穩健的替代方案：
```bash
# 獲取活動視窗
wmctrl -a

# 列出所有視窗及其詳細資訊
wmctrl -l -x

# 專門獲取 Firefox 視窗
wmctrl -l | grep -i firefox
```

### 2. **qdbus**（適用於 KDE/Qt 應用程式）
```bash
# 獲取活動視窗資訊
qdbus org.kde.KWin /KWin activeWindow

# 獲取視窗列表
qdbus org.kde.KWin /KWin windows
```

### 3. **xwininfo**
內建的 X11 工具：
```bash
# 互動式視窗選擇
xwininfo

# 獲取根視窗資訊
xwininfo -root -tree | grep -i firefox

# 獲取活動視窗（需要知道視窗 ID）
xwininfo -id $(xprop -root _NET_ACTIVE_WINDOW | cut -d' ' -f5)
```

### 4. **xprop**
另一個 X11 工具：
```bash
# 獲取活動視窗屬性
xprop -root _NET_ACTIVE_WINDOW

# 獲取視窗類別和標題
xprop -root | grep "_NET_ACTIVE_WINDOW(WINDOW)"
```

## 適用於 Wayland 系統

如果您正在運行 Wayland，X11 工具將無法使用。請嘗試以下替代方案：

### 5. **swaymsg**（適用於 Sway）
```bash
swaymsg -t get_tree | jq -r '.. | select(.focused? == true)'
```

### 6. **hyprctl**（適用於 Hyprland）
```bash
hyprctl activewindow
```

### 7. **gdbus**（GNOME/GTK）
```bash
gdbus call --session --dest org.gnome.Shell --object-path /org/gnome/Shell --method org.gnome.Shell.Eval "global.get_window_actors()"
```

## Python 解決方案

### 8. **使用 Xlib 的 Python**
```python
from Xlib import X, display
from Xlib.error import XError

def get_active_window():
    try:
        d = display.Display()
        root = d.screen().root
        
        # 獲取活動視窗
        active_window = root.get_full_property(
            d.intern_atom('_NET_ACTIVE_WINDOW'), X.AnyPropertyType
        )
        
        if active_window:
            window_id = active_window.value[0]
            window = d.create_resource_object('window', window_id)
            window_name = window.get_wm_name()
            return window_name
    except XError:
        return None

print(get_active_window())
```

### 9. **使用 subprocess 的 Python**
```python
import subprocess

def get_firefox_windows():
    try:
        # 使用 wmctrl
        result = subprocess.run(['wmctrl', '-l'], 
                              capture_output=True, text=True)
        firefox_windows = [line for line in result.stdout.split('\n') 
                          if 'firefox' in line.lower()]
        return firefox_windows
    except FileNotFoundError:
        return "wmctrl not installed"

print(get_firefox_windows())
```

## 疑難排解您的 xdotool 問題

「BadWindow」錯誤通常表示：

1. **權限問題**：嘗試使用不同的權限運行
2. **顯示問題**：檢查 `$DISPLAY` 是否設定正確
3. **Wayland 衝突**：您可能正在使用 Wayland 而不是 X11

要檢查您的顯示伺服器：
```bash
echo $XDG_SESSION_TYPE
loginctl show-session $(loginctl | grep $(whoami) | awk '{print $1}') -p Type
```

## 推薦方法

為了達到最大的兼容性，我建議按以下順序嘗試：

1. **wmctrl** - 在不同的視窗管理器中最可靠
2. **xwininfo + xprop** 組合 - 內建於大多數 X11 安裝中
3. **Python 解決方案** - 最靈活且可編程
4. **桌面環境特定工具**（swaymsg、hyprctl 等）

首先嘗試 `wmctrl -l | grep -i firefox` - 它通常是替代 xdotool 視窗檢測功能最直接的方法。