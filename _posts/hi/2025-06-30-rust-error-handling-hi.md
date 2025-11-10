---
audio: false
generated: true
lang: hi
layout: post
title: रस्ट में अपवादों के बिना त्रुटि प्रबंधन
translated: true
type: note
---

Rust में पारंपरिक अर्थों में **exceptions** नहीं हैं, जैसे Java या C\# में होती हैं। इसके बजाय, यह मुख्य रूप से **return values** के माध्यम से errors को हैंडल करता है, जो Go के `if err != nil` पैटर्न के समान है, लेकिन एक अधिक robust और type-safe approach के साथ।

Rust में errors को कैसे हैंडल किया जाता है, इसका विवरण यहाँ दिया गया है:

**1. Recoverable Errors के लिए `Result<T, E>` Enum:**

यह Rust में errors को हैंडल करने का सबसे आम और idiomatic तरीका है।

  * `Result<T, E>` एक enum है जिसके दो variants होते हैं:
      * `Ok(T)`: सफलता को दर्शाता है और इसमें type `T` का successful value होता है।
      * `Err(E)`: विफलता को दर्शाता है और इसमें type `E` का error value होता है।
  * जब कोई function fail हो सकता है, तो वह एक `Result` return करता है। यह caller को स्पष्ट रूप से success (`Ok`) और failure (`Err`) दोनों cases को deal करने के लिए मजबूर करता है।
  * आप `Ok` और `Err` variants को हैंडल करने के लिए `match` expressions या विभिन्न helper methods (जैसे `map`, `and_then`, `unwrap_or`, `unwrap_or_else`, आदि) का उपयोग करते हैं।

**उदाहरण:**

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

**2. Optional Values के लिए `Option<T>` Enum:**

हालांकि सख्ती से "errors" के लिए नहीं, `Option<T>` `Result` के समान है क्योंकि यह *absence की संभावना* को दर्शाता है।

  * `Option<T>` के दो variants होते हैं:
      * `Some(T)`: value मौजूद है।
      * `None`: value अनुपस्थित है।
  * इसका उपयोग तब किया जाता है जब कोई function वैध रूप से कोई value return नहीं कर सकता (उदाहरण के लिए, किसी list में किसी element को ढूंढना जो मौजूद नहीं हो सकता)।

**3. `?` ऑपरेटर (प्रश्न चिह्न ऑपरेटर):**

यह एक शक्तिशाली syntactic sugar है जो errors को propagate करने को अधिक concise बनाता है, जो Go में `if err != nil { return err }` के common तरीके के समान है।

  * यदि एक `Result` value `Ok` है, तो `?` ऑपरेटर `Ok` value को unwrap कर देता है और execution जारी रहती है।
  * यदि एक `Result` value `Err` है, तो `?` ऑपरेटर तुरंत current function से `Err` value return कर देता है।
  * `?` का उपयोग करने वाले function को स्वयं एक `Result` (या `Option` यदि यह एक `Option` को unwrap कर रहा है) return करना चाहिए।

**`?` के साथ उदाहरण:**

```rust
use std::fs::File;
use std::io::{self, Read}; // io::Read trait import करें

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?; // error propagate करता है यदि file मौजूद नहीं है
    let mut username = String::new();
    username_file.read_to_string(&mut username)?; // error propagate करता है यदि reading fail हो जाती है
    Ok(username)
}

fn main() {
    match read_username_from_file() {
        Ok(username) => println!("Username: {}", username),
        Err(e) => println!("Error reading username: {}", e),
    }
}
```

**4. Unrecoverable Errors के लिए `panic!` मैक्रो:**

`panic!` का उपयोग unrecoverable errors के लिए किया जाता है, जो आमतौर पर program में bug का संकेत देते हैं (उदाहरण के लिए, array की सीमा से बाहर access करना)।

  * जब `panic!` को call किया जाता है, तो program terminate हो जाएगा (या configuration के आधार पर stack को "unwind" करेगा)।
  * Recoverable errors के लिए जिन्हें आपके program को gracefully हैंडल करना चाहिए, इसके उपयोग को आम तौर पर हतोत्साहित किया जाता है।

**पारंपरिक Exceptions से मुख्य अंतर:**

  * **स्पष्टता:** Rust का error handling अत्यधिक explicit है। Function signature स्पष्ट रूप से इंगित करती है कि यह एक error return कर सकती है, और compiler आपको इसे हैंडल करने के लिए *मजबूर* करता है। आप गलती से किसी error को ignore नहीं कर सकते।
  * **कोई "Catch-all" ब्लॉक नहीं:** कोई `try-catch` ब्लॉक नहीं हैं जो किसी भी exception को silently catch कर लेते हैं। आप specific error types के साथ deal करते हैं।
  * **Type Safety:** Errors specific types (`Result<T, E>`) के values होते हैं, जो precise error handling की अनुमति देते हैं और generic exception types की ambiguity से बचाते हैं।
  * **Performance:** `Result` values return करना आम तौर पर exceptions को throw और catch करने की तुलना में अधिक performant होता है, क्योंकि exceptions में अक्सर significant overhead (stack unwinding, आदि) शामिल होती है। Rust को performance-critical applications के लिए डिज़ाइन किया गया है।

संक्षेप में, Rust का error handling model Java या C\# के exceptions की तुलना में Go की "check in every level" philosophy के बहुत करीब है। हालाँकि, `Result` enum और `?` ऑपरेटर के साथ, Rust इस explicit error handling को manageable और आनंददायक बनाने के लिए शक्तिशाली और ergonomic tools प्रदान करता है।