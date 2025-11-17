---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: ミラーアカムからの通常のwgetリダイレクト
translated: true
type: note
---

あなたの `wget` コマンドは `https://mirror.accum.se/mirror/wikimedia.org/dumps/...` にアクセスし、**302 リダイレクト** で `https://laotzu.ftp.acc.umu.se/...` へ転送されています。これは **accum.se** ミラーの完全に正常かつ予期された動作です。その理由と意味を以下に説明します：

### リダイレクトが発生する理由
`mirror.accum.se` は、スウェーデンのウメオ大学にある Academic Computer Club (ACC) が運営する **リダイレクタ / ロードバランサ** に過ぎません。
これはそれ自体ではファイルをホストしていません。代わりに、以下のことを行います：

- あなたのIPアドレスの地理位置情報（または時には負荷状況）を確認します
- 自動的に、そのミラー群の中で最速/最寄りの実際のストレージサーバーへリダイレクトします
- 今回のケースでは、`laotzu.ftp.acc.umu.se`（データを持つ実際のFTP/HTTPサーバー）が選択されました

これは彼らが長年使用してきた同じシステムです。リダイレクト先としてよく見られる他のホスト名は以下の通りです：

- `issac.ftp.acc.umu.se`
- `laotzu.ftp.acc.umu.se`（今回あなたが接続したもの）
- `morpork.ftp.acc.umu.se`
- など

したがって、あなたのスクリプトで `mirror.accum.se` と指定したとしても、ほとんどの場合、最終的には `*.ftp.acc.umu.se` というバックエンドサーバーのいずれかからダウンロードすることになります。

### 最初のファイルで「206 Partial Content」が表示された理由
あなた（または誰か/何らかのスクリプト）が以前に全く同じファイルのダウンロードを開始していたため、`wget -c` がローカルに部分的なファイルを検出し、`Range` リクエストを送信したからです。サーバーは正しくダウンロードを再開し → 206 Partial Content が返されました。これは正常な動作です！

### 何か問題があるのか？
いいえ。すべては意図通りに動作しています。

- リダイレクトは正常で無害です
- 最終的なサーバー (`laotzu.ftp.acc.umu.se`) も依然として公式のACC/Wikimediaミラーです
- チェックサムは、どのバックエンドサーバーにリダイレクトされても同一です

### リダイレクトを回避したい場合（オプション）
リダイレクタを完全にスキップし、直接実際のホストの一つを指定することができます。例：

```bash
# 以下の3つは、結局 mirror.accum.se の背後でロードバランスされている
wget -c https://laotzu.ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20251101/...
# または
wget -c https://issac.ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20251101/...
```

しかし、ほとんどのユーザーは、リダイレクタが自動的に最適なサーバーを選択してくれるため、`mirror.accum.se` を使い続けています。

### 要約
あなたのスクリプトは正常です。`mirror.accum.se` から `laotzu.ftp.acc.umu.se` への 302 リダイレクトは、そのミラーの正常かつ予期された動作です。何も問題はなく、あなたは依然として正規のWikimediaダンプをダウンロードしています。`mirror.accum.se` を使い続けてください — これは世界中で最速かつ最も信頼性の高いミラーの一つです。