---
audio: false
generated: true
lang: ja
layout: post
title: QRコード生成PHPツール
translated: true
type: note
---

### 主なポイント
- 「endroid/qr-code」バージョン2.2.2を使用するには、Composer経由でインストールし、GD拡張機能が有効になっていることを確認する必要があるようです。
- 調査によると、Builderクラスを使用してデータ、サイズ、ライターなどのパラメータを設定し、QRコードを生成して結果を保存または出力できることが示唆されています。
- このライブラリはPNG、SVGなどの形式と、ロゴやラベルのオプションをサポートしている可能性が高いですが、バージョン2.2.2については確認が必要です。

### インストール
まず、以下のコマンドでComposerを使用してライブラリをインストールします：
```
composer require endroid/qr-code:2.2.2
```
画像生成に必要であるため、PHP設定でGD拡張機能が有効になっていることを確認してください。

### 使用例
以下は、バージョン2.2.2と互換性がある可能性が高いBuilderクラスを使用した基本的な例です：
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
これはURL用のQRコードを作成し、PNGファイルとして保存します。Web表示用にデータURIとして出力することもできます。

### 追加の注意点
このライブラリは様々なライター（PNG、SVGなど）をサポートし、ロゴやラベルの追加などのカスタマイズが可能です。ただし、バージョン2.2.2は古いため、現在のドキュメントにある高度なロゴオプションなどの機能は利用できない可能性があります。特定のバージョンに関するドキュメントは[GitHub](https://github.com/endroid/qr-code)で確認してください。

---

### 調査ノート：「endroid/qr-code」バージョン2.2.2の使用に関する詳細ガイド

このノートは、PHPアプリケーションでQRコードを生成するための「endroid/qr-code」ライブラリ（バージョン2.2.2）の使用に関する包括的なガイドを提供します。直接の回答を拡張し、調査から得られたすべての関連詳細を含めることで、特にライブラリに不慣れな開発者にとって徹底的な理解を保証します。内容は専門的な記事を模倣して構成され、明確さのための表と参照用のインラインURLが含まれています。

#### はじめに
「endroid/qr-code」ライブラリは、製品追跡、文書管理、マーケティングなどのアプリケーションで広く使用されているPHPのQRコード生成ツールです。クエリで指定されたバージョン2.2.2は古いリリースですが、[Packagist](https://packagist.org/packages/endroid/qr-code)で放棄済みと記載されているにもかかわらず、基本的なQRコード生成には機能します。このガイドは、インストールと使用法を概説し、バージョン2.2.2との互換性を確保することに焦点を当て、新しいバージョンとの潜在的な違いを認識しています。

#### インストール手順
開始するには、PHPパッケージマネージャーであるComposer経由でライブラリをインストールする必要があります。コマンドは以下の通りです：
```
composer require endroid/qr-code:2.2.2
```
これにより、正確にバージョン2.2.2が取得されます。重要な要件は、画像生成に不可欠なGD拡張機能が有効かつ設定されていることです。これがないと、ライブラリは視覚的なQRコードを生成できません。

| ステップ                  | 詳細                                                                 |
|---------------------------|---------------------------------------------------------------------|
| インストールコマンド       | `composer require endroid/qr-code:2.2.2`                           |
| PHP要件                   | GD拡張機能が有効であることを確認（`phpinfo()`で確認）               |

調査によると、ライブラリのGitHubリポジトリ（[GitHub](https://github.com/endroid/qr-code)）と[Packagist](https://packagist.org/packages/endroid/qr-code)ページはこのインストール方法を確認しており、特定のバージョン2.2.2のドキュメントは見つからず、一般的な使用パターンに依存することが示唆されています。

#### 使用詳細
このライブラリは、QRコード生成のための2つの主要な方法、Builderクラスの使用とQrCodeクラスの直接使用を提供します。クエリの使用法への焦点を考慮し、Builderアプローチはそのシンプルさから推奨されますが、完全を期すために両方がここで詳細に説明されています。

##### Builderクラスの使用
Builderクラスは、QRコードを設定するための流暢なインターフェースを提供します。最近のドキュメントの例に基づくと、基本的な実装は以下の通りです：
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
このコードは、URL用のQRコードを作成し、PNG形式、バーコードスキャナーの互換性向上のためのISO-8859-1エンコーディング、高誤り訂正レベルを使用します。データURIとして出力することもできます：
```php
$qrCodeDataUri = $qrCode->getDataUri();
```
これはHTMLに埋め込む場合（例：`<img src="<?php echo $qrCodeDataUri; ?>">`）に便利です。

ただし、バージョン2.2.2は古いため、`ErrorCorrectionLevelHigh`などのクラスは異なる名前（例：古いバージョンでは`ErrorCorrectionLevel::HIGH`）である可能性があります。Stack Overflowの投稿（[Stack Overflow](https://stackoverflow.com/questions/40777377/endroid-qr-code)）からの調査によると、古いバージョンでは`setErrorCorrection('high')`のようなメソッドを使用していたため、2.2.2のAPIを確認してください。

##### QrCodeクラスの直接使用
より制御が必要な場合は、例に見られるようにQrCodeクラスを使用できます：
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
この方法はより冗長ですが、前景色と背景色の設定などの微調整が可能で、バージョン2.2.2に関連する可能性があります。再度、メソッドの可用性についてはドキュメントを確認してください。

#### 設定オプション
このライブラリは、以下の表に詳細を示すように、さまざまな出力形式に対応するさまざまなライターをサポートしています。これは現在のドキュメントに基づいており、バージョン2.2.2については確認が必要です：

| ライタークラス          | 形式     | 注意点                                                               |
|-------------------------|----------|----------------------------------------------------------------------|
| PngWriter               | PNG      | 圧縮レベル設定可能、デフォルトは-1                                  |
| SvgWriter               | SVG      | ベクターグラフィックスに適し、圧縮オプションなし                   |
| WebPWriter              | WebP     | 品質0-100、デフォルト80、Web使用に適している                        |
| PdfWriter               | PDF      | 単位はmm、デフォルト、印刷に適している                             |

エンコーディングオプションにはUTF-8（デフォルト）とISO-8859-1が含まれ、後者はバーコードスキャナーの互換性のために推奨されます。丸いブロックサイズモード（マージン、拡大、縮小、なし）は読みやすさを向上させることができますが、2.2.2での可用性は確認が必要です。

#### 高度な機能と考慮事項
ロゴの埋め込みなどの高度な使用法については、BuilderクラスはMedium記事（[Medium](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)）で見られる`logoPath()`や`logoResizeToWidth()`などのメソッドをサポートしています。ただし、これらは2.2.2以降の追加機能である可能性があるため、互換性をテストしてください。生成されたQRコードの検証は可能ですが、パフォーマンスに影響し、デフォルトでは無効になっています。これは[GitHub](https://github.com/endroid/qr-code)からの詳細です。

[Packagist](https://packagist.org/packages/endroid/qr-code)でのライブラリの放棄済みメモを考慮すると、潜在的なセキュリティやメンテナンスの懸念は留意に値しますが、基本的な使用には引き続き有効です。Symfonyユーザー向けにはバンドル（[GitHub](https://github.com/endroid/qr-code-bundle)）がありますが、それは一般的なPHP使用の範囲外です。

#### バージョン固有の注意点
調査では、バージョン2.2.2の直接のドキュメントは見つからず、GitHubのタグにはリストされていませんでした。これは、古いリリースまたはタイポである可能性を示唆しています。現在のリポジトリはバージョン6.0.0までを示しており、[Packagist](https://packagist.org/packages/endroid/qr-code)はそれを放棄済みとしてリストし、endroid/qr-codeを推奨していますが、これは同じパッケージであるため混乱を招きます。これは潜在的な名前変更またはバージョン管理の問題を示しているため、ユーザーは依存関係をロックし、アップグレードをテストする必要があります。

#### 結論
「endroid/qr-code」バージョン2.2.2の使用には、Composer経由でのインストール、GD拡張機能の確保、BuilderまたはQrCodeクラスを使用したQRコードの生成が含まれます。例は現在のドキュメントに基づいていますが、特に高度な機能については2.2.2のAPIの違いを確認してください。詳細については、ライブラリのGitHubページと関連するStack Overflowの議論を参照してください。

#### 主要な引用文献
- [QR Code Generator GitHub Repository](https://github.com/endroid/qr-code)
- [endroid/qr-code Packagist Page](https://packagist.org/packages/endroid/qr-code)
- [Creating QR Codes with Embedded Images Medium Article](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)
- [Endroid QR Code Stack Overflow Discussion](https://stackoverflow.com/questions/40777377/endroid-qr-code)