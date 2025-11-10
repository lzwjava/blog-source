---
audio: false
generated: true
lang: ja
layout: post
title: Palantir JavaフォーマットをSpotlessで設定する
translated: true
type: note
---

**Palantir Java Format** を **Spotless Maven Plugin** で設定するには、`pom.xml` ファイル内でプラグインを `palantirJavaFormat` を使用するように設定し、タブスペース、インデント、インポート順などのフォーマットオプションを指定する必要があります。以下は、Spotless プラグインと Palantir Java Format に基づいてこれらの設定と利用可能なオプションを詳細に説明するガイドです。

### Spotless Maven Plugin と Palantir Java Format の追加

`pom.xml` に Spotless Maven Plugin を含め、`palantirJavaFormat` を使用するように設定します。以下は、タブスペース、インデント、インポート順などの一般的な設定を含む基本的なセットアップです：

```xml
<plugin>
    <groupId>com.diffplug.spotless</groupId>
    <artifactId>spotless-maven-plugin</artifactId>
    <version>2.43.0</version> <!-- 最新バージョンを使用 -->
    <configuration>
        <java>
            <!-- フォーマット対象のファイルを指定 (オプション、デフォルトは全ての .java ファイル) -->
            <includes>
                <include>src/main/java/**/*.java</include>
                <include>src/test/java/**/*.java</include>
            </includes>
            <!-- Palantir Java Format -->
            <palantirJavaFormat>
                <version>2.53.0</version> <!-- 希望のバージョンを指定 -->
                <style>GOOGLE</style> <!-- オプション: GOOGLE, AOSP, PALANTIR -->
                <formatJavadoc>true</formatJavadoc> <!-- オプション: Javadoc をフォーマット -->
            </palantirJavaFormat>
            <!-- インデント設定 -->
            <indent>
                <tabs>true</tabs> <!-- スペースの代わりにタブを使用 -->
                <spacesPerTab>4</spacesPerTab> <!-- タブあたりのスペース数 -->
            </indent>
            <!-- インポート順設定 -->
            <importOrder>
                <order>java,javax,org,com,\\#</order> <!-- カスタムインポート順 -->
            </importOrder>
            <!-- 未使用インポートを削除 -->
            <removeUnusedImports/>
            <!-- その他のオプション設定 -->
            <trimTrailingWhitespace/>
            <endWithNewline/>
            <toggleOffOn/> <!-- spotless:off と spotless:on タグを有効化 -->
        </java>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>apply</goal> <!-- コードを自動フォーマット -->
            </goals>
            <phase>validate</phase> <!-- validate フェーズで実行 -->
        </execution>
    </executions>
</plugin>
```

### 設定オプションの説明

以下は、Spotless の `java` セクションにおける `palantirJavaFormat` の主要な設定オプションの内、タブスペース、インデント、インポート順およびその他の関連設定に焦点を当てた解説です：

#### 1. **Palantir Java Format (`<palantirJavaFormat>`)**

