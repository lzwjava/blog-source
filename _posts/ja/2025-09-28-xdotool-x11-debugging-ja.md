---
audio: false
generated: true
image: false
lang: ja
layout: post
model: anthropic/claude-sonnet-4
title: xdotool X11 デバッグガイド
translated: true
type: note
---

表示されているエラーは、`xdotool` が X サーバーからアクティブなウィンドウ情報を取得する際に問題が発生していることを示しています。以下に、詳細なエラー情報を診断・取得するための方法をいくつか紹介します：

## 1. X11 環境の確認
まず、ディスプレイ環境を確認してください：
```bash
echo $DISPLAY
echo $XDG_SESSION_TYPE
```

Wayland を実行している場合、`xdotool` は X11 用に設計されているため正しく動作しません。

## 2. 詳細モードの使用
より詳細な出力で xdotool を実行してみてください：
```bash
xdotool --help  # 利用可能なオプションを確認
```

## 3. 代替デバッグコマンド
以下のコマンドで情報を収集してみてください：

```bash
# X サーバーにアクセスできるか確認
xwininfo -root -tree

# よりシンプルな xdotool コマンドを試す
xdotool search --name ".*" | head -5

# ウィンドウマネージャーを確認
wmctrl -l  # すべてのウィンドウをリスト表示
wmctrl -d  # デスクトップをリスト表示

# X11 プロパティを直接確認
xprop -root _NET_ACTIVE_WINDOW
```

## 4. X11 拡張機能の確認
エラーは X11 拡張機能の不足に関連している可能性があります：
```bash
# 利用可能な拡張機能を確認
xdpyinfo | grep -i extension

# 必要な拡張機能を特に確認
xdpyinfo | grep -E "(XTEST|Extended-Visual-Information)"
```

## 5. 権限の問題
適切な権限があるか確認してください：
```bash
# ディスプレイにアクセスできるか確認
xhost +local:
```

## 6. 代替ツール
xdotool が引き続き失敗する場合、以下の代替ツールを試してください：

```bash
# Wayland の場合
if [ "$XDG_SESSION_TYPE" = "wayland" ]; then
    # 利用可能であれば wlr-activewindow を使用（Wayland）
    swaymsg -t get_tree | jq '.. | select(.focused?) | .name'
fi

# X11 の代替ツール
xtitle  # インストールされている場合
xprop -root | grep "_NET_ACTIVE_WINDOW(WINDOW)"
```

## 7. システム情報
システム設定を確認してください：
```bash
# デスクトップ環境を確認
echo $DESKTOP_SESSION
ps aux | grep -E "(gnome|kde|xfce|i3|sway)"

# コンテナまたは VM で実行しているか確認
systemd-detect-virt
```

最も可能性の高い原因は：
1. **Wayland セッション**: xdotool は Wayland では動作しません
2. **権限不足**: X サーバーアクセス制限
3. **ウィンドウマネージャーの非互換性**: 一部の WM は `_NET_ACTIVE_WINDOW` をサポートしていません
4. **X11 拡張機能の不足**: 必要な拡張機能が読み込まれていません

上記の診断コマンドを試して、どのような出力が得られるか教えてください - それにより正確な問題を特定するのに役立ちます。