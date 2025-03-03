---
audio: false
generated: true
lang: ja
layout: post
title: ffmpegをPHPで使用する
translated: true
---

### 重要ポイント
- "php-ffmpeg/php-ffmpeg" バージョン ~0.5 を使用するためには、まずシステムに FFMpeg をインストールし、次に Composer を使用して PHP ライブラリをインストールする必要があると考えられます。
- 研究によれば、オートロードファイルを含め、メディア操作のために `FFMpeg\FFMpeg` のインスタンスを作成し、必要に応じてバイナリパスを指定することが推奨されています。
- 基本操作には `open()`、`save()`、`frame()` のようなメソッドを使用することが多いですが、バージョンごとの違いがある可能性があるため、GitHub のドキュメントを確認することが重要です。

---

### インストール
まず、システムに FFMpeg がインストールされていることを確認してください：
- Ubuntu の場合は、`sudo apt-get install ffmpeg` を使用します。
- macOS の場合は、`brew install ffmpeg` を使用します。
- Windows の場合は、[このウェブサイト](https://www.gyan.dev/ffmpeg/builds/)からダウンロードし、指示に従ってください。

次に、Composer を使用して php-FFMpeg ライブラリをインストールします：
```sh
composer require php-FFMpeg/php-FFMpeg:~0.5
```

### セットアップと使用方法
PHP スクリプトにオートロードファイルを含めます：
```php
require_once 'vendor/autoload.php';
```

`FFMpeg\FFMpeg` のインスタンスを作成し、FFMpeg バイナリがシステム PATH にない場合はパスを指定します：
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'binary' => '/path/to/FFMpeg',
    'ffprobe' => '/path/to/FFprobe'
));
```

メディアファイルを開き、以下のような操作を行います：
- トランスコード: `$video->save('output.mp4', new FFMpeg\Format\Video\X264());`
- フレームの抽出: `$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5)); $frame->save('frame.jpg');`
- クリップ: `$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20)); $clip->save('clip.mp4');`

詳細については、ライブラリのドキュメントを [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg) でご確認ください。

---

### 調査ノート: php-FFMpeg/php-FFMpeg バージョン ~0.5 の包括的なガイド

このノートは、利用可能な情報に基づいて "php-FFMpeg/php-FFMpeg" ライブラリ、特にバージョン約 0.5 の使用について詳しく探求します。直接の回答を拡張し、すべての関連する詳細を含めることで、この PHP ライブラリをメディア操作に実装しようとするユーザーに対して包括的な理解を提供します。

#### 背景とコンテキスト
"php-FFMpeg/php-FFMpeg" ライブラリは、FFMpeg バイナリの PHP ラッパーであり、オブジェクト指向のビデオとオーディオファイルの操作を可能にします。トランスコード、フレーム抽出、クリップなどのタスクをサポートし、メディア関連のアプリケーションを作成する開発者にとって価値があります。バージョン指定 "~0.5" は、0.5 以上 1.0 未満のバージョンを示し、古い PHP バージョンとの互換性を示唆しています。

現在の日付は 2025 年 3 月 3 日であり、ライブラリの進化により、バージョン 0.5 はレガシー サポートの一部である可能性があります。メインブランチは PHP 8.0 以上を必要とすることが予想されます。このノートでは、このバージョンの制約内で作業しているユーザーを前提としており、新しいリリースとの機能の違いを認識しています。

#### インストール手順
まず、ライブラリは FFMpeg バイナリに依存しているため、システムに FFMpeg をインストールする必要があります。インストール方法は OS によって異なります：
- **Ubuntu**: パッケージマネージャーを使用して `sudo apt-get install ffmpeg` を実行します。
- **macOS**: Homebrew を使用して `brew install ffmpeg` を実行します。
- **Windows**: [このウェブサイト](https://www.gyan.dev/ffmpeg/builds/)から FFMpeg バイナリをダウンロードし、指示に従ってインストールします。システム PATH に実行ファイルがアクセス可能であることを確認し、必要に応じて手動で指定します。

FFMpeg のインストール後、Composer を使用して php-FFMpeg ライブラリをインストールします。PHP パッケージマネージャーである Composer を使用して `composer require php-FFMpeg/php-FFMpeg:~0.5` を実行すると、正しいバージョンが取得されます。このプロセスにより、プロジェクトに `vendor` ディレクトリが作成され、ライブラリとその依存関係が含まれ、Composer がオートロードを管理してシームレスな統合を実現します。

#### セットアップと初期化
インストール後、PHP スクリプトにオートロードファイルを含めることで、ライブラリのクラスにアクセスできます：
```php
require_once 'vendor/autoload.php';
```

ライブラリを使用するために `FFMpeg\FFMpeg` のインスタンスを作成します。作成メソッドは、特に FFMpeg バイナリがシステム PATH にない場合に重要な設定をサポートします：
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'timeout' => 0,
    'thread_count' => 12,
    'binary' => '/path/to/your/own/FFMpeg',
    'ffprobe' => '/path/to/your/own/FFprobe'
));
```
この設定により、タイムアウト、スレッド数、明示的なバイナリパスの設定が可能になり、異なるシステム設定に対する柔軟性が向上します。デフォルトの設定では、PATH にバイナリを探しますが、手動指定により互換性が確保され、特にカスタム環境で重要です。

