---
audio: false
generated: true
lang: hant
layout: post
title: Rust 程式語言
translated: true
type: note
---

好的，這是一份關於 Rust 程式語言的綜合指南，涵蓋其核心概念、語法及進階功能。Rust 是一種專注於安全性、速度和並行處理的系統程式語言。

**I. Rust 簡介**

* **什麼是 Rust？**
    * Rust 是一種多範式、靜態型別、編譯型的程式語言，專為效能和安全性而設計，特別適用於系統程式設計、遊戲引擎、Web Assembly 和嵌入式系統等領域。
    * 它透過所有權、借用和生命週期系統，在沒有垃圾收集器的情況下實現記憶體安全。
    * Rust 強調零成本抽象，意味著您可以使用高階功能而無需承擔顯著的執行時開銷。
* **主要特性與設計原則：**
    * **記憶體安全：** 在編譯時防止常見錯誤，如空指標解參考、資料競爭和緩衝區溢位。
    * **無資料競爭的並行處理：** 所有權系統使編寫安全的並行程式碼更加容易。
    * **高效能：** 低階控制、零成本抽象和高效的編譯帶來卓越的效能，通常可與 C++ 媲美。
    * **表達力強的型別系統：** 強大的型別推斷、泛型、特徵（類似於介面或型別類別）和代數資料型別。
    * **出色的工具鏈：** Cargo（建置系統和套件管理員）、rustfmt（程式碼格式化工具）、clippy（linter）。
    * **不斷成長的生態系統：** 擁有活躍且充滿活力的社群，以及數量不斷增加的函式庫和框架。
* **使用案例：**
    * 作業系統
    * 遊戲引擎
    * Web Assembly (Wasm)
    * 嵌入式系統
    * 命令列工具
    * 網路程式設計
    * 加密貨幣
    * 高效能運算

**II. 設定 Rust 開發環境**

