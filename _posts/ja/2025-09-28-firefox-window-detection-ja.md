---
audio: false
generated: true
image: false
lang: ja
layout: post
model: anthropic/claude-sonnet-4
title: Linux向けFirefoxウィンドウ検出ツール
translated: true
type: note
---

`xdotool`以外にも、LinuxでアクティブなFirefoxウィンドウの情報を取得するための代替ツールや方法がいくつかあります：

## 代替ツール

### 1. **wmctrl**
xdotoolよりも堅牢な代替ツール：
```bash
# アクティブウィンドウを取得
wmctrl -a

# 詳細情報とともにすべてのウィンドウをリスト表示
wmctrl -l -x

# Firefoxウィンドウを特定して取得
wmctrl -l | grep -i firefox
```

### 2. **qdbus** (KDE/Qtアプリケーション用)
```bash
# アクティブウィンドウ情報を取得
qdbus org.kde.KWin /KWin activeWindow

# ウィンドウリストを取得
qdbus org.kde.KWin /KWin windows
```

### 3. **xwininfo**
組み込みのX11ユーティリティ：
```bash
# インタラクティブなウィンドウ選択
xwininfo

# ルートウィンドウ情報を取得
xwininfo -root -tree | grep -i firefox

# アクティブウィンドウを取得（ウィンドウIDの知識が必要）
xwininfo -id $(xprop -root _NET_ACTIVE_WINDOW | cut -d' ' -f5)
```

### 4. **xprop**
もう一つのX11ユーティリティ：
```bash
# アクティブウィンドウのプロパティを取得
xprop -root _NET_ACTIVE_WINDOW

# ウィンドウクラスとタイトルを取得
xprop -root | grep "_NET_ACTIVE_WINDOW(WINDOW)"
```

## Waylandシステム用

Waylandを実行している場合、X11ツールは機能しません。代わりに以下を試してください：

### 5. **swaymsg** (Sway用)
```bash
swaymsg -t get_tree | jq -r '.. | select(.focused? == true)'
```

### 6. **hyprctl** (Hyprland用)
```bash
hyprctl activewindow
```

### 7. **gdbus** (GNOME/GTK用)
```bash
gdbus call --session --dest org.gnome.Shell --object-path /org/gnome/Shell --method org.gnome.Shell.Eval "global.get_window_actors()"
```

## Pythonソリューション

### 8. **Xlibを使用したPython**
```python
from Xlib import X, display
from Xlib.error import XError

def get_active_window():
    try:
        d = display.Display()
        root = d.screen().root
        
        # アクティブウィンドウを取得
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

### 9. **subprocessを使用したPython**
```python
import subprocess

def get_firefox_windows():
    try:
        # wmctrlを使用
        result = subprocess.run(['wmctrl', '-l'], 
                              capture_output=True, text=True)
        firefox_windows = [line for line in result.stdout.split('\n') 
                          if 'firefox' in line.lower()]
        return firefox_windows
    except FileNotFoundError:
        return "wmctrl not installed"

print(get_firefox_windows())
```

## xdotool問題のトラブルシューティング

「BadWindow」エラーは通常以下を意味します：

1. **権限の問題**: 異なる権限で実行してみてください
2. **ディスプレイの問題**: `$DISPLAY`が正しく設定されているか確認してください
3. **Waylandの競合**: X11ではなくWayland上で実行されている可能性があります

ディスプレイサーバーを確認するには：
```bash
echo $XDG_SESSION_TYPE
loginctl show-session $(loginctl | grep $(whoami) | awk '{print $1}') -p Type
```

## 推奨アプローチ

最大の互換性のために、以下の順序をお勧めします：

1. **wmctrl** - 異なるウィンドウマネージャー間で最も信頼性が高い
2. **xwininfo + xprop** の組み合わせ - ほとんどのX11インストールに組み込まれている
3. **Pythonソリューション** - 最も柔軟でプログラム可能
4. **デスクトップ環境固有のツール** (swaymsg, hyprctlなど)

最初に `wmctrl -l | grep -i firefox` を試してください - 通常、xdotoolのウィンドウ検出機能の最も簡単な代替手段です。