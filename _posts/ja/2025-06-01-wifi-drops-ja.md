---
audio: false
generated: true
lang: ja
layout: post
title: UbuntuのWi-Fi切断問題を解決する
translated: true
type: note
---

Ubuntuで有線接続は安定しているのにWi-Fiが切断される問題は、いくつかの要因によって発生する可能性があります。問題を診断して修正するためのステップバイステップガイドをご紹介します：

---

### **1. ドライバーの問題を確認する**
あなたのMSI B760M Mortar WiFiマザーボードは、おそらく**Intel Wi-Fi 6E AX211/AX210**カードを使用しています。Intelのドライバーは一般的にLinuxでよくサポートされていますが、問題が発生することもあります。

#### **手順:**
- **Wi-Fiチップセットを特定する:**  
  ターミナルで実行:  
  ```bash
  lspci -knn | grep -iA3 net
  ```
  Wi-Fiアダプター（おそらく`Intel Corporation Device [8086:...]`）を探してください。

- **正しいドライバーが読み込まれているか確認:**  
  ```bash
  lsmod | grep iwlwifi
  ```
  何も表示されない場合、ドライバーが読み込まれていません。

- **ドライバーのインストール/更新:**  
  Intel Wi-Fiドライバー（`iwlwifi`）はLinuxカーネルに含まれていますが、ファームウェアの更新が必要な場合があります:
  ```bash
  sudo apt update && sudo apt install --reinstall linux-firmware
  ```

---

### **2. Wi-Fiの省電力機能を無効にする**
Linuxは時としてWi-Fiカードを積極的に省電力状態にし、切断を引き起こすことがあります。

#### **手順:**
- 省電力機能を一時的に無効化:  
  ```bash
  sudo sed -i 's/wifi.powersave = 3/wifi.powersave = 2/' /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
  ```
  または手動で確認:
  ```bash
  iw dev wlan0 get power_save
  ```
  （`wlan0`は`ip a`で確認したインターフェース名に置き換えてください。）

- **変更を適用:**  
  ```bash
  sudo systemctl restart NetworkManager
  ```

---

### **3. 干渉やルーターの問題を確認する**
- **別のデバイス**（スマートフォン/ノートPC）で問題が再現するかテストしてください。
- **Wi-Fiチャンネルを変更**（混雑したチャンネルをスキャンするには`iwlist`を使用）:
  ```bash
  sudo iwlist wlan0 scan | grep Frequency
  ```
- 干渉が少ない**5GHz帯**を試してください（利用可能な場合）。

---

### **4. IPv6を無効にする**
一部のルーター/ISPではIPv6の互換性に問題があります。

#### **手順:**
- `/etc/sysctl.conf`を編集して以下を追加:
  ```plaintext
  net.ipv6.conf.all.disable_ipv6=1
  net.ipv6.conf.default.disable_ipv6=1
  ```
- 適用:
  ```bash
  sudo sysctl -p
  ```

---

### **5. カーネルとNetworkManagerを更新する**
新しいカーネルはWi-Fi問題を修正することがよくあります。
```bash
sudo apt update && sudo apt upgrade
```
必要に応じて、**メインラインカーネル**（例：6.5+）をインストール:
```bash
sudo apt install linux-image-generic-hwe-22.04
```

---

### **6. ハードウェア暗号化を無効にする（該当する場合）**
一部のIntel Wi-Fiカードはハードウェア暗号化に問題があります。  
`/etc/modprobe.d/iwlwifi.conf`を編集（存在しない場合は作成）:
```plaintext
options iwlwifi 11n_disable=1
```
その後:
```bash
sudo modprobe -r iwlwifi && sudo modprobe iwlwifi
```

---

### **7. RFKillやブロックされたWi-Fiを確認する**
```bash
rfkill list
```
Wi-Fiがブロックされている場合（例：`soft blocked: yes`）、ブロックを解除:
```bash
sudo rfkill unblock wifi
```

---

### **8. USB Wi-Fiアダプターでテストする**
問題が解決しない場合、**Linux互換のUSB Wi-Fiアダプター**（例：TP-Link Archer T4U）を試して、問題がIntelカードにあるかどうかを切り分けてください。

---

### **9. エラーのログを確認する**
```bash
journalctl -u NetworkManager --no-pager -n 50
```
`iwlwifi`のエラーや切断イベントを探してください。

---

### **最終的な注意点**
- 上記のいずれも機能しない場合、**Windowsとのデュアルブート**を検討して問題がハードウェア関連かどうかを確認してください。
- あるいは、Wi-Fiが不安定なままの場合、**USB-to-Ethernetアダプター**を使用してください。

さらにデバッグが必要な場合はお知らせください！