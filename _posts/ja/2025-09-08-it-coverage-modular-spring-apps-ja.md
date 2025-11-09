---
audio: false
date: 2025-09-08
generated: true
image: false
lang: ja
layout: post
title: モジュラーSpringアプリのITカバレッジ
translated: true
type: note
---

### 現在のセットアップの総合評価
現在の構成は、このような小規模なマルチモジュールプロジェクトにとって堅牢です。特に、JettyにJaCoCoエージェントをアタッチし、Execプラグイン経由で外部Python統合テストを実行し、`PlaygroundWeb`モジュールでレポートを生成するというコアフローが既に機能している点は優れています。これにより、Pythonの`unittest`でテストされたAPIエンドポイントからのランタイムカバレッジを取得でき、Spring Webアプリケーションにおける統合テスト（IT）カバレッジにまさに必要な要件を満たしています。

主な強み：
- **モジュール化されフェーズに紐づいている**: Mavenフェーズの活用（Jetty起動に`pre-integration-test`、Pythonテストに`integration-test`、停止に`post-integration-test`、レポート生成に`verify`）により、信頼性と再現性が確保されています。
- **エージェントのアタッチ**: JettyのJVM引数（`-javaagent:...`）がランタイムを正しく計装し、カバレッジを`jacoco.it.exec`に記録しています。
- **外部テストの統合**: ExecプラグインがPythonを適切に扱い、テストをリポジトリルート（`${project.parent.basedir}/tests`）に配置することで、Javaモジュールから分離されています。
- **不必要な重複の排除**: `PlaygroundUtils`（コントローラーを持たない）でJetty/Pythonを実行しないため、効率的です。

ご自身で認識されている課題：
- **`PlaygroundUtils`のようなライブラリモジュールのカバレッジ**: ユーティリティコードは`PlaygroundWeb`のJVM内（WARの依存関係として）で実行されるため、計装され、`PlaygroundWeb`の`jacoco.it.exec`に記録されます。しかし、レポートはモジュール固有であるため、集約または包含されない限り`PlaygroundUtils`のカバレッジは表示されません。
- **JaCoCoの自己完結性の欠如**: Checkstyle/Spotless（これらはソース/静的アーティファクトを分析するだけ）とは異なり、JaCoCoは外部テストからのランタイムデータ（`.exec`ファイル）とエージェントのアタッチを必要とします。このため、注意深い調整なしではマルチモジュール構成では脆くなりがちです。
- **集約ゴールの制限**: `jacoco:report-aggregate`はモジュールごとの`.exec`ファイル（例：ユニットテストからのもの）を期待しますが、あなたのカバレッジは1つのモジュールでのITからのみ得られています。強制的に集約すると、`PlaygroundUtils`のようなライブラリで空のレポートが生成される可能性があります。
- **10+モジュールへのスケーラビリティ**: モジュール間でJetty/Pythonセットアップを複製することは（冗長なサーバー/テストとなり）非効率的です。`.exec`ファイルのコピーや全二重実行（ご指摘の通り）のようなハック的な回避策は、保守性の低下とビルド時間の肥大化を招きます。

モジュールごとのレポートへのフォールバックは現実的ですが、重複なしでカバレッジを含めるための最適化が可能です。

### 推奨戦略
アプリを実行するモジュール（ここでは`PlaygroundWeb`）で**単一の包括的なITカバレッジレポートを生成**すること、そして`PlaygroundUtils`のような**依存モジュールのカバレッジデータを含める**ことに焦点を当てます。これにより、テストの複数回実行を回避し、すべてのコードが1つのJVMで実行されるという事実を活用できます。

集約よりもこの方法が優れている理由：
- 集約（`report-aggregate`）は、モジュール間で分散されたユニットテストカバレッジには適していますが、単一ランタイムからのITカバレッジ（あなたのケース）には過剰で、自然にフィットしません。
- 統一されたレポートは、アプリのカバレッジを包括的に把握でき（例：「全体で80%、ただしユーティリティ層は60%」）、サイロ化されたモジュールごとのレポートよりも有用な場合が多いです。
- 大規模プロジェクトでは、「アプリモジュール」（WAR/EAR）をカバレッジのハブとして扱い、依存関係を取り込むことでスケールします。

