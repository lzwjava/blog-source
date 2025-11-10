---
audio: false
generated: true
lang: ja
layout: post
title: JShellクイックガイド
translated: true
type: note
---

JShellはJDK 9以降のJava Development Kit（JDK）に含まれるインタラクティブなREPL（Read-Eval-Print Loop）ツールです。完全なプログラムを書く必要なく、Javaコードのスニペットを対話的に実行できます。以下はJShellの使い方に関する簡潔なガイドです：

### 1. **JShellの起動**
- **JDKのインストール確認**: JDK 9以降がインストールされていることを確認してください。ターミナルまたはコマンドプロンプトで `java -version` を実行して確認できます。
- **JShellの起動**:
  - ターミナルまたはコマンドプロンプトを開きます。
  - `jshell` と入力してEnterキーを押します。
  - `jshell>` のようなプロンプトが表示され、JShellの準備が整ったことを示します。

### 2. **基本的な使い方**
- **Javaコードの実行**:
  - プロンプトでJavaの式、文、または宣言を直接入力します。
  - 例:
    ```java
    jshell> System.out.println("Hello, JShell!")
    Hello, JShell!
    ```
  - JShellは入力を評価し、即座に結果を表示します。

- **変数と式**:
  - 変数を宣言したり式を評価したりします:
    ```java
    jshell> int x = 10
    x ==> 10
    jshell> x * 2
    $2 ==> 20
    ```
  - JShellは式の結果に一時的な名前（例: `$2`）を自動的に割り当てます。

- **メソッドとクラスの定義**:
  - メソッドやクラスを定義できます:
    ```java
    jshell> void sayHello() { System.out.println("Hello!"); }
    |  created method sayHello()
    jshell> sayHello()
    Hello!
    ```
    ```java
    jshell> class Test { int x = 5; }
    |  created class Test
    jshell> Test t = new Test()
    t ==> Test@7c417213
    jshell> t.x
    $5 ==> 5
    ```

### 3. **主要なコマンド**
JShellは `/` で始まる組み込みコマンドを提供します。以下はいくつかの必須コマンドです：
- **すべてのコードをリスト**: `/list` – セッションで入力されたすべてのスニペットを表示します。
  ```java
  jshell> /list
  ```
- **コードの編集**: `/edit <id>` – 指定されたID（`/list` から取得）のスニペットに対してGUIエディタを開きます。
- **セッションの保存**: `/save myfile.java` – すべてのスニペットをファイルに保存します。
- **ファイルの読み込み**: `/open myfile.java` – ファイルからコードを読み込んで実行します。
- **変数の表示**: `/vars` – 宣言されたすべての変数をリストします。
  ```java
  jshell> /vars
  |    int x = 10
  ```
- **メソッドの表示**: `/methods` – 定義されたすべてのメソッドをリストします。
- **JShellの終了**: `/exit` – JShellセッションを閉じます。
- **ヘルプ**: `/help` – 利用可能なすべてのコマンドを表示します。

### 4. **パッケージのインポート**
- JShellは一般的なパッケージ（例: `java.util`, `java.io`）を自動的にインポートします。他のパッケージを使用するには、手動でインポートします：
  ```java
  jshell> import java.time.LocalDate
  jshell> LocalDate.now()
  $3 ==> 2025-06-27
  ```

### 5. **コードの編集と修正**
- **既存のコードの変更**:
  - `/list` を使用してスニペットのIDを検索します。
  - 新しいバージョンを入力して再定義します。JShellは古い定義を上書きします。
    ```java
    jshell> int x = 5
    x ==> 5
    jshell> int x = 10
    x ==> 10
    ```
- **スニペットの削除**: `/drop <id>` – 特定のスニペットをIDで削除します。

### 6. **タブ補完**
- `Tab` キーを押して、クラス名、メソッド、またはコマンドを自動補完します。
- 例:
  ```java
  jshell> System.out.pr<tab>
  ```
  これは `println`, `print` などを提案します。

### 7. **外部スクリプトの実行**
- Javaファイルを読み込んで実行します:
  ```java
  jshell> /open MyScript.java
  ```
- スクリプトを指定してJShellを起動することもできます:
  ```bash
  jshell MyScript.java
  ```

### 8. **JShellのカスタマイズ**
- **スタートアップスクリプト**: インポートや共通コードを含むファイル（例: `startup.jsh`）を作成し、`/open startup.jsh` で読み込むか、デフォルトのスタートアップスクリプトとして設定します:
  ```bash
  jshell --start startup.jsh
  ```
- **フィードバックモード**: `/set feedback <mode>`（例: `normal`, `concise`, `verbose`）で出力の詳細度を調整します。

### 9. **ヒント**
- **迅速なプロトタイピング**: JShellを使用して小さなコードスニペットをテストしたり、APIを実験したり、Java構文を学んだりします。
- **エラーハンドリング**: JShellは明確なエラーメッセージを提供し、その場でミスを修正できます。
- **複数行入力**: 複雑なコードの場合、JShellは複数行編集をサポートします。行末にバックスラッシュ（`\`）を付けて続行します:
  ```java
  jshell> int sum(int a, int b) { \
      ...> return a + b; \
      ...> }
  ```

### 10. **トラブルシューティング**
- **JShellが見つからない**: JDKの `bin` ディレクトリがシステムのPATHに含まれていることを確認してください。
- **起動が遅い**: 一部のシステムでは、JShellの初期化に時間がかかる場合があります。JDKが最新であることを確認してください。
- **セッションのリセット**: `/reset` を使用してすべてのスニペットをクリアし、新しく開始します。

詳細については、公式のJDKドキュメントを参照するか、JShellで `/help` を実行してください。JShellで試したい特定のタスクやコードがある場合は、お知らせいただければさらに詳しく案内します！