* **安裝：**
    * 推薦使用 `rustup`（官方 Rust 工具鏈安裝程式）來安裝 Rust。
    * 訪問 [https://rustup.rs/](https://rustup.rs/) 並按照您作業系統的指示進行操作。
    * 在類 Unix 系統上，通常會執行類似以下的命令：`curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
* **驗證安裝：**
    * 開啟您的終端機或命令提示字元並執行：
        * `rustc --version`：顯示 Rust 編譯器版本。
        * `cargo --version`：顯示 Cargo 版本。
* **Cargo：Rust 建置系統與套件管理員：**
    * Cargo 對於管理 Rust 專案至關重要。它負責：
        * 建置您的程式碼。
        * 管理依賴項（crates）。
        * 執行測試。
        * 發布函式庫。
    * **建立新專案：** `cargo new <project_name>`（建立二進位制專案）。`cargo new --lib <library_name>`（建立函式庫專案）。
    * **專案結構：** 典型的 Cargo 專案包含：
        * `Cargo.toml`：包含專案元資料和依賴項的清單檔案。
        * `src/main.rs`：二進位制專案的進入點。
        * `src/lib.rs`：函式庫專案的進入點。
        * `Cargo.lock`：記錄專案中使用的依賴項確切版本。
    * **建置：** `cargo build`（以除錯模式建置專案）。`cargo build --release`（以發行版最佳化建置專案）。
    * **執行：** `cargo run`（建置並執行二進位制檔案）。
    * **新增依賴項：** 將 crate 名稱和版本新增到 `Cargo.toml` 的 `[dependencies]` 區段。Cargo 會自動下載並建置它們。
    * **更新依賴項：** `cargo update`。

**III. 基本 Rust 語法與概念**

* **Hello, World!**
    ```rust
    fn main() {
        println!("Hello, world!");
    }
    ```
    * `fn main()`：程式開始執行的主函式。
    * `println!()`：一個巨集（以 `!` 表示），用於將文字列印到控制台。
* **變數與可變性：**
    * 變數預設是不可變的。要讓變數可變，請使用 `mut` 關鍵字。
    * 宣告：`let variable_name = value;`（型別推斷）。`let variable_name: Type = value;`（顯式型別註解）。
    * 可變變數：`let mut counter = 0; counter = 1;`
    * 常數：使用 `const` 宣告，必須有型別註解，且其值必須在編譯時已知。`const MAX_POINTS: u32 = 100_000;`
    * 遮蔽：您可以宣告一個與先前變數同名的新變數；新變數會遮蔽舊變數。
* **資料型別：**
    * **純量型別：** 表示單一值。
        * **整數：** `i8`, `i16`, `i32`, `i64`, `i128`, `isize`（指標大小的有號整數）；`u8`, `u16`, `u32`, `u64`, `u128`, `usize`（指標大小的無號整數）。整數字面值可以有後綴（例如 `10u32`）。
        * **浮點數：** `f32`（單精度）, `f64`（雙精度）。
        * **布林值：** `bool` (`true`, `false`)。
        * **字元：** `char`（Unicode 純量值，4 位元組）。
        * **單元型別：** `()`（表示空元組或沒有值）。
    * **複合型別：** 將多個值分組。
        * **元組：** 固定大小的有序元素序列，元素型別可能不同。`let my_tuple = (1, "hello", 3.14); let (x, y, z) = my_tuple; let first = my_tuple.0;`
        * **陣列：** 固定大小、元素型別相同的集合。`let my_array = [1, 2, 3, 4, 5]; let months: [&str; 12] = ["...", "..."]; let first = my_array[0];`
        * **切片：** 對陣列或另一個切片中連續元素序列的動態大小檢視。`let slice = &my_array[1..3];`
    * **其他重要型別：**
        * **字串：**
            * `String`：可增長、可變、擁有所有權的字串資料。使用 `String::from("...")` 或轉換其他字串型別來建立。
            * `&str`：字串切片，對字串資料的不可變檢視。當直接嵌入程式碼時（例如 `"hello"`），通常稱為「字串字面值」。
        * **向量 (`Vec<T>`)：** 可調整大小的陣列，可以增長或縮小。`let mut my_vec: Vec<i32> = Vec::new(); my_vec.push(1); let another_vec = vec![1, 2, 3];`
        * **雜湊對映 (`HashMap<K, V>`)：** 儲存鍵值對，其中鍵是唯一的且為可雜湊的型別。需要 `use std::collections::HashMap;`。
* **運算子：**
    * **算術：** `+`, `-`, `*`, `/`, `%`。
    * **比較：** `==`, `!=`, `>`, `<`, `>=`, `<=`。
    * **邏輯：** `&&` (AND), `||` (OR), `!` (NOT)。
    * **位元運算：** `&` (AND), `|` (OR), `^` (XOR), `!` (NOT), `<<` (左移), `>>` (右移)。
    * **賦值：** `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `^=`, `<<=`, `>>=`。
* **控制流：**
    * **`if`, `else if`, `else`：** 條件執行。
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
    * **`loop`：** 無限迴圈（使用 `break` 退出）。
        ```rust
        loop {
            println!("again!");
            break;
        }
        ```
    * **`while`：** 只要條件為真就繼續執行的迴圈。
        ```rust
        let mut counter = 0;
        while counter < 5 {
            println!("counter is {}", counter);
            counter += 1;
        }
        ```
    * **`for`：** 遍歷集合。
        ```rust
        let a = [10, 20, 30, 40, 50];
        for element in a.iter() {
            println!("the value is: {}", element);
        }

        for number in 1..5 { // 從 1 迭代到（但不包括）5
            println!("{}", number);
        }
        ```
    * **`match`：** 強大的控制流結構，將值與一系列模式進行比較。
        ```rust
        let number = 3;
        match number {
            1 => println!("one"),
            2 | 3 => println!("two or three"),
            4..=6 => println!("four, five, or six"),
            _ => println!("something else"), // 萬用字元模式
        }
        ```
    * **`if let`：** 一種更簡潔的方式來處理列舉或 Option，當您只關心其中一個或少數幾個變體時使用。
        ```rust
        let some_value = Some(5);
        if let Some(x) = some_value {
            println!("The value is: {}", x);
        }
        ```

**IV. 所有權、借用與生命週期**

這是 Rust 記憶體安全保證的核心。

* **所有權：**
    * Rust 中的每個值都有一個變數作為其*擁有者*。
    * 一個值在同一時間只能有一個擁有者。
    * 當擁有者離開作用域時，該值將被丟棄（其記憶體被釋放）。
* **借用：**
    * 您可以建立值的參考，而不是轉移所有權。這稱為*借用*。
    * **不可變借用 (`&`):** 您可以同時擁有多個對某個值的不可變參考。不可變借用不允許修改借用的值。
    * **可變借用 (`&mut`):** 您在同一時間最多只能有一個對某個值的可變參考。可變借用允許修改借用的值。
    * **借用規則：**
        1.  在任何給定時間，您只能擁有*一個*可變參考*或*任意數量的不可變參考。
        2.  參考必須始終有效。
* **生命週期：**
    * 生命週期是描述參考有效範圍的註解。Rust 編譯器使用生命週期資訊來確保參考不會比它們指向的資料存活更久（懸垂指標）。
    * 在許多情況下，編譯器可以自動推斷生命週期（生命週期省略）。
    * 當參考的生命週期不明確時，您可能需要顯式註解函式簽章或結構定義中的生命週期。
    * 顯式生命週期註解範例：
        ```rust
        fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
            if x.len() > y.len() {
                x
            } else {
                y
            }
        }
        ```
        `'a` 表示回傳的字串切片將至少與兩個輸入字串切片存活一樣久。

**V. 結構、列舉與模組**

* **結構：** 將具名字段分組在一起的使用者定義資料型別。
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
            ..user1 // 結構更新語法，其餘字段來自 user1
        };
    }
    ```
    * 元組結構：沒有具名字段的具名元組。`struct Color(i32, i32, i32);`
    * 單元結構：沒有字段的結構。`struct AlwaysEqual;`
* **列舉：** 透過列舉其可能的變體來定義型別。
    ```rust
    enum Message {
        Quit,
        Move { x: i32, y: i32 }, // 匿名結構
        Write(String),
        ChangeColor(i32, i32, i32), // 類似元組
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
    * 列舉可以直接在其變體中儲存資料。
* **模組：** 在 crate（套件）內組織程式碼。
    * 使用 `mod` 關鍵字定義模組。
    * 模組可以包含其他模組、結構、列舉、函式等。
    * 使用 `pub`（公開）和 private（預設）控制可見性。
    * 使用模組路徑存取模組內的項目（例如 `my_module::my_function()`）。
    * 使用 `use` 關鍵字將項目引入目前作用域（例如 `use std::collections::HashMap;`）。
    * 將模組分離到不同的檔案中（慣例：名為 `my_module` 的模組放在 `src/my_module.rs` 或 `src/my_module/mod.rs` 中）。

**VI. 特徵與泛型**

* **特徵：** 類似於其他語言中的介面或型別類別。它們定義了一組型別必須實作以滿足特定契約的方法。
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
    * 特徵可以為方法提供預設實作。
    * 特徵可以作為泛型型別的約束。
* **泛型：** 編寫可以在編譯時處理多種型別而無需知道具體型別的程式碼。
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
    * 型別參數在角括號 `<T>` 內宣告。
    * 特徵約束 (`T: PartialOrd + Copy`) 指定了泛型型別必須實作的功能。
    * `PartialOrd` 允許使用 `>` 進行比較，而 `Copy` 表示該型別可以透過值複製。

**VII. 錯誤處理**

Rust 強調顯式的錯誤處理。

* **`Result` 列舉：** 表示成功 (`Ok`) 或失敗 (`Err`)。
    ```rust
    enum Result<T, E> {
        Ok(T),
        Err(E),
    }
    ```
    * `T` 是成功值的型別。
    * `E` 是錯誤值的型別。
    * 常用於可能失敗的操作（例如檔案 I/O、網路請求）。
    * `?` 運算子是處理 `Result` 值的語法糖。如果 `Result` 是 `Ok`，則解開其值；如果是 `Err`，則從目前函式提早回傳錯誤。
* **`panic!` 巨集：** 導致程式立即崩潰。通常用於不可恢復的錯誤。
    ```rust
    fn main() {
        let v = vec![1, 2, 3];
        // v[99]; // 這將在執行時導致 panic
        panic!("Crash and burn!");
    }
    ```
* **`Option` 列舉：** 表示一個可能存在也可能不存在的值。
    ```rust
    enum Option<T> {
        Some(T),
        None,
    }
    ```
    * 用於避免空指標。
    * 使用 `unwrap()`, `unwrap_or()`, `map()`, `and_then()` 等方法來處理 `Option` 值。
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
        println!("Result 2: {:?}", result2.unwrap_or(-1)); // 如果為 None 則回傳 -1
    }
    ```

**VIII. 閉包與迭代器**

* **閉包：** 可以從其周圍作用域捕獲變數的匿名函式。
    ```rust
    fn main() {
        let x = 4;
        let equal_to_x = |z| z == x; // 捕獲 x 的閉包

        println!("Is 5 equal to x? {}", equal_to_x(5));
    }
    ```
    * 閉包語法：`|parameters| -> return_type { body }`（回傳型別通常可以推斷）。
    * 閉包可以透過參考 (`&`)、可變參考 (`&mut`) 或值（移動所有權）來捕獲變數。Rust 會推斷捕獲型別。使用 `move` 關鍵字強制轉移所有權。
* **迭代器：** 提供處理元素序列的方法。
    * 透過在集合（如向量、陣列、雜湊對映）上呼叫 `iter()` 方法來建立（用於不可變迭代），`iter_mut()` 用於可變迭代，`into_iter()` 用於消耗集合并取得其元素的所有權。
    * 迭代器是惰性的；只有當明確消耗時才會產生值。
    * 常見的迭代器配接器（轉換迭代器的方法）：`map()`, `filter()`, `take()`, `skip()`, `zip()`, `enumerate()` 等。
    * 常見的迭代器消費者（產生最終值的方法）：`collect()`, `sum()`, `product()`, `fold()`, `any()`, `all()` 等。
    ```rust
    fn main() {
        let v1 = vec![1, 2, 3];

        let v1_iter = v1.iter(); // 建立一個遍歷 v1 的迭代器

        for val in v1_iter {
            println!("Got: {}", val);
        }

        let v2: Vec<_> = v1.iter().map(|x| x + 1).collect(); // 轉換並收集
        println!("v2: {:?}", v2);

        let sum: i32 = v1.iter().sum(); // 消耗迭代器以取得總和
        println!("Sum of v1: {}", sum);
    }
    ```

**IX. 智慧指標**

智慧指標是行為類似指標但具有額外元資料和功能的資料結構。它們強制執行與常規參考不同的規則集。

* **`Box<T>`：** 最簡單的智慧指標。它在堆積上分配記憶體並提供值的所有權。當 `Box` 離開作用域時，堆積上的值將被丟棄。適用於：
    * 在編譯時大小未知的資料。
    * 轉移大量資料的所有權。
    * 建立遞迴資料結構。
* **`Rc<T>`（參考計數）：** 允許程式的多個部分對同一資料具有唯讀存取權。只有當最後一個 `Rc` 指標離開作用域時，資料才會被清理。非執行緒安全。
* **`Arc<T>`（原子參考計數）：** 類似於 `Rc<T>`，但適用於並行情境，是執行緒安全的。與 `Rc<T>` 相比有一些效能開銷。
* **`Cell<T>` 和 `RefCell<T>`（內部可變性）：** 即使存在對資料的不可變參考，也允許修改資料。這違反了 Rust 通常的借用規則，並在特定、受控的情況下使用。
    * `Cell<T>`：適用於 `Copy` 型別。允許設定和取得值。
    * `RefCell<T>`：適用於非 `Copy` 型別。提供執行時借用檢查（如果在執行時違反借用規則則會 panic）。
* **`Mutex<T>` 和 `RwLock<T>`（並行原語）：** 提供跨執行緒安全共享可變存取的機制。
    * `Mutex<T>`：只允許一個執行緒持有鎖並存取資料。
    * `RwLock<T>`：允許多個讀取者或單個寫入者存取資料。

**X. 並行處理**

Rust 具有出色的內建並行處理支援。

* **執行緒：** 使用 `std::thread::spawn` 產生新的 OS 執行緒。
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

        handle.join().unwrap(); // 等待產生的執行緒完成
    }
    ```
