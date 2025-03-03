---
audio: false
generated: true
lang: zh
layout: post
title: PHPExcel库
translated: true
---

### 关键点
- 使用 "phpoffice/phpexcel": "^1.8" 似乎需要通过 Composer 安装，并使用 PHP 代码读取和写入 Excel 文件。
- 研究表明该库已废弃，因此建议为新项目使用 PhpSpreadsheet。
- 证据表明需要 PHP 扩展，如 mbstring、XML 和 XMLWriter。

### 安装
要开始，将 `"phpoffice/phpexcel": "^1.8"` 添加到您的 `composer.json` 文件中，然后运行 `composer install`。这将下载该库，这是在 PHP 中处理 Excel 文件所必需的。

### 基本用法
编写到 Excel 文件：
- 使用 `require 'vendor/autoload.php';` 包含库。
- 创建一个新的 PHPExcel 对象：`$objPHPExcel = new PHPExcel();`。
- 设置单元格值，例如 `$sheet->setCellValue('A1', 'value');`。
- 使用写入器保存文件，例如 `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');` 后跟 `$writer->save('filename.xlsx');`。

从 Excel 文件读取：
- 使用 `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');` 加载文件。
- 访问单元格值，例如 `$cellValue = $sheet->getCell('A1')->getValue();`。

### 意外细节
一个意外的方面是 PHPExcel 支持各种文件格式，如 .xls 和 .xlsx，并且在读取时可以自动检测文件类型，这简化了使用。

---

### 调查笔记：使用 "phpoffice/phpexcel": "^1.8" 的全面指南

此笔记详细探讨了使用 PHPExcel 库，特别是由 Composer 依赖项 "phpoffice/phpexcel": "^1.8" 指定的 1.8 或更高版本。鉴于其废弃状态，此指南还强调了现代替代方案的考虑，并确保初学者和高级用户都能全面理解。内容结构涵盖安装、使用、依赖项和额外上下文，确保包含所有相关的研究细节。

#### 背景和上下文
PHPExcel 是一个用于读取和写入电子表格文件的 PHP 库，特别是 Excel 格式，如 .xls 和 .xlsx。版本规范 "^1.8" 指示语义版本范围，这意味着从 1.8 到 2.0 但不包括 2.0，这与库的历史相符，指向 2015 年发布的 1.8.1 版本。然而，研究表明 PHPExcel 于 2017 年正式废弃，并于 2019 年归档，建议迁移到其继任者 PhpSpreadsheet，因为缺乏维护和潜在的安全问题。此上下文对用户至关重要，因为它建议对新项目谨慎，尽管指南将集中在使用指定版本，如所请求的那样。

该库的功能包括创建、读取和操作 Excel 文件，支持超出 Excel 的格式，如 CSV 和 HTML。它是 PHPOffice 项目的一部分，该项目已转向 PhpSpreadsheet，提供了改进的功能和 PHP 标准符合性。鉴于当前日期为 2025 年 3 月 3 日，以及该库的归档状态，用户应了解其限制，特别是与较新的 PHP 版本和安全更新。

#### 安装过程
要安装 "phpoffice/phpexcel": "^1.8"，该过程利用 Composer，PHP 依赖管理器。步骤如下：
- 在 "require" 部分将依赖项添加到 `composer.json` 文件中：`"phpoffice/phpexcel": "^1.8"`。
- 在项目目录中运行命令 `composer install`。此命令下载库并使用必要的文件更新 `vendor` 目录。

Composer 中的 caret (^) 符号遵循语义版本控制，确保安装版本 1.8、1.8.1 或任何补丁更新，但不安装可能会中断兼容性的版本（即不安装 2.0 或更高版本）。鉴于该库的最后发布版本是 2015 年的 1.8.1，这通常解析为版本 1.8.1。

研究确认 Packagist 页面列出 phpoffice/phpexcel 为废弃，建议使用 phpoffice/phpspreadsheet，但它仍然可用于安装，与用户的请求一致。

#### 基本用法：写入 Excel
安装后，使用 PHPExcel 涉及包含自动加载文件以进行类加载，然后使用其类进行电子表格操作。以下是详细说明：

- **包含自动加载文件**：使用 `require 'vendor/autoload.php';` 开始您的 PHP 脚本。此行确保所有通过 Composer 安装的库（包括 PHPExcel）都自动加载，利用 2015 年库的结构中的 PSR-0 自动加载。

- **创建一个新的 PHPExcel 对象**：使用 `$objPHPExcel = new PHPExcel();` 初始化新的电子表格。此对象表示整个工作簿，允许多个工作表和属性。

- **处理工作表**：使用 `$sheet = $objPHPExcel->getSheet(0);` 访问活动工作表，或使用 `$sheet = $objPHPExcel->createSheet();` 创建一个新的工作表。工作表是从零开始索引的，因此 `getSheet(0)` 目标是第一个工作表。

- **设置单元格值**：使用 `setCellValue` 方法填充单元格，例如 `$sheet->setCellValue('A1', 'Hello');`。此方法接受单元格引用（如 'A1'）和要插入的值，可以是文本、数字或公式。

- **保存文件**：要保存，为所需格式创建一个写入器。对于 Excel 2007 及更高版本 (.xlsx)，使用 `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');`。然后使用 `$writer->save('filename.xlsx');` 保存。其他格式包括 'Excel5' 用于 .xls（Excel 95）或 'CSV' 用于逗号分隔值。

一个编写示例脚本可能如下：
```php
require 'vendor/autoload.php';
$objPHPExcel = new PHPExcel();
$sheet = $objPHPExcel->getSheet(0);
$sheet->setCellValue('A1', 'Hello');
$sheet->setCellValue('B1', 'World');
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');
$writer->save('hello_world.xlsx');
```
这将创建一个简单的 Excel 文件，其中 A1 为 "Hello"，B1 为 "World"。

