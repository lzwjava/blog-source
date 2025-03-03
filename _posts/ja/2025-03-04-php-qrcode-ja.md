---
audio: false
generated: true
lang: ja
layout: post
title: PHPでQRコードを生成するツール
translated: true
---

### 主要ポイント
- "endroid/qr-code" バージョン 2.2.2 を使用するためには、Composer を通じてインストールし、GD 拡張機能が有効であることを確認する必要があると考えられます。
- 研究によると、Builder クラスを使用してデータ、サイズ、ライターなどのパラメータを設定し、結果を保存または出力することで QR コードを生成できることが示されています。
- ライブラリが PNG、SVG などのフォーマットをサポートしていることが示唆されていますが、ロゴやラベルのオプションもあります。ただし、バージョン 2.2.2 については確認が必要です。

### インストール
まず、以下のコマンドを使用して Composer を通じてライブラリをインストールします：
```
composer require endroid/qr-code:2.2.2
```
PHP の設定で GD 拡張機能が有効であることを確認してください。これは画像生成に必要です。

### 使用例
バージョン 2.2.2 と互換性があると考えられる Builder クラスを使用した基本的な例です：
```php
use Endroid\QrCode\Builder\Builder;
use Endroid\QrCode\Encoding\Encoding;
use Endroid\QrCode\ErrorCorrectionLevel\ErrorCorrectionLevelHigh;
use Endroid\QrCode\Writer\PngWriter;

$url = 'https://example.com';
$qrCode = Builder::create()
    ->writer(new PngWriter())
    ->data($url)
    ->encoding(new Encoding('ISO-8859-1'))
    ->errorCorrectionLevel(new ErrorCorrectionLevelHigh())
    ->build();
$qrCode->saveToFile('qr_code.png');
```
これにより、URL の QR コードが生成され、PNG ファイルとして保存されます。Web 表示用にデータ URI として出力することもできます。

