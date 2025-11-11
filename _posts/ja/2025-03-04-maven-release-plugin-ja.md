---
audio: false
generated: true
lang: ja
layout: post
title: Mavenリリースプラグイン
translated: true
type: note
---

**Maven Release Plugin**を使用してMavenプロジェクトのリリースプロセスを管理および自動化する方法に関する包括的なガイドです。

---

### Maven Release Pluginとは？

**Maven Release Plugin**は、Mavenプロジェクトのリリースプロセスを自動化するツールです。以下のタスクを処理します：

- プロジェクトのPOMファイル内のバージョン番号の更新
- Gitなどのバージョン管理システム（VCS）への変更のコミット
- VCSでのリリース用タグの作成
- リリースアーティファクトのビルドとデプロイ
- バージョン番号を再度更新して、次の開発サイクルに向けたプロジェクトの準備

このプラグインの主な2つのゴールは：

- **`release:prepare`**: バージョンの更新、変更のコミット、VCSでのリリースのタグ付けにより、リリースのためのプロジェクトを準備します。
- **`release:perform`**: VCSからタグ付けされたコードを使用して、リリースされたバージョンをビルドおよびデプロイします。

---

### Maven Release Pluginの使用法：ステップバイステップガイド

#### 1. POMファイルにMaven Release Pluginを追加する

プラグインを使用するには、プロジェクトの`pom.xml`に含める必要があります。`<build><plugins>`セクションの下に以下のように追加します：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-release-plugin</artifactId>
            <version>2.5.3</version> <!-- 最新の安定版を使用してください -->
        </plugin>
    </plugins>
</build>
```

**注意**: [公式Maven Release Pluginページ](https://maven.apache.org/maven-release/maven-release-plugin/)で最新バージョンを確認し、`2.5.3`を適宜置き換えてください。

#### 2. SCM（ソース管理）セクションを設定する

プラグインはVCS（例：Git）と対話して変更をコミットし、タグを作成します。`pom.xml`の`<scm>`セクションでVCSの詳細を指定する必要があります。GitHubでホストされているGitリポジトリの場合、以下のようになります：

```xml
<scm>
    <connection>scm:git:git://github.com/username/project.git</connection>
    <developerConnection>scm:git:git@github.com:username/project.git</developerConnection>
    <url>https://github.com/username/project</url>
</scm>
```

- `username`と`project`を実際のGitHubのユーザー名とリポジトリ名に置き換えてください。
- 異なるGitホスティングサービス（例：GitLab、Bitbucket）を使用している場合は、URLを調整してください。
- リポジトリに変更をプッシュするための必要な資格情報（例：SSHキーやパーソナルアクセストークン）が設定されていることを確認してください。

#### 3. リリースのためのプロジェクトを準備する

リリースコマンドを実行する前に、プロジェクトが準備できていることを確認してください：

- すべてのテストが合格する（`mvn test`）。
- 作業ディレクトリに未コミットの変更がない（`git status`を実行して確認）。
- リリース用の正しいブランチ（例：`master`または`main`）にいる。

#### 4. `release:prepare`を実行する

`release:prepare`ゴールは、リリースのためのプロジェクトを準備します。ターミナルで以下のコマンドを実行します：

```bash
mvn release:prepare
```

**`release:prepare`中に起こること**:

- **未コミットの変更のチェック**: 作業ディレクトリがクリーンであることを確認します。
- **バージョンのプロンプト**: リリースバージョンと次の開発バージョンを尋ねます。
  - 例：現在のバージョンが`1.0-SNAPSHOT`の場合、リリースには`1.0`、次の開発バージョンには`1.1-SNAPSHOT`を提案するかもしれません。デフォルトを受け入れるか、カスタムバージョン（例：パッチリリースの場合は`1.0.1`）を入力できます。
- **POMファイルの更新**: バージョンをリリースバージョン（例：`1.0`）に変更し、変更をコミットし、VCSでタグ付けします（例：`project-1.0`）。
- **次のサイクルの準備**: POMを次の開発バージョン（例：`1.1-SNAPSHOT`）に更新し、コミットします。

**オプションのドライラン**: 変更を加えずにプロセスをテストするには、以下を使用します：

```bash
mvn release:prepare -DdryRun=true
```

これにより、コミットやタグ付けを行わずに準備ステップがシミュレートされます。

#### 5. `release:perform`を実行する

リリースの準備ができたら、以下でビルドおよびデプロイします：

```bash
mvn release:perform
```

**`release:perform`中に起こること**:

- VCSからタグ付けされたバージョンをチェックアウトします。
- プロジェクトをビルドします。
- POMの`<distributionManagement>`セクションで指定されたリポジトリにアーティファクトをデプロイします。

**`<distributionManagement>`の設定**（リモートリポジトリにデプロイする場合）：

```xml
<distributionManagement>
    <repository>
        <id>releases</id>
        <url>http://my-repository-manager/releases</url>
    </repository>
    <snapshotRepository>
        <id>snapshots</id>
        <url>http://my-repository-manager/snapshots</url>
    </snapshotRepository>
