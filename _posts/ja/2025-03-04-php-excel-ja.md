---
audio: false
generated: true
lang: ja
layout: post
title: PHPExcelライブラリ
translated: true
---

### 主要ポイント
- "phpoffice/phpexcel": "^1.8" を使用するには、Composer を通じてインストールし、PHP コードを使用して Excel ファイルを読み書きする必要があると考えられます。
- 研究によると、このライブラリは非推奨になっているため、新しいプロジェクトでは PhpSpreadsheet を検討することをお勧めします。
- 証拠は、mbstring、XML、XMLWriter などの PHP 拡張機能が必要であることを示唆しています。

### インストール
始めるには、`composer.json` ファイルに `"phpoffice/phpexcel": "^1.8"` を追加し、`composer install` を実行します。これにより、Excel ファイルを PHP で操作するために必要なライブラリがダウンロードされます。

### 基本的な使用方法
Excel ファイルに書き込むためには:
- ライブラリを `require 'vendor/autoload.php';` でインクルードします。
- 新しい PHPExcel オブジェクトを作成します: `$objPHPExcel = new PHPExcel();`。
- セルの値を設定します、例: `$sheet->setCellValue('A1', 'value');`。
- 書き込み機能を使用してファイルを保存します、例: `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');` 後に `$writer->save('filename.xlsx');`。

Excel ファイルから読み込むためには:
- ファイルを `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');` で読み込みます。
- セルの値にアクセスします、例: `$cellValue = $sheet->getCell('A1')->getValue();`。

### 予期せぬ詳細
予期せぬ点は、PHPExcel が .xls と .xlsx などのさまざまなファイル形式をサポートし、読み込み時にファイルの種類を自動的に検出できるため、使用が簡単になっていることです。

---

### 調査ノート: "phpoffice/phpexcel": "^1.8" の使用に関する包括的なガイド

このノートでは、Composer 依存関係 "phpoffice/phpexcel": "^1.8" で指定された PHPExcel ライブラリ、特にバージョン 1.8 以降の使用について詳細に探求します。非推奨の状態であることを考慮し、このガイドでは現代的な代替案についても考慮し、初心者から上級者までのユーザーにとって包括的な理解を提供します。内容はインストール、使用方法、依存関係、追加のコンテキストをカバーし、研究から得られたすべての関連情報を含むように構成されています。

#### 背景とコンテキスト
PHPExcel は、特に .xls と .xlsx の Excel フォーマットのスプレッドシート ファイルを読み書きするための PHP ライブラリです。バージョン指定 "^1.8" はセマンティック バージョニングの範囲を示し、バージョン 1.8 から 2.0 未満のバージョンを意味します。ライブラリの履歴から、バージョン 1.8.1 が 2015 年にリリースされた最後のバージョンであることがわかります。しかし、研究によると、PHPExcel は 2017 年に正式に非推奨となり、2019 年にアーカイブされました。これにより、保守が行われていないため、セキュリティ上の問題が生じる可能性があるため、後継の PhpSpreadsheet に移行することを推奨しています。このコンテキストは、新しいプロジェクトに対する注意をユーザーに示すために重要ですが、このガイドは依然として指定されたバージョンを使用することを前提としています。

このライブラリの機能には、Excel ファイルの作成、読み込み、操作が含まれ、Excel 以外のフォーマットである CSV や HTML もサポートしています。これは PHPOffice プロジェクトの一部であり、現在は PhpSpreadsheet にフォーカスを移しており、改善された機能と PHP 標準準拠を提供しています。現在の日付が 2025 年 3 月 3 日であり、ライブラリがアーカイブされていることを考慮すると、ユーザーは特に新しい PHP バージョンやセキュリティ更新との互換性の制限について認識する必要があります。

#### インストール手順
"phpoffice/phpexcel": "^1.8" をインストールするには、Composer、PHP の依存関係管理ツールを利用します。手順は以下の通りです:
- `composer.json` ファイルの "require" セクションに依存関係を追加します: `"phpoffice/phpexcel": "^1.8"`。
- プロジェクトディレクトリで `composer install` コマンドを実行します。このコマンドはライブラリをダウンロードし、`vendor` ディレクトリに必要なファイルを更新します。

