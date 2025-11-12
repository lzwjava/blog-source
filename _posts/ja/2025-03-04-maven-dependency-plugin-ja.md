---
audio: false
generated: true
lang: ja
layout: post
title: Maven 依存関係プラグイン
translated: true
type: note
---

**Maven Dependency Plugin**は、Javaプロジェクトで広く使用されているビルド自動化ツールであるMavenの強力なツールであり、プロジェクトの依存関係を管理および操作するのに役立ちます。Mavenプロジェクトにおける依存関係とは、`pom.xml`ファイルで宣言された外部ライブラリまたはモジュールであり、Mavenはこれらをリポジトリからダウンロードし、コンパイル時、実行時、またはテスト時に利用可能にします。Dependency Pluginは、これらの依存関係を分析、コピー、リスト表示、またはその他の方法で処理するためのさまざまなゴール（タスク）を提供することで、この機能を拡張します。以下に、その効果的な使用方法を示します：

---

#### **1. 使用方法の概要**
Maven Dependency Pluginは、主に2つの方法で使用できます：
- **`pom.xml`ファイルで設定する**： これにより、特定のプラグインゴールをMavenビルドライフサイクルのフェーズ（例：`package`、`install`）にバインドして、ビルドプロセス中に自動的に実行できるようになります。
- **コマンドラインからゴールを直接実行する**： これは、一度限りのタスクや、`pom.xml`を変更したくない場合に理想的です。

このプラグインは、その座標（`groupId: org.apache.maven.plugins`、`artifactId: maven-dependency-plugin`）で識別されます。設定時にはバージョン（例：`3.2.0`）を指定する必要がありますが、コマンドラインでの使用時に省略すると、Mavenが最新バージョンを解決できることがよくあります。

---

#### **2. `pom.xml`へのプラグインの追加**
ビルドプロセスの一部としてプラグインを使用するには、`pom.xml`の`<build><plugins>`セクションに追加します。以下は基本的な例です：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-dependency-plugin</artifactId>
            <version>3.2.0</version>
        </plugin>
    </plugins>
</build>
```

この設定により、`<executions>`ブロックを追加することで、ビルドライフサイクル中に実行する特定のゴールを設定できます。

---

#### **3. 一般的なゴールとその使用方法**
このプラグインは、依存関係を管理するためのいくつかのゴールを提供します。以下に、最も一般的に使用されるゴールとその使用例をいくつか示します：

##### **a. `copy-dependencies`**
- **目的**： プロジェクトの依存関係を指定されたディレクトリ（例：`lib`フォルダへのパッケージング用）にコピーします。
- **`pom.xml`での設定**：
  このゴールを`package`フェーズにバインドして、`mvn package`実行中に依存関係をコピーします：

  ```xml
  <build>
      <plugins>
          <plugin>
              <groupId>org.apache.maven.plugins</groupId>
              <artifactId>maven-dependency-plugin</artifactId>
              <version>3.2.0</version>
              <executions>
                  <execution>
                      <id>copy-dependencies</id>
                      <phase>package</phase>
                      <goals>
                          <goal>copy-dependencies</goal>
                      </goals>
                      <configuration>
                          <outputDirectory>${project.build.directory}/lib</outputDirectory>
                          <includeScope>runtime</includeScope>
                      </configuration>
                  </execution>
              </executions>
          </plugin>
      </plugins>
  </build>
  ```

  - `${project.build.directory}/lib`は、プロジェクト内の`target/lib`に解決されます。
  - `<includeScope>runtime</includeScope>`は、`test`および`provided`を除き、`compile`および`runtime`スコープを持つ依存関係のコピーに制限します。

- **コマンドライン**：
  `pom.xml`を変更せずに直接実行します：

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib
  ```

##### **b. `tree`**
- **目的**： 依存関係ツリーを表示し、すべての直接依存関係と推移的依存関係およびそれらのバージョンを表示します。これはバージョンの競合を特定するのに役立ちます。
- **コマンドライン**：
  以下を実行するだけです：

  ```bash
  mvn dependency:tree
  ```

  これにより、依存関係の階層ビューがコンソールに出力されます。
