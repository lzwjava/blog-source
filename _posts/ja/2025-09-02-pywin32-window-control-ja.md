---
audio: false
generated: true
image: false
lang: ja
layout: post
title: PyWin32 ウィンドウ制御の基本
translated: true
type: note
---

**PyWin32ウィンドウ**の操作ガイド - プロパティ、アクティベーション、背面領域の扱いに焦点を当てて説明します。

---

## 1. PyWin32におけるウィンドウとは？

PyWin32において「ウィンドウ」とは、**ハンドル（HWND）** を持つWindows APIによって管理されるあらゆるGUI要素を指します。これはトップレベルのアプリケーションウィンドウ、ダイアログ、あるいはフォーム内のコントロールさえも含みます。

通常、ウィンドウとのやり取りは以下のモジュールを使用して行います：

* `win32gui` – ウィンドウハンドル、プロパティ、メッセージのための低レベル関数
* `win32con` – Windowsメッセージとスタイルのための定数
* `win32api` – 一般的なWindows API関数

---

## 2. 一般的なウィンドウプロパティ

ウィンドウには、問い合わせや変更が可能な多くの属性があります：

* **ハンドル (HWND)**: ウィンドウの一意な識別子
* **タイトル (キャプション)**: タイトルバーに表示されるテキスト (`win32gui.GetWindowText(hwnd)`)
* **クラス名**: ウィンドウの登録済みクラス (`win32gui.GetClassName(hwnd)`)
* **スタイル**: ウィンドウの動作/外観を定義 (`GetWindowLong` と `GWL_STYLE`)
* **位置とサイズ**: `GetWindowRect(hwnd)` または `MoveWindow` による矩形座標
* **可視性**: ウィンドウが表示されているかどうか (`IsWindowVisible`)
* **有効状態**: 入力を受け付けるかどうか (`IsWindowEnabled`)
* **親/オーナー**: ウィンドウの階層構造 (`GetParent(hwnd)`)

---

## 3. ウィンドウのアクティベーション

ウィンドウを前面に表示したりアクティブにするには：

* **SetForegroundWindow(hwnd)** – ウィンドウをアクティブにする
* **SetActiveWindow(hwnd)** – ウィンドウをアクティブにするが、最前面を保証しない
* **BringWindowToTop(hwnd)** – 他のウィンドウの上に持ち上げる
* **ShowWindow(hwnd, flag)** – `flag` に応じて表示/非表示/最小化/最大化を行う（例：`SW_SHOW`, `SW_MINIMIZE`, `SW_RESTORE`）

---

## 4. 「背面領域」（Zオーダーと配置）

ウィンドウはZオーダーで重ねられています：

* **最前面 (Topmost)** – 常に他のウィンドウの上に表示 (`SetWindowPos` と `HWND_TOPMOST`)
* **背面 (Bottom)** – `SetWindowPos(hwnd, win32con.HWND_BOTTOM, …)` を使用してウィンドウを他のすべての背面に送る
* **非アクティブ (NoActivate)** – ウィンドウをアクティブにせずに表示または配置できる（`SWP_NOACTIVATE` などのフラグを使用）

これは、バックグラウンドで動作するユーティリティウィンドウをフォーカスを奪わずに開いたままにしたい場合に便利です。

---

## 5. 使用する典型的な関数

以下に、例とともに主要なPyWin32関数を示します：

```python
import win32gui
import win32con

# タイトルでウィンドウを検索
hwnd = win32gui.FindWindow(None, "Untitled - Notepad")

# プロパティを取得
title = win32gui.GetWindowText(hwnd)
rect = win32gui.GetWindowRect(hwnd)  # (left, top, right, bottom)

# ウィンドウをアクティブ化
win32gui.SetForegroundWindow(hwnd)

# 背面に移動（他のウィンドウの背後に）
win32gui.SetWindowPos(hwnd, win32con.HWND_BOTTOM, 0, 0, 0, 0,
                      win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

# 表示/復元
win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
```

---

## 6. イベント/メッセージ処理

以下の方法でウィンドウイベント（アクティベーション、リサイズ、クローズ）にフックすることもできます：

* `SetWindowLong` を使用したサブクラス化
* `SendMessage` / `PostMessage` を使用したアクションのシミュレート
* `WM_ACTIVATE`, `WM_SIZE` などのメッセージ

---

✅ まとめ：

* **プロパティ**: タイトル、クラス、サイズ、スタイル、可視性、有効状態
* **アクティベーション**: `SetForegroundWindow`, `BringWindowToTop` を使用
* **背面領域**: `SetWindowPos` と `HWND_BOTTOM` でZオーダーを管理

**実用的なスクリプト**として、すべてのトップレベルウィンドウをそのプロパティ（タイトル、位置、Zオーダー）とともにリスト表示し、インタラクティブにアクティブ化したり背面に送ったりできるものを含めてほしいですか？