---
audio: false
generated: true
image: false
lang: ja
layout: post
model: anthropic/claude-sonnet-4
title: Xdotoolコマンドライン自動化ガイド
translated: true
type: note
---

## xdotoolとは？

xdotoolはX11（Linuxデスクトップ環境）向けのコマンドライン自動化ツールで、以下のことが可能です：
- マウスの移動とクリックの制御
- アプリケーションへのキーストローク送信
- ウィンドウ操作（移動、リサイズ、フォーカス）
- 様々な条件でのウィンドウ検索
- プログラムによるデスクトップ操作の自動化

## インストール

```bash
# Ubuntu/Debian
sudo apt install xdotool

# Fedora/RHEL/CentOS
sudo dnf install xdotool

# Arch Linux
sudo pacman -S xdotool

# ソースからインストール
git clone https://github.com/jordansissel/xdotool
cd xdotool
make
sudo make install
```

## コアコマンド

### ウィンドウ情報コマンド

#### `getactivewindow`
現在アクティブ/フォーカスされているウィンドウのIDを取得します。
```bash
xdotool getactivewindow
# 出力: 52428807 (ウィンドウID)

# アクティブウィンドウのタイトルを取得
xdotool getactivewindow getwindowname
```

#### `getwindowfocus`
getactivewindowと似ていますが、一部のウィンドウマネージャーでは異なる動作をします。
```bash
xdotool getwindowfocus
```

#### `getwindowname`
ウィンドウのタイトル/名前を取得します。
```bash
# アクティブウィンドウの名前を取得
xdotool getactivewindow getwindowname

# 特定のウィンドウIDの名前を取得
xdotool getwindowname 52428807
```

#### `getwindowpid`
ウィンドウに関連付けられたプロセスID（PID）を取得します。
```bash
xdotool getactivewindow getwindowpid
```

#### `getwindowgeometry`
ウィンドウの位置とサイズ情報を取得します。
```bash
xdotool getactivewindow getwindowgeometry
# 出力: Window 52428807
#   Position: 100,50 (screen: 0)
#   Geometry: 800x600
```

#### `getdisplaygeometry`
画面/ディスプレイの寸法を取得します。
```bash
xdotool getdisplaygeometry
# 出力: 1920x1080
```

### ウィンドウ検索と選択

#### `search`
様々な条件でウィンドウを検索します。
```bash
# ウィンドウ名/タイトルで検索
xdotool search --name "Firefox"
xdotool search --name "Terminal"

# クラス名で検索
xdotool search --class "firefox"

# 大文字小文字を区別しない検索
xdotool search --name --onlyvisible --maxdepth 1 "terminal"

# 一般的な検索オプション:
# --name: ウィンドウタイトルを検索
# --class: ウィンドウクラス名を検索
# --classname: ウィンドウクラスインスタンス名を検索
# --onlyvisible: 表示されているウィンドウのみ
# --maxdepth N: 検索深度を制限
# --limit N: 結果数を制限
# --desktop N: 特定のデスクトップ/ワークスペースを検索
```

#### `selectwindow`
対話型ウィンドウ選択（クリックで選択）。
```bash
xdotool selectwindow
# 任意のウィンドウをクリックしてIDを取得
```

### マウス制御

#### `click`
マウスクリックをシミュレートします。
```bash
# 現在位置で左クリック
xdotool click 1

# 右クリック
xdotool click 3

# 中クリック
xdotool click 2

# ダブルクリック
xdotool click --repeat 2 1

# 特定座標でクリック
xdotool mousemove 500 300 click 1

# 遅延付きクリック
xdotool click --delay 500 1
```

#### `getmouselocation`
現在のマウスカーソル位置を取得します。
```bash
xdotool getmouselocation
# 出力: x:500 y:300 screen:0 window:52428807

# 座標のみ取得
xdotool getmouselocation --shell
# 出力: X=500 Y=300 SCREEN=0 WINDOW=52428807
```

#### マウス移動
```bash
# マウスを絶対位置に移動
xdotool mousemove 500 300

# 現在位置からの相対移動
xdotool mousemove_relative 10 -20

# 移動とクリックを1コマンドで
xdotool mousemove 500 300 click 1
```

