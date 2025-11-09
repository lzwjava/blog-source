---
audio: false
date: 2025-09-07
generated: true
image: false
lang: hi
layout: post
title: मैकओएस पर ओपनजेडीके 8 की स्थापना
translated: true
type: note
---

यहां बताया गया है कि आप **OpenJDK 8** (Java SE 8) को macOS पर **2025** में कैसे इंस्टॉल कर सकते हैं, जिसमें Homebrew, SDKMAN, मैनुअल इंस्टॉलर, और MacPorts के तरीके शामिल हैं। कोई टेबल नहीं—बस स्पष्ट, आसान प्रवाह:

---

## 1. Homebrew का उपयोग करके (`openjdk@8`)

यह macOS पर OpenJDK 8 इंस्टॉल करने के सबसे सरल तरीकों में से एक बना हुआ है।

### चरण:

1. टर्मिनल खोलें।

2. रन करें:

   ```bash
   brew install openjdk@8
   ```

   ([Homebrew Formulae][1])

3. इंस्टॉलेशन के बाद, JDK को लिंक करें ताकि macOS टूल्स इसे डिटेक्ट कर सकें:

   ```bash
   sudo ln -sfn $(brew --prefix)/opt/openjdk@8/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-8.jdk
   ```

   ([Homebrew Formulae][1])

4. वैकल्पिक रूप से, अपने शेल कॉन्फ़िग (जैसे, `.zshrc`) में OpenJDK 8 को अपने PATH में जोड़ें:

   ```bash
   export PATH="$(brew --prefix openjdk@8)/bin:$PATH"
   ```

**Apple Silicon (M-series) उपयोगकर्ताओं के लिए नोट:**
यदि आपको आर्किटेक्चर संबंधी समस्याएँ आती हैं, तो आपको होमब्रू को Rosetta 2 के तहत रन करने की आवश्यकता हो सकती है:

```bash
env /usr/bin/arch -x86_64 /bin/zsh --login
brew install openjdk@8
```

फिर symlink और PATH सेटअप के साथ आगे बढ़ें ([Stack Overflow][2])।

---

## 2. SDKMAN के माध्यम से (Java version manager)

SDKMAN कई Java वर्जन को इंस्टॉल और स्विच करने के लिए एक लचीला टूल है।

### क्विक इंस्टॉल:

```bash
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk list java
sdk install java 8.xxx-tem
```

`8.xxx-tem` को `sdk list java` में दिखाए गए आइडेंटिफायर से रिप्लेस करें। ([Stack Overflow][2])

---

## 3. मैनुअल इंस्टॉलेशन (Oracle / Adoptium / AdoptOpenJDK)

### विकल्प A: Oracle का .dmg / .pkg इंस्टॉलर

1. Oracle के Java SE 8 डाउनलोड पेज से अपनी आर्किटेक्चर के लिए सही इंस्टॉलर डाउनलोड करें।
2. `.dmg` को खोलें, `.pkg` इंस्टॉलर को रन करें, और प्रॉम्प्ट का पालन करें। ([Oracle Documentation][3])
3. एक बार इंस्टॉल हो जाने पर, वर्जन चुनने के लिए `java_home` जैसे टूल्स का उपयोग करें:

   ```bash
   /usr/libexec/java_home -v 1.8 --exec java -version
   ```

### विकल्प B: AdoptOpenJDK या इसी तरह के बिल्ड

AdoptOpenJDK (अब Eclipse Adoptium के तहत) बिल्ड प्रदान करता है—जिसमें इंस्टॉलर और आर्काइव दोनों विकल्प शामिल हैं।

* उदाहरण के लिए, अगस्त 2025 में Salesforce डॉक्यूमेंटेशन AdoptOpenJDK साइट का उपयोग करने, HotSpot JVM के साथ OpenJDK 8 (LTS) चुनने, और इसके इंस्टॉलर के माध्यम से आगे बढ़ने का सुझाव देता है। ([Salesforce][4])

इंस्टॉल करने के बाद, अपना JAVA\_HOME सेट करें, उदा.:

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
export PATH=$JAVA_HOME/bin:$PATH
```

---

## 4. MacPorts

यदि आप Homebrew के बजाय MacPorts का उपयोग कर रहे हैं, तो OpenJDK 8 इंस्टॉल करना सीधा है:

```bash
sudo port install openjdk8
```

यह देखने के लिए कि क्या इंस्टॉल है:

```bash
port contents openjdk8
```

बाद में अपडेट करने के लिए:

```bash
sudo port selfupdate && sudo port upgrade openjdk8
```

([MacPorts][5])

---

## आपके लिए सही तरीका चुनना

| इरादा                                              | सबसे अच्छा तरीका                                  |
| -------------------------------------------------- | ----------------------------------------------- |
| क्विक इंस्टॉल और आसान मेंटेनेंस                  | **Homebrew (`brew install openjdk@8`)**         |
| एक साथ कई Java वर्जन मैनेज करना         | **SDKMAN**                                      |
| पूर्ण नियंत्रण और ऑफिशियल इंस्टॉलर (GUI-फ्रेंडली) | **मैनुअल `.dmg` या `.pkg`** Oracle/Adoptium के माध्यम से |
| MacPorts इकोसिस्टम को प्राथमिकता                  | **MacPorts**                                    |

---

## इंस्टॉलेशन को सत्यापित करना

इंस्टॉलेशन के बाद, इसकी जांच इससे करें:

```bash
java -version
```

Java 8 एक्टिव है इसकी पुष्टि करने के लिए `"1.8.0_xxx"` जैसा कुछ एक्सपेक्ट करें। सटीक नियंत्रण के लिए:

```bash
/usr/libexec/java_home -v 1.8 --exec javac -version
```

---

## अंतिम विचार

संक्षेप में:

* **Homebrew** 2025 में सबसे लोकप्रिय गो-टू है—बस `brew install openjdk@8`, फिर लिंक करें और PATH सेट अप करें।
* **SDKMAN** आपको लचीलापन देता है यदि आप अक्सर Java वर्जन स्विच करते हैं।
* **मैनुअल इंस्टॉलर** (Oracle, Adoptium) एक ठोस, GUI-आधारित फॉलबैक बने हुए हैं।
* **MacPorts** काम करता है यदि वह आपका पसंदीदा पैकेज मैनेजर है।

मुझे बताएं कि क्या आप अपने शेल में सेट अप करने, Java वर्जन के बीच स्विच करने, या रास्ते में किसी और चीज में मदद चाहते हैं!

[1]: https://formulae.brew.sh/formula/openjdk%408?utm_source=chatgpt.com "openjdk@8"
[2]: https://stackoverflow.com/questions/24342886/how-to-install-java-8-on-mac?utm_source=chatgpt.com "How to install Java 8 on Mac"
[3]: https://docs.oracle.com/javase/8/docs/technotes/guides/install/mac_jdk.html?utm_source=chatgpt.com "JDK 8 Installation for macOS"
[4]: https://help.salesforce.com/s/articleView?id=001117155&language=en_US&type=1&utm_source=chatgpt.com "How to Install OpenJDK 8 on macOS to Work with Anypoint ..."
[5]: https://ports.macports.org/port/openjdk8/?utm_source=chatgpt.com "Install openjdk8 on macOS with MacPorts"