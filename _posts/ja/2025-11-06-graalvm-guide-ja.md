---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GraalVMインストールと使用ガイド
translated: true
type: note
---

## GraalVMとは？

GraalVMは、Java、JavaScript、Pythonなど複数のプログラミング言語をサポートするオープンソースの高性能ランタイム（JDKディストリビューション）です。高速実行のための先進的なJITコンパイラを特徴とし、Native Imageを通じてJavaアプリケーションをネイティブ実行ファイルにコンパイルする機能により、起動時間とメモリ使用量を削減できます。

## インストール方法

1. **GraalVMのダウンロード**:
   - 公式GraalVMダウンロードページにアクセスします。
   - Community Edition（無料）またはOracle GraalVM（追加機能付き）を選択します。
   - ご使用のプラットフォーム（Linux、macOS、Windowsなど）とアーキテクチャ（x64またはARM）に合ったバージョンを選択します。
   - 2025年現在、最新の安定版リリースはGraalVM for JDK 22または23です。最新情報はサイトで確認してください。

2. **展開とインストール**:
   - ダウンロードしたアーカイブをディレクトリに解凍します（例：Linux/macOSでは`/opt/graalvm`、Windowsでは`C:\Program Files\GraalVM`）。
   - インストーラーは不要で、ポータブルなディストリビューションです。

3. **環境変数の設定**:
   - `JAVA_HOME`をGraalVMディレクトリに設定します（例：Linux/macOSでは`export JAVA_HOME=/opt/graalvm`）。
   - `bin`ディレクトリを`PATH`に追加します（例：`export PATH=$JAVA_HOME/bin:$PATH`）。
   - `java -version`で確認します。GraalVMの詳細が表示されるはずです。

4. **追加コンポーネントのインストール（オプション）**:
   - 言語ランタイムやNative Imageには`gu`（GraalVM Updater）を使用します：`gu install native-image`（Linuxでは`build-essential`などのビルドツールが必要です）。

## Hello Worldプログラムのビルド

この例では、GraalVMの主要言語であるJavaを使用します。シンプルな「Hello World」アプリを作成、コンパイル、実行します。

### ステップ1: コードの記述
`HelloWorld.java`というファイルを作成します：

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World from GraalVM!");
    }
}
```

### ステップ2: コンパイル
ファイルがあるディレクトリでターミナルを開き、以下を実行します：
```
javac HelloWorld.java
```
これにより`HelloWorld.class`が生成されます。

### ステップ3: 実行
```
java HelloWorld
```
出力：
```
Hello, World from GraalVM!
```

### 応用: ネイティブ実行ファイルへのコンパイル
GraalVMのNative Image機能を使用すると、スタンドアロンのバイナリをビルドできます。

1. Native Imageがインストールされていることを確認：`gu install native-image`。
2. 設定を生成（初回実行時にはこれが必要な場合があります）：
   ```
   native-image --no-fallback -H:+ReportExceptionStackTraces HelloWorld
   ```
   - これにより`HelloWorld`（Windowsでは`helloworld.exe`）というネイティブバイナリが作成されます。
   - 初回ビルド時にはアプリケーションを分析するため、数分かかる場合があります。

3. ネイティブバイナリを実行：
   ```
   ./HelloWorld
   ```
   出力は同じですが、瞬時に起動しメモリ使用量が少なくなります。

## GraalVM使用時のヒント
- **JDKの切り替え**: SDKMAN!（`sdk install java 22.0.2-graal`）を使用すると簡単に管理できます。
- **マルチ言語**: GraalVMの`node`でNode.jsコードを、`python`でPythonコードを実行できます。
- **パフォーマンス**: `-XX:+UnlockExperimentalVMOptions -XX:+UseJVMCICompiler`でGraalVMのJITを有効にします。
- **トラブルシューティング**: 問題がある場合は`~/.gu/`内のログを確認し、Native ImageにはCコンパイラがシステムにインストールされていることを確認してください。

詳細は公式ドキュメントを参照してください。

[GraalVM Downloads](https://www.graalvm.org/downloads/)  
[GraalVM User Guide](https://www.graalvm.org/latest/reference-manual/)  
[Native Image Tutorial](https://www.graalvm.org/latest/reference-manual/native-image/)