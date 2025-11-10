---
audio: false
generated: true
lang: hant
layout: post
title: 在 Ubuntu 中將 WebP 轉換為 JPG
translated: true
type: note
---

在 Ubuntu 系統中，你可以透過多種優秀方式將 WebP 格式轉換為 JPG，無論是使用命令行工具還是圖形界面工具都能輕鬆完成。

## 命令行工具

這類工具特別適合處理單一檔案或批次轉換，具有極佳的靈活性與效率。

### 1. ImageMagick

ImageMagick 是一套功能強大的命令行圖像處理工具集，廣泛應用於各種系統。

* **安裝方法：**
  ```bash
  sudo apt update
  sudo apt install imagemagick
  ```
* **單一檔案轉換：**
  ```bash
  convert input.webp output.jpg
  ```
  若使用 ImageMagick v7+ 版本，請改用 `magick` 指令：
  ```bash
  magick input.webp output.jpg
  ```
* **批次轉換當前目錄內多個檔案：**
  ```bash
  mogrify -format JPEG *.webp
  ```
  此指令會將當前目錄所有 `.webp` 檔案轉換為同檔名的 `.jpeg`（或 `.jpg`）格式。若需要將轉換後的檔案存放至獨立目錄：
  ```bash
  mkdir output_jpgs # 建立輸出專用目錄
  mogrify -format JPEG -path output_jpgs *.webp
  ```

### 2. `dwebp`（來自 `libwebp` 套件）

`dwebp` 是專門用於解碼 WebP 圖像的工具。

* **安裝方法：**
  ```bash
  sudo apt update
  sudo apt install webp
  ```
* **單一檔案轉換：**
  ```bash
  dwebp input.webp -o output.jpg
  ```
  雖然此處指定輸出為 `.jpg` 格式，但 `dwebp` 通常會輸出 PPM 格式，需要配合 ImageMagick 等工具才能轉換為標準 JPEG。若遇到問題，可先轉換為 PNG 再轉為 JPG：
  ```bash
  dwebp input.webp -o output.png
  convert output.png output.jpg
  ```

### 3. `ffmpeg`

`ffmpeg` 雖主要用於影音處理，但同樣能勝任圖像格式轉換。

* **安裝方法：**
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```
* **單一檔案轉換：**
  ```bash
  ffmpeg -i input.webp output.jpg
  ```
* **批次轉換多個檔案：**
  ```bash
  for file in *.webp; do ffmpeg -i "$file" "${file%.*}.jpg"; done
  ```
  此命令會遍歷當前目錄所有 `.webp` 檔案，並將其轉換為同檔名的 `.jpg` 格式（例如 `image.webp` 將轉換為 `image.jpg`）。

## 圖形界面工具

若你偏好使用圖形化操作介面，以下推薦幾款實用工具：

### 1. GIMP（GNU 圖像處理程式）

GIMP 是一款支援 WebP 格式的開源圖像編輯軟體。

* **安裝方法：**
  ```bash
  sudo apt update
  sudo apt install gimp
  ```
* **轉換步驟：**
  1. 使用 GIMP 開啟 WebP 圖像（檔案 > 開啟）
  2. 選擇「檔案 > 匯出為」
  3. 在「匯出圖像」對話框中，從「選擇檔案類型（依副檔名）」下拉選單選擇「JPEG 圖像」
  4. 點擊「匯出」並根據需要調整畫質設定

### 2. XnView MP / XnConvert

這是一套跨平台的圖像檢視器與批次轉換工具，全面支援包括 WebP 在內的多種格式。

* **安裝方法：**
  通常需要從官方網站下載 `.deb` 套件包，並透過 `sudo dpkg -i <套件名稱.deb>` 指令或圖形化套件安裝程式進行安裝
* **轉換步驟（通用流程）：**
  1. 開啟 XnView MP 或 XnConvert
  2. 加入欲轉換的 WebP 圖像
  3. 選擇 JPG 作為輸出格式
  4. 調整相關設定（畫質、尺寸等）
  5. 開始轉換程序

### 3. Converseen

Converseen 是一款免費的批次圖像轉換工具，同樣支援 WebP 格式。

* **安裝方法：** 可透過 Ubuntu 軟體中心搜尋安裝，或透過 apt 指令安裝（若軟體庫提供）
* **轉換步驟：** 提供直觀的圖形介面，可輕鬆添加圖像、選擇輸出格式並執行轉換

## 如何選擇適合的轉換方式？

* **需要快速轉換單一檔案或編寫自動化腳本：** 建議使用命令行工具 `ffmpeg` 或 `ImageMagick`，效率最為出色
* **偶爾需要轉換檔案，且希望透過視覺化介面進行圖像編輯：** GIMP 是最佳選擇
* **需要透過圖形介面批次轉換大量圖像並調整各項參數：** XnView MP/XnConvert 或 Converseen 都是極佳的解決方案

無論選擇何種轉換方式，請務必預先安裝所需的軟體套件。