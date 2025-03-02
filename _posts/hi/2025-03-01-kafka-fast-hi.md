---
audio: false
generated: false
lang: hi
layout: post
title: Kafka Kyun Tez Hai
translated: true
---

### मुख्य बिंदु
- लगता है कि वीडियो "System Design: Why is Kafka fast?" Apache Kafka की गति को उसके आर्किटेक्चर और डिजाइन चॉइसों के माध्यम से समझाता है।
- अनुसंधान सुझाता है कि Kafka की प्रदर्शन में append-only logs, zero-copy principles, batch processing, और efficient partitioning का योगदान है।
- सबूत इस ओर इशारा करते हैं कि Kafka की गति उसकी वितरित इवेंट स्ट्रीमिंग प्लेटफॉर्म डिजाइन से है, जिसमें key components जैसे producers, brokers, और consumers शामिल हैं।

### परिचय
यह ब्लॉग पोस्ट YouTube वीडियो "System Design: Why is Kafka fast?" द्वारा ByteByteGo के सामग्री पर आधारित है, जिसका उद्देश्य इसके insights को लिखित रूप में बदलना है ताकि पढ़ना और संदर्भ लेने आसान हो सके। Apache Kafka को real-time data processing में high performance के लिए जाना जाता है, और यह पोस्ट इसके गति के पीछे के कारणों को खोजता है, जिससे नए लोगों के लिए यह आसान हो सके।

### Kafka के Core Components
Apache Kafka एक वितरित इवेंट स्ट्रीमिंग प्लेटफॉर्म के रूप में काम करता है, जिसमें तीन मुख्य components हैं:
- **Producers**: Applications जो Kafka topics में data भेजते हैं।
- **Brokers**: Servers जो data को store और manage करते हैं, ensuring replication और distribution.
- **Consumers**: Applications जो topics से data को read और process करते हैं।

इस संरचना के कारण Kafka large volumes of data को efficiently handle कर सकता है, जो उसकी गति में योगदान करता है।

### Architectural Layers and Performance Optimizations
Kafka का architecture दो layers में विभाजित है:
- **Compute Layer**: Producers, consumers, और stream processing के लिए APIs शामिल हैं, जो interaction को facilitate करते हैं.
- **Storage Layer**: Brokers जो topics और partitions में data storage manage करते हैं, performance के लिए optimize किया गया है.

Key optimizations में शामिल हैं:
- **Append-Only Logs**: Data को file के end पर sequentially लिखना, जो random writes से तेज है।
- **Zero-Copy Principle**: Data को producer से consumer तक directly transfer करना, CPU overhead को कम करना.
- **Batch Processing**: Data को batches में handle करना, per-record overhead को कम करना.
- **Asynchronous Replication**: Leader broker requests serve करते हुए replicas update करते हैं, availability को ensure करते हुए performance loss को avoid करते हैं.
- **Partitioning**: Data को multiple partitions में distribute करना, parallel processing और high throughput के लिए.

ये design choices, ByteByteGo के supporting blog post में detailed हैं ([Why is Kafka so fast? How does it work?](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)), जो explain करते हैं कि Kafka speed और scalability में क्यों excel करता है।

### Data Flow and Record Structure
जब एक producer एक record को broker को send करता है, तो यह validated, commit log पर disk पर appended, और durability के लिए replicated होता है, producer को commitment पर notify किया जाता है। यह process sequential I/O के लिए optimize किया गया है, performance को enhance करता है।

Each record में शामिल हैं:
- Timestamp: जब event created हुआ था।
- Key: Partitioning और ordering के लिए.
- Value: Actual data.
- Headers: Optional metadata.

इस संरचना, blog post में outlined है, जो efficient data handling को ensure करता है और Kafka की speed में योगदान करता है।

---

### सर्वेक्षण नोट: Apache Kafka के प्रदर्शन का विस्तृत विश्लेषण

इस section में Apache Kafka के प्रदर्शन का एक व्यापक exploration है, जो ByteByteGo के वीडियो "System Design: Why is Kafka fast?" पर आधारित है, और additional resources से draw करता है ताकि thorough understanding ensure हो सके। विश्लेषण Kafka के architecture, components, और specific optimizations को cover करने के लिए structured है, detailed explanations और examples के साथ clarity के लिए।

