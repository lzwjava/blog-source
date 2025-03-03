---
audio: false
generated: true
lang: hant
layout: post
title: Pili 串流雲端圖書館 for PHP
translated: true
---

### 主要要點
- 使用 "pili-engineering/pili-sdk-php": "dev-master" 似乎需要通過 Composer 安裝並設置 Qiniu 認證。
- 研究表明該套件需要 PHP 5.3.0 或更高版本，適用於 Pili Streaming Cloud，與 Qiniu 相關。
- 證據顯示需要創建一個 Hub 對象並使用流操作，例如生成 RTMP URL，但具體方法可能會有所不同。

### 安裝
首先，確保已安裝 Composer。在 `composer.json` 文件中添加套件：
```json
"require": {
    "pili-engineering/pili-sdk-php": "dev-master"
}
```
然後，運行 `composer install` 或 `composer update`。在 PHP 腳本中，包含：
```php
require 'vendor/autoload.php';
```

### 設置和使用
您需要一個 Qiniu 帳戶和一個 Pili Hub。設置您的訪問密鑰、秘密密鑰和 Hub 名稱，然後創建一個 Hub 對象：
```php
use Qiniu\Credentials;
use Pili\Hub;

$credentials = new Credentials('your_access_key', 'your_secret_key');
$hub = new Hub($credentials, 'your_hub_name');
```
創建或獲取一個流，例如 `$stream = $hub->createStream('your_stream_key');`，並使用方法如 `$stream->rtmpPublishUrl(60)` 進行操作。

### 意外細節
請注意，"dev-master" 是一個開發版本，可能不穩定，有標記版本如 1.5.5 可用於生產。

---

### 使用 "pili-engineering/pili-sdk-php": "dev-master" 的全面指南

本指南提供了如何使用 "pili-engineering/pili-sdk-php" 套件的詳細探討，基於可用的文檔和示例。它涵蓋了安裝、設置、使用和其他考慮，確保開發人員在使用 Pili Streaming Cloud 服務時有全面的理解。

#### 背景和上下文
"pili-engineering/pili-sdk-php" 套件是一個 PHP 伺服器端庫，旨在與 Pili Streaming Cloud 互動，這是一項與 Qiniu 相關的雲存儲和 CDN 提供商的服務。"dev-master" 版本指的是最新的開發分支，可能包含最新的功能，但可能不如標記版本穩定。該套件需要 PHP 5.3.0 或更高版本，使其對於許多 PHP 環境（截至 2025 年 3 月 3 日）可訪問。

#### 安裝過程
首先，您必須安裝 Composer，這是 PHP 的依賴管理器。安裝過程涉及將套件添加到項目的 `composer.json` 文件中，並運行 Composer 命令來下載它。具體來說：

- 在 "require" 部分添加以下內容：
  ```json
  "require": {
      "pili-engineering/pili-sdk-php": "dev-master"
  }
  ```
- 在終端中執行 `composer install` 或 `composer update` 以獲取套件及其依賴項。這將創建一個包含必要文件的 `vendor` 目錄。
- 在您的 PHP 腳本中，包含自動加載器以訪問套件類：
  ```php
  require 'vendor/autoload.php';
  ```

這個過程確保了套件被整合到您的項目中，利用 Composer 的自動加載來輕鬆訪問類。

#### 預先條件和設置
在使用 SDK 之前，您需要一個 Qiniu 帳戶，並且必須設置一個 Pili Hub，因為 SDK 會與 Pili Streaming Cloud 服務進行交互。這涉及從 Qiniu 获取訪問密鑰和秘密密鑰，並在其平台上創建一個 Hub。文檔建議這些憑證對於身份驗證是必需的。

在 PHP 腳本中設置您的憑證：
- 訪問密鑰：您的 Qiniu 訪問密鑰。
- 秘密密鑰：您的 Qiniu 秘密密鑰。
- Hub 名稱：您的 Pili Hub 名稱，必須在使用之前存在。

一個示例設置如下：
```php
$accessKey = 'your_access_key';
$secretKey = 'your_secret_key';
$hubName = 'your_hub_name';
```

