---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Red Hat Enterprise Linux エッセンシャルズの習得
translated: true
type: note
---

## Red Hat Linux 入門
Red Hat Enterprise Linux (RHEL) は、Red Hat, Inc. によって開発された主要なオープンソースオペレーティングシステムです。企業環境向けに設計されており、ミッションクリティカルなアプリケーションに対する安定性、セキュリティ、強力なサポートを提供します。RHEL はサーバー、クラウド環境、企業ITインフラストラクチャで広く使用されています。

### 歴史
- **1994年**: Red Hat Linux が商用 Linux ディストリビューションとして初めてリリースされました。
- **2002年**: Red Hat は、エンタープライズグレードの信頼性に焦点を当てた Red Hat Enterprise Linux を導入しました。
- **2025年**: RHEL 9 が最新のメジャーリリースであり、RHEL 10 は開発中で、強化されたセキュリティやコンテナサポートなどの先進的な機能を提供します。

### 主な機能
- **安定性**: RHEL は、メジャーリリースごとに10年のライフサイクルという長期サポート (LTS) を優先します。
- **セキュリティ**: SELinux (Security-Enhanced Linux)、firewalld、定期的なセキュリティパッチなどの機能。
- **パフォーマンス**: ハイパフォーマンスコンピューティング、仮想化、クラウドデプロイメント向けに最適化されています。
- **サブスクリプションモデル**: Red Hat サブスクリプションを通じて、アップデート、サポート、認定ソフトウェアへのアクセスを提供します。
- **エコシステム**: Red Hat OpenShift、Ansible およびその他の DevOps と自動化のためのツールと統合します。

## インストール
### システム要件
- **最小**:
  - 1.5 GB RAM
  - 20 GB ディスク空き容量
  - 1 GHz プロセッサ
- **推奨**:
  - 4 GB RAM 以上
  - 40 GB 以上のディスク空き容量
  - マルチコアプロセッサ

### インストール手順
1. **RHEL のダウンロード**:
   - [Red Hat Customer Portal](https://access.redhat.com) から RHEL ISO を取得します（サブスクリプションまたはデベロッパーアカウントが必要）。
   - または、非生産環境での使用には無料のデベロッパーサブスクリプションを利用します。
2. **ブータブルメディアの作成**:
   - `dd` や Rufus などのツールを使用して、ブータブル USB ドライブを作成します。
   - コマンド例: `sudo dd if=rhel-9.3-x86_64.iso of=/dev/sdX bs=4M status=progress`
3. **起動とインストール**:
   - USB または DVD から起動します。
   - Anaconda インストーラーに従います:
     - 言語と地域を選択します。
     - ディスクパーティショニングを構成します（手動または自動）。
     - ネットワーク設定を構成します。
     - root パスワードとユーザーアカウントを作成します。
4. **システムの登録**:
   - インストール後、Red Hat Subscription Manager に登録します: `subscription-manager register --username <username> --password <password>`
   - サブスクリプションをアタッチします: `subscription-manager attach --auto`

## システム管理
### パッケージ管理
RHEL はパッケージ管理に **DNF** (Dandified YUM) を使用します。
- パッケージのインストール: `sudo dnf install <package-name>`
- システムの更新: `sudo dnf update`
- パッケージの検索: `sudo dnf search <keyword>`
- リポジトリの有効化: `sudo subscription-manager repos --enable <repo-id>`

### ユーザー管理
- ユーザーの追加: `sudo useradd -m <username>`
- パスワードの設定: `sudo passwd <username>`
- ユーザーの変更: `sudo usermod -aG <group> <username>`
- ユーザーの削除: `sudo userdel -r <username>`

### ファイルシステム管理
- ディスク使用量の確認: `df -h`
- マウントされたファイルシステムの一覧表示: `lsblk`
- パーティションの管理: ディスクパーティショニングには `fdisk` または `parted` を使用します。
- LVM (Logical Volume Manager) の構成:
  - 物理ボリュームの作成: `pvcreate /dev/sdX`
  - ボリュームグループの作成: `vgcreate <vg-name> /dev/sdX`
  - 論理ボリュームの作成: `lvcreate -L <size> -n <lv-name> <vg-name>`

### ネットワーキング
- `nmcli` によるネットワークの構成:
  - 接続の一覧表示: `nmcli connection show`
  - 静的 IP の追加: `nmcli con mod <connection-name> ipv4.addresses 192.168.1.100/24 ipv4.gateway 192.168.1.1 ipv4.method manual`
  - 接続の有効化: `nmcli con up <connection-name>`
- `firewalld` によるファイアウォールの管理:
  - ポートの開放: `sudo firewall-cmd --add-port=80/tcp --permanent`
  - ファイアウォールの再読み込み: `sudo firewall-cmd --reload`

### セキュリティ
- **SELinux**:
  - ステータスの確認: `sestatus`
  - モードの設定 (enforcing/permissive): `sudo setenforce 0` (permissive) または `sudo setenforce 1` (enforcing)
  - ポリシーの変更: カスタムポリシーには `semanage` と `audit2allow` を使用します。
- **アップデート**:
  - セキュリティパッチの適用: `sudo dnf update --security`
- **SSH**:
  - SSH のセキュア化: `/etc/ssh/sshd_config` を編集して root ログインを無効化 (`PermitRootLogin no`) し、デフォルトポートを変更します。
  - SSH の再起動: `sudo systemctl restart sshd`

## 高度な機能
### コンテナと仮想化
- **Podman**: RHEL の rootless コンテナツール。
  - コンテナの実行: `podman run -it docker.io/library/centos bash`
  - イメージのビルド: `podman build -t <image-name> .`
- **仮想化**: VM の管理に `libvirt` と `virt-manager` を使用します。
  - インストール: `sudo dnf install libvirt virt-manager`
  - libvirt の起動: `sudo systemctl start libvirtd`

### Ansible による自動化
- Ansible のインストール: `sudo dnf install ansible`
- プレイブックの作成:
  ```yaml
  - name: Apache のインストール
    hosts: all
    tasks:
      - name: httpd のインストール
        dnf:
          name: httpd
          state: present
  ```
- プレイブックの実行: `ansible-playbook playbook.yml`

### クラウド統合
- RHEL は AWS、Azure、Google Cloud と統合します。
- コンテナオーケストレーションには Red Hat OpenShift を使用します。
- Red Hat Cloud Access を介してクラウド環境に RHEL イメージをデプロイします。

## トラブルシューティング
- **ログ**: システムログは `/var/log` を確認します (例: `/var/log/messages` または `/var/log/secure`)。
- **Systemd**: `systemctl` でサービスを管理します:
  - サービスのステータス確認: `systemctl status <service>`
  - サービスの再起動: `systemctl restart <service>`
- **パフォーマンス**: `top`、`htop`、`vmstat` を使用してシステムパフォーマンスを監視します。
- **ネットワークの問題**: 診断に `ping`、`traceroute`、`nslookup` を使用します。

## ベストプラクティス
- 脆弱性を修正するためにシステムを定期的に更新します。
- 強力なパスワードを使用し、SELinux ポリシーを適用します。
- `rsync` や Red Hat の `rear` などのツールで重要なデータをバックアップします。
- Cockpit (`sudo dnf install cockpit`) などのツールでシステムの健全性を監視します。

## リソース
- [Red Hat Customer Portal](https://access.redhat.com)
- [RHEL Documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux)
- [Red Hat Developer Program](https://developers.redhat.com)
- [Red Hat Discuss](https://discuss.redhat.com) などのコミュニティフォーラム