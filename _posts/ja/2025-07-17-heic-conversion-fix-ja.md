---
audio: false
generated: true
lang: ja
layout: post
title: Pillow HEICサポートエラーの修正
translated: true
type: note
---

エラー `cannot identify image file` は、PillowがHEICファイルを読み取れないことを示しています。これは以下のいずれかの理由が考えられます：
1. **`libheif`ライブラリの欠如**: PillowがHEICファイルを処理するには`libheif`が必要ですが、システムにインストールされていないか、適切に設定されていない可能性があります。
2. **破損または互換性のないHEICファイル**: HEICファイルが破損しているか、Pillowが処理できない形式である可能性があります。
3. **Pillowのバージョン問題**: Pillow 9.0.0+はHEICをサポートしていますが、設定の問題や古いバージョンが原因である可能性があります。

以前の出力からmacOSを使用していると想定し、問題を診断するための追加のエラーハンドリングとロギングを含む修正済みPythonスクリプトを提供します。また、`libheif`のインストールとPillowのHEICサポートの確認手順も案内します。Pillowが引き続き失敗する場合、スクリプトにはHEIC変換のためのフォールバックとして`ImageMagick`（インストール済みの場合）の使用が含まれています。

### 問題解決の手順

#### 1. `libheif`のインストール
PillowはHEICサポートに`libheif`に依存しています。Homebrewを使用してインストールします：
```bash
brew install libheif
```
インストール後、Pillowが`libheif`とリンクするように再インストールします：
```bash
pip uninstall pillow
pip install pillow
```

#### 2. PillowのHEICサポートを確認
PillowがHEICファイルを処理できるか確認します：
```bash
python -c "from PIL import features; print(features.check_feature('heic'))"
```
- `True`と出力されれば、PillowはHEICサポートがあります。
- `False`またはエラーが出力される場合、`libheif`が適切に設定されていないか、PillowがHEICサポートなしでビルドされています。

#### 3. ファイルの整合性を確認
HEICファイルが破損していないことを確認します。macOSのPreviewなどのビューアでファイル（例：`IMG_5988.HEIC`）を開いてみてください。開かない場合、ファイルが破損している可能性があり、再エクスポートまたは新しいコピーを取得する必要があります。

#### 4. 更新されたPythonスクリプト
更新されたスクリプト：
- 改善されたエラーハンドリングでHEIC変換にPillowを使用します。
- PillowがHEICファイルの読み取りに失敗した場合、`ImageMagick`（インストール済みの場合）へのフォールバックを提供します。
- デバッグ用に詳細なエラーをファイル（`conversion_errors.log`）に記録します。
- `.heic`と`.heif`の両方の拡張子をサポートします。
- 出力JPGを約500KBに圧縮します。