* **訊息傳遞：** 使用通道（由 `std::sync::mpsc` 提供）在執行緒之間傳送資料。
    ```rust
    use std::sync::mpsc;
    use std::thread;
    use std::time::Duration;

    fn main() {
        let (tx, rx) = mpsc::channel();

        thread::spawn(move || {
            let val = String::from("hi");
            tx.send(val).unwrap();
            // println!("val is {}", val); // 錯誤：val 已被移動
        });

        let received = rx.recv().unwrap();
        println!("Got: {}", received);
    }
    ```
* **共享狀態並行處理：** 使用智慧指標如 `Mutex<T>` 和 `Arc<T>` 在多個執行緒之間實現安全的共享可變存取。

**XI. 巨集**

巨集是 Rust 中的一種元程式設計形式。它們允許您編寫能生成其他程式碼的程式碼。

* **宣告式巨集 (`macro_rules!`)：** 匹配模式並將其替換為其他程式碼。對於減少樣板程式碼非常強大。
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
* **程序式巨集：** 比宣告式巨集更強大和複雜。它們對 Rust 程式碼的抽象語法樹（AST）進行操作。有三種類型：
    * **類函式巨集：** 看起來像函式呼叫。
    * **類屬性巨集：** 與 `#[...]` 語法一起使用。
    * **派生巨集：** 與 `#[derive(...)]` 一起使用，用於自動實作特徵。

