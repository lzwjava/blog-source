---
audio: false
generated: true
lang: ja
layout: post
title: PHPExcelライブラリ
translated: true
type: note
---

### 主なポイント
- "phpoffice/phpexcel": "^1.8" を使用するには、Composer 経由でインストールし、PHP コードで Excel ファイルの読み書きを行う必要があるようです。
- 調査によると、このライブラリは非推奨となっているため、新規プロジェクトでは PhpSpreadsheet の使用を検討すべきです。
- 証拠から、mbstring、XML、XMLWriter などの PHP 拡張機能が必要である可能性が高いです。

### インストール
始めるには、`composer.json` ファイルに `"phpoffice/phpexcel": "^1.8"` を追加し、`composer install` を実行します。これにより、PHP で Excel ファイルを操作するために不可欠なライブラリがダウンロードされます。

### 基本的な使用方法
Excel ファイルへの書き込み:
- ライブラリを `require 'vendor/autoload.php';` でインクルードします。
- 新しい PHPExcel オブジェクトを作成: `$objPHPExcel = new PHPExcel();`
- セルに値を設定。例: `$sheet->setCellValue('A1', 'value');`
- ライターを使用してファイルを保存。例: `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');` の後、`$writer->save('filename.xlsx');` を実行。

Excel ファイルからの読み込み:
- `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');` でファイルをロード。
- セルの値にアクセス。例: `$cellValue = $sheet->getCell('A1')->getValue();`

### 予期せぬ詳細点
予想外の側面は、PHPExcel が .xls や .xlsx など様々なファイル形式をサポートし、読み取り時にファイルタイプを自動検出するため、使用が簡素化されることです。

---

### 調査ノート: "phpoffice/phpexcel": "^1.8" 使用包括的ガイド

このノートは、Composer の依存関係 "phpoffice/phpexcel": "^1.8" で指定された、特にバージョン 1.8 以上の PHPExcel ライブラリの使用について詳細に探求します。その非推奨ステータスを考慮し、このガイドは現代的な代替案に関する考慮事項も強調し、初心者と上級ユーザーの両方に対する完全な理解を保証します。内容は、インストール、使用方法、依存関係、および追加の文脈をカバーするように構成されており、調査から得られたすべての関連する詳細が含まれています。

#### 背景と文脈
PHPExcel は、スプレッドシートファイル、特に .xls や .xlsx などの Excel 形式の読み書きのために設計された PHP ライブラリです。バージョン指定 "^1.8" はセマンティックバージョニングの範囲を示し、2.0 未満の 1.8 以降のバージョンを意味します。これは、ライブラリの履歴を考慮すると、最新版として 2015 年にリリースされたバージョン 1.8.1 を指します。しかし、調査によると、PHPExcel は 2017 年に公式に非推奨となり、2019 年にアーカイブされ、メンテナンスの欠如と潜在的なセキュリティ問題から、後継である PhpSpreadsheet への移行が推奨されています。この文脈は、ユーザーにとって重要であり、新規プロジェクトには注意が必要であることを示唆していますが、このガイドは要求に応じて指定されたバージョンの使用に焦点を当てます。

ライブラリの機能には、Excel ファイルの作成、読み取り、操作が含まれ、Excel 以外にも CSV や HTML などの形式をサポートします。これは PHPOffice プロジェクトの一部でしたが、その後は焦点を PhpSpreadsheet に移し、改善された機能と PHP 標準への準拠を提供しています。現在の日付が 2025年3月3日であることと、ライブラリがアーカイブ済みステータスであることを考慮すると、ユーザーは特に新しい PHP バージョンとセキュリティ更新に関するその制限を認識すべきです。

#### インストールプロセス
"phpoffice/phpexcel": "^1.8" をインストールするには、PHP の依存関係マネージャーである Composer を活用します。手順は以下の通りです:
- 依存関係を `composer.json` ファイルの "require" セクションに追加: `"phpoffice/phpexcel": "^1.8"`
- プロジェクトディレクトリで `composer install` コマンドを実行します。このコマンドはライブラリをダウンロードし、必要なファイルで `vendor` ディレクトリを更新します。

Composer のキャレット (^) 表記はセマンティックバージョニングに従い、バージョン 1.8、1.8.1、または任意のパッチ更新がインストールされますが、互換性を破るバージョン (すなわち、2.0 以上) はインストールされません。ライブラリの最終リリースが 2015 年の 1.8.1 であることを考慮すると、これは通常バージョン 1.8.1 に解決されます。

