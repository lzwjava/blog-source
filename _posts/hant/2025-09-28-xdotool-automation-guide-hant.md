---
audio: false
generated: true
image: false
lang: hant
layout: post
model: anthropic/claude-sonnet-4
title: xdotool 命令行自動化指南
translated: true
type: note
---

## 什麼是 xdotool？

xdotool 是一個針對 X11（Linux 桌面環境）的命令列自動化工具，可讓您：
- 控制滑鼠移動和點擊
- 向應用程式發送按鍵輸入
- 操作視窗（移動、調整大小、聚焦）
- 根據各種條件搜尋視窗
- 以程式化方式自動化桌面互動

## 安裝

```bash
# Ubuntu/Debian
sudo apt install xdotool

# Fedora/RHEL/CentOS
sudo dnf install xdotool

# Arch Linux
sudo pacman -S xdotool

# 從原始碼安裝
git clone https://github.com/jordansissel/xdotool
cd xdotool
make
sudo make install
```

## 核心指令

### 視窗資訊指令

#### `getactivewindow`
取得目前使用中/聚焦視窗的視窗 ID。
```bash
xdotool getactivewindow
# 輸出：52428807 (視窗 ID)

# 取得使用中視窗的標題
xdotool getactivewindow getwindowname
```

#### `getwindowfocus`
與 getactivewindow 類似，但在某些視窗管理員中行為可能不同。
```bash
xdotool getwindowfocus
```

#### `getwindowname`
取得視窗的標題/名稱。
```bash
# 取得使用中視窗的名稱
xdotool getactivewindow getwindowname

# 取得特定視窗 ID 的名稱
xdotool getwindowname 52428807
```

#### `getwindowpid`
取得與視窗關聯的行程 ID (PID)。
```bash
xdotool getactivewindow getwindowpid
```

#### `getwindowgeometry`
取得視窗的位置和大小資訊。
```bash
xdotool getactivewindow getwindowgeometry
# 輸出：Window 52428807
#   Position: 100,50 (screen: 0)
#   Geometry: 800x600
```

#### `getdisplaygeometry`
取得螢幕/顯示器的尺寸。
```bash
xdotool getdisplaygeometry
# 輸出：1920x1080
```

### 視窗搜尋與選擇

#### `search`
根據各種條件搜尋視窗。
```bash
# 根據視窗名稱/標題搜尋
xdotool search --name "Firefox"
xdotool search --name "Terminal"

# 根據類別名稱搜尋
xdotool search --class "firefox"

# 不區分大小寫搜尋
xdotool search --name --onlyvisible --maxdepth 1 "terminal"

# 常用搜尋選項：
# --name: 搜尋視窗標題
# --class: 搜尋視窗類別名稱
# --classname: 搜尋視窗類別實例名稱
# --onlyvisible: 僅可見視窗
# --maxdepth N: 限制搜尋深度
# --limit N: 限制結果數量
# --desktop N: 搜尋特定桌面/工作區
```

#### `selectwindow`
互動式視窗選擇（點擊選擇）。
```bash
xdotool selectwindow
# 點擊任意視窗以取得其 ID
```

### 滑鼠控制

#### `click`
模擬滑鼠點擊。
```bash
# 在目前位置左鍵點擊
xdotool click 1

# 右鍵點擊
xdotool click 3

# 中鍵點擊
xdotool click 2

# 雙擊
xdotool click --repeat 2 1

# 在特定座標點擊
xdotool mousemove 500 300 click 1

# 帶延遲的點擊
xdotool click --delay 500 1
```

#### `getmouselocation`
取得目前滑鼠游標位置。
```bash
xdotool getmouselocation
# 輸出：x:500 y:300 screen:0 window:52428807

# 僅取得座標
xdotool getmouselocation --shell
# 輸出：X=500 Y=300 SCREEN=0 WINDOW=52428807
```

