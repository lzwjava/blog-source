---
audio: false
generated: true
lang: ja
layout: post
title: ビルドヘルパーMavenプラグイン
translated: true
type: note
---

`builder-helper-maven-plugin`（現在は**Build Helper Maven Plugin**として知られる）は、Mavenビルドライフサイクルにおける様々なタスクを支援する多目的なツールです。元々Codehausでホストされていましたが、現在はMojoHausによってメンテナンスされており、Maven座標では引き続き`org.codehaus.mojo`グループIDが使用されています。このプラグインは、追加のソースディレクトリの追加、追加アーティファクトのアタッチ、バージョン情報の解析などの操作を支援する一連のゴールを提供します。以下では、このプラグインをMavenプロジェクトで使用する方法を説明します。

### Mavenとは？
プラグインの詳細に入る前に、前提を整理しましょう。Mavenは、主にJavaプロジェクト向けに広く使用されているビルド自動化ツールです。依存関係の管理、コードのコンパイル、アプリケーションのパッケージ化などを中央ファイルである`pom.xml`を通じて簡素化し標準化します。

### ステップ1: `pom.xml`にプラグインを含める
Build Helper Maven Pluginを使用するには、Mavenプロジェクトの`pom.xml`ファイル内の`<build><plugins>`セクションに追加する必要があります。以下にその方法を示します：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <!-- 特定のゴールに対するexecutionsはここに追加されます -->
        </plugin>
    </plugins>
</build>
```

- **Group ID**: `org.codehaus.mojo`（現在はMojoHausの下にあるものの、起源を反映しています）。
- **Artifact ID**: `build-helper-maven-plugin`。
- **Version**: 最終更新時点では`3.6.0`が最新バージョンですが、最新リリースについては[Maven Central](https://mvnrepository.com/artifact/org.codehaus.mojo/build-helper-maven-plugin)で確認してください。

この宣言によりプラグインがプロジェクトで利用可能になりますが、特定のゴールを設定するまで何も実行しません。

### ステップ2: 特定のゴールに対するExecutionsを設定する
Build Helper Maven Pluginは、それぞれが特定のタスク向けに設計された複数のゴールを提供します。これらのゴールは、プラグイン宣言内に`<executions>`ブロックを追加し、いつ実行されるか（Mavenライフサイクルフェーズ経由で）およびどのように動作するかを指定することで設定します。

以下に、一般的に使用されるゴールとその目的を示します：

- **`add-source`**: プロジェクトに追加のソースディレクトリを追加します。
- **`add-test-source`**: 追加のテストソースディレクトリを追加します。
- **`add-resource`**: 追加のリソースディレクトリを追加します。
- **`attach-artifact`**: プロジェクトに追加のアーティファクト（例：ファイル）をインストールおよびデプロイ用にアタッチします。
- **`parse-version`**: プロジェクトのバージョンを解析し、プロパティ（例：メジャー、マイナー、インクリメンタルバージョン）を設定します。

各ゴールには独自の設定が必要であり、`<execution>`ブロック内で定義します。

### ステップ3: 例 – 追加のソースディレクトリを追加する
このプラグインの一般的な使用例は、追加のソースディレクトリを追加することです。Mavenは通常、デフォルトで1つ（`src/main/java`）しかサポートしていないためです。以下に、追加のソースディレクトリを含めるように`add-source`ゴールを設定する方法を示します：

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

- **`<id>`**: この実行に対する一意の識別子（例：`add-source`）。
- **`<phase>`**: ゴールが実行されるMavenライフサイクルフェーズ（例：`generate-sources`は、ビルドの早い段階でディレクトリが追加されることを保証します）。
- **`<goals>`**: 実行するゴールを指定します（この場合は`add-source`）。
- **`<configuration>`**: 追加のソースディレクトリを定義します（`path/to/your/extra/source/directory`を実際のパス、例えば`src/main/generated`に置き換えてください）。

`mvn compile`のようなMavenコマンドを実行すると、Mavenはこの追加ディレクトリをソースフォルダとして含めます。

### 追加の注意点
- **バージョン互換性**: バージョン3.0.0以降、このプラグインはMaven 3以上を必要とします。古いMavenバージョンを使用している場合は、プラグインバージョン1.12以前を使用する必要があります。
- **複数のゴール**: 同じプラグイン内に複数の`<execution>`ブロックを定義して、異なるゴールを実行できます。例えば、`add-source`と`add-test-source`のexecutionsを含めることで、ソースとテストソースの両方のディレクトリを追加できます。
- **プラグインの実行**: 設定後、Mavenコマンド（例：`mvn clean install`）を実行すると、指定されたフェーズでプラグインのゴールがトリガーされます。

### 追加リソース
他のゴールの詳細や例については、[公式使用法ページ](https://www.mojohaus.org/build-helper-maven-plugin/usage.html)を確認してください。このページには、利用可能なすべてのゴールに対する包括的なドキュメントとサンプル設定が提供されています。

### まとめ
Build Helper Maven Pluginは、特に非標準的なビルド設定を必要とするプロジェクトにおいて、Mavenツールキットへの強力な追加機能です。`pom.xml`に含め、適切なゴールを設定することで、特定のニーズに合わせてビルドプロセスを調整できます。Codehausで始まったものの、現在のホームはMojoHausであり、Mavenビルドを強化する信頼性の高い選択肢であり続けています。