- **`<version>`**: 使用する `palantir-java-format` のバージョンを指定します。[Maven Repository](https://mvnrepository.com/artifact/com.palantir.java-format/palantir-java-format) または [GitHub](https://github.com/palantir/palantir-java-format/releases) で最新バージョンを確認してください。例: `<version>2.53.0</version>`。
- **`<style>`**: フォーマットスタイルを定義します。オプションは：
  - `GOOGLE`: Google Java Style を使用 (2スペースインデント、100文字行制限)。
  - `AOSP`: Android Open Source Project スタイルを使用 (4スペースインデント、100文字行制限)。
  - `PALANTIR`: Palantir のスタイルを使用 (4スペースインデント、120文字行制限、ラムダ対応フォーマット)。[](https://github.com/palantir/palantir-java-format)
- **`<formatJavadoc>`**: Javadoc のフォーマットを有効/無効にするブール値 (Palantir Java Format バージョン ≥ 2.39.0 が必要)。例: `<formatJavadoc>true</formatJavadoc>`。[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)
- **カスタム Group Artifact**: 稀ですが、フォーマッタのカスタムグループとアーティファクトを指定できます。例: `<groupArtifact>com.palantir.java-format:palantir-java-format</groupArtifact>`。

#### 2. **インデント (`<indent>`)**

- **`<tabs>`**: インデントにタブ (`true`) またはスペース (`false`) を使用するブール値。例: `<tabs>true</tabs>`。[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<spacesPerTab>`**: タブあたりのスペース数 (`<tabs>` が `false` の場合、または混合インデントに使用)。一般的な値は `2` または `4`。例: `<spacesPerTab>4</spacesPerTab>`。[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
  - **注意**: Palantir Java Format のスタイル (例: `GOOGLE`, `AOSP`, `PALANTIR`) はインデントの動作に影響を与える可能性があります。例えば、`GOOGLE` はデフォルトで 2 スペース、`AOSP` と `PALANTIR` は 4 スペースを使用します。Spotless の `<indent>` 設定はこれらのデフォルトを上書きまたは補完できますが、競合を避けるため一貫性を保つようにしてください。[](https://stackoverflow.com/questions/50027892/override-google-java-format-with-spotless-maven-plugin)

#### 3. **インポート順 (`<importOrder>`)**

- **`<order>`**: インポートグループの順序をカンマ区切りで指定します。静的インポートには `\\#` を、未指定のインポートには空の文字列 (`""`) を使用します。例: `<order>java,javax,org,com,\\#</order>` は、`java` で始まるインポート、次に `javax` などでソートし、静的インポートを最後にします。[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)
- **`<file>`**: あるいは、インポート順を含むファイルを指定します。例: `<file>${project.basedir}/eclipse.importorder</file>`。ファイル形式は Eclipse のインポート順設定と一致します (例: `java|javax|org|com|\\#`)。[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)
  - ファイル内容の例:
    ```
    #sort
    java
    javax
    org
    com
    \#
    ```

#### 4. **その他の便利な設定**

- **`<removeUnusedImports>`**: 未使用のインポートを削除します。オプションでエンジンを指定可能：
  - デフォルト: 削除に `google-java-format` を使用。
  - 代替: `<engine>cleanthat-javaparser-unnecessaryimport</engine>` を指定すると、新しい Java 機能 (例: Java 17) との JDK8+ 互換性があります。[](https://stackoverflow.com/questions/77126927/spotless-eclipse-formatter-java-17-error-on-string-literals-removing-unu)
- **`<trimTrailingWhitespace>`**: 行末の空白を削除します。例: `<trimTrailingWhitespace/>`。[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<endWithNewline>`**: ファイルが改行で終わることを保証します。例: `<endWithNewline/>`。[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<toggleOffOn>`**: `// spotless:off` と `// spotless:on` コメントを有効にし、コードのセクションをフォーマット対象から除外します。例: `<toggleOffOn/>`。[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<licenseHeader>`**: ファイルにライセンスヘッダーを追加します。例：
  ```xml
  <licenseHeader>
      <content>/* (C) $YEAR */</content>
  </licenseHeader>
  ```
  ファイルを使用することも可能: `<file>${project.basedir}/license.txt</file>`。[](https://www.baeldung.com/java-maven-spotless-plugin)
- **`<formatAnnotations>`**: 型アノテーションが、それらが記述するフィールドと同じ行にあることを保証します。例: `<formatAnnotations/>`。[](https://www.baeldung.com/java-maven-spotless-plugin)
- **`<ratchetFrom>`**: Git ブランチ (例: `origin/main`) に対して変更されたファイルのみをフォーマット対象とします。例: `<ratchetFrom>origin/main</ratchetFrom>`。[](https://github.com/diffplug/spotless/blob/main/plugin-maven/README.md)

#### 5. **POM 固有のフォーマット (`<pom>`)**

`pom.xml` ファイル自体をフォーマットするには、`<pom>` セクションで `sortPom` を使用します：
```xml
<pom>
    <sortPom>
        <nrOfIndentSpace>2</nrOfIndentSpace> <!-- POM のインデント -->
        <predefinedSortOrder>recommended_2008_06</predefinedSortOrder> <!-- 標準的な POM 順序 -->
        <sortDependencies>groupId,artifactId</sortDependencies> <!-- 依存関係をソート -->
        <sortPlugins>groupId,artifactId</sortPlugins> <!-- プラグインをソート -->
        <endWithNewline>true</endWithNewline>
    </sortPom>
</pom>
```
- **`sortPom` のオプション**:
  - `<nrOfIndentSpace>`: インデントのスペース数 (例: `2` または `4`)。
  - `<predefinedSortOrder>`: 要素順のオプション (例: `recommended_2008_06` や `custom_1`)。[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)
  - `<sortDependencies>`: `groupId`, `artifactId` などでソート。
  - `<sortPlugins>`: プラグインも同様にソート。
  - `<endWithNewline>`: POM が改行で終わることを保証。
  - `<expandEmptyElements>`: 空の XML タグを展開 (例: `<tag></tag>` と `<tag/>`)。[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)

### Spotless の実行

- **フォーマットチェック**: `mvn spotless:check` – 設定されたルールに対してコードを検証し、違反が見つかった場合はビルドを失敗させます。
- **フォーマット適用**: `mvn spotless:apply` – ルールに準拠するようにコードを自動フォーマットします。

### 注意点とベストプラクティス

- **IDE との一貫性**: IntelliJ や Eclipse を Spotless に合わせるには、`palantir-java-format` IntelliJ プラグインをインストールするか、Eclipse フォーマッタ XML ファイルを使用します。IntelliJ の場合、互換性のあるスタイルファイル (例: Google スタイル用の `intellij-java-google-style.xml`) をインポートするか、Palantir 設定に合わせて手動で設定します。[](https://plugins.jetbrains.com/plugin/13180-palantir-java-format)
- **バージョン互換性**: 使用する `palantir-java-format` のバージョンが Java バージョンをサポートしていることを確認してください。Java 17+ の場合は、最近のバージョン (例: 2.53.0) を使用します。パターンマッチングなどの一部の機能はサポートが限られている可能性があります。[](https://www.reddit.com/r/java/comments/1g8zu8c/codestyle_and_formatters/)
- **カスタムフォーマット**: 高度なカスタマイズには、`<palantirJavaFormat>` の代わりに `<eclipse>` で Eclipse フォーマッタ XML ファイルを使用します：
  ```xml
  <eclipse>
      <file>${project.basedir}/custom-style.xml</file>
  </eclipse>
  ```
  `custom-style.xml` の例：
  ```xml
  <?xml version="1.0" encoding="utf-8"?>
  <profiles version="21">
      <profile kind="CodeFormatterProfile" name="custom" version="21">
          <setting id="org.eclipse.jdt.core.formatter.tabulation.char" value="space"/>
          <setting id="org.eclipse.jdt.core.formatter.indentation.size" value="4"/>
          <setting id="org.eclipse.jdt.core.formatter.tabulation.size" value="4"/>
      </profile>
  </profiles>
  ```
  [](https://www.baeldung.com/java-maven-spotless-plugin)
- **制限事項**: Palantir Java Format は Eclipse のフォーマッタよりも設定可能なオプションが少ないですが、一貫性と現代的な Java 機能 (例: ラムダ) のために設計されています。すべてのエッジケース (例: 深くネストされたラムダ) を処理できない可能性があります。[](https://www.reddit.com/r/java/comments/18z151f/strict_code_formatter/)

### 利用可能なオプションの概要

| **オプション**                  | **説明**                                                                 | **値の例**                              |
|-----------------------------|---------------------------------------------------------------------------------|------------------------------------------------|
| `<palantirJavaFormat>`      | Palantir Java Format を設定します。                                                | `<version>2.53.0</version>`, `<style>PALANTIR</style>` |
| `<indent>`                  | インデントスタイル (タブまたはスペース) とサイズを設定します。                               | `<tabs>true</tabs>`, `<spacesPerTab>4</spacesPerTab>` |
| `<importOrder>`             | インポートグループの順序を定義するか、ファイルを使用します。                                      | `<order>java,javax,org,com,\\#</order>`        |
| `<removeUnusedImports>`     | 未使用のインポートを削除します。オプションのエンジンを指定可能。                                   | `<engine>cleanthat-javaparser-unnecessaryimport</engine>` |
| `<trimTrailingWhitespace>`  | 行末の空白を削除します。                                                   | `<trimTrailingWhitespace/>`                    |
| `<endWithNewline>`         | ファイルが改行で終わることを保証します。                                              | `<endWithNewline/>`                           |
| `<toggleOffOn>`            | `spotless:off`/`spotless:on` タグを有効にします。                                     | `<toggleOffOn/>`                              |
| `<licenseHeader>`          | ライセンスヘッダーを追加します。                                                         | `<content>/* (C) $YEAR */</content>`           |
| `<formatAnnotations>`       | アノテーションがフィールドと同じ行になるようにフォーマットします。                          | `<formatAnnotations/>`                         |
| `<sortPom>`                | `pom.xml` をソートとインデントでフォーマットします。                                | `<nrOfIndentSpace>2</nrOfIndentSpace>`        |

### ソース

- Spotless Maven Plugin ドキュメント: [GitHub](https://github.com/diffplug/spotless/tree/main/plugin-maven)[](https://github.com/diffplug/spotless/blob/main/plugin-maven/README.md)
- Palantir Java Format: [GitHub](https://github.com/palantir/palantir-java-format)[](https://github.com/palantir/palantir-java-format)
- Spotless 設定に関する Stack Overflow およびコミュニティの例[](https://stackoverflow.com/questions/50027892/override-google-java-format-with-spotless-maven-plugin)[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)[](https://stackoverflow.com/questions/77126927/spotless-eclipse-formatter-java-17-error-on-string-literals-removing-unu)

この設定により、Palantir Java Format を使用した一貫性のあるコードフォーマットが保証され、タブスペース、インデント、インポート順に関する設定を反映できます。さらに説明や追加オプションが必要な場合はお知らせください！