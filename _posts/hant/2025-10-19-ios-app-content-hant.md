---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: iOS 應用程式內容結構與 NSArray
translated: true
type: note
---

### 在 iOS 應用程式中使用 NSArray 和 NSString 組織模擬電子學內容

在一個用於教授模擬電子學和電路分析的 iOS 應用程式（基於您分享的指南）中，`NSArray` 和 `NSString` 是來自 Apple Foundation 框架的基礎類別。它們非常適合處理結構化的文本教學內容：

- **`NSString`**：用於不可變字串，如標題、描述、公式和範例。對於靜態文本非常高效，並支援格式化（例如透過 `NSAttributedString` 在 UI 標籤中實現富文本）。
- **`NSArray`**：用於有序的資料集合，例如定律、步驟或範例的清單。預設情況下是不可變的，非常適合應用程式範圍的常數。如需可變性，可切換使用 `NSMutableArray`。

您通常會在應用程式啟動時載入這些資料（例如在 `AppDelegate` 或資料管理單例中），並在視圖中顯示，如 `UITableView`（用於章節/清單）或 `UILabel`（用於詳細內容）。下面我將展示如何使用這些類別來建模指南內容，並提供 Objective-C 程式碼片段。（Swift 對應使用 `Array` 和 `String`，但由於您提到了 NSArray/NSString，我將堅持使用經典語法。）

#### 1. 基礎範例：將關鍵概念儲存為 NSString 的 NSArray
對於簡單的清單，如電壓、電流或公式，建立一個 `NSString` 物件的 `NSArray`。這可以用來填充表格視圖單元的副標題。

```objective-c
// 在 .h 檔案或資料管理器中
@property (nonatomic, strong) NSArray<NSString *> *keyConcepts;

// 在 .m 檔案中（例如 viewDidLoad）
self.keyConcepts = @[
    @"電壓 (V)：兩點之間的電位差，以伏特 (V) 為單位。它驅動電流通過電路。",
    @"電流 (I)：電荷的流動，以安培 (A) 為單位。方向很重要（傳統電流從正極流向負極）。",
    @"電阻 (R)：對電流的阻力，以歐姆 (Ω) 為單位。電阻器是被動元件，以熱的形式耗散能量。",
    @"功率 (P)：能量消耗率，由 P = VI = I²R = V²/R 給出，以瓦特 (W) 為單位。"
];

// 用法：在 UITableView 中顯示
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"ConceptCell" forIndexPath:indexPath];
    cell.textLabel.text = self.keyConcepts[indexPath.row];
    return cell;
}
```

這會建立一個可滾動的定義清單。對於公式，使用 Unicode/LaTeX 類似的字串（使用 `UILabel` 或數學庫如 iosMath 以獲得更好的顯示效果）。

#### 2. 使用嵌套陣列建模章節（例如定律和範例）
指南中有像「基本電路概念與定律」這樣的章節。使用 `NSDictionary` 物件的 `NSArray`，其中每個字典都有 `NSString` 鍵/值對，用於標題、描述和子項目（另一個 `NSString` 的 `NSArray` 用於步驟/範例）。

