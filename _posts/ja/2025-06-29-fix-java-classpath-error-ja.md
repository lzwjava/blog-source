---
audio: false
generated: true
lang: ja
layout: post
title: Javaクラスパスエラーの修正
translated: true
type: note
---

発生したエラー（`Could not find or load main class scripts.benchmark.MultiMark`）は、プロジェクトのルートディレクトリ（`~/projects/lzwjava.github.io`）から完全修飾クラス名（`scripts.benchmark.MultiMark`）を使用してJavaプログラムを実行しようとしたためです。Javaランタイムは、パッケージ構造が開始するディレクトリからクラスを実行することを期待するか、クラスパスを正しく指定する必要があります。`scripts/benchmark` ディレクトリに移動して `java MultiMark` を実行したときに動作したのは、コマンドに対してクラスが正しいディレクトリにあったためです。

プロジェクトのルートディレクトリ（`~/projects/lzwjava.github.io`）からディレクトリを変更せずに `MultiMark.java` または `MultiMark.class` を実行するには、`java` コマンドで `-cp`（クラスパス）オプションを使用して、コンパイルされたクラスファイルの場所をJavaに伝えることができます。以下に、ルートディレクトリに留まったままこれを実現する2つの方法を示します。

---

### **オプション1: クラスパスを指定してコンパイル済みクラスを実行**
`MultiMark.class` が `scripts/benchmark/` に既に存在する場合（`ls` の出力に示されているように）、クラスパスを指定することでルートディレクトリから実行できます。

1. **ルートディレクトリに留まる**
   `~/projects/lzwjava.github.io` にいることを確認してください。

2. **プログラムを実行**
   `-cp` オプションを使用して、クラスファイルを含むディレクトリを指定します：
   ```bash
   java -cp scripts/benchmark MultiMark
   ```
   - `-cp scripts/benchmark` は、Javaに `scripts/benchmark` ディレクトリでクラスを探すように指示します。
   - `MultiMark` はクラス名です（`MultiMark.java` には `package` ステートメントがないため、`.class` やパッケージプレフィックスはなし）。

   これにより、次のような出力が得られるはずです：
   ```
   CPU cores: 32
   ...
   ```

3. **注意**: `MultiMark.class` が古いか存在しない場合は、まずルートディレクトリからソースファイルをコンパイルしてください：
   ```bash
   javac scripts/benchmark/MultiMark.java
   ```
   その後、上記のコマンドを実行します。

---

### **オプション2: クラスパスを指定してソースファイルを直接実行（Java 11以降）**
ソースファイルを直接実行する場合（`python script.py` のように）、ソースファイルのパスとクラスパスを指定して `java` コマンドを使用できます。

1. **ルートディレクトリに留まる**
   `~/projects/lzwjava.github.io` にいることを確認してください。

2. **ソースファイルを実行**
   以下を使用します：
   ```bash
   java -cp scripts/benchmark scripts/benchmark/MultiMark.java
   ```
   - `-cp scripts/benchmark` は、ソースを含むディレクトリにクラスパスを設定します。
   - `scripts/benchmark/MultiMark.java` は、コンパイルして実行するソースファイルを指定します。

   これは `MultiMark.java` を1ステップでコンパイルおよび実行し、以前と同じ出力を生成します。

---

### **オプション3: ルートディレクトリにシェルスクリプトを作成**
さらに便利にするために（ルートディレクトリから `./multimark` を実行するように）、ルートディレクトリ（`~/projects/lzwjava.github.io`）にシェルスクリプトを作成できます。

1. **シェルスクリプトを作成**
   ルートディレクトリに `multimark` という名前のファイルを作成します：
   ```bash
   nano multimark
   ```
   以下を追加します：
   ```bash
   #!/bin/bash
   java -cp scripts/benchmark MultiMark
   ```
   保存して終了します。

2. **実行可能にする**
   ```bash
   chmod +x multimark
   ```

3. **スクリプトを実行**
   ルートディレクトリから：
   ```bash
   ./multimark
   ```
   これにより、ディレクトリを変更する必要なしにJavaプログラムが実行されます。

4. **オプション: スクリプト内でコンパイル**
   スクリプトにコンパイルを処理させたい場合（例えば、ソースファイルが変更された場合）、スクリプトを変更します：
   ```bash
   #!/bin/bash
   javac scripts/benchmark/MultiMark.java
   java -cp scripts/benchmark MultiMark
   ```

---

### **主な注意点**
- **クラスパス (`-cp`)**: `-cp` オプションは、Javaにクラスまたはソースファイルをどこで見つけるかを伝えます。`MultiMark.java` には `package` ステートメントがないため、クラス名は単に `MultiMark` であり、`scripts.benchmark.MultiMark` ではありません。もし `package scripts.benchmark;` 行があった場合は、ルートから `java -cp . scripts.benchmark.MultiMark` を使用する必要があります。
- **Javaのバージョン**: ソースファイルの実行（`java scripts/benchmark/MultiMark.java`）にはJava 11以降が必要です。システムにはJavaがインストールされているようです。`scripts/benchmark` ディレクトリから動作したためです。
- **ディレクトリ**: これらの解決策は、あなたの希望に合わせて、ルートディレクトリ（`~/projects/lzwjava.github.io`）に留まります。
- **自動化**: シェルスクリプト（オプション3）は、Pythonのような体験に最も近く、Pythonスクリプトのように `./multimark` を実行できます。グローバルアクセスのために `PATH` に追加することもできますが、それはオプションです。
- **エラー処理**: `NoClassDefFoundError` のようなエラーが発生した場合は、`MultiMark.class` が `scripts/benchmark/` に存在することを確認するか、再コンパイルしてください。Javaが見つからない場合は、インストールを確認してください（`java --version`）。

Pythonスクリプトと統合したり、特定のワークフロー（例：`multimark.py` と `MultiMark.java` を一緒に実行する）が必要な場合は、お知らせください！