#### 2モジュールプロジェクトへのステップバイステップ実装
小規模から始める：現在のセットアップ（1つのアプリモジュール + 1つのライブラリ）にこれを適用します。テストしてから拡張してください。

1. **IT実行を`PlaygroundWeb`のみに維持**:
   - ここは変更不要です。JettyがWAR（`PlaygroundUtils`を埋め込んだもの）を起動し、Pythonテストがエンドポイントにアクセスし、カバレッジが`${project.build.directory}/jacoco.it.exec`に記録されます。
   - ユーティリティコードが実行されていることを確認：Pythonテストが`PlaygroundUtils`クラス（例：`SystemUtils`）を使用するエンドポイントを呼び出す場合、そのカバレッジは`.exec`ファイルに含まれます。

2. **`PlaygroundWeb`のJaCoCoレポートを強化して`PlaygroundUtils`を含める**:
   - `report`ゴールでJaCoCoの`<additionalClassesDirectories>`と`<additionalSourceDirectories>`を使用します。これにより、JaCoCoは同じ`.exec`ファイルに対して`PlaygroundUtils`のクラス/ソースをスキャンします。
   - `PlaygroundWeb`のPOMを更新（`jacoco-maven-plugin`設定内）:

     ```xml
     <plugin>
         <groupId>org.jacoco</groupId>
         <artifactId>jacoco-maven-plugin</artifactId>
         <executions>
             <!-- 既存のprepare-agent -->
             <execution>
                 <id>prepare-agent</id>
                 <goals>
                     <goal>prepare-agent</goal>
                 </goals>
             </execution>
             <!-- 強化されたレポート: utilsモジュールを含める -->
             <execution>
                 <id>report-it</id>
                 <phase>verify</phase>
                 <goals>
                     <goal>report</goal>
                 </goals>
                 <configuration>
                     <dataFile>${jacoco.it.exec}</dataFile>
                     <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
                     <!-- PlaygroundUtilsのカバレッジを含めるために以下を追加 -->
                     <additionalClassesDirectories>
                         <directory>${project.parent.basedir}/PlaygroundUtils/target/classes</directory>
                     </additionalClassesDirectories>
                     <additionalSourceDirectories>
                         <directory>${project.parent.basedir}/PlaygroundUtils/src/main/java</directory>
                     </additionalSourceDirectories>
                 </configuration>
             </execution>
         </executions>
     </plugin>
     ```

   - これにより、両モジュールをカバーする単一のレポート（`PlaygroundWeb/target/site/jacoco-it`内）が生成されます。ユーティリティの`org.lzw`を含む、パッケージ/クラスごとの内訳が表示されます。

3. **`PlaygroundUtils`からのJaCoCoを無効化/削除**:
   - これ自体にはITがないため、JaCoCoの設定/プロパティ（例：`<jacoco.it.exec>`、`<it.report.skip>`）を削除します。自身のレポートを生成する必要はなく、カバレッジは上流で処理されます。
   - ユーティリティにユニットテストがある場合は、ユニットテストカバレッジ用に別個の`prepare-agent` + `report`（デフォルトの`jacoco.exec`用）を維持しますが、ITからは分離します。

4. **ビルドと検証**:
   - 親から`mvn clean verify`を実行します。
   - Jetty/Pythonは一度だけ（`PlaygroundWeb`内で）実行されます。
   - `PlaygroundWeb/target/site/jacoco-it/index.html`を確認：両モジュールのクラスのカバレッジが表示されるはずです。
   - ユーティリティのカバレッジが0%の場合は、Pythonテストがそれらのクラス（例：エンドポイント経由で`SystemUtils`をトリガーするテストを追加）を実行していることを確認してください。

