---
audio: false
generated: false
image: false
lang: hi
layout: post
title: कंपनियों को एआई कॉन्टेक्स्ट प्रदान करना चाहिए ताकि एकीकरण सुगम हो
translated: true
---

मुझे एक दोस्त है जो Greptime DB में काम करता है, और मैंने सोचा है कि उनके उत्पाद को मौजूदा प्रणालियों में कैसे तेजी से एकीकृत किया जा सकता है।

## संदर्भ

एक संभावित दृष्टिकोण अधिक AI संदर्भ प्रदान करना है। Greptime DB अपने दस्तावेज़ों को AI उपकरणों जैसे ChatGPT के साथ संगत तरीके से व्यवस्थित कर सकता है, जिससे एकीकरण प्रक्रिया सरल हो जाए।

Greptime DB [https://greptime.com](https://greptime.com) पर दस्तावेज़ प्रदान करता है, लेकिन मुझे संदेह है कि ChatGPT या DeepSeek जैसे उपकरण उनके दस्तावेज़ों के सभी पृष्ठों को कुशलतापूर्वक प्रोसेस कर सकते हैं। इसके अलावा, बहुत सारी जानकारी GitHub रिपॉजिटरी, मुद्दों, आंतरिक दस्तावेज़ों, सार्वजनिक दस्तावेज़ों और अन्य छिपे हुए ज्ञान के टुकड़ों में फैली हुई है जो स्पष्ट रूप से दस्तावेज़ित नहीं हैं।

इसके लिए, Greptime DB को कई विशेष GPT बनाने पड़ सकते हैं। उदाहरण के लिए, वे इस तरह के प्रॉम्प्ट बना सकते हैं:

```

### Greptime Docs:
अधिकृत दस्तावेज़ उपलब्ध हैं: [https://docs.greptime.com](https://docs.greptime.com)

* [Quickstart Guide](https://docs.greptime.com/getting-started/quick-start)
* [User Guide](https://docs.greptime.com/user-guide/overview)
* [Demos](https://github.com/GreptimeTeam/demo-scene)
* [FAQ](https://docs.greptime.com/faq-and-others/faq)

### Repository URLs:
यहाँ GreptimeDB रिपॉजिटरी के रूट से मुख्य निर्देशिकाएँ और फाइलें हैं:

1. [benches](https://github.com/GreptimeTeam/greptimedb/tree/main/benches)
2. [docs](https://github.com/GreptimeTeam/greptimedb/tree/main/docs)
3. [src](https://github.com/GreptimeTeam/greptimedb/tree/main/src)
4. [test](https://github.com/GreptimeTeam/greptimedb/tree/main/test)
5. [third_party](https://github.com/GreptimeTeam/greptimedb/tree/main/third_party)
6. [tools](https://github.com/GreptimeTeam/greptimedb/tree/main/tools)

अतिरिक्त मुख्य फाइलें:

7. [Cargo.lock](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.lock)
8. [Cargo.toml](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.toml)
9. [LICENSE](https://github.com/GreptimeTeam/greptimedb/tree/main/LICENSE)
10. [Makefile](https://github.com/GreptimeTeam/greptimedb/tree/main/Makefile)
11. [README.md](https://github.com/GreptimeTeam/greptimedb/tree/main/README.md)
12. [NOTICE](https://github.com/GreptimeTeam/greptimedb/tree/main/NOTICE)

कृपया किसी भी उपयोगकर्ता प्रश्नों के जवाब देने से पहले इन संसाधनों की खोज करें।

```

इससे उपयोगकर्ता एक GPT-आधारित चैटबॉट के साथ बातचीत कर सकते हैं जो दस्तावेज़ों के आधार पर प्रश्नों के जवाब देता है, जिससे अधिक सटीक जवाब सुनिश्चित होते हैं।

इस GPT को बनाएं: [https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration](https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration)

इस प्रश्न का जवाब नहीं दिया जा सका,

```
`greptimedb/src/query/src/query_engine/context.rs` के बारे में क्या है?
```

## एजेंट

मुझे एक उपकरण `greptimedb-agent` का विचार है जो एकीकरण प्रक्रिया को सरल बनाए।

एक सरल कमांड चलाने का कल्पना करें:

```bash
pip install greptimedb-agent
greptimedb-agent
```

`greptimedb-agent` वर्तमान प्रणाली के बारे में जानकारी एकत्र करेगा, जैसे मशीन विवरण और मौजूदा कोड, ताकि संदर्भ समझा जा सके और Greptime DB को सबसे अच्छी तरह से एकीकृत करने का निर्णय लिया जा सके।

यह कमांड स्वचालित रूप से आपकी कोड को अपडेट करेगा ताकि Greptime DB को एकीकृत किया जा सके, और कुछ ही चरणों में आपका वर्तमान डेटाबेस Greptime DB से बदल दिया जाएगा।