---
audio: false
generated: true
lang: ja
layout: post
title: Rustプログラミング言語
translated: true
type: note
---

Rustプログラミング言語の包括的なガイドです。コアコンセプト、構文、高度な機能を網羅しています。Rustは安全性、速度、並行性に焦点を当てたシステムプログラミング言語です。

**I. Rust入門**

* **Rustとは？**
    * Rustは、パフォーマンスと安全性、特にシステムプログラミング、ゲームエンジン、Web Assembly、組み込みシステムなどの領域向けに設計された、マルチパラダイムで静的型付けのコンパイル型プログラミング言語です。
    * 所有権システム、借用、ライフタイムを通じて、ガベージコレクタを使用せずにメモリ安全性を実現します。
    * ゼロコスト抽象化を重視しており、大きな実行時オーバーヘッドなしで高水準の機能を利用できます。
* **主な機能と設計原則:**
    * **メモリ安全性:** コンパイル時にnullポインタ参照、データ競合、バッファオーバーフローなどの一般的なバグを防止します。
    * **データ競合のない並行性:** 所有権システムにより、安全な並行コードを容易に記述できます。
    * **パフォーマンス:** 低水準の制御、ゼロコスト抽象化、効率的なコンパイルにより、C++に匹敵する優れたパフォーマンスを発揮します。
    * **表現力豊かな型システム:** 強力な型推論、ジェネリクス、トレイト（インターフェースや型クラスに類似）、代数的データ型。
    * **優れたツーリング:** Cargo（ビルドシステム兼パッケージマネージャ）、rustfmt（コードフォーマッタ）、clippy（リンタ）。
    * **成長するエコシステム:** 活発で活気のあるコミュニティと、増え続けるライブラリやフレームワーク。
* **ユースケース:**
    * オペレーティングシステム
    * ゲームエンジン
    * Web Assembly (Wasm)
    * 組み込みシステム
    * コマンドラインツール
    * ネットワークプログラミング
    * 暗号通貨
    * 高性能コンピューティング

**II. Rust環境のセットアップ**

