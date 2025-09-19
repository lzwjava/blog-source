---
audio: false
generated: false
image: false
lang: ja
layout: post
title: 'プロキシツール: SquidとDanted'
translated: true
---

## Danted

コマンドラインの指示:

```bash
sudo apt-get install dante-server
sudo apt install net-tools
ifconfig
danted
tail -f danted.log
```

`/etc/danted.conf` の設定:

```bash
logoutput: /home/lzwjava/danted.log

internal: 0.0.0.0 port = 1080  # すべてのインターフェースでリッスン
external: ens4
# 認証 (クレデンシャルなしで全てを許可)
method: none

# ルール
client pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    method: none  # 明示的に認証なしを許可
}

socks pass {  # 非推奨の "pass" の代わりに "socks pass" を使用
    from: 0.0.0.0/0 to: 0.0.0.0/0
    protocol: tcp udp
    method: none  # 認証なしの場合に必要
}
```

## Squid の設定

```bash
acl all src all
http_access allow all
http_access deny all
http_port 1128
```

試行に失敗しました。まず `squid.conf` をクリーンアップする必要があります。

```
1737725543.236   1822 14.31.165.22 TCP_TUNNEL/200 1232 CONNECT 91.108.56.121:443 - HIER_DIRECT/91.108.56.121 -
```

## Google Cloud コマンドライン

```bash
gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS

gcloud compute ssh --zone "asia-east1-a" "i25" --project "graphite-ally-445108-k3"
```