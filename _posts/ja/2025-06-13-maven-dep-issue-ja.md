---
audio: false
generated: true
lang: ja
layout: post
title: Maven依存関係の問題
translated: true
type: note
---

### 問題の概要

ユーザーは、Mavenを使用してSpring Bootアプリケーションを実行する際にビルド失敗に遭遇しています。エラーメッセージは、`org/springframework/beans/factory/aot/BeanRegistrationExcludeFilter` による `NoClassDefFoundError` が原因の `IllegalArgumentException` を示しています。これは、プロジェクトの依存関係内にバージョンの非互換性が存在し、アプリケーションが正しく起動できないことを示唆しています。提供された `pom.xml` ファイルとMavenの出力が、問題の診断と解決に必要なコンテキストを提供しています。

### 根本原因

このエラーは、Spring BootアプリケーションがSpring Bootの自動設定プロセスに関与するクラスである `SharedMetadataReaderFactoryContextInitializer` をインスタンス化できないために発生します。根本的な原因は、Spring Framework 6.0 以降の一部である `BeanRegistrationExcludeFilter` クラスが見つからないことです。プロジェクトは Spring Boot 3.4.2 を使用していますが、これは Spring Framework 6.1.14 に依存しています。しかし、`pom.xml` には古い非互換なバージョンのSpring Framework依存関係が指定されているため、クラスパスの競合が発生しています。

`pom.xml` で特定された主な問題点は以下の通りです：

1. **非互換なSpring Boot Mavenプラグインバージョン:**
   - `spring-boot-maven-plugin` がバージョン `2.7.0` に設定されています。これは Spring Boot 2.x 向けに設計されたものであり、Spring Boot 3.4.2 (3.x バージョン) 向けではありません。この不一致は、ビルドおよび実行時フェーズで問題を引き起こす可能性があります。

2. **明示的な非互換なSpring Framework依存関係:**
   - `pom.xml` は `spring-aop` と `spring-aspects` をバージョン `5.3.23` (Spring Framework 5.x) で明示的に宣言していますが、Spring Boot 3.4.2 は Spring Framework 6.1.14 を必要とします。Mavenは、Spring Bootによって管理されるバージョンよりもこれらの明示的に宣言されたバージョンを優先するため、クラスパス上に Spring Framework 5.x と 6.x が混在する結果となります。この混在により、`BeanRegistrationExcludeFilter` (Spring Framework 6.x 由来) が古い 5.x のJARが読み込まれる際に利用できないため、`NoClassDefFoundError` が発生します。

### 解決策

この問題を解決するには、プロジェクトのすべてのコンポーネントが Spring Boot 3.4.2 と互換性があることを確認し、Spring Bootが依存関係のバージョンを管理して競合を回避するようにする必要があります。`pom.xml` に対して以下の変更を加える必要があります：

1. **Spring Boot Mavenプラグインのバージョンを更新:**
   - `spring-boot-maven-plugin` のバージョンを `2.7.0` から `3.4.2` に変更し、プロジェクトで使用されているSpring Bootのバージョンに合わせます。

2. **明示的なSpring Framework依存関係を削除:**
   - バージョン `5.3.23` の `spring-aop` と `spring-aspects` の明示的な宣言を削除します。Spring Boot 3.4.2 はこれらの依存関係をそのスターター (例: `spring-boot-starter-web` は正しいバージョン 6.1.14 の `spring-aop` を含む) を介して管理します。これらを削除することで、MavenがSpring Bootの依存関係管理を上書きするのを防ぎます。

### 更新された `pom.xml`

以下は、必要な変更を適用した修正済みの `pom.xml` ファイルです：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.lzwjava</groupId>
    <artifactId>blog-server</artifactId>
    <version>1.0</version>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <version>3.4.2</version>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-api</artifactId>
            <version>5.9.3</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-engine</artifactId>
            <version>5.9.3</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-core</artifactId>
            <version>5.3.1</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <version>3.4.2</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjrt</artifactId>
            <version>1.9.22</version>
        </dependency>
        <dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjweaver</artifactId>
            <version>1.9.22</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>3.4.2</version>
                <executions>
                    <execution>
                        <goals>
                            <goal>repackage</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.0.0-M8</version>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-checkstyle-plugin</artifactId>
                <version>3.1.1</version>
                <configuration>
                    <configLocation>google_checks.xml</configLocation>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>check</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### 変更点の説明

- **Spring Boot Mavenプラグインの更新:**
  - `spring-boot-maven-plugin` の設定で `<version>2.7.0</version>` を `<version>3.4.2</version>` に変更しました。これにより、プラグインが Spring Boot 3.4.2 と互換性を持ち、3.x シリーズに特有の機能と設定をサポートします。

- **`spring-aop` と `spring-aspects` の削除:**
  - 以下の依存関係を削除しました：
    ```xml
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-aop</artifactId>
        <version>5.3.23</version>
    </dependency>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-aspects</artifactId>
        <version>5.3.23</version>
    </dependency>
    ```
  - `spring-aop` は `spring-boot-starter-web` (を介して `spring-web` に含まれる) に既に含まれており、Spring Boot はそのバージョンを 3.4.2 と互換性のある 6.1.14 に管理します。
  - `spring-aspects` は Spring Boot スターターの標準的な依存関係ではありません。プロジェクトが明示的にそれを必要とする場合 (例: カスタムアスペクト用)、バージョンなしで再追加する (Spring Boot の依存関係管理に任せる) か、`6.1.14` に設定することができます。ただし、エラーが起動時に発生し、アスペクトの欠落ではなく自動設定に関連しているため、ここでは不要であり安全に削除できます。

### 追加の注意点

- **AspectJ 依存関係:**
  - `aspectjrt` と `aspectjweaver` の依存関係 (バージョン 1.9.22) は、Spring Framework 6.1.14 と互換性があり、プロジェクトが AspectJ 機能を使用する場合に必要となる可能性があるため、`pom.xml` に残しています。これらは Spring Boot 3.4.2 と競合しません。

- **ベストプラクティス:**
  - Spring Boot プロジェクトでは、親POMとして `spring-boot-starter-parent` を使用するか、`spring-boot-dependencies` BOM をインポートして依存関係のバージョンを自動的に管理することが推奨されます。現在の `pom.xml` はどちらも行っていませんが、明示的なオーバーライドが削除された場合、`spring-boot-starter-web` や他のスターターがバージョンの一貫性を強制するため、この変更を必要とせずに解決策は機能します。

- **検証:**
  - これらの変更を適用した後、`mvn clean spring-boot:run` を実行して、アプリケーションがエラーなく起動することを確認してください。プロジェクトが `spring-aspects` に依存している場合 (例: 特定のAOP機能用)、それを削除することで問題が発生する場合は、`<version>6.1.14</version>` を付けて再追加するか、バージョンを省略して適切な依存関係管理を確保してください。

### 結論

`spring-boot-maven-plugin` をバージョン 3.4.2 に更新し、明示的な `spring-aop` と `spring-aspects` の依存関係を削除することで、プロジェクトは Spring Boot (3.4.2) と Spring Framework (6.1.14) の一貫したバージョンを使用するようになります。これにより、`NoClassDefFoundError` を引き起こしていたクラスパスの競合が解決され、アプリケーションは正常に起動できるようになります。