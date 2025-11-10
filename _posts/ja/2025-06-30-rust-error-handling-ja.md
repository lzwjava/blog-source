---
audio: false
generated: true
lang: ja
layout: post
title: 例外を用いないRustのエラー処理
translated: true
type: note
---

Rustは、JavaやC#のような従来の意味での**例外**を持っていません。代わりに、主に**戻り値**を通じてエラーを処理します。これはGoの`if err != nil`パターンに似ていますが、より堅牢で型安全なアプローチです。

以下に、Rustがエラーを処理する方法の概要を示します：

**1. 回復可能なエラーのための`Result<T, E>`列挙型：**

これはRustにおいて最も一般的で慣用的なエラー処理方法です。

  * `Result<T, E>`は2つのバリアントを持つ列挙型です：
      * `Ok(T)`：成功を表し、型`T`の成功値を含みます。
      * `Err(E)`：失敗を表し、型`E`のエラー値を含みます。
  * 関数が失敗する可能性がある場合、`Result`を返します。これにより、呼び出し側は成功（`Ok`）と失敗（`Err`）の両方のケースを明示的に処理することを強制されます。
  * `match`式または様々なヘルパーメソッド（`map`、`and_then`、`unwrap_or`、`unwrap_or_else`など）を使用して、`Ok`と`Err`のバリアントを処理します。

**例：**

```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Problem creating the file: {:?}", e),
            },
            other_error => panic!("Problem opening the file: {:?}", other_error),
        },
    };

    println!("Successfully opened or created file: {:?}", greeting_file);
}
```

**2. オプション値のための`Option<T>`列挙型：**

厳密には「エラー」用ではありませんが、`Option<T>`は*値が存在しない可能性*を表すという点で`Result`と似ています。

  * `Option<T>`は2つのバリアントを持ちます：
      * `Some(T)`：値が存在します。
      * `None`：値が存在しません。
  * これは、関数が正当に値を返さない可能性がある場合（例えば、存在しないかもしれないリスト内の要素を検索する場合）に使用されます。

**3. `?`演算子（疑問符演算子）：**

これは、エラーの伝播をより簡潔にする強力な糖衣構文です。Goで`if err != nil { return err }`が一般的であるのと同様です。

  * `Result`値が`Ok`の場合、`?`演算子は`Ok`の値をアンラップし、実行を継続します。
  * `Result`値が`Err`の場合、`?`演算子は直ちにその`Err`値を現在の関数から返します。
  * `?`を使用する関数は、それ自体が`Result`（または`Option`をアンラップする場合は`Option`）を返さなければなりません。

**`?`を使用した例：**

```rust
use std::fs::File;
use std::io::{self, Read}; // io::Readトレイトをインポート

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?; // ファイルが存在しない場合、エラーを伝播
    let mut username = String::new();
    username_file.read_to_string(&mut username)?; // 読み取りに失敗した場合、エラーを伝播
    Ok(username)
}

fn main() {
    match read_username_from_file() {
        Ok(username) => println!("Username: {}", username),
        Err(e) => println!("Error reading username: {}", e),
    }
}
```

**4. 回復不能なエラーのための`panic!`マクロ：**

`panic!`は回復不能なエラーに使用され、通常はプログラムのバグ（例えば、配列の境界外へのアクセス）を示します。

  * `panic!`が呼び出されると、プログラムは終了します（または設定に応じてスタックの「巻き戻し」を行います）。
  * プログラムが適切に処理すべき回復可能なエラーに対しては、一般的に推奨されません。

**従来の例外との主な違い：**

  * **明示性：** Rustのエラー処理は非常に明示的です。関数シグネチャはエラーを返す可能性があることを明確に示し、コンパイラはそれを処理することを*強制*します。誤ってエラーを無視することはできません。
  * **「すべてをキャッチする」ブロックがない：** あらゆる例外を黙ってキャッチする`try-catch`ブロックはありません。特定のエラータイプを扱います。
  * **型安全性：** エラーは特定の型（`Result<T, E>`）の値であるため、正確なエラー処理が可能となり、一般的な例外タイプの曖昧さを回避します。
  * **パフォーマンス：** `Result`値を返すことは、一般的に例外をスローしてキャッチするよりも高性能です。例外はしばしば多大なオーバーヘッド（スタックの巻き戻しなど）を伴うためです。Rustはパフォーマンスがクリティカルなアプリケーション向けに設計されています。

要約すると、Rustのエラー処理モデルは、JavaやC#の例外よりも、Goの「各レベルでチェックする」哲学にはるかに近いものです。しかし、`Result`列挙型と`?`演算子により、Rustはこの明示的なエラー処理を管理可能にし、さらに楽しささえも感じられる強力で人間工学的なツールを提供します。