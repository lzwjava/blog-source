---
audio: false
generated: true
lang: ja
layout: post
title: PythonスクリプトのようにJavaを実行する
translated: true
type: note
---

`MultiMark.java`ファイルを直接実行するには、Pythonスクリプトを実行するのと同様に、いくつかの方法があります。Unix系システム（`~/projects`パスと`ls`コマンドから推測）を使用していることを踏まえて、Javaプログラムの実行をできるだけシームレスにする手順を説明します。主に2つのアプローチがあります：

---

### **オプション1: `java`コマンドで`MultiMark.java`を直接実行（Java 11以降）**
Java 11以降では、明示的なコンパイルなしで単一のJavaソースファイルを直接実行できるため、Pythonスクリプトの実行に近い感覚で利用できます。

1. **Javaがインストールされていることを確認**
   Java 11以降がインストールされているか確認：
   ```bash
   java --version
   ```
   Javaがインストールされていない場合、または古いバージョンの場合は、互換性のあるバージョン（例：OpenJDK）をインストール：
   ```bash
   sudo apt update
   sudo apt install openjdk-17-jdk
   ```

2. **Javaファイルを直接実行**
   `MultiMark.java`が含まれるディレクトリに移動：
   ```bash
   cd ~/projects/lzwjava.github.io/scripts/benchmark
   ```
   以下のコマンドでJavaファイルを直接実行：
   ```bash
   java MultiMark.java
   ```
   このコマンドは`MultiMark.java`ファイルを1ステップでコンパイルおよび実行します。出力（CPUコア数、スレッド数、時間など）がターミナルに表示されます。

---

### **オプション2: 利便性のためにシェルスクリプトを作成**
`MultiMark.java`の実行をPythonスクリプトの実行（例：`./multimark`）により近づけるために、シェルスクリプトのラッパーを作成できます。

1. **シェルスクリプトの作成**
   `scripts/benchmark`ディレクトリに`multimark`（拡張子なし）というファイルを作成：
   ```bash
   nano ~/projects/lzwjava.github.io/scripts/benchmark/multimark
   ```
   以下の内容を追加：
   ```bash
   #!/bin/bash
   java MultiMark.java
   ```
   保存して終了（nanoでは`Ctrl+O`、`Enter`、`Ctrl+X`）。

2. **スクリプトを実行可能にする**
   実行権限を設定：
   ```bash
   chmod +x multimark
   ```

3. **スクリプトの実行**
   これでPythonスクリプトのようにプログラムを実行できます：
   ```bash
   ./multimark
   ```
   内部的に`java MultiMark.java`が実行されます。

---

### **オプション3: コンパイルと実行を分離（従来のアプローチ）**
明示的にJavaファイルをコンパイルする必要がある場合（例：古いJavaバージョンやコンパイルエラーの確認）、以下の手順に従います：

1. **Javaファイルのコンパイル**
   ディレクトリに移動：
   ```bash
   cd ~/projects/lzwjava.github.io/scripts/benchmark
   ```
   Javaソースファイルをコンパイル：
   ```bash
   javac MultiMark.java
   ```
   これにより`MultiMark.class`ファイルが生成されます。

2. **コンパイルされたプログラムの実行**
   コンパイルされたクラスを実行：
   ```bash
   java MultiMark
   ```
   注意：コンパイルされたクラスファイルを実行するため、`.java`なしの`MultiMark`を使用します。

---

### **Pythonライクな実行方法**
Pythonスクリプトの実行に可能な限り近い体験にするには、**オプション1**（直接`java MultiMark.java`）が最もシンプルで、手動コンパイルをスキップします。**オプション2**（シェルスクリプト）は、`./script.py`を実行するような感覚で`./multimark`のような単一コマンドを希望する場合に理想的です。

### **注意点**
- **Javaバージョン**: コードは標準Javaライブラリ（`java.util.*`と`System.nanoTime`）を使用しているため、Java 8以降で動作するはずです。直接実行機能（`java MultiMark.java`）はJava 11以降が必要です。
- **パフォーマンス**: `MultiMark.java`プログラムはマルチスレッドでのソートをベンチマークします。直接実行またはスクリプト経由での実行はパフォーマンスに影響しませんが、テストされるスレッド数（最大64スレッド）に対してシステムに十分なリソース（CPU/メモリ）があることを確認してください。
- **ディレクトリコンテキスト**: `ls scripts/benchmark/`を表示していたため、`MultiMark.java`がそのディレクトリにあると仮定しました。他の場所にある場合はパスを調整してください。
- **エラーハンドリング**: エラーが発生した場合（例：`java: command not found`）、Javaがインストールされ`PATH`に追加されていることを確認してください。プログラムが失敗した場合（メモリやスレッド制限による）、詳細についてはスタックトレースを確認してください。

Pythonスクリプト（`executormark.py`、`multimark.py`、`threadmark.py`）とのワークフローにこれを統合したい場合は、それらを組み合わせる方法（例：PythonからJavaプログラムの呼び出し）を提案できますのでお知らせください。