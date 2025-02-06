---
audio: true
lang: hant
layout: post
title: 內網 IP 掃描器
translated: true
---

## LAN IP 掃描器

這段 Python 腳本掃描本機網絡以尋找活躍的 IP 位址。它使用 `ping` 命令檢查主機是否可達，並使用多線程來加快掃描速度。 訊號量限制同時運行的線程數量，以避免壓垮系統。 腳本接收網絡地址（例如，「192.168.1.0/24」）作為輸入，並列印網絡中每個 IP 位址的狀態（啟用或停用）。

此腳本有助於識別網絡上的設備，例如以線橋模式運作的 TP-LINK 網狀路由器，方法是掃描活躍的 IP 位址。


```python
import subprocess
import ipaddress
import threading
import os

MAX_THREADS = 50  # 最大線程數

def is_host_up(host):
    """
    使用 ping 檢查主機是否啟用。
    如果主機已啟用，則返回 True，否則返回 False。
    """
    try:
        # -c 1: 只發送 1 個封包
        # -W 1: 等待 1 秒以獲取回應
        subprocess.check_output(["ping", "-c", "1", "-W", "1", host], timeout=1)
        return True
    except subprocess.CalledProcessError:
        return False
    except subprocess.TimeoutExpired:
        return False

def scan_ip(ip_str):
    """
    掃描單個 IP 位址並列印其狀態。
    """
    if is_host_up(ip_str):
        print(f"{ip_str} is up")
    else:
        print(f"{ip_str} is down")

def scan_network(network):
    """
    使用線程掃描網絡以尋找活躍的主機，限制同時運行的線程數。
    """
    print(f"Scanning network: {network}")
    threads = []
    semaphore = threading.Semaphore(MAX_THREADS)  # 限制同時運行的線程數

    def scan_ip_with_semaphore(ip_str):
        semaphore.acquire()
        try:
            scan_ip(ip_str)
        finally:
            semaphore.release()

    for ip in ipaddress.IPv4Network(network):
        ip_str = str(ip)
        thread = threading.Thread(target=scan_ip_with_semaphore, args=(ip_str,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    network_to_scan = "192.168.1.0/24"  # 將此更改為您的網絡
    scan_network(network_to_scan)

```

## 跳過本地 IP

此腳本識別活躍的 IP 位址。 為確保正確的網絡通訊，請驗證是否已將代理設置配置為跳過這些本地 IP。

```bash
192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,127.0.0.1,localhost,*.local,timestamp.apple.com,sequoia.apple.com,seed-sequoia.siri.apple.com, 192.168.1.0/16
```
