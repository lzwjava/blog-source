---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: PIL Pillow画像処理ガイド
translated: true
type: note
---

### PIL/Pillowとは？
PILは元々Python Imaging Libraryの略称でしたが、現在はPillowパッケージ（モダンなフォーク）としてメンテナンスされています。コードでは`PIL`としてインポートしますが、インストールはpip経由でPillowをインストールする必要があります。Pythonで画像ファイルを開いたり、操作したり、保存するために使用されます。JPEG、PNG、GIF、BMPなどの形式をサポートしています。

### インストール方法
PILを使用するには、Pillowをインストールします：
```bash
pip install pillow
```

### 基本的なインポートと使用方法
インストール後、Pythonスクリプトで以下のようにインポートします：
```python
from PIL import Image
```
`import PIL.Image`とする必要はありません。これで直接Imageモジュールをインポートします。

### 一般的な画像操作
基本的なタスクの実行方法を以下に示します。ディレクトリに`example.jpg`という画像ファイルがあると仮定します。

#### 1. 画像を開く
```python
image = Image.open('example.jpg')  # 画像ファイルを開く
image.show()  # 画像を表示する（画像ビューアが利用可能なシステムで動作）
```

#### 2. 画像情報の取得
```python
print(image.format)  # 例: 'JPEG'
print(image.size)    # タプル: (幅, 高さ)
print(image.mode)    # 例: カラー画像の場合 'RGB'
```

#### 3. 画像のサイズ変更
```python
resized = image.resize((800, 600))  # 800x600ピクセルにリサイズ
resized.save('resized_example.jpg')  # リサイズした画像を保存
```

#### 4. フォーマット変換
```python
image.convert('L').save('grayscale_example.png')  # グレースケールに変換してPNGとして保存
```

#### 5. 画像の回転
```python
rotated = image.rotate(90)  # 時計回りに90度回転
rotated.save('rotated_example.jpg')
```

#### 6. 画像の切り抜き
```python
left, top, right, bottom = 100, 100, 300, 300  # 切り抜き範囲を定義 (x1, y1, x2, y2)
cropped = image.crop((left, top, right, bottom))
cropped.save('cropped_example.jpg')
```

#### 7. フィルターの適用（追加のインポートが必要）
フィルターを使用するには、`ImageFilter`をインポートします：
```python
from PIL import ImageFilter
blurred = image.filter(ImageFilter.BLUR)  # ぼかしフィルターを適用
blurred.save('blurred_example.jpg')
```

### 応用例：複数画像の一括処理
```python
import os
from PIL import Image

# フォルダ内の全JPEG画像を200x200にリサイズ
input_folder = 'images/'
output_folder = 'resized_images/'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        image = Image.open(os.path.join(input_folder, filename))
        resized = image.resize((200, 200))
        resized.save(os.path.join(output_folder, filename))
```

### ヒントと注意点
- **エラーハンドリング**: 無効なファイルに対してはtry-exceptを使用します。例: `try: image = Image.open('file.jpg')`
- **メモリ効率**: 大きな画像を扱う場合、操作後に`image.close()`を使用してメモリを解放します
- **ドキュメント**: Pillowの完全なドキュメントは[pillow.readthedocs.io](https://pillow.readthedocs.io/en/stable/)で確認できます。描画、テキスト追加、EXIFデータ処理などの機能について詳しく記載されています
- **依存関係**: Pillowは一部の環境ではシステムライブラリ（例: libjpeg）が必要な場合があります。問題が発生した場合はインストールガイドを参照してください

特定のタスクやエラーについて詳しい情報があれば、より具体的なサポートができます！