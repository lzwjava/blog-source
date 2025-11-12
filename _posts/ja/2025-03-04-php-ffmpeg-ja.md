---
audio: false
generated: true
lang: ja
layout: post
title: PHPでのffmpegの使用
translated: true
type: note
---

### 主なポイント
- 「php-ffmpeg/php-ffmpeg」バージョン ~0.5 を使用するには、まずシステムにFFMpegをインストールし、その後Composerを使用してPHPライブラリをインストールする必要があるようです。
- 調査によると、オートロードファイルをインクルードし、`FFMpeg\FFMpeg` のインスタンスを作成してメディア操作を行う必要があります。必要に応じてバイナリパスを指定するオプションもあります。
- 基本的な操作には `open()`、`save()`、`frame()` などのメソッドを使用する傾向がありますが、バージョン固有の違いがある可能性があるため、詳細はGitHubのドキュメントを確認してください。

---

### インストール
まず、システムにFFMpegがインストールされていることを確認してください：
- Ubuntuでは、`sudo apt-get install ffmpeg` を使用します。
- macOSでは、`brew install ffmpeg` を使用します。
- Windowsでは、[このWebサイト](https://www.gyan.dev/ffmpeg/builds/)からダウンロードし、指示に従ってください。

次に、Composer経由でphp-FFMpegライブラリをインストールします：
```
composer require php-FFMpeg/php-FFMpeg:~0.5
```

### セットアップと使用方法
PHPスクリプトにオートロードファイルをインクルードします：
```php
require_once 'vendor/autoload.php';
```

`FFMpeg\FFMpeg` のインスタンスを作成します。FFMpegバイナリがシステムPATHにない場合は、必要に応じてパスを指定します：
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'binary' => '/path/to/FFMpeg',
    'ffprobe' => '/path/to/FFprobe'
));
```

メディアファイルを開き、以下のような操作を実行します：
- トランスコード: `$video->save('output.mp4', new FFMpeg\Format\Video\X264());`
- フレーム抽出: `$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5)); $frame->save('frame.jpg');`
- クリッピング: `$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20)); $clip->save('clip.mp4');`

詳細については、ライブラリのドキュメントを[GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)で参照してください。

---

### 調査ノート: php-FFMpeg/php-FFMpeg バージョン ~0.5 使用に関する包括的ガイド

このノートは、利用可能な情報に基づき、「php-FFMpeg/php-FFMpeg」ライブラリ、特にバージョン約0.5の使用について詳細に探求します。メディア操作のためにこのPHPライブラリを実装しようとしているユーザーが完全に理解できるよう、調査から得られたすべての関連する詳細を含め、直接の回答を拡張しています。

#### 背景とコンテキスト
「php-FFMpeg/php-FFMpeg」ライブラリは、FFMpegバイナリ用のPHPラッパーであり、ビデオおよびオーディオファイルのオブジェクト指向操作を可能にします。トランスコード、フレーム抽出、クリッピングなどのタスクをサポートし、メディア関連アプリケーションを扱う開発者にとって貴重なものです。バージョン指定「~0.5」は、0.5以上1.0未満の任意のバージョンを示し、リポジトリの0.xブランチで見つかる可能性が高い、古いPHPバージョンとの互換性を示唆しています。

現在の日付が2025年3月3日であることと、ライブラリの進化を考慮すると、バージョン0.5はレガシーサポートの一部である可能性があり、メインブランチでは現在PHP 8.0以上が必要とされています。このノートは、ユーザーがこのバージョンの制約内で作業していることを想定し、新しいリリースとの機能の違いを認識しています。

#### インストールプロセス
開始するには、ライブラリが操作にそのバイナリに依存するため、システムにFFMpegがインストールされている必要があります。インストール方法はオペレーティングシステムによって異なります：
- **Ubuntu**: パッケージマネージャー経由でインストールするために、コマンド `sudo apt-get install ffmpeg` を使用します。
- **macOS**: 簡単なインストールのために、Homebrewを `brew install ffmpeg` で利用します。
- **Windows**: [このWebサイト](https://www.gyan.dev/ffmpeg/builds/)からFFMpegバイナリをダウンロードし、提供された指示に従い、実行ファイルがシステムPATHでアクセス可能であるか、手動で指定されていることを確認します。

FFMpegのインストール後、PHPパッケージマネージャーであるComposer経由でphp-FFMpegライブラリをインストールします。コマンド `composer require php-FFMpeg/php-FFMpeg:~0.5` は、正しいバージョンが取得されることを保証します。このプロセスにより、プロジェクト内にライブラリとその依存関係を収容する `vendor` ディレクトリが作成され、Composerがシームレスな統合のためにオートローディングを管理します。

#### セットアップと初期化
インストール後、ライブラリのクラスへのアクセスを可能にするために、PHPスクリプトにオートロードファイルをインクルードします：
```php
require_once 'vendor/autoload.php';
```

ライブラリの使用を開始するために、`FFMpeg\FFMpeg` のインスタンスを作成します。作成メソッドは、特にFFMpegバイナリがシステムPATHにない場合に重要な設定を可能にします：
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'timeout' => 0,
    'thread_count' => 12,
    'binary' => '/path/to/your/own/FFMpeg',
    'ffprobe' => '/path/to/your/own/FFprobe'
));
```
この設定は、タイムアウト、スレッド数、明示的なバイナリパスの設定をサポートし、異なるシステム設定に対する柔軟性を高めます。デフォルトの設定はPATH内のバイナリを探しますが、手動指定は、特にカスタム環境での互換性を保証します。

