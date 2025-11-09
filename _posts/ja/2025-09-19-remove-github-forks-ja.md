---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: 不要なGitHubフォークの削除
translated: true
type: note
---

了解しました。簡潔に言うと、他人のフォークを直接削除することはできません。しかし、(a) 本人に依頼する、(b) 機密情報を削除し今後の漏洩を防ぐ、(c) 正当な理由がある場合はGitHubの正式な手順（DMCAまたはサポート）を利用する、という方法があります。以下は、個人ブログに適した、表を使わないクリーンなプランです。

### 1) まず、フォークした人に連絡する（最速の方法）

その人のフォークでIssueを開くか、メールを送信します。以下のテンプレートをコピーして使えます：

> Hi @tornadobaflocer — このフォークには私の個人用ノートとアクティビティ履歴が含まれています。このリポジトリを公開したのは `lzwjava.github.io` ドメインを使用するためであり、再配布を目的としたものではありません。このフォークを削除してください。私はソースを非公開にし、公開されるのはビルド済みのサイトアセットのみとします。
> ご理解いただきありがとうございます。

相手が削除してくれれば完了です。そうでない場合は、続行します。

### 2) GitHubが対応する内容としない内容を理解する

* **公開**リポジトリを削除または非公開にしても、既存の公開フォークは**削除されません**。公開フォークは公開されたまま残り、独自の「ネットワーク」に分離します。([Stack Overflow][1])
* フォークを削除できるのは、そのフォークの**管理者**のみです（今回のケースではあなたは管理者ではありません）。([Stack Overflow][2])

### 3) フォークがあなたの著作権で保護されたコンテンツを許可なく複製している場合

GitHubにDMCA削除通知を提出できます。これはフォーク全体にわたって権利侵害コンテンツを削除するための正式な手順です。ポリシーと「提出方法」ガイドを読み、含める必要のある情報を確認してください。([GitHub Docs][3])

ヒント: リポジトリに**ライセンスがなかった**場合、デフォルトの著作権が適用され、削除依頼が通りやすくなります（再利用する権利が誰にもなかったことになります）。寛容なライセンスがあった場合でもDMCAは有効ですが、より複雑になります。

### 4) 将来のフォークによるソースコードの公開を防ぐ

**ドメイン**は公開したまま、**ソースコード**は非公開に保つために、リポジトリを分割します：

* **非公開のソースリポジトリ** (例: `blog-source`): Jekyll/Hugoのコンテンツ、下書き、ノート、設定ファイル。
* **`lzwjava.github.io`** という名前の**公開デプロイリポジトリ**: **ビルドされたサイトファイルのみ** (HTML/CSS/JS) を含む。下書きや履歴は含まない。

GitHub Pagesサイトは、リポジトリが非公開でも公開されます（Enterprise CloudでプライベートPagesを使用する場合を除く）。個人ブログの場合、この2つのリポジトリによる「デプロイのみ」の構成が安全なパターンです。([GitHub Docs][4])

今日利用できるデプロイオプション：

* ジェネレーターの `public/` または `docs/` 出力を `lzwjava.github.io` にプッシュする。([Quarto][5])
* または、`blog-source` 内でGitHub Actionsワークフローを使用し、出力をビルドして `lzwjava.github.io` リポジトリのデフォルトブランチに強制プッシュする。（ドキュメント: 「ブランチから公開」または「Actionsで公開」フローを選択。）([GitHub Docs][6])

### 5) 履歴から機密情報を削除する（自身のリポジトリと残存するコピー全て）

* 公開されたトークン/キーは全てローテーションする（侵害されたと想定する）。
* `git filter-repo`（GitHubが現在推奨）またはBFG（一般的なケースではより高速）を使用して、機密ファイル/パスを履歴から削除する。その後、強制プッシュする。([GitHub Docs][7])

これだけでは他の人のフォークを修正しませんが、あなたの正規リポジトリをクリーンにし、コンテンツが削除されたことを示すことで削除依頼をサポートします。

### 6) オプションの強化

* 明確なLICENSEを追加する（再利用を明示的に制限したい場合）。
* READMEに免責事項を追加する：「このリポジトリはビルド済みサイトの出力のみを目的としています。ソースをフォーク**しないでください**。ソースは非公開です。」
* **Organization**でホストする場合は、Organization全体およびリポジトリごとにプライベートリポジトリのフォークを無効にできる（公開コードのクローンは防げないが、プライベートリポジトリには有効）。([GitHub Docs][8])

---

## 具体的な次のステップ（効果的な順序）

1.  @tornadobaflocer にフォークの削除を依頼する（上記のメッセージを使用）。
2.  すぐにあなたのソースを新しい**非公開**リポジトリ (`blog-source`) に移動する。
3.  `lzwjava.github.io` を、ビルドされたファイルのみを含む**公開のデプロイ専用**リポジトリにする。Pagesがそのブランチ/フォルダから公開するように設定する。([GitHub Docs][6])
4.  古い公開リポジトリの履歴を書き換えて機密部分を削除し、その後アーカイブまたは削除する。([GitHub Docs][7])
5.  相手が拒否し、削除を希望する場合は、GitHubに**DMCA削除通知**を提出する。([GitHub Docs][9])

必要であれば、GitHubが要求する正確な形式でのDMCA通知の草案と、`blog-source` からサイトをビルドし、ビルドされたファイルのみを `lzwjava.github.io` にプッシュする最小限のGitHub Actionsワークフローを作成できます。

[1]: https://stackoverflow.com/questions/53052745/what-happens-to-the-forks-when-deleting-the-original-repository?utm_source=chatgpt.com "フォークは元のリポジトリを削除するとどうなりますか？"
[2]: https://stackoverflow.com/questions/50280412/github-delete-a-fork-that-was-created-from-my-repo?utm_source=chatgpt.com "Github - 自分のリポジトリから作成されたフォークを削除する"
[3]: https://docs.github.com/articles/dmca-takedown-policy?utm_source=chatgpt.com "DMCA削除ポリシー"
[4]: https://docs.github.com/articles/creating-project-pages-manually?utm_source=chatgpt.com "GitHub Pagesサイトの作成"
[5]: https://quarto.org/docs/publishing/github-pages.html?utm_source=chatgpt.com "GitHub Pages"
[6]: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site?utm_source=chatgpt.com "GitHub Pagesサイトの公開元の設定"
[7]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository?utm_source=chatgpt.com "リポジトリから機密データを削除する"
[8]: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-forking-policy-for-your-repository?utm_source=chatgpt.com "リポジトリのフォークポリシーの管理"
[9]: https://docs.github.com/en/site-policy/content-removal-policies/guide-to-submitting-a-dmca-takedown-notice?utm_source=chatgpt.com "DMCA削除通知提出ガイド"