* **インストール:**
    * Rustをインストールする推奨方法は、公式のRustツールチェーンインストーラである`rustup`を使用することです。
    * [https://rustup.rs/](https://rustup.rs/) にアクセスし、お使いのオペレーティングシステムに合わせた指示に従ってください。
    * Unix系システムでは、通常次のようなコマンドを実行します: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
* **インストールの確認:**
    * ターミナルまたはコマンドプロンプトを開き、以下を実行します:
        * `rustc --version`: Rustコンパイラのバージョンを表示します。
        * `cargo --version`: Cargoのバージョンを表示します。
* **Cargo: Rustのビルドシステム兼パッケージマネージャ:**
    * CargoはRustプロジェクトを管理するために不可欠です。以下の処理を行います:
        * コードのビルド。
        * 依存関係（クレート）の管理。
        * テストの実行。
        * ライブラリの公開。
    * **新規プロジェクトの作成:** `cargo new <プロジェクト名>`（バイナリプロジェクトを作成）。 `cargo new --lib <ライブラリ名>`（ライブラリプロジェクトを作成）。
    * **プロジェクト構造:** 典型的なCargoプロジェクトは以下を含みます:
        * `Cargo.toml`: プロジェクトのメタデータと依存関係を含むマニフェストファイル。
        * `src/main.rs`: バイナリプロジェクトのエントリーポイント。
        * `src/lib.rs`: ライブラリプロジェクトのエントリーポイント。
        * `Cargo.lock`: プロジェクトで使用された依存関係の正確なバージョンを記録します。
    * **ビルド:** `cargo build`（デバッグモードでプロジェクトをビルド）。 `cargo build --release`（リリース向けに最適化してプロジェクトをビルド）。
    * **実行:** `cargo run`（バイナリをビルドして実行）。
    * **依存関係の追加:** クレート名とバージョンを`Cargo.toml`の`[dependencies]`セクションに追加します。Cargoが自動的にダウンロードとビルドを行います。
    * **依存関係の更新:** `cargo update`.

**III. 基本的なRustの構文とコンセプト**

* **Hello, World!**
    ```rust
    fn main() {
        println!("Hello, world!");
    }
    ```
    * `fn main()`: プログラムの実行が開始されるmain関数。
    * `println!()`: テキストをコンソールに出力するマクロ（`!`で示されます）。
* **変数と可変性:**
    * 変数はデフォルトで不変です。変数を可変にするには、`mut`キーワードを使用します。
    * 宣言: `let 変数名 = 値;`（型推論）。 `let 変数名: 型 = 値;`（明示的な型注釈）。
    * 可変変数: `let mut counter = 0; counter = 1;`
    * 定数: `const`で宣言され、型注釈が必須で、その値はコンパイル時に既知でなければなりません。 `const MAX_POINTS: u32 = 100_000;`
    * シャドーイング: 以前の変数と同じ名前で新しい変数を宣言できます。新しい変数は古い変数を隠します。
* **データ型:**
    * **スカラ型:** 単一の値を表します。
        * **整数型:** `i8`, `i16`, `i32`, `i64`, `i128`, `isize`（ポインタサイズの符号付き）； `u8`, `u16`, `u32`, `u64`, `u128`, `usize`（ポインタサイズの符号なし）。整数リテラルには接尾辞を付けることができます（例: `10u32`）。
        * **浮動小数点型:** `f32`（単精度）, `f64`（倍精度）。
        * **ブーリアン型:** `bool` (`true`, `false`)。
        * **文字型:** `char`（Unicodeスカラ値、4バイト）。
        * **ユニット型:** `()`（空のタプルまたは値の不在を表します）。
    * **複合型:** 複数の値をグループ化します。
        * **タプル:** 固定長で順序付けられた、異なる型を持つ可能性のある要素のシーケンス。 `let my_tuple = (1, "hello", 3.14); let (x, y, z) = my_tuple; let first = my_tuple.0;`
        * **配列:** 固定長で同じ型の要素のコレクション。 `let my_array = [1, 2, 3, 4, 5]; let months: [&str; 12] = ["...", "..."]; let first = my_array[0];`
        * **スライス:** 配列や他のスライス内の連続した要素シーケンスへの動的サイズのビュー。 `let slice = &my_array[1..3];`
    * **その他の重要な型:**
        * **文字列:**
            * `String`: 拡張可能、可変、所有権を持つ文字列データ。 `String::from("...")`を使用するか、他の文字列型から変換して作成されます。
            * `&str`: 文字列スライス。文字列データへの不変のビュー。コードに直接埋め込まれる場合（例: `"hello"`）、しばしば「文字列リテラル」と呼ばれます。
        * **ベクター (`Vec<T>`):** サイズを変更可能な配列で、拡大または縮小できます。 `let mut my_vec: Vec<i32> = Vec::new(); my_vec.push(1); let another_vec = vec![1, 2, 3];`
        * **ハッシュマップ (`HashMap<K, V>`):** キーが一意でハッシュ可能な型であるキーと値のペアを格納します。 `use std::collections::HashMap;`が必要です。
* **演算子:**
    * **算術演算子:** `+`, `-`, `*`, `/`, `%`。
    * **比較演算子:** `==`, `!=`, `>`, `<`, `>=`, `<=`。
    * **論理演算子:** `&&` (AND), `||` (OR), `!` (NOT)。
    * **ビット演算子:** `&` (AND), `|` (OR), `^` (XOR), `!` (NOT), `<<` (左シフト), `>>` (右シフト)。
    * **代入演算子:** `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `^=`, `<<=`, `>>=`。
* **制御フロー:**
    * **`if`, `else if`, `else`:** 条件分岐。
        ```rust
        let number = 7;
        if number < 5 {
            println!("condition was true");
        } else if number == 7 {
            println!("number is seven");
        } else {
            println!("condition was false");
        }
        ```
    * **`loop`:** 無限ループ（終了するには`break`を使用）。
        ```rust
        loop {
            println!("again!");
            break;
        }
        ```
    * **`while`:** 条件が真である限り継続するループ。
        ```rust
        let mut counter = 0;
        while counter < 5 {
            println!("counter is {}", counter);
            counter += 1;
        }
        ```
    * **`for`:** コレクションに対する反復処理。
        ```rust
        let a = [10, 20, 30, 40, 50];
        for element in a.iter() {
            println!("the value is: {}", element);
        }

        for number in 1..5 { // 1から5（5を含まない）まで反復
            println!("{}", number);
        }
        ```
    * **`match`:** 値を一連のパターンと比較する強力な制御フロー構文。
        ```rust
        let number = 3;
        match number {
            1 => println!("one"),
            2 | 3 => println!("two or three"),
            4..=6 => println!("four, five, or six"),
            _ => println!("something else"), // ワイルドカードパターン
        }
        ```
    * **`if let`:** 列挙型やOptionで、一部のバリアントのみに関心がある場合に、より簡潔に処理する方法。
        ```rust
        let some_value = Some(5);
        if let Some(x) = some_value {
            println!("The value is: {}", x);
        }
        ```

**IV. 所有権、借用、ライフタイム**

これらはRustのメモリ安全性保証の核心です。

* **所有権:**
    * Rustの各値には、その*所有者*である変数があります。
    * ある時点で値の所有者は1つだけです。
    * 所有者がスコープを抜けると、値はドロップされます（そのメモリは解放されます）。
* **借用:**
    * 所有権を移す代わりに、値への参照を作成できます。これを*借用*と呼びます。
    * **不変借用 (`&`):** ある値への不変参照を複数同時に持つことができます。不変借用は借用された値の変更を許可しません。
    * **可変借用 (`&mut`):** ある値への可変参照は、同時に最大1つしか持つことができません。可変借用は借用された値の変更を許可します。
    * **借用のルール:**
        1.  任意の時点で、*一つ*の可変参照*または*任意の数の不変参照の*いずれか*を持つことができます。
        2.  参照は常に有効でなければなりません。
* **ライフタイム:**
    * ライフタイムは、参照が有効なスコープを記述する注釈です。Rustコンパイラはライフタイム情報を使用して、参照が指すデータよりも長生きしない（ダングリングポインタにならない）ことを保証します。
    * 多くの場合、コンパイラはライフタイムを自動的に推論できます（ライフタイム省略）。
    * 参照のライフタイムが明確でない場合、関数シグネチャや構造体定義で明示的にライフタイムを注釈する必要があるかもしれません。
    * 明示的なライフタイム注釈の例:
        ```rust
        fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
            if x.len() > y.len() {
                x
            } else {
                y
            }
        }
        ```
        `'a`は、返される文字列スライスが少なくとも両方の入力文字列スライスと同じ期間生存することを示します。

