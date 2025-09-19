---
audio: false
generated: false
image: false
lang: ja
layout: post
title: OpenClashとShadowsocksでOpenWRTを強化する
translated: true
---

### パッケージリストの更新

```bash
root@OpenWrt:~# opkg update
https://downloads.openwrt.org/releases/22.03.3/targets/ramips/mt7621/packages/Packages.gz をダウンロード中
/var/opkg-lists/openwrt_core で利用可能なパッケージのリストを更新しました
https://downloads.openwrt.org/releases/22.03.3/targets/ramips/mt7621/packages/Packages.sig をダウンロード中
署名チェックに合格しました。
https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/base/Packages.gz をダウンロード中
/var/opkg-lists/openwrt_base で利用可能なパッケージのリストを更新しました
https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/base/Packages.sig をダウンロード中
署名チェックに合格しました。
https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/Packages.gz をダウンロード中
/var/opkg-lists/openwrt_luci で利用可能なパッケージのリストを更新しました
https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/Packages.sig をダウンロード中
署名チェックに合格しました。
root@OpenWrt:~#
```

### Shadowsocksプラグインのインストール

`luci-app-shadowsocks-libev` プラグインをインストールするには:

```bash
root@OpenWrt:~# opkg install luci-app-shadowsocks-libev
luci-app-shadowsocks-libev (git-22.066.30464-cea4277) を root にインストール中...
https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/luci-app-shadowsocks-libev_git-22.066.30464-cea4277_all.ipk をダウンロード中
luci-app-shadowsocks-libev を設定中。
```

### OpenClashのインストール

詳細については、OpenClashの[GitHubリポジトリ](https://github.com/vernesong/OpenClash?tab=readme-ov-file)を参照してください。以下に必要なコンポーネントをインストールする手順を示します。

1. OpenSSH SFTPサーバーをインストールする:

```bash
opkg install openssh-sftp-server
```

2. `scp`を使用してOpenClashパッケージをルーターにコピーします:

```bash
scp luci-app-openclash_0.46.050-beta_all.ipk root@192.168.1.1:~/
```

このコマンドは、`luci-app-openclash_0.46.050-beta_all.ipk` というファイルを、ローカルマシンからIPアドレスが `192.168.1.1` のリモートサーバーの `root` ユーザーのホームディレクトリ (`~/`) にコピーします。`scp` は、Secure Copy Protocol を使用してファイルを安全に転送するためのコマンドです。

### OpenClashの設定例

```yaml
# OpenClashの設定ファイル例

# プロキシ設定
proxies:
  - name: "Proxy1"
    type: ss
    server: "example.com"
    port: 8388
    password: "password"
    cipher: "aes-256-cfb"

  - name: "Proxy2"
    type: vmess
    server: "example.net"
    port: 443
    uuid: "your-uuid"
    alterId: 64
    cipher: "auto"
    tls: true

# ルール設定
rules:
  - DOMAIN-SUFFIX,google.com,Proxy1
  - DOMAIN-SUFFIX,youtube.com,Proxy2
  - IP-CIDR,192.168.1.0/24,DIRECT
  - GEOIP,CN,DIRECT
  - MATCH,Proxy1

# DNS設定
dns:
  enable: true
  listen: 0.0.0.0:53
  enhanced-mode: redir-host
  nameserver:
    - 8.8.8.8
    - 8.8.4.4
  fallback:
    - 1.1.1.1
    - 1.0.0.1

# その他の設定
log-level: info
external-controller: 127.0.0.1:9090
secret: "your-secret"
```

この設定例では、OpenClashの基本的な設定を紹介しています。プロキシ、ルール、DNSなどの設定が含まれています。必要に応じて、これらの設定を変更して使用してください。

以下はOpenClashの設定例です：

```yaml
port: 7890
socks-port: 7891
mixed-port: 7892
allow-lan: true
mode: Rule
log-level: info
external-controller: 0.0.0.0:9090
experimental:
  ignore-resolve-fail: true
```

```yaml
dns:
  enable: true
  # ipv6: false
  listen: 0.0.0.0:53
  fake-ip-range: 198.18.0.1/16
  default-nameserver:
    - 119.29.29.29
    - 223.5.5.5
    #- 223.6.6.6
  nameserver:
    - https://223.5.5.5/dns-query
    - https://1.12.12.12/dns-query
    #- https://doh.pub/dns-query
    #- https://dns.alidns.com/dns-query
  fake-ip-filter:
    - "*.lan"
    - "*.localdomain"
    - "*.example"
    - "*.invalid"
    - "*.localhost"
    - "*.test"
    - "*.local"
```

```yaml
proxies:
  - name: "My SS Proxy"
    type: ss
    server: 209.97.0.0
    port: 57500
    cipher: chacha20-ietf-poly1305
    password: "jHLE54zNC000000"
    udp: true
    plugin: ""
    plugin-opts: {}
```

```yaml
proxy-groups:
  - name: "プロキシ"
    type: select
    proxies:
      - "My SS Proxy"
```

```yaml
rules:
  - GEOIP,CN,DIRECT
  - MATCH,Proxy
```

これらの手順に従うことで、OpenWRTデバイスを強化し、高度なネットワーク設定やプロキシ機能をサポートできるようになります。最新の情報やベストプラクティスについては、公式ドキュメントを常に参照してください。