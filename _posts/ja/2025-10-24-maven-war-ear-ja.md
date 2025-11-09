---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Maven WARおよびEARモジュール設定
translated: true
type: note
---

### WARからEARへのMavenマルチモジュールプロジェクト設定

Mavenで、1つのモジュールがWAR（例：Webアプリケーション）を生成し、別のモジュールがそれをEAR（Enterprise Archive）に組み立てるようにするには、マルチモジュールプロジェクト構造を使用します。EARモジュールは`maven-ear-plugin`を介してWARモジュールに依存します。これにより、ビルド中にWARがEARに含まれることが保証されます。

#### ステップ1: 親POMの作成
親POMはモジュールを定義し、共有設定を管理します。パッケージングを`pom`に設定します。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>parent</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <modules>
        <module>web-module</module>  <!-- これを最初にビルド -->
        <module>ear-module</module>
    </modules>

    <!-- オプション: 共有依存関係とプラグインバージョン -->
    <dependencyManagement>
        <dependencies>
            <!-- 子モジュールのバージョンをここで定義 -->
        </dependencies>
    </dependencyManagement>

    <build>
        <pluginManagement>
            <plugins>
                <!-- プラグインバージョンの管理 -->
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-ear-plugin</artifactId>
                    <version>3.3.0</version>
                </plugin>
            </plugins>
        </pluginManagement>
    </build>
</project>
```

#### ステップ2: WARモジュールの設定
このモジュールはWebアプリケーションをWARとしてビルドします。パッケージングを`war`に設定します。ここでは特別なEAR設定は必要ありません。最初にビルドされるだけで十分です。

ディレクトリ構造: `web-module/pom.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.example</groupId>
        <artifactId>parent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>web-module</artifactId>
    <packaging>war</packaging>

    <dependencies>
        <!-- Web依存関係を追加（例：servlet-api） -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.2</version>
            </plugin>
        </plugins>
    </build>
</project>
```

#### ステップ3: EARモジュールの設定
このモジュールはEARを組み立てます。パッケージングを`ear`に設定し、`maven-ear-plugin`を使用してWARモジュールを参照します。このプラグインはWARアーティファクトを取得し、EARにバンドルします。

ディレクトリ構造: `ear-module/pom.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.example</groupId>
        <artifactId>parent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>ear-module</artifactId>
    <packaging>ear</packaging>

    <dependencies>
        <!-- WARモジュールに依存してビルドに含める -->
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>web-module</artifactId>
            <version>${project.version}</version>
            <type>war</type>
        </dependency>
        <!-- オプション: EJBや他のモジュールを必要に応じて追加 -->
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-ear-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <!-- EARバージョン（例：Java EE用） -->
                    <version>8</version>
                    
                    <!-- EAR内のライブラリディレクトリ -->
                    <defaultLibBundleDir>lib</defaultLibBundleDir>
                    
                    <!-- スキニーWAR（EARライブラリに既にある依存関係を除外） -->
                    <skinnyWars>true</skinnyWars>
                    
                    <!-- 含めるモジュールを定義 -->
                    <modules>
                        <webModule>
                            <groupId>com.example</groupId>
                            <artifactId>web-module</artifactId>
                            <bundleDir>/</bundleDir>  <!-- EARのルート -->
                            <contextRoot>/mywebapp</contextRoot>  <!-- デプロイメントコンテキスト -->
                        </webModule>
                        <!-- 必要に応じて<ejbModule>や<jarModule>を追加 -->
                    </modules>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### ステップ4: プロジェクトのビルド
- **親ディレクトリ**から実行: `mvn clean install`
  - これによりモジュールが順番にビルドされます（最初にWAR、次にEAR）。
- EARは`ear-module/target/ear-module-1.0-SNAPSHOT.ear`に生成されます。
- EARのみをビルドする場合（WARが既にビルド済みと仮定）: `cd ear-module && mvn clean package`。

#### 主な注意点
- **ビルド順序**: 親の`<modules>`でWARモジュールをEARの前にリストして、Mavenが最初にWARをビルドするようにします。
- **依存関係**: EARモジュールのWARへの`<dependency>`により、パッケージング中に解決されます。
- **カスタマイズ**: WebアプリのURLパスには`<contextRoot>`を調整します。`<modules>`にさらにモジュール（例：EJB JAR）を追加します。
- **トラブルシューティング**: WARが含まれない場合、アーティファクト座標が正確に一致しているか確認します。EARモジュールで`mvn dependency:tree`を使用して検証します。

詳細は、公式のMaven EARプラグインのドキュメントを参照してください。

[Apache Maven EAR Plugin](https://maven.apache.org/plugins/maven-ear-plugin/)  
[Maven Multi-Module Projects](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html#Multi-module_Projects)