Composer のキャレット (^) 記法はセマンティック バージョニングに従い、バージョン 1.8、1.8.1、またはパッチ更新をインストールすることを保証し、互換性を破るバージョン（つまり 2.0 以上）はインストールしません。ライブラリの最後のリリースが 2015 年の 1.8.1 であったため、通常はバージョン 1.8.1 に解決されます。

研究によると、phpoffice/phpexcel の Packagist ページでは放棄されていると示されており、代わりに phpoffice/phpspreadsheet を推奨していますが、ユーザーのリクエストに従ってインストール可能です。

#### 基本的な使用方法: Excel に書き込む
インストール後、PHPExcel を使用するには、クラスの読み込みのためのオートロードファイルをインクルードし、スプレッドシート操作のためのクラスを利用します。以下に詳細な手順を示します:

- **オートロードファイルのインクルード:** PHP スクリプトの先頭で `require 'vendor/autoload.php';` を実行します。この行は、Composer でインストールされたすべてのライブラリ、PHPExcel を含む、自動的に読み込まれるようにします。これにより、2015 年のライブラリ構造に従って PSR-0 オートロードが利用されます。

- **新しい PHPExcel オブジェクトの作成:** 新しいスプレッドシートを `$objPHPExcel = new PHPExcel();` で初期化します。このオブジェクトは、複数のシートやプロパティを含むワークブック全体を表し、操作を可能にします。

- **シートの操作:** アクティブなシートにアクセスするには `$sheet = $objPHPExcel->getSheet(0);` を使用し、最初のシートを対象にします。新しいシートを作成するには `$sheet = $objPHPExcel->createSheet();` を使用します。シートは 0 から始まるため、`getSheet(0)` は最初のシートを対象にします。

- **セルの値の設定:** セルに値を設定するには `setCellValue` メソッドを使用します。例: `$sheet->setCellValue('A1', 'Hello');`。このメソッドはセル参照（例: 'A1'）と挿入する値（テキスト、数値、または式）を取ります。

- **ファイルの保存:** 保存するには、希望する形式のライターを作成します。Excel 2007 以降 (.xlsx) の場合は `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');` を使用し、その後 `$writer->save('filename.xlsx');` で保存します。他の形式には 'Excel5'（.xls、Excel 95）や 'CSV'（カンマ区切り値）があります。

書き込みの例スクリプトは以下の通りです:
```php
require 'vendor/autoload.php';
$objPHPExcel = new PHPExcel();
$sheet = $objPHPExcel->getSheet(0);
$sheet->setCellValue('A1', 'Hello');
$sheet->setCellValue('B1', 'World');
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');
$writer->save('hello_world.xlsx');
```
このスクリプトは、A1 に "Hello"、B1 に "World" を含む簡単な Excel ファイルを作成します。

#### 基本的な使用方法: Excel から読み込む
Excel ファイルから読み込む手順は似ていますが、ファイルの読み込みから始まります:
- **ファイルの読み込み:** 既存の Excel ファイルを `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');` で読み込みます。IOFactory はファイルの種類を自動的に検出しますが、明示的にリーダーを指定することもできます。例: `$objReader = PHPExcel_IOFactory::createReader('Excel2007'); $objPHPExcel = $objReader->load('filename.xlsx');`。

- **シートとセルへのアクセス:** 読み込み後、シートにアクセスします。例: `$sheet = $objPHPExcel->getSheet(0);`。セルの値を取得するには `$cellValue = $sheet->getCell('A1')->getValue();` を使用します。これにより、指定されたセルの内容が返されます。

読み込みの例は以下の通りです:
```php
require 'vendor/autoload.php';
$objPHPExcel = PHPExcel_IOFactory::load('hello_world.xlsx');
$sheet = $objPHPExcel->getSheet(0);
$cellValue = $sheet->getCell('A1')->getValue();
echo $cellValue; // "Hello" を出力
```
このスクリプトは A1 の値を読み込み、基本的な取得を示します。

#### 依存関係と要件
PHPExcel は、操作に必要な特定の PHP 要件と拡張機能があります:
- **PHP バージョン:** Packagist メタデータによると、PHP 5.2 または 7.0 以降が必要です。2025 年 3 月 3 日の現在、ほとんどの現代的な PHP インストールはこの要件を満たしているでしょうが、古いセットアップでは更新が必要になるかもしれません。
- **拡張機能:** ライブラリは `ext-mbstring`、`ext-XML`、`ext-XMLWriter` に依存しており、これらが PHP 設定で有効になっている必要があります。これらの拡張機能は文字エンコーディング、XML パース、XML 書き込みをそれぞれ処理し、Excel ファイル操作に不可欠です。

