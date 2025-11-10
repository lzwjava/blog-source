---
audio: false
generated: true
lang: ja
layout: post
title: Maven Javaプログラムでの入力リダイレクト
translated: true
type: note
---

`exec:java` プログラムへの入力リダイレクトは、`exec:java` が Maven と同じ *JVM* 内で Java プロセスを実行するため、少し扱いが難しい場合があります。これは、別プロセスに対して行うような標準的なシェルリダイレクト演算子 (`<`, `>`) を同じようには使用できないことを意味します。

しかし、`exec:java` プログラムに入力を提供する方法はいくつかあります：

## 1. プログラムによる入力 (標準の `System.in`)

最も簡単な方法は、Java プログラムを通常通り `System.in` から読み取るように設計することです。`mvn exec:java` を実行すると、コンソールで入力した内容が Java プログラムの `System.in` に直接渡されます。

**Java プログラムの例 (`MyInputProgram.java`):**

```java
package com.example.app;

import java.util.Scanner;

public class MyInputProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println("Hello, " + name + "!");

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        System.out.println("You are " + age + " years old.");

        scanner.close();
    }
}
```

**コマンドラインからの実行:**

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyInputProgram"
```

これを実行すると、Maven が起動し、プログラムが入力のプロンプトを表示します。コンソールに直接入力してください。

## 2. `exec.args` プロパティを使用した入力 (単純なケース向け)

プログラムが非常に単純な非対話型の入力を受け取る場合、引数として渡し、プログラムが `System.in` の代わりにその引数を読み取るように *できる可能性があります*。これは真の標準入力リダイレクトではありませんが、単純なデータに対しては同様の目的を果たします。

**Java プログラムの例 (`MyArgProgram.java`):**

```java
package com.example.app;

public class MyArgProgram {
    public static void main(String[] args) {
        if (args.length > 0) {
            String inputData = args[0];
            System.out.println("Received input from argument: " + inputData);
        } else {
            System.out.println("No input argument provided.");
        }
    }
}
```

**コマンドラインからの実行:**

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyArgProgram" -Dexec.args="MyCustomInputString"
```

またはスペースを含む場合:

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyArgProgram" -Dexec.args="\"Input with spaces\""
```

このアプローチは、プログラムが「入力」をコマンドライン引数として受け取るように変更できる場合にのみ適しています。

## 3. シェルリダイレクトを使用した入力リダイレクト (`exec:exec` を使用)

ファイルやパイプからの入力リダイレクトが絶対に必要な場合は、`exec:java` の代わりに `exec:exec` ゴールを **使用しなければなりません**。`exec:exec` ゴールは別プロセスを生成するため、シェルが標準入出力のリダイレクトを処理できるようになります。

**`exec:exec` のための `pom.xml` 設定:**

```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.yourcompany</groupId>
    <artifactId>my-maven-app</artifactId>
    <version>1.0-SNAPSHOT</version>

    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.2.0</version> <executions>
                    <execution>
                        <id>run-my-java-app</id>
                        <phase>package</phase> <goals>
                            <goal>exec</goal>
                        </goals>
                        <configuration>
                            <executable>java</executable>
                            <arguments>
                                <argument>-classpath</argument>
                                <classpath/> <argument>com.example.app.MyInputProgram</argument>
                                </arguments>
                            <workingDirectory>${project.build.directory}/classes</workingDirectory>
                            </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
    </properties>

</project>
```

**Java プログラムの例 (上記と同じ `MyInputProgram.java`):**

```java
package com.example.app;

import java.util.Scanner;

public class MyInputProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println("Hello, " + name + "!");

        // 名前の後に年齢をもう一行読み取ることを想定
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        System.out.println("You are " + age + " years old.");

        scanner.close();
    }
}
```

**入力ファイル (`input.txt`):**

```
Alice
30
```

**`exec:exec` と入力リダイレクトを使用した実行:**

まず、プロジェクトをコンパイルします:

```bash
mvn compile
```

次に、`exec:exec` ゴールを実行し、シェルを使用して入力をリダイレクトします:

```bash
mvn exec:exec@run-my-java-app < input.txt
```

**説明:**

  * `mvn exec:exec@run-my-java-app`: `exec-maven-plugin` の `exec` ゴールを ID "run-my-java-app" で実行します。
  * `< input.txt`: これは標準的なシェルリダイレクト演算子です。実行されるコマンド (`java com.example.app.MyInputProgram`) の標準入力として `input.txt` の内容を渡すようにシェルに指示します。

**`exec:exec` に関する重要な注意点:**

  * **`executable`:** 実行ファイルとして明示的に `java` を指定します。
  * **`arguments`:** `-classpath` や `mainClass` を含む `java` コマンドの引数を手動で構築する必要があります。`<classpath/>` タグは、`exec-maven-plugin` がプロジェクトの実際の計算されたクラスパスに置き換える特別な値です。
  * **`workingDirectory`:** `workingDirectory` を `${project.build.directory}/classes` に設定すると、Java がコンパイルされた `.class` ファイルを見つけやすくなることがよくあります。
  * **`outputFile` (オプション):** `exec:exec` 用の `exec-maven-plugin` は、プログラムの標準出力とエラーを、シェルリダイレクトに依存するのではなく、プラグインの設定内で直接ファイルにリダイレクトするための `<outputFile>` 設定オプションも提供します。これはロギングに役立ちます。

**まとめ:**

  * ユーザーが直接入力する対話型入力の場合、`exec:java` と `System.in` は問題なく動作します。
  * ファイルやパイプからの入力提供が必要な場合は、`exec:exec` に切り替え、シェルの入力リダイレクト機能 (`<`) を利用する必要があります。