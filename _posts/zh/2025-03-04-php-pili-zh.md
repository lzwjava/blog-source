---
audio: false
generated: true
lang: zh
layout: post
title: Pili 云流媒体库 for PHP
translated: true
---

### 关键点
- 使用 "pili-engineering/pili-sdk-php": "dev-master" 似乎需要通过 Composer 安装，并设置七牛云凭证。
- 研究表明，该包需要 PHP 5.3.0 或更高版本，适用于七牛云的 Pili 流媒体云。
- 证据表明需要创建一个 Hub 对象并使用流操作，如生成 RTMP URL，但具体方法可能会有所不同。

### 安装
首先，确保已经安装了 Composer。在 `composer.json` 文件中添加包：
```json
"require": {
    "pili-engineering/pili-sdk-php": "dev-master"
}
```
然后，运行 `composer install` 或 `composer update`。在 PHP 脚本中包含：
```php
require 'vendor/autoload.php';
```

### 设置和使用
您需要一个七牛云账户和一个 Pili Hub。设置您的访问密钥、秘密密钥和 Hub 名称，然后创建一个 Hub 对象：
```php
use Qiniu\Credentials;
use Pili\Hub;

$credentials = new Credentials('your_access_key', 'your_secret_key');
$hub = new Hub($credentials, 'your_hub_name');
```
创建或获取一个流，例如 `$stream = $hub->createStream('your_stream_key')`，并使用方法如 `$stream->rtmpPublishUrl(60)` 进行操作。

### 意外细节
请注意，"dev-master" 是一个开发版本，可能不稳定，有标记版本如 1.5.5 可用于生产。

---

### 使用 "pili-engineering/pili-sdk-php": "dev-master" 的全面指南

本指南详细探讨了如何使用 "pili-engineering/pili-sdk-php" 包的 "dev-master" 版本，基于可用的文档和示例。它涵盖了安装、设置、使用和其他考虑因素，确保开发人员在使用 Pili 流媒体云服务时有全面的理解。

#### 背景和上下文
"pili-engineering/pili-sdk-php" 包是一个为 PHP 设计的服务器端库，用于与 Pili 流媒体云交互，这是与七牛云（云存储和 CDN 提供商）相关的服务。"dev-master" 版本指的是最新的开发分支，可能包含最新的功能，但可能不如标记版本稳定。该包需要 PHP 5.3.0 或更高版本，因此适用于许多 PHP 环境，截至 2025 年 3 月 3 日。

#### 安装过程
首先，您必须安装 Composer，这是 PHP 的依赖管理器。安装过程涉及将包添加到项目的 `composer.json` 文件中，并运行 Composer 命令来下载它。具体来说：

- 在 "require" 部分添加以下内容到您的 `composer.json`：
  ```json
  "require": {
      "pili-engineering/pili-sdk-php": "dev-master"
  }
  ```
- 在终端中执行 `composer install` 或 `composer update` 以获取包及其依赖项。这将创建一个包含必要文件的 `vendor` 目录。
- 在您的 PHP 脚本中，包括自动加载器以访问包类：
  ```php
  require 'vendor/autoload.php';
  ```

此过程确保包集成到您的项目中，利用 Composer 的自动加载以便轻松访问类。

#### 先决条件和设置
在使用 SDK 之前，您需要一个七牛云账户，并必须设置一个 Pili Hub，因为 SDK 与 Pili 流媒体云服务交互。这涉及从七牛云获取访问密钥和秘密密钥，并在其平台上创建一个 Hub。文档建议这些凭证对身份验证至关重要。

在 PHP 脚本中设置您的凭证：
- 访问密钥：您的七牛云访问密钥。
- 秘密密钥：您的七牛云秘密密钥。
- Hub 名称：您的 Pili Hub 名称，必须在使用之前存在。

示例设置如下：
```php
$accessKey = 'your_access_key';
$secretKey = 'your_secret_key';
$hubName = 'your_hub_name';
```

