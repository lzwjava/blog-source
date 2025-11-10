---
audio: false
generated: true
lang: ja
layout: post
title: 'Maven Shade プラグイン: Uber-JAR の作成'
translated: true
type: note
---

`maven-shade-plugin`は、プロジェクトのコンパイル済みコードとその依存関係を組み合わせて「uber-JAR」（単一の自己完結型JARファイル）を作成するためのMavenプラグインです。Javaプロジェクトで、アプリケーションと必要なすべてのライブラリを1つの実行可能JARファイルにパッケージ化して、配布とデプロイを簡素化するために一般的に使用されます。

### 主な詳細:
- **Group ID**: `org.apache.maven.plugins` (公式Apache Mavenプラグインであることを示します)
- **Artifact ID**: `maven-shade-plugin` (特定のプラグイン名)
- **目的**:
  - **Shading**: クラス競合を避けるために依存関係のパッケージを再配置（名前変更）します（例：複数のライブラリが同じクラスの異なるバージョンを使用している場合）
  - **パッケージ化**: 依存関係を最終的なJARにバンドルし、スタンドアロンにします
  - **リソース変換**: リソースを変更できます（例：`MANIFEST.MF`のような設定ファイルのマージ）
- **一般的な使用例**:
  - コマンドラインアプリケーションのための実行可能JARの作成
  - 複数の依存関係を持つプロジェクトでのクラスパス競合の解決
  - SparkやHadoopジョブのようなアプリケーションのデプロイの簡素化
- **動作の仕組み**:
  - `pom.xml`ファイルの`<plugins>`セクションで設定されます
  - ビルドプロセス中（通常は`package`フェーズで）、クラスとリソースを結合し、オプションでパッケージを再配置し、最終的なJARを生成します
- **`pom.xml`での設定例**:
  ```xml
  <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-shade-plugin</artifactId>
      <version>3.5.0</version> <!-- 最新バージョンを使用 -->
      <executions>
          <execution>
              <phase>package</phase>
              <goals>
                  <goal>shade</goal>
              </goals>
              <configuration>
                  <transformers>
                      <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                          <mainClass>com.example.Main</mainClass>
                      </transformer>
                  </transformers>
              </configuration>
          </execution>
      </executions>
  </plugin>
  ```
  この例では、実行可能JARのメインクラスを指定し、`package`フェーズ中にプラグインを実行します

- **主な機能**:
  - **依存関係の包含**: 依存関係をJARに埋め込みます
  - **パッケージの再配置**: 競合を避けるためにパッケージ名を変更します（例：`com.google.common`を`shaded.com.google.common`に）
  - **リソースフィルタリング**: リソースファイルをマージまたは変換します
  - **実行可能JAR**: `java -jar`でJARを実行可能にするマニフェストエントリを追加します

### 使用する場合:
- 簡単な配布のために単一のJARが必要な場合
- 依存関係の競合に対処する場合（例：同じライブラリの異なるバージョン）
- 外部依存関係の管理が困難な環境へのアプリケーションのデプロイ時

設定や使用例について具体的な質問があれば、お知らせください！