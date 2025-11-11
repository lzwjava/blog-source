---
audio: false
generated: true
lang: ja
layout: post
title: Spring Boot CLIの使い方
translated: true
type: note
---

Spring Boot CLI（コマンドラインインターフェース）は、コマンドラインから直接Spring Bootアプリケーションを迅速に開発、テスト、プロトタイピングできる強力なツールです。特に、完全なプロジェクト構造を設定せずにGroovyスクリプトを実行したり、新しいプロジェクトを生成したり、Spring Bootの機能を実験したりするのに非常に便利です。以下は、Spring Boot CLIを効果的にインストールして使用するための完全ガイドです。

---

## インストール
Spring Boot CLIを使用する前に、インストールする必要があります。オペレーティングシステムに応じて主に2つの方法があります：

### 1. SDKMAN!を使用（LinuxやmacOSなどのUnixベースシステムで推奨）
SDKMAN!はソフトウェア開発キットを管理するツールで、Spring Boot CLIを簡単にインストールできます。

- **ステップ1: SDKMAN!をインストール**
  ターミナルを開いて以下を実行：
  ```bash
  curl -s "https://get.sdkman.io" | bash
  ```
  プロンプトに従ってスクリプトをソースしSDKMAN!を初期化：
  ```bash
  source "$HOME/.sdkman/bin/sdkman-init.sh"
  ```

- **ステップ2: Spring Boot CLIをインストール**
  次のコマンドを実行：
  ```bash
  sdk install springboot
  ```

### 2. 手動インストール（Windowsまたは手動セットアップ用）
Windowsを使用している場合、または手動インストールを希望する場合：
- [公式Spring Webサイト](https://spring.io/projects/spring-boot)からSpring Boot CLI ZIPファイルをダウンロード
- ZIPファイルを任意のディレクトリに展開
- 展開したフォルダ内の`bin`ディレクトリをシステムのPATH環境変数に追加

### インストールの確認
Spring Boot CLIが正しくインストールされたことを確認するには、ターミナルで次のコマンドを実行：
```bash
spring --version
```
インストールされたSpring Boot CLIのバージョン（例：`Spring CLI v3.3.0`）が表示されます。これが動作すれば、使用を開始できます！

---

## Spring Boot CLIの主な使用方法
Spring Boot CLIは、迅速な開発とプロトタイピングに理想的ないくつかの機能を提供します。主な使用方法は以下の通りです：

### 1. Groovyスクリプトの実行
Spring Boot CLIの特徴的な機能の1つは、完全なプロジェクト設定を必要とせずに直接Groovyスクリプトを実行できることです。これは迅速なプロトタイピングやSpring Bootの実験に最適です。

- **例：シンプルなWebアプリケーションの作成**
  `hello.groovy`というファイルを作成し、以下の内容を記述：
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
  ターミナルで`hello.groovy`を含むディレクトリに移動し、以下を実行：
  ```bash
  spring run hello.groovy
  ```
  これによりポート8080でWebサーバーが起動します。ブラウザで`http://localhost:8080`にアクセスすると「Hello, World!」が表示されます。

- **依存関係の追加**
  `@Grab`アノテーションを使用してスクリプト内に直接依存関係を含めることができます。例：
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
  これによりビルドファイルなしでSpring Data JPAがスクリプトに追加されます。

- **複数スクリプトの実行**
  カレントディレクトリ内のすべてのGroovyスクリプトを実行するには：
  ```bash
  spring run *.groovy
  ```

### 2. 新しいSpring Bootプロジェクトの作成
Spring Boot CLIは、必要な依存関係を含む新しいプロジェクト構造を生成でき、完全なアプリケーションを開始する際に時間を節約できます。

- **例：プロジェクトの生成**
  Webとdata-jpaの依存関係を持つ新しいプロジェクトを作成するには、このコマンドを実行：
  ```bash
  spring init --dependencies=web,data-jpa my-project
  ```
  これにより、Spring WebとSpring Data JPAで設定されたSpring Bootアプリケーションを含む`my-project`というディレクトリが作成されます。

- **カスタマイズオプション**
  以下のような追加オプションを指定できます：
  - ビルドツール：`--build=maven`または`--build=gradle`
  - 言語：`--language=java`、`--language=groovy`、または`--language=kotlin`
  - パッケージング：`--packaging=jar`または`--packaging=war`

  例：
  ```bash
  spring init --dependencies=web --build=gradle --language=kotlin my-kotlin-project
  ```

### 3. アプリケーションのパッケージ化
Spring Boot CLIでは、スクリプトを実行可能なJARまたはWARファイルにパッケージ化してデプロイできます。

- **JARファイルの作成**
  ```bash
  spring jar my-app.jar *.groovy
  ```
  これによりカレントディレクトリ内のすべてのGroovyスクリプトが`my-app.jar`にパッケージ化されます。

- **WARファイルの作成**
  ```bash
  spring war my-app.war *.groovy
  ```
  これによりサーブレットコンテナへのデプロイに適した`my-app.war`ファイルが生成されます。

### 4. テストの実行
Groovyテストスクリプトがある場合、以下で実行できます：
```bash
spring test *.groovy
```
これによりカレントディレクトリ内のすべてのテストスクリプトが実行されます。

### 5. インタラクティブシェルの使用
インタラクティブな体験のために、Spring Boot CLIシェルを起動：
```bash
spring shell
```
シェル内では`run`、`grab`、`jar`などのコマンドをインタラクティブに実行でき、実験に最適です。

---

## まとめ
Spring Boot CLIは、コマンドラインから迅速かつ効率的にSpring Bootを操作したい開発者にとって優れたツールです。簡単に使用方法をまとめると：

1. **インストール**：SDKMAN!（`sdk install springboot`）を使用するか、ZIPをダウンロードしてPATHを更新して手動インストール
2. **Groovyスクリプトの実行**：迅速なプロトタイピングのために`spring run <script.groovy>`を使用
3. **新しいプロジェクトの作成**：`spring init --dependencies=<deps> <project-name>`でプロジェクト生成
4. **アプリケーションのパッケージ化**：`spring jar`または`spring war`でJARまたはWARファイルにパッケージ化
5. **インタラクティブな実験**：`spring shell`で対話的に操作

アイデアのプロトタイピング、Spring Bootの学習、タスクの自動化など、完全なIDEやプロジェクト設定のオーバーヘッドなしで開始できる軽量で柔軟な方法をSpring Boot CLIは提供します。