5. **オプション: カバレッジしきい値の強制**:
   - `PlaygroundWeb`のJaCoCoプラグインに`check`実行を追加し、カバレッジがしきい値（例：全体のラインカバレッジ70%）を下回った場合にビルドを失敗させます。
     ```xml
     <execution>
         <id>check-it</id>
         <goals>
             <goal>check</goal>
         </goals>
         <configuration>
             <dataFile>${jacoco.it.exec}</dataFile>
             <rules>
                 <rule>
                     <element>BUNDLE</element>
                     <limits>
                         <limit>
                             <counter>LINE</counter>
                             <value>COVEREDRATIO</value>
                             <minimum>0.70</minimum>
                         </limit>
                     </limits>
                 </rule>
             </rules>
         </configuration>
     </execution>
     ```

#### 大規模プロジェクト（例：10モジュール）へのスケーリング
10以上のモジュール（例：複数のライブラリ + 1-2のアプリ/WARモジュール）の場合、複雑さを避けるために上記を拡張します：

- **アプリモジュールでのIT集中化**: 1つのメインWAR（`PlaygroundWeb`のような）がある場合、それを「カバレッジハブ」にします。すべての依存ライブラリに対して`<additionalClassesDirectories>`と`<additionalSourceDirectories>`を追加します（例：親POMでのループまたはプロパティリスト経由）。
  - 例：親プロパティでパスを定義:
    ```xml
    <properties>
        <lib1.classes>${project.basedir}/Lib1/target/classes</lib1.classes>
        <lib1.sources>${project.basedir}/Lib1/src/main/java</lib1.sources>
        <!-- 10ライブラリ分繰り返し -->
    </properties>
    ```
  - WARのJaCoCoレポート設定：これらを動的に参照。

- **複数のアプリ/WARがある場合**: WARに依存する専用のITモジュール（例：`App1-IT`、`App2-IT`）を作成し、そこでJetty/Exec/JaCoCoを設定し、関連する依存関係のクラス/ソースのみを含めます。これにより、ビルドがモジュール化された状態を保ちます（例：対象のカバレッジには`mvn verify -pl App1-IT`）。

- **モジュールごとのIT重複を回避**: ライブラリモジュールでJetty/Pythonを実行することは非効率的なので、絶対に避けてください。ライブラリが分離されたITを必要とする場合（稀）、それ用のミニサーバー/テストスイートを個別に与えます。

- **レポートのための集約（必要な場合）**: モジュールごとの個別レポートに固執する場合：
  - アプリモジュールで`.exec`を生成します。
  - 親の`post-integration-test`でMavenの`dependency:copy`またはカスタムスクリプト（Execプラグイン経由）を使用し、`.exec`を各ライブラリの`target/`に（例：`jacoco-it.exec`として）コピーします。
  - その後、各ライブラリで`report`を設定し、コピーされたファイルを使用します。
  - しかし、これはより複雑です。ステークホルダーがモジュールごとのメトリクスを要求しない限り、統一されたレポートを優先してください。

- **規模に対するツーリングのヒント**:
  - **Mavenプロファイル**: プロファイル（例：`-Pcoverage`）を使用して、より高速な開発ビルド用にIT/レポート生成を切り替えます。
  - **CI最適化**: CI（例：GitHub Actions）では、Mavenの依存関係をキャッシュし、テスト/エンドポイントへの変更時のみITを実行します。
  - **JaCoCoが複雑になりすぎた場合の代替案**: モジュール間でJaCoCoデータを取り込む集約分析のためにSonarQubeを検討してください。または、OpenCloverのようなランタイムツールに切り替えますが、ハブアプローチを守るならJaCoCoで十分です。
  - **テストのテスト**: Pythonにスモークテストを追加し、サーバー起動を検証します（例：`http://localhost:8080/health`をポーリング）。

この戦略は、実行回数を最小化（アプリごとに1回のJetty/Python実行）し、JaCoCoの依存関係をクリーンに扱い、爆発することなくスケールします。詳細（例：エンドポイントでユーティリティがどのように使用されているか）を共有いただければ、POMスニペットをさらに改良できます。