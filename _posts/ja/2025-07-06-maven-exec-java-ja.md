---
audio: false
generated: true
lang: ja
layout: post
title: Maven Exec を使用した Java クラスの実行
translated: true
type: note
---

Maven Exec Pluginの`exec:java`ゴールは、Mavenビルドから直接`main`メソッドを持つJavaクラスを実行する強力な方法です。このゴールは、プロジェクトの依存関係をクラスパスとして使用し、**Mavenビルドと同じJVM内**で指定されたJavaクラスを実行します。

以下に、一般的なシナリオと例を用いた使用方法を示します：

## 1. コマンドラインからの基本的な使用方法

`exec:java`を最も簡単に使用する方法は、コマンドラインから直接実行することです。特に、簡単なテストや特定のユーティリティクラスの実行に適しています。

**コマンド：**

```bash
mvn exec:java -Dexec.mainClass="com.yourcompany.YourMainClass"
```

**説明：**

* `mvn exec:java`：`exec-maven-plugin`の`java`ゴールを呼び出します。
* `-Dexec.mainClass="com.yourcompany.YourMainClass"`：このシステムプロパティは、実行したい`public static void main(String[] args)`メソッドを含むJavaクラスの完全修飾名を指定します。

**例：**

`main`メソッドを持つ`com.example.myapp.HelloWorld`クラスがあるとします：

```java
package com.example.myapp;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello from Maven exec:java!");
    }
}
```

以下のコマンドで実行できます：

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld"
```

**注意：** `exec:java`が実行を試みる前にクラスがコンパイルされていることを保証するために、最初に`mvn compile`を実行することが推奨されます。

## 2. Javaプログラムへの引数の渡し方

`exec.args`システムプロパティを使用して、Javaプログラムの`main`メソッドに引数を渡すことができます：

**コマンド：**

```bash
mvn exec:java -Dexec.mainClass="com.yourcompany.YourMainClass" -Dexec.args="arg1 arg2 \"arg with spaces\""
```

**例：**

`HelloWorld`クラスが以下のような場合：

```java
package com.example.myapp;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello from Maven exec:java!");
        if (args.length > 0) {
            System.out.println("Arguments received: ");
            for (String arg : args) {
                System.out.println("- " + arg);
            }
        }
    }
}
```

以下のように実行します：

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld" -Dexec.args="FirstArgument SecondArgument"
```

スペースを含む引数は、引用符で囲みます：

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld" -Dexec.args="\"Hello World\" AnotherArg"
```

## 3. `pom.xml`での`exec:java`の設定

より永続的またはデフォルトの設定のために、`exec-maven-plugin`を`pom.xml`に追加できます。これにより、デフォルトの`mainClass`やその他のパラメータを定義できるため、毎回コマンドラインで指定する必要がなくなります。

**`pom.xml`設定：**

```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.yourcompany</groupId>
    <artifactId>my-maven-app</artifactId>
    <version>1.0-SNAPSHOT</modelVersion>

    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.2.0</version> <executions>
                    <execution>
                        <goals>
                            <goal>java</goal>
                        </goals>
                    </execution>
                </executions>
                <configuration>
                    <mainClass>com.example.myapp.HelloWorld</mainClass>
                    <arguments>
                        <argument>defaultArg1</argument>
                        <argument>defaultArg2</argument>
                    </arguments>
                    <systemProperties>
                        <systemProperty>
                            <key>my.custom.property</key>
                            <value>someValue</value>
                        </systemProperty>
                    </systemProperties>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
    </properties>

</project>
```

**設定オプションの説明：**

* `<groupId>org.codehaus.mojo</groupId>`および`<artifactId>exec-maven-plugin</artifactId>`：プラグインの標準的な座標です。
* `<version>3.2.0</version>`：常にプラグインの最新バージョンを指定してください。
* `<goals><goal>java</goal></goals>`：`java`ゴールをバインドします。特定のフェーズにバインドしない場合、明示的に`mvn exec:java`を呼び出したときに実行されます。
* `<mainClass>com.example.myapp.HelloWorld</mainClass>`：実行するデフォルトのメインクラスを設定します。コマンドラインで`-Dexec.mainClass`を指定せずに`mvn exec:java`を実行すると、このクラスが使用されます。
* `<arguments>`：`main`メソッドに渡す引数のリストです。これらは、コマンドラインの`exec.args`で上書きできるデフォルトの引数です。
* `<systemProperties>`：`exec:java`実行時にJavaアプリケーションで利用可能なシステムプロパティ（`-Dkey=value`）を定義できます。

**`pom.xml`設定での実行方法：**

`pom.xml`で設定した後：

* デフォルトのメインクラスと引数で実行する場合：
  ```bash
  mvn compile exec:java
  ```
* コマンドラインからメインクラスを上書きする場合：
  ```bash
  mvn compile exec:java -Dexec.mainClass="com.example.myapp.AnotherMainClass"
  ```
* コマンドラインから引数を上書き/追加する場合：
  ```bash
  mvn compile exec:java -Dexec.args="commandLineArg1 commandLineArg2"
  ```
  （注意：`exec.args`は、コマンドラインで指定された場合、通常`pom.xml`で定義された`arguments`を*置き換えます*。）

## 4. `exec:exec`との主な違い

`exec:java`と`exec:exec`の違いを理解することが重要です：

* **`exec:java`**：JavaプログラムをMaven**と同じJVM内**で実行します。新しいプロセスを生成しないため、一般的に高速です。プロジェクトの依存関係を自動的にクラスパスに設定します。
* **`exec:exec`**：任意の外部プログラム（`java`自体を含む）を**別のプロセス内**で実行します。異なるJava実行ファイルを指定する必要がある場合、JVM引数（`-Xmx`など）を渡す必要がある場合、または非Javaの実行ファイルを実行する場合に便利です。`exec:exec`を使用してJavaプログラムを実行する場合、通常は引数で`%classpath`を使用してクラスパスを手動で構築する必要があります。

Mavenビルド内での標準的なJavaアプリケーション実行のほとんどの場合、`exec:java`がより便利な選択肢です。

## 5. 重要な考慮事項

* **クラスパス：** `exec:java`は、プロジェクトのコンパイル済みクラスとその依存関係を自動的にクラスパスに含めます。
* **JVM引数：** `exec:java`はMavenと*同じ*JVMで実行されるため、JVM引数（`-Xmx`、`-XX:MaxPermSize`など）を`exec:java`の設定や`exec.args`を通じて直接渡すことはできません。これらの引数は、通常`MAVEN_OPTS`環境変数を介してMaven JVM自体に渡す必要があります：
  ```bash
  export MAVEN_OPTS="-Xmx1024m -Dsome.jvm.property=value"
  mvn exec:java ...
  ```
* **System.exit()：** Javaプログラムが`System.exit()`を呼び出すと、プログラムだけでなくMavenビルドプロセス全体が終了します。`exec:java`を使用する際はこれに注意してください。プラグインにはこれを防ごうとする`blockSystemExit`オプション（バージョン3.2.0以降）がありますが、`main`メソッドを`System.exit()`を呼び出さずに正常に完了するように設計することが最善です。
* **依存関係：** `exec:java`はプロジェクトの依存関係に依存します。プロジェクトのビルドの一部ではない依存関係からクラスを実行する必要がある場合は、プラグインの設定を調整するか、明示的なクラスパス定義を使用した`exec:exec`の使用を検討する必要があります。
* **プラグインバージョン：** 最新の機能とバグ修正のために、常に`exec-maven-plugin`の最新バージョンを使用してください。最新の情報についてはMojoHausのWebサイトを確認してください。