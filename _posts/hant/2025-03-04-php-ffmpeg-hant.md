---
audio: false
generated: true
lang: hant
layout: post
title: 在 PHP 中使用 ffmpeg
translated: true
type: note
---

### 重點摘要
- 要使用 "php-ffmpeg/php-ffmpeg" 版本 ~0.5，似乎需要先安裝 FFMpeg 到系統中，然後使用 Composer 安裝該 PHP 函式庫。
- 研究指出需要引入自動載入檔案，並建立 `FFMpeg\FFMpeg` 的實例來進行媒體操作，如有需要可指定二進位檔路徑。
- 證據傾向於使用如 `open()`、`save()` 和 `frame()` 等方法進行基本操作，但由於可能存在版本差異，請查閱 GitHub 上的文件以獲取完整詳情。

---

### 安裝
首先，確保系統中已安裝 FFMpeg：
- 在 Ubuntu 上，使用 `sudo apt-get install ffmpeg`。
- 在 macOS 上，使用 `brew install ffmpeg`。
- 在 Windows 上，請從[此網站](https://www.gyan.dev/ffmpeg/builds/)下載並按照指示操作。

接著，透過 Composer 安裝 php-FFMpeg 函式庫：
```
composer require php-FFMpeg/php-FFMpeg:~0.5
```

### 設定與使用
在您的 PHP 腳本中引入自動載入檔案：
```php
require_once 'vendor/autoload.php';
```

建立 `FFMpeg\FFMpeg` 的實例，如果 FFMpeg 二進位檔不在系統 PATH 中，可選擇指定路徑：
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'binary' => '/path/to/FFMpeg',
    'ffprobe' => '/path/to/FFprobe'
));
```

開啟媒體檔案並執行操作，例如：
- 轉碼：`$video->save('output.mp4', new FFMpeg\Format\Video\X264());`
- 擷取影格：`$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5)); $frame->save('frame.jpg');`
- 剪輯片段：`$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20)); $clip->save('clip.mp4');`

更多詳情，請參閱函式庫在 [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg) 上的文件。

---

### 調查備註：使用 php-FFMpeg/php-FFMpeg 版本 ~0.5 的完整指南

本備註基於現有資訊，深入探討如何使用 "php-FFMpeg/php-FFMpeg" 函式庫，特別是版本約 0.5。它擴展了直接答案，包含了研究中的所有相關細節，確保尋求實作此 PHP 函式庫進行媒體操作的用戶能獲得全面理解。

#### 背景與情境
"php-FFMpeg/php-FFMpeg" 函式庫是 FFMpeg 二進位檔的 PHP 封裝，允許以物件導向的方式操作影片和音訊檔案。它支援轉碼、影格擷取、剪輯等任務，對於開發媒體相關應用的開發者非常有價值。版本規格 "~0.5" 表示任何大於或等於 0.5 且小於 1.0 的版本，暗示其與舊版 PHP 相容，很可能屬於儲存庫中 0.x 分支的一部分。

考慮到當前日期為 2025 年 3 月 3 日，以及函式庫的演進，版本 0.5 可能屬於舊版支援，而主分支現在要求 PHP 8.0 或更高版本。本備註假設用戶在此版本的限制下工作，並承認與新版本相比可能存在功能差異。

#### 安裝流程
首先，必須在系統中安裝 FFMpeg，因為函式庫依賴其二進位檔進行操作。安裝方法因作業系統而異：
- **Ubuntu**：使用指令 `sudo apt-get install ffmpeg` 透過套件管理員安裝。
- **macOS**：使用 Homebrew 執行 `brew install ffmpeg` 進行簡單安裝。
- **Windows**：從[此網站](https://www.gyan.dev/ffmpeg/builds/)下載 FFMpeg 二進位檔，並按照提供的指示操作，確保可執行檔可在系統 PATH 中存取或手動指定。

安裝 FFMpeg 後，透過 PHP 套件管理員 Composer 安裝 php-FFMpeg 函式庫。指令 `composer require php-FFMpeg/php-FFMpeg:~0.5` 確保獲取正確版本。此過程會在專案中建立一個 `vendor` 目錄，存放函式庫及其依賴項，並由 Composer 管理自動載入以實現無縫整合。

#### 設定與初始化
安裝後，在 PHP 腳本中引入自動載入檔案以啟用對函式庫類別的存取：
```php
require_once 'vendor/autoload.php';
```

建立 `FFMpeg\FFMpeg` 的實例以開始使用函式庫。建立方法允許進行配置，特別是當 FFMpeg 二進位檔不在系統 PATH 中時尤其重要：
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'timeout' => 0,
    'thread_count' => 12,
    'binary' => '/path/to/your/own/FFMpeg',
    'ffprobe' => '/path/to/your/own/FFprobe'
));
```
此配置支援設定逾時時間、執行緒數量和明確的二進位檔路徑，增強了對不同系統設定的靈活性。預設設定會在 PATH 中尋找二進位檔，但手動指定可確保相容性，特別是在自訂環境中。

