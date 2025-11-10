---
audio: false
generated: true
image: false
lang: hi
layout: post
title: रस्ट की प्रमुख विशेषताओं का उदाहरण
translated: true
type: note
---

यहाँ रस्ट कोड का एक सरल उदाहरण है जो कई महत्वपूर्ण विशेषताओं को प्रदर्शित करता है, जिसमें उधार लेना (borrowing), परिवर्तनशीलता (mutability), स्वामित्व (ownership), स्ट्रक्ट्स (structs), एनम्स (enums), पैटर्न मिलान (pattern matching), और भी बहुत कुछ शामिल है। मैं इसे संक्षिप्त रखूंगा लेकिन उदाहरणात्मक, साथ ही टिप्पणियों के साथ जो प्रत्येक विशेषता की व्याख्या करती हैं।

```rust
// एक Point को प्रस्तुत करने के लिए एक स्ट्रक्ट परिभाषित करें
struct Point {
    x: i32,
    y: i32,
}

// विभिन्न आकृतियों के लिए एक एनम परिभाषित करें
enum Shape {
    Circle(Point, f32), // केंद्र बिंदु और त्रिज्या
    Rectangle(Point, i32, i32), // ऊपरी-बायाँ बिंदु, चौड़ाई, ऊँचाई
}

// Point के लिए विधियों को लागू करें
impl Point {
    // मूल बिंदु से दूरी की गणना के लिए अपरिवर्तनीय उधार
    fn distance_from_origin(&self) -> f32 {
        ((self.x.pow(2) + self.y.pow(2)) as f32).sqrt()
    }

    // बिंदु को स्थानांतरित करने के लिए परिवर्तनशील उधार
    fn translate(&mut self, dx: i32, dy: i32) {
        self.x += dx;
        self.y += dy;
    }
}

// स्वामित्व और उधार लेने को प्रदर्शित करने वाला फ़ंक्शन
fn describe_shape(shape: &Shape) -> String {
    match shape {
        Shape::Circle(center, radius) => {
            // center का अपरिवर्तनीय उधार
            format!(
                "Circle at ({}, {}) with radius {}",
                center.x, center.y, radius
            )
        }
        Shape::Rectangle(top_left, width, height) => {
            // top_left का अपरिवर्तनीय उधार
            format!(
                "Rectangle at ({}, {}) with width {}, height {}",
                top_left.x, top_left.y, width, height
            )
        }
    }
}

fn main() {
    // परिवर्तनशील वेरिएबल बाइंडिंग
    let mut point = Point { x: 3, y: 4 };
    
    // विधि को कॉल करने के लिए अपरिवर्तनीय उधार
    println!("Distance from origin: {}", point.distance_from_origin());
    
    // बिंदु को संशोधित करने के लिए परिवर्तनशील उधार
    point.translate(2, 1);
    println!("After translation: ({}, {})", point.x, point.y);
    
    // एक आकृति बनाएँ (स्वामित्व वेरिएबल को स्थानांतरित)
    let circle = Shape::Circle(point, 5.0);
    
    // इसे वर्णित करने के लिए आकृति का अपरिवर्तनीय उधार
    println!("Shape: {}", describe_shape(&circle));
    
    // तत्वों के स्वामित्व वाला वेक्टर
    let mut shapes: Vec<Shape> = Vec::new();
    shapes.push(circle);
    shapes.push(Shape::Rectangle(Point { x: 0, y: 0 }, 10, 20));
    
    // अपरिवर्तनीय उधार के साथ पुनरावृति
    for shape in &shapes {
        println!("Shape in vec: {}", describe_shape(shape));
    }
    
    // Option और पैटर्न मिलान
    let maybe_number: Option<i32> = Some(42);
    match maybe_number {
        Some(num) => println!("Got a number: {}", num),
        None => println!("No number"),
    }
    
    // त्रुटि प्रबंधन के लिए Result
    let result: Result<i32, &str> = Ok(100);
    if let Ok(value) = result {
        println!("Result value: {}", value);
    }
}
```

### प्रमुख विशेषताएँ प्रदर्शित:
1.  **स्ट्रक्ट्स**: एक 2D बिंदु को प्रस्तुत करने के लिए `Point` स्ट्रक्ट।
2.  **एनम्स**: विभिन्न आकृतियों (Circle, Rectangle) को प्रस्तुत करने के लिए `Shape` एनम।
3.  **स्वामित्व**: `circle` वेरिएबल ने बनाए जाने पर `point` का स्वामित्व ले लिया।
4.  **उधार लेना**:
    - `distance_from_origin` में अपरिवर्तनीय उधार (`&self`)।
    - `translate` में परिवर्तनशील उधार (`&mut self`)।
    - `describe_shape` में अपरिवर्तनीय उधार (`&Shape`)।
5.  **परिवर्तनशीलता**: परिवर्तनशील वेरिएबल्स (`point`, `shapes`) के लिए `mut` कीवर्ड।
6.  **पैटर्न मिलान**: `describe_shape` में और `Option` के लिए `match` के साथ उपयोग किया गया।
7.  **विधियाँ**: `impl Point` ब्लॉक में परिभाषित।
8.  **वेक्टर्स**: आकृतियों के संग्रह को संग्रहीत करने के लिए `Vec<Shape>`।
9.  **Option**: `Some` और `None` के साथ वैकल्पिक मानों को संभालना।
10. **Result**: `Ok` और `Err` के साथ बुनियादी त्रुटि प्रबंधन।
11. **स्ट्रिंग फ़ॉर्मेटिंग**: गतिशील स्ट्रिंग्स के लिए `format!` का उपयोग।

### आउटपुट (जब चलाया जाता है):
```
Distance from origin: 5
After translation: (5, 5)
Shape: Circle at (5, 5) with radius 5
Shape in vec: Circle at (5, 5) with radius 5
Shape in vec: Rectangle at (0, 0) with width 10, height 20
Got a number: 42
Result value: 100
```

यह कोड संक्षिप्त है लेकिन रस्ट की मूल अवधारणाओं जैसे स्वामित्व, उधार लेना, और परिवर्तनशीलता, साथ ही इसकी टाइप सिस्टम और त्रुटि प्रबंधन को प्रदर्शित करता है। आप इसे `rustc` या `cargo run` के साथ एक रस्ट प्रोजेक्ट का उपयोग करके चला सकते हैं। यदि आप किसी विशिष्ट विशेषता में गहराई से जाना चाहते हैं तो मुझे बताएं!