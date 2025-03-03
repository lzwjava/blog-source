---
audio: false
generated: true
lang: ja
layout: post
title: リアルタイムiOS SDK
translated: true
---

CocoaPodsを使用してiOSプロジェクトに`pod 'AVOSCloudIM', '3.1.6.2'`を使用するには、以下の手順に従ってください。これは、CocoaPodsがインストールされていることと、基本的なiOS開発に関するXcodeの知識があることを前提としています。

---

### ステップ1: CocoaPodsのセットアップ（まだ行っていない場合）
まだCocoaPodsをインストールしていない場合は、ターミナルからインストールします：
```bash
sudo gem install cocoapods
```
インストールを確認します：
```bash
pod --version
```

---

### ステップ2: Xcodeプロジェクトの作成または開き
1. 既存のXcodeプロジェクトを開くか、新しいプロジェクトを作成します。
2. 今はXcodeを閉じておきます（後でワークスペースを使用して再度開きます）。

---

### ステップ3: Podfileの初期化
1. ターミナルを開き、プロジェクトのルートディレクトリ（`.xcodeproj`ファイルが存在する場所）に移動します：
   ```bash
   cd /path/to/your/project
   ```
2. まだPodfileがない場合は、以下のコマンドを実行して作成します：
   ```bash
   pod init
   ```
   これにより、プロジェクトディレクトリに基本的な`Podfile`が生成されます。

---

### ステップ4: Podfileの編集
1. テキストエディタ（例：`nano`、`vim`、またはVS Codeなどのコードエディタ）で`Podfile`を開きます：
   ```bash
   open Podfile
   ```
2. `Podfile`を編集して、`AVOSCloudIM`ポッドのバージョン`3.1.6.2`を含めます。以下は、`Podfile`の例です：
   ```ruby
   platform :ios, '9.0'  # 最小iOSバージョンを指定（必要に応じて調整）
   use_frameworks!       # オプション：プロジェクトがSwiftまたはフレームワークを使用している場合に使用

   target 'YourAppName' do
     pod 'AVOSCloudIM', '3.1.6.2'  # AVOSCloudIMバージョン3.1.6.2を含めるためにこの行を追加
   end
   ```
   - `'YourAppName'`を、実際のXcodeターゲットの名前（通常はアプリの名前）に置き換えます。
   - `platform :ios, '9.0'`行は最小iOSバージョンを指定します。プロジェクトの要件に応じて調整してください。
   - `use_frameworks!`は、プロジェクトがSwiftを使用している場合、またはポッドが動的フレームワークを必要とする場合に必要です。

3. `Podfile`を保存して閉じます。

---

### ステップ5: ポッドのインストール
1. ターミナルで、プロジェクトのルートディレクトリから以下のコマンドを実行します：
   ```bash
   pod install
   ```
   - これにより、`AVOSCloudIM`ライブラリ（バージョン3.1.6.2）がプロジェクトにダウンロードされ、統合されます。
   - 成功すると、以下のような出力が表示されます：
     ```
     Pod installation complete! There are X dependencies from the Podfile and X total pods installed.
     ```

2. エラーが発生した場合（例：ポッドが見つからない）、バージョン`3.1.6.2`がCocoaPodsリポジトリでまだ利用可能であることを確認してください。古いバージョンはサポートされていない場合があります。最新バージョンは[CocoaPods.org](https://cocoapods.org)の`AVOSCloudIM`で確認するか、新しいバージョン（例：`pod 'AVOSCloudIM', '~> 12.3'`）に更新してください。

---

### ステップ6: ワークスペースの開き
1. インストール後、プロジェクトディレクトリに`.xcworkspace`ファイルが作成されます（例：`YourAppName.xcworkspace`）。
2. このファイルをXcodeで開きます：
   ```bash
   open YourAppName.xcworkspace
   ```
   - 今後は、プロジェクトを操作する際には`.xcworkspace`ファイルを使用してください。

---

### ステップ7: コードでAVOSCloudIMをインポートして使用
1. SwiftまたはObjective-Cファイルで`AVOSCloudIM`モジュールをインポートします：
   - **Swift**:
     ```swift
     import AVOSCloudIM
     ```
   - **Objective-C**:
     ```objc
     #import <AVOSCloudIM/AVOSCloudIM.h>
     ```
2. ライブラリの機能を使用を開始します。`AVOSCloudIM`は、通常リアルタイムメッセージングに使用されるLeanCloud SDKの一部です。具体的な使用例については、[LeanCloudドキュメント](https://leancloud.app/docs/)を参照してください。例えば、チャットクライアントの設定：
   - 例（Swift）：
     ```swift
     let client = AVIMClient(clientId: "yourClientID")
     client.open { (succeeded, error) in
         if succeeded {
             print("Connected to LeanCloud IM!")
         } else {
             print("Error: \(error?.localizedDescription ?? "Unknown")")
         }
     }
     ```

---

### ステップ8: プロジェクトの設定（必要に応じて）
- **App Keyと初期化**：LeanCloud SDKは通常、アプリIDとキーが必要です。以下の初期化コードを追加します（例：`AppDelegate`）：
  - **Swift**:
    ```swift
    import AVOSCloud
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        AVOSCloud.setApplicationId("yourAppID", clientKey: "yourAppKey")
        return true
    }
    ```
  - `"yourAppID"`と`"yourAppKey"`を、LeanCloudアカウントの資格情報に置き換えます。
- **権限**：`Info.plist`でアプリが必要な権限（例：インターネットアクセス）を持っていることを確認します：
  ```xml
  <key>NSAppTransportSecurity</key>
  <dict>
      <key>NSAllowsArbitraryLoads</key>
      <true/>
  </dict>
  ```

---

### 注意点
- **バージョンの特定**：`pod 'AVOSCloudIM', '3.1.6.2'`はそのバージョンに固定されます。マイナーバージョンの更新を許可するには、`~>`を使用します（例：`pod 'AVOSCloudIM', '~> 3.1.6'`は3.1.6.1などの更新を許可しますが、3.2は許可しません）。
- **トラブルシューティング**：`pod install`が失敗した場合は、以下を試してください：
  - CocoaPodsの更新：`sudo gem install cocoapods`
  - キャッシュのクリア：`pod cache clean --all`
  - `pod repo update`を実行してローカルCocoaPods specリポジトリを更新します。
- **LeanCloud SDK**：`AVOSCloudIM`はLeanCloudの一部であるため、追加の設定（例：プラットフォームでの登録）に従ってください。

---

これで、`AVOSCloudIM`バージョン3.1.6.2をiOSプロジェクトに統合しました。Xcodeでアプリをビルドして実行してテストしてください。LeanCloudの特定の機能についてのヘルプが必要な場合はお知らせください！