### キーボード入力

#### `key`
アクティブウィンドウにキーストロークを送信します。
```bash
# 単一キー送信
xdotool key Return
xdotool key Escape
xdotool key Tab

# キー組み合わせ送信
xdotool key ctrl+c
xdotool key ctrl+alt+t
xdotool key shift+F10

# 複数キーを順次送信
xdotool key ctrl+l type "https://google.com" key Return

# 一般的なキー名:
# - 文字: a, b, c, ... (小文字)
# - 数字: 1, 2, 3, ...
# - 特殊: Return, Escape, Tab, space, BackSpace, Delete
# - ファンクション: F1, F2, ... F12
# - 修飾子: ctrl, alt, shift, super (Windowsキー)
# - 矢印: Up, Down, Left, Right
```

#### テキスト入力
```bash
# テキスト入力（各文字のタイピングをシミュレート）
xdotool type "Hello World"

# 文字間遅延付き入力
xdotool type --delay 100 "Slow typing"

# 高速入力のための遅延クリア
xdotool type --clearmodifiers --delay 0 "Fast text"
```

### ウィンドウ操作

```bash
# ウィンドウをフォーカス/アクティブ化
xdotool windowactivate WINDOW_ID

# ウィンドウを最小化
xdotool windowminimize WINDOW_ID

# ウィンドウを最大化
xdotool windowmaximize WINDOW_ID

# ウィンドウを閉じる
xdotool windowclose WINDOW_ID

# ウィンドウを位置に移動
xdotool windowmove WINDOW_ID 100 50

# ウィンドウをリサイズ
xdotool windowsize WINDOW_ID 800 600

# ウィンドウを特定のデスクトップに移動
xdotool set_desktop_for_window WINDOW_ID 2

# ウィンドウを最前面に表示
xdotool windowraise WINDOW_ID

# ウィンドウを表示
xdotool windowmap WINDOW_ID

# ウィンドウを非表示
xdotool windowunmap WINDOW_ID
```

### 高度な機能

#### `behave`
ウィンドウイベントの動作（トリガー）を設定します。
```bash
# ウィンドウがフォーカスを得たときにコマンド実行
xdotool behave WINDOW_ID focus exec echo "Window focused"

# ウィンドウ作成時に実行
xdotool behave WINDOW_ID create exec "notify-send 'New window'"

# 利用可能なイベント: focus, unfocus, mouse-enter, mouse-leave, create, destroy
```

#### `behave_screen_edge`
マウスが画面端に到達したときにアクションをトリガーします。
```bash
# マウスが左端に当たったときにコマンド実行
xdotool behave_screen_edge left exec "echo 'Left edge hit'"

# 利用可能な端: left, right, top, bottom
```

## 実用的な例

### 基本的な自動化スクリプト

#### ターミナルを開いてコマンド実行
```bash
#!/bin/bash
# ターミナルを開いてlsコマンドを実行
xdotool key ctrl+alt+t
sleep 1
xdotool type "ls -la"
xdotool key Return
```

#### アクティブウィンドウのスクリーンショット
```bash
#!/bin/bash
WINDOW=$(xdotool getactivewindow)
NAME=$(xdotool getwindowname $WINDOW | sed 's/[^a-zA-Z0-9]/_/g')
import -window $WINDOW "screenshot_${NAME}.png"
```

#### 特定アプリケーションにフォーカス
```bash
#!/bin/bash
# Firefoxにフォーカス、実行されていない場合は起動
WINDOW=$(xdotool search --onlyvisible --class "firefox" | head -1)
if [ -n "$WINDOW" ]; then
    xdotool windowactivate $WINDOW
else
    firefox &
fi
```

### ウィンドウ管理スクリプト

