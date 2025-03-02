---
audio: false
generated: false
lang: hi
layout: post
title: कंपनियों को एकीकरण को सुविधाजनक बनाने के लिए AI संदर्भ या एजेंट प्रदान करना
  चाहिए
translated: true
---

मेरा एक दोस्त है जो Greptime DB में काम करता है, और मैं सोच रहा हूँ कि उनके उत्पाद को मौजूदा सिस्टम में जल्दी से कैसे एकीकृत किया जाए।

## संदर्भ

एक संभावित दृष्टिकोण यह है कि अधिक AI संदर्भ प्रदान किया जाए। Greptime DB अपने दस्तावेज़ीकरण को इस तरह से व्यवस्थित कर सकता है जो ChatGPT जैसे AI टूल्स के साथ संगत हो, जिससे एकीकरण प्रक्रिया को सुव्यवस्थित किया जा सके।

Greptime DB का दस्तावेज़ीकरण [https://greptime.com](https://greptime.com) पर उपलब्ध है, लेकिन मुझे आश्चर्य है कि क्या ChatGPT या DeepSeek जैसे टूल उनके दस्तावेज़ीकरण के सभी पृष्ठों को कुशलतापूर्वक प्रोसेस कर सकते हैं। इसके अलावा, GitHub रिपॉजिटरीज़, इश्यूज़, आंतरिक दस्तावेज़, सार्वजनिक दस्तावेज़ और अन्य छिपे हुए ज्ञान के टुकड़ों में भी बहुत सारी जानकारी फैली हुई है जो स्पष्ट रूप से दस्तावेज़ीकृत नहीं हैं।

इसे संबोधित करने के लिए, Greptime DB को कई विशेषज्ञ GPT बनाने की आवश्यकता हो सकती है। उदाहरण के लिए, वे इस तरह के प्रॉम्प्ट बना सकते हैं:

कृपया ध्यान दें कि आपने केवल एक कोड ब्लॉक (` ``` `) दिया है, जिसमें कोई टेक्स्ट नहीं है। यदि आप किसी विशिष्ट टेक्स्ट या कोड को अनुवादित करना चाहते हैं, तो कृपया वह टेक्स्ट या कोड प्रदान करें।

### Greptime डॉक्स:  
आधिकारिक दस्तावेज़ यहाँ उपलब्ध है: [https://docs.greptime.com](https://docs.greptime.com)

* [त्वरित प्रारंभ गाइड](https://docs.greptime.com/getting-started/quick-start)  
* [उपयोगकर्ता गाइड](https://docs.greptime.com/user-guide/overview)  
* [डेमो](https://github.com/GreptimeTeam/demo-scene)  
* [सामान्य प्रश्न](https://docs.greptime.com/faq-and-others/faq)

### रिपॉजिटरी URLs:
यहां GreptimeDB रिपॉजिटरी की रूट से मुख्य डायरेक्टरीज़ और फाइलें दी गई हैं:

1. [benches](https://github.com/GreptimeTeam/greptimedb/tree/main/benches)  
2. [docs](https://github.com/GreptimeTeam/greptimedb/tree/main/docs)  
3. [src](https://github.com/GreptimeTeam/greptimedb/tree/main/src)  
4. [test](https://github.com/GreptimeTeam/greptimedb/tree/main/test)  
5. [third_party](https://github.com/GreptimeTeam/greptimedb/tree/main/third_party)  
6. [tools](https://github.com/GreptimeTeam/greptimedb/tree/main/tools)

अतिरिक्त प्रमुख फ़ाइलें:

7. [Cargo.lock](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.lock)  
8. [Cargo.toml](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.toml)  
9. [LICENSE](https://github.com/GreptimeTeam/greptimedb/tree/main/LICENSE)  
10. [Makefile](https://github.com/GreptimeTeam/greptimedb/tree/main/Makefile)  
11. [README.md](https://github.com/GreptimeTeam/greptimedb/tree/main/README.md)  
12. [NOTICE](https://github.com/GreptimeTeam/greptimedb/tree/main/NOTICE)

कृपया किसी भी उपयोगकर्ता प्रश्न का उत्तर देने से पहले इन संसाधनों को खोजें।

```
(यह एक कोड ब्लॉक है, इसे अनुवादित नहीं किया जाना चाहिए।)

यह उपयोगकर्ताओं को एक GPT-आधारित चैटबॉट के साथ बातचीत करने की अनुमति देगा जो दस्तावेज़ीकरण के आधार पर प्रश्नों के उत्तर देता है, जिससे अधिक सटीक प्रतिक्रियाएं सुनिश्चित होती हैं।

आइए इस GPT को बनाएं: [https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration](https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration)

इस प्रश्न का उत्तर नहीं दे सका,

```
`greptimedb/src/query/src/query_engine/context.rs` क्या है?
```



## एजेंट

मैं एक ऐसे टूल की कल्पना करता हूँ जिसे `greptimedb-agent` कहा जाता है, जो एकीकरण प्रक्रिया को सरल बनाने के लिए है।

कल्पना कीजिए कि आप एक साधारण कमांड चला रहे हैं जैसे:

```bash
pip install greptimedb-agent
greptimedb-agent
```

(नोट: कोड ब्लॉक्स को अनुवादित नहीं किया जाता है, क्योंकि ये प्रोग्रामिंग कमांड्स हैं और इन्हें मूल रूप में ही रखना जरूरी है।)

`greptimedb-agent` वर्तमान सिस्टम के बारे में जानकारी को बुद्धिमानी से एकत्र करेगा, जैसे कि मशीन का विवरण और मौजूदा कोड, ताकि संदर्भ को समझ सके और यह तय कर सके कि Greptime DB को सबसे अच्छे तरीके से कैसे एकीकृत किया जाए।

यह कमांड आपके कोड को स्वचालित रूप से अपडेट कर देगा ताकि वह Greptime DB के साथ एकीकृत हो सके, और आपके वर्तमान डेटाबेस को Greptime DB से बिना किसी परेशानी के कुछ ही चरणों में बदल देगा।

