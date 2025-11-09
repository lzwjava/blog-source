---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: HashiCorp Vault 概要
translated: true
type: note
---

### HashiCorp Vaultとは？

HashiCorp Vaultは、「シークレット」と呼ばれる機密データを安全に管理、保存、アクセスするためのオープンソースツールです。これにはAPIキー、パスワード、証明書、トークン、暗号化キーなどが含まれます。Vaultは、アイデンティティベースのシークレット管理、サービスとしての暗号化、特権アクセス制御のための中央集中型システムとして機能し、組織が動的、マルチクラウド、またはハイブリッド環境における機密情報を保護することを支援します。

#### 主な機能
- **シークレット管理**: Vaultは、静的シークレット（長期間有効なパスワードなど）と動的シークレット（オンデマンドで生成され、自動的に期限切れになるデータベースユーザーなどの短期有効資格情報）の両方を扱います。
- **暗号化と監査**: すべてのデータは保存時および転送時に暗号化され、アクセスと変更を追跡するための包括的なロギングと監査が行われます。
- **アイデンティティベースのアクセス**: IDプロバイダー（例：LDAP、OIDC）と連携してユーザーとシステムを認証し、誰が何にアクセスできるかについてのきめ細かいポリシーを適用します。
- **動的認証情報とリース**: シークレットは限られた時間リースされ、長期的な露出のリスクを軽減します。
- **クラウド非依存およびセルフホステッド**: あらゆるインフラストラクチャで動作し、オンプレミス展開またはマネージドサービスのオプションがあります。

#### 仕組み
Vaultはクライアント-サーバーアプリケーションとして動作します。クライアント（アプリケーションまたはユーザー）はVaultサーバーに対して認証を行い、サーバーはポリシーに基づいてリクエストを承認します。承認されると、Vaultは保存されたシークレットを取得したり、新しいシークレットを生成したり、アクセスを無効にしたりできます。例えば、アプリケーションが一時的なデータベース資格情報を要求し、それを使用し、自動的に期限切れにさせることができます。このアーキテクチャには、永続性のためのストレージバックエンド（例：Consul、PostgreSQL）が含まれ、クラスタリングによる高可用性をサポートします。

Vaultは、DevOps、セキュリティ、コンプライアンスのシナリオで広く使用され、手動でのシークレット処理に代わり、低信頼環境における侵害リスクを軽減します。

#### 参考文献
- [What is Vault? | Vault - HashiCorp Developer](https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault)
- [HashiCorp Vault | Identity-based secrets management](https://www.hashicorp.com/en/products/vault)
- [hashicorp/vault: A tool for secrets management, encryption ... - GitHub](https://github.com/hashicorp/vault)
- [What Is HashiCorp Vault & How Does Vault Work? - KodeKloud](https://kodekloud.com/blog/what-is-hashicorp-vault/)