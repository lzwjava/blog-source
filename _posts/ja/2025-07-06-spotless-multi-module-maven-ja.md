---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: マルチモジュールMavenプロジェクトにおけるスポットレス
translated: true
type: note
---

### マルチモジュール Maven プロジェクトにおける Spotless

Spotless は Maven と Gradle の両方で利用可能なコードフォーマットプラグインです。Maven の `-pl` (プロジェクトリスト) フラグについて言及されていることから、**Spotless Maven プラグイン**をマルチモジュールの Java プロジェクトで使用していると想定します。これにより、フォーマットチェック (例: `spotless:check`) や修正の適用 (例: `spotless:apply`) を特定のモジュールに対して選択的に実行でき、大規模なプロジェクトにおいて (例えば特定のサブモジュールでの開発中に) 特定のモジュールのみをフォーマットする必要がある場合に効率的です。

#### 前提条件
-   プロジェクトが Maven を使用し、マルチモジュール構造であること (親 `pom.xml` で `<modules>...</modules>` として定義されている)。
-   Spotless Maven プラグインがプロジェクトで設定されていること (通常は親 POM または個々のモジュールの POM に記述)。設定されていない場合は、以下のように POM に追加してください:
    ```xml
    <build>
      <plugins>
        <plugin>
          <groupId>com.diffplug.spotless</groupId>
          <artifactId>spotless-maven-plugin</artifactId>
          <version>2.43.0</version>  <!-- 最新バージョンを使用してください -->
          <configuration>
            <!-- ここにフォーマットルールを記述 (例: Java, Groovy 用) -->
          </configuration>
        </plugin>
      </plugins>
    </build>
    ```
    -   一般的なルールには、Google Java Format、Eclipse JDT (Java 用)、またはインポートやスペースに関するカスタマイズなどがあります。
    -   Spotless は多くのファイルタイプ (Java, Kotlin, XML など) をサポートし、CI ツールとの連携も良好です (コミット前フックとして `spotless:check` ゴールを使用し、フォーマットされていないコードがある場合にビルドを失敗させることができます)。

#### モジュールのフォーマットを制御する `-pl` の使用
Maven の `-pl` (プロジェクトリスト) フラグを使用すると、ビルド/プラグイン実行に含めるモジュールのカンマ区切りリストを指定できます。デフォルトでは Maven は全てのモジュールで実行されますが、`-pl` を使用することで実行を制限し、影響を受けないモジュールでの不要な作業を避けて時間を節約できます。

-   **基本的なコマンド構造**:
    -   フォーマットをチェックする場合 (変更を適用せず): `mvn spotless:check -pl module1,module2`
    -   フォーマット修正を適用する場合: `mvn spotless:apply -pl module1,module2`
    -   `module1,module2` は実際のモジュール名 (例: ルートからの相対パス、`core,api` など) に置き換えてください。

-   **例**:
    1.  **`core` モジュールのみでフォーマットをチェック**:
        ```
        mvn spotless:check -pl core
        ```
        -   これは `core` のソースファイルのみをスキャンして検証します。フォーマットに問題がある場合、ビルドは詳細情報 (例: "修正するには `spotless:apply` を実行してください") とともに失敗します。

    2.  **複数のモジュール (`api` と `utils`) にフォーマットを適用**:
        ```
        mvn spotless:apply -pl api,utils
        ```
        -   これはファイルをその場で修正し、Spotless のルールに合わせます。変更後は、バージョン管理で予期せぬ問題が発生しないように、必ず変更をコミットしてください。

    3.  **プロジェクト全体の実行時に特定のモジュールを除外**: `-pl !moduleToSkip` を使用して、特定のモジュールを*除く*全てのモジュールで実行します (Maven 3.2.1+ は `!` による否定をサポート)。
        -   例: `mvn spotless:check -pl !legacy` (`legacy` を除く全てのモジュールで実行)。

-   **効率化のためのヒント**:
    -   **並列実行**: マルチスレッドビルドのために `-T 4` を追加 (例: `mvn spotless:check -pl core,api -T 4`)。
    -   **Dry Run**: 変更を加える前に `spotless:check` を使用して問題をプレビューできます。これは冪等で安全です。
    -   **IDE/バージョン管理との連携**: IDE (例: IntelliJ の Spotless プラグイン経由) で保存時/コミット時に Spotless が実行されるように設定するか、自動チェックのために (pre-commit や Git フックなどのツールを使用して) コミット前フックとして使用します。
    -   **リアクター解決の扱い**: モジュールの依存関係が複雑な場合、Maven は `-pl` 使用時にそれらを自動的に解決し、必要に応じて依存モジュールが先に処理されるようにします。
    -   **一般的な問題**:
        -   `-pl` が機能しない場合は、モジュールが `<modules>` で定義されていることを確認し、あいまいさがある場合は完全修飾パスを使用してください (例: マルチリポジトリ設定の場合 `-pl :core`)。
        -   Gradle ユーザーの場合 (Spotless Gradle プラグインを意図していた場合)、同等の機能はプロジェクトパスに対する `-p` ですが、お問い合わせでは `-pl` が指定されているため、Maven を想定しています。Gradle の場合は、`gradle task -p submodule` のようなプラグインに切り替えてください。

詳細なドキュメントについては、[Spotless Maven Plugin ドキュメント](https://github.com/diffplug/spotless/tree/v2.43.0/plugin-maven)を参照してください。設定が異なる場合 (例: Gradle) は、詳細を提供していただければ、より適切なアドバイスを差し上げます。