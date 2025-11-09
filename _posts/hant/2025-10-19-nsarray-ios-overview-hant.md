---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: iOS 開發中的 NSArray 概述
translated: true
type: note
---

### 什麼是 NSArray？

`NSArray` 是 Apple Foundation 框架中的一個類別，屬於 iOS SDK（以及 macOS 等）的一部分。它代表一個不可變的、有序的物件集合，類似於其他語言中的陣列。這意味著一旦你創建了 `NSArray`，就無法新增、移除或替換元素——你只能從中讀取資料。在 Objective-C 的 iOS 應用程式開發中，它通常用於儲存和管理資料列表，例如用戶偏好設定、資料庫查詢結果或 UI 元素。

主要特性：
- **不可變性**：創建後大小和內容固定（可變版本請使用 `NSMutableArray`）。
- **物件類型安全**：儲存指向 Objective-C 物件的指標（例如 `NSString`、`NSNumber`、自定義類別）。不直接支援基本資料類型——需將其包裝在 `NSNumber` 或類似類別中。
- **索引存取**：透過整數索引（從 0 開始）存取元素。
- **執行緒安全**：通常可安全進行並行讀取，但不支援寫入（因為它是不可變的）。
- **整合性**：與其他 Foundation 類別（如 `NSDictionary`、`NSString`）和 Cocoa Touch UI 元件無縫協作。

在 Swift 中，`NSArray` 會橋接到 `Array`，但如果你在 Objective-C 中工作（常見於舊版 iOS 程式碼），則會直接使用 `NSArray`。

### 如何在 iOS 中使用 NSArray

在 iOS 專案中使用 `NSArray`：
1. 匯入 Foundation 框架（通常在 iOS 應用程式中預設包含）。
   ```objc
   #import <Foundation/Foundation.h>
   ```

2. **創建 NSArray**：
   - 字面值語法（iOS 6+）：`@[object1, object2, ...]`
   - 初始化方法：`[[NSArray alloc] initWithObjects:object1, object2, nil]`
   - 從 C 陣列創建：`initWithArray:copyItems:`

   範例：
   ```objc
   NSArray *fruits = @[@"apple", @"banana", @"cherry"];
   // 或：
   NSArray *numbers = [[NSArray alloc] initWithObjects:@1, @2, @3, nil];
   ```

3. **存取元素**：
   - `objectAtIndex:` 用於取得項目。
   - `count` 用於取得長度。
   - `firstObject` / `lastObject` 用於存取首尾元素。
   - `containsObject:` 用於檢查是否存在。

   範例：
   ```objc
   NSString *firstFruit = [fruits objectAtIndex:0]; // "apple"
   NSUInteger count = [fruits count]; // 3
   BOOL hasOrange = [fruits containsObject:@"orange"]; // NO
   ```

4. **迭代**：
   - 快速枚舉：`for (id obj in array) { ... }`
   - `enumerateObjectsUsingBlock:` 用於基於區塊的迭代（iOS 4+）。

   範例：
   ```objc
   for (NSString *fruit in fruits) {
       NSLog(@"Fruit: %@", fruit);
   }
   ```

5. **常見操作**：
   - 排序：`sortedArrayUsingSelector:` 或 `sortedArrayUsingComparator:`。
   - 篩選：`filteredArrayUsingPredicate:`（與 NSPredicate 配合使用）。
   - 連接：`componentsJoinedByString:`（用於字串）。
   - 寫入檔案：`writeToFile:atomically:`。

   範例（篩選）：
   ```objc
   NSPredicate *predicate = [NSPredicate predicateWithFormat:@"length > 5"];
   NSArray *longFruits = [fruits filteredArrayUsingPredicate:predicate];
   // 結果：@[@"banana", @"cherry"]
   ```

6. **在 iOS 情境中的應用**：
   - **表格視圖**：將 `NSArray` 傳遞給 `UITableView` 的資料源方法，如 `tableView:numberOfRowsInSection:`（透過 `count`）和 `tableView:cellForRowAtIndexPath:`（透過 `objectAtIndex:`）。
   - **用戶預設設定**：使用 `NSUserDefaults` 儲存/讀取：`[defaults setObject:array forKey:@"savedItems"];`。
   - **JSON 處理**：使用 `JSONObjectWithData:options:error:` 與 `NSData` 互相轉換。

對於可變需求（例如動態新增項目），請改用 `NSMutableArray`：
```objc
NSMutableArray *mutableFruits = [NSMutableArray arrayWithArray:fruits];
[mutableFruits addObject:@"date"];
```

### 提示
- 始終檢查 `nil` 或邊界以避免崩潰：使用 `objectAtIndex:` 時進行索引驗證。
- 效能：存取為 O(1)，搜尋為 O(n)。
- 現代 iOS 開發：新專案建議考慮使用 Swift 的 `Array`——它更具類型安全性。

[NSArray 文件](https://developer.apple.com/documentation/foundation/nsarray)  
[NSMutableArray 文件](https://developer.apple.com/documentation/foundation/nsmutablearray)