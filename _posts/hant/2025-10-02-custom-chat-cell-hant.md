---
audio: false
generated: true
image: false
lang: hant
layout: post
model: deepseek/deepseek-v3.2-exp
title: 自訂聊天對話表格儲存格
translated: true
type: note
---

這是一個 Objective-C 實現的自定義表格視圖單元格，用於在聊天應用程式（如 iMessage 或 WhatsApp）中顯示對話項目。讓我解析關鍵組件：

## 概覽
`LZConversationCell` 類別創建了一個自定義單元格，用於顯示：
- 用戶頭像/圖片
- 聯絡人名稱
- 最後訊息預覽
- 時間戳記
- 未讀訊息的徽章指示器

## 關鍵組件

### 1. 佈局常數
```objc
static CGFloat kLZImageSize = 45;           // 頭像尺寸
static CGFloat kLZVerticalSpacing = 8;      // 垂直間距
static CGFloat kLZHorizontalSpacing = 10;   // 水平間距
static CGFloat kLZTimestampeLabelWidth = 100; // 時間戳記標籤寬度
```

### 2. UI 元素
- **`avatarImageView`**：用戶個人資料圖片（45x45 點）
- **`nameLabel`**：聯絡人名稱顯示
- **`messageTextLabel`**：最後訊息預覽
- **`timestampLabel`**：訊息時間/日期
- **`litteBadgeView`**：新訊息的小紅點指示器
- **`badgeView`**：未讀計數的數字徽章

### 3. 單元格管理方法
- **`+dequeueOrCreateCellByTableView:`**：標準表格視圖單元格重用模式
- **`+registerCellToTableView:`**：向表格視圖註冊單元格類別
- **`+heightOfCell`**：固定高度計算（61 點）

### 4. 佈局設置
`setup` 方法：
- 根據比例計算標籤高度
- 創建並定位所有子視圖
- 使用基於框架的佈局（非 Auto Layout）

### 5. 框架計算
每個子視圖都相對於其他組件進行定位：
- 頭像位於左側，具有固定間距
- 名稱和訊息標籤位於頭像右側
- 時間戳記對齊右邊緣
- 徽章視圖定位在頭像上方

### 6. 記憶體管理
- **`prepareForReuse`**：在單元格被回收時清除所有內容
- 所有子視圖的懶初始化（僅在需要時創建）

## 使用模式
此單元格將用於對話列表表格視圖中，顯示每個聊天對話的：
- 聯絡人資訊
- 訊息預覽
- 已讀/未讀狀態指示器
- 最後訊息的時間戳記

該單元格遵循 iOS 設計模式，並提供訊息應用程式中常見的視覺指示器。