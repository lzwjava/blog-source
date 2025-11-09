---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 自動WiFi接続テストスクリプト
translated: true
type: note
---

```python
import subprocess
import time
import os

def get_wifi_interfaces():
    """WiFiインターフェースを検索するヘルパー関数"""
    try:
        result = subprocess.run("nmcli dev status | grep wifi | awk '{print $1}'", shell=True, capture_output=True, text=True)
        interfaces = [iface.strip() for iface in result.stdout.split('\n') if iface.strip()]
        return interfaces
    except:
        return []

def test_wifi_connection(ssid, password="88888888", timeout=30):
    """WiFi接続を非対話的にテストする。タプル(成功: bool, エラー: str)を返す"""
    interfaces = get_wifi_interfaces()
    if not interfaces:
        return False, "利用可能なWiFiインターフェースがありません"
    interface = interfaces[0]  # 最初の利用可能なインターフェースを使用
    con_name = f"test-{ssid}"  # テストプロファイルの一意な名前
    
    # コマンド
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
        # 既存のプロファイルを削除（存在しない場合のエラーは無視）
        subprocess.run(delete_cmd, shell=True, capture_output=True, timeout=5)
        time.sleep(1)
        
        # 埋め込みパスワードで新しいプロファイルを作成（非対話的）
        add_result = subprocess.run(add_cmd, shell=True, capture_output=True, text=True, timeout=10)
        if add_result.returncode != 0:
            error = add_result.stderr.strip() or add_result.stdout.strip() or "接続プロファイルの作成に失敗しました"
            return False, f"プロファイル作成エラー: {error}"
        
        # プロファイルをアクティブ化（非対話的）
        up_result = subprocess.run(up_cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        if up_result.returncode != 0:
            error = up_result.stderr.strip() or up_result.stdout.strip() or "アクティベーションに失敗しました"
            if "secrets were required" in error.lower():
                error = "パスワードが間違っているか認証に失敗しました"
            elif "activation failed" in error.lower():
                error = f"接続アクティベーション失敗: {error}"
            return False, f"nmcliエラー: {error}"
        
        # 安定化のために待機
        time.sleep(2)
        
        # pingでインターネット接続をテスト
        ping_test = subprocess.run("ping -c 1 -W 3 8.8.8.8", shell=True, capture_output=True, text=True, timeout=5)
        if ping_test.returncode == 0:
            return True, None
        else:
            error = ping_test.stderr.strip() or "pingが失敗しました"
            return False, f"接続済みですがインターネットに接続できません: {error}"
        
    except subprocess.TimeoutExpired:
        return False, f"{timeout}秒後に操作がタイムアウトしました"
    except subprocess.SubprocessError as e:
        return False, f"コマンドエラー: {str(e)}"
    finally:
        # クリーンアップ: 接続をダウンしプロファイルを削除
        try:
            subprocess.run(f"nmcli connection down '{con_name}'", shell=True, capture_output=True, timeout=5)
            subprocess.run(delete_cmd, shell=True, capture_output=True, timeout=5)
            subprocess.run(disconnect_cmd, shell=True, capture_output=True, timeout=5)
        except subprocess.SubprocessError:
            pass  # クリーンアップの問題は無視
```