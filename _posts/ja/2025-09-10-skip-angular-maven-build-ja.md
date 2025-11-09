---
audio: false
date: 2025-09-10
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: MavenでのAngularビルドのスキップ
translated: true
type: note
---

短い答え: はい — Angular/npm ビルドをスキップできますが、`--skip-web` のような組み込みフラグではできません。以下のいずれかのアプローチを使用してください。

### 1) マルチモジュールビルドで web モジュールを除外する

Angular アプリが独自の Maven モジュール（例: `web`）である場合、リアクターでそれを除外するだけです:

```
mvn -pl '!web' -am clean package
```

または、バックエンドモジュールのみをビルドします:

```
mvn -pl :backend -am clean package
```

（`-am` は必要な依存関係をビルドします; `!web` 構文はそのモジュールを除外します。）

### 2) 「フロントエンドをスキップ」プロパティを追加する (frontend-maven-plugin または exec で動作)

npm ゴールをプロパティでガードし、コマンドラインから切り替えます。

**POM (web モジュールまたは親):**

```xml
<properties>
  <skip.frontend>false</skip.frontend>
</properties>

<build>
  <plugins>
    <!-- 例: com.github.eirslett:frontend-maven-plugin -->
    <plugin>
      <groupId>com.github.eirslett</groupId>
      <artifactId>frontend-maven-plugin</artifactId>
      <version>...your version...</version>
      <configuration>
        <skip>${skip.frontend}</skip>
      </configuration>
      <executions>
        <execution>
          <id>npm-build</id>
          <phase>prepare-package</phase>
          <goals>
            <goal>npm</goal>
          </goals>
          <configuration>
            <arguments>run build</arguments>
          </configuration>
        </execution>
      </executions>
    </plugin>

    <!-- exec-maven-plugin を使用して npm を呼び出す場合 -->
    <plugin>
      <groupId>org.codehaus.mojo</groupId>
      <artifactId>exec-maven-plugin</artifactId>
      <version>...your version...</version>
      <executions>
        <execution>
          <id>npm-build</id>
          <phase>prepare-package</phase>
          <goals><goal>exec</goal></goals>
          <configuration>
            <skip>${skip.frontend}</skip>
            <executable>npm</executable>
            <arguments>
              <argument>run</argument>
              <argument>build</argument>
            </arguments>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

**CLI:**

```
mvn -Dskip.frontend=true clean package
```

### 3) Maven プロファイルを使用する

フロントエンドビルドを「with-frontend」プロファイルにのみバインドし、開発時にはデフォルトで「skip-frontend」プロファイルを使用します。

**POM:**

```xml
<profiles>
  <profile>
    <id>with-frontend</id>
    <activation>
      <property>
        <name>!skip.frontend</name>
      </property>
    </activation>
    <build>
      <plugins>
        <!-- 上記と同じプラグイン設定（skip なし） -->
      </plugins>
    </build>
  </profile>
</profiles>
```

**CLI:**

* 通常 (スキップ): `mvn -Dskip.frontend clean package`
* リリース (UI ビルド): `mvn -Pwith-frontend clean package`

---

## UI をビルド *する* 場合の高速化のヒント

* Angular の永続キャッシュが有効になっていることを確認してください (Angular CLI はデフォルトでキャッシュします; CI で `node_modules` と `.angular/cache` をキャッシュされた状態に保ちます)。
* リリース時のみ `ng build` を実行します; 開発時には UI を別途サーブし (`npm start`)、Spring には事前ビルドされた静的アセットをサーブさせます (例えば、パッケージ化ビルド用に `dist/` を `src/main/resources/static` の下に配置します)。
* リポジトリを分割して、Angular アプリが Maven モジュールにならないようにすることを検討してください; フロントエンドファイルが変更されたときのみビルドします。
* 最近の Angular を使用している場合、デフォルトの esbuild/Vite ビルダーを使用し、CI リリースビルドではソースマップを無効にしたままにします。

---

### 結論

web モジュールを除外するには `-pl '!web'` を使用するか、**または** `skip.frontend` プロパティを追加して、プラグインの実行がそれを尊重するように設定します。標準の `mvn package --skip-web` はありませんが、上記の 2 つのパターンは信頼性が高く一般的です。