#### 核心用法與操作
函式庫提供流暢的物件導向介面用於媒體操作。首先開啟媒體檔案：
```php
$video = $ff->open('input.mp4');
```
這支援本地檔案系統路徑、HTTP 資源以及其他 FFMpeg 支援的協定，支援的類型清單可透過 `ffmpeg -protocols` 指令查閱。

##### 轉碼
轉碼涉及將媒體轉換為不同格式。使用帶有格式實例的 `save` 方法：
```php
$format = new FFMpeg\Format\Video\X264();
$video->save('output.mp4', $format);
```
`X264` 格式是一個例子；函式庫支援各種影片和音訊格式，可透過 `FFMpeg\Format\FormatInterface` 實作，並有特定介面如 `VideoInterface` 和 `AudioInterface` 用於各自的媒體類型。

##### 影格擷取
擷取影格對於縮圖或分析很有用。以下程式碼在 5 秒處擷取一個影格：
```php
$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5));
$frame->save('frame.jpg');
```
`TimeCode` 類別是 `FFMpeg\Coordinate` 的一部分，確保精確的時間控制，並提供影格擷取準確性的選項。

##### 剪輯
要剪輯影片的一部分，請指定開始和結束時間：
```php
$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20));
$clip->save('clip.mp4');
```
這會建立一個新的影片片段，保持原始品質和格式，並能夠在需要時套用其他濾鏡。

