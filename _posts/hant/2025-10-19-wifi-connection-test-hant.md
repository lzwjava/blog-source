---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 自動化WiFi連接測試腳本
translated: true
type: note
---

```python
import subprocess
import time
import os

def get_wifi_interfaces():
    """輔助函數用於尋找WiFi介面。"""
    try:
        result = subprocess.run("nmcli dev status | grep wifi | awk '{print $1}'", shell=True, capture_output=True, text=True)
        interfaces = [iface.strip() for iface in result.stdout.split('\n') if iface.strip()]
        return interfaces
    except:
        return []

def test_wifi_connection(ssid, password="88888888", timeout=30):
    """非互動式測試WiFi連接。返回元組(success: bool, error: str)。"""
    interfaces = get_wifi_interfaces()
    if not interfaces:
        return False, "沒有可用的WiFi介面"
    interface = interfaces[0]  # 使用第一個可用介面
    con_name = f"test-{ssid}"  # 測試配置檔的唯一名稱
    
    # 指令
    delete_cmd = f"nmcli connection delete '{con_name}'"
    add_cmd = (
        f"nmcli connection add type wifi con-name '{con_name}' "
        f"ifname {interface} ssid '{ssid}' "
        f"wifi-sec.key-mgmt wpa-psk wifi-sec.psk '{password}' "
        f"-- autoconnect no"
    )
    up_cmd = f"nmcli connection up '{con_name}'"
    disconnect_cmd = f"nmcli device disconnect {interface}"
    
    try:
        # 刪除任何現有配置檔（如果不存在則忽略錯誤）
        subprocess.run(delete_cmd, shell=True, capture_output=True, timeout=5)
        time.sleep(1)
        
        # 創建帶有嵌入式密碼的新配置檔（非互動式）
        add_result = subprocess.run(add_cmd, shell=True, capture_output=True, text=True, timeout=10)
        if add_result.returncode != 0:
            error = add_result.stderr.strip() or add_result.stdout.strip() or "創建連接配置檔失敗"
            return False, f"配置檔創建錯誤: {error}"
        
        # 啟動配置檔（非互動式）
        up_result = subprocess.run(up_cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        if up_result.returncode != 0:
            error = up_result.stderr.strip() or up_result.stdout.strip() or "啟動失敗"
            if "secrets were required" in error.lower():
                error = "密碼錯誤或認證失敗"
            elif "activation failed" in error.lower():
                error = f"連接啟動失敗: {error}"
            return False, f"nmcli錯誤: {error}"
        
        # 等待穩定
        time.sleep(2)
        
        # 使用ping測試互聯網連接
        ping_test = subprocess.run("ping -c 1 -W 3 8.8.8.8", shell=True, capture_output=True, text=True, timeout=5)
        if ping_test.returncode == 0:
            return True, None
        else:
            error = ping_test.stderr.strip() or "Ping失敗"
            return False, f"已連接但無法訪問互聯網: {error}"
        
    except subprocess.TimeoutExpired:
        return False, f"操作在{timeout}秒後超時"
    except subprocess.SubprocessError as e:
        return False, f"指令錯誤: {str(e)}"
    finally:
        # 清理：關閉連接並刪除配置檔
        try:
            subprocess.run(f"nmcli connection down '{con_name}'", shell=True, capture_output=True, timeout=5)
            subprocess.run(delete_cmd, shell=True, capture_output=True, timeout=5)
            subprocess.run(disconnect_cmd, shell=True, capture_output=True, timeout=5)
        except subprocess.SubprocessError:
            pass  # 忽略清理問題
```