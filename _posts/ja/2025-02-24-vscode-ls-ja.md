---
audio: false
generated: true
lang: ja
layout: post
title: 'Java Language Server in Visual Studio Code


  Java言語サーバー in Visual Studio Code'
translated: true
---

こんにちは！`java.jdt.ls.java.home`設定は、Visual Studio Code (VSCode) の「Java Language Server」（「Language Support for Java(TM) by Red Hat」拡張機能の一部であり、Java Extension Packに含まれています）で使用される特定の設定オプションです。詳しく説明します。

---

### 意味
- **JDT**: 「Java Development Tools」の略で、元々はEclipse IDEの一部です。VSCodeのJava Language Serverは、EclipseのJDTに基づいており、コード補完、デバッグ、コンパイルなどの機能を提供します。
- **LS**: 「Language Server」の略で、VSCodeのJavaサポート（例：IntelliSense、エラーチェック）を実行するバックグラウンドプロセスです。
- **`java.jdt.ls.java.home`**: この設定は、Java Language Serverが操作に使用するJava Development Kit (JDK) の正確な場所を指定します。`java.home`設定とは異なりますが、関連しています。

簡単に言うと、`java.jdt.ls.java.home`は、Java Language Serverが使用するJDKのパスを指定し、以下の操作を行います：
- Javaコードを解析します。
- 言語機能（例：自動補完、定義への移動）を提供します。
- 一部の場合、コードをコンパイルおよび実行します（ただし、コンパイルは他の設定やビルドツールに依存することが多いです）。

---

### `java.home`との違い
- **`java.home`**: VSCodeの一般的な設定で、VSCode内のすべてのJava関連の拡張機能とタスクに対してJDKを指定します。他の設定で上書きされない限り使用されます。
- **`java.jdt.ls.java.home`**: より具体的な設定で、`java.home`をJava Language Serverのみ上書きします。この設定がなければ、Language Serverは`java.home`に戻ります。

したがって、`java.jdt.ls.java.home`を設定すると、Language Serverの操作に優先され、言語機能に異なるJDKを使用することができます。

---

### 設定方法
WindowsでVSCode 1.96.4とJava Extension Packを使用している場合、以下のように設定します：

1. **設定を開く:**
   - `Ctrl + ,`を押して設定UIを開くか、`Ctrl + Shift + P`を押して「Open Settings (JSON)」と入力して`settings.json`を編集します。

2. **パスを設定:**
   - **設定UIで:**
     - 「java.jdt.ls.java.home」を検索します。
     - JDKのフルパスを入力します（例：`C:\Program Files\Java\jdk-17.0.1`）。
   - **settings.jsonで:**
     - 次の行を追加します（JDKのパスに置き換えます）：
       ```json
       "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
       ```
     - 例の`settings.json`：
       ```json
       {
           "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
       }
       ```

3. **JDKパスの確認:**
   - パスが`bin`ディレクトリを含むJDKフォルダを指していることを確認します（`javac.exe`と`java.exe`を含む）。

4. **VSCodeの再読み込み:**
   - ウィンドウを再読み込み（`Ctrl + Shift + P` > "Reload Window"）またはVSCodeを再起動して変更を適用します。

---

### 使用時機
通常、`java.jdt.ls.java.home`を設定するのは以下の場合です：
- 複数のJDKがインストールされている場合で、Language Serverに特定のJDK（例：JDK 17）を使用させ、他のJavaタスク（例：コードの実行）は異なるJDKを`java.home`経由で使用する場合。
- Language Serverの問題をトラブルシューティングする場合（例：適切なJDKが自動的に選択されない場合）。
- プロジェクトが言語機能に対して特定のJDKバージョンを必要とする場合。

設定しない場合、Language Serverは`java.home`（またはシステムの`JAVA_HOME`環境変数を最終手段として）からJDKを使用します。

---

### 実践例
JDK 8とJDK 17がインストールされている場合：
- 一般的な使用に対して`"java.home": "C:\\Program Files\\Java\\jdk1.8.0_291"`を設定します。
- Language ServerがJDK 17を使用して最新のJava構文サポートを得るために`"java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"`を設定します。

このようにして、JDK 8でデバッグ/実行を行いながら、JDK 17の機能を言語サポートとして得ることができます。

---

これでわかりますか？設定がどのように組み合わさるか、またはさらに調整する必要がある場合は、お知らせください！ 😊