#### Background and Context
Apache Kafka, एक वितरित इवेंट स्ट्रीमिंग प्लेटफॉर्म के रूप में विकसित किया गया है, high-throughput, low-latency data streaming handle करने के लिए जाना जाता है, making it a staple in modern data architectures. 29 जून, 2022 को published वीडियो, system design के playlist का हिस्सा, Kafka क्यों तेज है, इस topic पर focus करता है, जो data streaming needs के exponential growth के साथ significant interest है। यह विश्लेषण ByteByteGo के detailed blog post से informed है ([Why is Kafka so fast? How does it work?](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)), जो video content को complement करता है और additional insights प्रदान करता है।

#### Kafka के Core Components और Architecture
Kafka की speed उसके core components से शुरू होती है:
- **Producers**: ये applications या systems हैं जो Kafka topics में events generate और send करते हैं। उदाहरण के लिए, एक web application user interactions के लिए events produce कर सकता है।
- **Brokers**: ये servers हैं जो cluster में data store, partitions manage, और replication handle करते हैं। एक typical setup में multiple brokers fault tolerance और scalability के लिए शामिल होते हैं।
- **Consumers**: Applications जो topics को subscribe करते हैं events को read और process करने के लिए, जैसे analytics engines जो real-time data process करते हैं।

Architecture Kafka को एक event streaming platform के रूप में position करता है, "event" के बजाय "message" का use करते हुए, traditional message queues से अलग। यह design में evident है, जहाँ events immutable और offsets के द्वारा partitions में ordered हैं, blog post में detailed है।

| Component       | Role                                                                 |
|-----------------|----------------------------------------------------------------------|
| Producer        | Topics में events send करते हैं, data flow initiate करते हैं.                        |
| Broker          | Data store और manage करते हैं, replication handle करते हैं, और consumers serve करते हैं.   |
| Consumer        | Topics से events read और process करते हैं, real-time analytics enable करते हैं. |

Blog post में एक diagram शामिल है [इस URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3690db-87b8-4165-8798-37d1d083f837_1600x1527.png) पर, जो इस architecture को illustrate करता है, जो producers, brokers, और consumers के interaction को cluster mode में दिखाता है।

#### Layered Architecture: Compute और Storage
Kafka का architecture दो layers में bifurcated है:
- **Compute Layer**: Communication facilitate करते हैं through APIs:
  - **Producer API**: Applications द्वारा events send करने के लिए use किया जाता है.
  - **Consumer API**: Events read करने ke लिए enable करता है.
  - **Kafka Connect API**: External systems जैसे databases के साथ integrate करता है.
  - **Kafka Streams API**: Stream processing support करता है, जैसे "orders" के लिए KStream create करना, Serdes के साथ serialization, और ksqlDB के साथ stream processing jobs, REST API के साथ. एक example provided है "orders" subscribe करना, products के द्वारा aggregate करना, और "ordersByProduct" के लिए analytics send करना.
- **Storage Layer**: Kafka brokers in clusters, data topics और partitions में organize किया गया है। Topics database tables के समान हैं, और partitions nodes के across distributed हैं, ensuring scalability। Partitions में events offsets के द्वारा ordered, immutable, और append-only हैं, deletion को event के रूप में treat किया जाता है, write performance enhance करता है.

Blog post details this, noting कि brokers partitions, reads, writes, और replications manage करते हैं, एक diagram के साथ [इस URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869cd88-3d6e-43af-8fd0-26f3737d8f1f_1600x559.png) पर, replication illustrate करता है, जैसे "orders" में Partition 0 के साथ three replicas: leader on Broker 1 (offset 4), followers on Broker 2 (offset 2), और Broker 3 (offset 3).

| Layer           | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| Compute Layer   | Interaction के लिए APIs: Producer, Consumer, Connect, Streams, और ksqlDB.     |
| Storage Layer   | Brokers in clusters, topics/partitions distributed, events offsets के द्वारा ordered. |

#### Control और Data Planes
- **Control Plane**: Cluster metadata manage करता है, historically Zookeeper use करते हुए, अब KRaft module के साथ controllers selected brokers पर। इस simplification Zookeeper को eliminate करता है, configuration easier बनाता है और metadata propagation more efficient बनाता है via a special topic, blog post में noted है।
- **Data Plane**: Data replication handle करता है, एक process में followers FetchRequest issue करते हैं, leader data send करता है, और records certain offset ke पहले commit करता है, consistency ensure करता है। Partition 0 के साथ offsets 2, 3, और 4 का example highlight करता है, एक diagram के साथ [इस URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17a4454-a194-45f9-8a1f-f4882501657c_1095x1600.png) पर.

