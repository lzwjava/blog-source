---
audio: false
generated: true
lang: hant
layout: post
title: 使用 ffmpeg 在 PHP 中
translated: true
---

### 關鍵要點
- 使用 "php-ffmpeg/php-ffmpeg" 版本 ~0.5，首先需要在系統上安裝 FFMpeg，然後使用 Composer 安裝 PHP 圖書館。
- 研究建議包含自動加載文件並創建 `FFMpeg\FFMpeg` 的實例進行媒體操作，並且可以指定二進制路徑（如果需要）。
- 方法如 `open()`、`save()` 和 `frame()` 用於基本操作，但請查閱 GitHub 文檔以獲取完整詳細信息，因為可能會有版本特定的差異。

---

### 安裝
首先，確保系統上已安裝 FFMpeg：
- 在 Ubuntu 上，使用 `sudo apt-get install ffmpeg`。
- 在 macOS 上，使用 `brew install ffmpeg`。
- 在 Windows 上，從 [這個網站](https://www.gyan.dev/ffmpeg/builds/) 下載並按照說明進行操作。

接下來，通過 Composer 安裝 php-FFMpeg 圖書館：
```
composer require php-FFMpeg/php-FFMpeg:~0.5
```

### 設置和使用
在 PHP 腳本中包含自動加載文件：
```php
require_once 'vendor/autoload.php';
```

創建 `FFMpeg\FFMpeg` 的實例，可選地指定路徑（如果 FFMpeg 二進制文件不在系統 PATH 中）：
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'binary' => '/path/to/FFMpeg',
    'ffprobe' => '/path/to/FFprobe'
));
```

打開媒體文件並執行操作，例如：
- 轉碼：`$video->save('output.mp4', new FFMpeg\Format\Video\X264());`
- 提取一個帧：`$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5)); $frame->save('frame.jpg');`
- 剪輯：`$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20)); $clip->save('clip.mp4');`

有關更多詳細信息，請參閱圖書館的文檔 [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)。

---

### 調查筆記：使用 php-FFMpeg/php-FFMpeg 版本 ~0.5 的全面指南

這篇筆記深入探討了使用 "php-FFMpeg/php-FFMpeg" 圖書館，特別是版本約 0.5，基於可用的信息。它擴展了直接答案，包括所有相關的研究細節，確保用戶在尋求實現這個 PHP 圖書館進行媒體操作時能夠全面理解。

#### 背景和背景
"php-FFMpeg/php-FFMpeg" 圖書館是 FFMpeg 二進制文件的 PHP 包裝器，使得對象導向的視頻和音頻文件操作成為可能。它支持轉碼、帧提取、剪輯等任務，對於從事媒體相關應用程序的開發人員來說非常有價值。版本規範 "~0.5" 表示任何大於或等於 0.5 且小於 1.0 的版本，這表明與較舊的 PHP 版本兼容，可能在 0.x 分支的存儲庫中找到。

考慮到當前日期為 2025 年 3 月 3 日，以及圖書館的演變，版本 0.5 可能是遺留支持的一部分，而主分支現在需要 PHP 8.0 或更高版本。這篇筆記假設用戶在這個版本的約束下工作，並且承認與較新版本相比，功能可能會有所不同。

#### 安裝過程
首先，必須在系統上安裝 FFMpeg，因為圖書館依賴其二進制文件進行操作。安裝方法因操作系統而異：
- **Ubuntu**：使用命令 `sudo apt-get install ffmpeg` 通過包管理器安裝。
- **macOS**：使用 Homebrew 使用 `brew install ffmpeg` 進行簡單安裝。
- **Windows**：從 [這個網站](https://www.gyan.dev/ffmpeg/builds/) 下載 FFMpeg 二進制文件並按照提供的說明進行操作，確保可執行文件在系統 PATH 中可見，或者手動指定。

安裝 FFMpeg 後，通過 Composer 安裝 php-FFMpeg 圖書館，這是 PHP 包管理器。命令 `composer require php-FFMpeg/php-FFMpeg:~0.5` 確保獲取正確的版本。這個過程在項目中創建一個 `vendor` 目錄，其中包含圖書館及其依賴項，Composer 管理自動加載以實現無縫集成。

#### 設置和初始化
安裝後，在 PHP 腳本中包含自動加載文件以啟用對圖書館類的訪問：
```php
require_once 'vendor/autoload.php';
```

創建 `FFMpeg\FFMpeg` 的實例以開始使用圖書館。創建方法允許配置，特別重要的是如果 FFMpeg 二進制文件不在系統 PATH 中：
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'timeout' => 0,
    'thread_count' => 12,
    'binary' => '/path/to/your/own/FFMpeg',
    'ffprobe' => '/path/to/your/own/FFprobe'
));
```
這個配置支持設置超時、線程計數和顯式二進制路徑，增強了不同系統設置的靈活性。默認設置在 PATH 中查找二進制文件，但手動指定確保兼容性，特別是在自定義環境中。

#### 核心使用和操作
圖書館提供了一個流暢的對象導向界面進行媒體操作。從打開媒體文件開始：
```php
$video = $ff->open('input.mp4');
```
這支持本地文件系統路徑、HTTP 資源和其他 FFMpeg 支持的協議，支持的類型列表可通過 `ffmpeg -protocols` 命令獲取。

##### 轉碼
轉碼涉及將媒體轉換為不同的格式。使用 `save` 方法和格式實例：
```php
$format = new FFMpeg\Format\Video\X264();
$video->save('output.mp4', $format);
```
`X264` 格式是一個例子；圖書館支持各種視頻和音頻格式，可通過 `FFMpeg\Format\FormatInterface` 實現，具體接口如 `VideoInterface` 和 `AudioInterface` 適用於相應的媒體類型。

