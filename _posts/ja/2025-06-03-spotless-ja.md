---
audio: false
generated: true
lang: ja
layout: post
title: スポットレスを使用したコードフォーマット
translated: true
type: note
---

Maven Checkstyle Pluginには`mvn checkstyle:format`コマンドは存在しません。このプラグインは主にコードをCheckstyle設定に対してチェックし、違反を報告することを目的としており、コードを自動的にフォーマットするものではありません。ただし、Checkstyle設定に基づいたコードフォーマットは、SpotlessやMaven Formatter Pluginなどの他のツールを使用して実現できます。これらはCheckstyleルールに合わせて設定することが可能です。

以下では、**Spotless Maven Plugin**を使用してCheckstyle設定に基づいてコードをフォーマットする方法を説明します。このプラグインはこの目的で人気があり、Checkstyleルールと統合できます。

### 解決策: SpotlessとCheckstyle設定の使用

Spotless Maven Pluginは、Checkstyle設定ファイル（例: `checkstyle.xml`）に従ってJavaコードをフォーマットできます。設定方法は以下の通りです。

#### 1. `pom.xml`にSpotlessを追加
`pom.xml`にSpotlessプラグインを追加し、Checkstyle設定ファイルを使用するように設定します。

```xml
<build>
  <plugins>
    <plugin>
      <groupId>com.diffplug.spotless</groupId>
      <artifactId>spotless-maven-plugin</artifactId>
      <version>2.43.0</version> <!-- 最新バージョンを使用 -->
      <configuration>
        <java>
          <!-- Checkstyle設定ファイルを指定 -->
          <googleJavaFormat>
            <version>1.22.0</version> <!-- 任意: 特定のバージョンを使用 -->
            <style>GOOGLE</style> <!-- またはAOSP、またはデフォルトの場合は省略 -->
          </googleJavaFormat>
          <formatAnnotations>
            <!-- フォーマットにCheckstyle設定を使用 -->
            <checkstyle>
              <file>${project.basedir}/checkstyle.xml</file> <!-- Checkstyle設定ファイルへのパス -->
              <version>10.17.0</version> <!-- 使用中のCheckstyleバージョンに合わせる -->
            </checkstyle>
          </formatAnnotations>
        </java>
      </configuration>
      <executions>
        <execution>
          <goals>
            <goal>apply</goal> <!-- コードを自動フォーマット -->
          </goals>
          <phase>process-sources</phase> <!-- 任意: 特定のフェーズにバインド -->
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

#### 2. Checkstyle設定ファイルの確認
プロジェクトに`checkstyle.xml`ファイルが存在することを確認してください（例: ルートディレクトリまたはサブディレクトリ）。このファイルは、Spotlessがコードをフォーマットする際に使用するコーディング標準（インデント、空白など）を定義します。Google Java Formatのような標準を使用している場合はそれを参照するか、プロジェクトに合わせたカスタムCheckstyle設定を使用できます。

基本的なフォーマットルールのための`checkstyle.xml`の例:
```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN" "https://checkstyle.sourceforge.io/dtds/configuration_1_3.dtd">
<module name="Checker">
  <module name="TreeWalker">
    <module name="Indentation">
      <property name="basicOffset" value="2"/>
      <property name="braceAdjustment" value="0"/>
    </module>
  </module>
</module>
```

#### 3. Spotlessの実行によるコードフォーマット
Checkstyle設定に基づいてコードをフォーマットするには、以下を実行します:
```bash
mvn spotless:apply
```

このコマンドは、Checkstyle設定で定義されたルールと追加のフォーマット設定（例: Google Java Format）に従って、プロジェクト内のすべてのJavaファイルをフォーマットします。

#### 4. Checkstyleによるフォーマットの検証
フォーマット後、`mvn checkstyle:check`を実行して、フォーマットされたコードがCheckstyleルールに準拠していることを確認できます。以前のアドバイスに従って`<failOnViolation>false</failOnViolation>`を設定している場合は、ビルドを停止せずに残りの違反を報告します。

### 代替案: Maven Formatter Plugin
Spotlessを使用したくない場合は、**Maven Formatter Plugin**を使用することもできます。このプラグインもルールに基づいたフォーマットをサポートしますが、Checkstyle設定を直接使用する場合はあまり一般的ではありません。基本的な設定は以下の通りです。

```xml
<build>
  <plugins>
    <plugin>
      <groupId>net.revelc.code.formatter</groupId>
      <artifactId>formatter-maven-plugin</artifactId>
      <version>2.23.0</version> <!-- 最新バージョンを使用 -->
      <configuration>
        <configFile>${project.basedir}/checkstyle.xml</configFile> <!-- Checkstyle設定ファイルへのパス -->
      </configuration>
      <executions>
        <execution>
          <goals>
            <goal>format</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

フォーマットを実行するには:
```bash
mvn formatter:format
```

### 注意点
- **Checkstyleフォーマットコマンドの非存在**: Checkstyle Maven Pluginは`format`ゴールを提供しません。Checkstyleルールに基づいたフォーマットを適用するには、SpotlessやFormatter Pluginなどのツールが必要です。
- **Checkstyleバージョンの互換性**: Spotless（またはFormatter）で指定されたCheckstyleバージョンが、Checkstyleプラグインで使用されているバージョンと一致することを確認し、ルールの不一致を避けてください。
- **カスタムCheckstyleルール**: Spotlessが正しく適用されるためには、`checkstyle.xml`にフォーマット関連のルール（例: `Indentation`, `WhitespaceAround`など）が含まれている必要があります。
- **マルチモジュールプロジェクト**: マルチモジュールのMavenプロジェクトでは、親`pom.xml`にSpotless/Formatter設定を配置してすべてのモジュールに適用するか、必要に応じてモジュールごとに設定できます。
- **フォーマット後のチェック**: 特にCheckstyle設定に非フォーマットルール（メソッドの長さ、複雑さなど）が含まれている場合は、フォーマット後に常に`mvn checkstyle:check`を実行して準拠を確認してください。

`checkstyle.xml`がない場合や作成にヘルプが必要な場合は、お知らせください。サンプルを提供したり、さらに案内したりできます。また、別のツールを希望したり、特定のフォーマット要件がある場合は、共有してください。それに応じて解決策を調整します。