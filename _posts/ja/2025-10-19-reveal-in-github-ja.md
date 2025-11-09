---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GitHub Xcodeプラグインで表示
translated: true
type: note
---

### Reveal-In-GitHubとは？

Reveal-In-GitHubは、Xcodeワークスペースから現在のリポジトリのGitHubの主要機能へ素早く移動できるXcodeプラグインです。GitHubでホストされているGitプロジェクトで作業する開発者のために設計されており、Xcodeを離れたりURLを手動で入力することなく、コミット履歴、blameビュー、プルリクエスト、イシュー、通知などにワンクリック（またはキーボードショートカット）でアクセスできます。

### 前提条件
- Xcodeがインストールされていること（最近のバージョンでテスト済み；特定の最小バージョンの記載はなし）。
- プロジェクトがGitHubでホストされているGitリポジトリであること（プラグインがリポジトリURLとファイルパスを自動検出します）。
- プロジェクトに複数のGitリモートがある場合、初回使用時にデフォルトを選択するよう促されます。

### インストール
主に2つのインストール方法があります：

#### オプション1: Alcatrazを使用（推奨）
1. まだインストールしていない場合は、Alcatraz（Xcodeプラグインのパッケージマネージャー）をインストールします。オンラインでセットアップガイド（例えば[こちら](http://blog.devtang.com/blog/2014/03/05/use-alcatraz-to-manage-xcode-plugins/)（中国語の説明））を見つけることができます。
2. XcodeでAlcatrazを開きます（メニューから：`Window > Package Manager`）。
3. "Reveal In GitHub"を検索します。
4. **Install**をクリックします。
5. Xcodeを再起動します。

#### オプション2: 手動インストール
1. リポジトリをクローンします：  
   ```
   git clone https://github.com/lzwjava/Reveal-In-GitHub.git
   ```
2. `Reveal-In-GitHub.xcodeproj`ファイルをXcodeで開きます。
3. プロジェクトをビルドします（Product > Build または ⌘B）。これにより`Reveal-In-GitHub.xcplugin`ファイルが生成されます。
4. プラグインを以下に移動します：  
   `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins/`
5. Xcodeを再起動します。

インストール後、プラグインはXcodeのメニューバーの**Editor > Reveal In GitHub**に表示されるはずです。

### 使用方法
インストールしXcodeを再起動した後：
1. XcodeでGitHubホストのプロジェクトを開き、ソースファイルを編集します（例：特定の行に移動）。
2. キーボードショートカットまたは**Editor > Reveal In GitHub**のメニュー項目のいずれかを使用してGitHubにジャンプします。プラグインはあなたのリポジトリ、現在のファイル、行番号、最新のコミットハッシュを自動検出します。

以下に、組み込みのメニュー項目とショートカットのクイックリファレンスを示します（ショートカットは ⌃⇧⌘ + タイトルの最初の文字 のパターンに従います）：

| メニュー項目      | ショートカット    | 機能 | GitHub URLの例 (リポジトリ lzwjava/LZAlbum、コミット fd7224 のファイル LZAlbumManager.m の40行目の場合) |
|----------------|-------------|--------------|-----------------------------------------------------------------------------------------------|
| **Setting**    | ⌃⇧⌘S      | カスタマイズパネルを開く | N/A |
| **Repo**       | ⌃⇧⌘R      | メインのリポジトリページを開く | https://github.com/lzwjava/LZAlbum |
| **Issues**     | ⌃⇧⌘I      | イシューリストを開く | https://github.com/lzwjava/LZAlbum/issues |
| **PRs**        | ⌃⇧⌘P      | プルリクエストリストを開く | https://github.com/lzwjava/LZAlbum/pulls |
| **Quick File** | ⌃⇧⌘Q      | 現在の行のファイルビューを開く | https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40 |
| **List History**| ⌃⇧⌘L     | ファイルのコミット履歴を開く | https://github.com/lzwjava/LZAlbum/commits/fd7224/LZAlbum/manager/LZAlbumManager.m |
| **Blame**      | ⌃⇧⌘B      | 現在の行のblameビューを開く | https://github.com/lzwjava/LZAlbum/blame/fd7224/LZAlbum/manager/LZAlbumManager.m#L40 |
| **Notifications**| ⌃⇧⌘N   | リポジトリの通知を開く | https://github.com/lzwjava/LZAlbum/notifications?all=1 |

- **ヒント**:
  - ショートカットはXcodeのデフォルトと競合しません。
  - テキスト範囲が選択されている場合、一部のアクション（Blameなど）はその範囲にアンカーします（例: #L40-L43）。
  - テスト方法：プロジェクトを開き、行に移動し、⌃⇧⌘Bを押すと、ブラウザでblameページが開くはずです。

### カスタマイズ
メニュー項目を調整または追加するには：
1. ⌃⇧⌘Sを押すか、**Editor > Reveal In GitHub > Setting**に移動します。
2. パネルで：
   - "+"ボタンをクリックして新しい項目を追加：タイトル（例："Wiki"）、ショートカット、URLパターンを入力します。
   - URLパターンでは以下のプレースホルダーを使用します：
     - `{git_remote_url}`: フルリポジトリURL（例: https://github.com/user/repo）。
     - `{commit}`: 現在のブランチの最新コミットハッシュ。
     - `{file_path}`: ファイルへの相対パス。
     - `#{selection}`: 現在の行または選択範囲（例: #L40）。
   - 例：Wikiリンクの場合、パターンを`{git_remote_url}/wiki`に設定します。
3. 複数のリモートがある場合は、"Clear Default Repos"ボタンを使用して選択をリセットします。

このプラグインは[ShowInGitHub](https://github.com/larsxschneider/ShowInGitHub)に触発されており、MITライセンスの下でライセンスされています。

[Reveal-In-GitHub GitHub Repository](https://github.com/lzwjava/Reveal-In-GitHub)