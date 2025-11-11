---
audio: false
generated: true
lang: ja
layout: post
title: Javaでのコンソール入力の読み取り
translated: true
type: note
---

Javaで`org.jline.reader`パッケージを使用するには、JLineライブラリの一部であるこのパッケージを活用して、行編集、履歴、補完などの高度な機能を備えたコンソール入力を処理します。以下に、実用的なアプローチで始められる完全なガイドを提供します。

### 前提条件
プロジェクトにJLineライブラリが追加されていることを確認してください。Mavenを使用している場合は、`pom.xml`に以下の依存関係を追加します：

```xml
<dependency>
    <groupId>org.jline</groupId>
    <artifactId>jline</artifactId>
    <version>3.21.0</version> <!-- 最新バージョンを使用 -->
</dependency>
```

### `org.jline.reader`の基本的な使用方法

1. **Terminalインスタンスの作成**
   - `org.jline.terminal`の`TerminalBuilder`クラスを使用して、`Terminal`オブジェクトを作成します。これは入力が読み取られるコンソール環境を表します。
   - 例：
     ```java
     import org.jline.terminal.Terminal;
     import org.jline.terminal.TerminalBuilder;

     Terminal terminal = TerminalBuilder.builder().build();
     ```
   - `build()`メソッドは、ほとんどの環境に適したデフォルトのターミナルを作成します。さらにカスタマイズ（例：ターミナルタイプの設定）も可能ですが、デフォルトで十分な場合が多いです。

2. **LineReaderインスタンスの作成**
   - `org.jline.reader`の`LineReaderBuilder`クラスを使用して、`Terminal`インスタンスを渡して`LineReader`オブジェクトを作成します。
   - `LineReader`は、JLineの機能を備えたユーザー入力読み取りの主要インターフェースです。
   - 例：
     ```java
     import org.jline.reader.LineReader;
     import org.jline.reader.LineReaderBuilder;

     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .build();
     ```

3. **ユーザーからの入力読み取り**
   - `LineReader`の`readLine()`メソッドを使用して、ユーザーが入力したテキスト行を読み取ります。オプションで表示するプロンプトを指定できます。
   - 例：
     ```java
     String line = reader.readLine("> ");
     ```
   - これは`> `をプロンプトとして表示し、ユーザー入力を待機し、ユーザーがEnterを押すと入力された文字列を返します。

### 簡単な例
以下は、ユーザーが「exit」と入力するまでループでユーザー入力を読み取る完全な最小限の例です：

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
        
        // ループで入力読み取り
        String line;
        while ((line = reader.readLine("> ")) != null) {
            System.out.println("入力: " + line);
            if (line.equals("exit")) {
                break;
            }
        }
    }
}
```

- **出力**: 実行すると`> `プロンプトが表示されます。テキストを入力し、バックスペースや矢印キーで編集（`System.in`では簡単に利用できない機能）し、Enterを押せます。「exit」と入力するとプログラムが終了します。

### オプション機能
`LineReader`を追加機能で強化できます：

#### 1. **コマンド履歴の有効化**
   - `History`オブジェクトを追加して、以前の入力を保存し呼び出せるようにします（例：上下矢印キー）。
   - 例：
     ```java
     import org.jline.reader.impl.history.DefaultHistory;
     import org.jline.reader.History;

     History history = new DefaultHistory();
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .history(history)
         .build();
     ```
   - これでユーザーは入力履歴をナビゲートできます。

#### 2. **オートコンプリートの追加**
   - `Completer`を実装して、ユーザーがTabを押したときに補完候補を提案します。
   - 簡単な文字列コンプリータの例：
     ```java
     import org.jline.reader.Completer;
     import org.jline.reader.impl.completer.StringsCompleter;

     Completer completer = new StringsCompleter("foo", "bar", "baz");
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .completer(completer)
         .build();
     ```
   - 「f」と入力してTabを押すと「foo」が提案されます。

#### 3. **パスワード読み取り（マスク入力）**
   - マスク文字を指定した`readLine()`を使用して入力を隠します（例：パスワード用）。
   - 例：
     ```java
     String password = reader.readLine("パスワードを入力: ", '*');
     ```
   - 入力された文字の代わりにアスタリスク（`*`）が表示されます。

### リソース管理
堅牢なアプリケーションでは、リソースを解放するために`Terminal`を終了時にクローズします。`Terminal`は`Closeable`を実装しているため、try-with-resourcesブロックを使用します：

```java
try (Terminal terminal = TerminalBuilder.builder().build()) {
    LineReader reader = LineReaderBuilder.builder()
        .terminal(terminal)
        .build();
    String line = reader.readLine("> ");
    System.out.println("入力: " + line);
}
```

### `org.jline.reader`を使用する理由
`System.in`と`BufferedReader`を使った基本的な入力とは異なり、`org.jline.reader`は以下を提供します：
- **行編集**: バックスペース、カーソル移動など
- **履歴**: 以前の入力の呼び出し
- **補完**: オートサジェスト機能
- **クロスプラットフォームターミナル処理**: 異なる環境で一貫して動作

### 注意点
- `LineReaderBuilder`で`Terminal`を指定しない場合、内部的にデフォルトのものが作成されるため、`LineReader reader = LineReaderBuilder.builder().build();`とすれば簡単なケースで動作します。
- `LineReader`は同時読み取りに対してスレッドセーフではないため、複数のスレッドから同時に`readLine()`を呼び出さないでください。
- 高度な使用例（例：複数行入力、カスタムキーバインディング）では、パーサーやキーマップなどの追加JLine機能を探索してください。

これで、Javaで効果的にコンソール入力を読み取るための`org.jline.reader`の基本を網蓋しました。基本的なセットアップから始め、アプリケーションの必要に応じて履歴や補完などの機能を追加してください！