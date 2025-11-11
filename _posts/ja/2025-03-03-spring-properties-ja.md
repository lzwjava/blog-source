---
audio: false
generated: true
lang: ja
layout: post
title: Spring Bootにおけるプロパティファイルの選択
translated: true
type: note
---

Spring Boot Mavenプロジェクトにおいて、`src/main/resources`配下に2つのプロパティファイル`appProperties.properties`と`appProperties-hk.properties`がある場合、特に`-hk`プロパティを使用するように指定するには、Spring Bootの設定メカニズムを活用できます。以下にその方法を示します：

### 解決策

1. **`application.properties`ファイルの作成**
   - デフォルトでは、Spring Bootは`src/main/resources`にある`application.properties`または`application.yml`を探して設定を読み込みます。
   - カスタムプロパティファイル（`appProperties.properties`と`appProperties-hk.properties`）を使用するには、Spring Bootにデフォルトの`application`ではなくベース名`appProperties`のファイルを探すように指示する必要があります。
   - `src/main/resources`に新しい`application.properties`ファイルを作成し、以下の行を追加します：

     ```properties
     spring.config.name=appProperties
     ```

   - この設定により、Spring Bootはベース設定ファイルとして`appProperties.properties`を読み込み、プロファイルがアクティブな場合には`appProperties-{profile}.properties`のようなプロファイル固有のバリアントも自動的に探します。

2. **Spring Profilesを使用して`-hk`プロパティを指定**
   - Spring Bootはプロファイルをサポートしており、アクティブなプロファイルに基づいて追加または上書きするプロパティファイルを読み込むことができます。
   - ファイル名が`appProperties-hk.properties`であるため、これは`appProperties-{profile}.properties`というパターンに従っています。ここで「hk」はプロファイル名として扱うことができます。
   - `appProperties-hk.properties`を使用するには、アプリケーション実行時に「hk」プロファイルをアクティブにします。Spring Bootは`appProperties.properties`と`appProperties-hk.properties`の両方を読み込み、`appProperties-hk.properties`内のプロパティが`appProperties.properties`内の一致するプロパティを上書きします。

3. **「hk」プロファイルをアクティブ化する方法**
   - **コマンドライン経由**: Spring Bootアプリケーションを実行する際に、`--spring.profiles.active`引数を使用してアクティブなプロファイルを指定します。例：
     ```bash
     java -jar target/myapp.jar --spring.profiles.active=hk
     ```
     `myapp.jar`をMavenで生成されたアプリケーションのJARファイル名に置き換えてください。

   - **Maven経由**: `spring-boot:run`ゴールを使用してアプリケーションを実行する場合は、`pom.xml`でプロファイルを設定します：
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
     その後、以下を実行します：
     ```bash
     mvn spring-boot:run
     ```

   - **システムプロパティ経由**: JVM引数としてプロファイルを設定します：
     ```bash
     java -Dspring.profiles.active=hk -jar target/myapp.jar
     ```

   - **環境変数経由**: 環境でプロファイルをエクスポートします（例：Unix系システム）：
     ```bash
     export SPRING_PROFILES_ACTIVE=hk
     java -jar target/myapp.jar
     ```

### 動作の仕組み
- `application.properties`で`spring.config.name=appProperties`が設定されると、Spring Bootは設定ファイルのベース名として`appProperties`を使用します。
- プロファイルがアクティブでない場合、`appProperties.properties`のみが読み込まれます。
- 「hk」プロファイルがアクティブ化されると（例：`--spring.profiles.active=hk`経由）、Spring Bootは`appProperties.properties`と`appProperties-hk.properties`の両方を読み込みます。重複がある場合、`appProperties-hk.properties`で定義されたプロパティが`appProperties.properties`のプロパティより優先されます。

### 最終的な手順
- `appProperties.properties`と`appProperties-hk.properties`の両方が`src/main/resources`にあることを確認してください。
- `spring.config.name=appProperties`を含む`application.properties`を`src/main/resources`に追加してください。
- `-hk`プロパティを使用するには、「hk」プロファイルをアクティブにしてアプリケーションを実行してください。

このアプローチはSpring Bootの規約に沿っており、プロジェクトで使用するプロパティファイルを制御する典型的で簡単な方法です。特に`-hk`プロパティを使用するには、上記のように「hk」プロファイルをアクティブにするだけです。