---
audio: false
generated: true
lang: hi
layout: post
title: पोस्टग्रेएसक्यूएल इंस्टॉल करके साइकोपग२ को ठीक करें
translated: true
type: note
---

आपको यह त्रुटि इसलिए मिल रही है क्योंकि `psycopg2` पैकेज को सोर्स से बिल्ड करने के लिए PostgreSQL के `pg_config` एक्जीक्यूटेबल की आवश्यकता होती है, लेकिन यह आपके सिस्टम पर नहीं मिल रहा है। इसका मतलब है कि आपको आवश्यक डिपेंडेंसीज प्रदान करने के लिए अपने macOS सिस्टम पर PostgreSQL इंस्टॉल करने की आवश्यकता है। macOS पर PostgreSQL इंस्टॉल करने और इस समस्या को हल करने के चरण नीचे दिए गए हैं।

### macOS पर PostgreSQL इंस्टॉल करने के चरण

#### 1. **Homebrew का उपयोग करके PostgreSQL इंस्टॉल करें (अनुशंसित)**
macOS पर PostgreSQL को इंस्टॉल और प्रबंधित करने का सबसे आसान तरीका Homebrew है।

1. **Homebrew इंस्टॉल करें (यदि पहले से इंस्टॉल नहीं है)**:
   - टर्मिनल खोलें और यह कमांड चलाएँ:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - होमब्रू इंस्टॉलेशन को पूरा करने के लिए स्क्रीन पर दिए गए निर्देशों का पालन करें।

2. **PostgreSQL इंस्टॉल करें**:
   - टर्मिनल में, यह कमांड चलाएँ:
     ```bash
     brew install postgresql
     ```
   - यह कमांड PostgreSQL और उसकी डिपेंडेंसीज, जिसमें `psycopg2` के लिए आवश्यक `pg_config` एक्जीक्यूटेबल भी शामिल है, को इंस्टॉल कर देगा।

3. **PostgreSQL शुरू करें**:
   - PostgreSQL सर्विस को शुरू करने के लिए, चलाएँ:
     ```bash
     brew services start postgresql
     ```
   - वैकल्पिक रूप से, इसे मैन्युअल रूप से एक सिंगल सेशन के लिए शुरू करने के लिए:
     ```bash
     pg_ctl -D /opt/homebrew/var/postgres start
     ```

4. **इंस्टॉलेशन सत्यापित करें**:
   - जाँचें कि PostgreSQL इंस्टॉल और चल रहा है या नहीं:
     ```bash
     psql --version
     ```
   - आपको PostgreSQL वर्जन दिखाई देना चाहिए (उदाहरण: `psql (PostgreSQL) 17.0`)।
   - आप पुष्टि करने के लिए PostgreSQL शेल में लॉग इन भी कर सकते हैं:
     ```bash
     psql -U $(whoami)
     ```

#### 2. **PostgreSQL के बाद `psycopg2` इंस्टॉल करें**
एक बार PostgreSQL इंस्टॉल हो जाने के बाद, `psycopg2` इंस्टॉल करने का प्रयास करें। अब `pg_config` एक्जीक्यूटेबल आपके PATH में उपलब्ध होना चाहिए।

1. **`psycopg2` इंस्टॉल करें**:
   - चलाएँ:
     ```bash
     pip install psycopg2
     ```
   - यदि आप कोई requirements फ़ाइल उपयोग कर रहे हैं, तो चलाएँ:
     ```bash
     pip install -r scripts/requirements/requirements.local.txt
     ```

2. **विकल्प: `psycopg2-binary` इंस्टॉल करें (आसान विकल्प)**:
   - यदि आप सोर्स से `psycopg2` बिल्ड करने (जिसके लिए PostgreSQL डिपेंडेंसीज की आवश्यकता होती है) से बचना चाहते हैं, तो आप प्रीकंपाइल्ड `psycopg2-binary` पैकेज इंस्टॉल कर सकते हैं:
     ```bash
     pip install psycopg2-binary
     ```
   - नोट: संभावित कम्पैटिबिलिटी समस्याओं के कारण `psycopg2-binary` प्रोडक्शन एनवायरनमेंट के लिए अनुशंसित नहीं है, लेकिन यह डेवलपमेंट या टेस्टिंग के लिए ठीक है।

#### 3. **वैकल्पिक: PATH में `pg_config` जोड़ें (यदि आवश्यक हो)**
यदि PostgreSQL इंस्टॉल करने के बाद भी `pg_config` एक्जीक्यूटेबल नहीं मिल रहा है, तो आपको इसे मैन्युअल रूप से अपने PATH में जोड़ने की आवश्यकता हो सकती है।

