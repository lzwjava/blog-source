---
audio: false
generated: true
lang: ja
layout: post
title: Mavenプロキシ設定
translated: true
type: note
---

`checkproxy`コマンドの出力に基づくと、HTTPおよびHTTPSプロキシが両方とも`http://127.0.0.1:7890`に設定されています。以下は、Mavenがこれらのプロキシ設定を使用するように設定するための更新されたMaven `settings.xml`設定スニペットです。

### 更新された `settings.xml` プロキシ設定スニペット

Mavenの`settings.xml`ファイル（`~/.m2/settings.xml`または`/usr/share/maven/conf/settings.xml`にあります）の`<proxies>`セクションを以下の内容で追加または更新してください：

```xml
<settings>
  <proxies>
    <proxy>
      <id>http-proxy</id>
      <active>true</active>
      <protocol>http</protocol>
      <host>127.0.0.1</host>
      <port>7890</port>
      <nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>
    </proxy>
    <proxy>
      <id>https-proxy</id>
      <active>true</active>
      <protocol>https</protocol>
      <host>127.0.0.1</host>
      <port>7890</port>
      <nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>
    </proxy>
  </proxies>
</settings>
```

### スニペットの説明
- **`<id>`**: 各プロキシ設定の一意の識別子（`http-proxy`および`https-proxy`）。
- **`<active>true</active>`**: プロキシを有効にします。
- **`<protocol>`**: `checkproxy`の出力に合わせて、HTTPプロキシには`http`、HTTPSプロキシには`https`を設定。
- **`<host>127.0.0.1</host>`**: プロキシ設定に表示されているプロキシサーバーのIPアドレス。
- **`<port>7890</port>`**: 指定された両方のプロキシのポート番号。
- **`<nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>`**: `localhost`と`127.0.0.1`をプロキシ対象から除外。ローカルサービスでの問題を避けるための標準的な設定です。
- **`<username>`や`<password>`なし**: プロキシ出力に認証が示されていないため、これらのフィールドは省略されています。認証が必要な場合は、資格情報を追加してください。

### 適用手順
1. **`settings.xml`を開く**:
   - `~/.m2/settings.xml`が存在する場合は、それを編集（例: `nano ~/.m2/settings.xml`）。
   - 存在しない場合は、作成するか、グローバルファイル`/usr/share/maven/conf/settings.xml`を編集（`sudo`が必要）。

2. **`<proxies>`セクションを挿入または更新**:
   - `<proxies>`が既に存在する場合は、`<proxy>`エントリを上記のスニペットで置き換えるかマージ。
   - `<settings>`が空または最小限の場合は、ファイルの内容としてスニペット全体を使用できます。

3. **ファイルを保存して閉じる**。

### 設定の確認
インターネットアクセスを必要とするMavenコマンドを実行して、プロキシが使用されていることを確認します：
```bash
cd ~/Projects/blog-server
mvn -X clean checkstyle:check
```

デバッグ出力（`-X`）で、Mavenがプロキシを使用していることを示す行（例: `127.0.0.1:7890`への接続）を探してください。コマンドが依存関係をダウンロードするか、ネットワークエラーなしで完了すれば、プロキシは動作しています。

### トラブルシューティング
- **プロキシが動作しない場合**:
  - `127.0.0.1:7890`のプロキシサーバーが実行されていることを確認（例: `curl -x http://127.0.0.1:7890 https://repo.maven.apache.org`でテスト）。
  - `settings.xml`ファイルのタイプミスを確認。
- **設定ファイルが無視される場合**:
  - デバッグ出力でファイルパスを確認し、Mavenが`~/.m2/settings.xml`を読み取っていることを確認。
  - グローバルファイルを使用している場合は、`/usr/share/maven/conf/settings.xml`を正しく編集したことを確認。
- **認証が必要な場合**:
  - プロキシがユーザー名とパスワードを必要とする場合は、各`<proxy>`ブロックに以下を追加：
    ```xml
    <username>yourusername</username>
    <password>yourpassword</password>
    ```

### 以前のコンテキストに関する注意
`blog-server`プロジェクトでの`checkstyle:check`の問題（`checks.xml`と`SuppressWithNearbyTextFilter`に関連）は、以前に提案したように`pom.xml`を更新することで（`maven-checkstyle-plugin:3.3.1`とCheckstyle `10.17.0`、および`<configLocation>${project.basedir}/checks.xml</configLocation>`を使用して）別途解決する必要があります。上記のプロキシ設定は、Mavenがその修正に必要なアーティファクトをダウンロードできるようにします。

更新された`pom.xml`やさらなるプロキシのデバッグに関して問題が発生した場合やヘルプが必要な場合は、お知らせください！