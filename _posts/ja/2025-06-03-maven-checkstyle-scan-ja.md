---
audio: false
generated: true
lang: ja
layout: post
title: 'Maven Checkstyle: スキャン継続'
translated: true
type: note
---

`mvn checkstyle:check` が違反を検出しても早期に失敗せず、すべてのモジュールのスキャンを継続するようにするには、Checkstyle Maven プラグインの `failOnViolation` オプションを無効に設定する必要があります。デフォルトでは `failOnViolation` は `true` に設定されているため、違反が検出されるとビルドが停止します。これを `false` に設定すると、ビルドを停止することなくすべてのモジュールのスキャンが完了し、すべての違反が報告されます。

### 解決策
`pom.xml` を以下のように更新して Checkstyle プラグインを設定します:

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-checkstyle-plugin</artifactId>
      <version>3.3.1</version> <!-- 最新バージョンを使用 -->
      <configuration>
        <failOnViolation>false</failOnViolation>
        <logViolationsToConsole>true</logViolationsToConsole> <!-- オプション: 違反をコンソールに出力 -->
      </configuration>
      <executions>
        <execution>
          <id>checkstyle</id>
          <phase>validate</phase> <!-- または希望のフェーズ -->
          <goals>
            <goal>check</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

### 説明
- **`<failOnViolation>false</failOnViolation>`**: この設定により、Checkstyle 違反が検出されてもビルドが失敗せず、すべてのモジュールのスキャンが継続されます。
- **`<logViolationsToConsole>true</logViolationsToConsole>`**: (オプション) ビルドが失敗しない場合でも、違反がコンソールに出力されて可視化されます。
- **実行フェーズ**: `<phase>validate</phase>` は Checkstyle チェックを Maven ライフサイクルの `validate` フェーズにバインドします。異なる段階（例: `compile`, `verify`）で実行したい場合はフェーズを調整してください。

### コマンドの実行
以下のコマンドを再度実行します:
```bash
mvn checkstyle:check
```
`failOnViolation` を `false` に設定すると、Maven はすべてのモジュールをスキャンし、すべての違反を報告し、早期に停止することなくビルドを完了します。

### 注意点
- `maven-checkstyle-plugin` の最近のバージョン（例示の 3.3.1 など）を使用していることを確認してください。必要に応じて Maven Central で最新バージョンを確認してください。
- マルチモジュールプロジェクトで作業している場合、この設定は子 `pom.xml` で上書きされない限り、すべてのモジュールに適用されます。
- 違反のレポートを生成するには、デフォルトではビルドを失敗させずに HTML レポートを生成する `mvn checkstyle:checkstyle` の実行を検討してください。

特定の要件（カスタム Checkstyle ルールや異なる設定など）がある場合は、お知らせください。さらにソリューションを調整いたします。