調査により、phpoffice/phpexcel の Packagist ページはそれを放棄されたものとしてリストし、代わりに phpoffice/phpspreadsheet を提案していますが、ユーザーの要求に合わせてインストール可能なままであることが確認されています。

#### 基本的な使用方法: Excel への書き込み
インストール後、PHPExcel の使用には、クラスローディング用のオートロードファイルをインクルードし、そのクラスをスプレッドシート操作に利用することが含まれます。詳細な内訳は以下の通りです:

- **オートロードファイルのインクルード:** PHP スクリプトを `require 'vendor/autoload.php';` で開始します。この行は、Composer でインストールされたすべてのライブラリ (PHPExcel を含む) が、2015 年時点のライブラリ構造に従った PSR-0 オートローディングを活用して自動的にロードされることを保証します。

- **新しい PHPExcel オブジェクトの作成:** `$objPHPExcel = new PHPExcel();` で新しいスプレッドシートを初期化します。このオブジェクトはワークブック全体を表し、複数のシートとプロパティを可能にします。

- **シートの操作:** 最初のシートには `$sheet = $objPHPExcel->getSheet(0);` を使用してアクティブシートにアクセスするか、`$sheet = $objPHPExcel->createSheet();` で新しいシートを作成します。シートは 0 から始まるインデックスであるため、`getSheet(0)` は最初のシートを対象とします。

- **セル値の設定:** `setCellValue` メソッドを使用してセルに値を設定します。例: `$sheet->setCellValue('A1', 'Hello');`。このメソッドはセル参照 ('A1' など) と挿入する値 (テキスト、数値、または数式) を取ります。

- **ファイルの保存:** 保存するには、希望の形式用のライターを作成します。Excel 2007 以降 (.xlsx) の場合、`$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');` を使用します。その後、`$writer->save('filename.xlsx');` で保存します。その他の形式には、.xls (Excel 95) 用の 'Excel5' や、カンマ区切り値用の 'CSV' などがあります。

書き込み用のスクリプト例は以下のようになります:
```php
require 'vendor/autoload.php';
$objPHPExcel = new PHPExcel();
$sheet = $objPHPExcel->getSheet(0);
$sheet->setCellValue('A1', 'Hello');
$sheet->setCellValue('B1', 'World');
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');
$writer->save('hello_world.xlsx');
```
これは、A1 に "Hello"、B1 に "World" を持つ簡単な Excel ファイルを作成します。

#### 基本的な使用方法: Excel からの読み込み
Excel ファイルからの読み込みは同様のパターンに従いますが、ファイルのロードから始まります:
- **ファイルのロード:** 既存の Excel ファイルをロードするには `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');` を使用します。IOFactory はファイルタイプを自動検出できますが、明示的なタイプ指定には、例: `$objReader = PHPExcel_IOFactory::createReader('Excel2007'); $objPHPExcel = $objReader->load('filename.xlsx');` のようにリーダーを指定できます。

- **シートとセルへのアクセス:** ロード後、以前と同様にシートにアクセスします。例: `$sheet = $objPHPExcel->getSheet(0);`。指定されたセルの内容を返す `$cellValue = $sheet->getCell('A1')->getValue();` でセル値を取得します。

読み込み用の例:
```php
require 'vendor/autoload.php';
$objPHPExcel = PHPExcel_IOFactory::load('hello_world.xlsx');
$sheet = $objPHPExcel->getSheet(0);
$cellValue = $sheet->getCell('A1')->getValue();
echo $cellValue; // "Hello" を出力
```
これは A1 からの値を読み取り、基本的な取得を示します。

#### 依存関係と要件
PHPExcel には、操作に必要な特定の PHP 要件と拡張機能があります:
- **PHP バージョン:** Packagist メタデータによると、PHP 5.2 または 7.0 以上が必要です。現在の日付を考慮すると、ほとんどの現代的な PHP インストール環境はこれを満たすべきですが、古いセットアップでは更新が必要な場合があります。
- **拡張機能:** ライブラリは `ext-mbstring`、`ext-XML`、`ext-XMLWriter` に依存しており、これらは PHP 設定で有効にする必要があります。これらの拡張機能は、Excel ファイル操作に不可欠な、文字列エンコーディング、XML 解析、および XML 書き込みを扱います。

ユーザーは、`phpinfo()` を使用するか `php.ini` ファイルをチェックしてこれらの拡張機能がアクティブであることを確認し、互換性の問題が発生しないようにすべきです。