**XII. 測試**

Rust 內建了編寫和執行測試的支援。

* **單元測試：** 測試程式碼的獨立單元（函式、模組）。通常放在與被測試程式碼相同的檔案中，位於 `#[cfg(test)]` 模組內。
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
* **整合測試：** 測試您的函式庫或二進位制檔案的不同部分如何協同工作。放在專案頂層的單獨 `tests` 目錄中。
* **執行測試：** 使用 `cargo test` 命令。

**XIII. 不安全 Rust**

Rust 的安全性保證是由編譯器強制執行的。然而，在某些情況下，您可能需要繞過這些保證。這是透過使用 `unsafe` 關鍵字來完成的。

* **`unsafe` 區塊：** `unsafe` 區塊內的程式碼可以執行編譯器無法保證安全的操作，例如：
    * 解參考原始指標 (`*const T`, `*mut T`)。
    * 呼叫 `unsafe` 函式或方法。
    * 存取 `union` 的字段。
    * 連結到外部（非 Rust）程式碼。
* **`unsafe` 函式：** 包含 `unsafe` 操作的函式本身被標記為 `unsafe`。呼叫 `unsafe` 函式需要 `unsafe` 區塊。
* **使用 `unsafe` 的原因：** 與 C 函式庫互動、低階系統程式設計、在手動維護安全不變量的情況下對效能至關重要的程式碼。
* **重要注意事項：** 應謹慎且極度小心地使用 `unsafe`。您有責任確保 `unsafe` 區塊內的記憶體安全。