#### 滑鼠移動
```bash
# 將滑鼠移動到絕對位置
xdotool mousemove 500 300

# 相對於目前位置移動滑鼠
xdotool mousemove_relative 10 -20

# 在單一指令中移動並點擊
xdotool mousemove 500 300 click 1
```

### 鍵盤輸入

#### `key`
向使用中視窗發送按鍵輸入。
```bash
# 發送單一按鍵
xdotool key Return
xdotool key Escape
xdotool key Tab

# 發送按鍵組合
xdotool key ctrl+c
xdotool key ctrl+alt+t
xdotool key shift+F10

# 依序發送多個按鍵
xdotool key ctrl+l type "https://google.com" key Return

# 常用按鍵名稱：
# - 字母：a, b, c, ... (小寫)
# - 數字：1, 2, 3, ...
# - 特殊鍵：Return, Escape, Tab, space, BackSpace, Delete
# - 功能鍵：F1, F2, ... F12
# - 修飾鍵：ctrl, alt, shift, super (Windows 鍵)
# - 方向鍵：Up, Down, Left, Right
```

#### 文字輸入
```bash
# 輸入文字（模擬輸入每個字元）
xdotool type "Hello World"

# 在字元之間帶延遲輸入
xdotool type --delay 100 "Slow typing"

# 清除延遲以快速輸入
xdotool type --clearmodifiers --delay 0 "Fast text"
```

### 視窗操作

```bash
# 聚焦/啟動視窗
xdotool windowactivate WINDOW_ID

# 最小化視窗
xdotool windowminimize WINDOW_ID

# 最大化視窗
xdotool windowmaximize WINDOW_ID

# 關閉視窗
xdotool windowclose WINDOW_ID

# 移動視窗到指定位置
xdotool windowmove WINDOW_ID 100 50

# 調整視窗大小
xdotool windowsize WINDOW_ID 800 600

# 移動視窗到特定桌面
xdotool set_desktop_for_window WINDOW_ID 2

# 將視窗提升到頂層
xdotool windowraise WINDOW_ID

# 顯示視窗
xdotool windowmap WINDOW_ID

# 隱藏視窗
xdotool windowunmap WINDOW_ID
```

### 進階功能

#### `behave`
設定視窗事件行為（觸發器）。
```bash
# 當視窗獲得焦點時執行指令
xdotool behave WINDOW_ID focus exec echo "Window focused"

# 當視窗建立時執行
xdotool behave WINDOW_ID create exec "notify-send 'New window'"

# 可用事件：focus, unfocus, mouse-enter, mouse-leave, create, destroy
```

#### `behave_screen_edge`
當滑鼠到達螢幕邊緣時觸發動作。
```bash
# 當滑鼠觸及左邊緣時執行指令
xdotool behave_screen_edge left exec "echo 'Left edge hit'"

# 可用邊緣：left, right, top, bottom
```

## 實用範例

### 基礎自動化腳本

#### 開啟終端機並執行指令
```bash
#!/bin/bash
# 開啟終端機並執行 ls 指令
xdotool key ctrl+alt+t
sleep 1
xdotool type "ls -la"
xdotool key Return
```

#### 截取使用中視窗畫面
```bash
#!/bin/bash
WINDOW=$(xdotool getactivewindow)
NAME=$(xdotool getwindowname $WINDOW | sed 's/[^a-zA-Z0-9]/_/g')
import -window $WINDOW "screenshot_${NAME}.png"
```

#### 聚焦特定應用程式
```bash
#!/bin/bash
# 聚焦 Firefox，若未執行則開啟
WINDOW=$(xdotool search --onlyvisible --class "firefox" | head -1)
if [ -n "$WINDOW" ]; then
    xdotool windowactivate $WINDOW
else
    firefox &
fi
```

### 視窗管理腳本

