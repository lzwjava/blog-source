---
audio: false
generated: true
lang: hant
layout: post
title: PHPExcel 程式庫
translated: true
type: note
---

### 重點摘要
- 要使用 "phpoffice/phpexcel": "^1.8"，似乎需要透過 Composer 安裝並使用 PHP 程式碼來讀寫 Excel 檔案。
- 研究顯示此函式庫已過時，建議新專案考慮使用 PhpSpreadsheet。
- 證據顯示可能需要安裝 PHP 擴充功能如 mbstring、XML 和 XMLWriter。

### 安裝方法
要開始使用，請將 `"phpoffice/phpexcel": "^1.8"` 加入您的 `composer.json` 檔案，然後執行 `composer install`。這將下載此函式庫，對於在 PHP 中操作 Excel 檔案至關重要。

### 基本用法
寫入 Excel 檔案：
- 使用 `require 'vendor/autoload.php';` 引入函式庫。
- 建立新的 PHPExcel 物件：`$objPHPExcel = new PHPExcel();`。
- 設定儲存格數值，例如：`$sheet->setCellValue('A1', 'value');`。
- 使用寫入器儲存檔案，例如：`$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');` 接著執行 `$writer->save('filename.xlsx');`。

讀取 Excel 檔案：
- 使用 `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');` 載入檔案。
- 存取儲存格數值，例如：`$cellValue = $sheet->getCell('A1')->getValue();`。

### 特別注意事項
一個令人意外的細節是 PHPExcel 支援多種檔案格式如 .xls 和 .xlsx，並能在讀取時自動偵測檔案類型，這簡化了使用流程。

---

### 調查筆記：使用 "phpoffice/phpexcel": "^1.8" 完整指南

本筆記詳細探討如何使用 PHPExcel 函式庫，特別是版本 1.8 或更高，如 Composer 依賴項 "phpoffice/phpexcel": "^1.8" 所指定。考慮到其已過時的狀態，本指南也強調了現代替代方案的考量，並確保初學者和進階使用者都能全面理解。內容結構涵蓋安裝、使用、依賴項和額外背景資訊，確保包含研究中的所有相關細節。

#### 背景與情境
PHPExcel 是一個專為讀寫試算表檔案設計的 PHP 函式庫，特別是 Excel 格式如 .xls 和 .xlsx。版本規範 "^1.8" 表示語意化版本範圍，涵蓋從 1.8 開始但不包含 2.0 的所有版本，考慮到函式庫的歷史，這指向 2015 年發布的 1.8.1 版為最新版本。然而，研究顯示 PHPExcel 已於 2017 年正式過時並在 2019 年封存，建議遷移到其繼任者 PhpSpreadsheet，原因是缺乏維護和潛在安全問題。這個背景對使用者至關重要，因為它建議新專案需謹慎使用，不過本指南將依要求聚焦於指定版本的使用。

此函式庫的功能包括建立、讀取和操作 Excel 檔案，支援 Excel 以外的格式如 CSV 和 HTML。它曾是 PHPOffice 專案的一部分，該專案現已將重心轉向 PhpSpreadsheet，提供改進的功能和 PHP 標準合規性。考慮到當前日期為 2025 年 3 月 3 日，以及函式庫的封存狀態，使用者應注意其限制，特別是與新版 PHP 版本和安全更新的相容性。

#### 安裝流程
要安裝 "phpoffice/phpexcel": "^1.8"，流程利用 Composer（PHP 依賴管理工具）。步驟如下：
- 將依賴項加入您的 `composer.json` 檔案中的 "require" 部分：`"phpoffice/phpexcel": "^1.8"`。
- 在您的專案目錄中執行指令 `composer install`。此指令將下載函式庫並更新 `vendor` 目錄中的必要檔案。

Composer 中的脫字號 (^) 標記遵循語意化版本控制，確保安裝 1.8、1.8.1 或任何修補更新，但不會安裝破壞相容性的版本（即不包含 2.0 或更高）。考慮到函式庫的最後發布是 2015 年的 1.8.1 版，這通常會解析為版本 1.8.1。

