---
audio: false
generated: true
lang: ja
layout: post
title: リーンクラウドリアルタイム iOS SDK
translated: true
type: note
---

`pod 'AVOSCloudIM', '3.1.6.2'` を iOS プロジェクトで CocoaPods を使用して利用するには、以下の手順に従ってください。ここでは、CocoaPods がインストール済みであり、Xcode を使用した基本的な iOS 開発に慣れていることを前提としています。

---

### ステップ 1: CocoaPods のセットアップ（まだの場合）
CocoaPods をまだインストールしていない場合は、ターミナルからインストールします：
```bash
sudo gem install cocoapods
```
インストールを確認します：
```bash
pod --version
```

---

### ステップ 2: Xcode プロジェクトを作成または開く
1. 既存の Xcode プロジェクトを開くか、Xcode で新規プロジェクトを作成します。
2. 一旦 Xcode を閉じます（後でワークスペースで再び開きます）。

---

### ステップ 3: Podfile の初期化
1. ターミナルを開き、プロジェクトのルートディレクトリ（`.xcodeproj` ファイルがある場所）に移動します：
   ```bash
   cd /path/to/your/project
   ```
2. まだ Podfile がない場合は、以下を実行して作成します：
   ```bash
   pod init
   ```
   これにより、プロジェクトディレクトリに基本的な `Podfile` が生成されます。

---

### ステップ 4: Podfile の編集
1. テキストエディタ（例: `nano`, `vim`, または VS Code などのコードエディタ）で `Podfile` を開きます：
   ```bash
   open Podfile
   ```
2. `Podfile` を修正して、バージョン `3.1.6.2` の `AVOSCloudIM` pod を含めます。以下は `Podfile` の例です：
   ```ruby
   platform :ios, '9.0'  # 最小 iOS バージョンを指定（必要に応じて調整）
   use_frameworks!       # オプション: プロジェクトが Swift またはフレームワークを使用する場合はこれを使用

   target 'YourAppName' do
     pod 'AVOSCloudIM', '3.1.6.2'  # この行を追加して AVOSCloudIM バージョン 3.1.6.2 を含める
   end
   ```
   - `'YourAppName'` を実際の Xcode ターゲットの名前に置き換えます（通常はアプリの名前）。
   - `platform :ios, '9.0'` の行は最小 iOS バージョンを指定します。プロジェクトの要件に基づいて調整してください。
   - `use_frameworks!` は、プロジェクトが Swift を使用する場合、または pod が動的フレームワークを必要とする場合に必要です。

3. `Podfile` を保存して閉じます。

---

### ステップ 5: Pod のインストール
1. ターミナルで、プロジェクトのルートディレクトリから以下のコマンドを実行します：
   ```bash
   pod install
   ```
   - これにより、`AVOSCloudIM` ライブラリ（バージョン 3.1.6.2）がダウンロードされ、プロジェクトに統合されます。
   - 成功すると、以下のような出力が表示されます：  
     ```
     Pod installation complete! There are X dependencies from the Podfile and X total pods installed.
     ```

2. エラーが発生した場合（例: pod が見つからない）、バージョン `3.1.6.2` が CocoaPods リポジトリでまだ利用可能であることを確認してください。古いバージョンはサポートされていない可能性があります。[CocoaPods.org](https://cocoapods.org) の `AVOSCloudIM` で最新バージョンを確認するか、新しいバージョンに更新してください（例: `pod 'AVOSCloudIM', '~> 12.3'`）。

---

### ステップ 6: ワークスペースを開く
1. インストール後、プロジェクトディレクトリに `.xcworkspace` ファイル（例: `YourAppName.xcworkspace`）が作成されます。
2. このファイルを Xcode で開きます：
   ```bash
   open YourAppName.xcworkspace
   ```
   - 今後は、プロジェクトを操作する際に常に `.xcworkspace` ファイルを使用し、`.xcodeproj` ファイルは使用しないでください。

---

### ステップ 7: コードで AVOSCloudIM をインポートして使用する
1. Swift または Objective-C ファイルで、`AVOSCloudIM` モジュールをインポートします：
   - **Swift**:
     ```swift
     import AVOSCloudIM
     ```
   - **Objective-C**:
     ```objc
     #import <AVOSCloudIM/AVOSCloudIM.h>
     ```
2. ライブラリの機能の使用を開始します。`AVOSCloudIM` は LeanCloud SDK の一部であり、通常はリアルタイムメッセージングに使用されます。具体的な使用例（チャットクライアントのセットアップなど）については、[LeanCloud ドキュメント](https://leancloud.app/docs/)を参照してください：
   - 例 (Swift):
     ```swift
     let client = AVIMClient(clientId: "yourClientID")
     client.open { (succeeded, error) in
         if succeeded {
             print("Connected to LeanCloud IM!")
         } else {
             print("Error: \\(error?.localizedDescription ?? "Unknown")")
         }
     }
     ```

---

### ステップ 8: プロジェクトの設定（必要な場合）
- **App Key と初期化**: LeanCloud SDK では、多くの場合、アプリ ID とキーが必要です。この初期化コードを（例: `AppDelegate` に）追加します：
  - **Swift**:
    ```swift
    import AVOSCloud
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        AVOSCloud.setApplicationId("yourAppID", clientKey: "yourAppKey")
        return true
    }
    ```
  - `"yourAppID"` と `"yourAppKey"` を、あなたの LeanCloud アカウントの認証情報に置き換えます。
- **権限**: アプリが必要な権限（例: インターネットアクセス）を `Info.plist` で持っていることを確認します：
  ```xml
  <key>NSAppTransportSecurity</key>
  <dict>
      <key>NSAllowsArbitraryLoads</key>
      <true/>
  </dict>
  ```

---

### 注意点
- **バージョンの指定**: `pod 'AVOSCloudIM', '3.1.6.2'` を使用すると、その正確なバージョンに固定されます。マイナーアップデートにある程度の柔軟性を持たせたい場合は、`~>` を使用します（例: `pod 'AVOSCloudIM', '~> 3.1.6'` は 3.1.6.1 のような更新を許可しますが、3.2 は許可しません）。
- **トラブルシューティング**: `pod install` が失敗した場合は、以下を試してください：
  - CocoaPods の更新: `sudo gem install cocoapods`
  - キャッシュのクリア: `pod cache clean --all`
  - ローカルの CocoaPods spec リポジトリを更新するために `pod repo update` を実行。
- **LeanCloud SDK**: `AVOSCloudIM` は LeanCloud の一部であるため、追加の設定（例: 彼らのプラットフォームでの登録）については、彼らのセットアップガイドに従ってください。

---

以上です！これで `AVOSCloudIM` バージョン 3.1.6.2 が iOS プロジェクトに統合されました。Xcode でアプリをビルドして実行し、テストしてください。特定の LeanCloud 機能についてヘルプが必要な場合はお知らせください！