---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: लापता प्रोटोबफ़ इंक्लूड फ़ाइलें ठीक करें
translated: true
type: note
---

### त्रुटि को समझना

यह `greptime-proto` (GreptimeTeam रेपो से commit `14b9dc40` पर पिन किया गया) में विफलता protobuf कंपाइलेशन के दौरान होती है। विशेष रूप से, `protoc` मानक Google well-known type `google/protobuf/duration.proto` (और संभवतः `timestamp.proto` जैसे अन्य) का पता नहीं लगा पा रहा है। इससे GreptimeDB की अपनी protos में import errors का सिलसिला शुरू हो जाता है (उदाहरण के लिए, `ddl.proto` Duration को import करता है, जिससे `database.proto` में undefined type errors होती हैं)।

मूल कारण: आपकी `protoc` इंस्टॉलेशन (मैन्युअल अपग्रेड से) में केवल बाइनरी (`/usr/local/bin/protoc`) शामिल है, लेकिन Google की core protos वाली include files शामिल नहीं हैं। क्रेट के `build.rs` में `prost-build`, Google के includes को स्पष्ट रूप से `--proto_path` सेट किए बिना `protoc` चलाता है, इसलिए यह `"google/protobuf/duration.proto"` जैसे relative imports पर विफल हो जाता है।

यह binary-only protobuf इंस्टॉलेशन के साथ आम है; पूर्ण SDK `/usr/include/google/protobuf/` (या समकक्ष) प्रदान करता है।

### त्वरित समाधान: Protobuf Includes इंस्टॉल करें

चूंकि आपके पास पहले से ही एक recent `protoc` बाइनरी है, इसलिए डाउनग्रेड किए बिना लापता includes को जोड़ें:

1. **पूर्ण Protobuf रिलीज डाउनलोड करें** (आपके protoc संस्करण से मेल खाता हुआ, उदा. 27.3 या नवीनतम):
   ```
   wget https://github.com/protocolbuffers/protobuf/releases/download/v27.3/protoc-27.3-linux-x86_64.zip
   unzip protoc-27.3-linux-x86_64.zip -d protoc-full
   ```

2. **Include Files इंस्टॉल करें**:
   ```
   sudo mkdir -p /usr/local/include/google/protobuf
   sudo cp -r protoc-full/include/google /usr/local/include/
   sudo chmod -R a+r /usr/local/include/google/protobuf  # पठनीयता सुनिश्चित करें
   rm -rf protoc-full protoc-*.zip  # सफाई
   ```

3. **सत्यापित करें**:
   - protoc जांचें: `protoc --version` (≥3.21 होना चाहिए)।
   - includes टेस्ट करें: `ls /usr/local/include/google/protobuf/duration.proto` (मौजूद होना चाहिए)।
   - Quick smoke test: `protoc --proto_path=/usr/local/include proto/greptime/v1/ddl.proto --decode_raw=stdin < /dev/null` (अपने प्रोजेक्ट डिरेक्टरी से; आउटपुट को नजरअंदाज करें, बस "File not found" न होने की जांच करें)।

4. **बिल्ड फिर से आजमाएं**:
   ```
   make clean  # आंशिक बिल्ड्स साफ करता है
   make
   ```

यदि आप `apt` वाले डिस्ट्रो पर हैं (उदा., Ubuntu), एक विकल्प `sudo apt install libprotobuf-dev` है—लेकिन यह एक पुराना संस्करण (उदा., 3.12) इंस्टॉल कर सकता है, जो आपके मैन्युअल protoc से conflict करेगा। यदि ऐसा है, तो मैन्युअल include कॉपी से चिपके रहें और `PROTOC=/usr/local/bin/protoc` को स्पष्ट रूप से सेट करें।

### अतिरिक्त सुझाव
- यदि errors बनी रहती हैं (उदा., `wrappers.proto` जैसी अन्य लापता protos), तो पूर्ण `include/google/` कॉपी उन्हें कवर कर लेगी।
- containerized builds (Docker) के लिए, इन steps को अपने Dockerfile में जोड़ें।
- Post-build, यह सुनिश्चित करने के लिए test करें कि protos सही ढंग से integrate हो रही हैं: `cargo run --bin greptime -- standalone start`।
- greptime-proto का यह revision recent (Oct 2024-ish) है; यदि issues बनी रहती हैं, तो repo में upstream fixes के लिए जांचें।

[GreptimeDB Build Docs](https://github.com/GreptimeTeam/greptimedb#build-from-source)  
[Protobuf Well-Known Types](https://protobuf.dev/reference/protobuf/google.protobuf/)