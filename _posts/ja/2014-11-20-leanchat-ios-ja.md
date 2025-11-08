---
audio: false
generated: false
image: false
lang: ja
layout: post
title: LeanChat iOSは
translated: true
type: post
---

このREADME.mdは、GitHubプロジェクト[https://github.com/lzwjava/leanchat-ios](https://github.com/lzwjava/leanchat-ios)からのものです。

---

![ライセンスMIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat)&nbsp;
[![CocoaPods](http://img.shields.io/cocoapods/v/LeanChatLib.svg?style=flat)](http://cocoapods.org/?q=LeanChatLib)&nbsp;
[![CocoaPods](http://img.shields.io/cocoapods/p/LeanChatLib.svg?style=flat)](http://cocoapods.org/?q=LeanChatLib)&nbsp;
[![サポート](https://img.shields.io/badge/support-iOS%207%2B%20-blue.svg?style=flat)](https://www.apple.com/nl/ios/)

![leanchat](https://cloud.githubusercontent.com/assets/5022872/8431636/4eff0aca-1f6d-11e5-8728-f8f450dac380.gif)

## App Store
LeanChatはApp Storeで利用できます。以下のURLを訪れてください。https://itunes.apple.com/gb/app/leanchat/id943324553 または、App StoreでLeanChatを検索してください。

## はじめに
この例プロジェクトは、LeanCloudのリアルタイム通信機能の応用を包括的に示しています。ただし、UIコードや他の機能が多く含まれており、迅速な学習には向いていません。LeanMessageに新しい方は、[LeanMessage-Demo](https://github.com/leancloud/LeanMessage-Demo)プロジェクトをお勧めします。理解が深まったら、[LeanCloud-Demos](https://github.com/leancloud/leancloud-demos)に進み、好きなIMスキンを選んで統合してください。統合中に難しい問題に直面したら、LeanChatプロジェクトを参考にしてください。

## LeanChatプロジェクトの構造

* [leanchat-android](https://github.com/leancloud/leanchat-android): Androidクライアント
* [leanchat-ios](https://github.com/leancloud/leanchat-ios): iOSクライアント
* [leanchat-webapp](https://github.com/leancloud/leanchat-webapp): Webクライアント
* [leanchat-cloud-code](https://github.com/leancloud/leanchat-cloudcode): サーバーサイド

## 有益なフィードバック

質問があれば、[issue](https://github.com/leancloud/leanchat-ios/issues)を立てて、わからない点を記載してください。できるだけ早くサポートいたします。

## ダウンロード
以下の画像に示すように、Githubの「Download Zip」を直接クリックして最新バージョンをダウンロードしてください。`git clone`を使用すると、大量のコミット履歴を含むため非常に遅くなることがあります。試験では1.5M:40Mの違いがあります。

![qq20150618-2 2x](https://cloud.githubusercontent.com/assets/5022872/8223520/4c25415a-15ab-11e5-912d-b5dab916ce86.png)

## 実行
```bash
  // LeanChat (複雑な例)
  cd LeanChat
  pod install --verbose  // AVOSCloud依存ライブラリがローカルにある場合、--no-repo-updateオプションを追加してプロセスを加速できます
  open LeanChat.workspace

  // LeanChatExample (簡単な例)
  cd LeanChatExample
  pod install --verbose --no-repo-update
  open LeanChatExample.xcworkspace

  // LeanChatSwift (Swift例)
  cd LeanChatSwift
  pod install --verbose --no-repo-update
  open LeanChatSwift.xcworkspace

  // LeanChatLib (LeanCloud通信コンポーネントとUIをカプセル化するライブラリ)
  cd LeanChatLib
  pod install --verbose --no-repo-update
  open LeanChatLib.xcworkspace
```

`definition of 'AVUser' must be imported from module 'LeanChatLib.CDChatListVC' before it is required`のような問題が発生した場合、ProductメニューでOptionキーを押しながら[Clean Build Folder](http://stackoverflow.com/questions/8087065/xcode-4-clean-vs-clean-build-folder)をクリックしてすべてのビルドファイルをクリアし、再コンパイルしてください。この問題は、Cocoapodsが複雑なコンパイルを実行している際のバグのようです。この[Gif](https://cloud.githubusercontent.com/assets/5022872/9230256/cf822fe4-4153-11e5-876d-ed819babad89.gif)を参照してください。

デフォルトでは生産用証明書を使用しているため、開発中にオフラインメッセージのプッシュ通知はありません。ただし、オンラインエディションは[App Store](https://itunes.apple.com/gb/app/leanchat/id943324553)からダウンロードでき、プッシュ通知が利用できます。詳細については、この[issue](https://github.com/leancloud/leanchat-ios/issues/40)をご参照ください。

以下に、3つのプロジェクトの説明があります。

## サブプロジェクトの紹介

* LeanChatLib: チャットのコアロジックとUIライブラリ。これを使用すると、迅速にチャット機能を統合でき、テキスト、音声、画像、絵文字メッセージ、メッセージ通知がサポートされます。また、[Android版](https://github.com/leancloud/leanchat-android)もあります。
* LeanChatExample: LeanChatLibの最も簡単な使用例。少量のコードを使用してLeanChatLibを呼び出してチャットに参加する方法を示します。LeanCloudのユーザーシステムを使用するか、独自のユーザーシステムを使用するかを問わずです。
* LeanChat-ios: 完全なLeanChatアプリケーション。友人管理、グループ管理、位置情報メッセージ、近隣のユーザー、個人ページ、ログイン、登録など、すべてがLeanCloudのストレージと通信機能に基づいています。これは、LeanChatLibのより複雑なアプリケーションです。

## LeanChatLibの紹介

最新の会話ページとチャットページをカプセル化しています。LeanChatとLeanChatExampleプロジェクトの両方が依存しています。以下のようにインストールできます。
```bash
    pod 'LeanChatLib'
```

ほとんどの場合、LeanChatLibをプロジェクトにドラッグしてソースコードを統合することで、LeanChatLibが統合されます。この場合、`AVOSCloud.framework`と`AVOSCloudIM.framework`をインストールする必要があります。`pod install 'AVOSCloud'`、`pod install 'AVOSCloudIM'`を使用してインストールしていない場合、`pod install`を実行する前に必要なフレームワークをLeanCloudの[クイックスタートガイド](https://leancloud.cn/docs/start.html)に従って設定してください。また、他の2つの依存ライブラリ`JSBadgeView`と`DateTools`をインストールしてください。`pod install`を実行すると、このDemo用にPodsディレクトリが生成され、このディレクトリから2つのPodを検索できます。オンラインで検索することもできます。また、[.podspecファイル](https://github.com/leancloud/leanchat-ios/blob/master/LeanChatLib.podspec#L9)を通じて設定することもできます。このファイルでは、統合する必要があるソースファイルと導入する必要があるシステムフレームワークについて説明しています。または、この[チケット](https://ticket.leancloud.cn/tickets/7666)を参照してください。

## 3ステップでIMを追加する方法

1. LeanCloudでアプリケーションを作成します。
2. LeanChatLibのpod依存関係を追加するか、UIのカスタマイズや機能の調整がしやすいようにLeanChatLibのコードファイルをプロジェクトにドラッグして追加します。
3. 適切な場所に以下のコードを追加します。

アプリケーションの起動時に、IMユーザーを初期化および設定します。
```objc
    [AVOSCloud setApplicationId:@"YourAppId" clientKey:@"YourAppKey"];
    [CDChatManager manager].userDelegate = [[CDUserFactory alloc] init];
```
CDUserDelegateプロトコルを実装するUserFactoryを設定します。
```objc
#import "CDUserFactory.h"

#import <LeanChatLib/LeanChatLib.h>

@interface CDUserFactory ()<CDUserDelegate>

@end

@implementation CDUserFactory

#pragma mark - CDUserDelegate
-(void)cacheUserByIds:(NSSet *)userIds block:(AVIMArrayResultBlock)block{
    block(nil,nil); // 忘れないでください
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
ここでCDUserはアプリケーション内のUserオブジェクトであり、UserオブジェクトにCDUserModelプロトコルを実装できます。

CDUserModel、
```objc
@protocol CDUserModel <NSObject>

@required

-(NSString*)userId;

-(NSString*)avatarUrl;

-(NSString*)username;

@end
```
ログイン時に呼び出します。
```objc
        [[CDChatManager manager] openWithClientId:selfId callback: ^(BOOL succeeded, NSError *error) {
            if (error) {
                DLog(@"%@", error);
            }
            else {
               //メインコントローラーへ進む
            }
        }];
```
誰かとチャットするには、
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
グループチャットするには、
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
ログアウトするには、
```objc
    [[CDChatManager manager] closeWithCallback: ^(BOOL succeeded, NSError *error) {
    }];
```
これで、上のスクリーンショットに示すようにチャットすることができます。現在、Podメソッドを使用してLeanChatLibを直接インポートすることはお勧めしません。いくつかのインターフェースと機能は、あなたがカスタマイズする必要があるためです。したがって、プロジェクトにLeanChatLibのコードをコピーしてカスタマイズを簡略化することをお勧めします。

## LeanChatLibの変更履歴

0.2.6

SDKを3.1.4にアップグレードしてiOS 9に適合

0.2.5

AVIMConversationQueryでcachePolicyを使用してトラフィックを節約し、オフラインサポートを向上

fetchConvWithConvidを呼び出す際に会話が存在しない場合にクラッシュが発生する問題を修正

0.2.4

Tuzki絵文字を追加

0.2.3

fetchConvWithMembers:インターフェースにパラメータの検証を追加し、会話リスト内でのクラッシュの可能性を修正

0.2.2

AVOSCloudライブラリを3.1.2.8にアップグレード

0.2.1

ChatListDelegateにconfigureCell:とprepareConversaion:インターフェースを追加して、より複雑な会話のカスタマイズが可能

画像メッセージの場合、AVFileを使用して画像をキャッシュするため、自分の送った写真を再度ダウンロードする必要がなくなります。

0.2.0

コメントを追加し、メッセージの再送、失敗したメッセージの表示、サウンドエフェクトと振動をサポート

0.1.3

 swiftly pull-downで履歴メッセージを読み込む際にアプリがクラッシュする問題を修正

0.1.2

SDKのチャットキャッシュを使用し、FMDB依存を削除。サーバー上の履歴メッセージを表示でき、再インストール後の履歴チャットレコードを保持できるようになります。CDNotifyクラスを削除

0.1.1

リファクタリング

0.1.0

初期リリース

## LeanChatのデプロイメントノート

完全なLeanChatをデプロイしたい場合、アプリケーションには友人追加機能がありますので、設定→アプリケーションオプションに進み、相互フォローオプションをオンにしてください。一方が同意すると、お互いに友達として追加できます。

![qq20150407-5](https://cloud.githubusercontent.com/assets/5022872/7016645/53f91bb8-dd1b-11e4-8ce0-72312c655094.png)

## 開発ガイド

[リアルタイムメッセージングサービスの開発ガイド](https://leancloud.cn/docs/realtime_v2.html)

[さらに詳細](https://github.com/leancloud/leanchat-android)

## 謝辞

素晴らしいオープンソースライブラリ[MessageDisplayKit](https://github.com/xhzengAIB/MessageDisplayKit)を提供してくれた宋欣華さんに感謝します。