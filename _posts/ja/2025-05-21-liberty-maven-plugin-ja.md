---
audio: false
generated: true
lang: ja
layout: post
title: リバティメイヴンプラグイン
translated: true
type: note
---

あなたの目標である、Libertyサーバーを迅速に管理しプログラムをビルドするスクリプトをIntelliJ IDEAでWindows上で実行し、EARファイルを置き換える前にサーバーが確実に停止されている状態にするためには、**Liberty Maven Plugin**の使用をお勧めします。この方法は直接的で、Mavenビルドプロセスとよく統合され、コマンドのフォーマットやバッチファイルに関するあなたが遭遇した問題を回避できます。

設定方法は以下の通りです：

---

### 解決策：Liberty Maven Pluginの使用

#### ステップ 1: Liberty Maven Pluginを`pom.xml`に追加する
Liberty Maven Pluginを使用すると、Mavenから直接Libertyサーバー（起動、停止、デプロイなど）を制御できます。これにより、複雑なスクリプトやバッチファイルが不要になります。

- プロジェクトの`pom.xml`ファイルを開きます。
- `<build>`セクション内に以下のプラグイン設定を追加します：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>io.openliberty.tools</groupId>
            <artifactId>liberty-maven-plugin</artifactId>
            <version>3.3.4</version>
            <configuration>
                <serverName>default</serverName>
                <installDirectory>C:\path\to\liberty</installDirectory>
            </configuration>
        </plugin>
    </plugins>
</build>
```

- `C:\path\to\liberty`は、実際のLibertyインストールディレクトリへのパス（例: `C:\Program Files\IBM\WebSphere\Liberty`）に**置き換えてください**。
- `<serverName>default</serverName>`は、`server start default`および`server stop default`コマンドでの`default`の使用と一致します。

#### ステップ 2: IntelliJ IDEAでMaven実行構成を作成する
スクリプトやバッチファイルを使用する代わりに、IntelliJ IDEAを設定して、サーバーを停止し、プロジェクトをビルドし、サーバーを再起動する一連のMavenゴールを実行できます。

- IntelliJ IDEAで、**Run > Edit Configurations...**に移動します。
- **+** ボタンをクリックし、リストから**Maven**を選択します。
- 実行構成を設定します：
  - **Name:** 意味のある名前を付けます（例: `Run Liberty`）。
  - **Working directory:** プロジェクトディレクトリに設定されていることを確認します（通常は自動検出されます）。
  - **Command line:** 以下の一連のMavenゴールを入力します：
    ```
    liberty:stop package liberty:start
    ```
- **Apply**をクリックし、次に**OK**をクリックします。

#### ステップ 3: 構成を実行する
- IntelliJ IDEAの**Run**ボタン（緑色の三角）を使用してこの構成を実行します。
- これにより以下が実行されます：
  1. **Libertyサーバーを停止** (`liberty:stop`): EARファイルが置き換えられる際にサーバーが実行されていないことを保証します。
  2. **プロジェクトをビルド** (`package`): EARファイルを生成するために`mvn package`を実行します。
  3. **Libertyサーバーを起動** (`liberty:start`): 更新されたEARファイルでサーバーを再起動します。

---

### この方法が有効な理由
- **コマンドフォーマットの問題を修正:** 実行構成で「Script text」を使用すると`server start default`が別々の引数（`server`、`start`、`default`）に分割されるとのことでした。Mavenアプローチでは、明確に定義されたプラグインゴールを使用するため、この問題を完全に回避できます。
- **バッチファイルの複雑さを回避:** 正しく動作する`.bat`ファイルを作成するのが難しい（パスや環境設定が原因など）とのことでした。Liberty Maven Pluginはサーバー管理を内部で処理するため、バッチファイルのコマンドやパスのデバッグは不要です。
- **あなたの要件を満たす:** EARファイルを置き換える際にサーバーが停止されている必要があり、起動時の問題を避けたいという要件を満たします。この解決策は、ビルド前に明示的にサーバーを停止し、その後で起動するため、クリーンなプロセスを保証します。

---

### 代替案：バッチファイルの使用（もし希望すれば）
もしバッチファイルに固執したい場合は、以下に動作する例を示します。ただし、あなたが直面した問題により、これはあまりお勧めできません：

1. プロジェクトディレクトリに`runLiberty.bat`という名前のファイルを作成し、以下の内容を記述します：

```bat
@echo off
set LIBERTY_BIN=C:\path\to\liberty\bin
set MAVEN_HOME=C:\path\to\maven
set PATH=%PATH%;%LIBERTY_BIN%;%MAVEN_HOME%\bin

"%LIBERTY_BIN%\server" stop default
mvn package
"%LIBERTY_BIN%\server" start default
```

- `C:\path\to\liberty`および`C:\path\to\maven`は、実際のLibertyおよびMavenのインストール先へのパスに置き換えてください。

2. IntelliJ IDEAで：
   - **Run > Edit Configurations...**に移動します。
   - **+** をクリックし、**Batch file**を選択します。
   - **Path to batch file**を`runLiberty.bat`の場所に設定します。
   - **Working directory**をプロジェクトディレクトリに設定します。
   - **Apply**および**OK**をクリックします。

3. **Run**ボタンを使用して実行します。

ただし、この方法では、パスと環境変数が正しいことを手動で確認する必要があり、これは難しいと感じられた点です。Mavenプラグインアプローチの方がより簡単で信頼性があります。

---

### 推奨事項
上記で概説した**Liberty Maven Plugin**の方法を使用してください。それは：
- **統合的:** 既存のMavenビルドプロセスに組み込まれます。
- **シンプル:** バッチファイルの構文やパスに悩む必要がありません。
- **信頼性が高い:** サーバーの停止と起動を正しく処理し、EARファイルの置き換えに関する問題を回避します。

この設定により、IntelliJ IDEAでLibertyサーバー上でプログラムを迅速かつ一貫して実行できるようになります！