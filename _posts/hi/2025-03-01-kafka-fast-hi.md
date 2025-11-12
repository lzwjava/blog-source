---
audio: false
generated: true
lang: hi
layout: post
title: काफ्का तेज़ क्यों है
translated: true
type: note
---

### मुख्य बिंदु
- ऐसा प्रतीत होता है कि वीडियो "System Design: Why is Kafka fast?" Apache Kafka की गति को उसके आर्किटेक्चर और डिज़ाइन विकल्पों के माध्यम से समझाता है।
- शोध बताते हैं कि Kafka का प्रदर्शन append-only logs, zero-copy सिद्धांतों, batch processing, और कुशल partitioning द्वारा बढ़ाया जाता है।
- साक्ष्य इस ओर इशारा करते हैं कि Kafka की गति उसके distributed event streaming platform डिज़ाइन के कारण है, जिसमें producers, brokers, और consumers जैसे मुख्य घटक शामिल हैं।

### परिचय
यह ब्लॉग पोस्ट YouTube वीडियो "System Design: Why is Kafka fast?" by ByteByteGo की सामग्री पर आधारित है, जिसका उद्देश्य इसकी अंतर्दृष्टि को पठनीय और संदर्भ के लिए आसान लिखित प्रारूप में बदलना है। Apache Kafka वास्तविक समय डेटा प्रसंस्करण में अपने उच्च प्रदर्शन के लिए जाना जाता है, और यह पोस्ट इसकी गति के पीछे के कारणों का पता लगाती है, जिससे यह इस विषय में नए लोगों के लिए सुलभ हो जाती है।

### Kafka के मुख्य घटक
Apache Kafka एक distributed event streaming platform के रूप में कार्य करता है जिसमें तीन मुख्य घटक होते हैं:
- **Producers**: ऐसे एप्लिकेशन जो डेटा को Kafka topics पर भेजते हैं।
- **Brokers**: सर्वर जो डेटा को स्टोर और प्रबंधित करते हैं, replication और distribution सुनिश्चित करते हैं।
- **Consumers**: ऐसे एप्लिकेशन जो topics से डेटा पढ़ते हैं और उसका प्रसंस्करण करते हैं।

यह संरचना Kafka को डेटा की बड़ी मात्रा को कुशलतापूर्वक संभालने में सक्षम बनाती है, जिससे इसकी गति में योगदान होता है।

### आर्किटेक्चरल लेयर्स और प्रदर्शन ऑप्टिमाइज़ेशन
Kafka का आर्किटेक्चर दो लेयर्स में विभाजित है:
- **Compute Layer**: इसमें producers, consumers, और stream processing के लिए APIs शामिल हैं, जो इंटरैक्शन को सुविधाजनक बनाते हैं।
- **Storage Layer**: इसमें brokers शामिल हैं जो topics और partitions में डेटा स्टोरेज का प्रबंधन करते हैं, जो प्रदर्शन के लिए ऑप्टिमाइज़ किए गए हैं।

मुख्य ऑप्टिमाइज़ेशन में शामिल हैं:
- **Append-Only Logs**: डेटा को क्रमिक रूप से एक फ़ाइल के अंत में लिखना, जो रैंडम राइट्स की तुलना में तेज़ होता है।
- **Zero-Copy Principle**: डेटा को सीधे producer से consumer में स्थानांतरित करना, जिससे CPU ओवरहेड कम होता है।
- **Batch Processing**: डेटा को बैचों में संसाधित करना ताकि प्रति-रिकॉर्ड ओवरहेड कम हो।
- **Asynchronous Replication**: लीडर ब्रोकर को अनुरोधों को serve करने की अनुमति देना जबकि replicas अपडेट होती हैं, जिससे प्रदर्शन हानि के बिना उपलब्धता सुनिश्चित होती है।
- **Partitioning**: समानांतर प्रसंस्करण और उच्च थ्रूपुट के लिए डेटा को कई partitions में वितरित करना।