#### 追加機能と形式
基本的な読み書きを超えて、PHPExcel は様々なファイル形式をサポートしており、これは Excel にのみ精通しているユーザーにとって予想外の詳細点です。ライブラリは以下を扱うことができます:
- 'Excel2007' ライター/リーダー経由の Excel 2007 (.xlsx)
- 'Excel5' 経由の Excel 95 (.xls)
- 'CSV' 経由の CSV ファイル
- 'HTML' 経由の HTML

保存時にはライタータイプを指定します。読み取り時には、IOFactory が自動検出することが多いですが、信頼性のために明示的なリーダーを使用できます。例えば、.xls として保存するには:
```php
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel5');
$writer->save('filename.xls');
```
この柔軟性は、レガシーシステムや特定の形式のニーズに有用ですが、ユーザーは特に古い Excel バージョンでの形式固有の制限に注意すべきです。

#### 非推奨化と移行アドバイス
重要な点は、PHPExcel の非推奨化です。調査によると、それは 2019 年にアーカイブされ、最後の更新は 2015 年であり、もはやメンテナンスされていません。これは、セキュリティ脆弱性と、PHP 7.0 以降、特に PHP 8.x のような現代的な標準との互換性に関する懸念を提起します。GitHub リポジトリと Packagist ページは両方とも、名前空間、PSR 準拠、およびアクティブな開発を提供する PhpSpreadsheet への移行を推奨しています。

ユーザーにとって、これは以下を意味します:
- PHPExcel 1.8 を使用する既存のプロジェクトについては、セキュリティと互換性のテストを確実に行い、注意を払って継続します。
- 新規プロジェクトについては、PhpSpreadsheet のドキュメント ([Migration from PHPExcel](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/)) に記載されている移行ツールを利用して、強く PhpSpreadsheet を検討すべきです。

このアドバイスは、現在の日付を考慮すると特に関連性が高く、ユーザーが現代的なサポートされたライブラリに沿うことを保証します。

#### ドキュメントとさらなる学習
より深い探求のために、PHPExcel の公式ドキュメントは GitHub リポジトリの Documentation フォルダ内で利用可能ですが、開発者ドキュメント DOC のようなファイルのダウンロードが必要な場合があります。オンラインでは、SitePoint のチュートリアル ([Generate Excel Files and Charts with PHPExcel](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)) のようなチュートリアルが実用的な例を提供し、基本的な使用法を超えたチャートやフォーマットをカバーしています。Stack Overflow のスレッドもコミュニティの洞察を提供しますが、ライブラリのステータスを考慮して古い回答には注意すべきです。

#### 比較表: PHPExcel vs. PhpSpreadsheet
意思決定を支援するために、調査に基づく主な違いを強調した比較表を以下に示します:

| 機能                      | PHPExcel (1.8)                     | PhpSpreadsheet                  |
|--------------------------|------------------------------------|---------------------------------|
| 最終更新                  | 2015                              | アクティブ (2025年現在)         |
| 名前空間                  | なし、ルート名前空間               | あり、PSR-4 準拠               |
| メンテナンスステータス    | 非推奨、2019 年にアーカイブ        | アクティブにメンテナンス        |
| PHP バージョンサポート    | 7.0 まで                           | PHP 7.4+                        |
| ファイル形式サポート      | Excel, CSV, HTML など              | ODS, PDF を含む拡張            |
| パフォーマンス            | 中程度、メモリ集約的               | 最適化、スケーラブル            |

この表は、現代的なニーズには PhpSpreadsheet への移行を強調しますが、PHPExcel はレガシーな目的では機能し続けます。

#### 結論
"phpoffice/phpexcel": "^1.8" の使用には、Composer 経由でのインストール、Excel 操作のためのそのクラスの活用、および必要な PHP 拡張機能の確保が含まれます。機能的ではありますが、その非推奨化は注意を必要とし、将来のプロジェクトには PhpSpreadsheet が推奨されます。このガイドは、ユーザーがさらに探求するための例、依存関係、および追加リソースを提供する包括的な開始点を提供します。

### 主な引用文献
- [Packagist phpoffice/phpexcel ページ (インストール詳細)](https://packagist.org/packages/phpoffice/phpexcel)
- [SitePoint チュートリアル: PHPExcel で Excel ファイルとチャートを生成](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)
- [PHPExcel GitHub リポジトリ アーカイブ済みステータス](https://github.com/PHPOffice/PHPExcel)
- [PHPExcel からの PhpSpreadsheet 移行ガイド](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/)