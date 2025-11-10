---
audio: false
generated: true
lang: hant
layout: post
title: Rust 無需例外的錯誤處理
translated: true
type: note
---

Rust **並不像** Java 或 C# 那樣具有傳統意義上的異常處理機制。相反地，它主要透過**返回值**來處理錯誤，類似於 Go 語言的 `if err != nil` 模式，但採用了更穩健且類型安全的方法。

以下是 Rust 處理錯誤的方式解析：

**1. 用於可恢復錯誤的 `Result<T, E>` 枚舉：**

這是 Rust 中最常見且符合語言習慣的錯誤處理方式。

  * `Result<T, E>` 是具有兩種變體的枚舉：
      * `Ok(T)`：代表操作成功，並包含類型為 `T` 的成功值。
      * `Err(E)`：代表操作失敗，並包含類型為 `E` 的錯誤值。
  * 當函數可能失敗時，它會返回一個 `Result`。這強制呼叫方必須明確處理成功（`Ok`）和失敗（`Err`）兩種情況。
  * 您可以使用 `match` 表達式或各種輔助方法（例如 `map`、`and_then`、`unwrap_or`、`unwrap_or_else` 等）來處理 `Ok` 和 `Err` 變體。

**範例：**

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
                Err(e) => panic!("建立檔案時出現問題: {:?}", e),
            },
            other_error => panic!("開啟檔案時出現問題: {:?}", other_error),
        },
    };

    println!("成功開啟或建立檔案: {:?}", greeting_file);
}
```

**2. 用於可選值的 `Option<T>` 枚舉：**

雖然 `Option<T>` 嚴格來說並非用於處理「錯誤」，但它與 `Result` 相似，用於表示*值可能不存在*的情況。

  * `Option<T>` 有兩種變體：
      * `Some(T)`：值存在。
      * `None`：值不存在。
  * 當函數可能合法地不返回值時（例如，在可能不存在的列表中尋找元素），便會使用此枚舉。

**3. `?` 運算子（問號運算子）：**

這是一個強大的語法糖，能讓錯誤傳播變得更簡潔，類似於 Go 語言中常見的 `if err != nil { return err }` 模式。

  * 如果 `Result` 值是 `Ok`，則 `?` 運算子會解開 `Ok` 值並繼續執行。
  * 如果 `Result` 值是 `Err`，則 `?` 運算子會立即從當前函數返回該 `Err` 值。
  * 使用 `?` 的函數本身必須返回 `Result`（或者如果是解開 `Option`，則需返回 `Option`）。

**使用 `?` 的範例：**

```rust
use std::fs::File;
use std::io::{self, Read}; // 導入 io::Read trait

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?; // 若檔案不存在，則傳播錯誤
    let mut username = String::new();
    username_file.read_to_string(&mut username)?; // 若讀取失敗，則傳播錯誤
    Ok(username)
}

fn main() {
    match read_username_from_file() {
        Ok(username) => println!("使用者名稱: {}", username),
        Err(e) => println!("讀取使用者名稱時出錯: {}", e),
    }
}
```

**4. 用於不可恢復錯誤的 `panic!` 巨集：**

`panic!` 用於處理不可恢復的錯誤，這類錯誤通常表示程式存在錯誤（例如，存取陣列時超出索引範圍）。

  * 當呼叫 `panic!` 時，程式將會終止（或根據配置進行堆疊回溯）。
  * 通常不建議將它用於程式應優雅處理的可恢復錯誤。

**與傳統異常處理的主要區別：**

  * **明確性：** Rust 的錯誤處理具有高度明確性。函數簽名明確指出它可能返回錯誤，且編譯器會*強制*您處理該錯誤。您不可能意外地忽略錯誤。
  * **無「全捕」區塊：** 沒有能靜默捕獲任何異常的 `try-catch` 區塊。您需要處理特定的錯誤類型。
  * **類型安全：** 錯誤是特定類型（`Result<T, E>`）的值，這允許進行精確的錯誤處理，並避免了泛型異常類型的模糊性。
  * **效能：** 返回 `Result` 值通常比拋出和捕獲異常更高效，因為異常處理通常涉及大量開銷（堆疊回溯等）。Rust 是為高效能應用程式而設計的。

總而言之，Rust 的錯誤處理模型更接近於 Go 語言的「在每一層檢查」哲學，而非 Java 或 C# 的異常處理機制。然而，透過 `Result` 枚舉和 `?` 運算子，Rust 提供了強大且符合人體工學的工具，使這種明確的錯誤處理變得易於管理，甚至令人愉悅。