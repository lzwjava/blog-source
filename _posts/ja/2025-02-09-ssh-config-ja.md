---
audio: true
lang: ja
layout: post
title: SSH設定
translated: true
---

この `ssh-config` ファイルは、SSH クライアントの動作を設定します。各部分を分解してみましょう：

-   `Host * !192.*.*.*`: このセクションは、`192.*.*.*` パターンに一致するホストを除くすべてのホストに適用されます（通常、ローカルネットワークアドレス）。
    -   `ProxyCommand corkscrew localhost 7890 %h %p`: これが鍵です。SSH に `corkscrew` プログラムを使用してターゲットホストに接続するように指示します。
        -   `corkscrew`: HTTP または HTTPS プロキシを通じて SSH 接続をトンネルするためのツールです。
        -   `localhost 7890`: プロキシサーバーのアドレス (`localhost`) とポート (`7890`) を指定します。これにより、ローカルマシン上でポート 7890 でリッスンしているプロキシサーバー（例：Shadowsocks、SOCKS プロキシ、または他のトンネリングソリューション）があると仮定します。
        -   `%h`: 特殊な SSH 変数で、接続しようとしているターゲットホスト名に展開されます。
        -   `%p`: 別の SSH 変数で、ターゲットポート（通常は SSH の 22）に展開されます。
    - 要約すると、この `Host` ブロックは、ローカルネットワークへの接続を除くすべての接続に対して、SSH が `corkscrew` プロキシを使用するように設定します。

-   `Host *`: このセクションは、すべてのホストに適用されます。
    -   `UseKeychain yes`: macOS の場合、SSH にキーチェーンから SSH キーを保存および取得するように指示します。これにより、毎回パスワードを入力する必要がありません。
    -   `AddKeysToAgent yes`: これにより、SSH キーが自動的に SSH エージェントに追加され、リブートのたびに手動で追加する必要がありません。
    -   `IdentityFile ~/.ssh/id_rsa`: この設定は、プライベート SSH キーファイルのパスを指定します。`~/.ssh/id_rsa` は、RSA プライベートキーのデフォルトの場所です。

**要するに、この設定は、ローカルネットワーク以外のすべての SSH 接続に対してプロキシを設定し、キー管理を便利にします。**

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host * !192.*.*.* !47.*.*.*
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```