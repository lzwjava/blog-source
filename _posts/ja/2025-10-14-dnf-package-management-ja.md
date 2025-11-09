---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: RHELにおけるDNFパッケージ管理
translated: true
type: note
---

### Red Hat Enterprise Linux における DNF の紹介

DNF (Dandified YUM) は、Red Hat Enterprise Linux (RHEL) 8 から RHEL 9 に引き継がれている主要なパッケージ管理ツールです。これは、以前の YUM (Yellowdog Updater, Modified) ツールの後継として、パフォーマンスの向上、依存関係解決の改善、モジュラーコンテンツのサポートを提供します。RHEL では、DNF は RPM (Red Hat Package Manager) リポジトリを介して配布されるソフトウェアパッケージのインストール、更新、削除を処理します。BaseOS (コア OS 機能用) や AppStream (ユーザースペースアプリケーション、ランタイム、ツール用) などの必須コンテンツセットへのアクセスを、RHEL サブスクリプションを通じて管理します。

DNF の目的は、システムの安定性を維持しながら、ソフトウェアライフサイクル管理を簡素化することです。管理者とユーザーは、従来の RPM パッケージと最新のモジュラー形式を同時に扱うことができ、言語やデータベースなどのコンポーネントが、ベース OS を中断することなく複数の並行バージョン (「ストリーム」と呼ばれる) を持つことができます。

#### 主な機能
- **モジュラーコンテンツのサポート**: モジュール (関連する RPM のグループ)、ストリーム (バージョン固有のリポジトリ)、プロファイル (特定のユースケース、例えば Web サーバーや開発環境向けの事前設定済みパッケージセット) を管理します。
- **リポジトリの扱い**: BaseOS、AppStream、補助的なリポジトリなどのソースの検索、有効化/無効化、設定を可能にします。
- **インストールと更新**: パッケージ、グループ、またはモジュール全体をインストールする際に依存関係を自動的に解決します。更新の確認、特定のパッケージのアップグレード、またはシステム全体のアップグレードをサポートします。
- **削除とロールバック**: ソフトウェアを安全に削除し、変更を元に戻すためのトランザクション履歴を提供します。
- **カスタマイズと自動化**: `/etc/dnf/dnf.conf` で除外、プラグイン、キャッシュなどを設定可能です。DNF Automatic のようなツールと統合して、スケジュールされた更新を実行できます。
- **下位互換性**: RHEL では `yum` コマンドは `dnf` のエイリアスとなっており、古いバージョンからの移行が容易です。

使い始めるには、基本的なコマンドとして、インストール用の `dnf install <パッケージ名>`、アップグレード用の `dnf update`、ソフトウェア検索用の `dnf search <検索語>` があります。より高度な使用方法については、公式ドキュメントを参照してください。

[Red Hat Enterprise Linux 9: DNF ツールによるソフトウェアの管理](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/managing_software_with_the_dnf_tool/index)