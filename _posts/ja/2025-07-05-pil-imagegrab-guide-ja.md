---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: PIL ImageGrab スクリーンショットガイド
translated: true
type: note
---

### 前提条件
PIL（Pillow）ライブラリの `ImageGrab` を使用するには、Pillowがインストールされていることを確認してください。Windowsでは、pip経由でインストールします：
```
pip install Pillow
```
`ImageGrab` はネイティブのWindows APIを使用するため、Windowsでは通常追加のセットアップは必要ありません。

### 基本的な使用方法
`ImageGrab.grab()` は画面全体（すべてのモニター）をPIL Imageオブジェクトとしてキャプチャします。以下はスクリーンショットを撮影しPNGファイルとして保存する簡単な例です：

```python
from PIL import ImageGrab

# 画面全体をキャプチャ
screenshot = ImageGrab.grab()

# 画像をファイルに保存
screenshot.save("screenshot.png")
```

これにより、現在の作業ディレクトリに `screenshot.png` というファイルが保存されます。

### 追加オプション
- **特定の領域をキャプチャ**: ピクセル座標のタプルとしてバウンディングボックス（左、上、右、下）を指定します。
  ```python
  # (100, 100)から始まる300x300ピクセルの領域をキャプチャ
  region = (100, 100, 400, 400)  # 必要に応じて座標を調整
  screenshot = ImageGrab.grab(bbox=region)
  screenshot.save("region_screenshot.png")
  ```
- **マウスカーソルを含める**（サポートされている場合。バージョンの詳細についてはPillowドキュメントを確認）：
  ```python
  # 注：一部のシステムでは include_layered_windows=True が必要な場合があります
  screenshot = ImageGrab.grab(include_layered_windows=True)
  ```
- **画像を表示**: `screenshot.show()` を使用してデフォルトの画像ビューアーで開きます（テスト用）。

### 注意点
- 座標はピクセル単位で、(0, 0)はプライマリモニターの左上隅です。
- マルチモニター環境では、`grab()` はすべての画面を1つの合成画像としてキャプチャします。
- 問題が発生した場合（新しいWindowsバージョンでの権限エラーなど）、スクリプトに画面キャプチャの権限があることを確認するか、管理者権限で実行してみてください。
- 完全なドキュメント：[Pillow ImageGrab docs](https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html)。Windows固有の問題については、必要に応じてGitHubのイシューを確認してください。