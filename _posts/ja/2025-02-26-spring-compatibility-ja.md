---
audio: false
generated: true
lang: ja
layout: post
title: Spring Boot と Java バージョンの互換性
translated: true
type: note
---

### エラーの理解

Spring Boot 3.4.3 で `mvn spring-boot:run` を実行し、「class file has wrong version 61.0, should be 52.0」というエラーが発生した場合、Java のバージョン互換性の問題を示しています。Java では、クラスファイルにはコンパイル時に使用された Java バージョンに対応するバージョン番号が付与されます：

- **バージョン 52.0** は Java 8 に対応します。
- **バージョン 61.0** は Java 17 に対応します。

このエラーは、Spring Boot アプリケーションのクラスファイルが Java 17 (バージョン 61.0) でコンパイルされたにもかかわらず、それを実行しようとしている Java Virtual Machine (JVM) が Java 8 (バージョン 52.0) 互換のクラスファイルを期待していることを示唆しています。Java 8 の JVM は Java 17 でコンパイルされたクラスファイルを実行できないため（Java は後方互換性がありますが、この文脈では前方互換性がありません）、このエラーが発生します。

### 原因

Spring Boot 3.4.3 は、サポートされる最低バージョンとして **Java 17 以降** を必要とします。これは、プロジェクトのコンパイルと実行の両方に少なくとも Java 17 を使用する必要があることを意味します。この不一致は、主に以下の理由で発生します：

1.  **コンパイル**: プロジェクトが Java 17 でコンパイルされるように設定されており、バージョン 61.0 のクラスファイルが生成されています。これは通常、`pom.xml` の `maven-compiler-plugin` または `<java.version>` プロパティで設定されます。
2.  **実行時**: `mvn spring-boot:run` を実行すると、Spring Boot Maven プラグインはアプリケーションを実行するために新しい Java プロセスを起動します。しかし、使用される `java` 実行ファイルが Java 8 インストール (バージョン 52.0) からのものである場合、Java 17 でコンパイルされたクラスファイルを処理できません。

### 問題解決の手順

この問題を解決するには、コンパイル環境と実行環境の両方が Java 17 を使用していることを確認する必要があります。修正方法は以下の通りです：

#### 1. プロジェクトの Java バージョンを確認する
まず、プロジェクトが Java 17 を使用するように設定されていることを確認してください。`pom.xml` で以下を確認します：

```xml
<properties>
    <java.version>17</java.version>
</properties>
```

このプロパティは、`maven-compiler-plugin` に Java 17 でコードをコンパイルするように指示します。Spring Boot 3.4.3 はデフォルトでこれを設定しますが、確認することをお勧めします。もし設定が欠落しているか、異なるバージョン (例: 8) に設定されている場合は、17 に更新してください。

#### 2. Java 17 をインストールする
システムに Java 17 がインストールされていることを確認してください。以下からダウンロードできます：

- [Adoptium (Eclipse Temurin)](https://adoptium.net/)
- [Oracle JDK](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) (ライセンス条項に同意する場合)

Java 17 がインストールされているか確認するには、ターミナルを開いて以下を実行します：

```bash
java -version
```

Java 17 (例: `openjdk 17.x.x` など) が表示されない場合は、インストールしてから次に進んでください。

#### 3. 環境を Java 17 を使用するように更新する
Spring Boot Maven プラグインは、環境から `JAVA_HOME` 環境変数またはシステムの PATH 内の `java` コマンドによって決定される `java` 実行ファイルを使用します。現在の `java` コマンドが Java 8 を指している場合は、更新する必要があります。

##### オプション A: JAVA_HOME と PATH を設定する
`JAVA_HOME` 環境変数を Java 17 のインストールディレクトリに設定し、PATH 内の `java` コマンドがそれを使用するようにします。

- **Linux/Mac の場合**:
  1.  Java 17 のインストールディレクトリを探します (例: `/usr/lib/jvm/java-17-openjdk` またはインストールした場所)。
  2.  ターミナルで `JAVA_HOME` を設定し、`PATH` を更新します：
      ```bash
      export JAVA_HOME=/path/to/java-17
      export PATH=$JAVA_HOME/bin:$PATH
      ```
  3.  確認します：
      ```bash
      java -version
      ```
      これで Java 17 が表示されるはずです。

  これを恒久的にするには、`export` 行をシェル設定ファイル (例: `~/.bashrc`, `~/.zshrc`) に追加します。

- **Windows の場合**:
  1.  Java 17 のインストールディレクトリを探します (例: `C:\Program Files\Java\jdk-17`)。
  2.  `JAVA_HOME` を設定します：
      - システム プロパティ ウィンドウを開きます (スタート メニューで「環境変数」を検索)。
      - 「システム環境変数」で、`JAVA_HOME` を追加または更新して `C:\Program Files\Java\jdk-17` に設定します。
  3.  `Path` を更新します：
      - 「システム環境変数」で `Path` を編集し、`%JAVA_HOME%\bin` を追加します (先頭に置くか、古い Java 8 などのパスを削除してください)。
  4.  新しいコマンド プロンプトを開き、確認します：
      ```cmd
      java -version
      ```
      これで Java 17 が表示されるはずです。

##### オプション B: Maven で特定の Java バージョンを使用する
複数の Java バージョンがインストールされており、システム全体の `JAVA_HOME` を変更したくない場合は、特定の Java バージョンで Maven を実行できます：

- `mvn spring-boot:run` を実行する前に、そのコマンドに対してのみ `JAVA_HOME` を設定します：
  ```bash
  JAVA_HOME=/path/to/java-17 mvn spring-boot:run
  ```
  これにより、システム設定を変更することなく、Spring Boot Maven プラグインが Java 17 を使用するようになります。

#### 4. アプリケーションを再度実行する
Java 17 が正しく設定されたら、以下を実行します：

```bash
mvn spring-boot:run
```

プラグインはアプリケーションの実行に Java 17 を使用するようになり、コンパイルされたクラスファイルのバージョン (61.0) と一致するため、エラーは解消されます。

### 追加の確認事項
- **Maven の Java バージョン**: `mvn -version` を実行して、Maven が使用する Java バージョンを確認します。`JAVA_HOME` と一致するはずです。一致しない場合は、PATH と `JAVA_HOME` が正しく設定されていることを確認してください。
- **依存関係**: エラーが解消しない場合、依存関係の一部が Java 17 でコンパイルされており、実行時環境がまだ誤って設定されている可能性があります。Spring Boot 3.4.3 は Java 17 を強制するため、実行時環境が Java 17 であることを確認すれば解決するはずです。

### Java 8 が使えない理由
Spring Boot 3.4.3 は Java 8 をサポートしていません。Java 8 を使用する必要がある場合は、古い Spring Boot バージョン (例: 2.x) にダウングレードする必要がありますが、特定の制約がない限り推奨されません。クラスファイルがバージョン 61.0 であるため、Java 17 を使用することが Spring Boot 3.4.3 の要件に沿った対応となります。

### 最終的な解決策のまとめ
Spring Boot 3.4.3 で `mvn spring-boot:run` を実行する際の「class file has wrong version 61.0, should be 52.0」を修正するには：

1.  `pom.xml` に `<java.version>17</java.version>` が含まれていることを確認します。
2.  まだの場合は Java 17 をインストールします。
3.  `JAVA_HOME` を Java 17 のインストールディレクトリに設定します。
4.  `java -version` が Java 17 を表示するように PATH を更新します。
5.  再度 `mvn spring-boot:run` を実行します。

これにより、実行時環境がコンパイルされた Java 17 のクラスファイルと一致し、互換性の問題が解決されます。