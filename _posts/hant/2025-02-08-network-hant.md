---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 雲端 IP、網絡介面與 WiFi 優化
translated: true
---

### 目錄

1. [Hetzner Cloud 中的浮動 IP](#floating-ips-in-hetzner-cloud)
   - IP 配置命令
   - Netplan 配置設定
   - 網絡配置檔案

2. [網絡介面管理](#network-interface-management)
   - 刪除 TUN 介面
   - 介面狀態監控
   - 網絡故障排除

3. [區域網路 IP 掃描器](#lan-ip-scanner)
   - Python 網絡掃描腳本
   - 多線程主機發現
   - 端口掃描功能
   - 本地網絡設備識別

4. [繞過本地 IP](#bypassing-local-ips)
   - 本地網絡代理配置
   - 子網掩碼計算
   - 網絡範圍規劃

5. [使用 IPv6 地址進行 SSH 連接](#ssh-connection-using-ipv6-address)
   - IPv6 SSH 配置
   - SSH 配置檔案管理
   - 不同地址類型的代理命令設定
   - 效能優化

6. [提升 WiFi 速度](#improving-wifi-speed)
   - 舊款與新款調制解調器效能比較
   - 網絡設定配置
   - 有線與無線橋接模式
   - 網絡瓶頸故障排除

7. [OpenWrt 重置](#openwrt-reset)
   - 網頁介面重置方法
   - 命令列重置程序
   - 恢復出廠預設設定

---

## Hetzner Cloud 中的浮動 IP

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

## 網絡介面管理

刪除 `tun` 介面。

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

##區域網路 IP 掃描器

此 Python 腳本用於掃描本地網絡中的活躍 IP 地址。它使用 `ping` 命令檢查主機是否可達，並採用多線程加速掃描過程。信號量限制並發線程數量，以避免系統過載。腳本接受網絡地址（例如「192.168.1.0/24」）作為輸入，並列印網絡中每個 IP 地址的狀態（啟用或關閉）。

此腳本有助於識別網絡中的設備，例如以有線橋接模式運作的 TP-LINK 網狀路由器，透過掃描活躍 IP 地址實現。

```python
import subprocess
import ipaddress
import threading
import os
import socket
import argparse

MAX_THREADS = 50  # 最大線程數量

def is_host_up(host, port=None):
    """
    使用 ping 或 telnet 檢查主機是否啟用。
    若指定端口，則使用 telnet 檢查該端口是否開啟。
    否則使用 ping。
    如果主機啟用則返回 True，否則返回 False。
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
            # -c 1: 只發送 1 個封包
            # -W 1: 等待 1 秒響應
            subprocess.check_output(["ping", "-c", "1", "-W", "1", host], timeout=1)
            return True
        except subprocess.CalledProcessError:
            return False
        except subprocess.TimeoutExpired:
            return False

def scan_ip(ip_str, up_ips, port=None):
    """
    掃描單個 IP 地址並列印其狀態。
    """
    if is_host_up(ip_str, port):
        print(f"{ip_str} 已啟用")
        up_ips.append(ip_str)
    else:
        print(f"{ip_str} 未啟用")

def scan_network(network, port=None):
    """
    使用線程掃描網絡中的活躍主機，並限制並發線程數量。
    """
    print(f"正在掃描網絡：{network}")
    threads = []
    semaphore = threading.Semaphore(MAX_THREADS)  # 限制並發線程數量
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
    parser = argparse.ArgumentParser(description="掃描網絡中的活躍主機。")
    parser.add_argument("network", nargs='?', default="192.168.1.0/24", help="要掃描的網絡（例如：192.168.1.0/24）")
    parser.add_argument("-p", "--port", type=int, help="要檢查的端口（可選）")
    args = parser.parse_args()

    network_to_scan = args.network
    port_to_scan = args.port

    up_ips = scan_network(network_to_scan, port_to_scan)
    print("\n活躍的 IP：")
    for ip in up_ips:
        print(ip)
```

---

## 繞過本地 IP

此腳本識別活躍 IP 地址。為確保網絡通訊正常，請驗證代理設定是否配置為繞過這些本地 IP。

```bash
192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,127.0.0.1,localhost,*.local,timestamp.apple.com,sequoia.apple.com,seed-sequoia.siri.apple.com, 192.168.1.0/16
```

---

## 子網掩碼

我的第二台機器通常位於 192.168.1.16。

因此，以下命令有效：

```bash
python scripts/ip_scan.py 192.168.1.0/27 -p 22
```

因為 32 - 27 = 5，2^5 = 32，所以它會嘗試從 `192.168.1.0` 到 `192.168.1.31`。

但使用 `192.168.1.0/28` 時則無效，因為 2^4 = 16，所以它只會嘗試從 `192.168.1.0` 到 `192.168.1.15`，不包含 `192.168.1.16`。

---

## 使用 IPv6 地址進行 SSH 連接

我嘗試使用 IPv6 地址連接到 Hetzner Cloud 中的機器。`ssh 2a01:4f8:c17:2000::/64` 無效，但 `ssh root@2a01:4f8:c17:2000::1` 有效。

該 IPv6 地址從 Hetzner Cloud 控制台複製而來。

`~/.ssh/config` 檔案可配置為對 IPv4 和 IPv6 地址應用不同的代理規則。此設定允許為 IPv4 地址指定代理命令，而對 IPv6 地址採用不同的處理方式。

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

執行 `ssh root@192.168.1.3` 時，以下輸出顯示 SSH 客戶端從 `~/.ssh/config` 檔案應用配置選項：

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

SSH 連接速度明顯較慢，因此我恢復為以下較簡單的配置：

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

使用 `ProxyCommand corkscrew localhost 7890 %h %p` 指令時，若涉及 IPv6 地址，則可能無法正確處理。

上述配置仍不生效，但以下配置可行：

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

## 提升 WiFi 速度

### 舊款調制解調器問題

在父母家中，調制解調器相當陳舊，可能已有 10 年歷史。初始網絡設定如下：

調制解調器 -> 3 米無線 -> TP-Link AX3000（無線橋接模式） -> 2 米、一面牆、無線 -> 筆記本電腦

此設定下載速度較低，Speedtest 結果僅 10 Mbps。

改進後的設定採用有線連接：

調制解調器 -> 2 米網線 -> TP-Link AX3000（有線橋接模式） -> 4 米無線、一面牆 -> 筆記本電腦

下載速度提升至 90 Mbps。

### 新款調制解調器效能

在我的住所，調制解調器是新款，TP-Link 路由器在無線橋接模式下效能良好。網絡設定如下：

調制解調器 -> 4 米無線 -> TP-Link AX3000（無線橋接模式） -> 2 米無線 -> 筆記本電腦

網絡品質優良。

### 故障排除建議

提升 WiFi 速度並無萬能解決方案。建議使用網線逐段測試網絡，以識別瓶頸。比較有線連接與 WiFi 的速度，並嘗試直接以網線連接設備，檢查效能是否改善。

---

## OpenWrt 重置

### 透過網頁介面重置

建議使用以太網線連接路由器。重置後，WiFi SSID 將恢復為預設設定，可能與預期不同。

### 透過命令列（SSH）重置

可透過命令列介面（SSH）將 OpenWrt 重置為預設設定。步驟如下：

1. 透過 SSH 連接到 OpenWrt 路由器。
2. 執行以下命令：

```bash
root@OpenWrt:~# firstboot
This will erase all settings and remove any installed packages. Are you sure? [N/y]
y
/dev/ubi0_1 is mounted as /overlay, only erasing files
root@OpenWrt:~# reboot
```

3. 路由器將以預設設定重新啟動。

**命令說明：**

- `firstboot`：啟動重置流程，清除所有配置及已安裝套件。
- `reboot`：重啟路由器，應用重置。