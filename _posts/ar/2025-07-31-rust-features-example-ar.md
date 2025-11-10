---
audio: false
generated: true
image: false
lang: ar
layout: post
title: مثال على الميزات الرئيسية لـ Rust
translated: true
type: note
---

إليك مثالًا بسيطًا للكود بلغة Rust يوضح العديد من الميزات الرئيسية، بما في ذلك الاقتراض، القابلية للتغيير، الملكية، الهياكل، التعدادات، مطابقة الأنماط، والمزيد. سأحافظ على كونها موجزة مع توضيحية، مع تعليقات تشرح كل ميزة.

```rust
// تعريف هيكل لتمثيل Point
struct Point {
    x: i32,
    y: i32,
}

// تعريف تعداد لأشكال مختلفة
enum Shape {
    Circle(Point, f32), // نقطة المركز ونصف القطر
    Rectangle(Point, i32, i32), // النقطة العلوية اليسرى، العرض، الارتفاع
}

// تنفيذ طرق لـ Point
impl Point {
    // اقتراض غير قابل للتغيير لحساب المسافة من الأصل
    fn distance_from_origin(&self) -> f32 {
        ((self.x.pow(2) + self.y.pow(2)) as f32).sqrt()
    }

    // اقتراض قابل للتغيير لتحريك النقطة
    fn translate(&mut self, dx: i32, dy: i32) {
        self.x += dx;
        self.y += dy;
    }
}

// دورة توضح الملكية والاقتراض
fn describe_shape(shape: &Shape) -> String {
    match shape {
        Shape::Circle(center, radius) => {
            // اقتراض غير قابل للتغيير لـ center
            format!(
                "Circle at ({}, {}) with radius {}",
                center.x, center.y, radius
            )
        }
        Shape::Rectangle(top_left, width, height) => {
            // اقتراض غير قابل للتغيير لـ top_left
            format!(
                "Rectangle at ({}, {}) with width {}, height {}",
                top_left.x, top_left.y, width, height
            )
        }
    }
}

fn main() {
    // ربط متغير قابل للتغيير
    let mut point = Point { x: 3, y: 4 };
    
    // اقتراض غير قابل للتغيير لاستدعاء دالة
    println!("Distance from origin: {}", point.distance_from_origin());
    
    // اقتراض قابل للتغيير لتعديل النقطة
    point.translate(2, 1);
    println!("After translation: ({}, {})", point.x, point.y);
    
    // إنشاء شكل (تم نقل الملكية إلى المتغير)
    let circle = Shape::Circle(point, 5.0);
    
    // اقتراض غير قابل للتغيير للشكل لوصفه
    println!("Shape: {}", describe_shape(&circle));
    
    // متجه مع ملكية العناصر
    let mut shapes: Vec<Shape> = Vec::new();
    shapes.push(circle);
    shapes.push(Shape::Rectangle(Point { x: 0, y: 0 }, 10, 20));
    
    // التكرار باقتراض غير قابل للتغيير
    for shape in &shapes {
        println!("Shape in vec: {}", describe_shape(shape));
    }
    
    // Option ومطابقة الأنماط
    let maybe_number: Option<i32> = Some(42);
    match maybe_number {
        Some(num) => println!("Got a number: {}", num),
        None => println!("No number"),
    }
    
    // Result للتعامل مع الأخطاء
    let result: Result<i32, &str> = Ok(100);
    if let Ok(value) = result {
        println!("Result value: {}", value);
    }
}
```

### الميزات الرئيسية الموضحة:
1.  **الهياكل**: هيكل `Point` لتمثيل نقطة ثنائية الأبعاد.
2.  **التعدادات**: تعداد `Shape` لتمثيل أشكال مختلفة (Circle, Rectangle).
3.  **الملكية**: المتغير `circle` يأخذ ملكية `point` عند إنشائه.
4.  **الاقتراض**:
    - اقتراض غير قابل للتغيير (`&self`) في `distance_from_origin`.
    - اقتراض قابل للتغيير (`&mut self`) في `translate`.
    - اقتراض غير قابل للتغيير (`&Shape`) في `describe_shape`.
5.  **القابلية للتغيير**: الكلمة المفتاحية `mut` للمتغيرات القابلة للتغيير (`point`, `shapes`).
6.  **مطابقة الأنماط**: مستخدمة مع `match` في `describe_shape` ومع `Option`.
7.  **الطرق**: معرفة في كتلة `impl Point`.
8.  **المتجهات**: `Vec<Shape>` لتخزين مجموعة من الأشكال.
9.  **Option**: التعامل مع القيم الاختيارية باستخدام `Some` و `None`.
10. **Result**: التعامل الأساسي مع الأخطاء باستخدام `Ok` و `Err`.
11. **تنسيق النصوص**: استخدام `format!` للنصوص الديناميكية.

### الناتج (عند التشغيل):
```
Distance from origin: 5
After translation: (5, 5)
Shape: Circle at (5, 5) with radius 5
Shape in vec: Circle at (5, 5) with radius 5
Shape in vec: Rectangle at (0, 0) with width 10, height 20
Got a number: 42
Result value: 100
```

هذا الكود موجز لكنه يوضح مفاهيم Rust الأساسية مثل الملكية، الاقتراض، والقابلية للتغيير، إلى جانب نظام الأنواع والتحكم في الأخطاء. يمكنك تشغيله باستخدام `rustc` أو مشروع Rust باستخدام `cargo run`.