ये डिज़ाइन विकल्प, जिनका विवरण ByteByteGo की एक सहायक ब्लॉग पोस्ट ([Why is Kafka so fast? How does it work?](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)) में है, यह समझाते हैं कि Kafka गति और स्केलेबिलिटी में क्यों श्रेष्ठ है।

### डेटा फ्लो और रिकॉर्ड संरचना
जब एक producer एक ब्रोकर को एक रिकॉर्ड भेजता है, तो उसे वैलिडेट किया जाता है, डिस्क पर एक commit log में जोड़ा जाता है, और ड्यूरेबिलिटी के लिए replicate किया जाता है, तथा producer को commitment पर सूचित किया जाता है। यह प्रक्रिया sequential I/O के लिए ऑप्टिमाइज़ की गई है, जिससे प्रदर्शन बढ़ता है।

प्रत्येक रिकॉर्ड में शामिल होता है:
- टाइमस्टैम्प: जब event बनाया गया था।
- की: partitioning और ordering के लिए।
- वैल्यू: वास्तविक डेटा।
- हेडर्स: वैकल्पिक मेटाडेटा।

यह संरचना, जैसा कि ब्लॉग पोस्ट में बताया गया है, कुशल डेटा हैंडलिंग सुनिश्चित करती है और Kafka की गति में योगदान देती है।

---

### सर्वे नोट: Apache Kafka के प्रदर्शन का विस्तृत विश्लेषण

यह खंड Apache Kafka के प्रदर्शन की एक व्यापक खोज प्रदान करता है, वीडियो "System Design: Why is Kafka fast?" by ByteByteGo पर विस्तार करता है, और एक संपूर्ण समझ सुनिश्चित करने के लिए अतिरिक्त संसाधनों से जानकारी लेता है। विश्लेषण को Kafka के आर्किटेक्चर, घटकों, और विशिष्ट ऑप्टिमाइज़ेशन को कवर करने के लिए संरचित किया गया है, जिसमें स्पष्टता के लिए विस्तृत स्पष्टीकरण और उदाहरण दिए गए हैं।

#### पृष्ठभूमि और संदर्भ
Apache Kafka, जिसे एक distributed event streaming platform के रूप में विकसित किया गया है, उच्च-थ्रूपुट, कम-लेटेंसी डेटा स्ट्रीमिंग को संभालने की अपनी क्षमता के लिए प्रसिद्ध है, जिससे यह आधुनिक डेटा आर्किटेक्चर में एक मुख्य आधार बन गया है। यह वीडियो, 29 जून, 2022 को प्रकाशित और सिस्टम डिज़ाइन पर एक प्लेलिस्ट का हिस्सा, यह स्पष्ट करना चाहता है कि Kafka तेज़ क्यों है, एक ऐसा विषय जो डेटा स्ट्रीमिंग की जरूरतों में घातीय वृद्धि को देखते हुए महत्वपूर्ण रुचि रखता है। यहाँ का विश्लेषण ByteByteGo की एक विस्तृत ब्लॉग पोस्ट ([Why is Kafka so fast? How does it work?](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)) से सूचित है, जो वीडियो सामग्री को पूरक करती है और अतिरिक्त अंतर्दृष्टि प्रदान करती है।

#### Kafka के मुख्य घटक और आर्किटेक्चर
Kafka की गति इसके मुख्य घटकों से शुरू होती है:
- **Producers**: ये ऐसे एप्लिकेशन या सिस्टम हैं जो events उत्पन्न करते हैं और उन्हें Kafka topics पर भेजते हैं। उदाहरण के लिए, एक वेब एप्लिकेशन उपयोगकर्ता इंटरैक्शन के लिए events produce कर सकता है।
- **Brokers**: ये सर्वर हैं जो एक क्लस्टर बनाते हैं, जो डेटा स्टोर करने, partitions का प्रबंधन करने, और replication को संभालने के लिए जिम्मेदार हैं। एक विशिष्ट सेटअप में फॉल्ट टॉलरेंस और स्केलेबिलिटी के लिए कई brokers शामिल हो सकते हैं।
- **Consumers**: ऐसे एप्लिकेशन जो events को पढ़ने और प्रोसेस करने के लिए topics की सदस्यता लेते हैं, जैसे कि रियल-टाइम डेटा प्रोसेस करने वाले एनालिटिक्स इंजन।

