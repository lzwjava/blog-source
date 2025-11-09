---
audio: false
generated: true
image: false
lang: hant
layout: post
model: anthropic/claude-sonnet-4
title: xdotool X11 除錯指南
translated: true
type: note
---

你所遇到的錯誤顯示 `xdotool` 無法從你的 X 伺服器獲取活動視窗資訊。以下是幾種診斷和獲取更詳細錯誤資訊的方法：

## 1. 檢查 X11 環境
首先，驗證你的顯示環境：
```bash
echo $DISPLAY
echo $XDG_SESSION_TYPE
```

如果你正在使用 Wayland 而非 X11，`xdotool` 將無法正常運作，因為它是專為 X11 設計的。

## 2. 使用詳細模式
嘗試以更詳細的輸出模式執行 xdotool：
```bash
xdotool --help  # 檢查可用選項
```

## 3. 替代除錯指令
嘗試以下指令以收集更多資訊：

```bash
# 檢查 X 伺服器是否可存取
xwininfo -root -tree

# 嘗試較簡單的 xdotool 指令
xdotool search --name ".*" | head -5

# 檢查視窗管理員
wmctrl -l  # 列出所有視窗
wmctrl -d  # 列出桌面

# 直接檢查 X11 屬性
xprop -root _NET_ACTIVE_WINDOW
```

## 4. 檢查 X11 擴充功能
錯誤可能與缺少 X11 擴充功能有關：
```bash
# 檢查可用擴充功能
xdpyinfo | grep -i extension

# 特別檢查所需擴充功能
xdpyinfo | grep -E "(XTEST|Extended-Visual-Information)"
```

## 5. 權限問題
檢查你是否擁有適當權限：
```bash
# 檢查是否可以存取顯示器
xhost +local:
```

## 6. 替代工具
如果 xdotool 持續失敗，嘗試以下替代方案：

```bash
# 適用於 Wayland
if [ "$XDG_SESSION_TYPE" = "wayland" ]; then
    # 使用 wlr-activewindow（如果可用，適用於 Wayland）
    swaymsg -t get_tree | jq '.. | select(.focused?) | .name'
fi

# 適用於 X11 替代方案
xtitle  # 如果已安裝
xprop -root | grep "_NET_ACTIVE_WINDOW(WINDOW)"
```

## 7. 系統資訊
檢查你的系統設定：
```bash
# 檢查桌面環境
echo $DESKTOP_SESSION
ps aux | grep -E "(gnome|kde|xfce|i3|sway)"

# 檢查是否在容器或虛擬機器中執行
systemd-detect-virt
```

最可能的原因包括：
1. **Wayland 工作階段**：xdotool 無法與 Wayland 相容
2. **缺少權限**：X 伺服器存取限制
3. **視窗管理員不相容**：部分視窗管理員不支援 `_NET_ACTIVE_WINDOW`
4. **缺少 X11 擴充功能**：所需擴充功能未載入

請嘗試上述診斷指令，並告知我你獲得的輸出結果，這將有助於準確定位問題所在。