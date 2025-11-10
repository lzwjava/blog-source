---
audio: false
generated: true
image: false
lang: hi
layout: post
title: रस्ट प्राइवेसी त्रुटि को ठीक करना और बिल्ड को सुव्यवस्थित करना
translated: true
type: note
---

आपके पिछले संदेशों से, मैं समझता हूं कि आप `simple.rs` में `run_simple` फ़ंक्शन के लिए एक प्राइवेसी एरर (`E0603`) के कारण एक Rust प्रोजेक्ट को बिल्ड और रन करने में समस्या का सामना कर रहे हैं। अब आपने `cargo build` और `cargo run` कमांड्स को `Cargo.toml` में सेटल करने या प्रक्रिया को सुव्यवस्थित करने के अन्य तरीकों के बारे में पूछा है। मैं इसे आपके Rust प्रोजेक्ट को बिल्डिंग और रनिंग को सरल बनाने, संभावित रूप से प्रक्रिया को स्वचालित या कस्टमाइज़ करने के लिए कॉन्फ़िगर करने की इच्छा के रूप में व्याख्या करूंगा, और साथ ही पूर्ण समाधान सुनिश्चित करने के लिए पहले की एरर को भी संबोधित करूंगा।

### प्राइवेसी एरर को संबोधित करना
पहले, `E0603` एरर (`function run_simple is private`) को ठीक करते हैं ताकि `cargo build` और `cargo run` काम करें। एरर आउटपुट के आधार पर:

- **`simple.rs` को ठीक करें**:
  `src/simple.rs` खोलें और `run_simple` फ़ंक्शन को `pub` जोड़कर पब्लिक बनाएं:
  ```rust
  pub fn run_simple() {
      // आपका मौजूदा कोड, उदाहरण के लिए:
      println!("Hello from run_simple!");
  }
  ```

- **`main.rs` को सत्यापित करें**:
  सुनिश्चित करें कि `src/main.rs` `simple` मॉड्यूल को सही ढंग से रेफरेंस करता है:
  ```rust
  mod simple;

  fn main() {
      simple::run_simple();
  }
  ```

- **क्लीन और रीबिल्ड करें**:
  पुराने बिल्ड आर्टिफैक्ट्स से बचने के लिए, प्रोजेक्ट को क्लीन करें और दोबारा बिल्ड करें:
  ```bash
  cargo clean
  cargo build
  ```

- **रन करें**:
  अगर बिल्ड सफल होता है, तो प्रोग्राम को रन करें:
  ```bash
  cargo run
  ```

### `cargo build` और `cargo run` को `Cargo.toml` में सेटल करना
"settle down it into Cargo.toml" वाक्यांश बताता है कि आप अपने प्रोजेक्ट को ऐसे कॉन्फ़िगर करना चाहते हैं कि बिल्डिंग और रनिंग सुव्यवस्थित हो, संभवतः `Cargo.toml` में कस्टम बिल्ड या रन व्यवहार को परिभाषित करके। Rust में, `Cargo.toml` मुख्य रूप से प्रोजेक्ट मेटाडेटा, डिपेंडेंसीज़ और बिल्ड सेटिंग्स को कॉन्फ़िगर करता है, लेकिन यह सीधे `cargo build` या `cargo run` जैसी कमांड्स को एम्बेड नहीं करता है। इसके बजाय, आप कर सकते हैं:

1. **मल्टीपल बाइनरीज़ को परिभाषित करें** (अगर `simple.rs` एक अलग एक्जिक्यूटेबल है):
   अगर `simple.rs` एक स्टैंडअलोन बाइनरी होने का इरादा है (`main.rs` द्वारा उपयोग किया जाने वाला मॉड्यूल नहीं), तो आप इसे `Cargo.toml` में `[[bin]]` सेक्शन के अंतर्गत कॉन्फ़िगर कर सकते हैं। उदाहरण के लिए:
   ```toml
   [package]
   name = "example"
   version = "0.1.0"
   edition = "2024"

   [[bin]]
   name = "main"
   path = "src/main.rs"

   [[bin]]
   name = "simple"
   path = "src/simple.rs"
   ```
   - यह Cargo को बताता है कि आपके प्रोजेक्ट में दो बाइनरीज़ हैं: एक `main.rs` से (नाम `main`) और एक `simple.rs` से (नाम `simple`)।
   - दोनों बाइनरीज़ बिल्ड करें:
     ```bash
     cargo build
     ```
   - एक विशिष्ट बाइनरी रन करें:
     ```bash
     cargo run --bin main
     cargo run --bin simple
     ```
   - सुनिश्चित करें कि `simple.rs` में एक `main` फ़ंक्शन है:
     ```rust
     pub fn run_simple() {
         println!("Hello from run_simple!");
     }

     fn main() {
         run_simple();
     }
     ```

2. **एडिशन वार्निंग को ठीक करें**:
   आपके पहले के आउटपुट में `edition2024` फीचर के अनावश्यक होने की चेतावनी दिखाई दी। `Cargo.toml` को 2024 एडिशन का सीधे उपयोग करने के लिए अपडेट करें:
   ```toml
   [package]
   name = "example"
   version = "0.1.0"
   edition = "2024"
   ```
   अगर मौजूद है तो किसी भी `cargo-features = ["edition2024"]` लाइन को हटा दें।

