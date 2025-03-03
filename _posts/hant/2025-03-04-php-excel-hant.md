---
audio: false
generated: true
lang: hant
layout: post
title: PHPExcel 圖書館
translated: true
---

### 關鍵要點
- 使用 "phpoffice/phpexcel": "^1.8" 似乎需要通過 Composer 安裝，並使用 PHP 代碼讀取和寫入 Excel 文件。
- 研究表明該庫已經廢棄，因此建議新項目使用 PhpSpreadsheet。
- 證據顯示需要 PHP 擴展，如 mbstring、XML 和 XMLWriter。

### 安裝
要開始，將 `"phpoffice/phpexcel": "^1.8"` 添加到您的 `composer.json` 文件中，然後運行 `composer install`。這將下載該庫，這對於在 PHP 中處理 Excel 文件是必不可少的。

### 基本使用
寫入 Excel 文件：
- 使用 `require 'vendor/autoload.php';` 包含庫。
- 創建一個新的 PHPExcel 對象：`$objPHPExcel = new PHPExcel();`。
- 設置單元格值，例如 `$sheet->setCellValue('A1', 'value');`。
- 使用寫入器保存文件，例如 `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');` 後跟 `$writer->save('filename.xlsx');`。

從 Excel 文件讀取：
- 使用 `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');` 加載文件。
- 訪問單元格值，例如 `$cellValue = $sheet->getCell('A1')->getValue();`。

### 意外細節
意外的方面是 PHPExcel 支持各種文件格式，如 .xls 和 .xlsx，並且可以在讀取時自動檢測文件類型，這簡化了使用。

---

### 調查筆記：使用 "phpoffice/phpexcel": "^1.8" 的全面指南

這篇筆記提供了使用 PHPExcel 庫的詳細探討，特別是由 Composer 依賴 "phpoffice/phpexcel": "^1.8" 指定的 1.8 版或更高版本。考慮到其廢棄狀態，這個指南還強調了現代替代方案的考慮，並確保初學者和高級用戶都能全面理解。內容結構涵蓋安裝、使用、依賴和其他上下文，確保包含所有相關的研究細節。

#### 背景和上下文
PHPExcel 是一個設計用於讀取和寫入電子表格文件的 PHP 庫，特別是 Excel 格式，如 .xls 和 .xlsx。版本規範 "^1.8" 指示語義版本範圍，這意味著從 1.8 到但不包括 2.0 的任何版本，這與庫的歷史相符，指向 2015 年發布的 1.8.1 版本。然而，研究表明 PHPExcel 於 2017 年正式廢棄，並在 2019 年被封存，建議遷移到其繼任者 PhpSpreadsheet，因為缺乏維護和潛在的安全問題。這一背景對用戶至關重要，因為它建議對新項目保持謹慎，儘管這個指南將專注於使用指定的版本，如所請求的那樣。

該庫的功能包括創建、讀取和操作 Excel 文件，支持超出 Excel 的格式，如 CSV 和 HTML。它是 PHPOffice 項目的一部分，該項目已經轉向 PhpSpreadsheet，提供改進的功能和 PHP 標準合規性。考慮到當前日期，2025 年 3 月 3 日，以及庫的封存狀態，用戶應該意識到其限制，特別是與新的 PHP 版本和安全更新。

#### 安裝過程
要安裝 "phpoffice/phpexcel": "^1.8"，過程利用 Composer，PHP 依賴管理器。步驟如下：
- 在 "require" 部分將依賴項添加到您的 `composer.json` 文件中：`"phpoffice/phpexcel": "^1.8"`。
- 在項目目錄中運行命令 `composer install`。該命令下載庫並更新 `vendor` 目錄中的必要文件。

Composer 中的換行符 (^) 遵循語義版本控制，確保安裝 1.8、1.8.1 或任何補丁更新，但不安裝會破壞兼容性的版本（即不安裝 2.0 或更高版本）。考慮到庫的最後發布版本是 2015 年的 1.8.1，這通常解析為版本 1.8.1。

