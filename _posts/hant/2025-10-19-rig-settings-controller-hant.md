---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: RIG 設定視窗控制器概覽
translated: true
type: note
---

### 概述

此 Objective-C 程式碼實作了 `RIGSettingWindowController` 類別，負責管理「Reveal-In-GitHub」（RIG）macOS 應用程式（可能是一個 Xcode 外掛，用於快速在 GitHub 儲存庫中顯示選取的程式碼）的設定視窗。該視窗允許使用者為不同的 GitHub 儲存庫設定自訂選單項目、鍵盤快捷鍵和正規表示式模式。它使用表格狀檢視（`RIGConfigCellsView`）來顯示和編輯最多 10 個設定槽位（為保持 UI 一致性而填充空白項目）。

該類別遵循 `NSTableViewDataSource` 和 `NSTableViewDelegate` 協定，表明它處理自訂單元格檢視內表格檢視的資料和事件。它與應用程式全域單例（如用於持久化的 `RIGSetting` 和用於 UI 回饋的 `RIGUtils`）整合。

主要職責：
- 載入並顯示可設定的項目（例如選單標題、快捷鍵、正規表示式模式）。
- 驗證並儲存變更。
- 提供用於儲存、清除預設儲存庫設定和重設為預設值的按鈕。

### 匯入與定義

```objectivec
#import "RIGSettingWindowController.h"
#import "RIGConfigCellsView.h"
#import "RIGConfig.h"
#import "RIGPlugin.h"
#import "RIGUtils.h"
#import "RIGSetting.h"

#define kOutterXMargin 0
#define kOutterYMargin 0
```

- 匯入包含此類別的標頭檔、用於呈現設定行的自訂檢視（`RIGConfigCellsView`）、模型物件（用於個別設定的 `RIGConfig`、用於應用程式全域儲存的 `RIGSetting`）以及實用工具（用於警示的 `RIGUtils`、可能用於外掛生命週期的 `RIGPlugin`）。
- 定義設定配置檢視在視窗內全寬佈局的零邊距。

### 私有介面

```objectivec
@interface RIGSettingWindowController ()<NSTableViewDataSource, NSTableViewDelegate>

@property (nonatomic, strong) NSArray *configs;
@property (nonatomic, strong) RIGConfigCellsView *configCellsView;
@property (weak) IBOutlet NSView *mainView;
@property (weak) IBOutlet NSView *configsView;

@end
```

- 宣告私有擴展以用於內部屬性和協定遵循。
- `configs`：包含使用者設定（例如選單標題、最後按下的按鍵、正規表示式模式）的 `RIGConfig` 物件陣列。
- `configCellsView`：將設定呈現為可編輯行的自訂檢視（可能是可捲動的表格或單元格堆疊）。
- `mainView` 和 `configsView`：指向 Storyboard/NIB 檔案中容器檢視的 IBOutlet；`configsView` 用於承載動態單元格。

### 實作

#### 初始化方法

```objectivec
- (void)awakeFromNib {
    [super awakeFromNib];
}

- (void)windowDidLoad {
    [super windowDidLoad];
    
    self.configs = [self displayConfigs];
    
    self.configCellsView = [[RIGConfigCellsView alloc] initWithFrame:CGRectMake(kOutterXMargin, kOutterYMargin, CGRectGetWidth(self.configsView.frame) - 2 * kOutterXMargin, [RIGConfigCellsView heightForConfigs:self.configs])];
    self.configCellsView.configs = self.configs;
    [self.configsView addSubview:self.configCellsView];
    [self.configCellsView reloadData];
}
```

- `awakeFromNib`：空的重寫方法；在視窗從 NIB（Storyboard）載入時呼叫。僅呼叫父類別。
- `windowDidLoad`：視窗完全載入後的核心設定。
  - 透過 `displayConfigs` 載入 `configs`（詳見下文）。
  - 建立 `configCellsView`，其框架在水平方向上填滿 `configsView`（使用邊距），垂直方向則根據所有設定所需的總高度（由 `RIGConfigCellsView` 類別方法計算）設定。
  - 將設定分配給檢視，將其添加為子檢視，並觸發資料重新載入（可能重新整理表格單元格）。

有一個被註釋掉的 `updateConfigsViewHeight` 呼叫，表明曾考慮動態調整大小但已停用——可能是因為單元格檢視自動調整大小或視窗是固定的。

```objectivec
- (void)updateConfigsViewHeight {
    CGRect frame = self.configsView.frame;
    frame.size.height = CGRectGetHeight(self.configCellsView.frame);
    self.configsView.frame = frame;
}
```

- 用於將 `configsView` 調整為與單元格檢視高度匹配的實用工具。目前未使用，但可用於在添加更多設定時自動增長視窗。

#### 設定管理

```objectivec
- (NSMutableArray *)displayConfigs {
    NSMutableArray *configs = [NSMutableArray arrayWithArray:[RIGSetting setting].configs];
    while (configs.count < 10) {
        RIGConfig *config = [[RIGConfig alloc] init];
        config.menuTitle = @"";
        config.lastKey = @"";
        config.pattern = @"";
        [configs addObject:config];
    }
    return configs;
}
```

