---
audio: false
generated: true
image: false
lang: hi
layout: post
title: ओपनएसएसएल बिल्ड विफलता को ठीक करना
translated: true
type: note
---

आप `openssl-sys` बिल्ड फेल्योर का सामना कर रहे हैं क्योंकि आपके सिस्टम में pkg-config टूल या OpenSSL डेवलपमेंट हेडर इंस्टॉल नहीं हैं। Ubuntu/Debian पर, सबसे आसान उपाय है:

1. **pkg-config और OpenSSL डेव हेडर इंस्टॉल करें**

   ```bash
   sudo apt update
   sudo apt install pkg-config libssl-dev
   ```

   * `pkg-config` Rust बिल्ड स्क्रिप्ट को यह पता लगाने देता है कि OpenSSL कहाँ है।
   * `libssl-dev` हेडर और लाइब्रेरीज़ प्रदान करता है (यह "–dev" पैकेज है)।

2. **अपना बिल्ड दोबारा चलाएँ**

   ```bash
   cargo clean
   cargo run
   ```

---

### विकल्प: "vendored" फीचर का उपयोग करें

यदि आप सिस्टम OpenSSL पर निर्भर नहीं रहना चाहते (या आपके पास रूट एक्सेस नहीं है), तो आप क्रेट से OpenSSL की एक बंडल्ड कॉपी सोर्स से बनाने के लिए कह सकते हैं:

1. अपने **Cargo.toml** में, अपनी डिपेंडेंसी को इस तरह बदलें:

   ```toml
   [dependencies]
   openssl = { version = "0.10", features = ["vendored"] }
   ```
2. फिर से बिल्ड करें:

   ```bash
   cargo clean
   cargo run
   ```

यह OpenSSL को स्वयं कंपाइल करेगा और उसके साथ लिंक करेगा, जिससे सिस्टम इंस्टॉलेशन की जरूरत खत्म हो जाएगी।

---

### (वैकल्पिक) कस्टम OpenSSL इंस्टॉलेशन

यदि आपने OpenSSL को किसी गैर-मानक लोकेशन पर इंस्टॉल किया है, तो आप बिल्ड को उसकी ओर इशारा कर सकते हैं:

```bash
export OPENSSL_DIR=/path/to/your/openssl
export OPENSSL_LIB_DIR=$OPENSSL_DIR/lib
export OPENSSL_INCLUDE_DIR=$OPENSSL_DIR/include
```

फिर `cargo run` दोबारा चलाएँ। यह openssl-sys को सीधे बता देता है कि हेडर और लाइब्रेरीज़ कहाँ मिलेंगी।

---

> **नोट:** `edition2024` के स्टेबलाइज होने की वार्निंग हानिरहित है—आप उस फीचर को अपने `Cargo.toml` से हटा सकते हैं, लेकिन यह आपके बिल्ड को रोकेगी नहीं।