---
audio: false
generated: true
lang: hant
layout: post
title: PHP 二維碼生成工具
translated: true
type: note
---

### 重點摘要
- 要使用 "endroid/qr-code" 2.2.2 版本，您可能需要透過 Composer 安裝並確保 GD 擴充功能已啟用。
- 研究顯示您可以使用 Builder 類別生成 QR 碼，設定參數如資料、尺寸和寫入器，然後儲存或輸出結果。
- 證據傾向於該函式庫支援 PNG、SVG 及其他格式，並提供標誌和標籤的選項，但需針對 2.2.2 版本進行驗證。

### 安裝步驟
首先，使用以下 Composer 指令安裝函式庫：
```
composer require endroid/qr-code:2.2.2
```
請確保您的 PHP 環境已啟用 GD 擴充功能，因為這是生成圖像的必要條件。

### 使用範例
以下是使用 Builder 類別的基本範例，可能與 2.2.2 版本相容：
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
此程式碼會為 URL 建立 QR 碼並儲存為 PNG 檔案。您也可以將其輸出為 data URI 以供網頁顯示。

### 補充說明
該函式庫支援多種寫入器（如 PNG、SVG），並允許自訂選項如添加標誌或標籤。然而，由於 2.2.2 版本較舊，當前文檔中的某些功能（如進階標誌選項）可能不可用，因此請查閱該特定版本在 [GitHub](https://github.com/endroid/qr-code) 上的文檔。

---

### 調查備註：詳細使用 "endroid/qr-code" 2.2.2 版本指南

本備註提供了一份全面指南，介紹如何在 PHP 應用程式中使用 "endroid/qr-code" 函式庫的 2.2.2 版本來生成 QR 碼。它擴展了直接回答的內容，包含了研究中的所有相關細節，確保開發人員（尤其是該函式庫的新手）能夠全面理解。內容結構模仿專業文章，並使用表格以增強清晰度，以及內嵌 URL 以供進一步參考。

#### 簡介
"endroid/qr-code" 函式庫是一個用於生成 QR 碼的 PHP 工具，廣泛應用於產品追蹤、文件管理和行銷等場景。查詢中指定的 2.2.2 版本是一個較舊的發布版本，儘管該函式庫在 [Packagist](https://packagist.org/packages/endroid/qr-code) 上被標記為已棄用，但它仍可用於基本的 QR 碼生成。本指南概述了安裝和使用方法，重點確保與 2.2.2 版本的相容性，並承認可能與新版本存在的差異。

#### 安裝流程
首先，您必須透過 PHP 套件管理工具 Composer 安裝該函式庫。指令如下：
```
composer require endroid/qr-code:2.2.2
```
這確保您獲得確切的 2.2.2 版本。一個關鍵要求是 PHP 的 GD 擴充功能必須啟用並配置，因為它是生成圖像的基礎。沒有它，函式庫將無法產生視覺化的 QR 碼。

| 步驟                 | 詳細說明                                                                 |
|----------------------|-------------------------------------------------------------------------|
| 安裝指令             | `composer require endroid/qr-code:2.2.2`                                |
| PHP 要求             | 確保 GD 擴充功能已啟用（可檢查 `phpinfo()` 以確認）                     |

研究表明，該函式庫的 GitHub 儲存庫 ([GitHub](https://github.com/endroid/qr-code)) 和 [Packagist](https://packagist.org/packages/endroid/qr-code) 頁面確認了此安裝方法，但未找到特定的 2.2.2 版本文檔，這表明需依賴一般使用模式。

#### 使用詳情
該函式庫提供兩種主要的 QR 碼生成方法：使用 Builder 類別或直接使用 QrCode 類別。考慮到查詢的重點是使用方式，建議使用 Builder 方法，因為它更簡單，但為了完整性，這裡將詳細介紹兩種方法。

##### 使用 Builder 類別
Builder 類別提供了一個流暢的介面來配置 QR 碼。根據當前文檔中的範例，基本實現如下：
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
此程式碼為 URL 建立了一個 QR 碼，使用 PNG 格式，採用 ISO-8859-1 編碼以提升掃描器相容性，並具有高錯誤修正等級。您也可以將其輸出為 data URI：
```php
$qrCodeDataUri = $qrCode->getDataUri();
```
這對於嵌入 HTML 非常有用，例如：`<img src="<?php echo $qrCodeDataUri; ?>">`。

然而，考慮到 2.2.2 版本的年代，某些類別如 `ErrorCorrectionLevelHigh` 可能命名不同（例如，舊版本中可能是 `ErrorCorrectionLevel::HIGH`）。來自 Stack Overflow 貼文 ([Stack Overflow](https://stackoverflow.com/questions/40777377/endroid-qr-code)) 的研究表明，舊版本使用了像 `setErrorCorrection('high')` 這樣的方法，因此請驗證 2.2.2 版本的 API。

##### 直接使用 QrCode 類別
為了更精細的控制，您可以使用 QrCode 類別，如範例所示：
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
這種方法更為冗長，但允許微調，例如設定前景和背景顏色，這可能與 2.2.2 版本相關。同樣，請檢查文檔以確認方法的可用性。

#### 配置選項
該函式庫支援多種寫入器以適應不同的輸出格式，如下表所示，基於當前文檔，但需針對 2.2.2 版本進行驗證：

| 寫入器類別           | 格式     | 備註                                                                 |
|----------------------|----------|----------------------------------------------------------------------|
| PngWriter            | PNG      | 可配置壓縮等級，預設為 -1                                           |
| SvgWriter            | SVG      | 適用於向量圖形，無壓縮選項                                         |
| WebPWriter           | WebP     | 品質 0-100，預設 80，適合網頁使用                                  |
| PdfWriter            | PDF      | 單位為 mm，預設，適合列印                                          |

編碼選項包括 UTF-8（預設）和 ISO-8859-1，後者推薦用於條碼掃描器的相容性。圓形區塊大小模式（邊距、放大、縮小、無）可以提升可讀性，但其在 2.2.2 版本中的可用性需要確認。

#### 進階功能與注意事項
對於進階使用，例如嵌入標誌，Builder 類別支援 `logoPath()` 和 `logoResizeToWidth()` 等方法，如 Medium 文章 ([Medium](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)) 所述。然而，這些可能是 2.2.2 版本之後新增的功能，因此請測試相容性。生成 QR 碼的驗證是可能的，但會影響效能且預設禁用，此細節來自 [GitHub](https://github.com/endroid/qr-code)。

考慮到該函式庫在 [Packagist](https://packagist.org/packages/endroid/qr-code) 上的棄用說明，值得注意潛在的安全或維護問題，但對於基本使用，它仍然可行。對於 Symfony 用戶，有一個套件 ([GitHub](https://github.com/endroid/qr-code-bundle))，但這超出了通用 PHP 使用的範圍。

#### 版本特定說明
研究顯示沒有 2.2.2 版本的直接文檔，GitHub 標籤中也未列出，表明它可能是一個較舊的發布版本或拼寫錯誤。當前儲存庫顯示版本高達 6.0.0，且 [Packagist](https://packagist.org/packages/endroid/qr-code) 將其標記為棄用，推薦 endroid/qr-code，這令人困惑，因為它是同一個套件。這表明可能存在重新命名或版本控制問題，因此用戶應鎖定依賴關係並測試升級。

#### 結論
使用 "endroid/qr-code" 2.2.2 版本涉及透過 Composer 安裝、確保 GD 擴充功能啟用，以及使用 Builder 或 QrCode 類別生成 QR 碼。雖然範例基於當前文檔，但請驗證 2.2.2 版本的 API 差異，特別是進階功能。更多詳細資訊，請查閱該函式庫的 GitHub 頁面和相關的 Stack Overflow 討論。

#### 主要參考文獻
- [QR Code Generator GitHub 儲存庫](https://github.com/endroid/qr-code)
- [endroid/qr-code Packagist 頁面](https://packagist.org/packages/endroid/qr-code)
- [建立帶嵌入圖像的 QR 碼 Medium 文章](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)
- [Endroid QR Code Stack Overflow 討論](https://stackoverflow.com/questions/40777377/endroid-qr-code)