</distributionManagement>
```

- URLをリポジトリマネージャーのアドレス（例：Nexus、Artifactory）に置き換えてください。
- 資格情報が`~/.m2/settings.xml`ファイルの`<servers>`の下に、一致する`id`で設定されていることを確認してください。

#### 6. リリースを検証する

`release:perform`の後、リリースを検証してください：

- リポジトリマネージャーをチェックして、アーティファクト（例：JAR、ソース）がデプロイされていることを確認します。
- リリースされたバージョンを別のプロジェクトで、そのPOMに依存関係として追加してテストします。

---

### 追加の設定とヒント

#### 失敗の処理

- **クリーンアップ**: リリースプロセスが失敗した場合、以下を使用します：
  ```bash
  mvn release:clean
  ```
  これにより、プラグインによって作成された一時ファイルが削除されます。
- **ロールバック**: `release:prepare`による変更を元に戻すには：
  ```bash
  mvn release:rollback
  ```
  注意し、どの変更が元に戻されるかを確認してください。

#### マルチモジュールプロジェクト

マルチモジュールプロジェクトの場合、プラグインはデフォルトですべてのモジュールにわたってバージョンを一貫して更新します。親POMにプラグインとSCM設定が含まれていることを確認してください。

#### 自動化のためのバッチモード

リリースを非対話的に実行するには（例：CI/CDパイプライン内）、`-B`フラグを使用し、バージョンを指定します：

```bash
mvn release:prepare -B -DreleaseVersion=1.0 -DdevelopmentVersion=1.1-SNAPSHOT
mvn release:perform -B
```

#### 一般的な問題と解決策

- **VCSエラー**: Gitコマンド（例：`git commit`、`git push`）が手動で動作することを確認してください。認証（SSHキー、トークン）をチェックしてください。
- **ビルド失敗**: ビルドがローカルで成功する（`mvn clean install`）ことと、依存関係が正しく解決されることを確認してください。
- **バージョン戦略**: デフォルトがニーズに合わない場合は、プロンプト中またはプロパティを介してバージョンをカスタマイズしてください。

---

### コマンドのまとめ

1. **リリースの準備**:
   ```bash
   mvn release:prepare
   ```
2. **リリースの実行**:
   ```bash
   mvn release:perform
   ```
3. **オプションのドライラン**:
   ```bash
   mvn release:prepare -DdryRun=true
   ```
4. **必要に応じたクリーンアップまたはロールバック**:
   ```bash
   mvn release:clean
   mvn release:rollback
   ```

---

### 結論

Maven Release Pluginは、バージョン管理、VCSとの対話、デプロイを自動化することで、リリースプロセスを簡素化します。プラグインをPOMに追加し、SCMを設定し、`release:prepare`と`release:perform`のステップに従うことで、Mavenプロジェクトを効率的にリリースできます。常に設定をドライランでテストし、結果を検証して、スムーズなリリースプロセスを確保してください。