#### コアの使用法と操作
ライブラリは、メディア操作のための流暢なオブジェクト指向インターフェースを提供します。メディアファイルを開くことから始めます：
```php
$video = $ff->open('input.mp4');
```
これは、ローカルファイルシステムパス、HTTPリソース、およびその他のFFMpegがサポートするプロトコルをサポートし、サポートされるタイプのリストは `ffmpeg -protocols` コマンドで利用可能です。

##### トランスコード
トランスコードは、メディアを異なる形式に変換することを含みます。フォーマットインスタンスとともに `save` メソッドを使用します：
```php
$format = new FFMpeg\Format\Video\X264();
$video->save('output.mp4', $format);
```
`X264` フォーマットは一例です。ライブラリは、`FFMpeg\Format\FormatInterface` を介して実装可能な様々なビデオおよびオーディオフォーマットをサポートし、特定のインターフェース（`VideoInterface` および `AudioInterface`）をそれぞれのメディアタイプに対して提供します。

##### フレーム抽出
フレームの抽出は、サムネイルや分析に有用です。以下のコードは5秒時点のフレームを抽出します：
```php
$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5));
$frame->save('frame.jpg');
```
`FFMpeg\Coordinate` の一部である `TimeCode` クラスは、正確なタイミングを保証し、画像抽出における精度のオプションを提供します。

##### クリッピング
ビデオの一部をクリップするには、開始時間と終了時間を指定します：
```php
$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20));
$clip->save('clip.mp4');
```
これは、元の品質とフォーマットを維持した新しいビデオセグメントを作成し、必要に応じて追加のフィルターを適用する機能を提供します。