#### 並排排列視窗
```bash
#!/bin/bash
# 取得螢幕尺寸
eval $(xdotool getdisplaygeometry --shell)
HALF_WIDTH=$((WIDTH / 2))

# 取得兩個最近的視窗
WINDOWS=($(xdotool search --onlyvisible --maxdepth 1 "" | tail -2))

# 將第一個視窗置於左側
xdotool windowsize ${WINDOWS[0]} $HALF_WIDTH $HEIGHT
xdotool windowmove ${WINDOWS[0]} 0 0

# 將第二個視窗置於右側
xdotool windowsize ${WINDOWS[1]} $HALF_WIDTH $HEIGHT
xdotool windowmove ${WINDOWS[1]} $HALF_WIDTH 0
```

#### 置中使用中視窗
```bash
#!/bin/bash
WINDOW=$(xdotool getactivewindow)
eval $(xdotool getdisplaygeometry --shell)
eval $(xdotool getwindowgeometry --shell $WINDOW)

NEW_X=$(((WIDTH - WINDOW_WIDTH) / 2))
NEW_Y=$(((HEIGHT - WINDOW_HEIGHT) / 2))

xdotool windowmove $WINDOW $NEW_X $NEW_Y
```

### 應用程式特定自動化

#### 瀏覽器自動化
```bash
#!/bin/bash
# 開啟新分頁並導航
xdotool key ctrl+t
sleep 0.5
xdotool type "github.com"
xdotool key Return
```

#### 文字編輯器自動化
```bash
#!/bin/bash
# 全選並複製到剪貼簿
xdotool key ctrl+a
sleep 0.1
xdotool key ctrl+c
```

## 提示與最佳實踐

### 時序與延遲
```bash
# 為緩慢的應用程式添加延遲
xdotool key ctrl+alt+t
sleep 2  # 等待終端機開啟
xdotool type "echo hello"

# 使用 xdotool 內建的延遲
xdotool key --delay 100 ctrl+alt+t
```

### 錯誤處理
```bash
#!/bin/bash
# 在對視窗操作前檢查是否存在
WINDOW=$(xdotool search --name "MyApp" 2>/dev/null)
if [ -n "$WINDOW" ]; then
    xdotool windowactivate $WINDOW
else
    echo "Window not found"
    exit 1
fi
```

### 處理多個視窗
```bash
#!/bin/bash
# 對特定應用程式的所有視窗進行操作
xdotool search --name "Firefox" | while read WINDOW; do
    xdotool windowactivate $WINDOW
    xdotool key F5  # 重新整理
    sleep 0.5
done
```

### 除錯
```bash
# 啟用詳細輸出
xdotool --verbose key Return

# 取得詳細視窗資訊
xdotool search --name "Terminal" getwindowgeometry getwindowname getwindowpid
```

## 常見使用情境

1. **視窗管理**：以程式化方式聚焦、移動、調整視窗大小
2. **應用程式測試**：自動化 GUI 測試情境
3. **簡報工具**：自動化投影片導航和視窗切換
4. **遊戲巨集**：自動化重複性遊戲任務
5. **無障礙功能**：為殘疾使用者建立自訂輸入方法
6. **系統管理**：自動化基於 GUI 的管理任務
7. **開發工具**：與 IDE 和開發工作流程整合

## 疑難排解

### 常見問題

- **指令無效**：確保 X11 正在執行（非 Wayland）
- **權限問題**：某些操作可能需要適當的使用者權限
- **找不到視窗**：使用 `xdotool search` 驗證視窗存在且可見
- **時序問題**：在指令之間添加適當的延遲
- **特殊字元**：在文字輸入中對特殊字元使用正確的跳脫

### 安全性考量

- xdotool 可以控制任何應用程式，請謹慎使用
- 避免執行不受信任的 xdotool 腳本
- 處理敏感資料的自動化要特別小心
- 考慮僅在受控環境中使用 `xdotool`

本指南涵蓋了 xdotool 的基本和進階功能。嘗試這些指令，以建立符合您特定需求的強大桌面自動化腳本。