#### 基本用法：从 Excel 读取
从 Excel 文件读取遵循类似的模式，但从加载文件开始：
- **加载文件**：使用 `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');` 加载现有的 Excel 文件。IOFactory 可以自动检测文件类型，但您可以指定读取器，例如 `$objReader = PHPExcel_IOFactory::createReader('Excel2007'); $objPHPExcel = $objReader->load('filename.xlsx');` 用于显式类型。

- **访问工作表和单元格**：加载后，像以前一样访问工作表，例如 `$sheet = $objPHPExcel->getSheet(0);`。使用 `$cellValue = $sheet->getCell('A1')->getValue();` 检索单元格值，它返回指定单元格的内容。

一个读取示例：
```php
require 'vendor/autoload.php';
$objPHPExcel = PHPExcel_IOFactory::load('hello_world.xlsx');
$sheet = $objPHPExcel->getSheet(0);
$cellValue = $sheet->getCell('A1')->getValue();
echo $cellValue; // 输出 "Hello"
```
这将读取 A1 的值，演示基本检索。

#### 依赖项和要求
PHPExcel 有特定的 PHP 要求和操作所需的扩展：
- **PHP 版本**：需要 PHP 5.2 或 7.0 或更高版本，根据 Packagist 元数据。鉴于当前日期为 2025 年 3 月 3 日，大多数现代 PHP 安装应该满足此要求，但较旧的设置可能需要更新。
- **扩展**：该库依赖于 `ext-mbstring`、`ext-XML` 和 `ext-XMLWriter`，必须在 PHP 配置中启用。这些扩展分别处理字符串编码、XML 解析和 XML 写入，对于 Excel 文件操作是必需的。

用户应使用 `phpinfo()` 或检查 `php.ini` 文件，确保这些扩展处于活动状态，以确保没有兼容性问题。

#### 额外功能和格式
除了基本的读写，PHPExcel 还支持各种文件格式，这是用户熟悉的意外细节。该库可以处理：
- Excel 2007 (.xlsx) 通过 'Excel2007' 写入器/读取器。
- Excel 95 (.xls) 通过 'Excel5'。
- CSV 文件通过 'CSV'。
- HTML 通过 'HTML'。

保存时，指定写入器类型；读取时，IOFactory 通常会自动检测，但可以使用显式读取器以确保可靠性。例如，要保存为 .xls：
```php
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel5');
$writer->save('filename.xls');
```
这种灵活性对于遗留系统或特定格式需求非常有用，尽管用户应注意可能的格式特定限制，特别是较旧的 Excel 版本。

#### 废弃和迁移建议
一个关键点是 PHPExcel 的废弃。研究表明它于 2019 年归档，最后更新于 2015 年，不再维护。这引发了安全漏洞和与 PHP 版本 7.0 以上的兼容性问题的担忧，特别是与现代标准，如 PHP 8.x。GitHub 存储库和 Packagist 页面都建议迁移到 PhpSpreadsheet，它提供了命名空间、PSR 符合性和活跃开发。

对于用户，这意味着：
- 对于现有项目使用 PHPExcel 1.8，继续谨慎，确保测试安全性和兼容性。
- 对于新项目，强烈考虑 PhpSpreadsheet，迁移工具可用，如 PhpSpreadsheet 文档中所述 ([从 PHPExcel 迁移](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/))。

此建议在当前日期下尤为相关，确保用户与现代、受支持的库保持一致。

#### 文档和进一步学习
深入探索，官方文档可在其 GitHub 存储库的 Documentation 文件夹中找到，但访问可能需要下载文件，如开发者文档 DOC。在线，如 SitePoint 上的教程 ([使用 PHPExcel 生成 Excel 文件和图表](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)) 提供了实际示例，涵盖图表和格式，超出了基本用法。Stack Overflow 线程也提供了社区见解，但应注意过时答案，因为该库的状态。

#### 比较表：PHPExcel 与 PhpSpreadsheet
为了帮助决策，以下是基于研究的比较表，突出了关键差异：

| 特性                  | PHPExcel (1.8)                     | PhpSpreadsheet                  |
|--------------------------|------------------------------------|---------------------------------|
| 最后更新              | 2015                              | 活跃（截至 2025 年）             |
| 命名空间               | 否，根命名空间                | 是，PSR-4 符合            |
| 维护状态               | 废弃，2019 年归档         | 活跃维护             |
| PHP 版本支持            | 至 7.0                         | PHP 7.4+                        |
| 文件格式支持            | Excel、CSV、HTML 等            | 增强，包括 ODS、PDF    |
| 性能              | 中等，内存密集        | 优化，可扩展             |

此表强调了现代需求的转向 PhpSpreadsheet，尽管 PHPExcel 仍然适用于遗留用途。

#### 结论
使用 "phpoffice/phpexcel": "^1.8" 涉及通过 Composer 安装，利用其类进行 Excel 操作，并确保所需的 PHP 扩展。虽然功能齐全，但其废弃状态需要谨慎，建议为未来项目使用 PhpSpreadsheet。此指南提供了一个全面的起点，包括示例、依赖项和额外资源，供用户进一步探索。

### 关键引用
- [Packagist phpoffice/phpexcel 页面，带有安装详细信息](https://packagist.org/packages/phpoffice/phpexcel)
- [SitePoint 教程，使用 PHPExcel 生成 Excel 文件](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)
- [PHPExcel GitHub 存储库归档状态](https://github.com/PHPOffice/PHPExcel)
- [从 PHPExcel 迁移到 PhpSpreadsheet 的指南](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/)