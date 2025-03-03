---
audio: false
generated: true
lang: ja
layout: post
title: MBProgressHUDをiOSで使用する
translated: true
---

あなたがiOSプロジェクトで`MBProgressHUD`ライブラリを使用する方法について尋ねているようです。特にバージョン`0.9.1`をCocoaPodsのPodfileを通じて使用する方法についてです。以下にステップバイステップのガイドを示します。

### MBProgressHUDとは？
`MBProgressHUD`は、iOS用の人気のあるサードパーティライブラリで、アクティビティインジケータ、進捗バー、またはカスタムビューを表示する簡単な方法を提供します。通常、読み込み状態や簡単なメッセージを表示するために使用されます。

### `pod 'MBProgressHUD', '0.9.1'`を使用する手順

#### 1. **CocoaPodsのインストール（まだインストールしていない場合）**
CocoaPodsはiOSプロジェクトの依存関係管理ツールです。まだインストールしていない場合は、ターミナルで次のコマンドを実行してください：
```bash
sudo gem install cocoapods
```

#### 2. **Podfileの設定**
- ターミナルでXcodeプロジェクトのディレクトリに移動します：
  ```bash
  cd /path/to/your/project
  ```
- まだPodfileがない場合は、次のコマンドを実行して作成します：
  ```bash
  pod init
  ```
- テキストエディタで`Podfile`を開きます（例：`nano Podfile`または`open Podfile`）。

#### 3. **PodfileにMBProgressHUDを追加**
`Podfile`内のアプリのターゲットブロックに、`MBProgressHUD`バージョン`0.9.1`の行を追加します。以下のようになります：
```ruby
platform :ios, '9.0'  # 配置ターゲットを指定

target 'YourAppName' do
  use_frameworks!
  pod 'MBProgressHUD', '0.9.1'
end
```
- `'YourAppName'`を実際のXcodeターゲット名に置き換えます。
- `platform :ios, '9.0'`行は最小iOSバージョンを設定します。プロジェクトのニーズに応じて調整してください。

#### 4. **Podのインストール**
- `Podfile`を保存し、ターミナルで次のコマンドを実行します：
  ```bash
  pod install
  ```
- これにより、`MBProgressHUD`バージョン`0.9.1`がプロジェクトにダウンロードされ、統合されます。成功すると、インストールが確認される出力が表示されます。

#### 5. **ワークスペースを開く**
- インストール後、Xcodeプロジェクトを閉じ（開いている場合）、新しく作成された`.xcworkspace`ファイル（例：`YourAppName.xcworkspace`）を開きます。CocoaPodsはこのワークスペースを作成して依存関係を管理します。

#### 6. **コードでMBProgressHUDを使用する**
- **Swift**：モジュールをインポートし、コードで使用します：
  ```swift
  import MBProgressHUD

  class ViewController: UIViewController {
      override func viewDidLoad() {
          super.viewDidLoad()

          // 読み込みインジケータ付きの簡単なHUDを表示
          let hud = MBProgressHUD.showAdded(to: self.view, animated: true)
          hud.label.text = "Loading..."

          // 一定時間後に非表示にする（例：2秒）
          DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
              hud.hide(animated: true)
          }
      }
  }
  ```

- **Objective-C**：ヘッダーをインポートし、使用します：
  ```objc
  #import <MBProgressHUD/MBProgressHUD.h>

  @interface ViewController ()
  @end

  @implementation ViewController
  - (void)viewDidLoad {
      [super viewDidLoad];

      // 読み込みインジケータ付きの簡単なHUDを表示
      MBProgressHUD *hud = [MBProgressHUD showHUDAddedTo:self.view animated:YES];
      hud.label.text = @"Loading...";

      // 一定時間後に非表示にする（例：2秒）
      dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 2 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
          [hud hideAnimated:YES];
      });
  }
  @end
  ```

#### 7. **MBProgressHUDの一般的な機能**
- **基本的なHUD**：上記のように、オプションのテキスト付きのスピンインジケータを表示します。
- **カスタムテキストのみ**：
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .text
  hud.label.text = "Done!"
  hud.hide(animated: true, afterDelay: 1.5)
  ```
- **進捗バー**：
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .determinate
  hud.progress = 0.5 // 50%進捗
  ```

#### 注意点
- **バージョン0.9.1**：これは古いバージョン（2015年頃にリリース）です。2025年3月現在の最新バージョンはもっと新しいもの（例：1.2.0以上）です。最新バージョンを使用するには、`pod 'MBProgressHUD'`とバージョン番号を指定せずに記述します。互換性のために特定に0.9.1が必要でない限り、更新を検討してください。
- **ドキュメント**：[MBProgressHUD GitHubページ](https://github.com/jdg/MBProgressHUD)を確認して、さらに多くのオプションと例を確認してください。バージョン0.9.1は現代的なリリースよりも機能が少ないかもしれません。