```python
import os
import argparse
import subprocess
import logging
from PIL import Image
from datetime import datetime

# ロギングの設定
logging.basicConfig(
    filename="conversion_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# コマンドライン引数の解析
parser = argparse.ArgumentParser(description="HEIC画像をJPGに変換し、約500KBに圧縮します。")
parser.add_argument("input_dir", help="HEICファイルを含むディレクトリ")
args = parser.parse_args()

# 入力および出力ディレクトリの定義
input_dir = args.input_dir.rstrip(os.sep)
output_dir = input_dir + "_compressed"
target_size_kb = 500  # 目標ファイルサイズ（KB）

# 出力ディレクトリが存在しない場合は作成
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def get_file_size(file_path):
    """ファイルサイズをKBで返す。"""
    return os.path.getsize(file_path) / 1024

def convert_with_imagemagick(heic_path, jpg_path):
    """ImageMagickを使用したHEICからJPGへの変換（フォールバック）。"""
    try:
        subprocess.run(
            ["magick", heic_path, "-quality", "85", jpg_path],
            check=True, capture_output=True, text=True
        )
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"ImageMagick failed for {heic_path}: {e.stderr}")
        return False
    except FileNotFoundError:
        logging.error("ImageMagick not installed. Install it with 'brew install imagemagick'.")
        return False

def convert_heic_to_jpg(heic_path, jpg_path, quality=85):
    """HEICをJPGに変換し、おおよその目標サイズに圧縮。"""
    try:
        # まずPillowを試す
        image = Image.open(heic_path)
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        # 初期品質でJPGとして保存
        image.save(jpg_path, "JPEG", quality=quality)
        
        # 目標サイズに近づけるために品質を調整
        current_size = get_file_size(jpg_path)
        low, high = 10, 100
        while low <= high and abs(current_size - target_size_kb) > 10:
            quality = (low + high) // 2
            image.save(jpg_path, "JPEG", quality=quality)
            current_size = get_file_size(jpg_path)
            if current_size > target_size_kb:
                high = quality - 1
            else:
                low = quality + 1
        return True
    except Exception as e:
        logging.error(f"Pillow failed for {heic_path}: {e}")
        # ImageMagickにフォールバック
        return convert_with_imagemagick(heic_path, jpg_path)

# 入力ディレクトリ内のすべてのHEICファイルを処理
for filename in os.listdir(input_dir):
    if filename.lower().endswith((".heic", ".heif")):
        heic_path = os.path.join(input_dir, filename)
        jpg_filename = os.path.splitext(filename)[0] + ".jpg"
        jpg_path = os.path.join(output_dir, jpg_filename)

        try:
            if convert_heic_to_jpg(heic_path, jpg_path):
                print(f"Converted {filename} to {jpg_filename}, size: {get_file_size(jpg_path):.2f} KB")
            else:
                print(f"Error processing {filename}: Conversion failed (check conversion_errors.log)")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            logging.error(f"General error for {heic_path}: {e}")

print("Batch conversion complete! Check conversion_errors.log for any issues.")
```

### 使用方法
1. **スクリプトの保存**:
   コードを`photo_compress.py`として`scripts/media/`ディレクトリに保存します。

2. **依存関係のインストール**:
   - Pillowがインストールされていることを確認：
     ```bash
     pip install --upgrade pillow
     ```
   - `libheif`をインストール：
     ```bash
     brew install libheif
     ```
   - オプションで、フォールバック用にImageMagickをインストール：
     ```bash
     brew install imagemagick
     ```

3. **スクリプトの実行**:
   ```bash
   python scripts/media/photo_compress.py ./assets/images/yuebei
   ```
   - これにより、`assets/images/yuebei`内のすべての`.heic`および`.heif`ファイルが処理されます。
   - 出力JPGは`assets/images/yuebei_compressed`に保存されます。
   - エラーは現在のディレクトリの`conversion_errors.log`に記録されます。

4. **ログの確認**:
   変換に失敗したファイルがある場合、`conversion_errors.log`で詳細なエラーメッセージを確認してください。

### 追加のトラブルシューティング
- **Pillowがまだ失敗する場合**:
  - `libheif`が正しくインストールおよびリンクされていることを確認：
    ```bash
    pkg-config --modversion libheif
    ```
    これが失敗する場合、`libheif`とPillowを再インストールします。
  - 単一ファイルを手動でテスト：
    ```python
    from PIL import Image
    img = Image.open("./assets/images/yuebei/IMG_5988.HEIC")
    print("Image opened successfully")
    ```
    これが失敗する場合、ファイルが破損しているか、サポートされていないHEICバリアントである可能性があります。

- **破損したファイル**:
  - ImageMagickで1つのファイルを手動で変換してみてください：
    ```bash
    magick ./assets/images/yuebei/IMG_5988.HEIC test.jpg
    ```
    これが失敗する場合、ファイルが破損している可能性が高いです。

- **ImageMagickフォールバック**:
  - Pillowが一貫して失敗する場合、スクリプトはImageMagick（インストール済みの場合）を使用しようとします。
  - より良い圧縮制御のために`jpegoptim`をインストール：
    ```bash
    brew install jpegoptim
    ```
    その後、スクリプト実行後に出力を圧縮：
    ```bash
    for i in ./assets/images/yuebei_compressed/*.jpg; do jpegoptim --size=500k "$i"; done
    ```

### 参考文献
- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
- [ImageMagick](https://imagemagick.org/)
- [libheif](https://github.com/strukturag/libheif)
- [jpegoptim](https://github.com/tjko/jpegoptim)

まだ問題が発生する場合は、`conversion_errors.log`の内容または新しいエラーメッセージを共有していただければ、さらにサポートを提供します！