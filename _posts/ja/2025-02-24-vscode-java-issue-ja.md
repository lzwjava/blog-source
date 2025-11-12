---
audio: false
generated: true
lang: ja
layout: post
title: Java言語サーバーとMavenビルド
translated: true
type: note
---

Visual Studio Code (VSCode) で2つの関連する問題に直面しているようですね。1つは Java 21 以上が必要であるというエラー、もう1つは Maven ビルドは成功するにもかかわらず、VSCode が Java コード内の一部のオブジェクト定義を認識しない問題です。段階的に解決していきましょう。

この問題は、VSCode の Java 拡張機能（具体的には Java Language Server）と Maven ビルドとで、Java Development Kit (JDK) のバージョンやプロジェクト設定が一致していないために発生しています。VSCode は正常に機能するために JDK 21 を必要としており、パースエラーは、Maven とは異なる方法でコードを解釈していることを示唆しています。以下の方法で修正できます。

---

### ステップ 1: JDK 21 のインストール
VSCode が明示的に Java 21 を要求しているため、システムにインストールされていることを確認する必要があります。

- **JDK 21 のダウンロード**: [Oracle のウェブサイト](https://www.oracle.com/java/technologies/javase-jdk21-downloads.html) や [Adoptium](https://adoptium.net/) などの信頼できるソースから入手してください。
- **インストール**: インストール手順に従い、インストールパス（例: Windows では `C:\Program Files\Java\jdk-21`、Linux では `/usr/lib/jvm/java-21-openjdk`）を確認してください。
- **確認**: ターミナルを開き、`java -version` を実行してください。以下のような表示がされるはずです:
  ```
  java version "21.0.1" ...
  ```

---

### ステップ 2: VSCode に JDK 21 を使用するよう設定する
VSCode の Java 拡張機能に JDK 21 を使用するよう指示する必要があります。方法は以下の通りです:

1. **VSCode 設定を開く**:
   - `ファイル > 基本設定 > 設定` に移動する（または `Ctrl + ,` を押す）。
2. **JDK パスを設定する**:
   - `java.jdt.ls.java.home` を検索する。
   - JDK 21 のインストールパス（例: `C:\Program Files\Java\jdk-21`）を入力する。
   - オプションで、`java.home` を検索し、一貫性のために同じパスを設定する。
3. **`settings.json` を編集する（別の方法）**:
   - コマンドパレット (`Ctrl + Shift + P`) を開き、「Preferences: Open Settings (JSON)」と入力して、以下を追加する:
     ```json
     {
         "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-21",
         "java.home": "C:\\Program Files\\Java\\jdk-21"
     }
     ```
   - システムに基づいてパスを調整する（Linux/Mac ではスラッシュ `/` を使用する）。

これにより、VSCode 内の Java Language Server が JDK 21 を使用し、最低要件を満たすようになります。

---

### ステップ 3: VSCode でプロジェクトの JDK を設定する
パースの問題（例: オブジェクト定義が見つからない）を修正するには、VSCode 内のプロジェクトも JDK 21 を使用していることを確認してください:

- `settings.json` で、プロジェクトに JDK 21 を指定するために以下を追加する:
  ```json
  "java.configuration.runtimes": [
      {
          "name": "JavaSE-21",
          "path": "C:\\Program Files\\Java\\jdk-21",
          "default": true
      }
  ]
  ```
- これにより、VSCode のプロジェクトランタイムが JDK 21 に一致し、コードを正しくパースするのに役立ちます。

---

### ステップ 4: Maven の JDK 設定を確認する
Maven ビルド (`mvn compile`) が正常に動作するのであれば、互換性のある JDK を使用している可能性が高いです。確認し、VSCode と一致させましょう:

1. **Maven の JDK を確認する**:
   - ターミナルで `mvn -version` を実行する。「Java version」の行（例: `Java version: 21.0.1`）を確認する。
   - JDK 21 を使用していない場合は、環境変数 `JAVA_HOME` を JDK 21 のパスに設定する:
     - **Windows**: `set JAVA_HOME=C:\Program Files\Java\jdk-21`
     - **Linux/Mac**: `export JAVA_HOME=/usr/lib/jvm/java-21-openjdk`
   - 再度 `mvn -version` を実行して確認する。
2. **`pom.xml` で JDK を指定する（オプション）**:
   - Maven プロジェクトで JDK 21 を強制したい場合は、`pom.xml` に以下を追加する:
     ```xml
     <properties>
         <maven.compiler.source>21</maven.compiler.source>
         <maven.compiler.target>21</maven.compiler.target>
     </properties>
     ```

---

### ステップ 5: VSCode をリフレッシュする
これらの変更を加えた後、VSCode をリフレッシュして適用する必要があります:

- VSCode を再読み込みする:
  - コマンドパレット (`Ctrl + Shift + P`) を開き、「Developer: Reload Window」を選択する。
- あるいは、VSCode を閉じて再度開く。

---

### ステップ 6: 依存関係が読み込まれていることを確認する
VSCode がまだオブジェクト定義を見つけられない場合、Maven の依存関係が正しく読み込まれていない可能性があります:

1. **ワークスペースをクリーンする**:
   - コマンドパレット (`Ctrl + Shift + P`) を開く。
   - 「Java: Clean Java Language Server Workspace」を実行する。
2. **コンパイルを強制する**:
   - コマンドパレットから「Java: Force Java Compilation」を実行する。
3. **インポートを確認する**:
   - VSCode で `pom.xml` を右クリックし、「Update Project Configuration」を選択して、プロジェクトの Maven 依存関係がインポートされていることを確認する。

---

### トラブルシューティング
問題が解決しない場合:
- **ログを確認する**:
  - `settings.json` に `"java.trace.server": "verbose"` を追加する。
  - 出力パネル (`Ctrl + Shift + U`) を開き、「Java Language Server」を選択して詳細なログを表示する。
- **コードを確認する**:
   - 見つからないオブジェクト定義が、外部の問題ではなく、あなたのコードまたは `pom.xml` にリストされた依存関係からのものであることを再確認する。

---

### まとめ
JDK 21 をインストールし、VSCode で使用するように設定し、プロジェクトと Maven の設定を一致させ、環境をリフレッシュすることで、VSCode は Java 21 に関するエラーを停止し、Maven の成功したコンパイルと一致するようにコードを正しくパースするはずです。何か問題が発生したらお知らせください！