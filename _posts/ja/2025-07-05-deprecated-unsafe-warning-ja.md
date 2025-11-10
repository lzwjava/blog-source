---
audio: false
generated: true
lang: ja
layout: post
title: Guiceのアップグレードによる安全でない警告の修正
translated: true
type: note
---

表示されている警告:

```
WARNING: A terminally deprecated method in sun.misc.Unsafe has been called
WARNING: sun.misc.Unsafe::staticFieldBase has been called by com.google.inject.internal.aop.HiddenClassDefiner (file:/opt/homebrew/Cellar/maven/3.9.10/libexec/lib/guice-5.1.0-classes.jar)
WARNING: Please consider reporting this to the maintainers of class com.google.inject.internal.aop.HiddenClassDefiner
WARNING: sun.misc.Unsafe::staticFieldBase will be removed in a future release
```

これは**Java Virtual Machine (JVM) からの警告**であり、直接あなたのコードから出ているものではありません。これは、使用しているライブラリ（この場合は Guice、具体的には `guice-5.1.0-classes.jar`）が内部的に `sun.misc.Unsafe` のメソッド（`staticFieldBase`）を呼び出していることを意味します。

`sun.misc.Unsafe` は Java の内部 API であり、JDK 自体内部での低レベル操作を目的としています。これは標準的な Java API の一部ではなく、不安定または未定義の動作を引き起こす可能性があり、将来の Java リリースで変更または削除される可能性があるため、その使用は推奨されていません。JVM は、この特定のメソッドが「最終的に非推奨」となり削除される予定であるため、ライブラリが代替手段なしに使い続けると最終的にアプリケーションが壊れる可能性があることを警告しています。

**この警告を「削除」する方法:**

この使用はサードパーティライブラリ（Guice）内にあるため、コードを変更して直接「削除」することはできません。以下に、優先順位の高い順に対処法を示します:

1.  **Guice のアップグレード (最も推奨):**
    最善かつ持続可能な解決策は、`sun.misc.Unsafe` を使用しなくなった、または標準的な Java API（JDK 9 で導入された `VarHandle` や JDK 22 で標準化された Foreign Function & Memory API (JEP 454) など）に移行した新しいバージョンの Guice にアップグレードすることです。

    バージョン `guice-5.1.0-classes.jar` を見ると、Guice 5.1.0 を使用しているようです。公式の Guice リリースとそのドキュメントを確認し、新しい Java バージョンでの `sun.misc.Unsafe` の使用に特化して対応している更新がないか調べてください。多くの場合、ライブラリのメンテナーはこれらの非推奨化を認識しており、更新されたバージョンを提供しています。

    *   **アクション:** 新しい Guice バージョンを使用するように `pom.xml` を変更します。あなたの Java バージョン（あなたの場合は JDK 21）と互換性のある最新の安定版 Guice を見つける必要があります。

    ```xml
    <dependency>
        <groupId>com.google.inject</groupId>
        <artifactId>guice</artifactId>
        <version>LATEST_GUICE_VERSION</version> </dependency>
    ```

    プロジェクトが使用している場合は、`guice-assistedinject` や他の Guice モジュールを含める必要があるかもしれません。

2.  **警告の抑制 (一時的な回避策 - 長期的には非推奨):**
    長期的にこれに依存すべきではありませんが、警告が純粋に見た目上のものであり、*当面の間*アプリケーションの機能を妨げないのであれば、実行時に警告を抑制することができます。これは JVM のコマンドライン引数で行います。

    JDK 24（あなたの現在のターゲットは 21 ですが、Java が進化するにつれて知っておくと良い情報です）では、デフォルトは `warn` です。これを抑制するには、明示的に `allow` に設定できます:

    これを `exec-maven-plugin` の設定に追加できます:

    ```xml
    <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>exec-maven-plugin</artifactId>
        <version>3.5.0</version>
        <configuration>
            <executable>bash</executable>
            <arguments>
                <argument>-c</argument>
                <argument>java --add-opens java.base/sun.misc=ALL-UNNAMED --sun-misc-unsafe-memory-access=allow -cp ${project.build.directory}/classes com.lzw.solutions.uva.${problem}.Main &lt; src/main/resources/uva/${problem}/1.in</argument>
            </arguments>
        </configuration>
    </plugin>
    ```

    *自己修正:* 主な警告は「Illegal reflective access」についてではなく、`sun.misc.Unsafe::staticFieldBase` が「最終的に非推奨」であることについてです。したがって、`--add-opens java.base/sun.misc=ALL-UNNAMED` は、「Illegal reflective access」の警告も受け取っていない限り、ここでは必要ないかもしれません。「最終的に非推奨」の警告に対するより直接的なフラグは `--sun-misc-unsafe-memory-access=allow` です。

    **しかし、これは一時的な修正です。** このフラグは、警告を出力せずに `sun.misc.Unsafe` メソッドの使用を許可するよう JVM に指示するだけです。これは、`sun.misc.Unsafe` が最終的に削され、将来の JDK バージョンでアプリケーションが壊れる可能性があるという根本的な問題を*解決しません*。

3.  **Guice メンテナーへの報告 (警告自体によって提案済み):**
    警告自体が「`com.google.inject.internal.aop.HiddenClassDefiner` のメンテナーに報告することを検討してください」と提案しています。あなたは特定のバージョンを使用していますが、この問題が最新の Guice バージョンでも持続することを確認できれば（おそらくそうではないはずですが、彼らはこれらに対処する傾向があります）、それを報告することはコミュニティにとって有益です。

**まとめると、最善の対応は Guice の依存関係をアップグレードすることです。** `sun.misc.Unsafe` API は移り変わる対象であり、ライブラリは Java が提供する新しい、より安全で、公式にサポートされた API に適応する必要があります。