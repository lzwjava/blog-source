---
audio: false
generated: true
lang: ja
layout: post
title: JavaにおけるSpotlessとCheckstyleの比較
translated: true
type: note
---

**Spotless Maven Plugin** と **Checkstyle Maven Plugin** は、Javaプロジェクトで一緒に使用できます。これらは互いに補完する目的を持っています。ただし、両方が*必要*かどうかは、プロジェクトの要件によります。以下では、これらがどのように連携するか、その違い、そしてどちらかを選択する場合の判断基準について説明します。

### Spotless と Checkstyle の主な違い

| **観点**             | **Spotless**                                                                  | **Checkstyle**                                                               |
|----------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **目的**             | コードを自動的にフォーマットし、一貫したスタイルを強制し、問題を修正する。          | コーディング標準を強制し、違反を検出するためにコードを静的に解析する。           |
| **動作**             | コードを修正する（例：インデント、import順序の修正、未使用importの削除）。          | コードを修正せずに違反を報告する；チェックが失敗するとビルドを失敗させる。        |
| **設定**             | `palantir-java-format`, `google-java-format` などのフォーマッタを設定する。        | コーディング標準を定義するルールセット（例：Google や Sun のチェック）を使用する。 |
| **出力**             | フォーマットされたソースファイル（`mvn spotless:apply` で生成）。                 | スタイル違反をリストしたレポート（XML、HTML、またはコンソール）。                |
| **ユースケース**     | コミットやビルド前にコードが一貫してフォーマットされていることを保証する。          | フォーマット以外のコーディング標準（複雑さや悪いプラクティスなど）を強制する。    |

### Spotless と Checkstyle を併用する

**自動フォーマット**と**スタイル強制**の両方を実現するために、Spotless と Checkstyle を組み合わせることができます。以下に、それらがどのように補完し合うかを示します：

1.  **フォーマットのための Spotless**:
    *   Spotless は、`palantir-java-format` のようなツールを使用してフォーマットルール（例：インデント、import順序）を適用します。
    *   コードが一貫してフォーマットされることを保証し、手作業を減らします。
    *   例：2スペースと4スペースのインデントを修正、importをソート、未使用importを削除。

2.  **検証のための Checkstyle**:
    *   Checkstyle は、フォーマット以外のコーディング標準を強制します（例：メソッドの長さ、命名規則、複雑さ）。
    *   フォーマッタが対処しない可能性のある問題（Javadocの欠落や過度に複雑なメソッドなど）を検出します。
    *   例：パラメータが多すぎるメソッドにフラグを立てる、またはpublicメソッドにJavadocを強制する。

3.  **ワークフロー**:
    *   最初に Spotless (`mvn spotless:apply`) を実行してコードをフォーマットします。
    *   次に Checkstyle (`mvn checkstyle:check`) を実行して、追加のルールへの準拠を検証します。
    *   これにより、コードがフォーマットされ、かつより広範なスタイルガイドラインに従っていることが保証されます。

### `pom.xml` での設定例

以下は、`pom.xml` で両方のプラグインを設定する方法です：

```xml
<build>
    <plugins>
        <!-- フォーマットのための Spotless プラグイン -->
        <plugin>
            <groupId>com.diffplug.spotless</groupId>
            <artifactId>spotless-maven-plugin</artifactId>
            <version>2.43.0</version>
            <configuration>
                <java>
                    <includes>
                        <include>src/main/java/**/*.java</include>
                        <include>src/test/java/**/*.java</include>
                    </includes>
                    <palantirJavaFormat>
                        <version>2.53.0</version>
                        <style>GOOGLE</style> <!-- Google スタイルを使用 -->
                    </palantirJavaFormat>
                    <indent>
                        <spacesPerTab>2</spacesPerTab> <!-- 2スペースのインデント -->
                    </indent>
                    <importOrder>
                        <order>java,javax,org,com,\\#</order>
                    </importOrder>
                    <removeUnusedImports/>
                    <trimTrailingWhitespace/>
                    <endWithNewline/>
                </java>
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>apply</goal>
                    </goals>
                    <phase>validate</phase>
                </execution>
            </executions>
        </plugin>

        <!-- 検証のための Checkstyle プラグイン -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.4.0</version>
            <configuration>
                <configLocation>google_checks.xml</configLocation> <!-- Google スタイルまたはカスタム XML を使用 -->
                <includeTestSourceDirectory>true</includeTestSourceDirectory>
                <failOnViolation>true</failOnViolation> <!-- 違反時にビルドを失敗させる -->
                <consoleOutput>true</consoleOutput> <!-- 違反をコンソールに出力 -->
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>check</goal>
                    </goals>
                    <phase>validate</phase>
                </execution>
            </executions>
            <dependencies>
                <!-- Checkstyle のバージョンを指定 -->
                <dependency>
                    <groupId>com.puppycrawl.tools</groupId>
                    <artifactId>checkstyle</artifactId>
                    <version>10.17.0</version>
                </dependency>
            </dependencies>
        </plugin>
    </plugins>
</build>
```

### 設定に関する重要な注意点

