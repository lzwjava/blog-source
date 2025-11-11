---
audio: false
generated: true
lang: hant
layout: post
title: Pili 串流雲端 PHP 函式庫
translated: true
type: note
---

### 重點摘要
- 要使用 "pili-engineering/pili-sdk-php": "dev-master"，似乎需要透過 Composer 安裝並設定七牛憑證。
- 研究顯示該套件需要 PHP 5.3.0 或更高版本，用於七牛直播雲服務。
- 證據顯示需要建立 Hub 物件並使用串流操作（如生成 RTMP 網址），但具體方法可能有所不同。

### 安裝步驟
首先確保已安裝 Composer。將套件加入您的 `composer.json` 檔案：
```json
"require": {
    "pili-engineering/pili-sdk-php": "dev-master"
}
```
接著執行 `composer install` 或 `composer update`。在 PHP 腳本中加入：
```php
require 'vendor/autoload.php';
```

### 設定與使用
您需要擁有七牛帳號和 Pili Hub。設定您的存取金鑰、秘密金鑰和 hub 名稱，然後建立 Hub 物件：
```php
use Qiniu\Credentials;
use Pili\Hub;

$credentials = new Credentials('your_access_key', 'your_secret_key');
$hub = new Hub($credentials, 'your_hub_name');
```
建立或取得串流，例如 `$stream = $hub->createStream('your_stream_key');`，並使用如 `$stream->rtmpPublishUrl(60)` 等方法進行操作。

### 注意事項
請注意 "dev-master" 為開發版本，可能不穩定，生產環境建議使用如 1.5.5 等標籤版本。

---

### 使用 "pili-engineering/pili-sdk-php": "dev-master" 完整指南

本指南詳細探討如何使用 "pili-engineering/pili-sdk-php" 套件的 "dev-master" 版本，涵蓋安裝、設定、使用及相關注意事項，幫助開發者全面理解如何運用七牛直播雲服務。

#### 背景與環境
"pili-engineering/pili-sdk-php" 是 PHP 的伺服器端函式庫，用於與七牛直播雲服務互動。"dev-master" 版本指最新的開發分支，可能包含新功能但穩定性較標籤版本低。該套件要求 PHP 5.3.0 或更高版本，截至 2025年3月3日 仍適用於多數 PHP 環境。

#### 安裝流程
首先需安裝 Composer（PHP 相依性管理工具）。安裝步驟包含將套件加入專案的 `composer.json` 檔案並執行 Composer 指令：

- 在 `composer.json` 的 "require" 區段加入：
  ```json
  "require": {
      "pili-engineering/pili-sdk-php": "dev-master"
  }
  ```
- 在終端機執行 `composer install` 或 `composer update` 下載套件及其相依項目，這將建立包含必要檔案的 `vendor` 目錄。
- 在 PHP 腳本中引入自動載入器以存取套件類別：
  ```php
  require 'vendor/autoload.php';
  ```

此流程確保套件整合至專案，並利用 Composer 的自動載入功能方便類別存取。

#### 必要條件與設定
使用 SDK 前需擁有七牛帳號並設定 Pili Hub，因為 SDK 需與七牛直播雲服務互動。這包含從七牛取得存取金鑰和秘密金鑰，並在平台上建立 hub。文件顯示這些憑證是驗證的必要條件。

設定時在 PHP 腳本中定義憑證：
- 存取金鑰：您的七牛存取金鑰
- 秘密金鑰：您的七牛秘密金鑰
- Hub 名稱：您的 Pili Hub 名稱（需預先建立）

設定範例：
```php
$accessKey = 'your_access_key';
$secretKey = 'your_secret_key';
$hubName = 'your_hub_name';
```

#### 建立與使用 Hub 物件
SDK 的核心是 Hub 物件，用於管理串流。首先使用七牛金鑰建立 Credentials 物件：
```php
use Qiniu\Credentials;

$credentials = new Credentials($accessKey, $secretKey);
```
接著使用這些憑證和 hub 名稱實例化 Hub 物件：
```php
use Pili\Hub;

$hub = new Hub($credentials, $hubName);
```
此 Hub 物件讓您能執行各種串流相關操作，如建立、擷取或列出串流。

#### 串流操作
串流是七牛直播雲的核心，SDK 透過 Hub 物件提供管理方法。建立新串流：
```php
$streamKey = 'your_stream_key'; // 在 hub 內必須唯一
$stream = $hub->createStream($streamKey);
```
擷取現有串流：
```php
$stream = $hub->getStream($streamKey);
```
串流物件提供多種操作方法，詳見以下基於文件的表格：

| **操作類型**          | **方法**                     | **說明**                                      |
|-------------------------|--------------------------------|------------------------------------------------------|
| 建立串流          | `$hub->createStream($key)`     | 以指定金鑰建立新串流             |
| 取得串流             | `$hub->getStream($key)`        | 依金鑰擷取現有串流                 |
| 列出串流           | `$hub->listStreams($marker, $limit, $prefix)` | 以分頁選項列出串流               |
| RTMP 發布網址       | `$stream->rtmpPublishUrl($expire)` | 生成具有效期的 RTMP 發布網址  |
| RTMP 播放網址          | `$stream->rtmpPlayUrl()`       | 生成串流的 RTMP 播放網址           |
| HLS 播放網址           | `$stream->hlsPlayUrl()`        | 生成串流的 HLS 播放網址             |
| 停用串流         | `$stream->disable()`           | 停用串流                                 |
| 啟用串流          | `$stream->enable()`            | 啟用串流                                  |
| 取得串流狀態      | `$stream->status()`            | 擷取串流當前狀態          |

例如生成 60 秒有效期的 RTMP 發布網址：
```php
$expire = 60;
$url = $stream->rtmpPublishUrl($expire);
echo $url;
```
此網址可用於向七牛直播雲發布串流，有效期確保暫時存取權限。

#### 其他注意事項
- **版本穩定性**："dev-master" 版本為開發分支，可能不穩定。生產環境建議使用標籤版本，如 Packagist 上提供的 1.5.5 版 [pili-engineering/pili-sdk-php 版本](https://packagist.org/p/pili-engineering/pili-sdk-php)。歷史更新顯示 API 新增和方法改進，版本可追溯至 2016年。
- **錯誤處理**：文件建議在操作時使用 try-catch 區塊處理潛在例外情況。
- **文件與範例**：雖然具體範例未詳細說明，GitHub 儲存庫 [Pili Streaming Cloud server-side library for PHP](https://github.com/pili-engineering/pili-sdk-php) 提供安裝說明和功能列表，與其他語言 SDK（如 Python）的比較顯示類似功能（如網址生成）。

#### 比較分析
與其他 Pili SDK（如 Python 版）比較顯示相似模式：都需要憑證、hub 設定和串流操作。但 PHP 版採用物件導向設計（Hub 和 Stream 類別），與 Python 的函數式風格形成對比。這符合 PHP 典型開發實踐，提供型別安全和 IDE 支援。

#### 總結
使用 "pili-engineering/pili-sdk-php": "dev-master" 需透過 Composer 安裝、設定七牛憑證、建立 Hub 物件，並使用如 `rtmpPublishUrl` 等方法管理串流。請確保環境符合 PHP 5.3.0+ 要求，並考量生產環境的穩定性。本指南提供完整入門指引，更多細節請參考官方文件和儲存庫。

### 主要參考來源
- [Pili Streaming Cloud server-side library for PHP GitHub](https://github.com/pili-engineering/pili-sdk-php)
- [pili-engineering/pili-sdk-php versions Packagist](https://packagist.org/p/pili-engineering/pili-sdk-php)