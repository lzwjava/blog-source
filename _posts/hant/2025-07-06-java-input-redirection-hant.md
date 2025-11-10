---
audio: false
generated: true
lang: hant
layout: post
title: 重定向 Maven Java 程式的輸入
translated: true
type: note
---

為 `exec:java` 程式重新導向輸入可能會有點棘手，因為 `exec:java` 是在 *同一個 JVM* 中作為 Maven 來執行 Java 程序。這意味著您無法以相同方式對獨立程序使用標準的 shell 重新導向運算子（`<`、`>`）。

然而，您仍有幾種方式可以為 `exec:java` 程式提供輸入：

## 1. 程式化輸入（標準 `System.in`）

最直接的方式是設計您的 Java 程式像往常一樣從 `System.in` 讀取。當您執行 `mvn exec:java` 時，您在控制台中輸入的任何內容都會被導向到 Java 程式的 `System.in`。

**Java 程式範例 (`MyInputProgram.java`):**

```java
package com.example.app;

import java.util.Scanner;

public class MyInputProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("請輸入您的姓名: ");
        String name = scanner.nextLine();
        System.out.println("您好, " + name + "!");

        System.out.print("請輸入您的年齡: ");
        int age = scanner.nextInt();
        System.out.println("您今年 " + age + " 歲。");

        scanner.close();
    }
}
```

**從命令列執行:**

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyInputProgram"
```

當您執行此命令時，Maven 會啟動，然後您的程式會提示您輸入。您可以直接在控制台中輸入。

## 2. 使用 `exec.args` 屬性進行輸入（適用於簡單情況）

如果您的程式只需要非常簡單的非互動式輸入，您*或許*可以將其作為參數傳遞，然後您的程式讀取該參數而不是 `System.in`。這並非真正的標準輸入重新導向，但對於簡單資料來說能達到類似目的。

**Java 程式範例 (`MyArgProgram.java`):**

```java
package com.example.app;

public class MyArgProgram {
    public static void main(String[] args) {
        if (args.length > 0) {
            String inputData = args[0];
            System.out.println("從參數接收到輸入: " + inputData);
        } else {
            System.out.println("未提供輸入參數。");
        }
    }
}
```

**從命令列執行:**

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyArgProgram" -Dexec.args="MyCustomInputString"
```

或者包含空格的情況：

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyArgProgram" -Dexec.args="\"包含空格的輸入\""
```

此方法僅適用於您的程式可以修改為接受命令列參數作為「輸入」的情況。

## 3. 使用 Shell 重新導向輸入（搭配 `exec:exec`）

如果您絕對需要從檔案或管道重新導向輸入，您**必須**使用 `exec:exec` 目標而非 `exec:java`。`exec:exec` 目標會產生一個獨立的程序，這允許 shell 處理標準輸入/輸出重新導向。

**`pom.xml` 中 `exec:exec` 的配置:**

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

**Java 程式範例（與上述相同的 `MyInputProgram.java`）:**

```java
package com.example.app;

import java.util.Scanner;

public class MyInputProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("請輸入您的姓名: ");
        String name = scanner.nextLine();
        System.out.println("您好, " + name + "!");

        // 假設在姓名之後您還想讀取另一行作為年齡
        System.out.print("請輸入您的年齡: ");
        int age = scanner.nextInt();
        System.out.println("您今年 " + age + " 歲。");

        scanner.close();
    }
}
```

**輸入檔案 (`input.txt`):**

```
Alice
30
```

**使用 `exec:exec` 並重新導向輸入執行：**

首先，編譯您的專案：

```bash
mvn compile
```

然後，執行 `exec:exec` 目標並使用您的 shell 重新導向輸入：

```bash
mvn exec:exec@run-my-java-app < input.txt
```

**解釋:**

  * `mvn exec:exec@run-my-java-app`: 使用 ID "run-my-java-app" 執行 `exec-maven-plugin` 的 `exec` 目標。
  * `< input.txt`: 這是一個標準的 shell 重新導向運算子。它告訴您的 shell 讀取 `input.txt` 的內容，並將其作為標準輸入提供給正在執行的命令（`java com.example.app.MyInputProgram`）。

**`exec:exec` 的重要注意事項:**

  * **`executable`:** 您需明確指定 `java` 為可執行檔。
  * **`arguments`:** 您需要手動建構 `java` 命令的參數，包括 `-classpath` 和 `mainClass`。`<classpath/>` 標籤是一個特殊值，`exec-maven-plugin` 會將其替換為您專案的實際計算出的 classpath。
  * **`workingDirectory`:** 將 `workingDirectory` 設定為 `${project.build.directory}/classes` 通常有助於 Java 找到您編譯後的 `.class` 檔案。
  * **`outputFile` (可選):** 用於 `exec:exec` 的 `exec-maven-plugin` 也提供了一個 `<outputFile>` 配置選項，可以直接在插件配置中將程式的標準輸出和錯誤重新導向到檔案，而不需依賴 shell 重新導向。這對於記錄日誌很有用。

**總結:**

  * 對於使用者直接輸入的互動式輸入，`exec:java` 和 `System.in` 運作良好。
  * 對於從檔案或管道提供輸入，您需要切換到 `exec:exec` 並利用您 shell 的輸入重新導向功能（`<`）。