```objective-c
// 為整個指南定義一個頂層陣列
@property (nonatomic, strong) NSArray<NSDictionary *> *guideSections;

// 在 .m 中填充
self.guideSections = @[
    @{
        @"title": @"歐姆定律",
        @"description": @"歐姆定律指出，電阻器兩端的電壓與通過它的電流成正比：V = IR。",
        @"examples": @[
            @"在一個具有 12V 電池和 4Ω 電阻器的電路中，電流為 I = 12/4 = 3A。消耗的功率為 P = 12 × 3 = 36W。"
        ]
    },
    @{
        @"title": @"基爾霍夫電流定律 (KCL)",
        @"description": @"進入一個節點的電流總和等於離開該節點的電流總和（電荷守恆）。∑I_進入 = ∑I_離開。",
        @"examples": @[
            @"在一個節點處，如果一個分支有 2A 進入，另一個分支有 3A 進入，則第三個分支必須有 5A 離開。"
        ]
    },
    @{
        @"title": @"基爾霍夫電壓定律 (KVL)",
        @"description": @"任何閉合迴路中的電壓總和為零（能量守恆）。∑V = 0。",
        @"examples": @[
            @"在一個具有 10V 電源、R1 上 2V 壓降和 R2 上 3V 壓降的迴路中，剩餘壓降必須為 5V 以閉合迴路。"
        ]
    }
];

// 用法：為分段的 UITableView 迭代
- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView {
    return self.guideSections.count;
}

- (NSString *)tableView:(UITableView *)tableView titleForHeaderInSection:(NSInteger)section {
    NSDictionary *sectionData = self.guideSections[section];
    return sectionData[@"title"];
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    NSDictionary *sectionData = self.guideSections[section];
    NSArray<NSString *> *examples = sectionData[@"examples"];
    return 1 + examples.count; // 1 用於描述行 + 範例行
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    // ...（出列單元，根據行設置文本為描述或範例）
    NSDictionary *sectionData = self.guideSections[indexPath.section];
    if (indexPath.row == 0) {
        cell.textLabel.text = sectionData[@"description"];
    } else {
        NSArray<NSString *> *examples = sectionData[@"examples"];
        cell.textLabel.text = examples[indexPath.row - 1];
    }
    return cell;
}
```

這自然地嵌套了資料：點擊章節標題以展開範例。對於動態內容（例如用戶筆記），使用 `NSMutableArray` 和 `NSMutableDictionary`。

#### 3. 進階：使用結構化資料進行暫態分析
對於動態章節，如 RC/RL 電路，包括公式和基於時間的資料。使用 `NSString` 用於方程式，內部 `NSArray` 用於步階響應。

```objective-c
self.transientExamples = @[
    @{
        @"circuitType": @"RC 充電",
        @"formula": @"V_C(t) = V_s (1 - e^{-t/RC})",
        @"timeConstant": @"τ = RC",
        @"steps": @[
            @"初始：V_C(0) = 0；最終：V_C(∞) = V_s。",
            @"範例：R=1kΩ, C=1μF (τ=1ms), V_s=5V。在 t=1ms 時，V_C ≈ 3.16V。"
        ]
    },
    @{
        @"circuitType": @"RL 衰減",
        @"formula": @"I_L(t) = I_0 e^{-Rt/L}",
        @"timeConstant": @"τ = L/R",
        @"steps": @[
            @"電流不能瞬時改變。",
            @"穩定時間 ≈ 5τ。"
        ]
    }
];

// 在詳細視圖控制器中，以等寬字體顯示公式
UILabel *formulaLabel = [[UILabel alloc] init];
formulaLabel.font = [UIFont monospacedSystemFontOfSize:14 weight:UIFontWeightMedium];
formulaLabel.text = dict[@"formula"];
```

#### 實作提示
- **資料來源**：將這些資料儲存在 plist 檔案中（使用 `NSDictionary *data = [NSDictionary dictionaryWithContentsOfFile:path];` 載入）或如所示硬編碼以簡化。
- **UI 整合**：綁定到 `UITableView` 或 `UICollectionView` 以實現互動式測驗（例如從陣列中隨機選擇範例）。使用 `NSString` 方法如 `stringByAppendingString:` 用於動態文本（例如插入用戶值進行計算）。
- **效能**：陣列是輕量級的；對於大型指南，如果添加持久化，請考慮使用 Core Data。
- **增強功能**：橋接到 Swift 以用於現代應用程式，或添加 `NSAttributedString` 用於粗體公式。

這種設置使您的應用程式保持模組化——易於更新內容而無需更改 UI。有關完整程式碼，請查閱 Apple 的範例。

[Apple Foundation 框架文檔](https://developer.apple.com/documentation/foundation)  
[UITableView 教程](https://developer.apple.com/tutorials/app-dev-training/creating-a-list-with-a-table-view)