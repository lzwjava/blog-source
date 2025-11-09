---
audio: false
date: 2025-09-08
generated: true
image: false
lang: ja
layout: post
title: PythonテストのためのJaCoCoカバレッジ戦略
translated: true
type: note
---

# Python統合テストを用いたJaCoCoカバレッジの分析と戦略

## 現状分析

以下の構成でマルチモジュールMavenプロジェクトを設定しています：
- 親POM（`PlaygroundLib`）
- `PlaygroundUtils`モジュール（ユーティリティクラスを含むJAR）
- `PlaygroundWeb`モジュール（Spring MVCコントローラーを含むWAR）

目標は、Pythonの`unittest`を使用してAPIエンドポイントをテストし、Javaコードのカバレッジレポートを生成することです。課題は、PythonテストがJavaプロジェクトの外部に存在し、テスト中にJettyを実行してアプリケーションを提供する必要があることです。

## 現在のアプローチの問題点

1. **複数回実行の問題**：異なるモジュールに対して個別のカバレッジレポートを生成するために`PlaygroundWeb`を複数回実行しており、非効率的です。

2. **スケーラビリティの懸念**：このアプローチはモジュールが増えると拡張性に欠けます。10モジュールのプロジェクトでは10回の個別実行が必要になります。

3. **カバレッジの断片化**：モジュール単位のレポートでは、アプリケーション全体にわたるカバレッジの包括的な視点を得ることが困難です。

## 推奨戦略

### 1. 統合カバレッジ収集アプローチ

アプリケーションを複数回実行する代わりに、以下を推奨します：

1. **Webアプリケーションを1回実行**し、JaCoCoエージェントを接続
2. **すべてのPython統合テストを実行**し、この単一インスタンスに対して実施
3. **統合カバレッジレポートを生成**し、すべてのモジュールを含める

このアプローチはより効率的で、アプリケーション全体にわたる統一されたカバレッジ視点を提供します。

### 2. 実装手順

#### 親POM（`PlaygroundLib`）の修正

JaCoCoを使用した統合テスト用のプロファイルを追加：

```xml
<profiles>
    <profile>
        <id>integration-test</id>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.jacoco</groupId>
                    <artifactId>jacoco-maven-plugin</artifactId>
                    <executions>
                        <execution>
                            <id>merge</id>
                            <phase>post-integration-test</phase>
                            <goals>
                                <goal>merge</goal>
                            </goals>
                            <configuration>
                                <fileSets>
                                    <fileSet>
                                        <directory>${project.basedir}</directory>
                                        <includes>
                                            <include>*/target/jacoco-it.exec</include>
                                        </includes>
                                    </fileSet>
                                </fileSets>
                                <destFile>${project.build.directory}/jacoco-merged.exec</destFile>
                            </configuration>
                        </execution>
                        <execution>
                            <id>report-merged</id>
                            <phase>verify</phase>
                            <goals>
                                <goal>report</goal>
                            </goals>
                            <configuration>
                                <dataFile>${project.build.directory}/jacoco-merged.exec</dataFile>
                                <outputDirectory>${project.reporting.outputDirectory}/jacoco-merged</outputDirectory>
                            </configuration>
                        </execution>
                    </executions>
                </plugin>
            </plugins>
        </build>
    </profile>
</profiles>
```

#### PlaygroundWeb POMの修正

すべてのモジュールを含むようにJaCoCoエージェント設定を修正：

```xml
<plugin>
    <groupId>org.eclipse.jetty</groupId>
    <artifactId>jetty-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>start-jetty</id>
            <phase>pre-integration-test</phase>
            <goals>
                <goal>start</goal>
            </goals>
            <configuration>
                <daemon>true</daemon>
                <jvmArgs>
                    -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${project.build.directory}/jacoco-it.exec,includes=org.lzw.*
                </jvmArgs>
                <!-- その他の設定は変更なし -->
            </configuration>
        </execution>
        <!-- その他のexecutionは変更なし -->
    </executions>
</plugin>
```

JaCoCoエージェント設定に`includes=org.lzw.*`を追加している点に注意してください。これにより、`org.lzw`パッケージ内のすべてのクラス（すべてのモジュールにわたる）がカバレッジレポートに含まれます。

### 3. 実行フロー

推奨される実行フロー：

```bash
# すべてのモジュールをビルド
mvn clean install

# カバレッジ付きで統合テストを実行
mvn verify -Pintegration-test
```

これにより以下が実行されます：
1. すべてのモジュールのコンパイル
2. JaCoCoエージェント接続でJettyを起動
3. Python統合テストの実行
4. Jettyの停止
5. すべてのモジュールの統合カバレッジレポートの生成

### 4. 大規模プロジェクトへの拡張

10モジュールの大規模プロジェクトの場合：

1. **Webモジュール**（`PlaygroundWeb`など）は、JaCoCoエージェント接続でアプリケーションを実行するように設定されます。
2. **ユーティリティモジュール**（`PlaygroundUtils`など）は特別な設定を必要としません。
3. 親POMはすべてのモジュールからのカバレッジデータのマージを処理します。

独立してテストする必要がある複数のWebモジュールがある場合は、各Webモジュール用に個別のMavenプロファイルを作成し、それぞれに対して統合テストを個別に実行してから、親レベルですべてのカバレッジデータをマージできます。

### 5. JaCoCoの複雑さへの対応

JaCoCoの複雑さを管理するために：

1. **設定をカプセル化**し、メインPOMをクリーンに保つためにMavenプロファイルを使用
2. **プロセスを明確に文書化**し、チームメンバーがテスト実行とレポート生成方法を理解できるように
3. **CI/CD自動化を検討**し、開発者の手動作業の複雑さを軽減

## まとめ

推奨アプローチは、JaCoCoエージェント接続でWebアプリケーションを1回実行し、すべてのPython統合テストをこのインスタンスに対して実行し、統合カバレッジレポートを生成することで、カバレッジ収集を統合します。このアプローチはより効率的で、スケーラブルであり、アプリケーション全体にわたる統一されたカバレッジ視点を提供します。

この戦略は現在の課題を解決し、プロジェクトの成長に合わせて適切に拡張され、JaCoCoの複雑さの管理も簡素化するはずです。