ユーザーは `phpinfo()` を使用してこれらの拡張機能がアクティブかどうかを確認し、`php.ini` ファイルを確認して互換性の問題が生じないようにする必要があります。

#### 追加の機能とフォーマット
基本的な読み書きの他に、PHPExcel はさまざまなファイル形式をサポートするという予期せぬ詳細があります。ライブラリは以下を処理できます:
- Excel 2007 (.xlsx) を 'Excel2007' ライター/リーダーで。
- Excel 95 (.xls) を 'Excel5' で。
- CSV ファイルを 'CSV' で。
- HTML を 'HTML' で。

保存する際にはライターの種類を指定し、読み込み時には IOFactory が自動的に検出することが多いですが、信頼性を高めるために明示的なリーダーを使用することもできます。例として、.xls 形式で保存するには:
```php
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel5');
$writer->save('filename.xls');
```
この柔軟性は、レガシー システムや特定のフォーマット要件に役立ちますが、特に古い Excel バージョンの場合にはフォーマット固有の制限があることに注意してください。

#### 非推奨と移行のアドバイス
重要な点は PHPExcel の非推奨です。研究によると、2019 年にアーカイブされ、2015 年が最後の更新であり、保守されていないため、セキュリティ上の脆弱性や PHP バージョン 7.0 以降の互換性に関する懸念が生じます。GitHub リポジトリと Packagist ページの両方で、PhpSpreadsheet に移行することを推奨しています。

ユーザーにとってこれは以下を意味します:
- 既存の PHPExcel 1.8 を使用するプロジェクトについては、セキュリティと互換性のテストを行いながら慎重に続行します。
- 新しいプロジェクトについては、PhpSpreadsheet を強く検討し、移行ツールが利用可能であることを確認します（PhpSpreadsheet ドキュメントの [PHPExcel からの移行](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/) を参照）。

このアドバイスは特に現在の日付に基づいており、ユーザーが現代的でサポートされているライブラリに対応することを確保します。

#### ドキュメントとさらに学ぶ
より深い探求には、PHPExcel の公式ドキュメントが GitHub リポジトリの Documentation フォルダにありますが、アクセスにはファイルのダウンロードが必要になる場合があります。オンラインでは、SitePoint のチュートリアル ([PHPExcel を使用して Excel ファイルとチャートを生成する](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)) が実践的な例を提供し、チャートやフォーマットをカバーしています。Stack Overflow のスレッドもコミュニティの洞察を提供しますが、ライブラリの状態を考慮して古い回答には注意が必要です。

#### 比較表: PHPExcel vs. PhpSpreadsheet
決定を助けるために、以下に研究に基づく主要な違いを示す比較表を示します:

| 特徴                  | PHPExcel (1.8)                     | PhpSpreadsheet                  |
|--------------------------|------------------------------------|---------------------------------|
| 最終更新              | 2015                              | 2025 現在アクティブ             |
| 名前空間               | ない、ルート名前空間                | あり、PSR-4 準拠            |
| 保守状況               | 非推奨、2019 年アーカイブ         | アクティブに保守             |
| PHP バージョンサポート      | 7.0 まで                         | PHP 7.4+                        |
| ファイル形式サポート      | Excel、CSV、HTML、など            | 向上、ODS、PDF を含む            |
| パフォーマンス              | 中程度、メモリ集約型        | 最適化、スケーラブル             |

この表は、現代的なニーズに対応するために PhpSpreadsheet に移行することを強調していますが、PHPExcel は引き続きレガシー目的で機能します。

#### 結論
"phpoffice/phpexcel": "^1.8" を使用するには、Composer を通じてインストールし、Excel 操作のためにクラスを利用し、必要な PHP 拡張機能を確認します。機能的ですが、非推奨の状態であるため慎重に使用し、新しいプロジェクトには PhpSpreadsheet を推奨します。このガイドは、例、依存関係、追加のリソースを含む包括的な開始点を提供します。