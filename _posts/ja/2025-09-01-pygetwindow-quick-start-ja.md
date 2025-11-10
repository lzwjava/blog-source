---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: PyGetWindowクイックスタートガイド
translated: true
type: note
---

### インストール
PyGetWindowは、複数のプラットフォーム（Windows、macOS、Linux）でウィンドウを操作およびクエリするためのPythonライブラリです。pipを使用してインストールします：

```bash
pip install pygetwindow
```

### モジュールのインポート
Pythonスクリプトでモジュールをインポートします：

```python
import pygetwindow as gw
```

### ウィンドウオブジェクトの取得
PyGetWindowはウィンドウを`Window`オブジェクトとして表現します。タイトル、プロセス、その他の属性によってウィンドウを取得できます。

- **すべてのウィンドウオブジェクトを取得**:  
  `gw.getAllWindows()`を使用して、すべての開いているウィンドウのリストを返します。

- **タイトルでウィンドウを取得**:  
  部分一致または完全一致には`gw.getWindowsWithTitle(title)`または`gw.getFirstWindowWithTitle(title)`を使用します。

- **アクティブなウィンドウを取得**:  
  現在フォーカスされているウィンドウを取得するには`gw.getActiveWindow()`を使用します。

例：
```python
windows = gw.getAllWindows()
active = gw.getActiveWindow()
notepad = gw.getWindowsWithTitle('Notepad')  # タイトルに'Notepad'を含むウィンドウのリスト
```

### ウィンドウオブジェクトの一般的なメソッド
`Window`オブジェクトを取得したら、以下のようなプロパティとメソッドにアクセスできます：

- **プロパティ**: `title`、`left`、`top`、`width`、`height`、`isMinimized`、`isMaximized`、`isActive`。
- **メソッド**: 
  - `activate()`: ウィンドウを前面に移動させてアクティブにします。
  - `maximize()` / `minimize()` / `restore()` / `close()`: ウィンドウの状態を制御します。
  - `resize() / move()`: サイズと位置を調整します。

例：
```python
if notepad:
    win = notepad[0]
    print(win.title)  # 出力例: 'Untitled - Notepad'
    win.activate()
    win.maximize()
    win.move(100, 100)  # 位置(100, 100)に移動
    win.resize(800, 600)  # 800x600にリサイズ
```

### 複数プラットフォームの扱い
- WindowsとmacOSでは、ネイティブAPIを使用します。
- Linuxでは、X11またはWaylandのサポートに依存します。システムにインストールされていることを確認してください（例：Ubuntuでは`x11-utils`）。
- お使いのOSでメソッドがサポートされていない場合、`NotImplementedError`が発生する可能性があります。

### 例
実用的なコードスニペットをいくつか紹介します：

1. **すべてのウィンドウタイトルを表示**:
   ```python
   for win in gw.getAllWindows():
       print(win.title)
   ```

2. **特定のウィンドウを閉じる**:
   ```python
   firefox_wins = gw.getWindowsWithTitle('Mozilla Firefox')
   if firefox_wins:
       firefox_wins[0].close()
   ```

3. **複数のウィンドウを移動およびリサイズ**:
   ```python
   windows = gw.getAllWindows()
   for i, win in enumerate(windows[:3]):  # 最初の3つのウィンドウ
       win.move(50 * i, 50 * i)
       win.resize(400, 400)
   ```

高度な使用方法については、[公式ドキュメント](https://pygetwindow.readthedocs.io/)を参照してください。プラットフォーム固有の問題が発生した場合は、システムの権限やLinuxでの`xdotool`などの依存関係を確認してください。