研究確認 Packagist 頁面上的 phpoffice/phpexcel 列為廢棄，建議 phpoffice/phpspreadsheet，但它仍然可用於安裝，與用戶的請求一致。

#### 基本使用：寫入 Excel
安裝後，使用 PHPExcel 涉及包含自動加載文件以進行類加載，然後利用其類進行電子表格操作。以下是詳細說明：

- **包含自動加載文件**：從 `require 'vendor/autoload.php';` 开始您的 PHP 腳本。該行確保所有 Composer 安裝的庫，包括 PHPExcel，都自動加載，利用 2015 年庫的結構中的 PSR-0 自動加載。

- **創建一個新的 PHPExcel 對象**：使用 `$objPHPExcel = new PHPExcel();` 初始化新的電子表格。該對象表示整個工作簿，允許多個工作表和屬性。

- **處理工作表**：使用 `$sheet = $objPHPExcel->getSheet(0);` 訪問活動工作表，或使用 `$sheet = $objPHPExcel->createSheet();` 創建一個新的工作表。工作表是從零索引的，因此 `getSheet(0)` 針對第一個工作表。

- **設置單元格值**：使用 `setCellValue` 方法填充單元格，例如 `$sheet->setCellValue('A1', 'Hello');`。該方法接受單元格引用（如 'A1'）和要插入的值，該值可以是文本、數字或公式。

- **保存文件**：要保存，為所需格式創建寫入器。對於 Excel 2007 及更高版本 (.xlsx)，使用 `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');`。然後使用 `$writer->save('filename.xlsx');` 保存。其他格式包括 'Excel5' 為 .xls（Excel 95）或 'CSV' 為逗號分隔值。

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
這將創建一個簡單的 Excel 文件，其中 A1 中有 "Hello"，B1 中有 "World"。

#### 基本使用：從 Excel 讀取
從 Excel 文件讀取遵循類似的模式，但從加載文件開始：
- **加載文件**：使用 `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');` 加載現有的 Excel 文件。IOFactory 可以自動檢測文件類型，但您可以指定讀取器，例如 `$objReader = PHPExcel_IOFactory::createReader('Excel2007'); $objPHPExcel = $objReader->load('filename.xlsx');` 以明確類型。

- **訪問工作表和單元格**：加載後，像之前一樣訪問工作表，例如 `$sheet = $objPHPExcel->getSheet(0);`。使用 `$cellValue = $sheet->getCell('A1')->getValue();` 獲取單元格值，該值返回指定單元格的內容。

讀取的範例：
```php
require 'vendor/autoload.php';
$objPHPExcel = PHPExcel_IOFactory::load('hello_world.xlsx');
$sheet = $objPHPExcel->getSheet(0);
$cellValue = $sheet->getCell('A1')->getValue();
echo $cellValue; // 輸出 "Hello"
```
這將讀取 A1 的值，展示基本檢索。

#### 依賴和要求
PHPExcel 有特定的 PHP 要求和操作所需的擴展：
- **PHP 版本**：需要 PHP 5.2 或 7.0 或更高版本，根據 Packagist 元數據。考慮到當前日期，2025 年 3 月 3 日，大多數現代 PHP 安裝應該滿足這一要求，但較舊的設置可能需要更新。
- **擴展**：該庫依賴於 `ext-mbstring`、`ext-XML` 和 `ext-XMLWriter`，這些擴展必須在 PHP 配置中啟用。這些擴展分別處理字符編碼、XML 解析和 XML 寫入，這對於 Excel 文件操作是必不可少的。

用戶應該使用 `phpinfo()` 或檢查 `php.ini` 文件，驗證這些擴展是否處於活動狀態，確保不會出現兼容性問題。

