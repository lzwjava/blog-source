---
audio: false
generated: true
lang: ja
layout: post
title: Visual Studio Code の Java 言語サーバー
translated: true
type: note
---

こんにちは！Visual Studio Code（VSCode）の `java.jdt.ls.java.home` 設定は、Java Language Server（「Language Support for Java(TM) by Red Hat」拡張機能の一部で、Java Extension Pack に含まれています）によって使用される特定の設定オプションです。詳しく見ていきましょう：

---

### 意味する内容
- **JDT**: 「Java Development Tools」の略で、元々は Eclipse IDE の一部でした。VSCode の Java Language Server は Eclipse の JDT を基にしており、コード補完、デバッグ、コンパイルなどの機能を提供します。
- **LS**: 「Language Server」の略で、VSCode の Java サポート（IntelliSense、エラーチェックなど）を支えるバックグラウンドプロセスです。
- **`java.jdt.ls.java.home`**: この設定は、Java Language Server がその操作に使用する Java Development Kit（JDK）を正確に指定します。より広範な `java.home` 設定とは異なりますが、関連しています。

要するに、`java.jdt.ls.java.home` は、Java Language Server が以下を行うために使用する JDK のパスを指定します：
- Java コードの解析
- 言語機能の提供（オートコンプリート、定義へ移動など）
- 場合によってはコードのコンパイルと実行（ただしコンパイルは他の設定やビルドツールに依存することが多い）

---

### `java.home` との違い
- **`java.home`**: VSCode 内のすべての Java 関連拡張機能とタスクに使用する JDK を指す一般的な VSCode 設定です。より具体的な設定で上書きされない限り使用されます。
- **`java.jdt.ls.java.home`**: Java Language Server 専用に `java.home` を上書きする、より具体的な設定です。これが設定されていない場合、Language Server は `java.home` にフォールバックします。

したがって、`java.jdt.ls.java.home` を設定すると、Language Server の操作ではそれが優先され、言語機能用に実行やデバッグタスクとは異なる JDK を使用できるようになります。

---

### 設定方法
Windows で VSCode 1.96.4 と Java Extension Pack を使用している場合、以下の方法で設定できます：

1. **設定を開く:**
   - 設定 UI の場合は `Ctrl + ,` を押すか、`Ctrl + Shift + P` を押して **"Open Settings (JSON)"** と入力し、`settings.json` を編集します。

2. **パスを設定:**
   - **設定 UI の場合:**
     - **"java.jdt.ls.java.home"** を検索します。
     - JDK へのフルパスを入力します（例: `C:\Program Files\Java\jdk-17.0.1`）。
   - **settings.json の場合:**
     - この行を追加します（JDK パスに置き換えてください）：
       ```json
       "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
       ```
     - `settings.json` の例：
       ```json
       {
           "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
       }
       ```

3. **JDK パスを確認:**
   - パスが `javac.exe` と `java.exe` を含む `bin` ディレクトリがある JDK フォルダを指していることを確認してください。

4. **VSCode を再読み込み:**
   - ウィンドウを再読み込みする（`Ctrl + Shift + P` > "Reload Window"）か、VSCode を再起動して変更を適用します。

---

### いつ使用するか
通常、以下の場合に `java.jdt.ls.java.home` を設定します：
- 複数の JDK がインストールされており、Language Server に特定の JDK（例: JDK 17）を使用させたいが、他の Java タスク（コードの実行など）では `java.home` 経由で異なる JDK を使用する場合。
- Language Server の問題（適切な JDK を自動的に認識しないなど）のトラブルシューティングを行う場合。
- プロジェクトが言語機能に対して特定の JDK バージョンを要求する場合。

設定しない場合、Language Server は `java.home` の JDK（または最終的にはシステムの `JAVA_HOME` 環境変数）を使用します。

---

### 実践例
JDK 8 と JDK 17 がインストールされているとします：
- 一般的な使用のために `"java.home": "C:\\Program Files\\Java\\jdk1.8.0_291"` を設定します。
- Language Server がモダンな Java 構文サポートのために JDK 17 を使用することを保証するために、`"java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"` を設定します。

このようにすると、JDK 8 でデバッグ/実行しながら、JDK 17 の機能に対する言語サポートを得ることができます。

---

これでわかりましたか？この設定があなたの環境にどのように適合するか、またはさらに調整するためのヘルプが必要な場合は、お知らせください！😊