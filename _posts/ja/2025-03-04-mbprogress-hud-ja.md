---
audio: false
generated: true
lang: ja
layout: post
title: iOSでのMBProgressHUDの使用方法
translated: true
type: note
---

iOSプロジェクトでCocoaPodsのPodfileを使用して`MBProgressHUD`ライブラリ（バージョン`0.9.1`）を利用する方法についてお問い合わせのようです。ステップバイステップでご説明します。

### MBProgressHUDとは？
`MBProgressHUD`は、アクティビティインジケータ、プログレスバー、カスタムビューを含むHUD（ヘッドアップディスプレイ）を簡単に表示できる人気のiOSサードパーティライブラリで、ローディング状態や簡潔なメッセージ表示に使用されます。

### `pod 'MBProgressHUD', '0.9.1'`の使用方法

#### 1. **CocoaPodsのインストール（未インストールの場合）**
CocoaPodsはiOSプロジェクトの依存関係管理ツールです。未インストールの場合は、ターミナルで以下のコマンドを実行してください：
```bash
sudo gem install cocoapods
```

#### 2. **Podfileのセットアップ**
- ターミナルでXcodeプロジェクトディレクトリに移動：
  ```bash
  cd /path/to/your/project
  ```
- Podfileがまだない場合は、以下を実行して作成：
  ```bash
  pod init
  ```
- テキストエディタで`Podfile`を開く（例：`nano Podfile` または `open Podfile`）

#### 3. **PodfileへのMBProgressHUDの追加**
`Podfile`内のアプリターゲットブロック内に`MBProgressHUD`バージョン`0.9.1`の行を追加します。以下のようになります：
```ruby
platform :ios, '9.0'  # デプロイメントターゲットを指定

target 'YourAppName' do
  use_frameworks!
  pod 'MBProgressHUD', '0.9.1'
end
```
- `'YourAppName'`は実際のXcodeターゲット名に置き換えてください
- `platform :ios, '9.0'`行は最小iOSバージョンを設定します。プロジェクトの要件に応じて調整してください

#### 4. **Podのインストール**
- `Podfile`を保存し、ターミナルで以下のコマンドを実行：
  ```bash
  pod install
  ```
- これにより`MBProgressHUD`バージョン`0.9.1`がダウンロードされプロジェクトに統合されます。成功するとインストール確認の出力が表示されます

#### 5. **ワークスペースを開く**
- インストール後、Xcodeプロジェクトを閉じ（開いている場合）、`.xcodeproj`ファイルの代わりに新しく作成された`.xcworkspace`ファイル（例：`YourAppName.xcworkspace`）を開いてください。CocoaPodsは依存関係を管理するためにこのワークスペースを生成します

#### 6. **コードでのMBProgressHUDの使用方法**
- **Swift**: モジュールをインポートしてコード内で使用：
  ```swift
  import MBProgressHUD

  class ViewController: UIViewController {
      override func viewDidLoad() {
          super.viewDidLoad()
          
          // ローディングインジケータ付きのシンプルなHUDを表示
          let hud = MBProgressHUD.showAdded(to: self.view, animated: true)
          hud.label.text = "Loading..."
          
          // 一定時間後（例：2秒）に非表示
          DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
              hud.hide(animated: true)
          }
      }
  }
  ```

- **Objective-C**: ヘッダーをインポートして使用：
  ```objc
  #import <MBProgressHUD/MBProgressHUD.h>

  @interface ViewController ()
  @end

  @implementation ViewController
  - (void)viewDidLoad {
      [super viewDidLoad];
      
      // ローディングインジケータ付きのシンプルなHUDを表示
      MBProgressHUD *hud = [MBProgressHUD showHUDAddedTo:self.view animated:YES];
      hud.label.text = @"Loading...";
      
      // 一定時間後（例：2秒）に非表示
      dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 2 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
          [hud hideAnimated:YES];
      });
  }
  @end
  ```

#### 7. **MBProgressHUDの主な機能**
- **基本HUD**: 上記のように、テキスト付きのスピニングインジケータを表示
- **カスタムテキストのみ**:
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .text
  hud.label.text = "Done!"
  hud.hide(animated: true, afterDelay: 1.5)
  ```
- **プログレスバー**:
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .determinate
  hud.progress = 0.5 // 50% progress
  ```

#### 注意点
- **バージョン0.9.1**: これは古いバージョン（2015年頃リリース）です。最新バージョン（2025年3月現在では1.2.0以上）を使用するには、バージョン番号なしで`pod 'MBProgressHUD'`と記述してください。互換性のために0.9.1が必要な場合を除き、更新を検討してください
- **ドキュメント**: 詳細なオプションと例については[MBProgressHUD GitHubページ](https://github.com/jdg/MBProgressHUD)を確認してください。バージョン0.9.1は最新リリースよりも機能が少ない場合があります

トラブルシューティングやより具体的な例が必要な場合はお知らせください！