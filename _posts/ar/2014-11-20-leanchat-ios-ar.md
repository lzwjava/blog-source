---
audio: false
generated: false
image: false
lang: ar
layout: post
title: 'LeanChat iOS


  ياسم لينت شات أي أو إس'
translated: true
type: post
---

هذا هو README.md من مشروع github [https://github.com/lzwjava/leanchat-ios](https://github.com/lzwjava/leancloud-ios).

---

![ترخيص MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat)&nbsp;
[![CocoaPods](http://img.shields.io/cocoapods/v/LeanChatLib.svg?style=flat)](http://cocoapods.org/?q=LeanChatLib)&nbsp;
[![CocoaPods](http://img.shields.io/cocoapods/p/LeanChatLib.svg?style=flat)](http://cocoapods.org/?q=LeanChatLib)&nbsp;
[![دعم](https://img.shields.io/badge/support-iOS%207%2B%20-blue.svg?style=flat)](https://www.apple.com/nl/ios/)

![leanchat](https://cloud.githubusercontent.com/assets/5022872/8431636/4eff0aca-1f6d-11e5-8728-f8f450dac380.gif)

## متجر التطبيقات
LeanChat متاح على متجر التطبيقات. يمكنك زيارة [https://itunes.apple.com/gb/app/leanchat/id943324553](https://itunes.apple.com/gb/app/leanchat/id943324553) أو البحث عن LeanChat على متجر التطبيقات.

## مقدمة
يقدم هذا المثال المشروع كيفية تطبيق ميزة الاتصالات الفورية لـ LeanCloud بشكل شامل. ومع ذلك، يحتوي على الكثير من رموز الواجهة المستخدمية والأدوات الأخرى التي تجعل من الصعب التعلم بسرعة. إذا كنت جديدًا على LeanMessage، ننصحك بالمشروع [LeanMessage-Demo](https://github.com/leancloud/LeanMessage-Demo). بعد أن تصبح على دراية، يمكنك الانتقال إلى [LeanCloud-Demos](https://github.com/leancloud/leancloud-demos) لتحديد جلد IM المفضل لديك للتكامل. أثناء التكامل، إذا واجهت مشكلة صعبة، يمكنك الرجوع إلى مشروع LeanChat.

## هيكل مشروع LeanChat

* [leanchat-android](https://github.com/leancloud/leanchat-android): عميل Android
* [leanchat-ios](https://github.com/lzwjava/leanchat-ios): عميل iOS
* [leanchat-webapp](https://github.com/leancloud/leanchat-webapp): عميل ويب
* [leanchat-cloud-code](https://github.com/leancloud/leanchat-cloudcode): جانب الخادم

## آراء قيمة

إذا كان لديك أي استفسار، فلا تتردد في رفع [مشكلة](https://github.com/leancloud/leanchat-ios/issues) وشرح ما لا تفهمه، وسنقدم المساعدة بسرعة.

## تحميل
يرجى النقر مباشرة على `Download Zip` على Github كما هو موضح في الصورة أدناه لتحميل النسخة الأخيرة فقط. إذا كنت تستخدم `git clone`، قد تكون عملية التحميل بطيئة جدًا لأنها تحتوي على تاريخ التزامن الكبير. في تجربة، كان الفرق 1.5M:40M.

![qq20150618-2 2x](https://cloud.githubusercontent.com/assets/5022872/8223520/4c25415a-15ab-11e5-912d-b5dab916ce86.png)

## تشغيل
```bash
  // LeanChat (مثال معقد)
  cd LeanChat
  pod install --verbose  // إذا كان لديك مكتبة AVOSCloud المستقلة، يمكنك إضافة خيار --no-repo-update لتسريع العملية
  open LeanChat.workspace

  // LeanChatExample (مثال بسيط)
  cd LeanChatExample
  pod install --verbose --no-repo-update
  open LeanChatExample.xcworkspace

  // LeanChatSwift (مثال Swift)
  cd LeanChatSwift
  pod install --verbose --no-repo-update
  open LeanChatSwift.xcworkspace

  // LeanChatLib (مكتبة تحتوي على مكونات LeanCloud ومعالجة رسالة ويب)
  cd LeanChatLib
  pod install --verbose --no-repo-update
  open LeanChatLib.xcworkspace
```

إذا واجهت مشكلات مثل «يجب استيراد تعريف AVUser من Module LeanChatLib.CDChatListVC قبل أن يتطلب»، يمكنك الضغط على Option في قائمة المنتج و النقر على [Clean Build Folder](http://stackoverflow.com/questions/8087065/xcode-4-clean-vs-clean-build-folder) لمحو جميع ملفات البناء، ثم إعادة التجميع. يبدو أن هذه المشكلة هي عيب في عملية Cocoapods التي تقوم بالتجميع المعقد. يمكنك مشاهدتها [هنا](https://cloud.githubusercontent.com/assets/5022872/9230256/cf822fe4-4153-11e5-876d-ed819babad89.gif) للحصول على مزيد من التفاصيل.

يرجى ملاحظة أن نظرًا لأن الإصدارات الافتراضية تستخدم الشهادات الإنتاجية، فإن هناك بريد إلكتروني على الإنترنت محدود لرسائل offline في مرحلة التطوير. ومع ذلك، متاح في النسخة على الإنترنت، والتي يمكن تحميلها من [متجر التطبيقات](https://itunes.apple.com/gb/app/leanchat/id943324553). يمكنك أيضًا مراجعة هذه [المشكلة](https://github.com/leancloud/leanchat-ios/issues/40) للحصول على مزيد من التفاصيل.

 ascribed below.

## مقدمة للمشروع الفرعي
* LeanChatLib: مكتبة منطق وواجهة المستخدم الأساسية لالدردشة. يمكنك من خلالها تكامل وظيفة الدردشة بسرعة، دعم رسائل النص والصوت والصور والإيموجي، بالإضافة إلى إشعارات الرسائل. هناك إصدار [Android](https://github.com/leancloud/leanchat-android) متوافق كذلك.
* LeanChatExample: الأكثر بساطة في استخدام LeanChatLib. يوضح كيفية استخدام أقل كمية من الكود لاستدعاء LeanChatLib للانضمام إلى الدردشة، بغض النظر عن استخدامك لنسخة المستخدم في LeanCloud أو نظام المستخدم الخاص بك.
* LeanChat-ios: تطبيق LeanChat بالكامل. يتضمن محولات الأصدقاء وإدارة المجموعات والدردشة بناءً على الموقع، وأفراد مجاورون، وصفحات شخصية، تسجيل الدخول والتسجيل، كلها تعتمد على إمكانيات LeanCloud للاستخبار والتواصل. إنه تطبيق أكثر تعقيدًا من LeanChatLib.

## مقدمة LeanChatLib

يتضمن صفحة الحوار الأخيرة ومجال الدردشة. يعتمد كل من مشروع LeanChat وLeanChatExample عليه. يمكنك تثبيته كما يلي،
```
    pod 'LeanChatLib'
```

معظم الأوقات، ستكامل LeanChatLib من خلال سحب ملفات المصدر إلى مشروعك. في هذه الحالة، عليك تثبيت `AVOSCloud.framework` و `AVOSCloudIM.framework` أولاً. إذا لم تستخدم `pod install 'AVOSCloud'` و `pod install 'AVOSCloudIM'` لتثبيت، يمكنك تكوين الإطارات المطلوبة وفقًا ل[دليل البدايات السريعة](https://leancloud.cn/docs/start.html) لـ LeanCloud. كما تحتاج إلى تثبيت مكتبة `AVChatLib` و `AVChatLib`. عندما تجري `pod install` لهذا الشريط، ستنشئ مجلد Pods، يمكنك العثور على هذين الشريطين فيه. أو يمكنك البحث عبر الإنترنت. يمكنك أيضًا تكوينه من خلال [.podspec file](https://github.com/leancloud/leanchat-ios/blob/master/LeanChatLib.podspec#L9)، الذي يصف ملفات المصدر التي تحتاج إلى التكامل، وإطارات النظام المطلوبة على سبيل المثال، أو مراجعة هذه [المراجعة](https://ticket.leancloud.cn/tickets/7666).

## كيف تضيف IM في ثلاث خطوات
1. انشئ تطبيق في LeanCloud.
2. أضف التبعية LeanChatLib، أو سحب ملفات LeanChatLib إلى مشروعك للتخصيص السهل لأدوات الواجهة المستخدمية والوظائف.
3. أضف الكود التالي في

المكان المناسب،
عند إطلاق التطبيق، تهيئة وتكوين المستخدم IM،
```objc
    [AVOSCloud setApplicationId:@"YourAppId" clientKey:@"YourAppKey"];
    [CDChatManager manager].userDelegate = [[CDUserFactory alloc] init];
```

تكوين UserFactory، الذي يتوافق مع بروتوكول CDUserDelegate.

```objc
#import "CDUserFactory.h"

#import <LeanChatLib/LeanChatLib.h>

@interface CDUserFactory ()<CDUserDelegate>

@end


@implementation CDUserFactory

#pragma mark - CDUserDelegate
-(void)cacheUserByIds:(NSSet *)userIds block:(AVIMArrayResultBlock)block{
    block(nil,nil); // لا تنساه
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

هنا، CDUser هو موضوع المستخدم في التطبيق، ويمكنك تنفيذ بروتوكول CDUserModel في موضوع المستخدم الخاص بك.

CDUserModel،
```objc
@protocol CDUserModel <NSObject>

@required

-(NSString*)userId;

-(NSString*)avatarUrl;

-(NSString*)username;

@end
```

عند تسجيل الدخول،
```objc
        [[CDChatManager manager] openWithClientId:selfId callback: ^(BOOL succeeded, NSError *error) {
            if (error) {
                DLog(@"%@", error);
            }
            else {
               // انتقل إلى التحكم الرئيسي
            }
        }];
```

الدردشة مع شخص ما،
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

لدردشة المجموعات،
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

عند تسجيل الخروج،
```objc
    [[CDChatManager manager] closeWithCallback: ^(BOOL succeeded, NSError *error) {

    }];
```

ثم يمكنك الدردشة كما هو موضح في الصورة أعلاه. يرجى ملاحظة أننا لا ن recomend استخدام طريقة الشريط لتثبيت LeanChatLib مباشرة لأنه توجد بعض الواجهات والميزات التي تحتاج إلى التكامل بواسطةك. لذلك، نوصي بالنسخ LeanChatLib من المشروع.

## سجل التغييرات LeanChatLib

0.2.6

تحديث SDK إلى 3.1.4 لمواكبة iOS 9

0.2.5

استخدام cachePolicy في AVIMConversationQuery لتوفير النقل وتوفير الدعم في offline
إصلاح عيب في الاتصال fetchConvWithConvid عند عدم وجود الحوار قد يسبب تحطم

0.2.4

إضافة Emoji

0.2.3

إضافة التحقق من التبعيات في واجهة fetchConvWithMembers: وإصلاح عيب محتمل في قائمة الحوار وهي محادثات فردية ولكن لديها عضو واحد فقط

0.2.2

تحديث مكتبة AVOSCloud إلى 3.1.2.8

0.2.1

ChatListDelegate إضافات واجهة configureCell: و prepareConversaion: لتخصيص الحوار المعقد

لرسائل الصور، استخدم AVFile لكتلة الصور، بحيث لا تحتاج إلى تحميل الصور التي أرسلتها من جديد.

0.2.0

إضافة تعليقات، دعم إعادة إرسال الرسائل، عرض الرسائل الفاشلة، إضافة تأثيرات الصوت، والاهتزاز

0.1.3

إصلاح عيب قد يسبب تحطم التطبيق عند تحميل رسائل تاريخية بسرعة من خلال سحب لأسفل

0.1.2

استخدام التخزين المؤقت للمحادثة، إزالة التبعية FMDB. يمكنك رؤية الرسائل التاريخية على الخادم، وسجلات المحادثات التاريخية حتى بعد إعادة التثبيت. إزالة فئة CDNotify.

0.1.1

إعادة تركيب

0.1.0

الإصدار الأول

## ملاحظات توزيع LeanChat

إذا كنت تريد توزيع LeanChat الكامل، نظرًا لأن التطبيق يحتوي على ميزة إضافة أصدقاء، راجع الإعدادات> خيارات التطبيق وتفعيل خيار المتابعة المتبادل حتى يمكن للطرفين الموافقة على إضافتهما على مرأى بالآخر.

![qq20150407-5](https://cloud.githubusercontent.com/assets/5022872/7016645/53f91bb8-dd1b-11e4-8ce0-72312c655094.png)

## دليل التطوير

[دليل تطوير خدمة الرسائل الفورية](https://leancloud.cn/docs/realtime_v2.html)

[مزيد من المعلومات](https://github.com/leancloud/leanchat-android)

## شكر و تقدير

شكرًا لكتب [MessageDisplayKit](https://github.com/xhzengAIB/MessageDisplayKit) المفتوح المصدر من قبل Xian-Hua Han.