---
audio: false
generated: true
lang: ja
layout: post
title: Maven プラグイン
translated: true
---

Maven プロジェクトで `org.codehaus.mojo` Exec Maven プラグインを使用するには、`pom.xml` ファイルで設定し、ビルドプロセス中にプログラムを実行する方法を決める必要があります。プラグインは、2つの主要な目標を提供します：`exec:exec` は外部プログラムを実行し、`exec:java` は Java クラスを実行します。以下に、設定と効果的に使用するための手順を案内します。

### ステップ 1: `pom.xml` にプラグインを追加
まず、`pom.xml` の `<build><plugins>` セクションに Exec Maven プラグインを含めます。`groupId`、`artifactId`、およびバージョン（現在最新のバージョンは `3.1.0`）を指定します。

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

これにより、プラグインがプロジェクトに追加されますが、設定を行ったり、目標を手動で実行したりするまで何も起こりません。

### ステップ 2: 目標を選択
プラグインは、2つの主要な目標を提供します：
- **`exec:exec`**: 外部プログラム（例：シェルスクリプト、バイナリ、または `java` コマンド）を実行します。
- **`exec:java`**: プロジェクトの `main` メソッドを持つ Java クラスを、Maven と同じ JVM で実行します。

これらの目標は、コマンドラインから手動で実行するか（例：`mvn exec:exec`）、Maven ビルドライフサイクルの特定のフェーズにバインドすることで使用できます。

### オプション 1: `exec:java` で Java プログラムを実行
プロジェクトから Java クラスを実行する場合は、`exec:java` 目標を使用します。これは、プロジェクトのランタイムクラスパス（依存関係を含む）を自動的に利用して、プロジェクトの一部であるクラスの `main` メソッドを実行するのに最適です。

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

これにより、`com.example.Main` が Maven と同じ JVM で実行され、Maven の JVM 設定が継承されます。

#### ビルド中の自動実行
ビルドフェーズ（例：`test`）中に自動的に実行するには、`<executions>` セクションを使用します：

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

これで、`mvn test` を実行すると、`com.example.Main` クラスが `test` フェーズ中に実行されます。

#### 引数やシステムプロパティの渡し方
`main` メソッドに引数を渡したり、システムプロパティを設定したりすることができます：

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

`exec:java` は Maven と同じ JVM で実行されるため、JVM オプション（例：`-Xmx`）は Maven の呼び出し方法（例：`mvn -Xmx512m exec:java`）から継承されます。

### オプション 2: `exec:exec` で外部プログラムを実行
シェルスクリプトやコマンドのような外部プログラムを実行するには、`exec:exec` 目標を使用します。

#### 手動実行
プラグインを設定してスクリプトを実行します：

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

次に、以下のように実行します：

```bash
mvn exec:exec
```

これにより、`myScript.sh` が指定された引数と作業ディレクトリで実行されます。

#### ビルド中の自動実行
フェーズにバインドして、統合テストのためにサーバーを起動および停止するなどします：

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

`mvn integration-test` を実行すると、テストの前にサーバーが起動し、その後に停止します。

#### カスタム JVM オプションで Java を実行
カスタム JVM オプションを使用して Java を実行する必要がある場合（`exec:java` と異なります）、`exec:exec` を `java` 実行可能ファイルと一緒に使用します。クラスパスは手動で管理する必要があります。以下は例です：

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

依存関係を含むクラスパスを追加するには、`maven-dependency-plugin` を使用して生成します：

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

クラスパスの区切り文字（Unix では `:`、Windows では `;`）を必要に応じて調整してください。

### 追加の設定オプション
- **環境変数**（`exec:exec` 用）：
  ```xml
  <configuration>
      <executable>myScript.sh</executable>
      <environmentVariables>
          <MY_VAR>value</MY_VAR>
      </environmentVariables>
  </configuration>
  ```
- **作業ディレクトリ**：コマンドが実行される場所を設定するには `<workingDirectory>` を使用します。

### まとめ
Exec Maven プラグインは多機能です：
- `exec:java` を使用して、プロジェクトのクラスパスを利用して簡単に Java クラスを実行しますが、Maven の JVM で実行されます。
- `exec:exec` を使用して、外部プログラムやカスタム JVM オプションを使用した Java を実行します。必要に応じてクラスパスを手動で管理します。
- `pom.xml` で設定し、手動で実行するか（`mvn exec:java` または `mvn exec:exec`）、`<executions>` を使用してビルドフェーズにバインドします。

この設定により、Maven ビルドプロセスにカスタム実行をシームレスに統合できます！