**V. 構造体、列挙型、モジュール**

* **構造体:** 名前付きフィールドをグループ化したユーザー定義データ型。
    ```rust
    struct User {
        active: bool,
        username: String,
        email: String,
        sign_in_count: u64,
    }

    fn main() {
        let mut user1 = User {
            active: true,
            username: String::from("someusername123"),
            email: String::from("someone@example.com"),
            sign_in_count: 1,
        };

        user1.email = String::from("another@example.com");

        let user2 = User {
            email: String::from("another@example.com"),
            ..user1 // 構造体更新記法、残りのフィールドはuser1から
        };
    }
    ```
    * タプル構造体: 名前付きフィールドのない名前付きタプル。 `struct Color(i32, i32, i32);`
    * ユニット様構造体: フィールドのない構造体。 `struct AlwaysEqual;`
* **列挙型 (Enumerations):** 可能なバリアントを列挙して型を定義します。
    ```rust
    enum Message {
        Quit,
        Move { x: i32, y: i32 }, // 無名構造体
        Write(String),
        ChangeColor(i32, i32, i32), // タプル様
    }

    fn main() {
        let q = Message::Quit;
        let m = Message::Move { x: 10, y: 5 };
        let w = Message::Write(String::from("hello"));

        match m {
            Message::Quit => println!("Quit"),
            Message::Move { x, y } => println!("Move to x={}, y={}", x, y),
            Message::Write(text) => println!("Write: {}", text),
            Message::ChangeColor(r, g, b) => println!("Change color to r={}, g={}, b={}", r, g, b),
        }
    }
    ```
    * 列挙型はそのバリアント内に直接データを保持できます。
