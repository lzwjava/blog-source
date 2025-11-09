---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: RHELへのEmacsインストール
translated: true
type: note
---

### Red Hat Enterprise Linux への Emacs インストール

Red Hat Enterprise Linux (RHEL) では、ソフトウェアのインストールに主に DNF パッケージマネージャーを使用します。Emacs はデフォルトのリポジトリで利用可能であるため、インストールは簡単です。以下は、最新バージョン (RHEL 8 以降) の手順です。古いバージョン (例: RHEL 7) では、`dnf` を `yum` に置き換えてください。

#### 前提条件
- root 権限を持っていることを確認してください (`sudo` を使用)。
- 公式 RHEL リポジトリを使用する場合は、システムが Red Hat Subscription Management に登録されている必要があります。

#### インストール手順
1. **パッケージキャッシュを更新** (利用可能な最新バージョンを確実に入手するために推奨):  
   ```
   sudo dnf update
   ```

2. **Emacs をインストール**:  
   ```
   sudo dnf install emacs
   ```  
   これにより、リポジトリで利用可能な最新の安定版 (例: お使いの RHEL バージョンに応じて Emacs 28.x または 29.x) がインストールされます。

3. **インストールを確認**:  
   バージョンを確認するために以下を実行:  
   ```
   emacs --version
   ```  
   `GNU Emacs 28.2` (または類似) のような出力が表示されるはずです。

#### 注意点
- YUM を使用している古い RHEL バージョン (例: RHEL 7) の場合、コマンドは `sudo yum install emacs` です。
- 絶対最新の Emacs バージョン (例: 29+) の場合、ベースのリポジトリは遅れている可能性があるため、ソースからコンパイルするか、EPEL などのサードパーティ製リポジトリを使用する必要があるかもしれません。
- Emacs を起動するには、ターミナルで `emacs` と入力するだけです。

[GNU Emacs FAQ: Emacs のインストール](https://www.gnu.org/software/emacs/manual/html_node/efaq/Installing-Emacs.html)  
[Red Hat ドキュメント: DNF ツールによるソフトウェアの管理](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/managing_software_with_the_dnf_tool/index)