---
audio: false
generated: true
lang: ja
layout: post
title: Spring Boot CLIの使い方
translated: true
---

Spring Boot CLI（コマンドラインインターフェース）は、コマンドラインから直接Spring Bootアプリケーションを迅速に開発、テスト、プロトタイプ化するための強力なツールです。特に、完全なプロジェクト構造を設定せずにGroovyスクリプトを実行する、新しいプロジェクトを生成する、またはSpring Bootの機能を試験するのに特に便利です。以下は、Spring Boot CLIを効果的にインストールして使用するための完全なガイドです。

---

## インストール
Spring Boot CLIを使用する前に、インストールする必要があります。操作環境によって2つの主要な方法があります。

### 1. SDKMAN!を使用する（Unix系OS向け、推奨）
SDKMAN!は、ソフトウェア開発キットを管理するツールで、Spring Boot CLIを簡単にインストールする方法です。

- **ステップ1: SDKMAN!をインストールする**
  ターミナルを開き、以下のコマンドを実行します：
  ```bash
  curl -s "https://get.sdkman.io" | bash
  ```
  プロンプトに従ってSDKMAN!を初期化します：
  ```bash
  source "$HOME/.sdkman/bin/sdkman-init.sh"
  ```

- **ステップ2: Spring Boot CLIをインストールする**
  以下のコマンドを実行します：
  ```bash
  sdk install springboot
  ```

### 2. 手動インストール（Windowsまたは手動設定向け）
Windowsを使用している場合や手動インストールを希望する場合：
- [公式Springウェブサイト](https://spring.io/projects/spring-boot)からSpring Boot CLIのZIPファイルをダウンロードします。
- ZIPファイルを任意のディレクトリに展開します。
- 展開したフォルダから`bin`ディレクトリをシステムのPATH環境変数に追加します。

### インストールの確認
Spring Boot CLIが正しくインストールされているか確認するには、ターミナルで以下のコマンドを実行します：
```bash
spring --version
```
インストールされたSpring Boot CLIのバージョン（例：`Spring CLI v3.3.0`）が表示されます。これで使用を開始できます！

---

## Spring Boot CLIの主要な使用方法
Spring Boot CLIは、迅速な開発とプロトタイピングに適したいくつかの機能を提供します。以下に主要な使用方法を示します。

### 1. Groovyスクリプトの実行
Spring Boot CLIの特徴の一つは、完全なプロジェクト設定なしでGroovyスクリプトを直接実行できる点です。これは、迅速なプロトタイピングやSpring Bootの試験に最適です。

- **例：シンプルなWebアプリケーションの作成**
  `hello.groovy`という名前のファイルを作成し、以下の内容を追加します：
  ```groovy
  @RestController
  class HelloController {
      @RequestMapping("/")
      String home() {
          "Hello, World!"
      }
  }
  ```

- **スクリプトの実行**
  ターミナルで`hello.groovy`が含まれるディレクトリに移動し、以下のコマンドを実行します：
  ```bash
  spring run hello.groovy
  ```
  これにより、ポート8080でWebサーバーが起動します。ブラウザを開き、`http://localhost:8080`にアクセスして「Hello, World!」が表示されることを確認します。

- **依存関係の追加**
  `@Grab`アノテーションを使用して、スクリプトに依存関係を直接含めることができます。例えば：
  ```groovy
  @Grab('org.springframework.boot:spring-boot-starter-data-jpa')
  @RestController
  class HelloController {
      @RequestMapping("/")
      String home() {
          "Hello, World!"
      }
  }
  ```
  これにより、ビルドファイルなしでSpring Data JPAがスクリプトに追加されます。

- **複数のスクリプトの実行**
  現在のディレクトリ内のすべてのGroovyスクリプトを実行するには、以下のコマンドを使用します：
  ```bash
  spring run *.groovy
  ```

### 2. 新しいSpring Bootプロジェクトの作成
Spring Boot CLIは、希望する依存関係を含む新しいプロジェクト構造を生成し、完全なアプリケーションを開始する際に時間を節約できます。

- **例：プロジェクトの生成**
  Webとdata-jpaの依存関係を含む新しいプロジェクトを作成するには、以下のコマンドを実行します：
  ```bash
  spring init --dependencies=web,data-jpa my-project
  ```
  これにより、`my-project`という名前のディレクトリが作成され、Spring WebとSpring Data JPAで構成されたSpring Bootアプリケーションが含まれます。

- **カスタマイズオプション**
  追加のオプションを指定することもできます：
  - ビルドツール：`--build=maven`または`--build=gradle`
  - 言語：`--language=java`、`--language=groovy`または`--language=kotlin`
  - パッケージング：`--packaging=jar`または`--packaging=war`

  例えば：
  ```bash
  spring init --dependencies=web --build=gradle --language=kotlin my-kotlin-project
  ```

### 3. アプリケーションのパッケージ化
Spring Boot CLIを使用して、スクリプトを実行可能なJARまたはWARファイルにパッケージ化し、デプロイすることができます。

- **JARファイルの作成**
  ```bash
  spring jar my-app.jar *.groovy
  ```
  これにより、現在のディレクトリ内のすべてのGroovyスクリプトが`my-app.jar`にパッケージ化されます。

- **WARファイルの作成**
  ```bash
  spring war my-app.war *.groovy
  ```
  これにより、`my-app.war`という名前のファイルが生成され、サーブレットコンテナにデプロイするのに適しています。

### 4. テストの実行
Groovyのテストスクリプトがある場合、以下のコマンドで実行できます：
```bash
spring test *.groovy
```
これにより、現在のディレクトリ内のすべてのテストスクリプトが実行されます。

### 5. インタラクティブシェルの使用
インタラクティブな体験を得るには、Spring Boot CLIシェルを起動します：
```bash
spring shell
```
シェル内で`run`、`grab`、`jar`などのコマンドをインタラクティブに実行でき、これは実験に最適です。

---

## まとめ
Spring Boot CLIは、コマンドラインから迅速かつ効率的にSpring Bootを使用したい開発者にとって優れたツールです。以下のように使用します：

1. **インストール**：SDKMAN!を使用してインストールします（`sdk install springboot`）または、ZIPをダウンロードしてPATHを更新します。
2. **Groovyスクリプトの実行**：`spring run <script.groovy>`を使用して迅速なプロトタイピングを行います。
3. **新しいプロジェクトの作成**：`spring init --dependencies=<deps> <project-name>`を使用して新しいプロジェクトを作成します。
4. **アプリケーションのパッケージ化**：`spring jar`または`spring war`を使用してJARまたはWARファイルにパッケージ化します。
5. **インタラクティブな実験**：`spring shell`を使用してインタラクティブに実験します。

アイデアのプロトタイピング、Spring Bootの学習、またはタスクの自動化を行う場合、Spring Boot CLIは完全なIDEやプロジェクト設定なしで軽量で柔軟な方法を提供します。