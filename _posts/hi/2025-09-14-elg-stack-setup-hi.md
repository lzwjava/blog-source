---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast:free
title: ईएलजी स्टैक सेटअप और इंस्टालेशन गाइड
translated: true
type: note
---

### ELG स्टैक का अवलोकन (Elasticsearch, Logstash, Grafana)

ELG स्टैक (जो अक्सर ELK स्टैक का एक रूपांतर है जहाँ विज़ुअलाइज़ेशन के लिए Kibana को Grafana से बदल दिया जाता है) डेटा की बड़ी मात्रा, विशेष रूप से एप्लिकेशन, सर्वर और इन्फ्रास्ट्रक्चर से लॉग एकत्र करने, प्रोसेस करने, संग्रहीत करने और विज़ुअलाइज़ करने के लिए एक शक्तिशाली ओपन-सोर्स सूट है। यह रीयल-टाइम मॉनिटरिंग, एनालिटिक्स और अलर्टिंग सक्षम बनाता है। मुख्य घटक:

- **Elasticsearch**: एक वितरित सर्च और एनालिटिक्स इंजन जो बड़े पैमाने पर डेटा को संग्रहीत करने, खोजने और विश्लेषण करने के लिए है।
- **Logstash**: एक डेटा प्रोसेसिंग पाइपलाइन जो कई स्रोतों से डेटा ingests करती है, उसे रूपांतरित करती है, और Elasticsearch को भेजती है।
- **Grafana**: एक विज़ुअलाइज़ेशन और मॉनिटरिंग डैशबोर्ड टूल जो Elasticsearch जैसे डेटा स्रोतों से जुड़कर चार्ट, ग्राफ और अलर्ट बनाता है।

यह गाइड बुनियादी Linux ज्ञान (जैसे, Ubuntu/Debian; अन्य OS के लिए अनुकूलित करें) मानती है। पूर्ण विवरण के लिए आधिकारिक दस्तावेज़ों का उपयोग करें। elastic.co और grafana.com से डाउनलोड के माध्यम से इंस्टालेशन।

#### 1. Elasticsearch इंस्टॉल करें
Elasticsearch डेटा संग्रहण और इंडेक्सिंग संभालता है।

- **पूर्वापेक्षाएँ**: Java 11+ (`sudo apt update && sudo apt install openjdk-11-jdk` के माध्यम से इंस्टॉल करें)।
- डाउनलोड और इंस्टॉल करें:
  ```
  wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
  echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-7.x.list
  sudo apt update && sudo apt install elasticsearch
  ```
- प्रारंभ और सक्षम करें: `sudo systemctl start elasticsearch && sudo systemctl enable elasticsearch`।
- सत्यापित करें: `http://localhost:9200` पर जाएँ – क्लस्टर जानकारी के साथ JSON वापस आना चाहिए।
- बुनियादी कॉन्फ़िगरेशन (`/etc/elasticsearch/elasticsearch.yml` संपादित करें): रिमोट एक्सेस के लिए `network.host: 0.0.0.0` सेट करें (प्रोडक्शन में TLS/फ़ायरवॉल से सुरक्षित करें)।

#### 2. Logstash इंस्टॉल करें
Logstash स्रोतों (जैसे, फ़ाइलें, syslogs) से डेटा खींचता है और उसे Elasticsearch को भेजता है।

- Elasticsearch के साथ इंस्टॉल करें:
  ```
  sudo apt install logstash
  ```
- प्रारंभ और सक्षम करें: `sudo systemctl start logstash && sudo systemctl enable logstash`।
- लॉग ingest करने के लिए उदाहरण कॉन्फ़िगरेशन (`/etc/logstash/conf.d/simple.conf`):
  ```
  input {
    file {
      path => "/var/log/syslog"
      start_position => "beginning"
    }
  }
  filter {
    grok {
      match => { "message" => "%{SYSLOGTIMESTAMP:timestamp} %{SYSLOGHOST:host} %{WORD:program}: %{GREEDYDATA:message}" }
    }
  }
  output {
    elasticsearch {
      hosts => ["localhost:9200"]
    }
    stdout { codec => rubydebug }
  }
  ```