**XIV. Rust 生態系統**

* **Crates（套件）：** 可在 Rust 專案中使用的函式庫或可執行檔。可在 [https://crates.io/](https://crates.io/) 找到。
* **熱門 Crates：**
    * `serde`：序列化與反序列化。
    * `tokio`, `async-std`：非同步程式設計。
    * `actix-web`, `rocket`：Web 框架。
    * `diesel`, `sea-orm`：物件關聯對映 (ORM)。
    * `clap`, `structopt`：命令列引數解析。
    * `log`, `env_logger`：日誌記錄。
    * `rand`：亂數生成。
* **Rust 標準函式庫 (`std`)：** 提供基本功能。

**XV. 學習資源**

* **The Rust Programming Language Book：** 官方綜合指南 ([https://doc.rust-lang.org/book/](https://doc.rust-lang.org/book/))。
* **Rust by Example：** 一系列可執行的範例，說明各種 Rust 功能 ([https://doc.rust-lang.org/rust-by-example/](https://doc.rust-lang.org/rust-by-example/))。
* **The Rustlings Course：** 一系列小練習，讓您習慣閱讀和編寫 Rust 程式碼 ([https://github.com/rust-lang/rustlings](https://github.com/rust-lang/rustlings))。
* **Rust Documentation：** 官方 API 文件 ([https://doc.rust-lang.org/std/](https://doc.rust-lang.org/std/))。
* **The Rust Blog：** 官方公告和更新 ([https://blog.rust-lang.org/](https://blog.rust-lang.org/))。
* **Reddit (r/rust), Discord, 和其他社群平台。**

本指南為學習 Rust 提供了堅實的基礎。要熟練掌握 Rust，最好的方法是練習編寫 Rust 程式碼、探索生態系統並參與社群。祝您 Rust 學習之旅順利！