#### コアの使用方法と操作
ライブラリは、メディア操作のためのフルート、オブジェクト指向インターフェースを提供します。メディアファイルを開くことから始めます：
```php
$video = $ff->open('input.mp4');
```
これは、ローカルファイルシステムのパス、HTTP リソース、FFMpeg がサポートする他のプロトコルをサポートし、サポートされているタイプの一覧は `ffmpeg -protocols` コマンドで確認できます。

##### トランスコード
トランスコードは、メディアを異なる形式に変換するプロセスです。`save` メソッドとフォーマットインスタンスを使用します：
```php
$format = new FFMpeg\Format\Video\X264();
$video->save('output.mp4', $format);
```
`X264` フォーマットはその一例であり、ライブラリは `FFMpeg\Format\FormatInterface` を実装するさまざまなビデオとオーディオフォーマットをサポートし、特定のインターフェースである `VideoInterface` と `AudioInterface` を使用してそれぞれのメディアタイプを実装します。

##### フレーム抽出
フレームの抽出は、サムネイルや分析に役立ちます。以下のコードは、5 秒のフレームを抽出します：
```php
$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5));
$frame->save('frame.jpg');
```
`TimeCode` クラスは `FFMpeg\Coordinate` の一部であり、画像抽出の正確性を確保し、オプションを提供します。

##### クリップ
ビデオの一部をクリップするには、開始時間と終了時間を指定します：
```php
$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20));
$clip->save('clip.mp4');
```
これにより、新しいビデオセグメントが作成され、オリジナルの品質とフォーマットが維持され、必要に応じて追加のフィルターを適用できます。