#### ウィンドウを左右に並べる
```bash
#!/bin/bash
# 画面ジオメトリを取得
eval $(xdotool getdisplaygeometry --shell)
HALF_WIDTH=$((WIDTH / 2))

# 最新の2つのウィンドウを取得
WINDOWS=($(xdotool search --onlyvisible --maxdepth 1 "" | tail -2))

# 最初のウィンドウを左に配置
xdotool windowsize ${WINDOWS[0]} $HALF_WIDTH $HEIGHT
xdotool windowmove ${WINDOWS[0]} 0 0

# 2番目のウィンドウを右に配置
xdotool windowsize ${WINDOWS[1]} $HALF_WIDTH $HEIGHT
xdotool windowmove ${WINDOWS[1]} $HALF_WIDTH 0
```

#### アクティブウィンドウを中央に配置
```bash
#!/bin/bash
WINDOW=$(xdotool getactivewindow)
eval $(xdotool getdisplaygeometry --shell)
eval $(xdotool getwindowgeometry --shell $WINDOW)

NEW_X=$(((WIDTH - WINDOW_WIDTH) / 2))
NEW_Y=$(((HEIGHT - WINDOW_HEIGHT) / 2))

xdotool windowmove $WINDOW $NEW_X $NEW_Y
```

### アプリケーション固有の自動化

#### ブラウザ自動化
```bash
#!/bin/bash
# 新しいタブを開いてナビゲート
xdotool key ctrl+t
sleep 0.5
xdotool type "github.com"
xdotool key Return
```

#### テキストエディタ自動化
```bash
#!/bin/bash
# 全選択してクリップボードにコピー
xdotool key ctrl+a
sleep 0.1
xdotool key ctrl+c
```

## ヒントとベストプラクティス

### タイミングと遅延
```bash
# 遅いアプリケーションのために遅延を追加
xdotool key ctrl+alt+t
sleep 2  # ターミナルが開くのを待機
xdotool type "echo hello"

# xdotoolの組み込み遅延を使用
xdotool key --delay 100 ctrl+alt+t
```

### エラーハンドリング
```bash
#!/bin/bash
# ウィンドウが存在するか確認してから操作
WINDOW=$(xdotool search --name "MyApp" 2>/dev/null)
if [ -n "$WINDOW" ]; then
    xdotool windowactivate $WINDOW
else
    echo "Window not found"
    exit 1
fi
```

### 複数ウィンドウの操作
```bash
#!/bin/bash
# 特定アプリケーションの全ウィンドウに対して操作
xdotool search --name "Firefox" | while read WINDOW; do
    xdotool windowactivate $WINDOW
    xdotool key F5  # 更新
    sleep 0.5
done
```

### デバッグ
```bash
# 詳細出力を有効化
xdotool --verbose key Return

# 詳細なウィンドウ情報を取得
xdotool search --name "Terminal" getwindowgeometry getwindowname getwindowpid
```

## 一般的な使用例

1. **ウィンドウ管理**: プログラムによるウィンドウのフォーカス、移動、リサイズ
2. **アプリケーションテスト**: GUIテストシナリオの自動化
3. **プレゼンテーションツール**: スライドナビゲーションとウィンドウ切り替えの自動化
4. **ゲーミングマクロ**: 反復的なゲームタスクの自動化
5. **アクセシビリティ**: 障害を持つユーザーのためのカスタム入力方法の作成
6. **システム管理**: GUIベースの管理タスクの自動化
7. **開発ツール**: IDEと開発ワークフローとの統合

## トラブルシューティング

### 一般的な問題

- **コマンドが動作しない**: X11が実行されていることを確認（Waylandではない）
- **権限の問題**: 一部の操作には適切なユーザー権限が必要
- **ウィンドウが見つからない**: `xdotool search`を使用してウィンドウの存在と可視性を確認
- **タイミングの問題**: コマンド間に適切な遅延を追加
- **特殊文字**: テキスト入力での特殊文字の適切なエスケープを使用

### セキュリティ考慮事項

- xdotoolは任意のアプリケーションを制御可能、注意して使用
- 信頼できないxdotoolスクリプトの実行を避ける
- 機密データを扱う自動化には注意
- 制御された環境でのみ`xdotool`の使用を検討

このガイドはxdotoolの基本的および高度な機能をカバーしています。これらのコマンドを実験して、特定のニーズに合わせた強力なデスクトップ自動化スクリプトを作成してください。