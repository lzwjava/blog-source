---
audio: false
generated: true
lang: ja
layout: post
title: 組織で複数のGitHub Pagesをホストする方法
translated: true
type: note
---

はい、GitHub Organizationを作成することは、固有の`*.github.io`サブドメインを持つ追加のGitHub Pagesサイトをホストする有効な方法です。各Organizationは独自の`organization.github.io`サイトを持つことができ、個人の`username.github.io`サイトとは別になります。以下に方法と知っておくべきことを説明します。

### 重要なポイント
- **個人アカウントの制限**: 各GitHubユーザーアカウントが持てるユーザーサイトは1つだけで、`username.github.io`リポジトリに紐づき、`username.github.io`でホストされます。これを個人アカウントですでに使用している場合、同じアカウントでは別の`*.github.io`サブドメインを作成できません。
- **Organizationサイト**: 各GitHub Organizationも、`organization.github.io`という名前のリポジトリを作成することで、独自のOrganizationサイトを`organization.github.io`でホストできます。これにより、複数のOrganizationを設定することで追加の`*.github.io`サブドメインを作成できます。
- **プロジェクトサイト**: ユーザーとOrganizationアカウントの両方は、他のリポジトリから複数のプロジェクトサイト（例: `username.github.io/project` や `organization.github.io/project`）をホストできますが、これらはサブドメインではなくサブパスです。固有のサブドメイン（例: `sub.example.github.io`）を特に希望する場合、カスタムドメインなしではGitHub Pagesで直接これを実現することはできません。GitHubは`github.io`ドメイン配下でのカスタムサブドメイン（`sub.example.github.io`のような）をサポートしていません。

### 追加の `*.github.io` サブドメインを作成するためのGitHub Organization作成手順
1. **GitHub Organizationを作成**:
   - GitHubにアクセスし、アカウントでサインインします。
   - 右上の"+"アイコンをクリックし、**New organization**を選択します。
   - プロンプトに従ってOrganizationをセットアップし、一意の名前（例: `myorg`）を選択します。この名前がサブドメイン（例: `myorg.github.io`）を決定します。
   - 注意: Organizationは無料で作成できますが、一部の機能（プライベートリポジトリなど）は必要に応じて有料プランが必要になる場合があります。公開リポジトリ向けGitHub PagesはGitHub Freeで利用可能です。

2. **OrganizationのGitHub Pagesリポジトリを作成**:
   - 新しいOrganization内で、`myorg.github.io`（`myorg`はOrganization名に置き換えてください）と正確に名前を付けたリポジトリを作成します。
   - このリポジトリがOrganizationサイトをホストし、`https://myorg.github.io`でアクセス可能になります。

3. **GitHub Pagesをセットアップ**:
   - `myorg.github.io`リポジトリの**Settings**タブに移動します。
   - **Pages**セクションまでスクロールします。
   - **Source**で、公開したいブランチ（例: `main` または `gh-pages`）を選択し保存します。
   - 設定が完了すると、数分後にサイトが`https://myorg.github.io`で公開されます。

4. **コンテンツを追加**:
   - リポジトリの公開ブランチに`index.html`ファイルを追加するか、Jekyllのような静的サイトジェネレーターを使用します。
   - 変更をコミットしてプッシュします。例:
     ```bash
     git clone https://github.com/myorg/myorg.github.io
     cd myorg.github.io
     echo "Hello World" > index.html
     git add --all
     git commit -m "Initial commit"
     git push origin main
     ```
   - `https://myorg.github.io`にアクセスしてサイトが公開されていることを確認します。

5. **追加のサブドメインのために繰り返す**:
   - 追加のOrganization（例: `myorg2`, `myorg3`）を作成し、プロセスを繰り返して`myorg2.github.io`、`myorg3.github.io`などを取得します。
   - 各Organizationは1つの`*.github.io`サブドメインを持つことができるため、Organizationの数だけ多くのサブドメインを作成できます。