आर्किटेक्चर Kafka को एक event streaming platform के रूप में स्थापित करता है, जो पारंपरिक मैसेज कतारों से इसे अलग करते हुए "message" के बजाय "event" का उपयोग करता है। यह इसके डिज़ाइन में स्पष्ट है, जहाँ events अपरिवर्तनीय होते हैं और partitions के भीतर offsets द्वारा क्रमबद्ध होते हैं, जैसा कि ब्लॉग पोस्ट में विस्तृत है।

| घटक             | भूमिका                                                                 |
|------------------|------------------------------------------------------------------------|
| Producer         | डेटा फ्लो शुरू करते हुए, events को topics पर भेजता है।                 |
| Broker           | डेटा स्टोर और प्रबंधित करता है, replication संभालता है, और consumers को serve करता है। |
| Consumer         | topics से events पढ़ता है और उनका प्रसंस्करण करता है, रियल-टाइम एनालिटिक्स सक्षम करता है। |

ब्लॉग पोस्ट में [इस URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3690db-87b8-4165-8798-37d1d083f837_1600x1527.png) पर एक आरेख शामिल है, जो इस आर्किटेक्चर को दर्शाता है, जो क्लस्टर मोड में producers, brokers, और consumers के बीच इंटरैक्शन दिखाता है।

#### लेयर्ड आर्किटेक्चर: कम्प्यूट और स्टोरेज
Kafka का आर्किटेक्चर दो भागों में बंटा है:
- **Compute Layer**: APIs के माध्यम से संचार सुविधाजनक बनाता है:
  - **Producer API**: events भेजने के लिए एप्लिकेशन द्वारा उपयोग किया जाता है।
  - **Consumer API**: events पढ़ने में सक्षम बनाता है।
  - **Kafka Connect API**: डेटाबेस जैसी बाहरी प्रणालियों के साथ एकीकृत करता है।
  - **Kafka Streams API**: स्ट्रीम प्रोसेसिंग का समर्थन करता है, जैसे कि "orders" जैसे topic के लिए एक KStream बनाना, serialization के लिए Serdes के साथ, और एक REST API के साथ स्ट्रीम प्रोसेसिंग जॉब्स के लिए ksqlDB। दिया गया एक उदाहरण "orders" की सदस्यता लेना, उत्पादों द्वारा एकत्रीकरण करना, और एनालिटिक्स के लिए "ordersByProduct" पर भेजना है।
- **Storage Layer**: इसमें क्लस्टर में Kafka brokers शामिल हैं, जिसमें डेटा topics और partitions में व्यवस्थित होता है। Topics डेटाबेस टेबल के समान होते हैं, और partitions नोड्स में वितरित होते हैं, जिससे स्केलेबिलिटी सुनिश्चित होती है। Partitions के भीतर events offsets द्वारा क्रमबद्ध होते हैं, अपरिवर्तनीय और append-only होते हैं, तथा deletion को एक event के रूप में माना जाता है, जिससे write प्रदर्शन बढ़ता है।

ब्लॉग पोस्ट इसका विवरण देती है, यह नोट करते हुए कि brokers partitions, reads, writes, और replications का प्रबंधन करते हैं, जिसमें [इस URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869cd88-3d6e-43af-8fd0-26f3737d8f1f_1600x559.png) पर एक आरेख replication को दर्शाता है, जैसे कि "orders" में Partition 0 जिसमें तीन replicas हैं: Broker 1 पर leader (offset 4), Broker 2 पर follower (offset 2), और Broker 3 पर follower (offset 3)।

| लेयर            | विवरण                                                                 |
|-----------------|-----------------------------------------------------------------------|
| Compute Layer   | इंटरैक्शन के लिए APIs: Producer, Consumer, Connect, Streams, और ksqlDB। |
| Storage Layer   | क्लस्टर में brokers, topics/partitions वितरित, events offsets द्वारा क्रमबद्ध। |

