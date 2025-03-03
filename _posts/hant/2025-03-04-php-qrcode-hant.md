---
audio: false
generated: true
lang: hant
layout: post
title: PHP 產生 QR 碼工具
translated: true
---

### 關鍵要點
- 似乎需要通過 Composer 安裝 "endroid/qr-code" 版本 2.2.2，並確保啟用 GD 擴展。
- 研究表明，可以使用 Builder 類生成 QR 碼，設置數據、大小和寫入器等參數，然後保存或輸出結果。
- 證據顯示，該庫支持 PNG、SVG 等格式，並且有標誌和標籤的選項，但請驗證版本 2.2.2。

### 安裝
首先，使用以下命令通過 Composer 安裝庫：
```
composer require endroid/qr-code:2.2.2
```
確保您的 PHP 設置已啟用 GD 擴展，因為它是生成圖像所必需的。

### 使用範例
這是一個使用 Builder 類的基本範例，該類可能與版本 2.2.2 兼容：
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
這將為 URL 生成 QR 碼並將其保存為 PNG 文件。您也可以將其作為數據 URI 進行輸出以供網頁顯示。

### 附加說明
該庫支持各種寫入器（例如 PNG、SVG）並允許自定義，例如添加標誌或標籤。然而，由於版本 2.2.2 是較舊的版本，當前文檔中的某些功能（例如高級標誌選項）可能不適用，因此請查閱該特定版本的文檔 [GitHub](https://github.com/endroid/qr-code)。

---

### 調查說明：使用 "endroid/qr-code" 版本 2.2.2 的詳細指南

這篇說明提供了使用 "endroid/qr-code" 庫版本 2.2.2 在 PHP 應用程序中生成 QR 碼的全面指南。它擴展了直接答案，包括所有相關的研究細節，確保開發人員，特別是新手，能夠全面理解。內容結構模仿專業文章，並使用表格以便於理解，並內嵌 URL 以供進一步參考。

#### 介紹
"endroid/qr-code" 庫是一個用於生成 QR 碼的 PHP 工具，廣泛用於產品追蹤、文檔管理和營銷等應用。版本 2.2.2，如查詢中所指定，是較舊的版本，儘管 [Packagist](https://packagist.org/packages/endroid/qr-code) 上標註為已棄用，但它仍然可以用於基本的 QR 碼生成。本指南概述了安裝和使用，並專注於確保與版本 2.2.2 兼容，並承認與較新版本的潛在差異。

#### 安裝過程
首先，您必須通過 Composer，PHP 包管理器，安裝該庫。命令如下：
```
composer require endroid/qr-code:2.2.2
```
這樣可以確保您獲得精確的版本 2.2.2。一個關鍵要求是 PHP 的 GD 擴展，必須啟用並配置，因為它對於圖像生成至關重要。沒有它，該庫無法生成視覺 QR 碼。

| 步驟                  | 詳細說明                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| 安裝命令       | `composer require endroid/qr-code:2.2.2`                                |
| PHP 要求       | 確保 GD 擴展已啟用（檢查 `phpinfo()` 以確認）     |

研究表明，該庫的 GitHub 存儲庫 ([GitHub](https://github.com/endroid/qr-code)) 和 [Packagist](https://packagist.org/packages/endroid/qr-code) 頁面確認了這種安裝方法，沒有找到特定於版本 2.2.2 的文檔，這表明依賴於一般使用模式。

#### 使用細節
該庫提供了兩種主要方法來生成 QR 碼：使用 Builder 類或直接使用 QrCode 類。由於查詢專注於使用，建議使用 Builder 方法，因為它簡單易用，但這裡詳細說明了兩者，以便完整性。

##### 使用 Builder 類
Builder 類為配置 QR 碼提供了流暢的界面。根據最近文檔中的示例，基本實現如下：
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
這段代碼為 URL 生成 QR 碼，使用 PNG 格式，使用 ISO-8859-1 編碼以提高掃描器兼容性，並使用高錯誤校正。您也可以將其作為數據 URI 進行輸出：
```php
$qrCodeDataUri = $qrCode->getDataUri();
```
這對於嵌入 HTML 中非常有用，例如 `<img src="<?php echo $qrCodeDataUri; ?>">`。

然而，由於版本 2.2.2 的年齡較大，某些類（例如 `ErrorCorrectionLevelHigh`）可能命名不同（例如在較舊版本中為 `ErrorCorrectionLevel::HIGH`）。來自 Stack Overflow 文章 ([Stack Overflow](https://stackoverflow.com/questions/40777377/endroid-qr-code)) 的研究表明，較舊版本使用方法如 `setErrorCorrection('high')`，因此請驗證 2.2.2 的 API。

##### 直接使用 QrCode 類
為了獲得更多控制，您可以使用 QrCode 類，如示例所示：
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
這種方法更加冗長，但允許細調，例如設置前景和背景顏色，這對於版本 2.2.2 可能相關。再次檢查文檔以確認方法可用性。

#### 配置選項
該庫支持各種寫入器以生成不同的輸出格式，如下表所示，根據當前文檔，並附上驗證 2.2.2 的說明：

| 寫入器類          | 格式   | 註釋                                                                 |
|-----------------------|----------|----------------------------------------------------------------------|
| PngWriter             | PNG      | 压縮級別可配置，默認 -1                           |
| SvgWriter             | SVG      | 適合矢量圖形，無壓縮選項                 |
| WebPWriter            | WebP     | 質量 0-100，默認 80，適合網絡使用                          |
| PdfWriter             | PDF      | 單位為 mm，默認，適合打印                                 |

編碼選項包括 UTF-8（默認）和 ISO-8859-1，後者建議用於條形碼掃描器兼容性。圓塊大小模式（邊距、擴大、縮小、無）可以提高可讀性，但需要確認 2.2.2 中的可用性。

#### 高級功能和考慮
對於高級用途，例如嵌入標誌，Builder 類支持方法如 `logoPath()` 和 `logoResizeToWidth()`，如 Medium 文章 ([Medium](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)) 所示。然而，這些可能是 2.2.2 之後的添加，因此需要測試兼容性。生成的 QR 碼的驗證是可能的，但會影響性能，並且默認情況下禁用，這是來自 [GitHub](https://github.com/endroid/qr-code) 的細節。

由於 [Packagist](https://packagist.org/packages/endroid/qr-code) 上標註為已棄用，值得注意潛在的安全或維護問題，儘管對於基本用途，它仍然可行。對於 Symfony 用戶，有一個捆綁包 ([GitHub](https://github.com/endroid/qr-code-bundle))，但這超出了一般 PHP 使用範圍。

#### 版本特定說明
研究顯示沒有直接針對版本 2.2.2 的文檔，GitHub 標籤未列出它，這表明它可能是較舊的版本或拼寫錯誤。當前存儲庫顯示版本至 6.0.0，[Packagist](https://packagist.org/packages/endroid/qr-code) 將其標註為已棄用，並建議 endroid/qr-code，這令人困惑，因為它是同一個包。這表明可能存在重命名或版本問題，因此用戶應鎖定依賴項並測試升級。

#### 結論
使用 "endroid/qr-code" 版本 2.2.2 涉及通過 Composer 安裝，確保 GD 擴展，並使用 Builder 或 QrCode 類生成 QR 碼。儘管示例基於當前文檔，但請驗證 2.2.2 的 API 差異，特別是高級功能。有關更多詳細信息，請參閱庫的 GitHub 頁面和相關 Stack Overflow 談論。

#### 關鍵引用
- [QR 碼生成器 GitHub 存儲庫](https://github.com/endroid/qr-code)
- [endroid/qr-code Packagist 頁面](https://packagist.org/packages/endroid/qr-code)
- [在 PHP 中創建帶有嵌入圖像的 QR 碼 Medium 文章](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)
- [Endroid QR 碼 Stack Overflow 談論](https://stackoverflow.com/questions/40777377/endroid-qr-code)