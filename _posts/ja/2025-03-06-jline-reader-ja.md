---
audio: false
generated: true
lang: ja
layout: post
title: コンソール入力の読み取り
translated: true
---

`org.jline.reader` パッケージをJavaで使用するには、JLineライブラリを使用してコンソール入力を高度な機能（行編集、履歴、補完など）で処理する必要があります。このガイドでは、基本的な設定から始めるための完全で実践的なアプローチを提供します。

### 前提条件
JLineライブラリがプロジェクトに追加されていることを確認してください。Mavenを使用している場合は、`pom.xml`に次の依存関係を追加します。

```xml
<dependency>
    <groupId>org.jline</groupId>
    <artifactId>jline</artifactId>
    <version>3.21.0</version> <!-- 最新バージョンを使用 -->
</dependency>
```

### `org.jline.reader` の基本的な使用方法

1. **ターミナルインスタンスの作成**
   - `org.jline.terminal` から `TerminalBuilder` クラスを使用して `Terminal` オブジェクトを作成します。これは、入力が読み取られるコンソール環境を表します。
   - 例:
     ```java
     import org.jline.terminal.Terminal;
     import org.jline.terminal.TerminalBuilder;

     Terminal terminal = TerminalBuilder.builder().build();
     ```
   - `build()` メソッドは、ほとんどの環境に適したデフォルトのターミナルを作成します。さらにカスタマイズすることも可能ですが、デフォルトが十分な場合が多いです。

2. **LineReaderインスタンスの作成**
   - `org.jline.reader` から `LineReaderBuilder` クラスを使用して `LineReader` オブジェクトを作成し、その `Terminal` インスタンスを渡します。
   - `LineReader` は、JLineの機能を使用してユーザー入力を読み取るための主要なインターフェースです。
   - 例:
     ```java
     import org.jline.reader.LineReader;
     import org.jline.reader.LineReaderBuilder;

     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .build();
     ```

3. **ユーザーからの入力を読み取る**
   - `LineReader` の `readLine()` メソッドを使用して、ユーザーが入力したテキストの行を読み取ります。プロンプトを表示することも可能です。
   - 例:
     ```java
     String line = reader.readLine("> ");
     ```
   - これは `> ` をプロンプトとして表示し、ユーザーの入力を待ち、ユーザーがEnterキーを押すと入力された文字列を返します。

### 簡単な例
ユーザーが「exit」と入力するまで入力を読み取るループを実行する完全な最小限の例です。

```java
import org.jline.reader.LineReader;
import org.jline.reader.LineReaderBuilder;
import org.jline.terminal.Terminal;
import org.jline.terminal.TerminalBuilder;

public class ConsoleExample {
    public static void main(String[] args) throws Exception {
        // Terminalの作成
        Terminal terminal = TerminalBuilder.builder().build();

        // LineReaderの作成
        LineReader reader = LineReaderBuilder.builder()
            .terminal(terminal)
            .build();

        // 入力をループで読み取る
        String line;
        while ((line = reader.readLine("> ")) != null) {
            System.out.println("入力しました: " + line);
            if (line.equals("exit")) {
                break;
            }
        }
    }
}
```

- **出力**: これを実行すると `> ` プロンプトが表示されます。テキストを入力し、バックスペースや矢印キーを使用して編集（`System.in` で簡単に利用できない機能）し、Enterキーを押すことができます。「exit」と入力するとプログラムが終了します。

### オプションの機能
`LineReader` に追加の機能を追加して強化することができます。

#### 1. **コマンド履歴の有効化**
   - 入力を保存し、再度呼び出すための `History` オブジェクトを追加します（例：上下矢印キーを使用）。
   - 例:
     ```java
     import org.jline.reader.impl.history.DefaultHistory;
     import org.jline.reader.History;

     History history = new DefaultHistory();
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .history(history)
         .build();
     ```
   - これで、ユーザーは入力履歴をナビゲートできます。

#### 2. **自動補完の追加**
   - ユーザーがTabキーを押すと補完を提案するための `Completer` を実装します。
   - 簡単な文字列コンプリーターの例:
     ```java
     import org.jline.reader.Completer;
     import org.jline.reader.impl.completer.StringsCompleter;

     Completer completer = new StringsCompleter("foo", "bar", "baz");
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .completer(completer)
         .build();
     ```
   - 「f」と入力し、Tabキーを押すと「foo」が提案されます。

#### 3. **パスワードの読み取り（マスク入力）**
   - マスク文字を使用して入力を隠すために `readLine()` を使用します（例：パスワード）。
   - 例:
     ```java
     String password = reader.readLine("パスワードを入力してください: ", '*');
     ```
   - 入力された文字の代わりにアスタリスク（`*`）が表示されます。

### リソース管理
リソースを解放するために、使用が完了したら `Terminal` を閉じます。`Terminal` が `Closeable` を実装しているため、try-with-resources ブロックを使用します。

```java
try (Terminal terminal = TerminalBuilder.builder().build()) {
    LineReader reader = LineReaderBuilder.builder()
        .terminal(terminal)
        .build();
    String line = reader.readLine("> ");
    System.out.println("入力しました: " + line);
}
```

### `org.jline.reader` を使用する理由
基本的な入力 `System.in` と `BufferedReader` と比較して、`org.jline.reader` は以下を提供します。
- **行編集**: バックスペース、カーソル移動など。
- **履歴**: 以前の入力を再度呼び出す。
- **補完**: オプションを自動的に提案。
- **クロスプラットフォームターミナル処理**: 異なる環境で一貫して動作。

### 注意点
- `LineReaderBuilder` で `Terminal` を指定しない場合、内部的にデフォルトのものが作成されるため、`LineReader reader = LineReaderBuilder.builder().build();` は簡単な場合に動作します。
- `readLine()` を複数のスレッドから同時に呼び出さないようにしてください。`LineReader` は同時読み取りに対してスレッドセーフではありません。
- 高度な使用例（例：複数行入力、カスタムキーバインド）については、JLineの追加機能（例：パーサーやキーマップ）を探索してください。

これにより、`org.jline.reader` を使用してJavaでコンソール入力を効果的に読み取るための基本的な要素がカバーされます。基本的な設定から始めて、アプリケーションに必要な履歴や補完などの機能を追加してください！