#### कंट्रोल और डेटा प्लेन
- **Control Plane**: क्लस्टर मेटाडेटा का प्रबंधन करता है, ऐतिहासिक रूप से Zookeeper का उपयोग करता था, अब KRaft मॉड्यूल द्वारा प्रतिस्थापित किया गया है जिसमें चयनित brokers पर controllers होते हैं। यह सरलीकरण Zookeeper को समाप्त करता है, कॉन्फ़िगरेशन को आसान बनाता है और मेटाडेटा प्रसार को एक विशेष topic के माध्यम से अधिक कुशल बनाता है, जैसा कि ब्लॉग पोस्ट में नोट किया गया है।
- **Data Plane**: डेटा replication को संभालता है, जिसमें एक प्रक्रिया होती है जहाँ followers FetchRequest जारी करते हैं, leader डेटा भेजता है, और एक निश्चित offset से पहले रिकॉर्ड्स को commit करता है, जिससे स्थिरता सुनिश्चित होती है। Partition 0 के offsets 2, 3, और 4 का उदाहरण इसे उजागर करता है, जिसमें [इस URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17a4454-a194-45f9-8a1f-f4882501657c_1095x1600.png) पर एक आरेख है।

#### रिकॉर्ड संरचना और ब्रोकर ऑपरेशन
प्रत्येक रिकॉर्ड, जो एक event का अमूर्तन है, शामिल करता है:
- टाइमस्टैम्प: जब बनाया गया था।
- की: ordering, colocation, और retention के लिए, partitioning के लिए महत्वपूर्ण।
- वैल्यू: डेटा सामग्री।
- हेडर्स: वैकल्पिक मेटाडेटा।

की और वैल्यू बाइट एरे हैं, जो serdes के साथ एन्कोड/डिकोड होते हैं, लचीलापन सुनिश्चित करते हैं। ब्रोकर ऑपरेशन में शामिल हैं:
- Producer request सॉकेट रिसीव बफर में लैंड होती है।
- नेटवर्क थ्रेड एक साझा अनुरोध कतार में ले जाती है।
- I/O थ्रेड CRC वैलिडेट करती है, commit log (डिस्क सेगमेंट जिसमें डेटा और इंडेक्स होता है) में जोड़ती है।
- Replication के लिए requests को purgatory में छिपाया जाता है।
- प्रतिक्रिया कतारबद्ध होती है, नेटवर्क थ्रेड सॉकेट सेंड बफर के माध्यम से भेजती है।

यह प्रक्रिया, जो sequential I/O के लिए ऑप्टिमाइज़ की गई है, ब्लॉग पोस्ट में विस्तृत है, जिसमें फ्लो को दर्शाने वाले आरेख हैं, जो Kafka की गति में महत्वपूर्ण योगदान देते हैं।

| रिकॉर्ड घटक      | उद्देश्य                                                                 |
|-------------------|-------------------------------------------------------------------------|
| टाइमस्टैम्प       | रिकॉर्ड करता है कि event कब बनाया गया था।                                |
| की               | ordering, colocation, और retention सुनिश्चित करता है, partitioning के लिए। |
| वैल्यू           | वास्तविक डेटा सामग्री होती है।                                          |
| हेडर्स           | अतिरिक्त जानकारी के लिए वैकल्पिक मेटाडेटा।                               |