#### 高度な機能と考慮事項
ライブラリは、ドキュメントに記載されている追加の機能をサポートします：
- **オーディオ操作**: ビデオと同様に、オーディオは `FFMpeg\Media\Audio::save` を使用してトランスコードでき、フィルターを適用し、メタデータを追加し、リサンプリングできます。
- **GIF 作成**: `FFMpeg\Media\Gif::save` を使用してアニメーション GIF を保存でき、オプションの期間パラメータを指定できます。
- **連結**: `FFMpeg\Media\Concatenate::saveFromSameCodecs` を使用して同じコーデックの複数のメディアファイルを連結し、`saveFromDifferentCodecs` を使用して異なるコーデックを連結します。詳細については、[このリンク](https://trac.ffmpeg.org/wiki/Concatenate)、[このリンク](https://ffmpeg.org/ffmpeg-formats.html#concat-1)、[このリンク](https://ffmpeg.org/ffmpeg.html#Stream-copy) を参照してください。
- **高度なメディア処理**: `-filter_complex` を使用して複数の入力/出力をサポートし、複雑なフィルタリングとマッピングに役立ちます。内蔵フィルターのサポートもあります。
- **メタデータ抽出**: `FFMpeg\FFProbe::create` を使用してメタデータを取得し、`FFMpeg\FFProbe::isValid` を使用してファイルを検証します（v0.10.0 以降利用可能で、バージョン 0.5 ではこの機能が欠けている可能性があります）。

座標、例えば `FFMpeg\Coordinate\AspectRatio`、`Dimension`、`FrameRate`、`Point`（v0.10.0 以降動的）、`TimeCode` は、メディアのプロパティを正確に制御するために役立ちますが、バージョン 0.5 では動的ポイントのような機能が利用できない可能性があります。

#### バージョン固有の注意事項
"~0.5" の指定により、ライブラリは 0.x ブランチに対応している可能性が高く、古い PHP バージョンをサポートしています。GitHub リポジトリには、PHP 8.0 以上が必要なメインブランチがあり、0.x はレガシー サポートです。しかし、バージョン 0.5 の詳細がリリースに明示されていないため、コミット履歴やブランチコミットに含まれている可能性があります。ユーザーは互換性を確認し、バージョン 0.5 では利用できない新しい機能（例：動的ポイントのような座標タイプ）があることを認識する必要があります。

#### ドキュメントとさらに読む
Read the Docs ページ ([Read the Docs](https://FFMpeg-PHP.readthedocs.io/en/latest/)) は空だったため、GitHub リポジトリ ([GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)) に包括的なドキュメントが含まれています。README に API の使用方法、フォーマット、例が含まれており、バージョン 0.5 の主要なリソースです。

#### 表: 主要操作とメソッドの概要

| 操作               | メソッド例                                      | 説明                                      |
|-------------------------|----------------------------------------------------|-------------------------------------------------|
| メディアファイルを開く         | `$ff->open('input.mp4')`                           | メディアファイルを操作するために読み込み             |
| ビデオのトランスコード         | `$video->save('output.mp4', new X264())`           | 指定された形式に変換                    |
| フレームの抽出           | `$video->frame(TimeCode::fromSeconds(5))->save('frame.jpg')` | 指定した時間のフレームを抽出し、画像として保存 |
| ビデオのクリップ              | `$video->clip(TimeCode::fromSeconds(10), TimeCode::fromSeconds(20))->save('clip.mp4')` | 時間間隔のクリップを作成し、新しいファイルとして保存   |
| インスタンスの設定      | `FFMpeg::create(array('binary' => '/path/to/FFMpeg'))` | カスタムバイナリパスとオプションを設定            |

この表は、コア機能をまとめ、ライブラリを実装するユーザーが迅速に参照できるようにします。

#### 予期せぬ詳細: レガシー バージョンの影響
バージョン 0.5 が 0.x ブランチの一部である可能性があるため、古い PHP サポートに制限がある可能性があります。これにより、バージョン 0.10.0 で導入された動的座標ポイントのような新しい機能にアクセスできない可能性があり、ユーザーは正確な機能を確認するためにブランチコミットを確認する必要があります。これにより、新しいバージョンでは明らかでない複雑さが追加されます。

#### 結論
"php-FFMpeg/php-FFMpeg" バージョン ~0.5 を使用するには、FFMpeg をインストールし、Composer を使用してセットアップし、メディアタスクにオブジェクト指向 API を活用します。基本操作であるトランスコードやフレーム抽出は直感的ですが、バージョンごとの違いにより、[GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg) の 0.x ブランチのドキュメントを確認する必要がある場合があります。この包括的なアプローチにより、ユーザーはライブラリを効果的に利用し、その強力さとレガシー制約を認識することができます。

---

### 主要な引用
- [FFMpeg PHP オブジェクト指向ライブラリ Packagist](https://packagist.org/products/php-FFMpeg/php-FFMpeg)
- [PHP-FFMpeg GitHub リポジトリ ドキュメント](https://github.com/PHP-FFMpeg/PHP-FFMpeg)
- [FFMpeg PHP Read the Docs ドキュメント](https://FFMpeg-PHP.readthedocs.io/en/latest/)
- [FFMpeg ダウンロードとビルド ウェブサイト](https://www.gyan.dev/ffmpeg/builds/)
- [FFMpeg 連結 Wiki ページ](https://trac.ffmpeg.org/wiki/Concatenate)
- [FFMpeg フォーマット ドキュメント ページ](https://ffmpeg.org/ffmpeg-formats.html#concat-1)
- [FFMpeg コマンドラインツール ドキュメント](https://ffmpeg.org/ffmpeg.html#Stream-copy)