#### 高度な機能と考慮事項
ライブラリは、ドキュメントで概説されている追加機能をサポートします：
- **オーディオ操作**: ビデオと同様に、オーディオは `FFMpeg\Media\Audio::save` でトランスコードでき、フィルターの適用、メタデータの追加、リサンプリングが可能です。
- **GIF作成**: アニメーションGIFは、`FFMpeg\Media\Gif::save` を使用して保存でき、オプションの期間パラメータを指定できます。
- **連結**: 同じコーデックの場合は `FFMpeg\Media\Concatenate::saveFromSameCodecs` を、異なるコーデックの場合は `saveFromDifferentCodecs` を使用して複数のメディアファイルを結合し、さらなる読書のためのリソースは[このリンク](https://trac.ffmpeg.org/wiki/Concatenate)、[このリンク](https://ffmpeg.org/ffmpeg-formats.html#concat-1)、および[このリンク](https://ffmpeg.org/ffmpeg.html#Stream-copy)にあります。
- **高度なメディア処理**: 複雑なフィルタリングとマッピングに有用な `-filter_complex` を使用した複数の入力/出力をサポートし、組み込みフィルターサポートを提供します。
- **メタデータ抽出**: メタデータには `FFMpeg\FFProbe::create` を使用し、`FFMpeg\FFProbe::isValid` でファイルを検証します（v0.10.0以降で利用可能、バージョン0.5にはこれがない可能性があります）。

`FFMpeg\Coordinate\AspectRatio`、`Dimension`、`FrameRate`、`Point`（v0.10.0以降で動的）、`TimeCode` などの座標は、メディアプロパティに対する正確な制御を提供しますが、動的ポイントなどの一部の機能はバージョン0.5では利用できない可能性があります。

#### バージョン固有の注意点
「~0.5」の指定を考慮すると、ライブラリは古いPHPバージョンをサポートする0.xブランチに沿っている可能性が高いです。GitHubリポジトリは、メインブランチでPHP 8.0以上を示し、0.xはレガシーサポート用です。ただし、正確なバージョン0.5の詳細はリリースで明示的に見つからなかったため、コミット履歴またはブランチコミットの一部である可能性があります。ユーザーは互換性を確認する必要があります。なぜなら、特定の座標タイプ（例：動的ポイント）などの新しい機能は、0.5を超えるバージョンを必要とする可能性があるからです。

#### ドキュメントとさらなる読書
Read the Docsページ（[Read the Docs](https://FFMpeg-PHP.readthedocs.io/en/latest/)）は空のように見えましたが、GitHubリポジトリ（[GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)）にはREADME内にAPIの使用法、フォーマット、例をカバーする包括的なドキュメントが含まれています。このレガシーバージョンに対する特定のオンラインドキュメントの欠如を考えると、これがバージョン0.5の主要なリソースです。

#### 表: 主要な操作とメソッドの概要

| 操作               | メソッド例                                      | 説明                                      |
|--------------------|------------------------------------------------|------------------------------------------|
| メディアファイルを開く | `$ff->open('input.mp4')`                           | 操作のためにメディアファイルを読み込む             |
| ビデオをトランスコード | `$video->save('output.mp4', new X264())`           | 指定された形式に変換する                    |
| フレームを抽出       | `$video->frame(TimeCode::fromSeconds(5))->save('frame.jpg')` | 指定された時間でフレームを抽出し、画像として保存 |
| ビデオをクリップ     | `$video->clip(TimeCode::fromSeconds(10), TimeCode::fromSeconds(20))->save('clip.mp4')` | 時間間でクリップを作成し、新しいファイルとして保存   |
| インスタンスを設定   | `FFMpeg::create(array('binary' => '/path/to/FFMpeg'))` | カスタムバイナリパスとオプションを設定する            |

この表は、コア機能を要約し、ユーザーがライブラリを実装しながら簡単に参照するのに役立ちます。

#### 予期しない詳細: レガシーバージョンの影響
予期しない側面は、バージョン0.5の潜在的な制限です。これは、古いPHPサポートのための0.xブランチ内での配置を考えると、現代的な機能へのアクセスを制限する可能性があります。例えば、v0.10.0で導入された動的座標ポイントなど、ユーザーが正確な機能を確認するためにブランチコミットをチェックする必要があり、新しいバージョンではすぐには明らかではない複雑さの層を追加します。

#### 結論
「php-FFMpeg/php-FFMpeg」バージョン ~0.5 の使用は、FFMpegのインストール、Composerを介したセットアップ、およびメディアタスクのためのオブジェクト指向APIの活用を含みます。トランスコードやフレーム抽出などの基本的な操作は簡単ですが、バージョン固有の違いは[GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)の0.xブランドキュメントを参照する必要があるかもしれません。この包括的なアプローチは、ユーザーがその力と潜在的なレガシー制約の両方を認識しながら、ライブラリを効果的に利用できることを保証します。

---

### 主要な引用文献
- [FFMpeg PHP Object Oriented Library Packagist](https://packagist.org/products/php-FFMpeg/php-FFMpeg)
- [PHP-FFMpeg GitHub Repository Documentation](https://github.com/PHP-FFMpeg/PHP-FFMpeg)
- [FFMpeg PHP Read the Docs Documentation](https://FFMpeg-PHP.readthedocs.io/en/latest/)
- [FFMpeg Download and Builds Website](https://www.gyan.dev/ffmpeg/builds/)
- [FFMpeg Concatenation Wiki Page](https://trac.ffmpeg.org/wiki/Concatenate)
- [FFMpeg Formats Documentation Page](https://ffmpeg.org/ffmpeg-formats.html#concat-1)
- [FFMpeg Command Line Tool Documentation](https://ffmpeg.org/ffmpeg.html#Stream-copy)