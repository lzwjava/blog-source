---
audio: false
generated: true
lang: ja
layout: post
title: PopMenuをiOSで使用する
translated: true
---

`pod 'PopMenu', '2.4'` を iOS プロジェクトで使用するには、CocoaPods を通じて PopMenu ライブラリ（バージョン 2.4）を統合しています。このライブラリは、Sina Weibo や NetEase のようなアプリに触発されたポップアップアニメーションメニューを提供します。以下に、プロジェクトで設定して使用するための手順を示します。

---

### ステップ 1: CocoaPods のインストール（まだインストールしていない場合）
CocoaPods がシステムにインストールされていない場合は、まずインストールしてください：
1. ターミナルを開きます。
2. このコマンドを実行します：
   ```bash
   sudo gem install cocoapods
   ```
3. インストールを確認します：
   ```bash
   pod --version
   ```

---

### ステップ 2: Podfile の設定
1. ターミナルで Xcode プロジェクトのディレクトリに移動します：
   ```bash
   cd /path/to/your/project
   ```
2. Podfile がまだない場合は、以下のコマンドを実行して作成します：
   ```bash
   pod init
   ```
3. テキストエディタで `Podfile` を開きます（例：`nano Podfile` または Xcode を使用）。
4. ターゲットに対して PopMenu pod を指定するために、以下の行を追加します：
   ```ruby
   platform :ios, '8.0'  # 必要に応じて iOS バージョンを調整
   target 'YourAppName' do
     use_frameworks!
     pod 'PopMenu', '2.4'
   end
   ```
   - `YourAppName` を Xcode ターゲットの名前に置き換えます。
   - `use_frameworks!` 行は、PopMenu がフレームワークベースのライブラリであるために必要です。

5. Podfile を保存して閉じます。

---

### ステップ 3: Pod のインストール
1. ターミナルで以下のコマンドを実行します：
   ```bash
   pod install
   ```
2. これにより、PopMenu バージョン 2.4 がプロジェクトにダウンロードされて統合されます。以下のようなメッセージが表示されるまで待ちます：
   ```
   Pod installation complete! There are X dependencies from the Podfile and X total pods installed.
   ```
3. Xcode プロジェクトが開いている場合は閉じ、新しく生成された `.xcworkspace` ファイル（例：`YourAppName.xcworkspace`）を開きます。`.xcodeproj` ファイルではなく。

---

### ステップ 4: コードでの基本的な使用
PopMenu は Objective-C で記述されているため、それに応じて使用する必要があります。アプリに実装する方法の例を示します：

1. **ライブラリのインポート**:
   - Objective-C ファイル（例：`ViewController.m`）で：
     ```objective-c
     #import "PopMenu.h"
     ```
   - Swift を使用している場合は、ブリッジヘッダーを作成します：
     - `File > New > File > Header File`（例：`YourAppName-Bridging-Header.h`）に移動します。
     - 以下を追加します：
       ```objective-c
       #import "PopMenu.h"
       ```
     - Xcode で `Build Settings > Swift Compiler - General > Objective-C Bridging Header` のブリッジヘッダーをヘッダーファイルのパス（例：`YourAppName/YourAppName-Bridging-Header.h`）に設定します。

2. **メニュー項目の作成**:
   ポップアップメニューに含めたい項目を定義します。各項目にはタイトル、アイコン、グローカラーがあります。
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

3. **メニューの初期化と表示**:
   `PopMenu` インスタンスを作成し、ビューに表示します。
   ```objective-c
   PopMenu *popMenu = [[PopMenu alloc] initWithFrame:self.view.bounds items:items];
   popMenu.menuAnimationType = kPopMenuAnimationTypeNetEase; // オプション: kPopMenuAnimationTypeSina または kPopMenuAnimationTypeNetEase
   popMenu.perRowItemCount = 2; // 行ごとの項目数
   [popMenu showMenuAtView:self.view];
   ```

4. **選択の処理（オプション）**:
   タップを検出するためにサブクラス化または機能を拡張することができますが、PopMenu の基本バージョン（2.4）はデフォルトでデリゲートをサポートしていないかもしれません。GitHub のライブラリのドキュメント（`xhzengAIB/PopMenu`）を確認して、更新やカスタマイズが行われているかどうかを確認してください。

---

### ステップ 5: プロジェクトの実行
Xcode でプロジェクトをビルドして実行します（`Cmd + R`）。アイコン（例：`post_type_bubble_flickr`）がアセットカタログの一部である場合は、プロジェクトに追加されていることを確認してください。そうでない場合は、ソースまたは作成する必要があります。

---

### 注意点
- **バージョンの特定性**: `pod 'PopMenu', '2.4'` はバージョン 2.4 に固定されます。最新バージョンを使用する場合は、バージョン番号を省略して `pod 'PopMenu'` としますが、これは破壊的な変更を導入する可能性があります。
- **互換性**: プロジェクトのデプロイメントターゲットは少なくとも iOS 8.0 であることを確認し、必要に応じて Podfile の `platform` を調整します。
- **カスタマイズ**: PopMenu はアニメーションタイプやレイアウトの調整（例：`perRowItemCount`）を許可します。ソースコードを探索して、さらに多くのオプションを見つけてください。
- **トラブルシューティング**: 「ファイルが見つからない」といったエラーが発生した場合、Pods が正しくインストールされていることを確認し、ワークスペースが使用されていることを確認してください。

これで、iOS アプリで PopMenu 2.4 の使用が始まります！ さらに詳しい説明が必要な場合はお知らせください。