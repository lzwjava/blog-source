---
audio: false
generated: false
lang: ja
layout: post
title: Java言語サーバーとMavenビルド
translated: true
---

Visual Studio Code (VSCode) で 2 つの関連する問題に直面しているようです：Java 21 が必要であるという警告と、VSCode が Java コードの一部のオブジェクト定義を認識しない問題です。Maven ビルドは成功しているにもかかわらずです。これをステップバイステップで解決しましょう。

この問題は、VSCode の Java 拡張機能（特に Java Language Server）と Maven ビルドが JDK バージョンやプロジェクト設定で一致していないために発生します。VSCode は正しく機能するために JDK 21 が必要であることを示しており、解析エラーは Maven と同じようにコードを解釈していないことを示唆しています。以下に修正方法を示します。

---

### ステップ 1: JDK 21 をインストール
VSCode が明示的に Java 21 を要求しているため、システムにインストールされていることを確認する必要があります。

- **JDK 21 をダウンロード**: [Oracle のウェブサイト](https://www.oracle.com/java/technologies/javase-jdk21-downloads.html) または [Adoptium](https://adoptium.net/) から取得します。
- **インストール**: インストール手順に従い、インストールパスをメモします（例：Windows の `C:\Program Files\Java\jdk-21` または Linux の `/usr/lib/jvm/java-21-openjdk`）。
- **確認**: ターミナルを開き、`java -version` を実行します。以下のように表示されるはずです：
  ```
  java version "21.0.1" ...
  ```

---

### ステップ 2: VSCode を JDK 21 を使用するように設定
VSCode の Java 拡張機能に JDK 21 を使用するように指示する必要があります。以下のようにします：

1. **VSCode の設定を開く**:
   - `ファイル > 設定 > 設定` に移動します（または `Ctrl + ,` を押します）。
2. **JDK パスを設定**:
   - `java.jdt.ls.java.home` を検索します。
   - JDK 21 のインストールパスを入力します（例：`C:\Program Files\Java\jdk-21`）。
   - 一貫性を保つために、`java.home` を同じパスに設定することもできます。
3. **`settings.json` を編集（代替方法）**:
   - コマンドパレットを開き（`Ctrl + Shift + P`）、「Preferences: Open Settings (JSON)」と入力し、以下を追加します：
     ```json
     {
         "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-21",
         "java.home": "C:\\Program Files\\Java\\jdk-21"
     }
     ```
   - システムに応じてパスを調整します（Linux/Mac の場合はスラッシュ `/` を使用）。

これにより、VSCode の Java Language Server が JDK 21 を使用し、最低要件を満たすことができます。

---

### ステップ 3: VSCode でプロジェクトの JDK を設定
解析問題（例：オブジェクト定義が見つからない）を修正するために、VSCode のプロジェクトが JDK 21 を使用していることを確認します：

- `settings.json` に以下を追加して、プロジェクトに JDK 21 を指定します：
  ```json
  "java.configuration.runtimes": [
      {
          "name": "JavaSE-21",
          "path": "C:\\Program Files\\Java\\jdk-21",
          "default": true
      }
  ]
  ```
- これにより、VSCode のプロジェクトランタイムが JDK 21 に一致し、コードを正しく解析するのに役立ちます。

---

### ステップ 4: Maven の JDK 設定を確認
Maven ビルド (`mvn compile`) が正常に動作しているため、互換性のある JDK を使用している可能性が高いです。VSCode と一致させるために確認します：

1. **Maven の JDK を確認**:
   - ターミナルで `mvn -version` を実行し、「Java version」行を確認します（例：`Java version: 21.0.1`）。
   - JDK 21 を使用していない場合、`JAVA_HOME` 環境変数を JDK 21 のパスに設定します：
     - **Windows**: `set JAVA_HOME=C:\Program Files\Java\jdk-21`
     - **Linux/Mac**: `export JAVA_HOME=/usr/lib/jvm/java-21-openjdk`
   - 再度 `mvn -version` を実行して確認します。
2. **`pom.xml` で JDK を指定（任意）**:
   - Maven プロジェクトで JDK 21 を強制する場合、`pom.xml` に以下を追加します：
     ```xml
     <properties>
         <maven.compiler.source>21</maven.compiler.source>
         <maven.compiler.target>21</maven.compiler.target>
     </properties>
     ```

---

### ステップ 5: VSCode をリフレッシュ
これらの変更を適用するために、VSCode をリフレッシュする必要があります：

- VSCode をリロード：
  - コマンドパレットを開き（`Ctrl + Shift + P`）、「Developer: Reload Window」を選択します。
- 代替方法として、VSCode を閉じて再度開きます。

---

### ステップ 6: 依存関係が読み込まれていることを確認
VSCode が依然としてオブジェクト定義を見つけられない場合、Maven 依存関係が正しく読み込まれていない可能性があります：

1. **ワークスペースをクリーン**:
   - コマンドパレットを開き（`Ctrl + Shift + P`）、「Java: Clean Java Language Server Workspace」を実行します。
2. **強制コンパイル**:
   - コマンドパレットから「Java: Force Java Compilation」を実行します。
3. **インポートを確認**:
   - VSCode で `pom.xml` を右クリックし、「Update Project Configuration」を選択して、プロジェクトの Maven 依存関係がインポートされていることを確認します。

---

### トラブルシューティング
問題が解決しない場合：
- **ログを確認**:
  - `settings.json` に `"java.trace.server": "verbose"` を追加します。
  - 出力パネルを開き（`Ctrl + Shift + U`）、「Java Language Server」を選択して詳細なログを表示します。
- **コードを確認**:
  - 見つからないオブジェクト定義がコードまたは `pom.xml` にリストされている依存関係から来ていることを確認します。

---

### まとめ
JDK 21 をインストールし、VSCode をその使用に設定し、プロジェクトと Maven の設定を一致させ、環境をリフレッシュすることで、VSCode は Java 21 に関する警告を止め、Maven の成功したコンパイルと同じようにコードを正しく解析するはずです。何か問題があれば教えてください！