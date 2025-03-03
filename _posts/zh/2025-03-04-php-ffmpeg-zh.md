---
audio: false
generated: true
lang: zh
layout: post
title: 使用 ffmpeg 在 PHP 中
translated: true
---

### 关键点
- 使用 "php-ffmpeg/php-ffmpeg" 版本 ~0.5 似乎首先需要在系统上安装 FFMpeg，然后使用 Composer 安装 PHP 库。
- 研究表明，包括自动加载文件并创建 `FFMpeg\FFMpeg` 的实例进行媒体操作，如果需要可以指定二进制路径。
- 证据倾向于使用 `open()`、`save()` 和 `frame()` 等方法进行基本操作，但请查看 GitHub 文档以获取完整详细信息，因为可能存在版本特定的差异。

---

### 安装
首先，确保系统上安装了 FFMpeg：
- 在 Ubuntu 上，使用 `sudo apt-get install ffmpeg`。
- 在 macOS 上，使用 `brew install ffmpeg`。
- 在 Windows 上，从 [此网站](https://www.gyan.dev/ffmpeg/builds/) 下载并按照说明进行操作。

接下来，通过 Composer 安装 php-FFMpeg 库：
```
composer require php-FFMpeg/php-FFMpeg:~0.5
```

### 设置和使用
在 PHP 脚本中包含自动加载文件：
```php
require_once 'vendor/autoload.php';
```

创建 `FFMpeg\FFMpeg` 的实例，如果 FFMpeg 二进制文件不在系统 PATH 中，可以选择指定路径：
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'binary' => '/path/to/FFMpeg',
    'ffprobe' => '/path/to/FFprobe'
));
```

打开媒体文件并执行操作，例如：
- 转码：`$video->save('output.mp4', new FFMpeg\Format\Video\X264());`
- 提取帧：`$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5)); $frame->save('frame.jpg');`
- 剪辑：`$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20)); $clip->save('clip.mp4');`

有关更多详细信息，请参阅库的文档 [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)。

---

### 问卷说明：使用 php-FFMpeg/php-FFMpeg 版本 ~0.5 的全面指南

本说明深入探讨了使用 "php-FFMpeg/php-FFMpeg" 库的方法，特别是版本约为 0.5，基于可用信息。它扩展了直接答案，包括所有相关详细信息，确保用户在实现此 PHP 库进行媒体操作时能够全面理解。

#### 背景和上下文
"php-FFMpeg/php-FFMpeg" 库是 FFMpeg 二进制文件的 PHP 包装器，使对象化操作视频和音频文件成为可能。它支持转码、帧提取、剪辑等任务，对于从事媒体相关应用程序的开发人员非常有价值。版本规范 "~0.5" 表示任何大于或等于 0.5 且小于 1.0 的版本，暗示与较旧的 PHP 版本兼容，可能在存储库的 0.x 分支中找到。

鉴于当前日期为 2025 年 3 月 3 日，以及库的演变，版本 0.5 可能是遗留支持的一部分，主分支现在需要 PHP 8.0 或更高版本。本说明假设用户在该版本的约束下工作，承认与较新版本相比可能存在功能差异。

#### 安装过程
首先，必须在系统上安装 FFMpeg，因为库依赖其二进制文件进行操作。安装方法因操作系统而异：
- **Ubuntu**：使用命令 `sudo apt-get install ffmpeg` 通过包管理器进行安装。
- **macOS**：使用 Homebrew 进行安装，命令为 `brew install ffmpeg`。
- **Windows**：从 [此网站](https://www.gyan.dev/ffmpeg/builds/) 下载 FFMpeg 二进制文件并按照提供的说明进行操作，确保可执行文件在系统 PATH 中可访问或手动指定。

安装 FFMpeg 后，通过 Composer 安装 php-FFMpeg 库，这是 PHP 包管理器。命令 `composer require php-FFMpeg/php-FFMpeg:~0.5` 确保获取正确的版本。此过程在项目中创建一个 `vendor` 目录，其中包含库及其依赖项，Composer 管理自动加载以实现无缝集成。

#### 设置和初始化
安装后，在 PHP 脚本中包含自动加载文件以访问库的类：
```php
require_once 'vendor/autoload.php';
```

创建 `FFMpeg\FFMpeg` 的实例以开始使用库。创建方法支持配置，特别是如果 FFMpeg 二进制文件不在系统 PATH 中：
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'timeout' => 0,
    'thread_count' => 12,
    'binary' => '/path/to/your/own/FFMpeg',
    'ffprobe' => '/path/to/your/own/FFprobe'
));
```
此配置支持设置超时、线程计数和显式二进制路径，增强了不同系统设置的灵活性。默认设置在 PATH 中查找二进制文件，但手动指定确保兼容性，特别是在自定义环境中。

#### 核心使用和操作
库提供了流畅的对象化接口进行媒体操作。从打开媒体文件开始：
```php
$video = $ff->open('input.mp4');
```
这支持本地文件系统路径、HTTP 资源和其他 FFMpeg 支持的协议，支持类型列表可通过 `ffmpeg -protocols` 命令获取。

##### 转码
转码涉及将媒体转换为不同格式。使用 `save` 方法和格式实例：
```php
$format = new FFMpeg\Format\Video\X264();
$video->save('output.mp4', $format);
```
`X264` 格式是一个示例；库支持各种视频和音频格式，可以通过 `FFMpeg\Format\FormatInterface` 实现，具体接口如 `VideoInterface` 和 `AudioInterface` 适用于相应的媒体类型。