#### Record Structure और Broker Operations
Each record, event ka abstraction, में शामिल हैं:
- Timestamp: जब created हुआ था.
- Key: Ordering, colocation, और retention के लिए, partitioning के लिए crucial.
- Value: Data content.
- Headers: Optional metadata.

Key और value byte arrays हैं, serdes के साथ encoded/decoded, flexibility ensure करते हैं। Broker operations में शामिल हैं:
- Producer request socket receive buffer में landing.
- Network thread shared request queue में move.
- I/O thread CRC validate, commit log (disk segments के साथ data और index) में append.
- Requests replication के लिए purgatory में stashed.
- Response queued, network thread socket send buffer के द्वारा send.

इस process, sequential I/O के लिए optimize किया गया है, blog post में diagrams illustrate करते हैं, flow को contributing significantly Kafka की speed में.

| Record Component | Purpose                                                                 |
|------------------|-------------------------------------------------------------------------|
| Timestamp        | Records जब event created हुआ था.                                     |
| Key              | Ordering, colocation, और retention ensure करता है, partitioning के लिए.           |
| Value            | Actual data content contain करता है.                                       |
| Headers          | Optional metadata additional information के लिए.                           |

#### Performance Optimizations
Kafka की speed को enhance करने के लिए कई design decisions हैं:
- **Append-Only Logs**: File के end पर sequentially लिखना disk seek time minimize करता है, एक diary में entries add करने के समान, mid-document insert करने se तेज.
- **Zero-Copy Principle**: Data ko producer se consumer tak directly transfer करना, CPU overhead reduce करता है, एक box ko truck se warehouse tak move करना बिना unpacking, time save करता है.
- **Batch Processing**: Data ko batches में handle करना per-record overhead lower करता है, efficiency improve करता है.
- **Asynchronous Replication**: Leader broker requests serve करते hue replicas update करते hain, availability ensure करते hue performance impact ko avoid करते hain.
- **Partitioning**: Data ko partitions में distribute करना parallel processing ke लिए, throughput increase करता है, large data volumes handle करने ke key factor.

ये optimizations, blog post में explored हैं, Kafka high throughput और low latency achieve करने ke लिए, making it suitable for real-time applications.

#### Conclusion और Additional Insights
Apache Kafka की speed एक meticulously designed architecture और performance optimizations ke result है, append-only logs, zero-copy principles, batch processing, asynchronous replication, और efficient partitioning ka use karte hue। यह विश्लेषण, video par आधारित है और blog post se supplemented है, एक comprehensive view provide करता है, unexpected depth ke साथ, design choices ke intricate balance ko reveal करता है, जो Kafka ko data streaming ke leader बनata hai।

Blog post भी 7-day free trial ke लिए full archives ke लिए provide करता है, accessible [इस subscription link](https://blog.bytebytego.com/subscribe?simple=true&next=https%3A%2F%2Fblog.bytebytego.com%2Fp%2Fwhy-is-kafka-so-fast-how-does-it&utm_source=paywall-free-trial&utm_medium=web&utm_content=137028631&coupon=3920da80) पर, additional resources ke लिए interested लोगों के लिए।

इस detailed exploration complete understanding ensure करता है, video ke intent ke साथ align करता hai Kafka ke performance ke बारे में educate करना, और research और insights ke gathered sources se informed है, ensuring accuracy और depth.

#### Key Citations
- [System Design: Why is Kafka fast? YouTube video](https://www.youtube.com/watch?v=UNUz1-msbOM)
- [Why is Kafka so fast? How does it work? ByteByteGo blog post](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)
- [Kafka architecture diagram ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3690db-87b8-4165-8798-37d1d083f837_1600x1527.png)
- [Kafka replication diagram ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869cd88-3d6e-43af-8fd0-26f3737d8f1f_1600x559.png)
- [Kafka broker operations diagram ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17a4454-a194-45f9-8a1f-f4882501657c_1095x1600.png)
- [ByteByteGo newsletter subscription for Kafka post](https://blog.bytebytego.com/subscribe?simple=true&next=https%3A%2F%2Fblog.bytebytego.com%2Fp%2Fwhy-is-kafka-so-fast-how-does-it&utm_source=paywall-free-trial&utm_medium=web&utm_content=137028631&coupon=3920da80)