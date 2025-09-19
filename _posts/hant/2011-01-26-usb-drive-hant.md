---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 自訂 USB 闪存筆背景及圖標
translated: true
---

這篇文章最初以中文撰寫並在Qzone發布。

---

**I. 定制USB驅動器圖標:**

1. 首先，選擇一個喜歡的圖標。圖標文件擴展名應該是 `.ico`。
2. 將圖標文件複製到USB驅動器並在USB驅動器上創建一個新的文本文件。
3. 在文本文件中寫上以下內容：
   ```
   [autorun]
   ICON=\xxx.ico,0
   ```
   請將 `xxx.ico` 替換為您的圖標文件名稱（包括擴展名）。
4. 將文本文件另存為 `autorun.inf`。**注意：** 確保將擴展名更改為 `.inf`，而不是 `.txt`。如果文件圖標變成一個帶有黃色齒輪的圖標，則表示您已經完成。
   拔下USB驅動器並重新插入。您會看到USB驅動器圖標已經變成您選擇的圖標。
   這種方法也可用於外部硬碟或CD/DVD刻燒。

**II. 定制背景:**

1. 首先，選擇一個喜歡的背景圖片並將其複製到USB驅動器。
2. 創建一個新的文本文件並將以下內容複製進去：
   ```
   [ExtShellFolderViews]
   {BE098140-A513-11D0-A3A4-00C04FD706EC}={BE098140-A513-11D0-A3A4-00C04FD706EC}
   [{BE098140-A513-11D0-A3A4-00C04FD706EC}]
   Attributes=1
   IconArea_Image=aaa.jpg
   IconArea_Text=0x00FFFFFF
   [.ShellClassInfo]
   ConfirmFileOp=0
   ```
   代碼的意義是：

   請將 `aaa.jpg` 替換為您選擇的圖片文件名稱（包括擴展名）。

   `IconArea_Text= 0x00FFFFFF`  這行更改USB驅動器上的文本顏色。

   顏色代碼是：

   *   紅色: `0x000000FF`
   *   黃色: `0x0000FFFF`
   *   蓝色: `0x00FF0000`
   *   灰色: `0x00808080`
   *   橄欖綠: `0x006BDEC7`
   *   黑色: `0x00000000`
   *   Excel背景顏色: `0x00848284`
   *   白色: `0x00FFFFFF`
   *   綠色: `0x00008000`
   *   紫色: `0x00C000C0`

   選擇一個您喜歡且與背景相配的顏色，並替換現有的顏色代碼。

   您可以更改 `IconArea_Text=` 後面的顏色為您喜歡的顏色。

3. 將文本文件另存為 `Desktop.ini`。修改完成。
   刷新USB驅動器，您應該會看到變化。
   上述提到的所有四個文件都可以隱藏以防止意外刪除。
   更改圖標後，您需要拔下並重新插入USB驅動器才能看到效果。
   更改背景後，刷新USB驅動器即可看到變化。