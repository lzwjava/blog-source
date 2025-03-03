---
audio: false
generated: true
lang: ja
layout: post
title: LeanCloud iOS SDK
translated: true
---

`pod 'AVOSCloud', '3.1.6.2'` を iOS プロジェクトで使用するには、CocoaPods を使って AVOSCloud SDK（おそらく LeanCloud のクラウドサービス用 SDK）を統合することを指しています。以下はその設定方法のステップバイステップガイドです。

---

### 前提条件
1. **CocoaPods のインストール**: CocoaPods がインストールされていない場合は、まず以下のコマンドをターミナルで実行してインストールします:
   ```bash
   sudo gem install cocoapods
   ```
2. **Xcode プロジェクト**: Xcode に既存の iOS プロジェクトがあることを確認します。

---

### `pod 'AVOSCloud', '3.1.6.2'` を使用する手順

1. **プロジェクトディレクトリに移動**:
   ターミナルを開き、`.xcodeproj` ファイルを含むディレクトリに移動します:
   ```bash
   cd /path/to/your/project
   ```

2. **Podfile の初期化** (既に存在しない場合):
   以下のコマンドを実行して `Podfile` を作成します:
   ```bash
   pod init
   ```

3. **Podfile の編集**:
   テキストエディタ（例: `nano Podfile` または `open Podfile`）で `Podfile` を開き、特定のバージョン `3.1.6.2` の `AVOSCloud` pod を追加します。`Podfile` は以下のようになります:
   ```ruby
   platform :ios, '9.0'  # 最小 iOS バージョンを指定（必要に応じて調整）

   target 'YourAppName' do
     use_frameworks!
     pod 'AVOSCloud', '3.1.6.2'  # AVOSCloud SDK 用のこの行を追加
   end
   ```
   - `'YourAppName'` を実際の Xcode ターゲット名に置き換えます。
   - Swift または動的フレームワークを使用している場合、`use_frameworks!` は必要です。

4. **Pod のインストール**:
   `Podfile` を保存し、ターミナルで以下のコマンドを実行して指定されたバージョンの AVOSCloud をインストールします:
   ```bash
   pod install
   ```
   - これはバージョン `3.1.6.2` の AVOSCloud SDK をダウンロードし、プロジェクトを `.xcworkspace` ファイルと一緒に設定します。

5. **ワークスペースを開く**:
   インストール後、`.xcodeproj` が開いている場合は閉じ、新しく作成された `.xcworkspace` ファイルを開きます:
   ```bash
   open YourAppName.xcworkspace
   ```

6. **コードで AVOSCloud をインポートして使用**:
   - Objective-C:
     ```objc
     #import <AVOSCloud/AVOSCloud.h>

     - (void)example {
         [AVOSCloud setApplicationId:@"your_app_id" clientKey:@"your_client_key"];
         AVObject *testObject = [AVObject objectWithClassName:@"TestObject"];
         [testObject setObject:@"Hello" forKey:@"message"];
         [testObject save];
     }
     ```
   - Swift:
     ```swift
     import AVOSCloud

     func example() {
         AVOSCloud.setApplicationId("your_app_id", clientKey: "your_client_key")
         let testObject = AVObject(className: "TestObject")
         testObject["message"] = "Hello"
         try? testObject.save()
     }
     ```
   - `"your_app_id"` と `"your_client_key"` を LeanCloud のダッシュボードからのアプリの認証情報に置き換えます。

7. **アプリの認証情報を設定**:
   - [LeanCloud](https://leancloud.app)（または関連する AVOSCloud サービスプロバイダー）にサインアップします。
   - アプリの設定から `App ID` と `Client Key` を取得し、コードに設定します（上記のように）。

8. **ビルドと実行**:
   Xcode でプロジェクトをビルド (`Cmd + B`) して、すべてが正しく設定されていることを確認します。エラーがある場合は、Podfile の構文やネットワーク接続を確認します。

---

### 注意点
- **バージョン固定**: `'3.1.6.2'` を指定することで、SDK をそのバージョンに固定しています。これは 2025 年 3 月 3 日時点で古くなっているかもしれません。最新バージョンを使用するには、バージョン番号を省略して `pod 'AVOSCloud'` と記述します。
- **互換性**: バージョン `3.1.6.2` が iOS 9.0 以降のデプロイメントターゲットをサポートしていることを確認します。詳細については [LeanCloud ドキュメント](https://leancloud.app/docs) を確認してください。
- **Pod の更新**: CocoaPods を更新したりトラブルシューティングしたりするには、以下を実行します:
  ```bash
  pod update
  ```
- **トラブルシューティング**: `pod install` が失敗した場合は、以下を試してください:
  ```bash
  pod repo update
  pod install --verbose
  ```

---

特定の部分（例: プッシュ通知やリアルタイムメッセージングの機能の統合）でお手伝いが必要な場合はお知らせください！