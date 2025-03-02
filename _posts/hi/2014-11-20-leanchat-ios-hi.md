---
audio: false
generated: false
lang: hi
layout: post
title: LeanChat iOS का Hindi अनुवाद नहीं है।
translated: true
---

यह [https://github.com/lzwjava/leanchat-ios](https://github.com/lzwjava/leanchat-ios) से GitHub प्रोजेक्ट का README.md है।---

![License MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat)&nbsp;
[![CocoaPods](http://img.shields.io/cocoapods/v/LeanChatLib.svg?style=flat)](http://cocoapods.org/?q=LeanChatLib)&nbsp;
[![CocoaPods](http://img.shields.io/cocoapods/p/LeanChatLib.svg?style=flat)](http://cocoapods.org/?q=LeanChatLib)&nbsp;
[![Support](https://img.shields.io/badge/support-iOS%207%2B%20-blue.svg?style=flat)](https://www.apple.com/nl/ios/)

![leanchat](https://cloud.githubusercontent.com/assets/5022872/8431636/4eff0aca-1f6d-11e5-8728-f8f450dac380.gif)

## App Store
LeanChat App Store पर उपलब्ध है। आप [https://itunes.apple.com/gb/app/leanchat/id943324553](https://itunes.apple.com/gb/app/leanchat/id943324553) पर जाएं या App Store पर LeanChat खोज सकते हैं।

## परिचय
इस उदाहरण प्रोजेक्ट में LeanCloud के real-time communication feature का व्यापक अनुप्रयोग दिखाया गया है। लेकिन इसमें बहुत सी UI code और अन्य functionalities शामिल हैं, जो इसके लिए जल्दी सीखने के लिए अनुपयुक्त बनाते हैं। अगर आप LeanMessage के नए हैं, तो हम [LeanMessage-Demo](https://github.com/leancloud/LeanMessage-Demo) प्रोजेक्ट को सिफारिश करते हैं। जब आप familiar हो जाएँ, आप [LeanCloud-Demos](https://github.com/leancloud/leancloud-demos) पर जा सकते हैं और अपना पसंदीदा IM skin integration करने के लिए चुन सकते हैं। integration के दौरान, अगर आप किसी मुश्किल समस्या से आमना-सामना करते हैं, आप LeanChat प्रोजेक्ट पर वापस देख सकते हैं।

## LeanChat प्रोजेक्ट संरचना

* [leanchat-android](https://github.com/leancloud/leanchat-android): Android client
* [leanchat-ios](https://github.com/leancloud/leanchat-ios): iOS client
* [leanchat-webapp](https://github.com/leancloud/leanchat-webapp): Web client
* [leanchat-cloud-code](https://github.com/leancloud/leanchat-cloud-code): Server-side

## मूल्यवान फीडबैक

यदि आपके पास कोई सवाल है, तो आप [issue](https://github.com/leancloud/leanchat-ios/issues) उभार सकते हैं, जिसमें आप जो नहीं समझ पा रहे हैं, उसका उल्लेख करें, और हम जल्द से जल्द मदद करेंगे।

## डाउनलोड
कृपया GitHub पर दिए गए नीचे दिए गए छवि में दिखाए गए `Download Zip` पर क्लिक करें ताकि आप केवल आखिरी संस्करण डाउनलोड कर सकें। अगर आप `git clone` का उपयोग करते हैं, तो यह बहुत धीमा हो सकता है क्योंकि इसमें बड़ा commit इतिहास शामिल है। एक परीक्षण में अंतर 1.5M:40M था।

![qq20150618-2 2x](https://cloud.githubusercontent.com/assets/5022872/8223520/4c25415a-15ab-11e5-912d-b5dab916ce86.png)

## चलाने
```bash
  // LeanChat (Complex Example)
  cd LeanChat
  pod install --verbose  // अगर आपके पास AVOSCloud dependency library स्थानीय रूप से है, तो आप --no-repo-update option add कर सकते हैं ताकि प्रक्रिया तेज हो सके
  open LeanChat.workspace

  // LeanChatExample (Simple Example)
  cd LeanChatExample
  pod install --verbose --no-repo-update
  open LeanChatExample.xcworkspace

  // LeanChatSwift (Swift Example)
  cd LeanChatSwift
  pod install --verbose --no-repo-update
  open LeanChatSwift.xcworkspace

  // LeanChatLib (Library encapsulating LeanCloud communication components and UI)
  cd LeanChatLib
  pod install --verbose --no-repo-update
  open LeanChatLib.xcworkspace
```

यदि आप ऐसी समस्याओं को देखते हैं जैसे कि `definition of 'AVUser' must be imported from module 'LeanChatLib.CDChatListVC' before it is required` तो आप Option key को hold कर सकते हैं और Product menu में क्लिक कर सकते हैं [Clean Build Folder](http://stackoverflow.com/questions/8087065/xcode-4-clean-vs-clean-build-folder) सभी Build files को clear करने के लिए, फिर recompile करें। यह seems to be a bug है जब Cocoapods complex compilation कर रही है। आप इसे [Gif](https://cloud.githubusercontent.com/assets/5022872/9230256/cf822fe4-4153-11e5-876d-ed819babad89.gif) के लिए अधिक details के लिए देख सकते हैं।

कृपया ध्यान दें कि क्योंकि default production certificates का उपयोग करता है, development के दौरान offline messages के लिए कोई push notifications नहीं होती हैं। लेकिन, push notifications online version में उपलब्ध हैं, जो आप [App Store](https://itunes.apple.com/gb/app/leanchat/id943324553) से डाउनलोड कर सकते हैं। अधिक details के लिए, आप भी इस [issue](https://github.com/leancloud/leanchat-ios/issues/40) पर संदर्भ ले सकते हैं।

यहाँ तीन प्रोजेक्ट देखे जा सकते हैं, जैसे नीचे वर्णित है।

## Subproject परिचय
* LeanChatLib: Chatting के लिए core logic और UI library है। इसके साथ, आप quickly chat functionality को integrate कर सकते हैं, जो text, audio, image और emoji messages, तथा message notifications का समर्थन करता है। इसके साथ, एक [Android version](https://github.com/leancloud/leanchat-android) भी है।
* LeanChatExample: LeanChatLib का सरलतम उपयोग उदाहरण है। यह दिखाता है कि LeanChatLib को call करने के लिए कितनी कम code का उपयोग किया जा सकता है, चाहे आप LeanCloud के user system या अपना user system का उपयोग करें।
* LeanChat-ios: पूरी LeanChat application है। इसमें friend management, group management, location-based messaging, nearby users, personal pages, login और registration शामिल हैं, सब LeanCloud storage और communication capabilities पर आधारित. यह LeanChatLib का एक अधिक जटिल application है।

## LeanChatLib परिचय

यह recent conversation page और chat page encapsulates. both LeanChat और LeanChatExample projects इस पर निर्भर करता हैं। आप इसे नीचे दिए गए तरीके से install कर सकते हैं,

```
    pod 'LeanChatLib'
```

बहुत समय, आप LeanChatLib को अपने प्रोजेक्ट में source code drag करके integrate करेंगे। इस मामले में, आपको पहले `AVOSCloud.framework` और `AVOSCloudIM.framework` install करना होगा। अगर आप `pod install 'AVOSCloud'` और `pod install 'AVOSCloudIM'` का उपयोग नहीं करते हैं, तो आप LeanCloud [Quick Start Guide](https://leancloud.cn/docs/start.html) के अनुसार required Frameworks को configure कर सकते हैं। भी दो अन्य dependent libraries `JSBadgeView` और `DateTools` install करें। `pod install` इस Demo के लिए run करते समय, एक Pods directory generate होगी, जिसमें आप इन दो Pods को देख सकते हैं। अन्यथा, आप online search कर सकते हैं। आप इसे भी [.podspec file](https://github.com/leancloud/leanchat-ios/blob/master/LeanChatLib.podspec#L9) के माध्यम से configure कर सकते हैं, जो describe करता है कि कौन-से source files integrate करनी हैं और कौन-से system frameworks introduce करनी हैं आदि। या, कृपया इस [ticket](https://ticket.leancloud.cn/tickets/7666) के लिए संदर्भ ले।
## IM को तीन चरणों में जोड़ने का तरीका
1. LeanCloud में एक application create करें।
2. LeanChatLib pod dependency add करें, या LeanChatLib code files को आपके प्रोजेक्ट में drag करें ताकि UI customization और feature adjustment आसान हो सके।
3. नीचे दिए गए code को appropriate places में add करें,

Application launch पर, IM User initialize और configure करें,
```objc
    [AVOSCloud setApplicationId:@"YourAppId" clientKey:@"YourAppKey"];
    [CDChatManager manager].userDelegate = [[CDUserFactory alloc] init];
```

एक UserFactory configure करें, जो CDUserDelegate protocol conform करता है।

```objc
#import "CDUserFactory.h"

#import <LeanChatLib/LeanChatLib.h>

@interface CDUserFactory ()<CDUserDelegate>

@end

@implementation CDUserFactory

#pragma mark - CDUserDelegate
-(void)cacheUserByIds:(NSSet *)userIds block:(AVIMArrayResultBlock)block{
    block(nil,nil); // don't forget it
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

यहाँ, CDUser application के अंदर User object है, और आप CDUserModel protocol implement कर सकते हैं अपने user object में।

CDUserModel,
```objc
@protocol CDUserModel <NSObject>

@required

-(NSString*)userId;

-(NSString*)avatarUrl;

-(NSString*)username;

@end
```

login करते समय call करें,
```objc
        [[CDChatManager manager] openWithClientId:selfId callback: ^(BOOL succeeded, NSError *error) {
            if (error) {
                DLog(@"%@", error);
            }
            else {
               //go Main Controller
            }
        }];
```

किसी के साथ chat करने के लिए,
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

group chat करने के लिए,
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

logout करते समय,
```objc
    [[CDChatManager manager] closeWithCallback: ^(BOOL succeeded, NSError *error) {

    }];
```

तब, आप ऊपर दिए गए screenshot में दिखाए गए तरीके से chat कर सकते हैं। ध्यान दें कि हम अभी LeanChatLib को pod method का उपयोग करके directly import करने के लिए सिफारिश नहीं करते हैं क्योंकि कुछ interfaces और functionalities आपको customize करनी होंगी। इसलिए, हम आपको LeanChatLib code को प्रोजेक्ट में copy करने की सिफारिश करते हैं ताकि customize करना आसान हो सके।

## LeanChatLib ChangeLog

0.2.6

iOS 9 के लिए SDK को 3.1.4 में upgrade किया गया

0.2.5

AVIMConversationQuery में cachePolicy का उपयोग कर traffic save करना और offline support improve करना
fetchConvWithConvid call करते समय, conversation नहीं हुआ तो crash हो सकता है bug fixed

0.2.4

Tuzki emoji add किया गया

0.2.3

fetchConvWithMembers: interface में parameter check add किया गया, conversation list में crash की potentially crash fixed की संभावना

0.2.2

AVOSCloud library को 3.1.2.8 में upgrade किया गया

0.2.1

ChatListDelegate में configureCell: और prepareConversaion: interfaces add किया गया, अधिक complex conversation customization ke लिए

Image messages के लिए, AVFile images के लिए caching ke लिए use किया गया, so कि आपका sent photos re-download नहीं करना पड़े.

0.2.0

Comments add, message resend support, failed messages display, sound effects, और vibration add

0.1.3

Quickly historical messages को loading करते समय app crash हो सकता है bug fixed

0.1.2

SDK's chat cache का उपयोग, FMDB dependency remove. historical messages server पर देख सकते हैं और historical chat records even reinstallation के बाद. CDNotify class remove

0.1.1

Refactoring

0.1.0

Initial release

## LeanChat Deployment Notes

अगर आप पूरा LeanChat deploy करना चाहते हैं, क्योंकि application में friend adding feature है, तो Settings->Application Options पर जाएं और Mutual Follow option check करें ताकि जब एक पार्टी agree कर ले, तो वे एक-दूसरे को friends के रूप में add कर सकें।

![qq20150407-5](https://cloud.githubusercontent.com/assets/5022872/7016645/53f91bb8-dd1b-11e4-8ce0-72312c655094.png)

## Development Guide

[Realtime Messaging Service Development Guide](https://leancloud.cn/docs/realtime_v2.html)

[More Information](https://github.com/leancloud/leanchat-android)

## Acknowledgments

MessageDisplayKit open-source library का धन्यवाद [Xian-Hua Han](https://github.com/xhzengAIB/MessageDisplayKit) द्वारा