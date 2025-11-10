---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Rustの主な機能の例
translated: true
type: note
---

以下は、借用、可変性、所有権、構造体、列挙型、パターンマッチングなど、いくつかの重要な機能を示すシンプルなRustコード例です。各機能を説明するコメント付きで、簡潔でありながら示唆に富む例を提供します。

```rust
// Pointを表す構造体を定義
struct Point {
    x: i32,
    y: i32,
}

// 異なる図形のための列挙型を定義
enum Shape {
    Circle(Point, f32), // 中心点と半径
    Rectangle(Point, i32, i32), // 左上の点、幅、高さ
}

// Pointのメソッドを実装
impl Point {
    // 原点からの距離を計算する不変参照
    fn distance_from_origin(&self) -> f32 {
        ((self.x.pow(2) + self.y.pow(2)) as f32).sqrt()
    }

    // 点を移動する可変参照
    fn translate(&mut self, dx: i32, dy: i32) {
        self.x += dx;
        self.y += dy;
    }
}

// 所有権と借用を実演する関数
fn describe_shape(shape: &Shape) -> String {
    match shape {
        Shape::Circle(center, radius) => {
            // centerの不変参照
            format!(
                "中心点({}, {})、半径{}の円",
                center.x, center.y, radius
            )
        }
        Shape::Rectangle(top_left, width, height) => {
            // top_leftの不変参照
            format!(
                "左上点({}, {})、幅{}、高さ{}の長方形",
                top_left.x, top_left.y, width, height
            )
        }
    }
}

fn main() {
    // 可変変数バインディング
    let mut point = Point { x: 3, y: 4 };
    
    // メソッド呼び出しのための不変参照
    println!("原点からの距離: {}", point.distance_from_origin());
    
    // 点を変更するための可変参照
    point.translate(2, 1);
    println!("移動後: ({}, {})", point.x, point.y);
    
    // 図形の作成（所有権は変数に移動）
    let circle = Shape::Circle(point, 5.0);
    
    // 図形を説明するための不変参照
    println!("図形: {}", describe_shape(&circle));
    
    // 要素の所有権を持つベクター
    let mut shapes: Vec<Shape> = Vec::new();
    shapes.push(circle);
    shapes.push(Shape::Rectangle(Point { x: 0, y: 0 }, 10, 20));
    
    // 不変参照での反復処理
    for shape in &shapes {
        println!("ベクター内の図形: {}", describe_shape(shape));
    }
    
    // Optionとパターンマッチング
    let maybe_number: Option<i32> = Some(42);
    match maybe_number {
        Some(num) => println!("数値を取得: {}", num),
        None => println!("数値なし"),
    }
    
    // エラーハンドリングのためのResult
    let result: Result<i32, &str> = Ok(100);
    if let Ok(value) = result {
        println!("Resultの値: {}", value);
    }
}
```

### 実演されている主な機能:
1. **構造体**: 2次元の点を表す`Point`構造体
2. **列挙型**: 異なる図形（円、長方形）を表す`Shape`列挙型
3. **所有権**: `circle`変数が作成時に`point`の所有権を取得
4. **借用**:
   - `distance_from_origin`での不変参照（`&self`）
   - `translate`での可変参照（`&mut self`）
   - `describe_shape`での不変参照（`&Shape`）
5. **可変性**: 可変変数のための`mut`キーワード（`point`、`shapes`）
6. **パターンマッチング**: `describe_shape`と`Option`での`match`使用
7. **メソッド**: `impl Point`ブロックで定義
8. **ベクター**: 図形のコレクションを格納する`Vec<Shape>`
9. **Option**: `Some`と`None`を使ったオプショナル値の処理
10. **Result**: `Ok`と`Err`を使った基本的なエラーハンドリング
11. **文字列フォーマット**: 動的文字列のための`format!`使用

### 出力（実行時）:
```
原点からの距離: 5
移動後: (5, 5)
図形: 中心点(5, 5)、半径5の円
ベクター内の図形: 中心点(5, 5)、半径5の円
ベクター内の図形: 左上点(0, 0)、幅10、高さ20の長方形
数値を取得: 42
Resultの値: 100
```

このコードは簡潔ですが、所有権、借用、可変性といったRustの核となる概念と、型システム、エラーハンドリングを紹介しています。`rustc`または`cargo run`を使ったRustプロジェクトで実行できます。特定の機能についてより深く知りたい場合はお知らせください！