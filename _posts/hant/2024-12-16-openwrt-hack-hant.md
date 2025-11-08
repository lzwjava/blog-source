---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 增強OpenWRT與OpenClash及Shadowsocks的整合
translated: true
type: post
---

### 更新套件列表

```bash
root@OpenWrt:~# opkg update
正在下載 https://downloads.openwrt.org/releases/22.03.3/targets/ramips/mt7621/packages/Packages.gz
已更新可用套件列表於 /var/opkg-lists/openwrt_core
正在下載 https://downloads.openwrt.org/releases/22.03.3/targets/ramips/mt7621/packages/Packages.sig
簽名檢查通過。
正在下載 https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/base/Packages.gz
已更新可用套件列表於 /var/opkg-lists/openwrt_base
正在下載 https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/base/Packages.sig
簽名檢查通過。
正在下載 https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/Packages.gz
已更新可用套件列表於 /var/opkg-lists/openwrt_luci
正在下載 https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/Packages.sig
簽名檢查通過。
root@OpenWrt:~#
```

### 安裝 Shadowsocks 插件

要安裝 `luci-app-shadowsocks-libev` 插件：

```bash
root@OpenWrt:~# opkg install luci-app-shadowsocks-libev
正在安裝 luci-app-shadowsocks-libev (git-22.066.30464-cea4277) 到 root...
正在下載 https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/luci-app-shadowsocks-libev_git-22.066.30464-cea4277_all.ipk
正在配置 luci-app-shadowsocks-libev。
```

### OpenClash 安裝

請參考 OpenClash 的 [GitHub 倉庫](https://github.com/vernesong/OpenClash?tab=readme-ov-file) 以獲取更多詳細資訊。以下是安裝必要組件的步驟。

1. 安裝 OpenSSH SFTP 伺服器：

   ```bash
   opkg install openssh-sftp-server
   ```

2. 使用 `scp` 將 OpenClash 套件複製到路由器：

   ```bash
   scp luci-app-openclash_0.46.050-beta_all.ipk root@192.168.1.1:~/
   ```

### OpenClash 配置範例

以下是 OpenClash 的配置範例：

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

proxies:
  - name: "我的 SS 代理"
    type: ss
    server: 209.97.0.0
    port: 57500
    cipher: chacha20-ietf-poly1305
    password: "jHLE54zNC000000"
    udp: true
    plugin: ""
    plugin-opts: {}

proxy-groups:
  - name: "代理"
    type: select
    proxies:
      - "我的 SS 代理"

rules:
  - GEOIP,CN,DIRECT
  - MATCH,代理
```

通過這些步驟，您可以增強您的 OpenWRT 設備以支援高級網絡配置和代理功能。請始終參考官方文檔以獲取更新和最佳實踐。