---
audio: false
generated: true
lang: ja
layout: post
title: Maven プラグイン ビルド ヘルパー
translated: true
---

`builder-helper-maven-plugin`は、現在**Build Helper Maven Plugin**として知られています。これは、Mavenのビルドライフサイクルでさまざまなタスクをサポートするための多機能ツールです。元々はCodehausでホストされていましたが、現在はMojoHausでメンテナンスされています。ただし、Mavenの座標は依然として`org.codehaus.mojo`グループIDを使用しています。このプラグインは、追加のソースディレクトリを追加する、追加のアーティファクトをアタッチする、バージョン情報を解析するなど、さまざまな操作をサポートするためのゴールのセットを提供します。以下に、このプラグインをMavenプロジェクトで使用する方法を案内します。

### Mavenとは？
プラグインに入る前に、まずコンテキストを設定します。Mavenは、主にJavaプロジェクト用の広く使用されるビルド自動化ツールです。依存関係の管理、コードのコンパイル、アプリケーションのパッケージングなど、すべてを中央のファイル`pom.xml`を通じて設定することで、ビルドプロセスを簡素化し標準化します。

### ステップ1: `pom.xml`にプラグインを追加
Build Helper Maven Pluginを使用するには、Mavenプロジェクトの`pom.xml`ファイル内の`<build><plugins>`セクションに追加する必要があります。以下にその方法を示します：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <!-- 特定のゴールのための実行がここに追加されます -->
        </plugin>
    </plugins>
</build>
```

- **グループID**: `org.codehaus.mojo`（元々の場所を反映していますが、現在はMojoHausの下にあります）。
- **アーティファクトID**: `build-helper-maven-plugin`。
- **バージョン**: 最後の更新時点で、`3.6.0`が最新バージョンですが、最新のリリースについては[Maven Central](https://mvnrepository.com/artifact/org.codehaus.mojo/build-helper-maven-plugin)を確認してください。

この宣言により、プラグインがプロジェクトで利用可能になりますが、特定のゴールを設定するまで何も行いません。

### ステップ2: 特定のゴールのための実行を設定
Build Helper Maven Pluginは、特定のタスクに設計された複数のゴールを提供します。これらのゴールは、プラグインの宣言内に`<executions>`ブロックを追加することで設定され、どのMavenライフサイクルフェーズで実行されるか、どのように動作するかを指定します。

以下に、一般的に使用されるゴールとその目的を示します：

- **`add-source`**: プロジェクトに追加のソースディレクトリを追加します。
- **`add-test-source`**: 追加のテストソースディレクトリを追加します。
- **`add-resource`**: 追加のリソースディレクトリを追加します。
- **`attach-artifact`**: インストールとデプロイのためにプロジェクトに追加のアーティファクト（例：ファイル）をアタッチします。
- **`parse-version`**: プロジェクトのバージョンを解析し、プロパティ（例：メジャー、マイナー、インクリメンタルバージョン）を設定します。

各ゴールには独自の設定が必要で、これは`<execution>`ブロック内で定義します。

### ステップ3: 例 – 追加のソースディレクトリを追加
このプラグインの一般的な使用例は、追加のソースディレクトリを追加することです。Mavenは通常、デフォルトで1つのみをサポートします（`src/main/java`）。以下に、`add-source`ゴールを設定して追加のソースディレクトリを含める方法を示します：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <executions>
                <execution>
                    <id>add-source</id>
                    <phase>generate-sources</phase>
                    <goals>
                        <goal>add-source</goal>
                    </goals>
                    <configuration>
                        <sources>
                            <source>path/to/your/extra/source/directory</source>
                        </sources>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

- **`<id>`**: この実行の一意の識別子（例：`add-source`）。
- **`<phase>`**: ゴールが実行されるMavenライフサイクルフェーズ（例：`generate-sources`はディレクトリがビルドの早い段階で追加されることを確保します）。
- **`<goals>`**: 実行するゴールを指定します（この場合は`add-source`）。
- **`<configuration>`**: 追加のソースディレクトリを定義します（`path/to/your/extra/source/directory`を実際のパスに置き換えます。例：`src/main/generated`）。

Mavenコマンド（例：`mvn compile`）を実行すると、Mavenはこの追加のディレクトリをソースフォルダとして含めます。

### 追加の注意点
- **バージョンの互換性**: バージョン3.0.0以降、このプラグインはMaven 3以上が必要です。古いMavenバージョンを使用している場合は、プラグインバージョン1.12以前を使用する必要があります。
- **複数のゴール**: 同じプラグイン内に複数の`<execution>`ブロックを定義して、異なるゴールを実行できます。例えば、`add-source`と`add-test-source`の実行を含めることで、ソースディレクトリとテストソースディレクトリの両方を追加できます。
- **プラグインの実行**: 設定が完了すると、Mavenコマンド（例：`mvn clean install`）を実行することで、指定されたフェーズ中にプラグインのゴールがトリガーされます。

### 追加のリソース
他のゴールの詳細と例については、[公式の使用ページ](https://www.mojohaus.org/build-helper-maven-plugin/usage.html)を確認してください。このページには、すべての利用可能なゴールの包括的なドキュメントとサンプル設定が含まれています。

### 最後に
Build Helper Maven Pluginは、特に非標準のビルド構成が必要なプロジェクトにとって、Mavenツールキットの強力な追加です。`pom.xml`に含め、適切なゴールを設定することで、ビルドプロセスを特定のニーズに合わせてカスタマイズできます。元々はCodehausの下にありましたが、現在のホームはMojoHausであり、Mavenビルドを強化するための信頼できる選択肢のままです。