- **`pom.xml`での設定（オプション）**：
  これをビルドフェーズ（例：`verify`）中に実行したい場合は、`copy-dependencies`と同様に設定します。

##### **c. `analyze`**
- **目的**： 依存関係を分析して、以下のような問題を特定します：
  - 使用されているが宣言されていない依存関係。
  - 宣言されているが使用されていない依存関係。
- **コマンドライン**：
  以下を実行します：

  ```bash
  mvn dependency:analyze
  ```

  これにより、コンソールにレポートが生成されます。
- **注意**： このゴールは、複雑なプロジェクトでは分析を洗練させるために追加の設定が必要な場合があります。

##### **d. `list`**
- **目的**： プロジェクトの解決済みのすべての依存関係をリスト表示します。
- **コマンドライン**：
  以下を実行します：

  ```bash
  mvn dependency:list
  ```

  これにより、簡単な参照に役立つ依存関係のフラットリストが提供されます。

##### **e. `unpack`**
- **目的**： 特定の依存関係（例：JARファイル）の内容をディレクトリに展開します。
- **コマンドライン**：
  特定のアーティファクトを展開する例：

  ```bash
  mvn dependency:unpack -Dartifact=groupId:artifactId:version -DoutputDirectory=target/unpacked
  ```

  `groupId:artifactId:version`を依存関係の座標（例：`org.apache.commons:commons-lang3:3.12.0`）に置き換えてください。

##### **f. `purge-local-repository`**
- **目的**： ローカルのMavenリポジトリ（`~/.m2/repository`）から指定された依存関係を削除し、リモートリポジトリからの新しいダウンロードを強制します。
- **コマンドライン**：
  以下を実行します：

  ```bash
  mvn dependency:purge-local-repository
  ```

  これは、破損した依存関係ファイルのトラブルシューティングに役立ちます。

---

#### **4. カスタマイズオプション**
多くのゴールは、その動作を調整するための設定パラメータをサポートしています：
- **`outputDirectory`**： ファイルをコピーまたは展開する場所を指定します（例：`target/lib`）。
- **`includeScope`または`excludeScope`**： スコープ（例：`runtime`、`test`）で依存関係をフィルタリングします。
- **`artifact`**： `unpack`などのゴールに対して特定の依存関係をターゲットにします。

これらは、`pom.xml`の`<configuration>`セクションで設定するか、`-D`（例：`-DincludeScope=runtime`）を付けてコマンドライン引数として渡すことができます。

---

#### **5. 実用的な例**
- **シナリオ1: スタンドアロンアプリケーションのパッケージング**
  `copy-dependencies`を使用して、すべてのランタイム依存関係を`lib`フォルダに収集します：

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib -DincludeScope=runtime
  ```

- **シナリオ2: 依存関係の競合のデバッグ**
  `dependency:tree`を実行して推移的依存関係を調査します：

  ```bash
  mvn dependency:tree
  ```

  ライブラリの複数のバージョン（例：`commons-logging`）を発見した場合は、`pom.xml`に`<dependencyManagement>`セクションを追加して競合を解決します。

- **シナリオ3: リソースの抽出**
  依存関係を展開してその内容にアクセスします：

  ```bash
  mvn dependency:unpack -Dartifact=org.example:my-lib:1.0.0 -DoutputDirectory=target/resources
  ```

---

#### **6. まとめ**
Maven Dependency Pluginを使用するには：
- ビルドプロセスに統合したい場合は、特定のゴールと設定を指定して`pom.xml`に追加します。
- 一時的なタスクには、`copy-dependencies`、`tree`、`analyze`、`list`、`unpack`などのゴールをコマンドラインから直接実行します。
- 設定オプションを使用して動作をカスタマイズし、プロジェクトのニーズに合わせます。

このプラグインは、単純な宣言を超えた依存関係の管理における多目的なツールであり、Mavenプロジェクトの構築、デバッグ、および配布にとって貴重なものです。