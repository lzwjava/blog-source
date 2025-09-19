---
audio: false
generated: false
image: false
lang: ja
layout: post
title: 'Xcode プラグイン: GitHub で表示'
translated: true
---

これは、GitHubプロジェクト [https://github.com/lzwjava/Reveal-In-GitHub](https://github.com/lzwjava/Reveal-In-GitHub) からの README.md ファイルです。

---

# Reveal-In-GitHub

Xcode用のプラグインで、現在のリポジトリ内で重要なGitHub機能にシームレスにナビゲートします。クリック一つで、GitHubの履歴、ブレーム、プルリクエスト、Issues、通知などを数秒でアクセスできます。

![プラグイン](https://cloud.githubusercontent.com/assets/5022872/10867703/96e980be-80ab-11e5-9aaa-a06ef476b7f7.gif)

私たちの会社はGitHubで働いています。頻繁にGitHubを開きます。時々、Xcodeで編集中にコードを理解できない場合、GitHubでブレームします。また、ファイルの最新コミットを見てコードの進化を理解することで、問題を解決します。そのため、XcodeからGitHubを迅速に開くツールがあれば良いと考えました。このプラグインを作成しました。Xcodeでソースファイルを編集しているとき、どのGitHubリポジトリで作業しているか、どのファイルを編集しているかを簡単に知ることができます。したがって、GitHubのファイルに迅速にジャンプすることができます。現在編集中の行をGitHubで迅速にブレームすることができます。また、Xcodeで作業中の現在のリポジトリの問題やPRに迅速にジャンプすることができます。

## メニュー項目

<img width="700" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864813/5df3f05e-8034-11e5-9f3e-03ae3fbc3cfc.png">

以下の6つのメニュー項目があります：

 メニュータイトル     | ショートカット              | GitHub URL パターン（LZAlbumManager.m 行40を編集中の場合）
----------------|-----------------------|----------------------------------
 設定	    |⌃⇧⌘S |
 リポジトリ           |⌃⇧⌘R | https://github.com/lzwjava/LZAlbum
 Issues         |⌃⇧⌘I | https://github.com/lzwjava/LZAlbum/issues
 PRs            |⌃⇧⌘P | https://github.com/lzwjava/LZAlbum/pulls
 快速ファイル     |⌃⇧⌘Q | https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 履歴リスト   |⌃⇧⌘L | https://github.com/lzwjava/LZAlbum/commits/fd7224/LZAlbum/manager/LZAlbumManager.m
 ブレーム          |⌃⇧⌘B | https://github.com/lzwjava/LZAlbum/blame/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 通知  |⌃⇧⌘N | https://github.com/leancloud/LZAlbum/notifications?all=1

ショートカットは、Xcodeのデフォルトショートカットと競合しないように設計されています。ショートカットパターンは⌃⇧⌘（Ctrl+Shift+Command）に、メニュータイトルの先頭文字を追加したものです。

## カスタマイズ

時々、ウィキに迅速にジャンプしたい場合があります。以下のように設定を開くことができます：

<img width="500" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864939/fa83f286-8037-11e5-97d7-e9549485b11d.png">

例えば、

クイックファイルのパターンと実際のURL:

```
           {git_remote_url}       /blob/{commit}/          {file_path}         #{selection}
https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40-L43
```

{commit} は現在のブランチの最新コミットハッシュです。ブランチを使用するよりも優れています。 porque HEAD が変更される可能性があるためです。したがって、#L40-L43 のコードも変更される可能性があります。

したがって、現在のリポジトリのウィキにショートカットを追加したい場合は、メニュー項目を追加し、パターンを `{git_remote_url}/wiki` に設定してください。

設定で、`Clear Default Repos` は、複数のGitリモートがある場合、最初にトリガーすると、選択するよう促されます：

<img width="400" src="https://cloud.githubusercontent.com/assets/5022872/10865120/5794994a-803c-11e5-9527-965f7e617e8f.png">

その後、プラグインが選択したリモートを記憶します。したがって、メニューを再度トリガーすると、そのリモートリポジトリがデフォルトとして開きます。ボタン `Clear Default Repos` はこの設定をクリアし、再度選択するように促します。

## インストール

[Alcatraz](http://alcatraz.io/)でインストールすることをお勧めします。

![qq20151101-1 2x](https://cloud.githubusercontent.com/assets/5022872/10867743/0ce351c6-80ae-11e5-82e2-f740887153f7.jpg)

または

1. このリポジトリをクローンします。
2. `Reveal-In-GitHub.xcodeproj` を開き、ビルドします。
3. Reveal-In-GitHub.xcplugin は `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins` に配置されるべきです。
4. Xcodeを再起動します。
5. 任意のGitHubプロジェクトを開き、⌃⇧⌘B（Ctrl+Shift+Command+B）を押してコードをブレームします。

## 安装

[Alcatraz](http://alcatraz.io/)の使用をお勧めします。[博客](http://blog.devtang.com/blog/2014/03/05/use-alcatraz-to-manage-xcode-plugins/)を参照してください。インストール後、上記の画像で「Reveal In GitHub」を検索し、「Install」をクリックしてください。

このツールを使用しない場合は、以下の3ステップで完了します：

* このプロジェクトをローカルにクローンします。
* xcodeprojを開き、Buildをクリックしてビルドします。これにより、ディレクトリ`~/Library/Application Support/Developer/Shared/Xcode/Plug-ins`にReveal-In-GitHub.xcpluginファイルが生成されます。
* Xcodeを再起動し、GitHubに置かれた任意のプロジェクトを開きます。 `Ctrl+Shift+Command+B` を押してコードをブレームします。

## クレジット

開発中に、類似の機能を持つ他のプラグイン [ShowInGitHub](https://github.com/larsxschneider/ShowInGitHub) を発見しました。その技術を学びました。ありがとう。

## ライセンス

MIT