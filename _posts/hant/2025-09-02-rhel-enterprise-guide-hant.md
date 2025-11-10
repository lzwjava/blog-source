---
audio: false
generated: true
image: false
lang: hant
layout: post
title: RHEL 完整企業級 Linux 指南
translated: true
type: note
---

這是一份**Red Hat Enterprise Linux (RHEL) 的完整指南**。我將按步驟建構內容，讓您既能作為學習路徑，也能當作參考資料。

---

## 1. Red Hat Linux 簡介

Red Hat Enterprise Linux (RHEL) 是由 **Red Hat, Inc.** 開發的商業 Linux 發行版，專注於**穩定性、安全性及企業級支援**。因其長期支援生命週期與認證軟體生態系統，廣泛應用於銀行、醫療、政府及企業 IT 領域。

重點特色：

* 企業級技術支援（每個主要版本提供 10 年以上生命週期）
* 通過主流硬體認證（Dell、HP、IBM 等）
* 廣泛應用於雲端（AWS、Azure、GCP）、容器（OpenShift、Kubernetes）及虛擬化環境

---

## 2. 安裝與設定

* **下載**：可透過 Red Hat 客戶入口網站取得官方 ISO 映像檔（需訂閱授權）
* **安裝程式**：使用 **Anaconda 安裝程式**，支援圖形化與文字模式
* **磁碟分割**：支援 LVM、XFS（預設檔案系統）及磁碟加密選項
* **安裝後工具**：使用 `subscription-manager` 進行系統註冊

---

## 3. 套件管理

* **RPM (Red Hat Package Manager)** - 軟體套件的底層格式
* **DNF (Dandified Yum)** - RHEL 8 及以上版本的預設套件管理工具

  * 安裝套件：

    ```bash
    sudo dnf install httpd
    ```
  * 更新系統：

    ```bash
    sudo dnf update
    ```
  * 搜尋套件：

    ```bash
    sudo dnf search nginx
    ```

RHEL 同時支援 **AppStreams**，可提供多版本軟體並存（例如 Python 3.6 與 3.9）

---

## 4. 系統管理基礎

* **使用者管理**：
  `useradd`、`passwd`、`usermod`、`/etc/passwd`、`/etc/shadow`
* **行程管理**：
  `ps`、`top`、`htop`、`kill`、`systemctl`
* **磁碟管理**：
  `lsblk`、`df -h`、`mount`、`umount`、`fdisk`、`parted`
* **系統服務** (systemd)：

  ```bash
  systemctl start nginx
  systemctl enable nginx
  systemctl status nginx
  ```

---

## 5. 網路設定

* 組態檔案存放於 `/etc/sysconfig/network-scripts/`
* 常用指令：

  * `nmcli` (NetworkManager 命令行工具)
  * `ip addr`、`ip route`、`ping`、`traceroute`
* 防火牆：

  * 由 **firewalld** 管理（使用 `firewall-cmd`）
  * 範例：

    ```bash
    firewall-cmd --add-service=http --permanent
    firewall-cmd --reload
    ```

---

## 6. 安全性

* **SELinux**：強制存取控制系統

  * 檢查狀態：`sestatus`
  * 運作模式：enforcing、permissive、disabled
* **FirewallD**：管理網路安全
* **系統更新**：透過 `dnf update` 取得安全性修補程式
* **Auditd**：稽核紀錄與合規性管理

---

## 7. 記錄與監控

* **系統記錄**：
  存放於 `/var/log/` 目錄
* **Journald**：
  `journalctl -xe`
* **效能工具**：

  * `sar`（sysstat 套件）
  * `vmstat`、`iostat`、`dstat`
* **Red Hat Insights**：雲端系統分析服務

---

## 8. 虛擬化與容器

* **KVM** (Kernel-based Virtual Machine) 用於虛擬化
* **Podman**（替代 Docker）：

  ```bash
  podman run -it centos /bin/bash
  ```
* **OpenShift**（Kubernetes 平台）用於容器編排

---

## 9. 儲存管理

* **LVM (Logical Volume Manager)** 提供彈性磁碟管理
* **XFS**：預設檔案系統
* **Stratis**：支援精簡配置與快照的儲存管理工具

---

## 10. 自動化與組態管理

* **Ansible**：Red Hat 自動化平台
* **Kickstart**：自動化作業系統安裝
* **System Roles**：RHEL 預先定義的 Ansible 角色

---

## 11. 訂閱與支援

* Red Hat 採用**訂閱授權模式**
* 使用 `subscription-manager` 進行系統註冊、綁定訂閱與啟用軟體庫
* RHEL 開發者訂閱**提供個人免費使用**

---

## 12. 最佳實踐

* 持續透過安全性修補程式保持系統更新
* 除偵錯需求外，保持 SELinux 於 enforcing 模式
* 使用 `rsyslog` 或 ELK stack 進行集中化記錄管理
* 使用 Ansible 自動化重複性任務
* 透過 Red Hat Insights 監控系統健康狀態

---

## 13. 學習資源

* [Red Hat 官方文件](https://access.redhat.com/documentation)
* [Red Hat Academy](https://www.redhat.com/en/services/training-and-certification/red-hat-academy)
* 認證課程：

  * **RHCSA** (Red Hat 認證系統管理員)
  * **RHCE** (Red Hat 認證工程師)
  * **RHCA** (Red Hat 認證架構師)

---

✅ 以上是基礎架構。
您希望我**將此擴展為實務操作指南**（包含網頁伺服器、資料庫、防火牆等實際指令與工作流程），還是保持**理論與概念性內容**？