##### 帧提取
提取帧對於縮略圖或分析非常有用。以下代碼在 5 秒處提取一個帧：
```php
$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5));
$frame->save('frame.jpg');
```
`TimeCode` 類，屬於 `FFMpeg\Coordinate`，確保精確的時間，並且有選項來提取圖像的精確度。

##### 剪輯
要剪輯視頻的一部分，指定開始和結束時間：
```php
$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20));
$clip->save('clip.mp4');
```
這創建了一個新的視頻段，保持原始質量和格式，並且可以應用額外的過濾器（如果需要）。

#### 高級功能和考慮
圖書館支持額外的功能，如文檔中所述：
- **音頻操作**：類似於視頻，音頻可以使用 `FFMpeg\Media\Audio::save` 轉碼，應用過濾器，添加元數據和重新取樣。
- **GIF 創建**：可以使用 `FFMpeg\Media\Gif::save` 保存動畫 GIF，並且有可選的持續時間參數。
- **連接**：使用 `FFMpeg\Media\Concatenate::saveFromSameCodecs` 連接多個媒體文件，適用於相同的編碼器，或者 `saveFromDifferentCodecs` 適用於不同的編碼器，並且有更多資源可供閱讀 [這個鏈接](https://trac.ffmpeg.org/wiki/Concatenate)，[這個鏈接](https://ffmpeg.org/ffmpeg-formats.html#concat-1)，和 [這個鏈接](https://ffmpeg.org/ffmpeg.html#Stream-copy)。
- **高級媒體處理**：支持多個輸入/輸出 `-filter_complex`，適用於複雜的過濾和映射，並且有內置的過濾器支持。
- **元數據提取**：使用 `FFMpeg\FFProbe::create` 提取元數據，並且使用 `FFMpeg\FFProbe::isValid` 驗證文件（自 v0.10.0 可用，注意版本 0.5 可能缺少這一點）。

坐標，如 `FFMpeg\Coordinate\AspectRatio`、`Dimension`、`FrameRate`、`Point`（自 v0.10.0 可動態使用）和 `TimeCode`，提供對媒體屬性的精確控制，但某些功能如動態點可能在版本 0.5 中不可用。

#### 版本特定說明
考慮到 "~0.5" 規範，圖書館可能與 0.x 分支對應，支持較舊的 PHP 版本。GitHub 存儲庫指出主分支需要 PHP 8.0 或更高版本，而 0.x 用於遺留支持。然而，版本 0.5 的具體詳細信息未在發布中明確指出，這表明它可能是提交歷史或分支提交的一部分。用戶應該驗證兼容性，因為某些新功能如某些坐標類型（例如動態點）可能需要 0.5 版本之外的版本。

#### 文檔和進一步閱讀
儘管 Read the Docs 頁面 ([Read the Docs](https://FFMpeg-PHP.readthedocs.io/en/latest/)) 顯示為空，但 GitHub 存儲庫 ([GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)) 包含在 README 中的全面文檔，涵蓋 API 使用、格式和示例。這是版本 0.5 的主要資源，因為缺乏這個遺留版本的具體在線文檔。

#### 表：關鍵操作和方法摘要

| 操作               | 方法示例                                      | 描述                                      |
|-------------------------|----------------------------------------------------|-------------------------------------------------|
| 打開媒體文件         | `$ff->open('input.mp4')`                           | 加載媒體文件進行操作             |
| 轉碼視頻         | `$video->save('output.mp4', new X264())`           | 轉換為指定格式                    |
| 提取帧           | `$video->frame(TimeCode::fromSeconds(5))->save('frame.jpg')` | 提取指定時間的帧，保存為圖像 |
| 剪輯視頻              | `$video->clip(TimeCode::fromSeconds(10), TimeCode::fromSeconds(20))->save('clip.mp4')` | 創建時間段之間的剪輯，保存為新文件   |
| 配置實例      | `FFMpeg::create(array('binary' => '/path/to/FFMpeg'))` | 設置自定義二進制路徑和選項            |

這個表格總結了核心功能，幫助用戶在實現圖書館時進行快速參考。

#### 意外細節：遺留版本的影響
一個意外的方面是版本 0.5 的潛在限制，考慮到它在 0.x 分支中支持較舊的 PHP。這可能會限制對於現代功能（例如在 v0.10.0 中引入的動態坐標點）的訪問，要求用戶檢查分支提交以獲取具體功能，這增加了一層複雜性，並不立即顯示在較新版本中。

#### 結論
使用 "php-FFMpeg/php-FFMpeg" 版本 ~0.5 涉及安裝 FFMpeg、通過 Composer 設置並利用對象導向 API 進行媒體任務。儘管基本操作如轉碼和帧提取非常簡單，但版本特定的差異可能需要參考 0.x 分支文檔 [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)。這種全面的方法確保用戶能夠有效地利用圖書館，並且承認其強大和潛在的遺留約束。

---

### 關鍵引用
- [FFMpeg PHP 對象導向圖書館 Packagist](https://packagist.org/products/php-FFMpeg/php-FFMpeg)
- [PHP-FFMpeg GitHub 存儲庫文檔](https://github.com/PHP-FFMpeg/PHP-FFMpeg)
- [FFMpeg PHP Read the Docs 文檔](https://FFMpeg-PHP.readthedocs.io/en/latest/)
- [FFMpeg 下載和構建網站](https://www.gyan.dev/ffmpeg/builds/)
- [FFMpeg 連接 Wiki 頁面](https://trac.ffmpeg.org/wiki/Concatenate)
- [FFMpeg 格式文檔頁面](https://ffmpeg.org/ffmpeg-formats.html#concat-1)
- [FFMpeg 命令行工具文檔](https://ffmpeg.org/ffmpeg.html#Stream-copy)