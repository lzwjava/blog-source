---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 精通 Red Hat Enterprise Linux 基礎
translated: true
type: note
---

## Red Hat Linux 簡介
Red Hat Enterprise Linux (RHEL) 是由 Red Hat, Inc. 開發的領先開源作業系統。專為企業環境設計，提供穩定性、安全性及對關鍵任務應用程式的強大支援。RHEL 廣泛應用於伺服器、雲端環境及企業 IT 基礎架構。

### 歷史沿革
- **1994年**：Red Hat Linux 首次以商業 Linux 發行版形式發布
- **2002年**：Red Hat 推出專注於企業級可靠性的 Red Hat Enterprise Linux
- **2025年**：RHEL 9 為最新主要版本，RHEL 10 正在開發中，提供增強安全性與容器支援等進階功能

### 主要特性
- **穩定性**：RHEL 優先提供長期支援 (LTS)，每個主要版本具備 10 年生命週期
- **安全性**：具備 SELinux (安全增強型 Linux)、firewalld 及定期安全更新等功能
- **效能**：針對高效能運算、虛擬化及雲端部署進行優化
- **訂閱模式**：透過 Red Hat 訂閱提供更新、支援及認證軟體存取權限
- **生態系統**：與 Red Hat OpenShift、Ansible 及其他 DevOps 和自動化工具整合

## 安裝指南
### 系統需求
- **最低需求**：
  - 1.5 GB 記憶體
  - 20 GB 磁碟空間
  - 1 GHz 處理器
- **建議規格**：
  - 4 GB 或以上記憶體
  - 40 GB 以上磁碟空間
  - 多核心處理器

### 安裝步驟
1. **下載 RHEL**：
   - 從 [Red Hat 客戶入口網站](https://access.redhat.com) 取得 RHEL ISO 映像檔（需訂閱或開發者帳戶）
   - 或使用免費開發者訂閱供非生產環境使用
2. **建立可開機媒體**：
   - 使用 `dd` 或 Rufus 等工具建立可開機 USB 隨身碟
   - 指令範例：`sudo dd if=rhel-9.3-x86_64.iso of=/dev/sdX bs=4M status=progress`
3. **開機與安裝**：
   - 從 USB 或 DVD 開機
   - 遵循 Anaconda 安裝程式指引：
     - 選擇語言與地區
     - 設定磁碟分割（手動或自動）
     - 配置網路設定
     - 設定 root 密碼與使用者帳戶
4. **系統註冊**：
   - 安裝完成後，透過 Red Hat Subscription Manager 註冊：`subscription-manager register --username <username> --password <password>`
   - 附加訂閱：`subscription-manager attach --auto`

## 系統管理
### 套件管理
RHEL 使用 **DNF** (Dandified YUM) 進行套件管理
- 安裝套件：`sudo dnf install <package-name>`
- 更新系統：`sudo dnf update`
- 搜尋套件：`sudo dnf search <keyword>`
- 啟用儲存庫：`sudo subscription-manager repos --enable <repo-id>`

### 使用者管理
- 新增使用者：`sudo useradd -m <username>`
- 設定密碼：`sudo passwd <username>`
- 修改使用者：`sudo usermod -aG <group> <username>`
- 刪除使用者：`sudo userdel -r <username>`

### 檔案系統管理
- 檢查磁碟使用量：`df -h`
- 列出已掛載檔案系統：`lsblk`
- 管理分割區：使用 `fdisk` 或 `parted` 進行磁碟分割
- 設定 LVM (邏輯卷冊管理)：
  - 建立實體卷冊：`pvcreate /dev/sdX`
  - 建立卷冊群組：`vgcreate <vg-name> /dev/sdX`
  - 建立邏輯卷冊：`lvcreate -L <size> -n <lv-name> <vg-name>`

### 網路設定
- 使用 `nmcli` 配置網路：
  - 列出連線：`nmcli connection show`
  - 設定靜態 IP：`nmcli con mod <connection-name> ipv4.addresses 192.168.1.100/24 ipv4.gateway 192.168.1.1 ipv4.method manual`
  - 啟用連線：`nmcli con up <connection-name>`
- 使用 `firewalld` 管理防火牆：
  - 開啟通訊埠：`sudo firewall-cmd --add-port=80/tcp --permanent`
  - 重新載入防火牆：`sudo firewall-cmd --reload`

### 安全性設定
- **SELinux**：
  - 檢查狀態：`sestatus`
  - 設定模式 (強制/寬容)：`sudo setenforce 0` (寬容) 或 `sudo setenforce 1` (強制)
  - 修改政策：使用 `semanage` 與 `audit2allow` 建立自訂政策
- **更新管理**：
  - 安裝安全更新：`sudo dnf update --security`
- **SSH 安全**：
  - 強化 SSH：編輯 `/etc/ssh/sshd_config` 停用 root 登入 (`PermitRootLogin no`) 並變更預設通訊埠
  - 重啟 SSH：`sudo systemctl restart sshd`

## 進階功能
### 容器與虛擬化
- **Podman**：RHEL 的無根容器工具
  - 執行容器：`podman run -it docker.io/library/centos bash`
  - 建置映像檔：`podman build -t <image-name> .`
- **虛擬化**：使用 `libvirt` 與 `virt-manager` 管理虛擬機器
  - 安裝：`sudo dnf install libvirt virt-manager`
  - 啟動 libvirt：`sudo systemctl start libvirtd`

### Ansible 自動化
- 安裝 Ansible：`sudo dnf install ansible`
- 建立劇本：
  ```yaml
  - name: Install Apache
    hosts: all
    tasks:
      - name: Install httpd
        dnf:
          name: httpd
          state: present
  ```
- 執行劇本：`ansible-playbook playbook.yml`

### 雲端整合
- RHEL 與 AWS、Azure 及 Google Cloud 整合
- 使用 Red Hat OpenShift 進行容器編排
- 透過 Red Hat Cloud Access 在雲端環境部署 RHEL 映像檔

## 疑難排解
- **日誌檢查**：查看 `/var/log` 系統日誌（如 `/var/log/messages` 或 `/var/log/secure`）
- **Systemd**：使用 `systemctl` 管理服務
  - 檢查服務狀態：`systemctl status <service>`
  - 重啟服務：`systemctl restart <service>`
- **效能監控**：使用 `top`、`htop` 或 `vmstat` 監控系統效能
- **網路問題**：使用 `ping`、`traceroute` 或 `nslookup` 進行診斷

## 最佳實踐
- 定期更新系統以修補安全漏洞
- 使用強密碼並強制執行 SELinux 政策
- 使用 `rsync` 或 Red Hat 的 `rear` 等工具備份關鍵資料
- 使用 Cockpit (`sudo dnf install cockpit`) 等工具監控系統健康狀態

## 參考資源
- [Red Hat 客戶入口網站](https://access.redhat.com)
- [RHEL 說明文件](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux)
- [Red Hat 開發者計劃](https://developers.redhat.com)
- 社群論壇如 [Red Hat Discuss](https://discuss.redhat.com)