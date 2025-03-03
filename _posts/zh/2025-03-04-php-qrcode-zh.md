---
audio: false
generated: true
lang: zh
layout: post
title: PHP 生成二维码工具
translated: true
---

### 关键点
- 使用 "endroid/qr-code" 版本 2.2.2 似乎需要通过 Composer 安装，并确保 GD 扩展已启用。
- 研究表明，可以使用 Builder 类生成 QR 码，设置数据、大小和编写器等参数，然后保存或输出结果。
- 证据表明，该库支持 PNG、SVG 等格式，并有标志和标签的选项，但请验证 2.2.2 版本。

### 安装
首先，使用 Composer 安装库，命令如下：
```bash
composer require endroid/qr-code:2.2.2
```
确保 PHP 设置中启用了 GD 扩展，因为它是图像生成所必需的。

### 使用示例
这是一个使用 Builder 类的基本示例，可能与 2.2.2 版本兼容：
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
这将为 URL 生成一个 QR 码并将其保存为 PNG 文件。您也可以将其作为数据 URI 输出以供网页显示。

### 附加说明
该库支持各种编写器（例如 PNG、SVG）并允许自定义，如添加标志或标签。然而，由于 2.2.2 版本较旧，当前文档中的某些功能（如高级标志选项）可能不可用，因此请查看该特定版本的文档 [GitHub](https://github.com/endroid/qr-code)。

---

### 调查说明：关于使用 "endroid/qr-code" 版本 2.2.2 的详细指南

此说明提供了关于在 PHP 应用程序中使用 "endroid/qr-code" 库版本 2.2.2 生成 QR 码的全面指南。它扩展了直接答案，包括所有相关的研究详细信息，确保开发人员，特别是那些对该库不熟悉的人，能够全面理解。内容结构模仿专业文章，使用表格以便于理解，并使用内联 URL 以供进一步参考。

#### 引言
"endroid/qr-code" 库是一个用于生成 QR 码的 PHP 工具，广泛用于产品跟踪、文档管理和营销等应用。版本 2.2.2，如查询中所指定的，是一个较旧的发布版本，尽管该库在 [Packagist](https://packagist.org/packages/endroid/qr-code) 上被标记为废弃，但它仍然可以用于基本的 QR 码生成。本指南概述了安装和使用，重点确保与 2.2.2 版本兼容，并承认与较新版本的潜在差异。

#### 安装过程
首先，您必须通过 Composer 安装该库，这是 PHP 包管理器。命令如下：
```bash
composer require endroid/qr-code:2.2.2
```
这确保您获得了 2.2.2 版本。一个关键要求是 PHP 的 GD 扩展，必须启用并配置，因为它对图像生成至关重要。没有它，库无法生成可视化的 QR 码。

| 步骤                  | 详细信息                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| 安装命令       | `composer require endroid/qr-code:2.2.2`                                |
| PHP 要求       | 确保 GD 扩展已启用（使用 `phpinfo()` 进行确认）     |

研究表明，库的 GitHub 存储库 ([GitHub](https://github.com/endroid/qr-code)) 和 [Packagist](https://packagist.org/packages/endroid/qr-code) 页面确认了这种安装方法，没有找到特定于 2.2.2 版本的文档，这表明依赖于一般使用模式。

#### 使用详细信息
该库为 QR 码生成提供了两种主要方法：使用 Builder 类或直接使用 QrCode 类。鉴于查询的重点是使用，建议使用 Builder 方法，因为它更简单，尽管两者都详细说明以确保完整性。

##### 使用 Builder 类
Builder 类为配置 QR 码提供了流畅的接口。根据最近文档中的示例，基本实现如下：
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
此代码为 URL 生成 QR 码，使用 PNG 格式，使用 ISO-8859-1 编码以提高扫描器兼容性，并使用高错误校正。您也可以将其作为数据 URI 输出：
```php
$qrCodeDataUri = $qrCode->getDataUri();
```
这对于嵌入 HTML 非常有用，例如 `<img src="<?php echo $qrCodeDataUri; ?>">`。

然而，由于 2.2.2 版本较旧，某些类（例如 `ErrorCorrectionLevelHigh`）可能命名不同（例如，较旧版本中为 `ErrorCorrectionLevel::HIGH`）。Stack Overflow 文章 ([Stack Overflow](https://stackoverflow.com/questions/40777377/endroid-qr-code)) 的研究表明，较旧版本使用了 `setErrorCorrection('high')` 等方法，因此请验证 2.2.2 的 API。

##### 直接使用 QrCode 类
对于更多控制，可以使用 QrCode 类，如示例所示：
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
这种方法更冗长，但允许细调，例如设置前景和背景颜色，这对于 2.2.2 版本可能相关。同样，请检查文档以确认方法的可用性。

#### 配置选项
该库支持各种编写器以生成不同的输出格式，如下表所示，基于当前文档，并注意验证 2.2.2 版本：

| 编写器类          | 格式   | 说明                                                                 |
|-----------------------|----------|----------------------------------------------------------------------|
| PngWriter             | PNG      | 压缩级别可配置，默认 -1                           |
| SvgWriter             | SVG      | 适用于矢量图形，无压缩选项                 |
| WebPWriter            | WebP     | 质量 0-100，默认 80，适合网页使用                          |
| PdfWriter             | PDF      | 单位为毫米，默认，适合打印                                 |

编码选项包括 UTF-8（默认）和 ISO-8859-1，后者建议用于条形码扫描器兼容性。圆块大小模式（边距、放大、缩小、无）可以提高可读性，但需要确认 2.2.2 中的可用性。

#### 高级功能和考虑因素
对于高级用途，例如嵌入标志，Builder 类支持 `logoPath()` 和 `logoResizeToWidth()` 等方法，如 Medium 文章 ([Medium](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)) 所示。然而，这些可能是 2.2.2 之后的添加，因此需要测试兼容性。生成的 QR 码的验证是可能的，但会影响性能，默认情况下禁用，这是 [GitHub](https://github.com/endroid/qr-code) 的细节。

鉴于 [Packagist](https://packagist.org/packages/endroid/qr-code) 上的废弃说明，值得注意潜在的安全或维护问题，尽管对于基本用途，它仍然可行。对于 Symfony 用户，有一个捆绑包 ([GitHub](https://github.com/endroid/qr-code-bundle))，但这超出了一般的 PHP 使用范围。

#### 版本特定说明
研究表明，没有直接的 2.2.2 版本文档，GitHub 标签未列出它，这表明它可能是较旧的发布版本或拼写错误。当前存储库显示版本至 6.0.0，[Packagist](https://packagist.org/packages/endroid/qr-code) 列出它为废弃，建议 endroid/qr-code，这令人困惑，因为它是同一个包。这表明可能存在重命名或版本控制问题，因此用户应锁定依赖项并测试升级。

#### 结论
使用 "endroid/qr-code" 版本 2.2.2 涉及通过 Composer 安装，确保 GD 扩展，并使用 Builder 或 QrCode 类生成 QR 码。虽然示例基于当前文档，但请验证 2.2.2 的 API 差异，特别是高级功能。有关更多详细信息，请参阅库的 GitHub 页面和相关 Stack Overflow 讨论。

#### 关键引用
- [QR 码生成器 GitHub 存储库](https://github.com/endroid/qr-code)
- [endroid/qr-code Packagist 页面](https://packagist.org/packages/endroid/qr-code)
- [在 PHP 中创建带嵌入图像的 QR 码 Medium 文章](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)
- [Endroid QR 码 Stack Overflow 讨论](https://stackoverflow.com/questions/40777377/endroid-qr-code)