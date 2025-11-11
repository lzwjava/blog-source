---
audio: false
generated: true
lang: ja
layout: post
title: iOSでのPopMenuの使い方
translated: true
type: note
---

iOSプロジェクトで`pod 'PopMenu', '2.4'`を使用するには、人気のiOS依存関係マネージャーであるCocoaPodsを通じてPopMenuライブラリ（バージョン2.4）を統合します。このライブラリは、Sina WeiboやNetEaseのようなアプリにインスパイアされたポップアップアニメーションメニューを提供します。以下はプロジェクトでのセットアップと使用方法です：

---

### ステップ1: CocoaPodsのインストール（未インストールの場合）
システムにCocoaPodsがインストールされていない場合は、まずインストールしてください：
1. ターミナルを開きます。
2. 次のコマンドを実行します：
   ```bash
   sudo gem install cocoapods
   ```
3. インストールを確認します：
   ```bash
   pod --version
   ```

---

### ステップ2: Podfileの設定
1. ターミナルでXcodeプロジェクトディレクトリに移動します：
   ```bash
   cd /path/to/your/project
   ```
2. Podfileがまだない場合は、次のコマンドを実行して作成します：
   ```bash
   pod init
   ```
3. テキストエディタで`Podfile`を開きます（例：`nano Podfile`またはXcodeを使用）。
4. ターゲットにPopMenu podを指定するために次の行を追加します：
   ```ruby
   platform :ios, '8.0'  # 必要に応じてiOSバージョンを調整
   target 'YourAppName' do
     use_frameworks!
     pod 'PopMenu', '2.4'
   end
   ```
   - `YourAppName`をあなたのXcodeターゲット名に置き換えてください。
   - `use_frameworks!`行は、PopMenuがフレームワークベースのライブラリであるため必要です。

5. Podfileを保存して閉じます。

---

### ステップ3: Podのインストール
1. ターミナルで次のコマンドを実行します：
   ```bash
   pod install
   ```
2. これによりPopMenuバージョン2.4がプロジェクトにダウンロード・統合されます。次のようなメッセージが表示されるまで待ちます：
   ```
   Pod installation complete! There are X dependencies from the Podfile and X total pods installed.
   ```
3. 開いている場合はXcodeプロジェクトを閉じ、その後`.xcodeproj`ファイルの代わりに新しく生成された`.xcworkspace`ファイル（例：`YourAppName.xcworkspace`）を開きます。

---

### ステップ4: コードでの基本的な使用方法
PopMenuはObjective-Cで書かれているため、それに応じて使用する必要があります。アプリでの実装例を以下に示します：

1. **ライブラリのインポート**：
   - Objective-Cファイル（例：`ViewController.m`）の場合：
     ```objective-c
     #import "PopMenu.h"
     ```
   - Swiftを使用している場合は、ブリッジングヘッダーを作成します：
     - `File > New > File > Header File`に移動します（例：`YourAppName-Bridging-Header.h`）。
     - 以下を追加します：
       ```objective-c
       #import "PopMenu.h"
       ```
     - Xcodeで、`Build Settings > Swift Compiler - General > Objective-C Bridging Header`でブリッジングヘッダーのパスを設定します（例：`YourAppName/YourAppName-Bridging-Header.h`）。

2. **メニュー項目の作成**：
   ポップアップメニューに表示する項目を定義します。各項目にはタイトル、アイコン、グローカラーを設定できます。
   ```objective-c
   NSMutableArray *items = [[NSMutableArray alloc] init];
   
   MenuItem *menuItem1 = [[MenuItem alloc] initWithTitle:@"Flickr" 
                                               iconName:@"post_type_bubble_flickr" 
                                              glowColor:[UIColor grayColor] 
                                                  index:0];
   [items addObject:menuItem1];
   
   MenuItem *menuItem2 = [[MenuItem alloc] initWithTitle:@"Twitter" 
                                               iconName:@"post_type_bubble_twitter" 
                                              glowColor:[UIColor blueColor] 
                                                  index:1];
   [items addObject:menuItem2];
   ```

3. **メニューの初期化と表示**：
   `PopMenu`インスタンスを作成し、ビューに表示します。
   ```objective-c
   PopMenu *popMenu = [[PopMenu alloc] initWithFrame:self.view.bounds items:items];
   popMenu.menuAnimationType = kPopMenuAnimationTypeNetEase; // オプション: kPopMenuAnimationTypeSina または kPopMenuAnimationTypeNetEase
   popMenu.perRowItemCount = 2; // 行あたりの項目数
   [popMenu showMenuAtView:self.view];
   ```

4. **選択の処理（オプション）**：
   サブクラス化または機能拡張でタップを検出できますが、PopMenuの基本バージョン（2.4時点）ではデリゲートをネイティブサポートしていない可能性があります。更新やカスタマイズについては、GitHub（`xhzengAIB/PopMenu`）のライブラリドキュメントを確認してください。

---

### ステップ5: プロジェクトの実行
Xcodeでプロジェクトをビルドして実行します（`Cmd + R`）。アイコン（例：`post_type_bubble_flickr`）がアセットカタログの一部である場合は、プロジェクトに追加されていることを確認してください。そうでない場合は、入手または作成する必要があります。

---

### 注意点
- **バージョン指定**: `pod 'PopMenu', '2.4'`はバージョン2.4に固定します。最新バージョンを使用したい場合は、バージョン番号なしで`pod 'PopMenu'`を使用しますが、これは破壊的変更をもたらす可能性があります。
- **互換性**: プロジェクトのデプロイメントターゲットが少なくともiOS 8.0以上であることを確認してください（またはPodfileの`platform`を調整してください）。
- **カスタマイズ**: PopMenuはアニメーションタイプやレイアウトの調整（例：`perRowItemCount`）を可能にします。詳細なオプションについてはソースコードを探索してください。
- **トラブルシューティング**: 「file not found」のようなエラーが発生した場合は、Podsが正しくインストールされ、ワークスペースが使用されていることを確認してください。

これでiOSアプリでのPopMenu 2.4の使用を開始できるはずです！さらに説明が必要な場合はお知らせください。