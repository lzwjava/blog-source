---
audio: false
generated: true
lang: ja
layout: post
title: Javaでのコマンドライン引数の解析
translated: true
type: note
---

`net.sourceforge.argparse4j`（Pythonの`argparse`に触発されたコマンドライン引数解析用Javaライブラリ）を使用するには、以下の手順に従ってください：

---

### 1. **依存関係の追加**
プロジェクトに`argparse4j`を含めるには、依存関係として追加します。Mavenを使用している場合は、`pom.xml`を以下のように更新してください：

```xml
<dependency>
    <groupId>net.sourceforge.argparse4j</groupId>
    <artifactId>argparse4j</artifactId>
    <version>0.9.0</version>
</dependency>
```

Gradleなどの他のビルドツールを使用している場合は、[Maven Central Repository](https://central.sonatype.com/artifact/net.sourceforge.argparse4j/argparse4j)で同等の設定を確認してください。

---

### 2. **`ArgumentParser`オブジェクトの作成**
`ArgumentParsers.newFor("prog").build()`を使用して`ArgumentParser`インスタンスを作成します。`"prog"`はプログラムの名前です。説明を追加したり、自動ヘルプ生成を有効にすることもできます。

**例：**
```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;

ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
    .defaultHelp(true)  // -h/--helpオプションを有効化
    .description("Calculate checksum of given files.");
```

---

### 3. **引数の追加**
`parser.addArgument()`を使用して、プログラムが受け入れるコマンドライン引数を定義します。以下を指定できます：
- **オプション引数**（例：`-t`、`--type`）：フラグ、選択肢、デフォルト値、ヘルプテキストを指定
- **位置引数**（例：`file`）：`.nargs("*")`を使用して可変長サポートを追加可能

**例：**
```java
parser.addArgument("-t", "--type")
    .choices("SHA-256", "SHA-512", "SHA1")  // これらのオプションに制限
    .setDefault("SHA-256")                  // 指定がない場合のデフォルト値
    .help("Specify hash function to use");  // ヘルプメッセージの説明

parser.addArgument("file")
    .nargs("*")                             // 0個以上の引数を受け入れる
    .help("File to calculate checksum");    // ヘルプメッセージの説明
```

---

### 4. **コマンドライン引数の解析**
`parser.parseArgs()`を使用してコマンドライン引数（通常は`main`メソッドから`String[] args`として渡される）を解析します。解析エラーを適切に処理するために、try-catchブロックで囲んでください。

**例：**
```java
import net.sourceforge.argparse4j.inf.Namespace;
import net.sourceforge.argparse4j.inf.ArgumentParserException;

public class Checksum {
    public static void main(String[] args) {
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("Calculate checksum of given files.");
        
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("Specify hash function to use");
        parser.addArgument("file").nargs("*")
            .help("File to calculate checksum");

        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);  // 引数を解析
        } catch (ArgumentParserException e) {
            parser.handleError(e);        // エラーとヘルプメッセージを表示
            System.exit(1);               // エラー時に終了
        }
    }
}
```

---

### 5. **解析された値へのアクセス**
`parseArgs()`メソッドは、解析された引数値を含む`Namespace`オブジェクトを返します。`getString()`や`getList()`などのメソッドを使用して値を取得します。

**例：**
```java
String hashType = ns.getString("type");  // 例: "SHA-256"
List<String> files = ns.getList("file"); // ファイル名のリスト

System.out.println("Hash Type: " + hashType);
System.out.println("Files: " + files);
```

---

### 完全な実装例
完全な例を以下に示します：

```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;
import net.sourceforge.argparse4j.inf.ArgumentParserException;
import net.sourceforge.argparse4j.inf.Namespace;
import java.util.List;

public class Checksum {
    public static void main(String[] args) {
        // ステップ2: パーサーの作成
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("Calculate checksum of given files.");

        // ステップ3: 引数の追加
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("Specify hash function to use");
        parser.addArgument("file").nargs("*")
            .help("File to calculate checksum");

        // ステップ4: 引数の解析
        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);
        } catch (ArgumentParserException e) {
            parser.handleError(e);
            System.exit(1);
        }

        // ステップ5: 解析された値へのアクセス
        String hashType = ns.getString("type");
        List<String> files = ns.getList("file");

        // 出力例
        System.out.println("Hash Type: " + hashType);
        System.out.println("Files: " + files);
    }
}
```

---

### 追加機能
- **自動ヘルプ**: `-h`または`--help`を付けてプログラムを実行すると、生成されたヘルプメッセージが表示されます
- **サブコマンド**: 複雑なコマンド（例：`git commit`、`git push`）には`parser.addSubparsers()`を使用します
- **アノテーション**: アノテーションを使用して引数をクラスフィールドにバインドします（詳細はユーザーマニュアルを参照）

より高度な使用方法については、[Argparse4j User Manual](https://argparse4j.github.io/userguide.html)を参照してください。

---

このワークフローにより、`net.sourceforge.argparse4j`を使用してJavaアプリケーションでコマンドライン引数を簡単に解析および処理できます。