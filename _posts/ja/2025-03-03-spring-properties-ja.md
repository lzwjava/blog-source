---
audio: false
generated: true
lang: ja
layout: post
title: プロパティファイルの選択方法
translated: true
---

Spring Boot Maven プロジェクトで、`src/main/resources` に `appProperties.properties` と `appProperties-hk.properties` の2つのプロパティファイルがあります。どちらのプロパティファイルを使用するかを制御し、特に `-hk` プロパティの使用を指定するには、Spring Boot の設定メカニズムを活用できます。以下にその方法を示します。

### ソリューション

1. **`application.properties` ファイルを作成する**
   - デフォルトでは、Spring Boot は `src/main/resources` にある `application.properties` または `application.yml` を探して設定を読み込みます。
   - カスタムプロパティファイル (`appProperties.properties` と `appProperties-hk.properties`) を使用するには、Spring Boot に `application` ではなく `appProperties` をベース名として探すように指示する必要があります。
   - `src/main/resources` に新しい `application.properties` ファイルを作成し、以下の行を追加します：

     ```properties
     spring.config.name=appProperties
     ```

   - この設定により、Spring Boot は `appProperties.properties` をベースの設定ファイルとして読み込み、プロファイルがアクティブな場合には `appProperties-{profile}.properties` のようなプロファイル固有のバリエーションも自動的に探します。

2. **Spring プロファイルを使用して `-hk` プロパティを指定する**
   - Spring Boot はプロファイルをサポートしており、アクティブなプロファイルに基づいて追加または上書きするプロパティファイルを読み込むことができます。
   - ファイルが `appProperties-hk.properties` として名前付けられているため、これは `appProperties-{profile}.properties` のパターンに従っています。ここで "hk" はプロファイル名として扱われます。
   - `appProperties-hk.properties` を使用するには、アプリケーションを実行する際に "hk" プロファイルをアクティブにします。Spring Boot は `appProperties.properties` と `appProperties-hk.properties` の両方を読み込み、`appProperties-hk.properties` にあるプロパティが `appProperties.properties` にある同じプロパティを上書きします。

3. **「hk」プロファイルをアクティブにする方法**
   - **コマンドラインから**: Spring Boot アプリケーションを実行する際に、アクティブなプロファイルを `--spring.profiles.active` 引数で指定します。例えば：
     ```bash
     java -jar target/myapp.jar --spring.profiles.active=hk
     ```
     ここで `myapp.jar` は Maven によって生成されたアプリケーションの JAR ファイルの名前に置き換えてください。

   - **Maven から**: `spring-boot:run` ゴールを使用してアプリケーションを実行する場合、`pom.xml` でプロファイルを設定します：
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <configuration>
             <profiles>
                 <profile>hk</profile>
             </profiles>
         </configuration>
     </plugin>
     ```
     そして実行します：
     ```bash
     mvn spring-boot:run
     ```

   - **システムプロパティから**: プロファイルを JVM 引数として設定します：
     ```bash
     java -Dspring.profiles.active=hk -jar target/myapp.jar
     ```

   - **環境変数から**: 環境にプロファイルをエクスポートします（例：Unix 系システム）：
     ```bash
     export SPRING_PROFILES_ACTIVE=hk
     java -jar target/myapp.jar
     ```

### 仕組み
- `application.properties` に `spring.config.name=appProperties` が設定されているため、Spring Boot は `appProperties` を設定ファイルのベース名として使用します。
- プロファイルがアクティブでない場合、`appProperties.properties` だけが読み込まれます。
- 「hk」プロファイルがアクティブになっている場合（例：`--spring.profiles.active=hk` を使用して）、Spring Boot は `appProperties.properties` と `appProperties-hk.properties` の両方を読み込みます。`appProperties-hk.properties` に定義されているプロパティが `appProperties.properties` にある同じプロパティを上書きします。

### 最終ステップ
- `appProperties.properties` と `appProperties-hk.properties` が `src/main/resources` にあることを確認します。
- `application.properties` に `spring.config.name=appProperties` を追加して `src/main/resources` に配置します。
- 「hk」プロファイルをアクティブにしてアプリケーションを実行し、`-hk` プロパティを使用します。

このアプローチは Spring Boot の慣例に従っており、プロジェクトで使用するプロパティファイルを制御するための典型的で直感的な方法です。`-hk` プロパティを特定に使用するには、上記のように「hk」プロファイルをアクティブにするだけです。