- 從應用程式的單例 `RIGSetting` 載入現有設定。
- 用空白的 `RIGConfig` 實例將陣列填充至恰好 10 個項目。這確保了 UI 的一致性（例如 10 個可編輯行），即使用戶儲存的設定較少。空白項目在儲存時會被過濾掉。

```objectivec
- (void)reloadConfigs {
    self.configs = [self displayConfigs];
    self.configCellsView.configs = self.configs;
    [self.configCellsView reloadData];
}
```

- 從儲存重新整理顯示的設定並更新檢視。在重設後使用。

```objectivec
- (BOOL)isValidConfigs:(NSArray *)configs {
    for (RIGConfig *config in configs) {
        if (![config isValid]) {
            return NO;
        }
    }
    return YES;
}
```

- 遍歷設定並對每個設定呼叫 `isValid`（可能檢查非空的 `menuTitle` 和 `pattern`）。僅當所有設定有效或為空時返回 `YES`（但請參見下面的過濾說明）。

```objectivec
- (NSArray *)filteredConfigs {
    NSMutableArray *filtered = [NSMutableArray array];
    NSArray *configs = self.configCellsView.configs;
    for (RIGConfig *config in configs) {
        if (config.menuTitle.length > 0 || config.lastKey.length > 0 || config.pattern.length > 0) {
            [filtered addObject:config];
        }
    }
    return filtered;
}
```

- 將 10 槽位陣列過濾為僅包含非空設定（基於任何欄位有內容）。這在驗證/儲存前去除空白，因此 `isValidConfigs` 僅檢查真實條目。

#### 動作處理器（IBAction）

這些透過 Interface Builder 連接到 UI 中的按鈕。

```objectivec
- (IBAction)saveButtonClcked:(id)sender {
    NSArray *configs = [self filteredConfigs];
    if (![self isValidConfigs:configs]) {
        [RIGUtils showMessage:@"Please complete the config, should at least have menuTitle and pattern."];
        return;
    }
    [RIGSetting setting].configs = self.configCellsView.configs;
    [RIGUtils showMessage:@"Save succeed. Will Take effect when reopen Xcode."];
}
```

- **儲存按鈕**：過濾設定，驗證它們（無效時顯示錯誤警示），然後將完整（填充後）的陣列儲存回 `RIGSetting`。注意：它儲存完整的 10 個槽位，但空白項目在載入/過濾時會被忽略。顯示成功訊息，提示需要重新啟動 Xcode（外掛重新載入）。

方法名稱中的拼寫錯誤："Clcked" 應為 "Clicked"。

```objectivec
- (IBAction)clearButtonClicked:(id)sender {
    RIGSetting *setting = [RIGSetting settingForGitPath:self.gitRepo.localPath];
    NSString *defaultRepo = setting.defaultRepo;
    if (defaultRepo == nil) {
        [RIGUtils showMessage:@"There's no default repo setting."];
    } else {
        setting.defaultRepo = nil;
        [RIGUtils showMessage:[NSString stringWithFormat:@"Succeed to clear current default repo(%@) setting. In the next time to open github, will ask you to select new default repo.", defaultRepo]];
    }
}
```

- **清除按鈕**：透過 `settingForGitPath` 目標為特定專案的設定（假設 `self.gitRepo` 可用，可能在其他地方設定）。清除 `defaultRepo`（例如後備 GitHub URL）。如果未設定則警示，或確認清除並提供詳細資訊。

注意：`self.gitRepo` 未在此處宣告——可能是來自父類別或類別擴展的屬性。

```objectivec
- (IBAction)resetMenusButtonClicked:(id)sender {
    [[RIGSetting setting] setConfigs:[RIGSetting defaultConfigs]];
    [self reloadConfigs];
}
```

- **重設按鈕**：使用應用程式預設值（來自 `RIGSetting`）覆寫設定，然後重新載入 UI。無確認對話框——直接執行操作。

### 潛在改進/注意事項

- **UI 流程**：視窗為非模態（此處無明確顯示呼叫），因此可能透過 `[controller showWindow:sender]` 呈現。由於外掛特性，變更需要 Xcode 重新啟動。
- **驗證**：依賴 `RIGConfig.isValid`，此處未顯示——可能確保必填欄位（如標題和模式）非空。
- **邊界情況**：填充至 10 個項目假設 UI 固定；動態調整大小可使用被註釋的 `updateConfigsViewHeight`。重設/清除無撤銷/確認。
- **依賴關係**：與應用程式模型（`RIGConfig`、`RIGSetting`）緊密耦合——完整理解需要這些標頭檔。

此程式碼來自 2015 年，因此使用較舊的 Cocoa 模式（例如，手動框架設定而非 Auto Layout）。對於現代 SwiftUI，它將是一個帶有 `@State` 設定配置的 `View`。