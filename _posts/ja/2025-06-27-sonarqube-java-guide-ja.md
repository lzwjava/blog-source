---
audio: false
generated: true
lang: ja
layout: post
title: JavaとSpringプロジェクトのためのSonarQubeマスタリング
translated: true
type: note
---

# JavaとSpringプロジェクトでのSonarQube活用包括的ガイド

## はじめに
SonarQubeはコード品質を継続的に検査するためのオープンソースプラットフォームです。静的コード解析を行い、バグ、コードスメル、脆弱性を検出し、コードカバレッジを計算します。このガイドでは、Java SpringプロジェクトでのSonarQubeのセットアップと使用方法について、インストール、設定、統合、ベストプラクティスを含め包括的に解説します。

## 目次
1. [SonarQubeとは？](#sonarqubeとは)
2. [前提条件](#前提条件)
3. [SonarQubeのインストール](#sonarqubeのインストール)
4. [Java Springプロジェクトの設定](#java-springプロジェクトの設定)
5. [プロジェクトへのSonarQube設定](#プロジェクトへのsonarqube設定)
6. [SonarQube解析の実行](#sonarqube解析の実行)
7. [SonarQube結果の解釈](#sonarqube結果の解釈)
8. [ベストプラクティス](#ベストプラクティス)
9. [一般的な問題のトラブルシューティング](#一般的な問題のトラブルシューティング)
10. [まとめ](#まとめ)

## SonarQubeとは？
SonarQubeは、以下のためのソースコード解析を通じて継続的なコード品質検査を提供するツールです：
- **バグ**: コード内の潜在的なエラー
- **コードスメル**: 技術的負債につながる可能性のある保守性の問題
- **脆弱性**: 悪用される可能性のあるセキュリティ問題
- **コードカバレッジ**: 単体テストでカバーされるコードの割合
- **重複**: リファクタリング可能な重複コードブロック

Javaを含む複数の言語をサポートし、MavenやGradleなどのビルドツールやCI/CDパイプラインとシームレスに統合します。

## 前提条件
SonarQubeをセットアップする前に、以下を確認してください：
- **Java Development Kit (JDK)**: バージョン11以降（SonarQubeはJava 11または17が必要）
- **MavenまたはGradle**: Java Springプロジェクト用のビルドツール
- **SonarQubeサーバー**: バージョン9.9 LTS以降（ほとんどのユースケースではCommunity Editionで十分）
- **SonarScanner**: 解析を実行するCLIツール
- **データベース**: SonarQubeはデータベースが必要（例：PostgreSQL、MySQL、またはテスト用の組み込みH2）
- **Springプロジェクト**: 動作するSpring BootまたはSpring Frameworkプロジェクト
- **IDE**: 開発用のIntelliJ IDEA、Eclipse、またはVS Code

## SonarQubeのインストール

### ステップ1: SonarQubeのダウンロードとインストール
1. **SonarQubeのダウンロード**:
   - [SonarQubeダウンロードページ](https://www.sonarqube.org/downloads/)にアクセス
   - ニーズに基づいてCommunity Edition（無料）または他のエディションを選択
   - ZIPファイル（例：`sonarqube-9.9.0.zip`）をダウンロード

2. **ZIPの展開**:
   - ダウンロードしたファイルをディレクトリに展開（例：`/opt/sonarqube` または `C:\sonarqube`）

3. **データベースの設定**:
   - SonarQubeはデータベースを必要とします。本番環境ではPostgreSQLまたはMySQLを使用。テストには組み込みH2データベースで十分
   - PostgreSQLの例：
     - PostgreSQLをインストールし、データベースを作成（例：`sonarqube`）
     - SonarQube設定ファイル（`conf/sonar.properties`）を更新：
       ```properties
       sonar.jdbc.url=jdbc:postgresql://localhost:5432/sonarqube
       sonar.jdbc.username=sonarqube_user
       sonar.jdbc.password=sonarqube_pass
       ```

4. **SonarQubeの起動**:
   - SonarQubeディレクトリ（`bin/<platform>`）に移動
   - 起動スクリプトを実行：
     - Linux/Mac: `./sonar.sh start`
     - Windows: `StartSonar.bat`
   - `http://localhost:9000`（デフォルトポート）でSonarQubeにアクセス

5. **ログイン**:
   - デフォルト認証情報：`admin/admin`
   - 初回ログイン後にパスワードを変更

### ステップ2: SonarScannerのインストール
1. **SonarScannerのダウンロード**:
   - [SonarQube Scannerページ](https://docs.sonarqube.org/latest/analyzing-source-code/scanners/sonarscanner/)からダウンロード
   - ディレクトリに展開（例：`/opt/sonar-scanner`）

2. **環境変数の設定**:
   - PATHにSonarScannerを追加：
     - Linux/Mac: `export PATH=$PATH:/opt/sonar-scanner/bin`
     - Windows: システムPATHに `C:\sonar-scanner\bin` を追加

3. **インストールの確認**:
   - `sonar-scanner --version` を実行してインストールを確認

## Java Springプロジェクトの設定
このガイドでは、Mavenを使用したSpring Bootプロジェクトを使用します。Gradleまたは非Boot Springプロジェクトでも手順は同様です。

1. **Spring Bootプロジェクトの作成**:
   - [Spring Initializer](https://start.spring.io/)を使用してプロジェクトを作成：
     - 依存関係：Spring Web、Spring Data JPA、H2 Database、Spring Boot Starter Test
     - ビルドツール：Maven
   - プロジェクトをダウンロードして展開

2. **単体テストの追加**:
   - コードカバレッジを測定するためにプロジェクトに単体テストがあることを確認
   - テストクラスの例：
     ```java
     import org.junit.jupiter.api.Test;
     import org.springframework.boot.test.context.SpringBootTest;

     @SpringBootTest
     public class ApplicationTests {
         @Test
         void contextLoads() {
         }
     }
     ```

3. **コードカバレッジ用にJacocoを追加**:
   - コードカバレッジレポートを生成するためにJaCoCo Mavenプラグインを `pom.xml` に追加：
     ```xml
     <plugin>
         <groupId>org.jacoco</groupId>
         <artifactId>jacoco-maven-plugin</artifactId>
         <version>0.8.8</version>
         <executions>
             <execution>
                 <goals>
                     <goal>prepare-agent</goal>
                 </goals>
             </execution>
             <execution>
                 <id>report</id>
                 <phase>test</phase>
                 <goals>
                     <goal>report</goal>
                 </goals>
             </execution>
         </executions>
     </plugin>
     ```

## プロジェクトへのSonarQube設定

1. **SonarQubeプロジェクトの作成**:
   - SonarQube（`http://localhost:9000`）にログイン
   - **Create Project** > **Manually** をクリック
   - **Project Key**（例：`my-spring-project`）と **Display Name** を入力
   - 認証用トークンを生成（例：`my-token`）

2. **`sonar-project.properties`の設定**:
   - Springプロジェクトのルートに `sonar-project.properties` ファイルを作成：
     ```properties
     sonar.projectKey=my-spring-project
     sonar.projectName=My Spring Project
     sonar.host.url=http://localhost:9000
     sonar.token=my-token
     sonar.java.binaries=target/classes
     sonar.sources=src/main/java
     sonar.tests=src/test/java
     sonar.junit.reportPaths=target/surefire-reports
     sonar.jacoco.reportPaths=target/jacoco.exec
     sonar.sourceEncoding=UTF-8
     ```

3. **Maven統合（代替方法）**:
   - `sonar-project.properties` の代わりに `pom.xml` でSonarQubeを設定：
     ```xml
     <properties>
         <sonar.host.url>http://localhost:9000</sonar.host.url>
         <sonar.token>my-token</sonar.token>
         <sonar.projectKey>my-spring-project</sonar.projectKey>
         <sonar.projectName>My Spring Project</sonar.projectName>
     </properties>
     <build>
         <plugins>
             <plugin>
                 <groupId>org.sonarsource.scanner.maven</groupId>
                 <artifactId>sonar-maven-plugin</artifactId>
                 <version>3.9.1.2184</version>
             </plugin>
         </plugins>
     </build>
     ```

## SonarQube解析の実行

1. **SonarScannerの使用**:
   - プロジェクトルートに移動
   - 実行：
     ```bash
     sonar-scanner
     ```
   - 解析前にテストが実行されていることを確認（Mavenプロジェクトでは `mvn test`）

2. **Mavenの使用**:
   - 実行：
     ```bash
     mvn clean verify sonar:sonar
     ```
   - このコマンドはコードをコンパイルし、テストを実行し、カバレッジレポートを生成し、結果をSonarQubeに送信

3. **結果の確認**:
   - SonarQube（`http://localhost:9000`）を開き、プロジェクトに移動
   - ダッシュボードで解析結果を確認

## SonarQube結果の解釈
SonarQubeダッシュボードは以下を提供します：
- **概要**: 問題、カバレッジ、重複のサマリー
- **問題**: 重大度（ブロッカー、クリティカル、メジャーなど）別のバグ、脆弱性、コードスメルのリスト
- **コードカバレッジ**: テストでカバーされるコードの割合（JaCoCo経由）
- **重複**: 重複コードブロック
- **品質ゲート**: 事前定義されたしきい値（例：カバレッジ > 80%）に基づく合格/不合格ステータス

### アクション例：
- **バグの修正**: nullポインタデリファレンスなどの重大な問題に対処
- **コードスメルのリファクタリング**: 複雑なメソッドの簡素化や未使用コードの削除
- **カバレッジの改善**: カバーされていないコードに対する追加の単体テストを作成

## ベストプラクティス
1. **CI/CDとの統合**:
   - CI/CDパイプライン（Jenkins、GitHub Actionsなど）にSonarQube解析を追加
   - GitHub Actionsワークフローの例：
     ```yaml
     name: CI with SonarQube
     on: [push]
     jobs:
       build:
         runs-on: ubuntu-latest
         steps:
           - uses: actions/checkout@v3
           - name: Set up JDK 11
             uses: actions/setup-java@v3
             with:
               java-version: '11'
           - name: Build and Analyze
             run: mvn clean verify sonar:sonar -Dsonar.host.url=http://localhost:9000 -Dsonar.token=${{ secrets.SONAR_TOKEN }}
     ```

2. **品質ゲートの定義**:
   - SonarQubeでコードカバレッジ、バグ、脆弱性のしきい値を設定
   - 例：カバレッジ < 80% または重大な問題がある場合にビルドを失敗

3. **SonarLintの使用**:
   - IDE（IntelliJ IDEAなど）にSonarLintプラグインをインストールし、開発中に問題を検出

4. **定期的な解析**:
   - すべてのコミットまたは毎日SonarQube解析を実行し、問題を早期に発見

5. **ルールのカスタマイズ**:
   - プロジェクトのニーズに合わせてSonarQubeルールを調整（無関係なルールを無効化したり、カスタムルールを追加）

## 一般的な問題のトラブルシューティング
1. **解析のアップロード失敗**:
   - 設定の `sonar.host.url` と `sonar.token` を確認
   - SonarQubeサーバーが実行中であることを確認（`http://localhost:9000`）

2. **コードカバレッジがない**:
   - `pom.xml` でJaCoCoプラグインが正しく設定されていることを確認
   - 解析前に `mvn test` を実行して `jacoco.exec` を生成

3. **データベース接続エラー**:
   - `sonar.properties` のデータベース認証情報を確認
   - データベースサーバーが実行中であることを確認

4. **メモリ不足**:
   - `sonar.properties` でJVMメモリを増加：
     ```properties
     sonar.web.javaOpts=-Xmx2g -Xms1g
     ```

## まとめ
SonarQubeは、Java Springプロジェクトでコード品質を維持するための強力なツールです。開発ワークフローに統合することで、問題を早期に発見し、コードの保守性を向上させ、堅牢なセキュリティを確保できます。定期的な解析と、CI/CD統合やSonarLintなどのベストプラクティスを組み合わせることで、高品質なコードベースを維持できます。