#### 創建和使用 Hub 對象
SDK 的核心是 Hub 對象，它促進流管理。首先，使用您的 Qiniu 密鑰創建一個 Credentials 對象：
```php
use Qiniu\Credentials;

$credentials = new Credentials($accessKey, $secretKey);
```
然後，使用這些憑證和您的 Hub 名稱實例化一個 Hub 對象：
```php
use Pili\Hub;

$hub = new Hub($credentials, $hubName);
```
這個 Hub 對象允許您執行各種流相關操作，例如創建、檢索或列出流。

#### 使用流
流是 Pili Streaming Cloud 的核心，SDK 提供了通過 Hub 對象管理它們的方法。要創建一個新流：
```php
$streamKey = 'your_stream_key'; // 必須在 Hub 中唯一
$stream = $hub->createStream($streamKey);
```
要檢索現有流：
```php
$stream = $hub->getStream($streamKey);
```
然後，流對象提供各種方法進行操作，以下表格基於可用文檔進行詳細說明：

| **操作**          | **方法**                     | **描述**                                      |
|-------------------------|--------------------------------|------------------------------------------------------|
| 創建流          | `$hub->createStream($key)`     | 使用給定密鑰創建新流。             |
| 获取流             | `$hub->getStream($key)`        | 通過密鑰檢索現有流。                 |
| 列出流           | `$hub->listStreams($marker, $limit, $prefix)` | 列出流，帶有分頁選項。               |
| RTMP 發布 URL       | `$stream->rtmpPublishUrl($expire)` | 生成帶有過期時間的 RTMP 發布 URL。  |
| RTMP 播放 URL          | `$stream->rtmpPlayUrl()`       | 生成流的 RTMP 播放 URL。           |
| HLS 播放 URL           | `$stream->hlsPlayUrl()`        | 生成流的 HLS 播放 URL。             |
| 禁用流         | `$stream->disable()`           | 禁用流。                                 |
| 启用流          | `$stream->enable()`            | 启用流。                                  |
| 获取流狀態      | `$stream->status()`            | 檢索流的當前狀態。          |

例如，生成一個 60 秒過期的 RTMP 發布 URL：
```php
$expire = 60;
$url = $stream->rtmpPublishUrl($expire);
echo $url;
```
這個 URL 可以用於將流發布到 Pili Streaming Cloud，過期時間確保了臨時訪問。

#### 其他考慮
- **版本穩定性**："dev-master" 版本是開發分支，可能不穩定。對於生產，考慮使用標記版本，例如 1.5.5，可在 Packagist 上找到 [pili-engineering/pili-sdk-php 版本](https://packagist.org/p/pili-engineering/pili-sdk-php)。歷史顯示更新，例如 API 添加和方法精炼，版本可追溯到 2016 年。
- **錯誤處理**：文檔建議使用 try-catch 塊進行操作，例如流創建和檢索的示例，以處理潛在的異常。
- **文檔和示例**：雖然沒有詳細列出具體示例，但 GitHub 存儲庫 [Pili Streaming Cloud 伺服器端庫 PHP](https://github.com/pili-engineering/pili-sdk-php) 提供了安裝指示和功能列表，並與其他語言 SDK（例如 Python）進行了比較，顯示了相似的功能，例如 URL 生成。

#### 比較見解
與其他 Pili SDK（例如 Python 版本）相比，顯示了相似的模式：兩者都需要憑證、 Hub 設置和流操作。然而，PHP 版本使用了面向對象的方法，具有 Hub 和 Stream 類，與 Python 的更功能性風格形成對比。這與 PHP 的典型開發實踐一致，提供了類型安全和 IDE 支持。

#### 結論
使用 "pili-engineering/pili-sdk-php": "dev-master" 涉及通過 Composer 安裝，設置 Qiniu 認證，創建一個 Hub 對象，並使用方法如 `rtmpPublishUrl` 管理流。確保您的環境滿足 PHP 5.3.0+ 要求，並考慮生產使用的穩定性。本指南提供了全面的起點，更多詳細信息可在官方文檔和存儲庫中找到。

### 主要引用
- [Pili Streaming Cloud 伺服器端庫 PHP GitHub](https://github.com/pili-engineering/pili-sdk-php)
- [pili-engineering/pili-sdk-php 版本 Packagist](https://packagist.org/p/pili-engineering/pili-sdk-php)