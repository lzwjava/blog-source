---
audio: false
generated: true
image: false
lang: ja
layout: post
title: PILとPyAutoGUIのスクリーンショット比較
translated: true
type: note
---

**PILの`ImageGrab`**と**PyAutoGUIのスクリーンショットツール**はどちらも画面キャプチャが可能ですが、使用方法、機能、クロスプラットフォーム対応が異なります。

---

## 1. PIL (Pillow) – `ImageGrab`

`ImageGrab`は**Pillow（モダンなPILフォーク）**の一部です。画面全体または一部をキャプチャできます。

### 動作方法

* **WindowsとmacOS**では、ネイティブAPI（WindowsではGDI、macOSではQuartz）を使用してピクセルをキャプチャします。
* **Linux**では、デフォルトではサポートされていません（`xwd`などの追加ライブラリが必要）。

### 使用例

```python
from PIL import ImageGrab

# 画面全体をキャプチャ
screenshot = ImageGrab.grab()
screenshot.save("screenshot.png")

# 領域をキャプチャ（左、上、右、下）
region = (100, 100, 500, 500)
cropped_screenshot = ImageGrab.grab(bbox=region)
cropped_screenshot.show()
```

### 長所

* シンプルで、Pillowの一部（追加の依存関係なし）。
* 画像処理に既にPillowを使用している場合に適しています。

### 短所

* デフォルトではLinuxをサポートしていません。
* 柔軟性が低い（マルチモニター対応なし）。

---

## 2. PyAutoGUI – `screenshot()`

PyAutoGUIは自動化（マウス/キーボード＋画面キャプチャ）のためのより汎用的なツールです。

### 動作方法

* **内部的にPillowをラップ**しています。
* OS APIを使用（クロスプラットフォーム：Windows、macOS、Linux）。
* Pillowの`Image`オブジェクトを直接返すか、ファイルに保存できます。

### 使用例

```python
import pyautogui

# 画面全体をキャプチャ
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

# 領域をキャプチャ（左、上、幅、高さ）
region_screenshot = pyautogui.screenshot(region=(100, 100, 400, 400))
region_screenshot.show()
```

### 長所

* クロスプラットフォーム（Windows、macOS、Linux）。
* 自動化スクリプト（マウス/キーボード制御）との統合が容易。
* 特定の領域を直接キャプチャ可能。

### 短所

* より多くの抽象化を行うため、`ImageGrab`より若干遅い。
* 追加の依存関係（`pip install pyautogui`）。

---

## どちらを使用すべきか？

* **スクリーンショットのみが必要で、Windows/macOSを使用している場合** → `ImageGrab`は軽量で高速です。
* **自動化機能やLinuxサポートも必要な場合** → `pyautogui`が適しています。

---

👉 `ImageGrab`と`pyautogui.screenshot()`のパフォーマンス差を**ベンチマークする方法**もPythonコードでお見せしましょうか？