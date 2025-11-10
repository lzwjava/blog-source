---
audio: false
generated: true
image: false
lang: ja
layout: post
title: RHEL完全エンタープライズLinuxガイド
translated: true
type: note
---

以下は**Red Hat Enterprise Linux (RHEL) の包括的ガイド**です。学習パスとリファレンスの両方として活用できるよう、段階的に構成しています。

---

## 1. Red Hat Linux の紹介

Red Hat Enterprise Linux (RHEL) は、**Red Hat, Inc.** によって開発された商用Linuxディストリビューションであり、**安定性、セキュリティ、エンタープライズサポート**を目的として設計されています。長期サポートライフサイクルと認定されたソフトウェアエコシステムにより、銀行、医療、政府、企業ITなどで広く利用されています。

主な特徴:

* エンタープライズグレードのサポート (メジャーリリースごとに10年以上のライフサイクル)
* 主要ハードウェア (Dell, HP, IBMなど) での認定
* クラウド (AWS, Azure, GCP)、コンテナ (OpenShift, Kubernetes)、仮想化での広範な使用

---

## 2. インストールとセットアップ

* **ダウンロード**: 公式ISOイメージはRed Hatカスタマーポータルから入手可能 (サブスクリプションが必要)
* **インストーラー**: **Anaconda インストーラー**を使用 (グラフィカルモードとテキストモード)
* **パーティショニング**: LVM、XFS (デフォルトファイルシステム)、暗号化ディスクのオプション
* **インストール後ツール**: システム登録用の `subscription-manager`

---

## 3. パッケージ管理

* **RPM (Red Hat Package Manager)** – ソフトウェアの基盤フォーマット
* **DNF (Dandified Yum)** – RHEL 8以降のデフォルトパッケージマネージャー

  * パッケージのインストール:

    ```bash
    sudo dnf install httpd
    ```
  * システムの更新:

    ```bash
    sudo dnf update
    ```
  * パッケージの検索:

    ```bash
    sudo dnf search nginx
    ```

RHELは、ソフトウェアの複数バージョン (例: Python 3.6 と 3.9) に対応する **AppStream** もサポートしています。

---

## 4. システム管理の基礎

* **ユーザー管理**:
  `useradd`, `passwd`, `usermod`, `/etc/passwd`, `/etc/shadow`
* **プロセス管理**:
  `ps`, `top`, `htop`, `kill`, `systemctl`
* **ディスク管理**:
  `lsblk`, `df -h`, `mount`, `umount`, `fdisk`, `parted`
* **システムサービス** (systemd):

  ```bash
  systemctl start nginx
  systemctl enable nginx
  systemctl status nginx
  ```

---

## 5. ネットワーキング

* 設定は `/etc/sysconfig/network-scripts/` に保存
* コマンド:

  * `nmcli` (NetworkManager CLI)
  * `ip addr`, `ip route`, `ping`, `traceroute`
* ファイアウォール:

  * **firewalld** によって管理 (`firewall-cmd`)
  * 例:

    ```bash
    firewall-cmd --add-service=http --permanent
    firewall-cmd --reload
    ```

---

## 6. セキュリティ

* **SELinux**: 強制アクセス制御システム

  * ステータス確認: `sestatus`
  * モード: enforcing, permissive, disabled
* **FirewallD**: ネットワークセキュリティを管理
* **システム更新**: `dnf update` によるセキュリティパッチ適用
* **Auditd**: ロギングとコンプライアンス

---

## 7. ロギングとモニタリング

* **システムログ**:
  `/var/log/` 以下に保存
* **Journald**:
  `journalctl -xe`
* **パフォーマンスツール**:

  * `sar` (sysstat パッケージ)
  * `vmstat`, `iostat`, `dstat`
* **Red Hat Insights**: クラウドベースのシステム分析

---

## 8. 仮想化とコンテナ

* 仮想化には **KVM (Kernel-based Virtual Machine)**
* **Podman** (Dockerの代替):

  ```bash
  podman run -it centos /bin/bash
  ```
* オーケストレーションには **OpenShift** (Kubernetesプラットフォーム)

---

## 9. ストレージ管理

* 柔軟なディスク管理のための **LVM (Logical Volume Manager)**
* **XFS**: デフォルトファイルシステム
* **Stratis**: シンプロビジョニングとスナップショットを備えたストレージ管理

---

## 10. 自動化と構成管理

* **Ansible**: Red Hatの自動化プラットフォーム
* **Kickstart**: OSインストールの自動化
* **System Roles**: RHEL用の事前定義済みAnsibleロール

---

## 11. サブスクリプションとサポート

* Red Hatは**サブスクリプションモデル**を採用
* `subscription-manager` でシステムの登録、サブスクリプションの割り当て、リポジトリの有効化を実行
* RHEL開発者向けサブスクリプションは**個人向けに無料**

---

## 12. ベストプラクティス

* セキュリティパッチを適用し、システムを常に最新の状態に保つ
* デバッグ時以外はSELinuxを enforcing モードで使用する
* `rsyslog` またはELKスタックでログを集中管理する
* 繰り返しタスクはAnsibleで自動化する
* Red Hat Insightsでシステムの健全性を監視する

---

## 13. 学習リソース

* [Red Hat Documentation](https://access.redhat.com/documentation)
* [Red Hat Academy](https://www.redhat.com/en/services/training-and-certification/red-hat-academy)
* 認定資格:

  * **RHCSA** (Red Hat Certified System Administrator)
  * **RHCE** (Red Hat Certified Engineer)
  * **RHCA** (Red Hat Certified Architect)

---

✅ 以上が基礎となります。
これを、実際のコマンドとワークフロー (Webサーバー、データベース、ファイアウォールの設定など) を含む実践的な「ハンズオンガイド」に**拡充**しますか？それとも、より**理論的、概念的な内容**のままにしますか？