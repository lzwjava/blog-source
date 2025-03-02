---
audio: false
generated: false
lang: hant
layout: post
title: 聊天iOS
translated: true
---

---

![許可證 MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat)&nbsp;
[![CocoaPods](http://img.shields.io/cocoapods/v/LeanChatLib.svg?style=flat)](http://cocoapods.org/?q=LeanChatLib)&nbsp;
[![CocoaPods](http://img.shields.io/cocoapods/p/LeanChatLib.svg?style=flat)](http://cocoapods.org/?q=LeanChatLib)&nbsp;
[![支持](https://img.shields.io/badge/support-iOS%207%2B%20-blue.svg?style=flat)](https://www.apple.com/nl/ios/)

![leanchat](https://cloud.githubusercontent.com/assets/5022872/8431636/4eff0aca-1f6d-11e5-8728-f8f450dac380.gif)

## App Store

LeanChat 可在 App Store 上找到。您可以訪問 [https://itunes.apple.com/gb/app/leanchat/id943324553](https://itunes.apple.com/gb/app/leanchat/id943324553) 或在 App Store 搜索 LeanChat。

## 介紹

此範例項目全面展示了 LeanCloud 的即時通訊功能的應用。但它包含大量的 UI 代碼和其他功能，使其不適合快速學習。如果您是 LeanMessage 的新手，我們建議您使用 [LeanMessage-Demo](https://github.com/leancloud/LeanMessage-Demo) 專案。熟悉後，您可以前往 [LeanCloud-Demos](https://github.com/leancloud/leancloud-demos) 選擇您喜歡的 IM 外觀進行整合。在整合過程中，如果遇到困難，您可以參考 LeanChat 專案。

## LeanChat 專案結構

* [leanchat-android](https://github.com/leancloud/leanchat-android)：Android 客戶端
* [leanchat-ios](https://github.com/leancloud/leanchat-ios)：iOS 客戶端
* [leanchat-webapp](https://github.com/leancloud/leanchat-webapp)：Web 客戶端
* [leanchat-cloud-code](https://github.com/leancloud/leanchat-cloudcode)：伺服器端

## 有價值的反饋

如果您有任何問題，請隨時提出 [issue](https://github.com/leancloud/leanchat-ios/issues)，說明您不理解的部分，我們會盡快提供幫助。

## 下載

請直接在 GitHub 上點擊 `Download Zip` 如下圖所示，下載最新版本。如果使用 `git clone`，可能會非常慢，因為它包含大量的提交歷史。根據測試，差異為 1.5M:40M。

![qq20150618-2 2x](https://cloud.githubusercontent.com/assets/5022872/8223520/4c25415a-15ab-11e5-912d-b5dab916ce86.png)

## 運行

```bash
  // LeanChat (複雜範例)
  cd LeanChat
  pod install --verbose  // 如果本地有 AVOSCloud 依賴庫，您可以添加 --no-repo-update 選項以加快過程
  open LeanChat.workspace

  // LeanChatExample (簡單範例)
  cd LeanChatExample
  pod install --verbose --no-repo-update
  open LeanChatExample.xcworkspace

  // LeanChatSwift (Swift 範例)
  cd LeanChatSwift
  pod install --verbose --no-repo-update
  open LeanChatSwift.xcworkspace

  // LeanChatLib (封裝 LeanCloud 通訊組件和 UI 的庫)
  cd LeanChatLib
  pod install --verbose --no-repo-update
  open LeanChatLib.xcworkspace
```

如果遇到類似 `definition of 'AVUser' must be imported from module 'LeanChatLib.CDChatListVC' before it is required` 的問題，您可以在產品菜單中按住 Option 鍵並點擊 [Clean Build Folder](http://stackoverflow.com/questions/8087065/xcode-4-clean-vs-clean-build-folder) 清除所有 Build 文件，然後重新編譯。這個問題似乎是 Cocoapods 在執行複雜編譯時出現的錯誤。您可以查看這個 [Gif](https://cloud.githubusercontent.com/assets/5022872/9230256/cf822fe4-4153-11e5-876d-ed819babad89.gif) 以獲取更多詳細信息。

請注意，因為默認使用生產證書，因此在開發過程中，離線消息沒有推送通知。然而，線上版本有推送通知，您可以從 [App Store](https://itunes.apple.com/gb/app/leanchat/id943324553) 下載。有關更多詳細信息，您也可以參考這個 [issue](https://github.com/leancloud/leanchat-ios/issues/40)。

您可以看到以下三個專案，如下所述。

## 子專案介紹

* LeanChatLib：聊天的核心邏輯和 UI 庫。使用它，您可以迅速整合聊天功能，支持文本、音頻、圖像和表情符號消息以及消息通知。也有一個相應的 [Android 版本](https://github.com/leancloud/leanchat-android)。
* LeanChatExample：LeanChatLib 的最簡單用法範例。它展示了如何使用最少的代碼調用 LeanChatLib 加入聊天，無論您是使用 LeanCloud 的用戶系統還是您自己的用戶系統。
* LeanChat-ios：完整的 LeanChat 應用程序。它包括好友管理、群組管理、基於位置的消息、附近的用戶、個人頁面、登錄和註冊等功能，均基於 LeanCloud 的存儲和通訊能力。它是 LeanChatLib 的更複雜應用。

## LeanChatLib 介紹

它封裝了最近對話頁和聊天頁。LeanChat 和 LeanChatExample 專案都依賴它。您可以按照以下方式安裝它，

```
    pod 'LeanChatLib'
```

大多數時間，您會通過將源代碼拖放到項目中來整合 LeanChatLib。在這種情況下，您需要先安裝 `AVOSCloud.framework` 和 `AVOSCloudIM.framework`。如果您沒有使用 `pod install 'AVOSCloud'`, `pod install 'AVOSCloudIM'` 安裝，您可以根據 LeanCloud [快速開始指南](https://leancloud.cn/docs/start.html) 配置所需的框架。還有兩個其他依賴庫 `JSBadgeView` 和 `DateTools`。當運行此演示的 `pod install` 時，會生成一個 Pods 目錄，您可以從中找到這兩個 Pods。或者，您可以在線搜索。您也可以通過 [.podspec 文件](https://github.com/leancloud/leanchat-ios/blob/master/LeanChatLib.podspec#L9) 配置它，該文件描述了需要整合哪些源文件以及需要介紹哪些系統框架等。或者，請參考這個 [票](https://ticket.leancloud.cn/tickets/7666)。

## 如何在三個步驟中添加 IM

1. 在 LeanCloud 中創建一個應用程序。
2. 添加 LeanChatLib pod 依賴，或者將 LeanChatLib 代碼文件拖放到您的項目中，以便更容易自定義 UI 和功能調整。
3. 在適當的地方添加以下代碼，

在應用程序啟動時初始化和配置 IM 用戶，

```objc
    [AVOSCloud setApplicationId:@"您的應用ID" clientKey:@"您的應用密鑰"];
    [CDChatManager manager].userDelegate = [[CDUserFactory alloc] init];
```

配置一個 UserFactory，該 UserFactory 遵循 CDUserDelegate 協議。

```objc
#import "CDUserFactory.h"

#import <LeanChatLib/LeanChatLib.h>

@interface CDUserFactory ()<CDUserDelegate>

@end

@implementation CDUserFactory

#pragma mark - CDUserDelegate
-(void)cacheUserByIds:(NSSet *)userIds block:(AVIMArrayResultBlock)block{
    block(nil,nil); // 不要忘記它
}

-(id<CDUserModel>)getUserById:(NSString *)userId{
    CDUser* user=[[CDUser alloc] init];
    user.userId=userId;
    user.username=userId;
    user.avatarUrl=@"http://ac-x3o016bx.clouddn.com/86O7RAPx2BtTW5zgZTPGNwH9RZD5vNDtPm1YbIcu";
    return user;
}

@end
```

這裡，CDUser 是應用程序中的用戶對象，您可以在用戶對象中實現 CDUserModel 協議。

CDUserModel，
```objc
@protocol CDUserModel <NSObject>

@required

-(NSString*)userId;

-(NSString*)avatarUrl;

-(NSString*)username;

@end
```

在登錄時調用，

```objc
        [[CDChatManager manager] openWithClientId:selfId callback: ^(BOOL succeeded, NSError *error) {
            if (error) {
                DLog(@"%@", error);
            }
            else {
               // 轉到主控制器
            }
        }];
```

與某人聊天，

```objc
        [[CDChatManager manager] fetchConvWithOtherId : otherId callback : ^(AVIMConversation *conversation, NSError *error) {
            if (error) {
                DLog(@"%@", error);
            }
            else {
                LCEChatRoomVC *chatRoomVC = [[LCEChatRoomVC alloc] initWithConv:conversation];
                [weakSelf.navigationController pushViewController:chatRoomVC animated:YES];
            }
        }];
```

群聊，

```objc
        NSMutableArray *memberIds = [NSMutableArray array];
        [memberIds addObject:groupId1];
        [memberIds addObject:groupId2];
        [memberIds addObject:[CDChatManager manager].selfId];
        [[CDChatManager manager] fetchConvWithMembers:memberIds callback: ^(AVIMConversation *conversation, NSError *error) {
            if (error) {
                DLog(@"%@", error);
            }
            else {
                LCEChatRoomVC *chatRoomVC = [[LCEChatRoomVC alloc] initWithConv:conversation];
                [weakSelf.navigationController pushViewController:chatRoomVC animated:YES];
            }
        }];
```

在登出時，

```objc
    [[CDChatManager manager] closeWithCallback: ^(BOOL succeeded, NSError *error) {

    }];
```

然後，您可以像上圖所示的那樣聊天。請注意，目前我們不建議使用 pod 方法直接導入 LeanChatLib，因為某些接口和功能需要由您自定義。因此，我們建議將 LeanChatLib 代碼複製到項目中，以便更容易自定義。

## LeanChatLib 變更日誌

0.2.6

將 SDK 升級到 3.1.4 以適應 iOS 9

0.2.5

在 AVIMConversationQuery 中使用 cachePolicy 以節省流量並更好地支持離線
修復了調用 fetchConvWithConvid 時對話不存在可能導致崩潰的錯誤

0.2.4

添加了 Tuzki 表情符號

0.2.3

為 fetchConvWithMembers: 接口添加了參數檢查，修復了對話列表中的潛在崩潰問題，當它是單聊但只有一個成員時

0.2.2

將 AVOSCloud 庫升級到 3.1.2.8

0.2.1

ChatListDelegate 添加了 configureCell: 和 prepareConversaion: 接口以進行更複雜的對話自定義。

對於圖像消息，使用 AVFile 進行圖像緩存，因此您不需要重新下載自己發送的照片。

0.2.0

添加註釋，支持消息重發，顯示失敗的消息，添加聲音效果和振動

0.1.3

修復了快速下拉加載歷史消息時應用程序可能崩潰的錯誤

0.1.2

使用 SDK 的聊天緩存，移除了 FMDB 依賴。您可以在伺服器上查看歷史消息，即使重新安裝後，歷史聊天記錄也仍然存在。移除了 CDNotify 類。

0.1.1

重構

0.1.0

初始版本

## LeanChat 部署注意事項

如果您要部署完整的 LeanChat，因為應用程序具有添加好友功能，請前往設置 -> 應用程序選項並勾選相互關注選項，以便雙方同意後可以互相添加為好友。

![qq20150407-5](https://cloud.githubusercontent.com/assets/5022872/7016645/53f91bb8-dd1b-11e4-8ce0-72312c655094.png)

## 开發指南

[即時消息服務開發指南](https://leancloud.cn/docs/realtime_v2.html)

[更多信息](https://github.com/leancloud/leanchat-android)

## 鳴謝

感謝由 Xian-Hua Han 開發的優秀的 [MessageDisplayKit](https://github.com/xhzengAIB/MessageDisplayKit) 开放源代码庫。