研究確認 phpoffice/phpexcel 的 Packagist 頁面將其標記為已棄用，建議改用 phpoffice/phpspreadsheet，但它仍可供安裝，符合使用者的要求。

#### 基本用法：寫入 Excel
安裝完成後，使用 PHPExcel 涉及引入自動載入檔案以載入類別，然後使用其類別進行試算表操作。以下是詳細說明：

- **引入自動載入檔案：** 在 PHP 腳本開頭使用 `require 'vendor/autoload.php';`。此行確保所有透過 Composer 安裝的函式庫（包括 PHPExcel）都能自動載入，利用 PSR-0 自動載入機制（根據 2015 年函式庫的結構）。

- **建立新的 PHPExcel 物件：** 使用 `$objPHPExcel = new PHPExcel();` 初始化新的試算表。此物件代表整個活頁簿，允許使用多個工作表和工作表屬性。

- **操作工作表：** 使用 `$sheet = $objPHPExcel->getSheet(0);` 存取使用中的工作表（第一個工作表），或使用 `$sheet = $objPHPExcel->createSheet();` 建立新工作表。工作表以零為索引，因此 `getSheet(0)` 指向第一個工作表。

- **設定儲存格數值：** 使用 `setCellValue` 方法填入儲存格，例如：`$sheet->setCellValue('A1', 'Hello');`。此方法接受儲存格參照（如 'A1'）和要插入的數值，可以是文字、數字或公式。

- **儲存檔案：** 要儲存時，為所需格式建立寫入器。對於 Excel 2007 及以上版本 (.xlsx)，使用 `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');`。然後使用 `$writer->save('filename.xlsx');` 儲存。其他格式包括用於 .xls (Excel 95) 的 'Excel5' 或用於逗號分隔值的 'CSV'。

寫入的範例腳本可能如下：
```php
require 'vendor/autoload.php';
$objPHPExcel = new PHPExcel();
$sheet = $objPHPExcel->getSheet(0);
$sheet->setCellValue('A1', 'Hello');
$sheet->setCellValue('B1', 'World');
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');
$writer->save('hello_world.xlsx');
```
這將建立一個簡單的 Excel 檔案，在 A1 儲存格中填入 "Hello"，在 B1 儲存格中填入 "World"。

#### 基本用法：讀取 Excel
讀取 Excel 檔案遵循類似模式，但從載入檔案開始：
- **載入檔案：** 使用 `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');` 載入現有的 Excel 檔案。IOFactory 通常能自動偵測檔案類型，但您也可以指定讀取器，例如：`$objReader = PHPExcel_IOFactory::createReader('Excel2007'); $objPHPExcel = $objReader->load('filename.xlsx');` 以明確指定類型。

- **存取工作表和儲存格：** 載入後，如前所述存取工作表，例如：`$sheet = $objPHPExcel->getSheet(0);`。使用 `$cellValue = $sheet->getCell('A1')->getValue();` 擷取儲存格數值，這將回傳指定儲存格的內容。

讀取的範例：
```php
require 'vendor/autoload.php';
$objPHPExcel = PHPExcel_IOFactory::load('hello_world.xlsx');
$sheet = $objPHPExcel->getSheet(0);
$cellValue = $sheet->getCell('A1')->getValue();
echo $cellValue; // 輸出 "Hello"
```
這將讀取 A1 的數值，示範基本的擷取操作。

#### 依賴項與需求
PHPExcel 有特定的 PHP 需求和運作所需的擴充功能：
- **PHP 版本：** 根據 Packagist 元數據，需要 PHP 5.2 或 7.0 或更高版本。考慮到當前日期為 2025 年 3 月 3 日，大多數現代 PHP 安裝應符合此要求，但較舊的設定可能需要更新。
- **擴充功能：** 函式庫依賴 `ext-mbstring`、`ext-XML` 和 `ext-XMLWriter`，這些必須在您的 PHP 配置中啟用。這些擴充功能處理字串編碼、XML 解析和 XML 寫入，對於 Excel 檔案操作至關重要。

使用者應使用 `phpinfo()` 或檢查 `php.ini` 檔案來驗證這些擴充功能是否啟用，確保不會出現相容性問題。

