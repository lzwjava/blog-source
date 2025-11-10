---
audio: false
generated: true
lang: ja
layout: post
title: UbuntuでのWebPからJPGへの変換
translated: true
type: note
---

UbuntuでWebPをJPGに変換するには、コマンドラインとGUIツールの両方でいくつかの優れた選択肢があります。

## コマンドラインツール

これらは単一ファイルまたはバッチ変換において、一般的に最も柔軟で効率的です。

### 1. ImageMagick

ImageMagickは強力なコマンドライン画像操作スイートで、広く利用可能です。

*   **インストール:**
    ```bash
    sudo apt update
    sudo apt install imagemagick
    ```
*   **単一ファイルの変換:**
    ```bash
    convert input.webp output.jpg
    ```
    または、ImageMagick v7+では `magick` を使用:
    ```bash
    magick input.webp output.jpg
    ```
*   **現在のディレクトリ内の複数ファイル（一括変換）:**
    ```bash
    mogrify -format JPEG *.webp
    ```
    これは現在のディレクトリ内のすべての `.webp` ファイルを同じファイル名で `.jpeg`（または `.jpg`）に変換します。変換されたファイルを別のディレクトリに保存したい場合:
    ```bash
    mkdir output_jpgs # 出力用ディレクトリを作成
    mogrify -format JPEG -path output_jpgs *.webp
    ```

### 2. `dwebp` (`libwebp` パッケージ)

`dwebp` はWebP画像をデコードするための専用ツールです。

*   **インストール:**
    ```bash
    sudo apt update
    sudo apt install webp
    ```
*   **単一ファイルの変換:**
    ```bash
    dwebp input.webp -o output.jpg
    ```
    出力に `.jpg` を指定しますが、`dwebp` はしばしばPPM形式で出力し、適切なJPEGに変換するためにImageMagickなどの別のツールを必要とすることがあります。ただし、一部の情報源では、単純なケースでは直接 `.jpg` を出力として使用できることが示唆されています。問題が発生した場合は、まずPNGに変換してからJPGに変換してください:
    ```bash
    dwebp input.webp -o output.png
    convert output.png output.jpg
    ```

### 3. `ffmpeg`

`ffmpeg` は主にビデオとオーディオ用ですが、画像形式にも非常に有能です。

*   **インストール:**
    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```
*   **単一ファイルの変換:**
    ```bash
    ffmpeg -i input.webp output.jpg
    ```
*   **複数ファイルの変換（一括変換）:**
    ```bash
    for file in *.webp; do ffmpeg -i "$file" "${file%.*}.jpg"; done
    ```
    このコマンドは、現在のディレクトリ内のすべての `.webp` ファイルを繰り返し処理し、同じ名前（例: `image.webp` が `image.jpg` になる）で `.jpg` に変換します。

## GUIツール

グラフィカルインターフェースを好む場合は、以下のいくつかの選択肢があります:

### 1. GIMP (GNU Image Manipulation Program)

GIMPはWebPをサポートする強力なオープンソースの画像編集ソフトです。

*   **インストール:**
    ```bash
    sudo apt update
    sudo apt install gimp
    ```
*   **変換方法:**
    1.  GIMPでWebP画像を開きます（ファイル > 開く）。
    2.  ファイル > 名前を付けてエクスポート に進みます。
    3.  「画像のエクスポート」ダイアログで、「ファイルタイプの選択（拡張子で）」ドロップダウンから「JPEG image」を選択します。
    4.  「エクスポート」をクリックし、必要に応じて品質設定を調整します。

### 2. XnView MP / XnConvert

これらはクロスプラットフォームの画像ビューアーおよびバッチコンバーターで、WebPを含む包括的な形式をサポートしています。

*   **インストール:**
    公式ウェブサイトから `.deb` パッケージをダウンロードし、`sudo dpkg -i <パッケージ名.deb>` またはグラフィカルなパッケージインストーラーを使用してインストールする必要があるかもしれません。
*   **変換方法（一般的な手順）:**
    1.  XnView MPまたはXnConvertを開きます。
    2.  変換したいWebP画像を追加します。
    3.  出力形式としてJPGを選択します。
    4.  （品質、サイズ変更などの）設定を調整します。
    5.  変換を開始します。

### 3. Converseen

ConverseenはWebPをサポートする無料のバッチ画像変換ソフトです。

*   **インストール:** Ubuntu Software Centerで通常見つかるか、リポジトリで利用可能な場合はapt経由でインストールできます。
*   **変換方法:** 画像の追加、出力形式の選択、変換のための直感的なGUIを備えています。

## どの方法を選ぶべきか？

*   **迅速な単一ファイルの変換や自動化タスクのスクリプト化には:** コマンドラインから `ffmpeg` または `ImageMagick` を使用します。これらは非常に効率的です。
*   **時折の変換で、ビジュアルなインターフェースと画像編集のより多くの制御を望む場合:** GIMPは優れた選択です。
*   **GUIとさまざまなオプションを使用して多くの画像を一括変換するには:** XnView MP/XnConvertまたはConverseenが優れています。

どの方法を選択する場合でも、まず必要なパッケージをインストールしてください。