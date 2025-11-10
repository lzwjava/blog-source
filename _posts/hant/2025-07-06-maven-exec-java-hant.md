---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Maven Exec 執行 Java 類別
translated: true
type: note
---

Maven Exec Plugin 的 `exec:java` 目標是一種強大的方式，可直接從您的 Maven 構建中運行帶有 `main` 方法的 Java 類。它**在與 Maven 構建相同的 JVM 中**執行指定的 Java 類，並使用項目的依賴項作為類路徑。

以下是使用方法，包含常見場景和範例：

## 1. 從命令列的基本用法

使用 `exec:java` 最簡單的方式是直接從命令列，特別適用於快速測試或運行特定的工具類。

**命令：**

```bash
mvn exec:java -Dexec.mainClass="com.yourcompany.YourMainClass"
```

**說明：**

  * `mvn exec:java`：調用 `exec-maven-plugin` 的 `java` 目標。
  * `-Dexec.mainClass="com.yourcompany.YourMainClass"`：此系統屬性指定包含您要執行的 `public static void main(String[] args)` 方法的 Java 類的完整限定名稱。

**範例：**

假設您有一個帶有 `main` 方法的類 `com.example.myapp.HelloWorld`：

```java
package com.example.myapp;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello from Maven exec:java!");
    }
}
```

您可以使用以下命令運行它：

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld"
```

**注意：** 最好先運行 `mvn compile`，以確保在 `exec:java` 嘗試運行之前您的類已編譯。

## 2. 傳遞參數給您的 Java 程式

您可以使用 `exec.args` 系統屬性將參數傳遞給 Java 程式的 `main` 方法：

**命令：**

```bash
mvn exec:java -Dexec.mainClass="com.yourcompany.YourMainClass" -Dexec.args="arg1 arg2 \"arg with spaces\""
```

**範例：**

如果您的 `HelloWorld` 類是：

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

您會這樣運行它：

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld" -Dexec.args="FirstArgument SecondArgument"
```

對於帶有空格的參數，請用引號括起來：

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld" -Dexec.args="\"Hello World\" AnotherArg"
```

## 3. 在 `pom.xml` 中配置 `exec:java`

對於更永久或預設的配置，您可以將 `exec-maven-plugin` 添加到您的 `pom.xml` 中。這允許您定義預設的 `mainClass` 和其他參數，這樣您就不必每次都在命令列指定它們。

**`pom.xml` 配置：**

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

**配置選項說明：**

  * `<groupId>org.codehaus.mojo</groupId>` 和 `<artifactId>exec-maven-plugin</artifactId>`：插件的標準座標。
  * `<version>3.2.0</version>`：始終指定插件的最新版本。
  * `<goals><goal>java</goal></goals>`：這會綁定 `java` 目標。如果您不將其綁定到特定階段，則在您明確調用 `mvn exec:java` 時將執行它。
  * `<mainClass>com.example.myapp.HelloWorld</mainClass>`：設置要執行的預設主類。如果您在命令列上運行 `mvn exec:java` 而沒有使用 `-Dexec.mainClass`，則將使用此類。
  * `<arguments>`：傳遞給 `main` 方法的參數列表。這些是預設參數，可以通過命令列上的 `exec.args` 覆蓋。
  * `<systemProperties>`：允許您定義系統屬性 (`-Dkey=value`)，這些屬性在 `exec:java` 運行時對您的 Java 應用程式可用。

**使用 `pom.xml` 配置運行：**

在 `pom.xml` 中配置後：

  * 使用預設主類和參數運行：
    ```bash
    mvn compile exec:java
    ```
  * 從命令列覆蓋主類：
    ```bash
    mvn compile exec:java -Dexec.mainClass="com.example.myapp.AnotherMainClass"
    ```
  * 從命令列覆蓋/添加參數：
    ```bash
    mvn compile exec:java -Dexec.args="commandLineArg1 commandLineArg2"
    ```
    （注意：如果在命令列上提供了 `exec.args`，它通常會*替換*在 `pom.xml` 中定義的 `arguments`。）

## 4. 與 `exec:exec` 的主要區別

了解 `exec:java` 和 `exec:exec` 之間的區別很重要：

  * **`exec:java`**：**在與 Maven 相同的 JVM 中**運行 Java 程式。這通常更快，因為它避免了產生新進程。它會自動將項目的依賴項設置在類路徑上。
  * **`exec:exec`**：**在單獨的進程中**運行任意外部程式（包括 `java` 本身）。當您需要指定不同的 Java 可執行文件、傳遞 JVM 參數（如 `-Xmx`）或運行非 Java 可執行文件時，這很有用。如果您使用 `exec:exec` 來運行 Java 程式，通常必須使用參數中的 `%classpath` 手動構建類路徑。

對於在 Maven 構建中執行大多數標準的 Java 應用程式，`exec:java` 是更方便的選擇。

## 5. 重要注意事項

  * **類路徑：** `exec:java` 會自動將您項目的編譯類及其依賴項包含在類路徑中。
  * **JVM 參數：** 由於 `exec:java` 在*與 Maven 相同的* JVM 中運行，您無法通過其配置或 `exec.args` 直接將 JVM 參數（如 `-Xmx`、`-XX:MaxPermSize`）傳遞給 `exec:java`。這些參數需要傳遞給 Maven JVM 本身，通常是通過 `MAVEN_OPTS` 環境變數：
    ```bash
    export MAVEN_OPTS="-Xmx1024m -Dsome.jvm.property=value"
    mvn exec:java ...
    ```
  * **System.exit()**：如果您的 Java 程式調用 `System.exit()`，它將終止整個 Maven 構建過程，而不僅僅是您的程式。使用 `exec:java` 時請注意這一點。該插件有一個選項 `blockSystemExit`（自版本 3.2.0 起）試圖防止這種情況，但最好設計您的 main 方法在不調用 `System.exit()` 的情況下優雅完成。
  * **依賴項：** `exec:java` 依賴於項目的依賴項。如果您需要運行不屬於項目構建一部分的依賴項中的類，您可能需要調整插件的配置或考慮使用帶有明確類路徑定義的 `exec:exec`。
  * **插件版本：** 始終使用最新版本的 `exec-maven-plugin` 以獲得最新功能和錯誤修復。請查閱 MojoHaus 網站以獲取最新信息。