#### 額外功能和格式
除了基本的讀寫，PHPExcel 還支持各種文件格式，這對於僅熟悉 Excel 的用戶來說是意外的細節。該庫可以處理：
- Excel 2007 (.xlsx) 通過 'Excel2007' 寫入器/讀取器。
- Excel 95 (.xls) 通過 'Excel5'。
- CSV 文件通過 'CSV'。
- HTML 通過 'HTML'。

保存時，指定寫入器類型；讀取時，IOFactory 通常自動檢測，但可以使用明確的讀取器以確保可靠性。例如，將其保存為 .xls：
```php
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel5');
$writer->save('filename.xls');
```
這種靈活性對於遺留系統或特定格式需求非常有用，儘管用戶應該注意潛在的格式特定限制，特別是較舊的 Excel 版本。

#### 廢棄和遷移建議
關鍵點是 PHPExcel 的廢棄。研究顯示它於 2019 年被封存，最後更新於 2015 年，不再維護。這引發了對安全漏洞和與 PHP 版本 7.0 以上的兼容性的擔憂，特別是與現代標準，如 PHP 8.x。GitHub 存儲庫和 Packagist 頁面都建議遷移到 PhpSpreadsheet，該庫提供命名空間、PSR 合規性和積極開發。

對於用戶，這意味著：
- 對於使用 PHPExcel 1.8 的現有項目，請繼續謹慎，確保測試安全性和兼容性。
- 對於新項目，強烈考慮 PhpSpreadsheet，並且有遷移工具可用，如 PhpSpreadsheet 文檔中所述 ([從 PHPExcel 遷移](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/))。

這一建議特別相關，確保用戶與現代、受支持的庫保持一致。

#### 文檔和進一步學習
深入探索，PHPExcel 的官方文檔可在其 GitHub 存儲庫的文檔文件夾中找到，儘管訪問可能需要下載文件，如開發者文檔 DOC。在線教程，如 SitePoint 上的教程 ([使用 PHPExcel 生成 Excel 文件和圖表](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)) 提供實際示例，涵蓋圖表和格式化，這些超出了基本使用。Stack Overflow 線程也提供社區見解，儘管應該小心處理過時的答案，考慮到庫的狀態。

#### 比較表：PHPExcel 與 PhpSpreadsheet
為了幫助決策，以下是基於研究的比較表，突出了關鍵差異：

| 功能                  | PHPExcel (1.8)                     | PhpSpreadsheet                  |
|--------------------------|------------------------------------|---------------------------------|
| 最後更新              | 2015                              | 活躍（截至 2025 年）             |
| 命名空間               | 無，根命名空間                | 是，PSR-4 合規            |
| 維護狀態               | 廢棄，2019 年封存         | 活躍維護             |
| PHP 版本支持            | 至 7.0                         | PHP 7.4+                        |
| 文件格式支持            | Excel、CSV、HTML 等            | 增強，包括 ODS、PDF    |
| 性能                  | 中等，記憶體密集        | 優化，可擴展             |

該表強調了轉向 PhpSpreadsheet 以滿足現代需求，儘管 PHPExcel 仍然功能齊全，適用於遺留用途。

#### 結論
使用 "phpoffice/phpexcel": "^1.8" 涉及通過 Composer 安裝，利用其類進行 Excel 操作，並確保所需的 PHP 擴展。儘管功能齊全，其廢棄狀態需要謹慎，建議對未來項目使用 PhpSpreadsheet。該指南提供了全面的起點，包括示例、依賴和其他資源，供用戶進一步探索。

### 關鍵引用
- [Packagist phpoffice/phpexcel 頁面，安裝詳細信息](https://packagist.org/packages/phpoffice/phpexcel)
- [SitePoint 教程，使用 PHPExcel 生成 Excel 文件](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)
- [PHPExcel GitHub 存儲庫封存狀態](https://github.com/PHPOffice/PHPExcel)
- [PhpSpreadsheet 從 PHPExcel 遷移指南](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/)