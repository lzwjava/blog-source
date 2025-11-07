---
audio: false
generated: false
image: false
lang: ja
layout: post
title: Netplan、Systemd、SSH、Condaクリーンアップ
translated: true
type: post
---

### 目次

1. [Netplanを試す](#trying-netplan)
   - 静的IPアドレスの設定によりSSH接続が失われた
   - 物理的なアクセスによる復元が必要
   - システムのDNSリゾルバファイルを変更

2. [Systemdサービス](#systemd-service)
   - ローカルLLM推論のためのサービス設定
   - LLMモデル用ウェブインターフェースの設定
   - ルールベースのプロキシツールサービスを確立
   - サービス管理に`systemctl`コマンドを使用

3. [SSH設定](#ssh-configuration)
   - `corkscrew`経由での外部接続のプロキシ
   - ローカルネットワークをプロキシから除外
   - `keychain`と`agent`によるSSHキーの管理
   - デフォルトの秘密鍵の場所を指定

4. [LinuxでCondaを削除する](#delete-conda-in-linux)
   - Condaのインストールディレクトリ全体を削除
   - `.bashrc`からConda初期化コードを削除
   - `PATH`環境変数を更新
   - システムパスからCondaのバイナリを削除


## Netplanを試す

Ubuntuマシンに静的IPアドレスを割り当てるために、以下の構成を試しました。このサーバーではOpenWebUIとllama.cppを実行しています。

```
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.128/32
      gateway4: 192.168.1.1
```

`sudo netplan apply`を実行した後、マシンには`ssh lzw@192.168.1.128`経由でアクセスできなくなりました。

キーボードとマウスを使ってマシンにログインし、ファイルを削除して設定を元に戻しました。

`/etc/resolv.conf`が変更されました。

---

## Systemdサービス

*2025.02.13*

## LLaMAサーバーサービスの設定

このセクションでは、ローカルLLM推論機能を提供するLLaMAサーバーを実行するためのsystemdサービスを設定する方法について説明します。

```bash
sudo emacs /etc/systemd/system/llama.service
sudo systemctl daemon-reload
sudo systemctl enable llama.service
journalctl -u llama.service
```

```bash
[Unit]
Description=Llama Script

[Service]
ExecStart=/home/lzw/Projects/llama.cpp/build/bin/llama-server -m /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-Distill-Qwen-14B-Q5_K_M.gguf --port 8000  --ctx-size 2048 --batch-size 512 --n-gpu-layers 49 --threads 8 --parallel 1
WorkingDirectory=/home/lzw/Projects/llama.cpp
StandardOutput=append:/home/lzw/llama.log
StandardError=append:/home/lzw/llama.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

## Open WebUIサービスの設定

このセクションでは、LLMモデルと対話するためのウェブインターフェースを提供するOpen WebUIを実行するためのsystemdサービスを設定する方法について説明します。

```bash
[Unit]
Description=Open Web UI Service

[Service]
ExecStart=/home/lzw/.local/bin/open-webui serve
WorkingDirectory=/home/lzw
StandardOutput=append:/home/lzw/open-webui.log
StandardError=append:/home/lzw/open-webui.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

```bash
sudo systemctl enable openwebui.service
sudo systemctl daemon-reload
sudo systemctl start  openwebui.service
```

## Clashサービスの設定

このセクションでは、ルールベースのプロキシツールであるClashを実行するためのsystemdサービスを設定する方法について説明します。

```bash
[Unit]
Description=Clash Service

[Service]
ExecStart=/home/lzw/clash-linux-386-v1.17.0/clash-linux-386
WorkingDirectory=/home/lzw/clash-linux-386-v1.17.0
StandardOutput=append:/home/lzw/clash.log
StandardError=append:/home/lzw/clash.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

```bash
# サービスファイルの作成
sudo emacs /etc/systemd/system/clash.service 

# systemdデーモンのリロード
sudo systemctl daemon-reload

# サービスの有効化と開始
sudo systemctl enable clash.service
sudo systemctl start clash.service
sudo systemctl restart clash.service

# ステータスの確認
sudo systemctl status clash.service
```

---

## SSH設定

*2025.02.09*

この`ssh-config`ファイルは、SSHクライアントの動作を設定します。各部分を詳しく見ていきましょう。

-   `Host * !192.*.*.*`: このセクションは、`192.*.*.*`パターン（通常、ローカルネットワークアドレス）に一致するホストを*除く*すべてのホストに適用されます。
    -   `ProxyCommand corkscrew localhost 7890 %h %p`: これが重要な部分です。SSHに`corkscrew`プログラムを使用してターゲットホストに接続するように指示します。
        -   `corkscrew`: HTTPまたはHTTPSプロキシ経由でSSH接続をトンネルできるツールです。
        -   `localhost 7890`: プロキシサーバーのアドレス（`localhost`）とポート（`7890`）を指定します。これは、ローカルマシン上でポート7890でリッスンしているプロキシサーバー（例：Shadowsocks、SOCKSプロキシ、または別のトンネリングソリューション）が実行されていることを前提としています。
        -   `%h`: 接続しようとしているターゲットホスト名に展開される特殊なSSH変数です。
        -   `%p`: ターゲットポート（SSHの場合は通常22）に展開される別のSSH変数です。
    -   要するに、この`Host`ブロックは、ローカルネットワークへの接続を除くすべての接続に対してSSHが`corkscrew`プロキシを使用するように設定します。

-   `Host *`: このセクションは*すべて*のホストに適用されます。
    -   `UseKeychain yes`: macOSでは、SSHにSSHキーをKeychainに保存および取得するように指示するため、毎回パスワードを入力する必要がありません。
    -   `AddKeysToAgent yes`: これにより、SSHキーがSSHエージェントに自動的に追加されるため、再起動後に手動で追加する必要がありません。
    -   `IdentityFile ~/.ssh/id_rsa`: プライベートSSHキーファイルのパスを指定します。`~/.ssh/id_rsa`はRSAプライベートキーのデフォルトの場所です。

**要するに、この設定は、ローカルネットワーク上の接続を除くすべてのSSH接続に対してプロキシを設定し、利便性のためにキー管理を設定します。**

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

---

## LinuxでCondaを削除する

*2025.02.07*

```bash
rm -rf ~/anaconda3
```

`.bashrc`の以下のコードを削除してください：

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/lzw/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/lzw/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/lzw/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/lzw/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

パスを以下から：

```bash
export PATH="/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/anaconda3/bin:/home/lzw/anaconda3/condabin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"
```

以下に更新：

```bash
export PATH="/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"
```