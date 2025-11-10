---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: PythonによるWindowsトースト通知
translated: true
type: note
---

### win10toastとは？
win10toastは、PythonスクリプトからWindows 10でトースト通知（ポップアップアラート）を送信できる軽量なPythonライブラリです。デスクトップアプリケーションやスクリプトでのユーザー通知に有用で、ネイティブのWindowsトーストと同様の機能を提供します。

### 前提条件
- Python 3.x がインストールされていること
- Windows 10（Windows固有のAPIに依存しています）
- Python以外の追加の依存関係はありません

### インストール
pip（Pythonパッケージインストーラー）経由でライブラリをインストールします：

```
pip install win10toast
```

仮想環境を使用している場合は、先に仮想環境を有効化してください。

### 基本的な使用方法
1. モジュールをインポートします：
   ```python
   from win10toast import ToastNotifier
   ```

2. `ToastNotifier`インスタンスを作成し、その`show_toast`メソッドを呼び出して通知を表示します：
   ```python
   toaster = ToastNotifier()
   toaster.show_toast("タイトル", "メッセージ", icon_path=None, duration=5)
   ```
   - **タイトル**: 通知の見出しとなる文字列
   - **メッセージ**: 通知の本文となる文字列
   - **icon_path**: 通知アイコンとして使用する.icoまたは.pngファイルへのオプショナルなパス（例: `"path/to/icon.ico"`）。アイコンなしの場合は省略します
   - **duration**: トーストが表示される時間（秒単位）。デフォルトは5秒（Windowsがこれを上書きする場合があります）

通知はアクションセンターとポップアップとして表示されます。

### 高度な使用方法
- **アイコンのカスタマイズ**: 画像ファイルを使用します（最高品質を得るには128x128ピクセルを推奨）
- **クリックイベントの処理**: コールバック関数を渡します（サポートは限定的。主にオンクリック動作は基本的なものです）
- **複数の通知**: `ToastNotifier`を一度インスタンス化し、再利用して複数のトーストを送信します
- **エラーハンドリング**: try-exceptでラップし、通知が無効になっている場合などのWindows APIの問題を処理します

アイコンとエラーハンドリングを使用した例：
```python
from win10toast import ToastNotifier
import os

try:
    toaster = ToastNotifier()
    icon = "C:\\path\\to\\icon.ico"  # 実際のパスに置き換えてください
    toaster.show_toast("アラート！", "スクリプトが完了しました。", icon_path=icon, duration=10)
except Exception as e:
    print(f"通知に失敗しました: {e}")
```

### 制限事項とヒント
- 通知にはWindows 10のアクションセンターが有効である必要があります（設定 > システム > 通知とアクション）
- より複雑な機能（アクションや画像など）が必要な場合は、plyerやwinrt（最新のWindows SDKの一部）などの代替手段を検討してください
- 通知が表示されない場合は、Windowsのフォーカスアシスト設定を確認するか、スクリプトを管理者として実行してみてください

完全なドキュメントについては、[win10toast GitHubリポジトリ](https://github.com/Charnelx/win10toast)を確認してください。問題が発生した場合は、エラーの詳細を提供すると適切なヘルプが得られます。