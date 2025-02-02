---
audio: false
lang: ja
layout: post
title: 'Xcode プラグイン: GitHub で表示する'
translated: true
---

これは GitHub プロジェクト [https://github.com/lzwjava/Reveal-In-GitHub](https://github.com/lzwjava/Reveal-In-GitHub) の README.md です。

---

# Reveal-In-GitHub

現在のリポジトリ内で主要な GitHub 機能に対してシームレスなナビゲーションを提供する Xcode プラグインです。クリック一つで、GitHub の履歴、Blame、プルリクエスト、イシュー、通知などに簡単にアクセスできます。

![plugin](https://cloud.githubusercontent.com/assets/5022872/10867703/96e980be-80ab-11e5-9aaa-a06ef476b7f7.gif)

私の会社では GitHub を使用しています。頻繁に GitHub を開きます。時には、Xcode で編集中にコードの意味がわからないことがありますので、GitHub にアクセスして Blame を確認します。時には、特定のファイルの最新コミットを確認して、コードがどのように進化したかを理解するために使用します。そのため、Xcode から GitHub を迅速に開くツールがあればと思い、このプラグインを作成しました。Xcode でソースファイルを編集中には、現在の GitHub リポジトリとファイルを知ることができます。したがって、GitHub 上のファイルに迅速にジャンプすることができ、現在編集中の行の Blame を迅速に行い、Xcode で作業中の現在のリポジトリのイシューや PR に迅速にジャンプすることができます。

## メニュー項目

<img width="700" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864813/5df3f05e-8034-11e5-9f3e-03ae3fbc3cfc.png">

6つのメニュー項目を持っています：

 メニュータイトル     | ショートカット              | GitHub URL パターン（LZAlbumManager.m のライン 40 を編集中）
----------------|-----------------------|----------------------------------
 設定             |⌃⇧⌘S |
 リポジトリ         |⌃⇧⌘R | https://github.com/lzwjava/LZAlbum
 イシュー         |⌃⇧⌘I | https://github.com/lzwjava/LZAlbum/issues
 PRs             |⌃⇧⌘P | https://github.com/lzwjava/LZAlbum/pulls
 クイックファイル     |⌃⇧⌘Q | https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 履歴リスト       |⌃⇧⌘L | https://github.com/lzwjava/LZAlbum/commits/fd7224/LZAlbum/manager/LZAlbumManager.m
 Blame          |⌃⇧⌘B | https://github.com/lzwjava/LZAlbum/blame/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 通知           |⌃⇧⌘N | https://github.com/leancloud/LZAlbum/notifications?all=1

 ショートカットは慎重に設計されています。Xcode のデフォルトショートカットと競合しません。ショートカットのパターンは ⌃⇧⌘ (Ctrl+Shift+Command) です。

## カスタマイズ

時には、迅速に Wiki にジャンプしたい場合があります。その方法は、設定を開くことです：

<img width="500" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864939/fa83f286-8037-11e5-97d7-e9549485b11d.png">

例えば、

クイックファイルのパターンと実際の URL：

```
           {git_remote_url}       /blob/{commit}/          {file_path}         #{selection}
https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40-L43
```

{commit} は現在のブランチの最新コミットハッシュです。ブランチを使用するよりも良いです。ブランチの HEAD が変更される可能性があるためです。したがって、#L40-L43 のコードも変更される可能性があります。

したがって、現在のリポジトリの Wiki をショートカットに追加する場合は、メニュー項目を追加し、パターンを `{git_remote_url}/wiki` に設定してください。

設定で、`Clear Default Repos` は、複数の Git リモートがある場合に、最初にトリガーされたときに、どれを選択するかを尋ねます：

<img width="400" src="https://cloud.githubusercontent.com/assets/5022872/10865120/5794994a-803c-11e5-9527-965f7e617e8f.png">

次回、メニューをトリガーすると、そのリモートリポジトリがデフォルトとして開きます。ボタン `Clear Default Repos` をクリックすると、この設定がクリアされ、再度選択するように求められます。

## インストール

[Alcatraz](http://alcatraz.io/) を使用してインストールすることをお勧めします、

![qq20151101-1 2x](https://cloud.githubusercontent.com/assets/5022872/10867743/0ce351c6-80ae-11e5-82e2-f740887153f7.jpg)

または

1. このリポジトリをクローンします。
2. `Reveal-In-GitHub.xcodeproj` を開き、ビルドします。
3. `Reveal-In-GitHub.xcplugin` は `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins` に配置されます。
4. Xcode を再起動します。
5. 任意の GitHub プロジェクトを開き、⌃⇧⌘B (Ctrl+Shift+Command+B) を押してコードの Blame を確認します。

## インストール

[Alcatraz](http://alcatraz.io/) を使用することをお勧めします。[巧神のブログ](http://blog.devtang.com/blog/2014/03/05/use-alcatraz-to-manage-xcode-plugins/)を参照してください。インストール後、上の画像のように `Reveal In GitHub` を検索し、`Install` をクリックしてください。

このツールを使用しない場合は、次の手順に従ってください：

* このプロジェクトをローカルにクローンします。
* xcodeproj を開き、Build をクリックしてビルドします。これにより、ディレクトリ `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins` に Reveal-In-GitHub.xcplugin ファイルが生成されます。
* Xcode を再起動し、任意の GitHub にあるプロジェクトを開きます。`Ctrl+Shift+Command+B` を押してコードの Blame を確認します。

## クレジット

開発中に、似たような機能を持つ他のプラグイン [ShowInGitHub](https://github.com/larsxschneider/ShowInGitHub) を発見しました。その技術をいくつか学びました。感謝します。

## ライセンス

MIT