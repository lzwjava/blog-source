---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Rust 主要功能範例
translated: true
type: note
---

這是一個簡單的 Rust 程式碼範例，展示了幾個關鍵功能，包括借用（borrowing）、可變性（mutability）、所有權（ownership）、結構體（structs）、枚舉（enums）、模式匹配（pattern matching）等。我將保持簡潔但具說明性，並附上解釋每個功能的註解。

```rust
// 定義結構體表示點
struct Point {
    x: i32,
    y: i32,
}

// 定義不同形狀的枚舉
enum Shape {
    Circle(Point, f32), // 中心點和半徑
    Rectangle(Point, i32, i32), // 左上角點、寬度、高度
}

// 為 Point 實現方法
impl Point {
    // 不可變借用計算與原點的距離
    fn distance_from_origin(&self) -> f32 {
        ((self.x.pow(2) + self.y.pow(2)) as f32).sqrt()
    }

    // 可變借用平移點
    fn translate(&mut self, dx: i32, dy: i32) {
        self.x += dx;
        self.y += dy;
    }
}

// 展示所有權和借用的函數
fn describe_shape(shape: &Shape) -> String {
    match shape {
        Shape::Circle(center, radius) => {
            // 對 center 的不可變借用
            format!(
                "圓形位於 ({}, {})，半徑為 {}",
                center.x, center.y, radius
            )
        }
        Shape::Rectangle(top_left, width, height) => {
            // 對 top_left 的不可變借用
            format!(
                "矩形位於 ({}, {})，寬度為 {}，高度為 {}",
                top_left.x, top_left.y, width, height
            )
        }
    }
}

fn main() {
    // 可變變數綁定
    let mut point = Point { x: 3, y: 4 };
    
    // 不可變借用呼叫方法
    println!("與原點的距離: {}", point.distance_from_origin());
    
    // 可變借用修改點
    point.translate(2, 1);
    println!("平移後: ({}, {})", point.x, point.y);
    
    // 建立形狀（所有權轉移給變數）
    let circle = Shape::Circle(point, 5.0);
    
    // 對形狀的不可變借用進行描述
    println!("形狀: {}", describe_shape(&circle));
    
    // 擁有元素所有權的向量
    let mut shapes: Vec<Shape> = Vec::new();
    shapes.push(circle);
    shapes.push(Shape::Rectangle(Point { x: 0, y: 0 }, 10, 20));
    
    // 使用不可變借用迭代
    for shape in &shapes {
        println!("向量中的形狀: {}", describe_shape(shape));
    }
    
    // Option 與模式匹配
    let maybe_number: Option<i32> = Some(42);
    match maybe_number {
        Some(num) => println!("獲得數字: {}", num),
        None => println!("沒有數字"),
    }
    
    // 用於錯誤處理的 Result
    let result: Result<i32, &str> = Ok(100);
    if let Ok(value) = result {
        println!("Result 數值: {}", value);
    }
}
```

### 展示的關鍵功能：
1. **結構體**：用 `Point` 結構體表示二維點
2. **枚舉**：用 `Shape` 枚舉表示不同形狀（圓形、矩形）
3. **所有權**：建立 `circle` 時取得 `point` 的所有權
4. **借用**：
   - `distance_from_origin` 中的不可變借用（`&self`）
   - `translate` 中的可變借用（`&mut self`）
   - `describe_shape` 中的不可變借用（`&Shape`）
5. **可變性**：用於可變變數的 `mut` 關鍵字（`point`、`shapes`）
6. **模式匹配**：在 `describe_shape` 和 `Option` 中使用 `match`
7. **方法**：在 `impl Point` 區塊中定義
8. **向量**：使用 `Vec<Shape>` 儲存形狀集合
9. **Option**：使用 `Some` 和 `None` 處理可選值
10. **Result**：使用 `Ok` 和 `Err` 進行基本錯誤處理
11. **字串格式化**：使用 `format!` 建立動態字串

### 輸出（執行時）：
```
與原點的距離: 5
平移後: (5, 5)
形狀: 圓形位於 (5, 5)，半徑為 5
向量中的形狀: 圓形位於 (5, 5)，半徑為 5
向量中的形狀: 矩形位於 (0, 0)，寬度為 10，高度為 20
獲得數字: 42
Result 數值: 100
```

這段程式碼簡潔地展示了 Rust 的核心概念，如所有權、借用和可變性，以及其類型系統和錯誤處理。您可以使用 `rustc` 或帶有 `cargo run` 的 Rust 專案來執行它。