#### प्रदर्शन ऑप्टिमाइज़ेशन
कई डिज़ाइन निर्णय Kafka की गति को बढ़ाते हैं:
- **Append-Only Logs**: एक फ़ाइल के अंत में क्रमिक रूप से लिखना डिस्क सीक टाइम को कम करता है, जैसे कि एक डायरी में प्रविष्टियों को अंत में जोड़ना, दस्तावेज़ के बीच में डालने की तुलना में तेज़।
- **Zero-Copy Principle**: डेटा को सीधे producer से consumer में स्थानांतरित करता है, CPU ओवरहेड कम करता है, जैसे बॉक्स को ट्रक से वेयरहाउस में बिना खोले ले जाना, समय बचाता है।
- **Batch Processing**: डेटा को बैचों में संसाधित करना प्रति-रिकॉर्ड ओवरहेड कम करता है, दक्षता में सुधार करता है।
- **Asynchronous Replication**: लीडर ब्रोकर अनुरोधों को serve करता है जबकि replicas अपडेट होती हैं, जिससे प्रदर्शन प्रभाव के बिना उपलब्धता सुनिश्चित होती है।
- **Partitioning**: डेटा को partitions में वितरित करना समानांतर प्रसंस्करण के लिए, थ्रूपुट बढ़ाता है, बड़ी डेटा मात्रा को संभालने में एक प्रमुख कारक।

ये ऑप्टिमाइज़ेशन, जैसा कि ब्लॉग पोस्ट में खोजा गया है, यही कारण हैं कि Kafka उच्च थ्रूपुट और कम लेटेंसी प्राप्त करता है, जिससे यह रियल-टाइम एप्लिकेशन के लिए उपयुक्त होता है।

#### निष्कर्ष और अतिरिक्त अंतर्दृष्टि
Apache Kafka की गति इसके सावधानीपूर्वक डिज़ाइन किए गए आर्किटेक्चर और प्रदर्शन ऑप्टिमाइज़ेशन का परिणाम है, जो append-only logs, zero-copy सिद्धांतों, batch processing, asynchronous replication, और कुशल partitioning का लाभ उठाता है। यह विश्लेषण, वीडियो पर आधारित और ब्लॉग पोस्ट द्वारा पूरक, एक व्यापक दृष्टिकोण प्रदान करता है, जो एक सरल अवलोकन की अपेक्षा रखने वालों के लिए अपनी गहराई में अप्रत्याशित है, जो डिज़ाइन विकल्पों के जटिल संतुलन को प्रकट करता है जो Kafka को डेटा स्ट्रीमिंग में एक नेता बनाते हैं।

ब्लॉग पोस्ट पूर्ण संग्रह के लिए 7-दिवसीय निःशुल्क परीक्षण भी प्रदान करती है, जो [इस सब्सक्रिप्शन लिंक](https://blog.bytebytego.com/subscribe?simple=true&next=https%3A%2F%2Fblog.bytebytego.com%2Fp%2Fwhy-is-kafka-so-fast-how-does-it&utm_source=paywall-free-trial&utm_medium=web&utm_content=137028631&coupon=3920da80) पर सुलभ है, जो रुचि रखने वालों के लिए अतिरिक्त संसाधन प्रदान करती है।

यह विस्तृत खोज एक पूर्ण समझ सुनिश्चित करती है, वीडियो के इरादे के साथ संरेखित करती है कि Kafka के प्रदर्शन पर शिक्षित किया जाए, और विभिन्न स्रोतों से एकत्रित शोध और अंतर्दृष्टि से सूचित है, जिससे सटीकता और गहराई सुनिश्चित होती है।

#### मुख्य उद्धरण
- [System Design: Why is Kafka fast? YouTube video](https://www.youtube.com/watch?v=UNUz1-msbOM)
- [Why is Kafka so fast? How does it work? ByteByteGo blog post](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)
- [Kafka architecture diagram ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3690db-87b8-4165-8798-37d1d083f837_1600x1527.png)
- [Kafka replication diagram ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869cd88-3d6e-43af-8fd0-26f3737d8f1f_1600x559.png)
- [Kafka broker operations diagram ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17a4454-a194-45f9-8a1f-f4882501657c_1095x1600.png)
- [ByteByteGo newsletter subscription for Kafka post](https://blog.bytebytego.com/subscribe?simple=true&next=https%3A%2F%2Fblog.bytebytego.com%2Fp%2Fwhy-is-kafka-so-fast-how-does-it&utm_source=paywall-free-trial&utm_medium=web&utm_content=137028631&coupon=3920da80)