#### 创建和使用 Hub 对象
SDK 的核心是 Hub 对象，它促进流管理。首先，使用您的七牛云密钥创建一个 Credentials 对象：
```php
use Qiniu\Credentials;

$credentials = new Credentials($accessKey, $secretKey);
```
然后，使用这些凭证和您的 Hub 名称实例化一个 Hub 对象：
```php
use Pili\Hub;

$hub = new Hub($credentials, $hubName);
```
此 Hub 对象允许您执行各种流相关的操作，例如创建、检索或列出流。

#### 使用流
流是 Pili 流媒体云的核心，SDK 提供方法通过 Hub 对象管理它们。要创建新流：
```php
$streamKey = 'your_stream_key'; // 必须在 Hub 内唯一
$stream = $hub->createStream($streamKey);
```
要检索现有流：
```php
$stream = $hub->getStream($streamKey);
```
然后，流对象提供各种方法进行操作，以下表格基于可用文档详细说明：

| **操作**          | **方法**                     | **描述**                                      |
|-------------------------|--------------------------------|------------------------------------------------------|
| 创建流          | `$hub->createStream($key)`     | 使用给定密钥创建新流。             |
| 获取流             | `$hub->getStream($key)`        | 通过密钥检索现有流。                 |
| 列出流           | `$hub->listStreams($marker, $limit, $prefix)` | 列出流，带有分页选项。               |
| RTMP 发布 URL       | `$stream->rtmpPublishUrl($expire)` | 生成带有过期时间的 RTMP 发布 URL。  |
| RTMP 播放 URL          | `$stream->rtmpPlayUrl()`       | 生成流的 RTMP 播放 URL。           |
| HLS 播放 URL           | `$stream->hlsPlayUrl()`        | 生成流的 HLS 播放 URL。             |
| 禁用流         | `$stream->disable()`           | 禁用流。                                 |
| 启用流          | `$stream->enable()`            | 启用流。                                  |
| 获取流状态      | `$stream->status()`            | 检索流的当前状态。          |

例如，生成一个 60 秒过期的 RTMP 发布 URL：
```php
$expire = 60;
$url = $stream->rtmpPublishUrl($expire);
echo $url;
```
此 URL 可以用于将流发布到 Pili 流媒体云，过期时间确保临时访问。

#### 附加考虑
- **版本稳定性**："dev-master" 版本是开发分支，可能不稳定。对于生产，考虑使用标记版本，例如 1.5.5，可在 Packagist 上找到 [pili-engineering/pili-sdk-php 版本](https://packagist.org/p/pili-engineering/pili-sdk-php)。历史显示更新，如 API 添加和方法改进，版本可追溯到 2016 年。
- **错误处理**：文档建议使用 try-catch 块进行操作，如流创建和检索示例中所示，以处理潜在异常。
- **文档和示例**：虽然没有详细列出具体示例，但 GitHub 仓库 [Pili 流媒体云 PHP 服务器端库](https://github.com/pili-engineering/pili-sdk-php) 提供了安装说明和功能列表，与其他语言 SDK（例如 Python）的比较表明类似功能，例如 URL 生成。

#### 比较见解
与其他 Pili SDK（例如 Python 版本）相比，可以看出相似的模式：两者都需要凭证、Hub 设置和流操作。然而，PHP 版本使用面向对象的方法，具有 Hub 和 Stream 类，与 Python 的更功能化风格形成对比。这与 PHP 的典型开发实践一致，提供类型安全性和 IDE 支持。

#### 结论
使用 "pili-engineering/pili-sdk-php": "dev-master" 涉及通过 Composer 安装，设置七牛云凭证，创建 Hub 对象，并使用方法如 `rtmpPublishUrl` 管理流。确保您的环境满足 PHP 5.3.0+ 要求，并考虑生产使用的稳定性。本指南提供了全面的起点，更多详细信息可在官方文档和仓库中找到。

### 关键引用
- [Pili 流媒体云 PHP 服务器端库 GitHub](https://github.com/pili-engineering/pili-sdk-php)
- [pili-engineering/pili-sdk-php 版本 Packagist](https://packagist.org/p/pili-engineering/pili-sdk-php)