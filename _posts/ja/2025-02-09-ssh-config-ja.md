---
audio: true
lang: ja
layout: post
title: SSH設定
translated: true
---

この`ssh-config`ファイルはSSHクライアントの動作を設定します。各部分を分解してみましょう。

- `Host * !192.*.*.*`: このセクションは、`192.*.*.*`パターン（通常はローカルネットワークアドレス）に一致するホストを除くすべてのホストに適用されます。
    - `ProxyCommand corkscrew localhost 7890 %h %p`: これが重要な部分です。SSHに`corkscrew`プログラムを使用してターゲットホストに接続するように指示します。
        - `corkscrew`: HTTPまたはHTTPSプロキシを介してSSH接続をトンネリングできるツールです。
        - `localhost 7890`: プロキシサーバーのアドレス（`localhost`）とポート（`7890`）を指定します。これは、ローカルマシンでポート7890（例：Shadowsocks、SOCKSプロキシ、またはその他のトンネリングソリューション）をリッスンしているプロキシサーバーが実行されていることを前提としています。
        - `%h`: ターゲットホスト名に展開される特別なSSH変数です。
        - `%p`: ターゲットポート（通常はSSHの22）に展開される別のSSH変数です。
    - 要約すると、この`Host`ブロックは、ローカルネットワークへの接続を除くすべての接続に対して`corkscrew`プロキシを使用するようにSSHを設定します。

- `Host *`: このセクションはすべてのホストに適用されます。
    - `UseKeychain yes`: macOSでは、SSHキーをキーチェーンに保存および取得するようにSSHに指示するため、毎回パスワードを入力する必要がありません。
    - `AddKeysToAgent yes`: これは、SSHキーをSSHエージェントに自動的に追加するため、再起動後に手動で追加する必要がありません。
    - `IdentityFile ~/.ssh/id_rsa`: プライベートSSHキーファイルへのパスを指定します。`~/.ssh/id_rsa`はRSAプライベートキーのデフォルトの場所です。

**要するに、この設定は、ローカルネットワーク上の接続を除くすべてのSSH接続に対してプロキシを設定し、利便性のためにキー管理を設定します。**


```bash
Host * !192.*.*.*
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```
