---
audio: false
generated: true
lang: ja
layout: post
title: リーンクラウド iOS SDK
translated: true
type: note
---

iOSプロジェクトで`pod 'AVOSCloud', '3.1.6.2'`を使用するには、CocoaPods（iOSプロジェクトの依存関係マネージャー）を介してAVOSCloud SDK（おそらくLeanCloudのクラウドサービス向けSDK）を統合することを指します。以下は設定のステップバイステップガイドです：

---

### 前提条件
1. **CocoaPodsのインストール**: CocoaPodsがインストールされていない場合は、まずターミナルで以下を実行してインストールしてください：
   ```bash
   sudo gem install cocoapods
   ```
2. **Xcodeプロジェクト**: Xcodeで既存のiOSプロジェクトがあることを確認してください。

---

### `pod 'AVOSCloud', '3.1.6.2'`を使用する手順

1. **プロジェクトディレクトリに移動**:
   ターミナルを開き、`.xcodeproj`ファイルを含むディレクトリに移動します：
   ```bash
   cd /path/to/your/project
   ```

2. **Podfileの初期化**（まだない場合）:
   以下のコマンドを実行して`Podfile`を作成します：
   ```bash
   pod init
   ```

3. **Podfileの編集**:
   テキストエディタで`Podfile`を開き（例：`nano Podfile`または`open Podfile`）、特定のバージョン`3.1.6.2`の`AVOSCloud` podを追加します。`Podfile`は以下のようになります：
   ```ruby
   platform :ios, '9.0'  # 最小iOSバージョンを指定（必要に応じて調整）

   target 'YourAppName' do
     use_frameworks!
     pod 'AVOSCloud', '3.1.6.2'  # AVOSCloud SDK用にこの行を追加
   end
   ```
   - `'YourAppName'`を実際のXcodeターゲット名に置き換えてください。
   - Swiftまたはダイナミックフレームワークを使用する場合は`use_frameworks!`が必要です。

4. **Podのインストール**:
   `Podfile`を保存し、ターミナルで以下のコマンドを実行して指定されたバージョンのAVOSCloudをインストールします：
   ```bash
   pod install
   ```
   - これによりAVOSCloud SDKのバージョン`3.1.6.2`がダウンロードされ、`.xcworkspace`ファイルでプロジェクトが設定されます。

5. **ワークスペースを開く**:
   インストール後、開いている場合は`.xcodeproj`を閉じ、新しく作成された`.xcworkspace`ファイルを開きます：
   ```bash
   open YourAppName.xcworkspace
   ```

6. **コードでAVOSCloudをインポートして使用**:
   - Objective-Cの場合：
     ```objc
     #import <AVOSCloud/AVOSCloud.h>

     - (void)example {
         [AVOSCloud setApplicationId:@"your_app_id" clientKey:@"your_client_key"];
         AVObject *testObject = [AVObject objectWithClassName:@"TestObject"];
         [testObject setObject:@"Hello" forKey:@"message"];
         [testObject save];
     }
     ```
   - Swiftの場合：
     ```swift
     import AVOSCloud

     func example() {
         AVOSCloud.setApplicationId("your_app_id", clientKey: "your_client_key")
         let testObject = AVObject(className: "TestObject")
         testObject["message"] = "Hello"
         try? testObject.save()
     }
     ```
   - `"your_app_id"`と`"your_client_key"`を、LeanCloudダッシュボードからのアプリ認証情報に置き換えてください。

7. **アプリ認証情報の設定**:
   - [LeanCloud](https://leancloud.app)（または関連するAVOSCloudサービスプロバイダー）でサインアップします。
   - アプリの設定から`App ID`と`Client Key`を取得し、コード内で設定します（上記のように）。

8. **ビルドと実行**:
   Xcodeでプロジェクトをビルド（`Cmd + B`）し、すべてが正しく設定されていることを確認します。エラーがある場合は、Podfileの構文またはネットワーク接続を確認してください。

---

### 注意点
- **バージョン指定**: `'3.1.6.2'`を指定することで、SDKをその正確なバージョンに固定しています。これは2025年3月3日時点で古い可能性があります。最新バージョンを使用するには、バージョン番号なしで`pod 'AVOSCloud'`と記述します。
- **互換性**: バージョン`3.1.6.2`がiOSデプロイメントターゲット（例：iOS 9.0以上）をサポートしていることを確認してください。詳細は[LeanCloudドキュメント](https://leancloud.app/docs)を確認してください。
- **Podの更新**: CocoaPodsの更新やトラブルシューティングが必要な場合は、以下を実行します：
  ```bash
  pod update
  ```
- **トラブルシューティング**: `pod install`が失敗する場合は、以下を試してください：
  ```bash
  pod repo update
  pod install --verbose
  ```

---

AVOSCloudからの特定の機能（プッシュ通知、リアルタイムメッセージングなど）の統合など、特定の部分でヘルプが必要な場合はお知らせください！