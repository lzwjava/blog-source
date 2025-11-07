---
audio: false
generated: false
image: false
lang: ja
layout: post
title: クラウドIP、ネットワークインターフェースおよびWiFi最適化
translated: true
type: post
---

```markdown
### 目次

1. [Hetzner CloudでのFloating IP](#floating-ips-in-hetzner-cloud)
   - IP設定コマンド
   - Netplan設定
   - ネットワーク設定ファイル

2. [ネットワークインターフェース管理](#network-interface-management)
   - TUNインターフェースの削除
   - インターフェースステータスの監視
   - ネットワークトラブルシューティング

3. [LAN IPスキャナー](#lan-ip-scanner)
   - Pythonネットワークスキャンスクリプト
   - マルチスレッドホスト検出
   - ポートスキャン機能
   - ローカルネットワークでのデバイス識別

4. [ローカルIPのバイパス](#bypassing-local-ips)
   - ローカルネットワーク用プロキシ設定
   - サブネットマスクの計算
   - ネットワーク範囲の計画

5. [IPv6アドレスを使用したSSH接続](#ssh-connection-using-ipv6-address)
   - IPv6 SSH設定
   - SSH設定ファイルの管理
   - 異なるアドレスタイプ用のプロキシコマンド設定
   - パフォーマンス最適化

6. [WiFi速度の改善](#improving-wifi-speed)
   - 古いモデムと新しいモデムのパフォーマンス比較
   - ネットワーク設定
   - 有線と無線ブリッジモード
   - ネットワークボトルネックのトラブルシューティング

7. [OpenWrtのリセット](#openwrt-reset)
   - Webインターフェースを使用したリセット方法
   - コマンドラインによるリセット手順
   - 工場出荷時設定への復元

---

## Hetzner CloudでのFloating IP

### IP

```bash
sudo ip addr add 78.47.144.0 dev eth0
```

### Netplan

```bash
touch /etc/netplan/60-floating-ip.yaml
nano /etc/netplan/60-floating-ip.yaml
```

```yaml
network:
   version: 2
   renderer: networkd
   ethernets:
     eth0:
       addresses:
       - 78.47.144.0/32
```

```bash
sudo netplan apply
```

---

## ネットワークインターフェース管理

`tun`インターフェースを削除します。

```bash
$ ipconfig

