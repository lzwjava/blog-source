---
audio: false
generated: true
lang: ja
layout: post
title: GitHub PagesプロジェクトサイトのURL規則
translated: true
type: note
---

GitHub Pagesでは、ユーザーサイト（`username.github.io`）に加えて、個人アカウントで**プロジェクトサイト**を作成できます。ただし、プロジェクトサイトのURL形式は特定のパターンに限定され、すべてのサブドメインまたはサブパス設定がネイティブでサポートされているわけではありません。プロジェクトサイトに `username.github.io/project1` または `project1.username.github.io` を使用できるかどうかについて説明します。

### 主なポイント
- **ユーザーサイト**: `username.github.io` という名前の単一リポジトリが `https://username.github.io` でコンテンツを提供します。
- **プロジェクトサイト**: 個人アカウント内の他のリポジトリは、プロジェクトサイトとして設定でき、`https://username.github.io/repository-name`（サブドメインではなくサブパス）で提供されます。
- **サブドメインの制限**: GitHub Pagesは、`github.io` ドメイン配下の `project1.username.github.io` のようなサブドメインをネイティブでサポートしていません。`github.io` ドメインはGitHubによって管理されており、トップレベルサブドメインとしてサポートされているのは、ユーザー向けの `username.github.io` またはOrganization向けの `organization.github.io` のみです。`project1.username.github.io` のようなカスタムサブドメインを使用するには、カスタムドメインとDNS設定が必要です。

### `username.github.io/project1` は使用できるか？
**はい**、プロジェクトサイトに `username.github.io/project1` を使用できます。これはGitHub Pagesがプロジェクトサイトを扱う標準的な方法です：
- 個人アカウントにリポジトリを作成します（例: `username/project1`）。
- そのリポジトリでGitHub Pagesを有効にします：
  - リポジトリの **Settings** タブに移動します。
  - **Pages** セクションまでスクロールします。
  - **Source** で、公開するブランチ（例: `main` または `gh-pages`）を選択して保存します。
- 設定が完了すると、サイトは `https://username.github.io/project1` でアクセス可能になります。
- 追加のリポジトリ（`username/project2`、`username/project3` など）でGitHub Pagesを有効にすることで、複数のプロジェクトサイト（例: `username.github.io/project2`、`username.github.io/project3`）を作成できます。
- **コンテンツ**: 各リポジトリの公開ブランチに `index.html` を追加するか、Jekyllなどの静的サイトジェネレーターを使用します。

### `project1.username.github.io` は使用できるか？
**いいえ**、GitHub Pagesは `github.io` ドメイン配下の `project1.username.github.io` のようなサブドメインをネイティブでサポートしていません。`github.io` ドメインで許可されているのは以下のみです：
- ユーザーサイト向けの `username.github.io`。
- Organizationサイト向けの `organization.github.io`。
- プロジェクトサイト向けの `username.github.io/repository-name` のようなサブパス。

`project1.username.github.io` のようなURLを実現するには、以下が必要です：
1. **カスタムドメイン**: NamecheapやGoDaddyなどのレジストラからドメイン（例: `example.com`）を購入します。
2. **DNS設定**: サブドメイン（例: `project1.example.com`）をGitHub Pagesサイト（例: `username.github.io` または `username.github.io/project1`）に向けるようにCNAMEレコードを設定します。
3. **GitHub Pages設定**:
   - リポジトリの **Pages** 設定で、カスタムドメイン（例: `project1.example.com`）を設定します。
   - オプションで、セキュリティのために「Enforce HTTPS」を有効にします。
4. **結果**: `project1.example.com` を `project1` リポジトリのコンテンツにマッピングできますが、`project1.username.github.io` はできません。GitHubは `github.io` ドメインを管理しており、その配下のカスタムサブドメインを許可していないためです。

### `username.github.io/project1` の設定例
1. アカウント（`username/project1`）に `project1` という名前のリポジトリを作成します。
2. コンテンツを追加します（例: `index.html`）：
   ```bash
   git clone https://github.com/username/project1
   cd project1
   echo "Hello from Project 1" > index.html
   git add --all
   git commit -m "Initial commit"
   git push origin main
   ```
3. GitHub Pagesを有効にします：
   - `username/project1` → **Settings** → **Pages** に移動します。
   - ソースを `main`（または別のブランチ）に設定して保存します。
4. サイトが公開されていることを確認するには、`https://username.github.io/project1` にアクセスします（伝播に数分かかる場合があります）。

### カスタムドメインを使用したカスタムサブドメインの例
`project1.example.com` が必要な場合：
1. ドメイン（例: `example.com`）を所有します。
2. DNSプロバイダの設定で、CNAMEレコードを追加します：
   - 名前: `project1`
   - 値: `username.github.io`
3. `project1` リポジトリの **Pages** 設定で、カスタムドメインを `project1.example.com` に設定します。
4. `project1` リポジトリにコンテンツをプッシュすると、`project1.example.com` で提供されます。

### 制限事項
- **`github.io` ではサブパスのみ**: カスタムドメインがない場合、プロジェクトサイトは常にサブパス（`username.github.io/project1`）として提供され、サブドメイン（`project1.username.github.io`）としては提供されません。
- **ユーザーサイトは1つのみ**: `username.github.io` リポジトリはユーザーサイト用に予約されています。プロジェクトサイトは他のリポジトリを使用し、サブパスとして表示されます。
- **カスタムサブドメインにはカスタムドメインが必要**: `project1.something` を取得するには、`something`（例: `example.com`）を所有し、DNSを設定する必要があります。
- **プライベートリポジトリ**: プライベートリポジトリ内のプロジェクトサイトには、GitHub Pro、Team、またはEnterpriseが必要です。無料アカウントの場合、リポジトリは公開されている必要があります。

### まとめ
- **`username.github.io/project1` を使用する**: はい、これはリポジトリ（`username/project1`）を作成しGitHub Pagesを有効にすることでネイティブにサポートされています。この方法で複数のプロジェクトサイト（例: `username.github.io/project2` など）を作成できます。
- **`project1.username.github.io` を使用する**: いいえ、これは `github.io` 配下ではサポートされていません。同様の効果を得るには、カスタムドメイン（例: `project1.example.com`）とDNS設定が必要です。
- **複数のサブドメイン**: 複数の `*.github.io` サブドメインを取得するには、GitHub Organizationを作成して `org1.github.io`、`org2.github.io` などを設定するか、`project1.example.com` のようなサブドメインにカスタムドメインを使用します。

特定のプロジェクトサイトの設定、カスタムドメインの設定、または複数サイトの管理についてヘルプが必要な場合は、お知らせください！