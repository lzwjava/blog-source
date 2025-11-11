---
audio: false
generated: true
lang: ja
layout: post
title: Ubuntuでイーサネットリンク速度を確認する
translated: true
type: note
---

Ubuntuでは、いくつかのコマンドラインツールを使用してイーサネットリンク速度を確認できます。以下に最も一般的な方法を紹介します。

### **1. `ethtool`の使用（推奨）**
`ethtool`は、イーサネットインターフェースの現在のリンク速度を確認する最も信頼性の高い方法です。

#### `ethtool`のインストール（未インストールの場合）:
```bash
sudo apt install ethtool
```

#### リンク速度の確認:
```bash
sudo ethtool <interface_name>
```
`<interface_name>`をイーサネットインターフェース名に置き換えてください（例: `eth0`, `enp3s0`, `ens33`）。

#### 例:
```bash
sudo ethtool enp3s0
```
出力内の`Speed`と`Duplex`フィールドを確認:
```
Settings for enp3s0:
    Supported ports: [ TP ]
    Supported link modes:   10baseT/Half 10baseT/Full 
                            100baseT/Half 100baseT/Full 
                            1000baseT/Full 
    Supported pause frame use: No
    Supports auto-negotiation: Yes
    Supported FEC modes: Not reported
    Advertised link modes:  10baseT/Half 10baseT/Full 
                            100baseT/Half 100baseT/Full 
                            1000baseT/Full 
    Advertised pause frame use: No
    Advertised auto-negotiation: Yes
    Advertised FEC modes: Not reported
    Speed: 1000Mb/s   # <--- 現在のリンク速度
    Duplex: Full      # <--- 全二重または半二重
    Port: Twisted Pair
    PHYAD: 1
    Transceiver: internal
    Auto-negotiation: on
    MDI-X: on (auto)
    Supports Wake-on: pumbg
    Wake-on: d
    Current message level: 0x00000007 (7)
                           drv probe link
    Link detected: yes      # <--- ケーブル接続状態
```

---

### **2. `ip`または`ifconfig`の使用（基本情報）**
これらのコマンドはインターフェースが起動しているかどうかを表示しますが、リンク速度は直接表示しません。

#### `ip`の使用:
```bash
ip link show <interface_name>
```
例:
```bash
ip link show enp3s0
```
（速度は表示されず、リンク状態のみ）

#### `ifconfig`の使用（非推奨だが利用可能）:
```bash
ifconfig <interface_name>
```
例:
```bash
ifconfig enp3s0
```
（インターフェースの起動状態は表示するが速度は非表示）

---

### **3. `dmesg`の使用（ドライバログの確認）**
イーサネットドライバが初期化時にネゴシエートされた速度をログに記録している場合があります。
```bash
dmesg | grep <interface_name>
```
例:
```bash
dmesg | grep enp3s0
```
以下のような行を探してください:
```
[    5.123456] e1000e: enp3s0 NIC Link is Up 1000 Mbps Full Duplex
```

---

### **4. `mii-tool`の使用（旧式システム）**
非常に古いシステムでは、`mii-tool`が動作する場合があります:
```bash
sudo apt install net-tools
sudo mii-tool -v <interface_name>
```
例:
```bash
sudo mii-tool -v eth0
```
（現代のギガビットイーサネットには非推奨）

---

### **まとめ**
- **最適な方法:** `sudo ethtool <interface>`（速度、二重通信、自動ネゴシエーションを表示）
- **代替方法:** `ethtool`が利用できない場合は`dmesg`ログを確認
- **基本状態確認:** `ip link show`または`ifconfig`（速度は表示しない）

ご不明な点がございましたら、お知らせください！🚀