#### 額外功能與格式
除了基本的讀寫功能，PHPExcel 支援多種檔案格式，這對僅熟悉 Excel 的使用者來說是一個意外的細節。函式庫可處理：
- Excel 2007 (.xlsx) 透過 'Excel2007' 寫入器/讀取器。
- Excel 95 (.xls) 透過 'Excel5'。
- CSV 檔案透過 'CSV'。
- HTML 透過 'HTML'。

儲存時，指定寫入器類型；讀取時，IOFactory 通常會自動偵測，但為確保可靠性可使用明確的讀取器。例如，要儲存為 .xls：
```php
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel5');
$writer->save('filename.xls');
```
這種靈活性對於舊系統或特定格式需求很有用，但使用者應注意潛在的格式特定限制，特別是與舊版 Excel 的相容性。

#### 過時狀態與遷移建議
一個關鍵點是 PHPExcel 的過時狀態。研究顯示它於 2019 年封存，最後更新於 2015 年，且不再維護。這引發了對安全漏洞和與 PHP 7.0 以上版本（特別是現代標準如 PHP 8.x）相容性的擔憂。GitHub 儲存庫和 Packagist 頁面均建議遷移到 PhpSpreadsheet，後者提供命名空間、PSR 合規性和活躍開發。

對使用者而言，這意味著：
- 對於現有使用 PHPExcel 1.8 的專案，請謹慎繼續使用，確保進行安全和相容性測試。
- 對於新專案，強烈考慮使用 PhpSpreadsheet，並使用可用的遷移工具，如 PhpSpreadsheet 文件中所述（[從 PHPExcel 遷移](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/)）。

考慮到當前日期，此建議尤其相關，確保使用者與現代、受支援的函式庫保持一致。

#### 文件與進一步學習
要深入探索，PHPExcel 的官方文件可在其 GitHub 儲存庫的 Documentation 資料夾中找到，但存取可能需要下載如開發者文件 DOC 等檔案。線上，像 SitePoint 上的教學（[使用 PHPExcel 生成 Excel 檔案和圖表](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)）提供實用範例，涵蓋圖表和格式化，這些內容超出了基本用法。Stack Overflow 討論串也提供社群見解，但考慮到函式庫的狀態，應注意過時的答案。

#### 比較表格：PHPExcel vs. PhpSpreadsheet
為協助決策，以下是基於研究的比較表格，突顯關鍵差異：

| 功能特點             | PHPExcel (1.8)                    | PhpSpreadsheet                   |
|----------------------|-----------------------------------|----------------------------------|
| 最後更新             | 2015                              | 活躍維護（截至 2025 年）         |
| 命名空間             | 無，使用根命名空間               | 有，符合 PSR-4 標準              |
| 維護狀態             | 已過時，2019 年封存              | 積極維護                         |
| PHP 版本支援         | 最高至 7.0                        | PHP 7.4+                         |
| 檔案格式支援         | Excel、CSV、HTML 等               | 增強，包括 ODS、PDF              |
| 效能表現             | 中等，記憶體消耗較大              | 優化，可擴展性佳                 |

此表格強調了對於現代需求應轉向 PhpSpreadsheet，儘管 PHPExcel 對於舊有用途仍可運作。

#### 結論
使用 "phpoffice/phpexcel": "^1.8" 涉及透過 Composer 安裝，利用其類別進行 Excel 操作，並確保必要的 PHP 擴充功能。雖然功能正常，但其過時狀態需要謹慎，建議新專案使用 PhpSpreadsheet。本指南提供全面的起點，包含範例、依賴項和額外資源，供使用者進一步探索。

### 主要參考文獻
- [Packagist phpoffice/phpexcel 頁面含安裝細節](https://packagist.org/packages/phpoffice/phpexcel)
- [SitePoint 關於使用 PHPExcel 生成 Excel 檔案的教學](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)
- [PHPExcel GitHub 儲存庫封存狀態](https://github.com/PHPOffice/PHPExcel)
- [從 PHPExcel 遷移至 PhpSpreadsheet 的指南](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/)