#### 進階功能與注意事項
如文件所述，函式庫支援其他功能：
- **音訊操作**：與影片類似，音訊可以使用 `FFMpeg\Media\Audio::save` 進行轉碼，套用濾鏡、添加元資料和重新取樣。
- **GIF 建立**：可以使用 `FFMpeg\Media\Gif::save` 儲存動畫 GIF，並帶有可選的持續時間參數。
- **串接**：使用 `FFMpeg\Media\Concatenate::saveFromSameCodecs` 合併多個相同編解碼器的媒體檔案，或使用 `saveFromDifferentCodecs` 處理不同編解碼器，進一步閱讀資源請參閱[此連結](https://trac.ffmpeg.org/wiki/Concatenate)、[此連結](https://ffmpeg.org/ffmpeg-formats.html#concat-1) 和 [此連結](https://ffmpeg.org/ffmpeg.html#Stream-copy)。
- **進階媒體處理**：支援使用 `-filter_complex` 處理多個輸入/輸出，對於複雜的濾鏡和映射很有用，並內建濾鏡支援。
- **元資料擷取**：使用 `FFMpeg\FFProbe::create` 獲取元資料，並使用 `FFMpeg\FFProbe::isValid` 驗證檔案（自 v0.10.0 起可用，請注意版本 0.5 可能缺少此功能）。

座標，例如 `FFMpeg\Coordinate\AspectRatio`、`Dimension`、`FrameRate`、`Point`（自 v0.10.0 起動態）和 `TimeCode`，提供了對媒體屬性的精確控制，儘管某些功能（如動態點）在版本 0.5 中可能不可用。

#### 版本特定注意事項
考慮到 "~0.5" 規格，函式庫很可能與 0.x 分支一致，支援舊版 PHP。GitHub 儲存庫指出主分支需要 PHP 8.0 或更高版本，而 0.x 用於舊版支援。然而，未在發布中明確找到確切版本 0.5 的細節，暗示它可能屬於提交歷史或分支提交的一部分。用戶應驗證相容性，因為某些新功能（如特定座標類型，例如動態點）可能需要版本 0.5 以上的版本。

#### 文件與進一步閱讀
雖然 Read the Docs 頁面 ([Read the Docs](https://FFMpeg-PHP.readthedocs.io/en/latest/)) 顯示為空白，但 GitHub 儲存庫 ([GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)) 的 README 中包含全面的文件，涵蓋 API 用法、格式和範例。考慮到此舊版本缺乏特定的線上文件，這是版本 0.5 的主要資源。

#### 表格：關鍵操作與方法摘要

| 操作               | 方法範例                                      | 描述                                      |
|--------------------|-----------------------------------------------|-------------------------------------------|
| 開啟媒體檔案       | `$ff->open('input.mp4')`                      | 載入媒體檔案以進行操作                    |
| 轉碼影片           | `$video->save('output.mp4', new X264())`      | 轉換為指定格式                            |
| 擷取影格           | `$video->frame(TimeCode::fromSeconds(5))->save('frame.jpg')` | 在指定時間擷取影格，儲存為影像            |
| 剪輯影片           | `$video->clip(TimeCode::fromSeconds(10), TimeCode::fromSeconds(20))->save('clip.mp4')` | 在時間點之間建立剪輯片段，儲存為新檔案    |
| 設定實例           | `FFMpeg::create(array('binary' => '/path/to/FFMpeg'))` | 設定自訂二進位檔路徑和選項                |

此表格封裝了核心功能，協助用戶在實作函式庫時快速參考。

#### 意外細節：舊版本的影響
一個意外的方面是版本 0.5 的潛在限制，考慮到它位於 0.x 分支以支援舊版 PHP。這可能會限制對現代功能的存取，例如 v0.10.0 中引入的動態座標點，要求用戶檢查分支提交以獲取確切功能，增加了在新版本中不明顯的複雜性。

#### 結論
使用 "php-FFMpeg/php-FFMpeg" 版本 ~0.5 涉及安裝 FFMpeg、透過 Composer 進行設定，並利用物件導向 API 進行媒體任務。雖然基本操作如轉碼和影格擷取很直接，但版本特定差異可能需要查閱 [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg) 上的 0.x 分支文件。這種全面的方法確保用戶能夠有效利用函式庫，同時承認其強大功能和潛在的舊版限制。

---

### 主要引用來源
- [FFMpeg PHP Object Oriented Library Packagist](https://packagist.org/products/php-FFMpeg/php-FFMpeg)
- [PHP-FFMpeg GitHub Repository Documentation](https://github.com/PHP-FFMpeg/PHP-FFMpeg)
- [FFMpeg PHP Read the Docs Documentation](https://FFMpeg-PHP.readthedocs.io/en/latest/)
- [FFMpeg Download and Builds Website](https://www.gyan.dev/ffmpeg/builds/)
- [FFMpeg Concatenation Wiki Page](https://trac.ffmpeg.org/wiki/Concatenate)
- [FFMpeg Formats Documentation Page](https://ffmpeg.org/ffmpeg-formats.html#concat-1)
- [FFMpeg Command Line Tool Documentation](https://ffmpeg.org/ffmpeg.html#Stream-copy)