### 制限と考慮事項
- **`github.io`上のカスタムサブドメイン**: `sub.myorg.github.io`のようなサブドメインをGitHub Pagesで直接作成することはできません。`github.io`ドメインはGitHubによって管理されており、サポートされているのは`username.github.io`または`organization.github.io`のみです。カスタムサブドメイン（例: `blog.example.com`）を使用するには、カスタムドメインを所有し、DNS設定（CNAMEレコード）を`myorg.github.io`を指すように設定する必要があります。
- **サブドメインごとの単一リポジトリ**: 各`*.github.io`サブドメインは単一のリポジトリ（`username.github.io` または `organization.github.io`）に紐づいています。カスタムドメインと追加のホスティングまたはプロキシサービスなしでは、単一のリポジトリから複数のサブドメインを提供することはできません。
- **管理オーバーヘッド**: 各Organizationには個別の管理（メンバー、権限、請求など）が必要です。複数のOrganizationを管理することに問題ないことを確認してください。
- **DNSとカスタムドメイン**: `*.github.io`の代わりにカスタムドメイン（例: `example.com` または `sub.example.com`）を使用したい場合は、リポジトリの**Pages**設定で設定し、DNSプロバイダーにCNAMEレコードを追加できます。例えば、`sub.example.com`を`myorg.github.io`に向けます。引き継ぎリスクを防ぐため、ドメインを必ず確認してください。
- **プライベートリポジトリ**: プライベートリポジトリ向けGitHub PagesにはGitHub Pro、Team、またはEnterpriseプランが必要です。無料プランを使用している場合は、`myorg.github.io`リポジトリが公開されていることを確認してください。

### 複数サブドメインの代替案
単一のカスタムドメイン配下に複数のサブドメイン（例: `blog.example.com`, `shop.example.com`）を持ちたい場合:
1. NamecheapやGoDaddyなどのレジストラからカスタムドメイン（例: `example.com`）を購入します。
2. Organization内に複数のリポジトリ（例: `myorg/blog`, `myorg/shop`）を作成します。
3. 各リポジトリに対してGitHub Pagesを有効にし、それぞれの**Pages**設定で`blog.example.com`や`shop.example.com`のようなカスタムドメインを設定します。
4. DNSプロバイダーでCNAMEレコードを設定し、`blog.example.com`を`myorg.github.io`に向け、`shop.example.com`を`myorg.github.io`に向けます。独自のカスタムドメインがないリポジトリはすべて、Organizationのカスタムドメインのサブパス（例: `example.com/blog`）として表示されることに注意してください。
5. 単一のリポジトリから複数のサブドメインを提供することは、GitHub Pagesによってネイティブにサポートされておらず、CDNやリバースプロキシなどの外部サービスが必要になる場合があります。

### 例となるシナリオ
- 個人サイトに`username.github.io`を使用済み。
- `myorg`というOrganizationと`myorg.github.io`リポジトリを作成して`myorg.github.io`を取得。
- `myorg2`という別のOrganizationと`myorg2.github.io`リポジトリを作成して`myorg2.github.io`を取得。
- カスタムサブドメインの場合、`example.com`を所有し、CNAMEレコードを介して`blog.example.com`（`myorg.github.io`を指す）と`shop.example.com`（`myorg2.github.io`を指す）を設定。

### 最終的な注意点
- 複数のOrganizationを作成することは、カスタムドメインを必要とせずに追加の`*.github.io`サブドメインを取得する簡単な方法です。
- 真のサブドメイン（例: `sub.myorg.github.io`）を希望する場合、GitHubの`github.io`はこれをネイティブにサポートしていないため、カスタムドメインとDNS設定が必要になります。
- ドメインの引き継ぎリスクを避けるため、常にカスタムドメインを確認してください。
- DNSの変更が反映されるまでに最大24時間かかる場合があります。

特定の設定についてさらに質問や助けが必要な場合は、お知らせください！