1.  **共有されるスタイルルール**:
    *   競合を避けるために、Spotless と Checkstyle の設定を揃えてください。例えば、Spotless では `palantirJavaFormat` に `style>GOOGLE` を、Checkstyle では `google_checks.xml` を使用します。
    *   `google_checks.xml` は [Checkstyle の GitHub](https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml) からダウンロードするか、カスタムルールセットを作成してください。

2.  **実行順序**:
    *   検証の前にコードがフォーマットされるように、`validate` フェーズで Spotless を Checkstyle の前に実行します。
    *   例: `mvn spotless:apply checkstyle:check`.

3.  **カスタム Checkstyle ルール**:
    *   `google_checks.xml` をカスタマイズするか、独自のルール（例: `my_checks.xml`）を作成して、特定のルールを強制できます。例：
        ```xml
        <module name="Indentation">
            <property name="basicOffset" value="2"/>
            <property name="lineWrappingIndentation" value="4"/>
        </module>
        <module name="ImportOrder">
            <property name="groups" value="java,javax,org,com"/>
            <property name="ordered" value="true"/>
            <property name="separated" value="true"/>
        </module>
        ```

4.  **冗長性の回避**:
    *   Spotless がフォーマット（例：インデント、import順序）を処理する場合、重複するチェックを避けるために、該当する Checkstyle ルールを無効にしてください。例えば、Spotless がインデントを強制する場合は、Checkstyle の `Indentation` モジュールを無効にします：
        ```xml
        <module name="Indentation">
            <property name="severity" value="ignore"/>
        </module>
        ```

### どちらか一方を使用する場合と両方を使用する場合

*   **Spotless のみを使用**:
    *   一貫したコードフォーマット（例：インデント、import順序、空白）のみが必要な場合。
    *   厳格なスタイル強制なしで自動フォーマットを求めるチームに理想的。
    *   例：小規模プロジェクトやIDEベースのフォーマットを使用するチーム。

*   **Checkstyle のみを使用**:
    *   コードを修正せずにコーディング標準（例：命名規則、Javadoc、メソッドの複雑さ）を強制する必要がある場合。
    *   開発者が手動でコードをフォーマットするが、検証が必要なプロジェクトに適しています。

*   **両方を使用**:
    *   堅牢なコード品質のために：Spotless はコードを自動的にフォーマットし、Checkstyle は追加の問題（例：Javadocの欠落、複雑なメソッド）を検出します。
    *   大規模なチームや厳格なコーディング標準を要求するプロジェクトで一般的。
    *   例：一貫したスタイルと品質チェックを要求するエンタープライズプロジェクトやオープンソースリポジトリ。

### 実践的な考慮事項

*   **パフォーマンス**: 両方のプラグインを実行するとビルド時間が増加します。CIパイプラインでは、コードを修正せずに検証するために `spotless:check`（`apply` の代わりに）と `checkstyle:check` を使用します。
*   **IDE 統合**:
    *   Spotless: Spotless の Gradle/Maven タスクまたは IDE プラグイン（例：IntelliJ 用の `palantir-java-format`）を使用します。
    *   Checkstyle: 同じ `google_checks.xml` で設定された Checkstyle-IDEA プラグイン（IntelliJ 用）または Eclipse Checkstyle プラグインを使用します。
*   **CI/CD**: 両方のプラグインを CI パイプライン（例：Jenkins, GitHub Actions）で設定し、プルリクエストに対してフォーマットとスタイルチェックを強制します。
    ```yaml
    # GitHub Actions ワークフローの例
    name: CI
    on: [pull_request]
    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v3
          - name: Set up JDK 17
            uses: actions/setup-java@v3
            with: { java-version: '17' }
          - name: Run Spotless and Checkstyle
            run: mvn spotless:check checkstyle:check
    ```

### 潜在的な競合と解決策

*   **重複するルール**: Spotless のコードフォーマットが Checkstyle のルールと異なる場合（例：2スペース vs 4スペースのインデント）、ビルドが失敗する可能性があります。解決策：設定を揃える（例：両方で `GOOGLE` スタイルを使用）。
*   **ビルド失敗**: Spotless が実行されていない場合、Checkstyle の `failOnViolation` がビルドを中断させる可能性があります。解決策：Spotless が最初に実行されることを保証するか、フォーマットを検証するために `spotless:check` を使用します。
*   **チームの導入**: 開発者が自動フォーマットに抵抗する可能性があります。解決策：CI で `spotless:check` を使用し、チームに IDE 統合について教育します。

### 情報源

*   Spotless ドキュメント: [GitHub](https://github.com/diffplug/spotless/tree/main/plugin-maven)
*   Checkstyle Maven Plugin: [Maven Site](https://maven.apache.org/plugins/maven-checkstyle-plugin/)
*   Stack Overflow や GitHub issues でのコミュニティディスカッション

### 結論

Spotless と Checkstyle を併用することは、コード品質を維持するための強力な組み合わせです：Spotless は一貫したフォーマットを保証し、Checkstyle はより広範なコーディング標準を強制します。これらを（同じインデントやimport順序ルールなどで）揃えて設定し、ビルドプロセスで順次実行してください。プロジェクトがフォーマットのみを必要とする場合は、Spotless のみで十分かもしれません。厳格な検証が必要な場合は、Checkstyle の追加を検討してください。特定の設定やサンプルの `google_checks.xml` ファイルについてヘルプが必要な場合は、お知らせください！