---
audio: false
generated: true
lang: ja
layout: post
title: Visual Studio CodeでのJavaコンパイラ設定
translated: true
type: note
---

こんにちは！WindowsでVisual Studio Code（VSCode）バージョン1.96.4のJavaコンパイラを設定するには、特にJava Extension Packを既にインストールしている場合、Java Development Kit（JDK）のパスを設定する必要があります。JavaコンパイラはJDKの一部であり、VSCodeがJavaコードをコンパイルするためにはその場所を知っている必要があります。以下に設定手順を説明します：

---

### ステップ1: JDKがインストールされていることを確認する
VSCodeで設定を行う前に、WindowsマシンにJDK（JREだけでなく）がインストールされていることを確認してください。JDKにはJavaコンパイラ（`javac`）が含まれています。まだインストールしていない場合は、Oracle、OpenJDK、Adoptiumなどのプロバイダーからダウンロードできます（例：JDK 17またはプロジェクトに互換性のある別のバージョン）。インストール後、インストールパスをメモしてください（例：`C:\Program Files\Java\jdk-17.0.1`）。

---

### ステップ2: VSCodeの設定を開く
VSCodeにJDKの場所を伝えるには、設定を調整する必要があります：

- **設定UIを使用：**
  - `Ctrl + ,`を押して設定パネルを開きます。
  - または、`ファイル > 基本設定 > 設定`に移動します。
- **settings.jsonを使用（オプション）：**
  - `Ctrl + Shift + P`を押してコマンドパレットを開きます。
  - **"Open Settings (JSON)"**と入力し、選択して`settings.json`ファイルを直接編集します。

---

### ステップ3: `java.home`でJDKパスを設定する
Java Extension Packは、コンパイルと言語機能（IntelliSenseなど）のためにJDKを見つけるために`java.home`設定に依存しています。設定方法は以下の通りです：

- **設定UIで：**
  - 設定パネルで**"java.home"**を検索します。
  - 「Java: Home」フィールドに、JDKのインストール先の完全なパスを入力します。例：
    ```
    C:\Program Files\Java\jdk-17.0.1
    ```
  - Windowsなのでバックスラッシュ（`\`）を使用し、パスがJDKのルートディレクトリを指していることを確認してください（`javac.exe`を含む`bin`フォルダがあるはずです）。

- **settings.jsonで：**
  - `settings.json`を編集する場合、この行を追加します（パスは実際のJDKの場所に置き換えてください）：
    ```json
    "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    ```
  - 完全な`settings.json`の例：
    ```json
    {
        "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    }
    ```
  - 編集後、ファイルを保存します。

---

### ステップ4: パスを確認する
以下をダブルチェックしてください：
- パスがJDK（JREではない）を指していること。JDKの`bin`フォルダには`javac.exe`が含まれているはずです。
- パスにタイプミスがなく、JDKのインストール場所と一致していること（例：`C:\Program Files\Java\jdk-17.0.1`）。

JDKがどこにインストールされているかわからない場合は、`C:\Program Files\Java`またはインストール時に選択した場所を確認してください。

---

### ステップ5: オプション - 複数のJDKを設定する
複数のJDKバージョンがインストールされており、切り替えたい場合（例：あるプロジェクトではJDK 8、別のプロジェクトではJDK 17）、`java.configuration.runtimes`設定を使用できます：

- `settings.json`にこれを追加します：
  ```json
  "java.configuration.runtimes": [
      {
          "name": "JavaSE-1.8",
          "path": "C:\\Program Files\\Java\\jdk1.8.0_291"
      },
      {
          "name": "JavaSE-17",
          "path": "C:\\Program Files\\Java\\jdk-17.0.1",
          "default": true
      }
  ]
  ```
- `default: true`オプションは、コードを実行するためのデフォルトのランタイムを設定します。ただし、コンパイルの場合、Java拡張機能は主に`java.home`で指定されたJDKを使用します。

---

### ステップ6: VSCodeをリロードまたは再起動する
`java.home`を設定した後、以下の操作が必要な場合があります：
- VSCodeウィンドウをリロードする（`Ctrl + Shift + P`を押し、**"Reload Window"**と入力して選択）。
- または、変更を反映させるためにVSCodeを完全に再起動する。

---

### コンパイルに関する注意点
- **単一のJavaファイル：** 個々の`.java`ファイル（ビルドツールなし）を扱う場合、Java Extension Packの「Language Support for Java(TM) by Red Hat」は`java.home`のJDKを使用してコードをコンパイルおよび実行します。「実行」ボタンまたは**"Java: Run"**コマンドを使用できます。
- **ビルドツールを使用するプロジェクト：** Maven、Gradle、または別のビルドツールを使用している場合、コンパイラはビルドツールの設定（例：`JAVA_HOME`環境変数、Mavenの`pom.xml`、Gradleの`build.gradle`）によって管理されます。ただし、`java.home`を設定することで、VSCodeの言語機能が正しく動作することが保証されます。

---

### トラブルシューティング
- **パスに関する問題：** VSCodeがJDKを見つけられない場合、`java.home`のパスをダブルチェックしてください。余分なスペースや引用符は避けてください。
- **JDKがインストールされていない：** `javac`が見つからないというエラーが発生した場合は、JDKがインストールされていることを確認してください。
- **バージョンの互換性：** JDKのバージョンがプロジェクトの要件（例：JDK 8、11、17）と一致していることを確認してください。

---

以上です！これでVSCodeでJavaコンパイラが設定されたはずです。問題が発生した場合、または特定のビルドツールの使用などについてさらに質問がある場合は、お気軽にお知らせください。喜んでお手伝いします！😊

---

`maven.terminal.userJavaHome`をtrueに設定してください。ターミナルでJavaのバージョンを確認できます。