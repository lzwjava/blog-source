---
audio: false
generated: true
image: false
lang: hant
layout: post
model: deepseek/deepseek-v3.2-exp
title: iOS 程式碼審查問題與建議
translated: true
type: note
---

從 iOS 工程師的角度，以下是詳細的程式碼審查與技術建議：

## 🚨 **架構與設計問題**

### **1. 龐大視圖控制器違規**
```objc
// 此控制器處理過多職責：
- 網路操作（訊息發送/接收）
- 資料庫操作（快取、失敗訊息）
- 媒體處理（圖片/影片/音訊處理）
- UI 配置與管理
- 通知處理
- 訊息業務邏輯
```

**建議**：拆分為專門類別：
- `MessageService` - 處理網路操作
- `MessageRepository` - 處理資料持久化
- `MediaProcessor` - 處理媒體內容
- `MessageViewModel` - 處理業務邏輯

### **2. 依賴項緊密耦合**
```objc
// 全程直接依賴 LeanCloud 框架
@property (nonatomic, strong, readwrite) AVIMConversation *conv;
// 混用第三方 UI 框架
[self.shareMenuView reloadData];
```

**問題**：難以測試、替換或遷移服務。

### **3. 錯誤處理不當**
```objc
- (BOOL)filterError:(NSError *)error {
    return [self alertError:error] == NO;  // 驗證方法中產生副作用
}

- (void)sendImage:(UIImage *)image {
    // 錯誤處理與業務邏輯混雜
    if (error) {
        [self alert:@"write image to file error"];
    }
}
```

## 🔧 **記憶體管理問題**

### **1. 保留循環與通知問題**
```objc
- (void)dealloc {
    [[NSNotificationCenter defaultCenter] removeObserver:self];
    // 但觀察者是在 viewDidLoad 中添加，而非 viewWillAppear
    // 若通知在 dealloc 後到達可能導致崩潰
}
```

**修正**：
```objc
- (void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
    [self addObservers];
}

- (void)viewDidDisappear:(BOOL)animated {
    [super viewDidDisappear:animated];
    [self removeObservers];
}
```

### **2. 執行緒安全問題**
```objc
@property (atomic, assign) BOOL isLoadingMsg;
// atomic 無法保證複雜操作的執行緒安全

- (void)insertMessage:(AVIMTypedMessage *)message {
    if (self.isLoadingMsg) {
        [self performSelector:@selector(insertMessage:) withObject:message afterDelay:1];
        return;  // 可能出現競爭條件
    }
}
```

## 📱 **UI 與效能問題**

### **1. 主執行緒阻塞**
```objc
- (void)cacheMsgs:(NSArray *)msgs callback:(AVBooleanResultBlock)callback {
    [self runInGlobalQueue:^{
        for (AVIMTypedMessage *msg in msgs) {
            // 在主執行緒進行檔案操作？
            NSData *data = [file getData:&error]; // 阻塞呼叫！
        }
    }];
}
```

### **2. 低效的 TableView 更新**
```objc
- (void)insertMessage:(AVIMTypedMessage *)message {
    [self.messages addObject:xhMessage];
    NSIndexPath *indexPath = [NSIndexPath indexPathForRow:self.msgs.count -1 inSection:0];
    [self.messageTableView insertRowsAtIndexPaths:@[indexPath] withRowAnimation:UITableViewRowAnimationNone];
    // 未進行批次處理，每條訊息單獨插入
}
```

## 🗂 **程式碼組織問題**

### **1. 抽象層級混雜**
```objc
// 低階檔案操作與高階業務邏輯混雜
NSData *imageData = UIImageJPEGRepresentation(image, 0.6);
NSString *path = [[CDChatManager manager] tmpPath];
[imageData writeToFile:path options:NSDataWritingAtomic error:&error];

// 與 UI 程式碼混雜
[self finishSendMessageWithBubbleMessageType:XHBubbleMessageMediaTypeText];
```

### **2. 過長的方法**
```objc
- (XHMessage *)getXHMessageByMsg:(AVIMTypedMessage *)msg {
    // 80+ 行程式碼的方法包含多種職責
    // 訊息轉換、媒體處理、狀態映射
}
```

## 🧪 **測試與維護性**

### **1. 不可測試的設計**
```objc
// 直接使用單例阻止了依賴注入
[[CDChatManager manager] sendMessage:msg...]
[[CDSoundManager manager] playSendSoundIfNeed]

// 硬編碼的依賴使得單元測試無法進行
```

### **2. 違反 SOLID 原則**
- **單一職責**：控制器處理所有事務
- **開閉原則**：難以擴展而不需修改
- **依賴反轉**：隨處可見具體依賴

## 🛠 **建議重構方案**

### **1. 提取服務層**
```objc
@interface MessageDataService : NSObject
- (void)sendMessage:(AVIMTypedMessage *)message 
     conversation:(AVIMConversation *)conversation
        completion:(void(^)(BOOL success, NSError *error))completion;
@end

@interface MediaService : NSObject
- (void)processImage:(UIImage *)image completion:(void(^)(NSString *filePath, NSError *error))completion;
@end
```

### **2. 使用 MVVM 架構**
```objc
@interface ChatRoomViewModel : NSObject
@property (readonly) NSArray<MessageViewModel *> *messages;
@property (readonly) RACSignal *updateSignal;
- (void)sendTextMessage:(NSString *)text;
@end
```

### **3. 實現適當的資料綁定**
```objc
// 取代手動 tableView 更新
self.viewModel.updateSignal = [RACObserve(self.viewModel, messages) 
    deliverOnMainThread];
[self.viewModel.updateSignal subscribeNext:^(id x) {
    [self.tableView reloadData];
}];
```

## 📊 **立即改進措施**

1. **提取所有網路呼叫**至服務層
2. **使用依賴注入**管理管理器
3. **實施適當的錯誤處理**策略
4. **為 tableView 添加效能監控**
5. **建立基礎類別**處理通用聊天功能
6. **添加全面的單元測試**
7. **使用現代並發技術**（async/await 取代 GCD）
8. **使用弱參考實現適當的記憶體管理**

此程式碼展示了 iOS 開發中常見的反模式，採用現代架構模式和更好的關注點分離將能顯著改善程式品質。