3. **कस्टम बिल्ड स्क्रिप्ट्स** (एडवांस्ड):
   अगर आप विशिष्ट बिल्ड स्टेप्स को स्वचालित करना चाहते हैं (जैसे, `cargo build` से पहले या बाद में कस्टम कमांड्स चलाना), तो आप एक बिल्ड स्क्रिप्ट का उपयोग कर सकते हैं। प्रोजेक्ट रूट में एक `build.rs` फ़ाइल बनाएं:
   ```rust
   fn main() {
       println!("cargo:rerun-if-changed=src/simple.rs");
       // कस्टम बिल्ड लॉजिक यहाँ जोड़ें, उदाहरण के लिए, फ़ाइलें जनरेट करना
   }
   ```
   इसे `Cargo.toml` में रेफरेंस करें:
   ```toml
   [package]
   name = "example"
   version = "0.1.0"
   edition = "2024"
   build = "build.rs"
   ```
   यह `cargo build` को रिप्लेस नहीं करता है लेकिन कस्टम प्री-बिल्ड टास्क्स की अनुमति देता है। आप अभी भी हमेशा की तरह `cargo build` और `cargo run` चलाएंगे।

### `cargo build` और `cargo run` को सुव्यवस्थित करने के वैकल्पिक तरीके
अगर आपका लक्ष्य इन कमांड्स को चलाना सरल या स्वचालित बनाना है, तो यहां अन्य तरीके दिए गए हैं:

1. **शेल एलियासेज़**:
   अपनी शेल कॉन्फ़िगरेशन (जैसे, `~/.bashrc` या `~/.zshrc`) में कमांड्स को छोटा करने के लिए एलियासेज़ बनाएं:
   ```bash
   alias cb='cargo build'
   alias cr='cargo run'
   ```
   - सेव करें और अपनी शेल को रीलोड करें:
     ```bash
     source ~/.bashrc
     ```
   - फिर उपयोग करें:
     ```bash
     cb
     cr
     ```

2. **Makefile**:
   शॉर्टकट्स को परिभाषित करने के लिए प्रोजेक्ट रूट में एक `Makefile` बनाएं:
   ```makefile
   build:
   	cargo build

   run:
   	cargo run

   clean:
   	cargo clean

   all: build run
   ```
   - रन करें:
     ```bash
     make build
     make run
     make all
     ```

3. **Cargo Watch** (डेवलपमेंट के लिए):
   फ़ाइलों में बदलाव होने पर स्वचालित रूप से रीबिल्ड और रन करने के लिए `cargo-watch` का उपयोग करें:
   - इंस्टॉल करें:
     ```bash
     cargo install cargo-watch
     ```
   - रन करें:
     ```bash
     cargo watch -x run
     ```
   - यह `src/` में बदलावों पर नज़र रखता है और `cargo run` को दोबारा चलाता है।

4. **VS Code टास्क्स** (अगर IDE का उपयोग कर रहे हैं):
   अगर आप Visual Studio Code का उपयोग करते हैं, तो एक `.vscode/tasks.json` फ़ाइल बनाएं:
   ```json
   {
       "version": "2.0.0",
       "tasks": [
           {
               "label": "Build",
               "type": "shell",
               "command": "cargo build",
               "group": "build"
           },
           {
               "label": "Run",
               "type": "shell",
               "command": "cargo run",
               "group": "build"
           }
       ]
   }
   ```
   - कमांड पैलेट (`Ctrl+Shift+P` > "Tasks: Run Task") के माध्यम से टास्क्स चलाएं।

5. **`Cargo.toml` में स्क्रिप्ट्स** (लिमिटेड सपोर्ट):
   Cargo मूल रूप से `Cargo.toml` में स्क्रिप्ट एलियासेज़ का समर्थन नहीं करता है, लेकिन आप `cargo-xtask` जैसे टूल का उपयोग कर सकते हैं या स्क्रिप्ट्स को एक अलग `scripts` डायरेक्टरी में परिभाषित कर सकते हैं और उन्हें मैन्युअली रन कर सकते हैं। सरलता के लिए, `Makefile` या शेल एलियासेज़ का उपयोग करें।

### अनुशंसित समाधान
- **एरर को ठीक करें**: `simple.rs` में `run_simple` में `pub` जोड़ें और `main.rs` को सत्यापित करें।
- **`Cargo.toml` को कॉन्फ़िगर करें**: अगर आपको मल्टीपल बाइनरीज़ की आवश्यकता है तो `[[bin]]` सेक्शन का उपयोग करें, या `main.rs` में सिंगल बाइनरी के साथ सरल रखें।
- **कमांड्स को सुव्यवस्थित करें**: डेवलपमेंट के दौरान सुविधा के लिए शेल एलियासेज़ या `Makefile` का उपयोग करें।

### उदाहरण सेटअप
**`Cargo.toml`**:
```toml
[package]
name = "example"
version = "0.1.0"
edition = "2024"
```

**`src/simple.rs`**:
```rust
pub fn run_simple() {
    println!("Hello from run_simple!");
}
```

**`src/main.rs`**:
```rust
mod simple;

fn main() {
    simple::run_simple();
}
```

**`Makefile`** (वैकल्पिक):
```makefile
build:
	cargo build

run:
	cargo run
```

- बिल्ड और रन करें:
  ```bash
  make build
  make run
  ```
  या:
  ```bash
  cargo build
  cargo run
  ```

### ट्रबलशूटिंग
- अगर प्राइवेसी एरर बनी रहती है, तो `src/simple.rs` और `src/main.rs` की सामग्री साझा करें।
- अगर आका "settle down into Cargo.toml" से कुछ विशिष्ट मतलब था (जैसे, कस्टम रन स्क्रिप्ट्स या प्रोफाइल्स), तो स्पष्ट करें, और मैं समाधान को अनुकूलित करूंगा।
- Rust वर्जन चेक करें:
  ```bash
  rustc --version
  ```
  सुनिश्चित करें कि यह `edition = "2024"` के लिए 1.85 या बाद का है।

मुझे बताएं अगर आपको और स्पष्टीकरण की आवश्यकता है या नई एरर आती हैं!