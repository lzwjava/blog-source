---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GPG暗号化の受信者についての解説
translated: true
type: note
---

### GPGコマンドと「Recipient」プロンプトの理解

実行しているコマンドは、GnuPG（GPG）を使用してファイル（`inputfile.txt`）を暗号化するためのものです：

```
gpg --homedir /path/to/custom/dir -e -r recipient@example.com --encrypt inputfile.txt
```

- `--homedir /path/to/custom/dir`: GPGのキーリングと設定にカスタムディレクトリを使用します（デフォルトの `~/.gnupg` の代わり）。
- `-e`（または `--encrypt`）: GPGにファイルを暗号化するように指示します。
- `-r recipient@example.com`: **受信者**（暗号化の*対象*となる人物またはエンティティ）を指定します。これは、受信者の公開鍵からのメールアドレス、名前、または鍵IDである必要があります。
- `--encrypt inputfile.txt`: 暗号化するファイル（出力は `inputfile.txt.gpg` になります）。

#### ここでの「Recipient」とはどういう意味ですか？
GPG暗号化では：
- **受信者**とは、ファイルを*受け取り、復号化する*人物です。あなたは*受信者の公開鍵*を使用してファイルを暗号化するため、受信者（とその秘密鍵）だけが復号化できます。
- これは「送信者」（あなた）ではありません。なぜなら、暗号化は*受信者のために*データを保護するからです。送信者としてのあなたの役割は、（署名を追加するために `-s` を使用する場合の）署名に関連するものであり、ここでは純粋な暗号化です。

これは「送信」のための安全なデータであるという認識は正しいですが、用語は受信者に焦点を当てています。なぜなら、それが誰の鍵がそれを保護するかに関係するからです。誰か他の人の南京錠で箱をロックするようなものと考えてください—彼らだけがそれを開けることができます。

#### エラー「You did not specify a user ID. (you may use '-r')」とプロンプトが表示される理由
この対話型プロンプトは、以下の理由で発生します：
1.  GPGがあなたのキーリング（カスタムhomedir内）で `recipient@example.com` に一致する公開鍵を見つけられなかった。
2.  `-r` フラグは提供されているが、有効な鍵に解決されないため、GPGは手動でユーザーIDを入力するよう求めるプロンプトにフォールバックします。

プロンプトは以下の通りです：
```
Current recipients:
Enter the user ID.  End with an empty line:
```

- **ユーザーID**とは、受信者の完全な識別子を意味します。例えば、`John Doe <recipient@example.com>` や、その鍵のフィンガープリント/ID（例: `ABCDEF123456`）です。
- 必要に応じて行ごとに（例: 名前、メール、コメント）入力し、終了するにはEnterを2回（空行）押します。

#### 修正方法
1.  **まず受信者の公開鍵をインポートする**（最も一般的な問題）:
    - 受信者に公開鍵（`gpg --export -a their@email.com` でエクスポートされたもの）を送信するよう依頼してください。
    - それをインポートします: `gpg --homedir /path/to/custom/dir --import their-public-key.asc`。
    - その後、コマンドを再実行してください。

2.  **鍵がすでにインポートされているが一致しない場合**:
    - 鍵をリスト表示します: `gpg --homedir /path/to/custom/dir --list-keys`。
    - そこから正確なユーザーIDを `-r` で使用します（例: `-r "John Doe <recipient@example.com>"`）。

3.  **プロンプトで**（クイックワークアラウンドとして）:
    - 完全なユーザーIDを入力します。例：
      ```
      John Doe
      recipient@example.com
      
      ```
      （空行で終了します。）

#### 「Sender」ではなく「Recipient」である理由
- 暗号化は*非対称*です：公開鍵（誰でも暗号化可能）→ 秘密鍵（所有者のみが復号化可能）。
- 送信者（あなた）は受信者の**公開**鍵で暗号化します。
- あなたが送信者であることを証明したい場合は、署名を追加します： `gpg ... -e -r recipient@example.com -s --encrypt inputfile.txt`（*あなたの*秘密鍵を使用して署名します）。
- 「Recipient」は標準的なGPGの用語です—誰が送信するかではなく、誰が受信/復号化するかが問題です。これを「sender」と呼ぶと、送信者は暗号化には鍵を必要としない（署名には必要）ため、混乱を招きます。

これで解決しない場合は、`--list-keys` の出力（センシティブな情報は編集してください）を共有していただければ、デバッグをお手伝いします！

#### 参考文献
- [GPG Encryption Basics](https://www.gnupg.org/documentation/manuals/gnupg/Encrypting-and-Decrypting.html)
- [GPG Man Page](https://www.gnupg.org/documentation/manuals/gnupg/gpg.html)