---
audio: false
generated: true
lang: ja
layout: post
title: Ubuntu 22.04でのOpenJDK 21.0.7インストール場所の確認
translated: true
type: note
---

`java --version` コマンドを実行した結果、お使いのシステムに OpenJDK 21.0.7 がインストールされていることが確認できます。これは特に Ubuntu 22.04 用にパッケージ化されたバージョンです。この出力は、Java Development Kit (JDK) がインストールされており、コマンドラインからアクセス可能であることを確認しています。

Java のインストール場所は、通常 `java` バイナリの場所を確認することで見つけることができます。Ubuntu ベースのシステムを使用しているため、OpenJDK は `/usr/lib/jvm/` のような標準的なシステムディレクトリにインストールされている可能性が高いです。

Java のインストールの正確なパスを見つけるには:

1. **`java` バイナリのパスを探す**:
   ターミナルで次のコマンドを実行します:
   ```bash
   which java
   ```
   これにより、おそらく `/usr/bin/java` のような出力が得られます。これは実際の Java バイナリへのシンボリックリンクです。

2. **シンボリックリンクをたどって実際の場所を見つける**:
   `/usr/bin/java` は通常シンボリックリンクなので、実際のインストールディレクトリを見つけるには以下を実行します:
   ```bash
   readlink -f $(which java)
   ```
   これにより、`/usr/lib/jvm/java-21-openjdk-amd64/bin/java` のような出力が得られる可能性があり、JDK が `/usr/lib/jvm/java-21-openjdk-amd64/` にインストールされていることを示しています。

3. **インストールディレクトリを確認する**:
   JVM ディレクトリの内容をリストして確認できます:
   ```bash
   ls /usr/lib/jvm/
   ```
   `java-21-openjdk-amd64` または類似のディレクトリが表示されるはずで、これが OpenJDK のインストールを含んでいます。

### まとめ
Java のインストールは、おそらく `/usr/lib/jvm/java-21-openjdk-amd64/` (または `/usr/lib/jvm/` 下の類似のディレクトリ) にあります。実行した `java` コマンドは、このディレクトリ内の `java` バイナリを指すシンボリックリンクです。正確なパスを確認したい場合は、`readlink -f $(which java)` コマンドを使用してください。