* **モジュール:** クレート（パッケージ）内でコードを整理します。
    * `mod`キーワードを使用してモジュールを定義します。
    * モジュールは他のモジュール、構造体、列挙型、関数などを含むことができます。
    * 可視性は`pub`（公開）と非公開（デフォルト）で制御します。
    * モジュールパスを使用してモジュール内のアイテムにアクセスします（例: `my_module::my_function()`）。
    * `use`キーワードでアイテムを現在のスコープに持ち込みます（例: `use std::collections::HashMap;`）。
    * モジュールを異なるファイルに分割します（慣例: `my_module`という名前のモジュールは`src/my_module.rs`または`src/my_module/mod.rs`に配置されます）。

**VI. トレイトとジェネリクス**

* **トレイト:** 他の言語のインターフェースや型クラスに類似しています。特定の契約を満たすために型が実装しなければならないメソッドのセットを定義します。
    ```rust
    pub trait Summary {
        fn summarize(&self) -> String;
    }

    pub struct NewsArticle {
        pub headline: String,
        pub location: String,
        pub author: String,
        pub content: String,
    }

    impl Summary for NewsArticle {
        fn summarize(&self) -> String {
            format!("{}, by {} ({})", self.headline, self.author, self.location)
        }
    }

    pub struct Tweet {
        pub username: String,
        pub content: String,
        pub reply: bool,
        pub retweet: bool,
    }

    impl Summary for Tweet {
        fn summarize(&self) -> String {
            format!("{}: {}", self.username, self.content)
        }
    }

    fn main() {
        let tweet = Tweet {
            username: String::from("horse_ebooks"),
            content: String::from("of course, as you probably already know, people"),
            reply: false,
            retweet: false,
        };

        println!("New tweet available! {}", tweet.summarize());
    }
    ```
    * トレイトはメソッドのデフォルト実装を持つことができます。
    * トレイトはジェネリック型の境界として使用できます。
* **ジェネリクス:** コンパイル時に特定の型を知らなくても、複数の型で動作するコードを記述できます。
    ```rust
    fn largest<T: PartialOrd + Copy>(list: &[T]) -> T {
        let mut largest = list[0];

        for &item in list.iter() {
            if item > largest {
                largest = item;
            }
        }

        largest
    }

    fn main() {
        let number_list = vec![34, 50, 25, 100, 65];
        let result = largest(&number_list);
        println!("The largest number is {}", result);

        let char_list = vec!['y', 'm', 'a', 'q'];
        let result = largest(&char_list);
        println!("The largest char is {}", result);
    }
    ```
    * 型パラメータは山括弧`<T>`内で宣言されます。
    * トレイト境界（`T: PartialOrd + Copy`）は、ジェネリック型が実装しなければならない機能を指定します。
    * `PartialOrd`は`>`を使用した比較を可能にし、`Copy`は型が値によってコピーできることを意味します。

**VII. エラーハンドリング**

Rustは明示的なエラーハンドリングを重視します。