- पाइपलाइन टेस्ट करें: `sudo /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/simple.conf` (लगातार उपयोग के लिए बैकग्राउंड में चलाएँ)।
- कॉन्फ़िगरेशन रीलोड करें: `sudo systemctl restart logstash`।

#### 3. Grafana इंस्टॉल करें
Grafana Elasticsearch डेटा को विज़ुअलाइज़ करने के लिए डैशबोर्ड प्रदान करता है।

- इंस्टॉल करें:
  ```
  wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
  echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
  sudo apt update && sudo apt install grafana
  ```
- प्रारंभ और सक्षम करें: `sudo systemctl start grafana-server && sudo systemctl enable grafana-server`।
- एक्सेस करें: `http://localhost:3000` पर जाएँ (डिफ़ॉल्ट लॉगिन: admin/admin; पासवर्ड बदलें)।
- Elasticsearch से कनेक्ट करें:
  1. Configuration > Data Sources > Add data source पर जाएँ।
  2. "Elasticsearch" चुनें, URL को `http://localhost:9200` सेट करें, इंडेक्स नाम (जैसे, `logstash-*`), और टाइम फ़ील्ड (जैसे, `@timestamp`)।
  3. कनेक्शन सेव करें और टेस्ट करें।

#### पूर्ण ELG पाइपलाइन सेट अप करना
1. **डेटा प्रवाह**: Logstash लॉग एकत्र करता/पार्स करता है → Elasticsearch को भेजता है → Grafana क्वेरी करता है और विज़ुअलाइज़ करता है।
2. **उदाहरण वर्कफ़्लो**:
   - नमूना डेटा भेजें: टेस्टिंग के लिए Logstash इनपुट प्लगइन्स या `stdout` जैसे टूल्स का उपयोग करें।
   - Elasticsearch में इंडेक्स करें: लॉग दस्तावेज़ों के रूप में दिखाई देते हैं (जैसे, Kibana API या सीधे curl के माध्यम से: `curl -X GET "localhost:9200/_search?pretty"`)।
   - Grafana में डैशबोर्ड: पैनल बनाएँ (जैसे, Lucene क्वेरीज़ जैसे `program:kern*` का उपयोग करके समय के साथ लॉग एरर के लिए लाइन चार्ट)।
3. **सुरक्षा की मूल बातें**: HTTPS/TLS, प्रमाणीकरण (जैसे, Elasticsearch के लिए X-Pack), और फ़ायरवॉल का उपयोग करें। प्रोडक्शन के लिए, कई नोड्स/क्लस्टर के साथ स्केल करें।
4. **मॉनिटरिंग**: Elasticsearch में JVM मॉनिटरिंग सक्षम करें; Grafana में थ्रेशोल्ड के लिए बिल्ट-इन अलर्ट हैं।

#### सामान्य समस्याएं और सुझाव
- **मेमोरी की कमी**: `/etc/elasticsearch/jvm.options` में JVM heap बढ़ाएँ (जैसे, `-Xms1g -Xmx1g`)।
- **पोर्ट कॉन्फ्लिक्ट्स**: डिफ़ॉल्ट पोर्ट: Elasticsearch 9200/9300, Logstash 5044, Grafana 3000 – `netstat -tulpn` से जाँचें।
- **प्रदर्शन**: हल्के वजन वाले शिपिंग के लिए Logstash के बजाय beats (जैसे, Filebeat) का उपयोग करें।
- **सीखने के संसाधन**: Elastic के आधिकारिक गाइड (elastic.co/guide), Grafana दस्तावेज़ (grafana.com/docs)। Docker के साथ अभ्यास करें: GitHub पर "ELG stack Docker Compose" खोजें।

कस्टम सेटअप या विशिष्ट त्रुटियों के ट्रबलशूटिंग के लिए, अधिक विवरण प्रदान करें। यह एक प्रारंभिक बिंदु है; ELG लॉग विश्लेषण, IoT डेटा और ऐप मॉनिटरिंग में उत्कृष्ट है।