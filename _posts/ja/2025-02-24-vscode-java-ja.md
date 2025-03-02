---
audio: false
generated: true
lang: ja
layout: post
title: Java コンパイラを Visual Studio Code で設定する
translated: true
---

こんにちは！Visual Studio Code (VSCode) バージョン 1.96.4でJavaコンパイラを設定する方法を説明します。特に、Java Extension Packをすでにインストールしている場合、Java Development Kit (JDK) のパスを設定する必要があります。JavaコンパイラはJDKの一部であり、VSCodeはそれを見つける必要があります。以下に、設定方法の手順を示します。

---

### ステップ1: JDKがインストールされていることを確認
VSCodeで何かを設定する前に、WindowsマシンにJDK（JREではなく）がインストールされていることを確認してください。JDKにはJavaコンパイラ（`javac`）が含まれています。まだインストールしていない場合は、Oracle、OpenJDK、またはAdoptium（例：JDK 17またはプロジェクトに対応する他のバージョン）からダウンロードできます。インストール後、インストールパスをメモしてください（例：`C:\Program Files\Java\jdk-17.0.1`）。

---

### ステップ2: VSCodeの設定を開く
VSCodeにJDKの場所を教えるには、設定を調整する必要があります：

- **設定UIを使用する場合:**
  - `Ctrl + ,` を押して設定パネルを開きます。
  - または、`ファイル > 設定 > 設定`に移動します。
- **settings.jsonを使用する場合（オプション）:**
  - `Ctrl + Shift + P` を押してコマンドパレットを開きます。
  - 「Open Settings (JSON)」と入力し、選択して`settings.json`ファイルを直接編集します。

---

### ステップ3: `java.home`でJDKパスを設定
Java Extension Packは、コンパイルと言語機能（例：IntelliSense）のためにJDKを検索するために`java.home`設定を使用します。以下にその設定方法を示します：

- **設定UIを使用する場合:**
  - 設定パネルで「java.home」を検索します。
  - 「Java: Home」フィールドにJDKのインストールパスのフルパスを入力します。例：
    ```
    C:\Program Files\Java\jdk-17.0.1
    ```
  - Windowsであるため、バックスラッシュ（`\`）を使用し、パスがJDKのルートディレクトリを指していることを確認してください（`bin`フォルダに`javac.exe`が含まれているはずです）。

- **settings.jsonを使用する場合:**
  - `settings.json`を編集している場合は、以下の行を追加します（パスを実際のJDKの場所に置き換えてください）：
    ```json
    "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    ```
  - 例の完全な`settings.json`：
    ```json
    {
        "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    }
    ```
  - 編集後、ファイルを保存します。

---

### ステップ4: パスの確認
以下を確認してください：
- パスがJDK（JREではなく）を指していること。JDKの`bin`フォルダには`javac.exe`が含まれているはずです。
- パスにタイポがないこと、そしてインストール場所に一致していること（例：`C:\Program Files\Java\jdk-17.0.1`）。

JDKがインストールされている場所が不明な場合は、`C:\Program Files\Java`またはインストール時に選択した場所で見つけることができます。

---

### ステップ5: オプション - 複数のJDKを設定
複数のJDKバージョンをインストールしており、それらの間で切り替えたい場合（例：プロジェクトAにJDK 8、プロジェクトBにJDK 17を使用する場合）、`java.configuration.runtimes`設定を使用できます：

- `settings.json`に以下を追加します：
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
- `default: true`オプションは、コードの実行に使用するデフォルトランタイムを設定します。ただし、コンパイルにはJava拡張機能が`java.home`で指定されたJDKを主に使用します。

---

### ステップ6: VSCodeを再読み込みまたは再起動
`java.home`を設定した後、以下を実行する必要があるかもしれません：
- VSCodeウィンドウを再読み込み（`Ctrl + Shift + P`を押し、「Reload Window」と入力し、選択）
- または、変更が有効になるようにVSCodeを完全に再起動

---

### コンパイルに関する注意点
- **単一のJavaファイル:** 個々の`.java`ファイル（ビルドツールなし）を扱っている場合、「Language Support for Java(TM) by Red Hat」は`java.home`からJDKを使用してコードをコンパイルおよび実行します。「Run」ボタンまたは「Java: Run」コマンドを使用できます。
- **ビルドツールを使用するプロジェクト:** Maven、Gradle、または他のビルドツールを使用している場合、コンパイラはビルドツールの設定（例：`JAVA_HOME`環境変数、`pom.xml` for Maven、または`build.gradle` for Gradle）によって管理されます。ただし、`java.home`を設定することでVSCodeの言語機能が正しく動作することを確認します。

---

### トラブルシューティング
- **パスの問題:** VSCodeがJDKを見つけられない場合は、`java.home`のパスを確認してください。不要なスペースや引用符を避けるようにしてください。
- **JDKがインストールされていない:** `javac`が見つからないエラーが発生する場合は、JDKがインストールされていることを確認してください。
- **バージョンの互換性:** JDKバージョンがプロジェクトの要件と一致していることを確認してください（例：JDK 8、11、17）。

---

これで、VSCodeでJavaコンパイラが設定されました。問題が発生した場合や、特定のビルドツールを使用する方法について質問がある場合は、お知らせください。お手伝いできることがあれば、喜んでお手伝いします！ 😊

---

`maven.terminal.userJavaHome`を`true`に設定します。ターミナルでJavaバージョンを確認できます。