* **`Result`列挙型:** 成功（`Ok`）または失敗（`Err`）のいずれかを表します。
    ```rust
    enum Result<T, E> {
        Ok(T),
        Err(E),
    }
    ```
    * `T`は成功値の型。
    * `E`はエラー値の型。
    * 失敗する可能性のある操作（例: ファイルI/O、ネットワークリクエスト）で一般的に使用されます。
    * `?`演算子は`Result`値を処理するための糖衣構文です。`Result`が`Ok`の場合、値をアンラップします。`Err`の場合、現在の関数から早期にエラーを返します。
* **`panic!`マクロ:** プログラムを即座にクラッシュさせます。一般的に回復不能なエラーに使用されます。
    ```rust
    fn main() {
        let v = vec![1, 2, 3];
        // v[99]; // これは実行時にパニックを引き起こします
        panic!("Crash and burn!");
    }
    ```
* **`Option`列挙型:** 存在するかもしれないししないかもしれない値を表します。
    ```rust
    enum Option<T> {
        Some(T),
        None,
    }
    ```
    * nullポインタを避けるために使用されます。
    * `unwrap()`, `unwrap_or()`, `map()`, `and_then()`などのメソッドは`Option`値を操作するために使用されます。
    ```rust
    fn divide(a: i32, b: i32) -> Option<i32> {
        if b == 0 {
            None
        } else {
            Some(a / b)
        }
    }

    fn main() {
        let result1 = divide(10, 2);
        match result1 {
            Some(value) => println!("Result: {}", value),
            None => println!("Cannot divide by zero"),
        }

        let result2 = divide(5, 0);
        println!("Result 2: {:?}", result2.unwrap_or(-1)); // Noneの場合-1を返す
    }
    ```

**VIII. クロージャとイテレータ**

* **クロージャ:** 周囲のスコープから変数を捕捉できる無名関数。
    ```rust
    fn main() {
        let x = 4;
        let equal_to_x = |z| z == x; // xを捕捉するクロージャ

        println!("Is 5 equal to x? {}", equal_to_x(5));
    }
    ```
    * クロージャ構文: `|パラメータ| -> 戻り値の型 { 本体 }`（戻り値の型はしばしば推論可能）。
    * クロージャは参照（`&`）、可変参照（`&mut`）、または値（所有権を移動）によって変数を捕捉できます。Rustは捕捉の型を推論します。`move`キーワードを使用して所有権の移転を強制します。
* **イテレータ:** 一連の要素を処理する方法を提供します。
    * ベクター、配列、ハッシュマップなどのコレクションに対して`iter()`メソッド（不変反復用）、`iter_mut()`（可変反復用）、`into_iter()`（コレクションを消費して要素の所有権を取得）を呼び出すことで作成されます。
    * イテレータは遅延評価されます。明示的に消費されたときにのみ値を生成します。
    * 一般的なイテレータアダプタ（イテレータを変換するメソッド）: `map()`, `filter()`, `take()`, `skip()`, `zip()`, `enumerate()`など。
    * 一般的なイテレータコンシューマ（最終的な値を生成するメソッド）: `collect()`, `sum()`, `product()`, `fold()`, `any()`, `all()`など。
    ```rust
    fn main() {
        let v1 = vec![1, 2, 3];

        let v1_iter = v1.iter(); // v1に対するイテレータを作成

        for val in v1_iter {
            println!("Got: {}", val);
        }

        let v2: Vec<_> = v1.iter().map(|x| x + 1).collect(); // 変換して収集
        println!("v2: {:?}", v2);

        let sum: i32 = v1.iter().sum(); // 合計を得るためにイテレータを消費
        println!("Sum of v1: {}", sum);
    }
    ```

**IX. スマートポインタ**

スマートポインタは、ポインタのように振る舞うが、追加のメタデータと機能を持つデータ構造です。通常の参照とは異なるルールのセットを強制します。

