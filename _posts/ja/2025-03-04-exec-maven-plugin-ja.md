---
audio: false
generated: true
lang: ja
layout: post
title: Exec Maven プラグイン
translated: true
type: note
---

Mavenプロジェクトで`org.codehaus.mojo` Exec Maven Pluginを使用するには、`pom.xml`ファイルで設定し、ビルドプロセス中に外部コマンドまたはJavaプログラムを実行する方法を決定する必要があります。このプラグインは2つの主要なゴールを提供します：外部プログラムを実行するための`exec:exec`と、Javaクラスを実行するための`exec:java`です。以下では、セットアップと効果的な使用方法について説明します。

### ステップ1: プラグインを`pom.xml`に追加する
まず、`pom.xml`の`<build><plugins>`セクションにExec Maven Pluginを含めます。`groupId`、`artifactId`、およびバージョン（現在の最新は`3.1.0`）を指定します：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
        </plugin>
    </plugins>
</build>
```

これによりプラグインがプロジェクトに追加されますが、設定するか手動でゴールを実行するまで何も行いません。

### ステップ2: ゴールを選択する
プラグインは2つの主要なゴールを提供します：
- **`exec:exec`**: 外部プログラム（シェルスクリプト、バイナリ、`java`コマンドなど）を実行します。
- **`exec:java`**: プロジェクト内の`main`メソッドを持つJavaクラスをMavenと同じJVMで実行します。

これらのゴールは、コマンドラインから手動で実行する（例：`mvn exec:exec`）か、Mavenビルドライフサイクルの特定のフェーズにバインドして使用できます。

### オプション1: `exec:java`でJavaプログラムを実行する
プロジェクトからJavaクラスを実行したい場合は、`exec:java`ゴールを使用します。これはプロジェクトの一部であるクラスの`main`メソッドを実行するのに理想的で、プロジェクトのランタイムクラスパス（依存関係を含む）を自動的に活用します。

#### 手動実行
メインクラスを指定する設定を追加します：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <mainClass>com.example.Main</mainClass>
            </configuration>
        </plugin>
    </plugins>
</build>
```

次に、コマンドラインから実行します：

```bash
mvn exec:java
```

これにより、`com.example.Main`がMavenと同じJVMで実行され、MavenのJVM設定を継承します。

#### ビルド中の自動実行
ビルドフェーズ（例：`test`）中に自動的に実行するには、`<executions>`セクションを使用します：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>run-my-java</id>
                    <phase>test</phase>
                    <goals>
                        <goal>java</goal>
                    </goals>
                    <configuration>
                        <mainClass>com.example.Main</mainClass>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

これで、`mvn test`を実行すると、`test`フェーズ中に`com.example.Main`クラスが実行されます。

#### 引数やシステムプロパティの渡し方
`main`メソッドに引数を渡したり、システムプロパティを設定できます：

```xml
<configuration>
    <mainClass>com.example.Main</mainClass>
    <arguments>
        <argument>arg1</argument>
        <argument>arg2</argument>
    </arguments>
    <systemProperties>
        <systemProperty>
            <key>propertyName</key>
            <value>propertyValue</value>
        </systemProperty>
    </systemProperties>
</configuration>
```

`exec:java`はMavenと同じJVMで実行されるため、JVMオプション（例：`-Xmx`）はMavenの起動方法から継承されます（例：`mvn -Xmx512m exec:java`）。

### オプション2: `exec:exec`で外部プログラムを実行する
シェルスクリプトやコマンドなどの外部プログラムを実行するには、`exec:exec`ゴールを使用します。

#### 手動実行
スクリプトを実行するようにプラグインを設定します：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <executable>myScript.sh</executable>
                <workingDirectory>/path/to/dir</workingDirectory>
                <arguments>
                    <argument>param1</argument>
                    <argument>param2</argument>
                </arguments>
            </configuration>
        </plugin>
    </plugins>
</build>
```

以下で実行します：

```bash
mvn exec:exec
```

これにより、指定された作業ディレクトリで引数を指定して`myScript.sh`が実行されます。

#### ビルド中の自動実行
統合テストのためのサーバー起動や停止など、フェーズにバインドします：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>start-server</id>
                    <phase>pre-integration-test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>startServer.sh</executable>
                    </configuration>
                </execution>
                <execution>
                    <id>stop-server</id>
                    <phase>post-integration-test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>stopServer.sh</executable>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

`mvn integration-test`を実行すると、テスト前にサーバーが起動し、テスト後に停止します。

#### カスタムJVMオプションでJavaを実行する
（`exec:java`とは異なり）特定のオプションを持つ別のJVMが必要な場合は、`exec:exec`を`java`実行ファイルと共に使用します。クラスパスを手動で管理する必要があります。以下は例です：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <executable>java</executable>
                <arguments>
                    <argument>-Xmx512m</argument>
                    <argument>-classpath</argument>
                    <argument>${project.build.outputDirectory}</argument>
                    <argument>com.example.Main</argument>
                </arguments>
            </configuration>
        </plugin>
    </plugins>
</build>
```

クラスパスに依存関係を含めるには、`maven-dependency-plugin`を使用して生成できます：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-dependency-plugin</artifactId>
            <version>3.2.0</version>
            <executions>
                <execution>
                    <id>build-classpath</id>
                    <phase>generate-resources</phase>
                    <goals>
                        <goal>build-classpath</goal>
                    </goals>
                    <configuration>
                        <outputProperty>project.classpath</outputProperty>
                    </configuration>
                </execution>
            </executions>
        </plugin>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>run-java</id>
                    <phase>test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>java</executable>
                        <arguments>
                            <argument>-Xmx512m</argument>
                            <argument>-classpath</argument>
                            <argument>${project.classpath}:${project.build.outputDirectory}</argument>
                            <argument>com.example.Main</argument>
                        </arguments>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

クラスパス区切り文字（Unixは`:`、Windowsは`;`）を必要に応じて調整してください。

### 追加の設定オプション
- **環境変数**（`exec:exec`用）：
  ```xml
  <configuration>
      <executable>myScript.sh</executable>
      <environmentVariables>
          <MY_VAR>value</MY_VAR>
      </environmentVariables>
  </configuration>
  ```
- **作業ディレクトリ**: コマンドを実行する場所を設定するには`<workingDirectory>`を使用します。

### まとめ
Exec Maven Pluginは多目的です：
- `exec:java`は、プロジェクトのクラスパスを活用してプロジェクトからJavaクラスを簡単に実行するために使用しますが、MavenのJVMで実行されます。
- `exec:exec`は、外部プログラムやカスタムJVMオプションを持つJava用に使用し、必要に応じて手動でクラスパスを管理する必要があります。
- `pom.xml`で設定し、手動で実行する（`mvn exec:java`または`mvn exec:exec`）か、`<executions>`でビルドフェーズにバインドします。

このセットアップにより、カスタム実行をMavenビルドプロセスにシームレスに統合できます！