### 追加のメモ
ライブラリは PNG、SVG などのさまざまなライターをサポートし、ロゴやラベルの追加などのカスタマイズが可能です。ただし、バージョン 2.2.2 は古いため、現在のドキュメントに記載されている高度なロゴオプションなどの機能が利用できない場合があります。バージョン 2.2.2 に関するドキュメントは [GitHub](https://github.com/endroid/qr-code) で確認してください。

---

### アンケートノート: "endroid/qr-code" バージョン 2.2.2 の詳細ガイド

このノートは、PHP アプリケーションで QR コードを生成するために "endroid/qr-code" ライブラリのバージョン 2.2.2 を使用するための包括的なガイドを提供します。研究から得られたすべての関連情報を含め、特にライブラリに新しい開発者のための理解を深めるために構造化されています。内容は、テーブルを使用して明確にし、さらに参照するためのインライン URL を含むプロフェッショナルな記事を模倣しています。

#### はじめに
"endroid/qr-code" ライブラリは、製品追跡、ドキュメント管理、マーケティングなどのアプリケーションで広く使用される PHP ツールです。クエリで指定されたバージョン 2.2.2 は古いリリースであり、[Packagist](https://packagist.org/packages/endroid/qr-code) で放棄されていると記載されていますが、基本的な QR コード生成には機能します。このガイドでは、バージョン 2.2.2 との互換性を確保し、新しいバージョンとの違いを認識しながら、インストールと使用方法を説明します。

#### インストール手順
まず、Composer を使用してライブラリをインストールする必要があります。コマンドは以下の通りです：
```
composer require endroid/qr-code:2.2.2
```
これにより、バージョン 2.2.2 が正確に取得されます。画像生成に必要な GD 拡張機能が有効で、適切に設定されていることを確認してください。これを行わないと、ライブラリは視覚的な QR コードを生成できません。

| ステップ                  | 詳細                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| インストールコマンド       | `composer require endroid/qr-code:2.2.2`                                |
| PHP 要件       | GD 拡張機能が有効であることを確認（`phpinfo()` で確認）     |

研究によると、ライブラリの GitHub リポジトリ ([GitHub](https://github.com/endroid/qr-code)) と [Packagist](https://packagist.org/packages/endroid/qr-code) ページは、このインストール方法を確認していますが、バージョン 2.2.2 の特定のドキュメントは見つからず、一般的な使用パターンに依存していると考えられます。

#### 使用詳細
ライブラリは、QR コード生成のための 2 つの主要な方法を提供しています。Builder クラスを使用する方法と、QrCode クラスを直接使用する方法です。クエリの使用に焦点を当てているため、Builder 方法を推奨しますが、両方の方法を完全に説明します。

##### Builder クラスの使用
Builder クラスは、QR コードの設定にフルートインターフェースを提供します。最近のドキュメントの例に基づく基本的な実装は以下の通りです：
```php
use Endroid\QrCode\Builder\Builder;
use Endroid\QrCode\Encoding\Encoding;
use Endroid\QrCode\ErrorCorrectionLevel\ErrorCorrectionLevelHigh;
use Endroid\QrCode\Writer\PngWriter;

$url = 'https://example.com';
$qrCode = Builder::create()
    ->writer(new PngWriter())
    ->data($url)
    ->encoding(new Encoding('ISO-8859-1'))
    ->errorCorrectionLevel(new ErrorCorrectionLevelHigh())
    ->build();
$qrCode->saveToFile('qr_code.png');
```
このコードは、URL の QR コードを生成し、PNG フォーマットで ISO-8859-1 エンコーディングを使用し、高いエラーコレクションを使用します。データ URI として出力することもできます：
```php
$qrCodeDataUri = $qrCode->getDataUri();
```
これは、HTML に埋め込むのに便利です。例えば、`<img src="<?php echo $qrCodeDataUri; ?>">`。

ただし、バージョン 2.2.2 は古いため、`ErrorCorrectionLevelHigh` クラスなどが異なる名前で使用されている場合があります（古いバージョンでは `ErrorCorrectionLevel::HIGH` など）。Stack Overflow の投稿 ([Stack Overflow](https://stackoverflow.com/questions/40777377/endroid-qr-code)) に基づく研究によると、古いバージョンでは `setErrorCorrection('high')` などのメソッドが使用されていたため、2.2.2 の API を確認してください。

##### QrCode クラスの直接使用
より多くの制御を得るために、QrCode クラスを使用することもできます。例として以下のようなものがあります：
```php
use Endroid\QrCode\QrCode;
use Endroid\QrCode\Writer\PngWriter;

$qrCode = new QrCode('Life is too short to be generating QR codes');
$qrCode->setSize(300);
$qrCode->setMargin(10);
$writer = new PngWriter();
$result = $writer->write($qrCode);
$result->saveToFile('qrcode.png');
```
この方法はより冗長ですが、前景色や背景色などの細かい調整が可能です。バージョン 2.2.2 に関連するメソッドの利用可能性を確認してください。

#### 構成オプション
ライブラリは、以下の表に示すように、さまざまなライターをサポートしています。バージョン 2.2.2 に関しては確認が必要です。

| ライタークラス          | フォーマット   | メモ                                                                 |
|-----------------------|----------|----------------------------------------------------------------------|
| PngWriter             | PNG      | 圧縮レベルは設定可能、デフォルトは -1                           |
| SvgWriter             | SVG      | ベクターグラフィックスに適しており、圧縮オプションはありません                 |
| WebPWriter            | WebP     | 0-100、デフォルトは 80、Web 使用に適しています                          |
| PdfWriter             | PDF      | 単位は mm、デフォルト、印刷に適しています                                 |

エンコーディングオプションには、UTF-8（デフォルト）と ISO-8859-1 が含まれ、後者はバーコードスキャナーの互換性が推奨されます。丸めブロックサイズモード（マージン、拡大、縮小、なし）は読み取り性を向上させることができますが、バージョン 2.2.2 での利用可能性を確認してください。

#### 高度な機能と考慮事項
高度な使用、例えばロゴの埋め込みについては、Builder クラスが `logoPath()` や `logoResizeToWidth()` などのメソッドをサポートしています。ただし、これらがバージョン 2.2.2 以降の追加機能である可能性があるため、互換性をテストしてください。生成された QR コードの検証は可能ですが、パフォーマンスに影響を与えるため、デフォルトでは無効になっています。これは [GitHub](https://github.com/endroid/qr-code) からの詳細です。

[Packagist](https://packagist.org/packages/endroid/qr-code) でライブラリが放棄されていると記載されているため、セキュリティやメンテナンスに関する懸念が考えられますが、基本的な使用には依然として有効です。Symfony ユーザーにはバンドル ([GitHub](https://github.com/endroid/qr-code-bundle)) がありますが、これは一般的な PHP 使用を超えています。

#### バージョン固有のメモ
研究では、バージョン 2.2.2 の直接のドキュメントは見つからず、GitHub のタグにリストされていないため、古いリリースまたはタイポである可能性があります。現在のリポジトリにはバージョン 6.0.0 までのバージョンが表示されており、[Packagist](https://packagist.org/packages/endroid/qr-code) はこれを放棄していると記載していますが、endroid/qr-code を推奨しています。これは、名前変更やバージョン管理の問題を示唆しており、依存関係をロックし、アップグレードをテストすることを推奨します。

#### 結論
"endroid/qr-code" バージョン 2.2.2 を使用するには、Composer を通じてインストールし、GD 拡張機能を確認し、Builder または QrCode クラスを使用して QR コードを生成します。例は現在のドキュメントに基づいていますが、バージョン 2.2.2 の API の違いを確認してください。特に高度な機能については、ライブラリの GitHub ページと関連する Stack Overflow の議論を参照してください。

#### 主要な引用
- [QR コードジェネレータ GitHub リポジトリ](https://github.com/endroid/qr-code)
- [endroid/qr-code Packagist ページ](https://packagist.org/packages/endroid/qr-code)
- [PHP で埋め込み画像付き QR コードを作成する Medium 記事](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)
- [Endroid QR コード Stack Overflow 討論](https://stackoverflow.com/questions/40777377/endroid-qr-code)