* **`Box<T>`:** 最も単純なスマートポインタ。ヒープにメモリを確保し、値の所有権を提供します。`Box`がスコープを抜けると、ヒープ上の値がドロップされます。以下の場合に有用です:
    * コンパイル時にサイズがわからないデータ。
    * 大量のデータの所有権の転送。
    * 再帰的なデータ構造の作成。
* **`Rc<T>` (参照カウント):** プログラムの複数の部分が同じデータへの読み取り専用アクセスを持つことを可能にします。データは最後の`Rc`ポインタがスコープを抜けたときにのみクリーンアップされます。スレッドセーフではありません。
* **`Arc<T>` (アトミック参照カウント):** `Rc<T>`に類似していますが、並行シナリオで使用するためのスレッドセーフです。`Rc<T>`と比較して多少のパフォーマンスオーバーヘッドがあります。
* **`Cell<T>` と `RefCell<T>` (内部可変性):** 不変参照がある場合でもデータを変更できるようにします。これはRustの通常の借用ルールに違反し、特定の制御された状況で使用されます。
    * `Cell<T>`: `Copy`である型用。値の設定と取得を許可します。
    * `RefCell<T>`: `Copy`でない型用。実行時借用チェックを提供します（実行時に借用ルールが違反されるとパニックします）。
* **`Mutex<T>` と `RwLock<T>` (並行性プリミティブ):** スレッド間での安全な共有可変アクセスのためのメカニズムを提供します。
    * `Mutex<T>`: 一度に1つのスレッドのみがロックを保持し、データにアクセスできます。
    * `RwLock<T>`: 複数のリーダーまたは単一のライターがデータにアクセスできます。

**X. 並行性**

Rustは優れた組み込みの並行性サポートを備えています。

* **スレッド:** `std::thread::spawn`を使用して新しいOSスレッドを生成します。
    ```rust
    use std::thread;
    use std::time::Duration;

    fn main() {
        let handle = thread::spawn(|| {
            for i in 1..10 {
                println!("hi number {} from the spawned thread!", i);
                thread::sleep(Duration::from_millis(1));
            }
        });

        for i in 1..5 {
            println!("hi number {} from the main thread!", i);
            thread::sleep(Duration::from_millis(1));
        }

        handle.join().unwrap(); // 生成されたスレッドが終了するのを待つ
    }
    ```
* **メッセージパッシング:** チャネル（`std::sync::mpsc`によって提供）を使用してスレッド間でデータを送信します。
    ```rust
    use std::sync::mpsc;
    use std::thread;
    use std::time::Duration;

    fn main() {
        let (tx, rx) = mpsc::channel();

        thread::spawn(move || {
            let val = String::from("hi");
            tx.send(val).unwrap();
            // println!("val is {}", val); // エラー: valは移動済み
        });

        let received = rx.recv().unwrap();
        println!("Got: {}", received);
    }
    ```
* **共有状態並行性:** 複数のスレッド間での安全な共有可変アクセスのために、`Mutex<T>`や`Arc<T>`などのスマートポインタを使用します。

**XI. マクロ**

マクロはRustにおけるメタプログラミングの一形態です。他のコードを記述するコードを書くことを可能にします。

* **宣言的マクロ (`macro_rules!`):** パターンに対してマッチし、それらを他のコードで置き換えます。ボイラープレートを減らすのに強力です。
    ```rust
    macro_rules! vec {
        ( $( $x:expr ),* ) => {
            {
                let mut temp_vec = Vec::new();
                $(
                    temp_vec.push($x);
                )*
                temp_vec
            }
        };
    }

    fn main() {
        let my_vec = vec![1, 2, 3, 4];
        println!("{:?}", my_vec);
    }
    ```
* **手続き的マクロ:** 宣言的マクロよりも強力で複雑です。Rustコードの抽象構文木（AST）に対して操作します。3つのタイプがあります:
    * **関数様マクロ:** 関数呼び出しのように見えます。
    * **属性様マクロ:** `#[...]`構文で使用されます。
    * **導出マクロ:** `#[derive(...)]`で使用され、トレイトを自動的に実装します。