##### 帧提取
提取帧对于缩略图或分析非常有用。以下代码在 5 秒处提取一帧：
```php
$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5));
$frame->save('frame.jpg');
```
`TimeCode` 类是 `FFMpeg\Coordinate` 的一部分，确保精确定时，图像提取的精度有选项。

##### 剪辑
要剪辑视频的一部分，指定开始和结束时间：
```php
$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20));
$clip->save('clip.mp4');
```
这创建了一个新的视频段，保留了原始质量和格式，可以应用额外的过滤器（如果需要）。

#### 高级功能和考虑因素
库支持文档中概述的其他功能：
- **音频操作**：类似于视频，音频可以使用 `FFMpeg\Media\Audio::save` 转码，应用过滤器、添加元数据和重新采样。
- **GIF 创建**：可以使用 `FFMpeg\Media\Gif::save` 保存动画 GIF，带有可选的持续时间参数。
- **连接**：使用 `FFMpeg\Media\Concatenate::saveFromSameCodecs` 连接多个媒体文件，适用于相同编解码器，或 `saveFromDifferentCodecs` 适用于不同编解码器，有关更多资源，请参阅 [此链接](https://trac.ffmpeg.org/wiki/Concatenate)、[此链接](https://ffmpeg.org/ffmpeg-formats.html#concat-1) 和 [此链接](https://ffmpeg.org/ffmpeg.html#Stream-copy)。
- **高级媒体处理**：支持多个输入/输出，使用 `-filter_complex` 进行复杂过滤和映射，具有内置过滤器支持。
- **元数据提取**：使用 `FFMpeg\FFProbe::create` 提取元数据，使用 `FFMpeg\FFProbe::isValid` 验证文件（自 v0.10.0 可用，注意版本 0.5 可能缺少此功能）。

坐标，如 `FFMpeg\Coordinate\AspectRatio`、`Dimension`、`FrameRate`、`Point`（自 v0.10.0 动态）、`TimeCode`，提供对媒体属性的精确控制，但某些功能（如动态点）可能在版本 0.5 中不可用。

#### 版本特定说明
鉴于 "~0.5" 规范，库可能与 0.x 分支对齐，支持较旧的 PHP 版本。GitHub 存储库指示主分支需要 PHP 8.0 或更高版本，0.x 用于遗留支持。然而，未在发布中明确找到版本 0.5 的详细信息，这可能是提交历史或分支提交的一部分。用户应验证兼容性，因为某些功能（例如某些坐标类型）可能需要 0.5 版本之外的版本。

#### 文档和进一步阅读
虽然 Read the Docs 页面 ([Read the Docs](https://FFMpeg-PHP.readthedocs.io/en/latest/)) 显示为空，但 GitHub 存储库 ([GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)) 包含 README 中的全面文档，涵盖 API 使用、格式和示例。这是版本 0.5 的主要资源，因为缺乏此遗留版本的特定在线文档。

#### 表：关键操作和方法摘要

| 操作               | 方法示例                                      | 描述                                      |
|-------------------------|----------------------------------------------------|-------------------------------------------------|
| 打开媒体文件         | `$ff->open('input.mp4')`                           | 加载媒体文件以进行操作             |
| 转码视频         | `$video->save('output.mp4', new X264())`           | 转换为指定格式                    |
| 提取帧           | `$video->frame(TimeCode::fromSeconds(5))->save('frame.jpg')` | 提取指定时间的帧，保存为图像 |
| 剪辑视频              | `$video->clip(TimeCode::fromSeconds(10), TimeCode::fromSeconds(20))->save('clip.mp4')` | 创建时间段之间的剪辑，保存为新文件   |
| 配置实例      | `FFMpeg::create(array('binary' => '/path/to/FFMpeg'))` | 设置自定义二进制路径和选项            |

此表总结了核心功能，帮助用户在实现库时进行快速参考。

#### 意外细节：遗留版本的含义
意外的方面是版本 0.5 的潜在限制，鉴于其在 0.x 分支中用于较旧的 PHP 支持。这可能限制对现代功能（例如在 v0.10.0 中引入的动态坐标点）的访问，要求用户检查分支提交以获取精确功能，增加了与较新版本相比不立即明显的复杂性。

#### 结论
使用 "php-FFMpeg/php-FFMpeg" 版本 ~0.5 涉及安装 FFMpeg、通过 Composer 设置以及利用对象化 API 进行媒体任务。虽然基本操作（如转码和帧提取）非常直观，但版本特定的差异可能需要参考 0.x 分支文档 [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)。这种全面的方法确保用户能够有效利用库，同时承认其强大功能和潜在的遗留约束。

---

### 关键引用
- [FFMpeg PHP 对象化库 Packagist](https://packagist.org/products/php-FFMpeg/php-FFMpeg)
- [PHP-FFMpeg GitHub 存储库文档](https://github.com/PHP-FFMpeg/PHP-FFMpeg)
- [FFMpeg PHP Read the Docs 文档](https://FFMpeg-PHP.readthedocs.io/en/latest/)
- [FFMpeg 下载和构建网站](https://www.gyan.dev/ffmpeg/builds/)
- [FFMpeg 连接维基页面](https://trac.ffmpeg.org/wiki/Concatenate)
- [FFMpeg 格式文档页面](https://ffmpeg.org/ffmpeg-formats.html#concat-1)
- [FFMpeg 命令行工具文档](https://ffmpeg.org/ffmpeg.html#Stream-copy)