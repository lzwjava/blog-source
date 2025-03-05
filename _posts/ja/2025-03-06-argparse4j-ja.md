---
audio: false
generated: true
lang: ja
layout: post
title: コマンドライン引数の解析方法
translated: true
---

`net.sourceforge.argparse4j`というJavaライブラリを使用してコマンドライン引数を解析するには、以下の手順に従ってください。このライブラリは、Pythonの`argparse`に触発されています。

---

### 1. **依存関係を追加する**
プロジェクトに`argparse4j`を含めるには、依存関係として追加してください。Mavenを使用している場合は、`pom.xml`を以下のように更新してください。

```xml
<dependency>
    <groupId>net.sourceforge.argparse4j</groupId>
    <artifactId>argparse4j</artifactId>
    <version>0.9.0</version>
</dependency>
```

他のビルドツール（例：Gradle）を使用している場合は、[Maven Central Repository](https://central.sonatype.com/artifact/net.sourceforge.argparse4j/argparse4j)で対応する設定を確認してください。

---

### 2. **`ArgumentParser`オブジェクトを作成する**
まず、`ArgumentParsers.newFor("prog").build()`を使用して`ArgumentParser`のインスタンスを作成します。ここで、`"prog"`はプログラムの名前です。また、説明を追加し、自動ヘルプ生成を有効にすることもできます。

**例:**
```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;

ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
    .defaultHelp(true)  // -h/--helpオプションを有効にする
    .description("指定されたファイルのチェックサムを計算します。");
```

---

### 3. **引数を追加する**
プログラムが受け入れるコマンドライン引数を`parser.addArgument()`を使用して定義します。以下を指定できます：
- **オプション引数**（例：`-t`, `--type`）には、フラグ、選択肢、デフォルト値、ヘルプテキストがあります。
- **位置引数**（例：`file`）には、`.nargs("*")`を使用して任意の長さの変数をサポートすることができます。

**例:**
```java
parser.addArgument("-t", "--type")
    .choices("SHA-256", "SHA-512", "SHA1")  // これらのオプションに制限
    .setDefault("SHA-256")                  // 指定されていない場合のデフォルト値
    .help("使用するハッシュ関数を指定します");  // ヘルプメッセージの説明

parser.addArgument("file")
    .nargs("*")                             // 0個以上の引数を受け入れる
    .help("チェックサムを計算するファイル");    // ヘルプメッセージの説明
```

---

### 4. **コマンドライン引数を解析する**
コマンドライン引数（通常は`main`メソッドから渡される`String[] args`）を解析するには、`parser.parseArgs()`を使用します。これをtry-catchブロックでラップして、解析エラーを優雅に処理します。

**例:**
```java
import net.sourceforge.argparse4j.inf.Namespace;
import net.sourceforge.argparse4j.inf.ArgumentParserException;

public class Checksum {
    public static void main(String[] args) {
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("指定されたファイルのチェックサムを計算します。");

        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("使用するハッシュ関数を指定します");
        parser.addArgument("file").nargs("*")
            .help("チェックサムを計算するファイル");

        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);  // 引数を解析
        } catch (ArgumentParserException e) {
            parser.handleError(e);        // エラーとヘルプメッセージを表示
            System.exit(1);               // エラー時には終了
        }
    }
}
```

---

### 5. **解析された値にアクセスする**
`parseArgs()`メソッドは、解析された引数値を含む`Namespace`オブジェクトを返します。`getString()`や`getList()`などのメソッドを使用して、これらを取得します。

**例:**
```java
String hashType = ns.getString("type");  // 例："SHA-256"
List<String> files = ns.getList("file"); // ファイル名のリスト

System.out.println("ハッシュタイプ: " + hashType);
System.out.println("ファイル: " + files);
```

---

### 全体をまとめる
以下は、完全な例です：

```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;
import net.sourceforge.argparse4j.inf.ArgumentParserException;
import net.sourceforge.argparse4j.inf.Namespace;
import java.util.List;

public class Checksum {
    public static void main(String[] args) {
        // ステップ2：パーサを作成
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("指定されたファイルのチェックサムを計算します。");

        // ステップ3：引数を追加
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("使用するハッシュ関数を指定します");
        parser.addArgument("file").nargs("*")
            .help("チェックサムを計算するファイル");

        // ステップ4：引数を解析
        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);
        } catch (ArgumentParserException e) {
            parser.handleError(e);
            System.exit(1);
        }

        // ステップ5：解析された値にアクセス
        String hashType = ns.getString("type");
        List<String> files = ns.getList("file");

        // 例の出力
        System.out.println("ハッシュタイプ: " + hashType);
        System.out.println("ファイル: " + files);
    }
}
```

---

### 追加機能
- **自動ヘルプ**：プログラムを`-h`または`--help`で実行すると、生成されたヘルプメッセージが表示されます。
- **サブコマンド**：複雑なコマンド（例：`git commit`, `git push`）に対して`parser.addSubparsers()`を使用します。
- **アノテーション**：アノテーションを使用して引数をクラスフィールドにバインドします（詳細については、ユーザーマニュアルを参照）。

より高度な使用方法については、[Argparse4j ユーザーマニュアル](https://argparse4j.github.io/userguide.html)を参照してください。

---

このワークフローを使用すると、`net.sourceforge.argparse4j`を使用してJavaアプリケーションでコマンドライン引数を簡単に解析し、処理することができます。