outline-tun0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1500
        inet 10.0.85.1  netmask 255.255.255.255  destination 10.0.85.1
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 500  (UNSPEC)
        RX packets 208  bytes 8712 (8.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 385  bytes 23322 (23.3 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

$ sudo ip link delete outline-tun0
```

---

## LAN IPスキャナー

このPythonスクリプトは、ローカルネットワーク内でアクティブなIPアドレスをスキャンします。ホストが到達可能かどうかを確認するために`ping`コマンドを使用し、マルチスレッディングを活用してスキャンプロセスを高速化します。セマフォを使用して同時実行スレッド数を制限し、システムへの過負荷を防ぎます。このスクリプトはネットワークアドレス（例: "192.168.1.0/24"）を入力として受け取り、各IPアドレスがアップかダウンかを表示します。

このスクリプトは、有線ブリッジモードで動作するTP-LINKメッシュルーターなど、ネットワーク上のデバイスを識別するのに役立ちます。

```python
import subprocess
import ipaddress
import threading
import os
import socket
import argparse

MAX_THREADS = 50  # 使用する最大スレッド数

def is_host_up(host, port=None):
    """
    pingまたはtelnetを使用してホストがアップしているか確認します。
    ポートが指定されている場合は、そのポートが開いているかを確認します。
    そうでない場合はpingを使用します。
    ホストがアップしている場合はTrue、それ以外はFalseを返します。
    """
    if port:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                return True
            else:
                return False
        except socket.error as e:
            return False
        finally:
            sock.close()
    else:
        try:
            # -c 1: パケットを1つだけ送信
            # -W 1: 応答を1秒待つ
            subprocess.check_output(["ping", "-c", "1", "-W", "1", host], timeout=1)
            return True
        except subprocess.CalledProcessError:
            return False
        except subprocess.TimeoutExpired:
            return False

def scan_ip(ip_str, up_ips, port=None):
    """
    単一のIPアドレスをスキャンし、ステータスを表示します。
    """
    if is_host_up(ip_str, port):
        print(f"{ip_str} is up")
        up_ips.append(ip_str)
    else:
        print(f"{ip_str} is down")

def scan_network(network, port=None):
    """
    スレッドを使用してネットワーク内のアクティブホストをスキャンし、同時実行スレッド数を制限します。
    """
    print(f"Scanning network: {network}")
    threads = []
    semaphore = threading.Semaphore(MAX_THREADS)  # 同時実行スレッド数を制限
    up_ips = []

    def scan_ip_with_semaphore(ip_str):
        semaphore.acquire()
        try:
            scan_ip(ip_str, up_ips, port)
        finally:
            semaphore.release()

    for ip in ipaddress.IPv4Network(network):
        ip_str = str(ip)
        thread = threading.Thread(target=scan_ip_with_semaphore, args=(ip_str,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return up_ips

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ネットワーク内のアクティブホストをスキャンします。")
    parser.add_argument("network", nargs='?', default="192.168.1.0/24", help="スキャンするネットワーク（例: 192.168.1.0/24）")
    parser.add_argument("-p", "--port", type=int, help="確認するポート（オプション）")
    args = parser.parse_args()

    network_to_scan = args.network
    port_to_scan = args.port

    up_ips = scan_network(network_to_scan, port_to_scan)
    print("\nアクティブなIP:")
    for ip in up_ips:
        print(ip)
```

---

## ローカルIPのバイパス

このスクリプトはアクティブなIPアドレスを識別します。適切なネットワーク通信を確保するために、プロキシ設定がこれらのローカルIPをバイパスするように構成されていることを確認してください。

```bash
192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,127.0.0.1,localhost,*.local,timestamp.apple.com,sequoia.apple.com,seed-sequoia.siri.apple.com, 192.168.1.0/16
```

---

## サブネットマスク

2台目のマシンは通常192.168.1.16にあります。

そのため、以下のコマンドで動作します。

```bash
python scripts/ip_scan.py 192.168.1.0/27 -p 22
```

32 - 27 = 5、2^5 = 32なので、`192.168.1.0`から`192.168.1.31`までを試します。

しかし、`192.168.1.0/28`では動作しません。なぜなら、2^4 = 16なので、`192.168.1.0`から`192.168.1.15`までしか試さず、`192.168.1.16`を含まないためです。

---

## IPv6アドレスを使用したSSH接続

Hetzner CloudのマシンにIPv6で接続しようとしています。`ssh 2a01:4f8:c17:2000::/64`は動作しませんが、`ssh root@2a01:4f8:c17:2000::1`は動作します。

IPv6アドレスはHetzner Cloudコンソールからコピーしました。

`~/.ssh/config`ファイルを設定して、IPv4とIPv6のアドレスに対して異なるプロキシルールを適用できます。この設定では、IPv4アドレスに対してプロキシコマンドを指定し、IPv6アドレスを別の方法で処理できます。

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host *.*.*.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```

`ssh root@192.168.1.3`を実行すると、SSHクライアントが`~/.ssh/config`ファイルから設定オプションを適用していることがわかります。

```bash
debug1: Reading configuration data /Users/lzwjava/.ssh/config
debug1: /Users/lzwjava/.ssh/config line 1: Applying options for 192.168.1.*
debug1: /Users/lzwjava/.ssh/config line 5: Applying options for *.*.*.*
debug2: add_identity_file: ignoring duplicate key ~/.ssh/id_rsa
debug1: /Users/lzwjava/.ssh/config line 10: Applying options for *
debug2: add_identity_file: ignoring duplicate key ~/.ssh/id_rsa
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 21: include /etc/ssh/ssh_config.d/* matched no files
debug1: /etc/ssh/ssh_config line 54: Applying options for *
debug2: resolve_canonicalize: hostname 192.168.1.3 is address
debug3: expanded UserKnownHostsFile '~/.ssh/known_hosts' -> '/Users/lzwjava/.ssh/known_hosts'
debug3: expanded UserKnownHostsFile '~/.ssh/known_hosts2' -> '/Users/lzwjava/.ssh/known_hosts2'
debug1: Authenticator provider $SSH_SK_PROVIDER did not resolve; disabling
debug3: channel_clear_timeouts: clearing
debug1: Executing proxy command: exec corkscrew localhost 7890 192.168.1.3 22
```

SSH接続速度が遅くなったため、以下の簡単な設定に戻しました。

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
```

`ProxyCommand corkscrew localhost 7890 %h %p`ディレクティブをIPv6アドレスで使用すると問題が発生します。このプロキシコマンドはIPv6アドレスを正しく処理できない可能性があります。

上記の設定はまだ動作しません。しかし、以下の設定は問題ありません。

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host !192.*.*.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```

---

## WiFi速度の改善

### 古いモデムの問題

実家のモデムはかなり古く、10年以上経っています。初期のネットワーク設定は以下の通りでした。

モデム -> 3m 無線 -> TP-Link AX3000（無線ブリッジモード） -> 2m、壁、無線 -> ラップトップ

これにより、ダウンロード速度はSpeedtestで10 Mbpsしか出ませんでした。

改善された設定では、有線接続を使用しました。

モデム -> 2m ケーブル -> TP-Link AX3000（有線ブリッジモード） -> 4m 無線、壁 -> ラップトップ

これにより、ダウンロード速度は最大90 Mbpsまで向上しました。

### 新しいモデムのパフォーマンス

自宅のモデムは新しく、TP-Linkルーターは無線ブリッジモードで良好に動作します。ネットワーク設定は以下の通りです。

モデム -> 4m 無線 -> TP-Link AX3000（無線ブリッジモード） -> 2m 無線 -> ラップトップ

ネットワーク品質は良好です。

### トラブルシューティングのヒント

Wi-Fi速度を改善するための単一の解決策はありません。ネットワークの各部分をテストしてボトルネックを特定するために、ケーブルを使用するのが良い方法です。有線接続とWi-Fiを使用した場合の速度を比較してください。また、デバイスを直接ケーブルで接続してパフォーマンスが向上するか確認してください。

---

## OpenWrtのリセット

### Webインターフェースを使用したリセット

イーサネットケーブルを使用してルーターに接続することをお勧めします。リセット後、Wi-Fi SSIDはデフォルト設定に戻ります。

### コマンドライン（SSH）を使用したリセット

コマンドラインインターフェース（SSH）を使用してOpenWrtをデフォルト設定にリセットできます。以下が手順です。

1. SSHでOpenWrtルーターに接続します。
2. 以下のコマンドを実行します。

    ```bash
    root@OpenWrt:~# firstboot
    This will erase all settings and remove any installed packages. Are you sure? [N/y]
    y
    /dev/ubi0_1 is mounted as /overlay, only erasing files
    root@OpenWrt:~# reboot
    ```
3. ルーターがデフォルト設定で再起動します。

**コマンドの説明:**

* `firstboot`: このコマンドはリセットプロセスを開始し、すべての設定とインストールされたパッケージを削除します。
* `reboot`: このコマンドはルーターを再起動し、リセットを適用します。
```