1. `pg_config` का पता लगाएँ:
   - होमब्रू आमतौर पर PostgreSQL को `/opt/homebrew/bin` (Apple Silicon के लिए) या `/usr/local/bin` (Intel Macs के लिए) में इंस्टॉल करता है।
   - लोकेशन सत्यापित करें:
     ```bash
     find /opt/homebrew -name pg_config
     ```
     या
     ```bash
     find /usr/local -name pg_config
     ```

2. PATH में जोड़ें:
   - यदि `pg_config` मिल जाता है (उदाहरण के लिए, `/opt/homebrew/bin` में), तो इसे अपने शेल कॉन्फ़िगरेशन फ़ाइल (जैसे `~/.zshrc` या `~/.bash_profile`) को एडिट करके अपने PATH में जोड़ें:
     ```bash
     echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
     ```
   - परिवर्तनों को लागू करें:
     ```bash
     source ~/.zshrc
     ```

3. `pg_config` सत्यापित करें:
   - चलाएँ:
     ```bash
     pg_config --version
     ```
   - यदि यह कोई वर्जन रिटर्न करता है, तो PATH सही ढंग से सेट है।

#### 4. **समस्या निवारण**
- **त्रुटि बनी रहती है**: यदि `pip install psycopg2` अभी भी फेल हो रहा है, तो सुनिश्चित करें कि आपके पास आवश्यक बिल्ड टूल्स हैं:
  - Xcode कमांड लाइन टूल्स इंस्टॉल करें:
    ```bash
    xcode-select --install
    ```
  - यदि आवश्यक हो तो `libpq` (PostgreSQL क्लाइंट लाइब्रेरी) एक्सप्लिसिटली इंस्टॉल करें:
    ```bash
    brew install libpq
    ```

- **Python वर्जन कम्पैटिबिलिटी**: सुनिश्चित करें कि आपका Python वर्जन (आपके मामले में 3.13) `psycopg2` के साथ कम्पैटिबल है। यदि समस्याएँ बनी रहती हैं, तो थोड़े पुराने Python वर्जन (जैसे 3.11 या 3.12) के साथ वर्चुअल एनवायरनमेंट का उपयोग करने पर विचार करें:
  ```bash
  python3.11 -m venv venv
  source venv/bin/activate
  pip install psycopg2
  ```

- **Homebrew जाँचें**: सुनिश्चित करें कि Homebrew अप-टू-डेट है:
  ```bash
  brew update
  brew upgrade
  ```

#### 5. **वैकल्पिक इंस्टॉलेशन विधियाँ (वैकल्पिक)**
यदि आप Homebrew का उपयोग नहीं करना चाहते हैं, तो आप PostgreSQL को इनके माध्यम से इंस्टॉल कर सकते हैं:
- **Postgres.app**:
  - [postgresapp.com](https://postgresapp.com/) से डाउनलोड करें।
  - PostgreSQL को इंस्टॉल और शुरू करने के लिए सेटअप निर्देशों का पालन करें।
  - ऊपर बताए अनुसार `bin` डायरेक्टरी (जैसे `/Applications/Postgres.app/Contents/Versions/latest/bin`) को अपने PATH में जोड़ें।
- **ऑफिशियल PostgreSQL इंस्टॉलर**:
  - [postgresql.org](https://www.postgresql.org/download/macosx/) से macOS इंस्टॉलर डाउनलोड करें।
  - इंस्टॉलेशन विजार्ड का पालन करें।

#### 6. **अपने प्रोजेक्ट को पुनः चलाने का प्रयास करें**
PostgreSQL और `psycopg2` (या `psycopg2-binary`) इंस्टॉल करने के बाद, अपने प्रोजेक्ट को चलाने या requirements को पुनः इंस्टॉल करने का प्रयास करें:
```bash
pip install -r scripts/requirements/requirements.local.txt
```

### अतिरिक्त नोट्स
- **त्रुटि क्यों हुई**: `psycopg2` पैकेज को सोर्स से बिल्ड करने के लिए PostgreSQL डेवलपमेंट लाइब्रेरीज (विशेष रूप से `libpq`) की आवश्यकता होती है। होमब्रू के माध्यम से PostgreSQL इंस्टॉल करने से ये लाइब्रेरीज प्रदान हो जाती हैं।
- **प्रोडक्शन विचार**: प्रोडक्शन के लिए, `psycopg2` (न कि `psycopg2-binary`) का उपयोग करें और सुनिश्चित करें कि आपका PostgreSQL वर्जन टारगेट एनवायरनमेंट से मेल खाता हो।
- **डॉक्युमेंटेशन**: अधिक जानकारी के लिए, `psycopg2` इंस्टॉलेशन गाइड [psycopg.org/docs/install.html](https://www.psycopg.org/docs/install.html) देखें।

यदि आपको और कोई समस्या आती है, तो कृपया विशिष्ट त्रुटि संदेश साझा करें, और मैं आगे समस्या निवारण में मदद कर सकता हूँ!