**XII. テスト**

Rustはテストの記述と実行のための組み込みサポートを備えています。

* **単体テスト:** 個々のコード単位（関数、モジュール）をテストします。通常、テスト対象のコードと同じファイル内の`#[cfg(test)]`モジュール内に配置されます。
    ```rust
    pub fn add(left: usize, right: usize) -> usize {
        left + right
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        fn it_works() {
            let result = add(2, 2);
            assert_eq!(result, 4);
        }
    }
    ```
* **結合テスト:** ライブラリやバイナリの異なる部分がどのように連携するかをテストします。プロジェクトの最上位の別個の`tests`ディレクトリに配置されます。
* **テストの実行:** `cargo test`コマンドを使用します。

**XIII. Unsafe Rust**

Rustの安全性保証はコンパイラによって強制されます。しかし、これらの保証を迂回する必要がある状況があります。これは`unsafe`キーワードを使用して行われます。

* **`unsafe`ブロック:** `unsafe`ブロック内のコードは、コンパイラが安全であると保証できない操作を実行できます。例えば:
    * 生ポインタの参照外し（`*const T`, `*mut T`）。
    * `unsafe`関数またはメソッドの呼び出し。
    * `union`のフィールドへのアクセス。
    * 外部（非Rust）コードへのリンク。
* **`unsafe`関数:** `unsafe`操作を含む関数自体が`unsafe`としてマークされます。`unsafe`関数を呼び出すには`unsafe`ブロックが必要です。
* **`unsafe`を使用する理由:** Cライブラリとのインターフェース、低水準システムプログラミング、安全性の不変条件を手動で維持するパフォーマンスクリティカルなコード。
* **重要な注意:** `unsafe`は控えめに、細心の注意を払って使用すべきです。`unsafe`ブロック内でメモリ安全性を保証するのはあなたの責任です。

**XIV. Rustエコシステム**

* **クレート (パッケージ):** Rustプロジェクトで使用できるライブラリまたは実行可能ファイル。 [https://crates.io/](https://crates.io/) で見つかります。
* **人気のクレート:**
    * `serde`: 直列化と復元。
    * `tokio`, `async-std`: 非同期プログラミング。
    * `actix-web`, `rocket`: Webフレームワーク。
    * `diesel`, `sea-orm`: オブジェクト関係マッパー (ORM)。
    * `clap`, `structopt`: コマンドライン引数解析。
    * `log`, `env_logger`: ロギング。
    * `rand`: 乱数生成。
* **Rust標準ライブラリ (`std`):** 必須の機能を提供します。

**XV. 学習リソース**

* **The Rust Programming Language Book:** 公式かつ包括的なガイド ([https://doc.rust-lang.org/book/](https://doc.rust-lang.org/book/))。
* **Rust by Example:** 様々なRust機能を説明する実行可能な例のコレクション ([https://doc.rust-lang.org/rust-by-example/](https://doc.rust-lang.org/rust-by-example/))。
* **The Rustlings Course:** Rustコードを読み書きすることに慣れるための一連の小さな演習 ([https://github.com/rust-lang/rustlings](https://github.com/rust-lang/rustlings))。
* **Rust Documentation:** 公式APIドキュメント ([https://doc.rust-lang.org/std/](https://doc.rust-lang.org/std/))。
* **The Rust Blog:** 公式発表と更新 ([https://blog.rust-lang.org/](https://blog.rust-lang.org/))。
* **Reddit (r/rust), Discord, その他のコミュニティプラットフォーム。**

このガイドはRustを学ぶための強固な基盤を提供します。熟達するための最良の方法は、Rustコードを書く練習をし、エコシステムを探検し、コミュニティに参加することです。Rustの旅での幸運を祈ります！