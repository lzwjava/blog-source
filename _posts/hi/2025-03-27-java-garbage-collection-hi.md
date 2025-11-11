---
audio: false
generated: true
lang: hi
layout: post
title: जावा में कचरा संग्रह
translated: true
type: note
---

ठीक है, आइए Java में Garbage Collection (GC) के बारे में सीखते हैं! यह Java के memory management का एक महत्वपूर्ण पहलू है जो डेवलपर्स को manual memory allocation और deallocation से बचने में मदद करता है।

**Java में Garbage Collection क्या है?**

Garbage Collection एक स्वचालित प्रक्रिया है जो उन objects द्वारा घेरी गई memory को वापस प्राप्त करती है जो अब Java एप्लिकेशन द्वारा उपयोग में नहीं हैं। संक्षेप में, यह Java का नए objects के लिए जगह बनाने हेतु "कचरे" (अनुपयोगी objects) की सफाई करने का तरीका है।

**Garbage Collection की आवश्यकता क्यों है?**

कई अन्य प्रोग्रामिंग भाषाओं (जैसे C या C++) में, डेवलपर्स `malloc` और `free` जैसे functions का उपयोग करके स्मृति को स्पष्ट रूप से allocate और deallocate करने के लिए जिम्मेदार होते हैं। यह manual memory management कई समस्याएं पैदा कर सकता है:

* **Memory Leaks:** यदि memory allocate की गई है लेकिन कभी मुक्त नहीं की जाती है, तो एप्लिकेशन अंततः memory खत्म होने के कारण क्रैश हो सकता है।
* **Dangling Pointers:** यदि memory मुक्त कर दी जाती है लेकिन एक pointer अभी भी उस memory location को refer करता है, तो उस pointer का उपयोग अप्रत्याशित व्यवहार या क्रैश का कारण बन सकता है।
* **बढ़ी हुई Development Complexity:** मैन्युअल रूप से memory प्रबंधित करना सॉफ्टवेयर डेवलपमेंट में जटिलता की एक महत्वपूर्ण परत जोड़ता है।

Java की Garbage Collection इस प्रक्रिया को स्वचालित करती है, जिससे डेवलपर्स manual memory management के बोझ से मुक्त हो जाते हैं और सुरक्षित तथा अधिक विश्वसनीय कोड लिखना आसान हो जाता है।

**Garbage Collection कैसे काम करती है?**

Garbage collection के पीछे मूल विचार यह पहचानना है कि memory में कौन से objects अभी भी एप्लिकेशन द्वारा उपयोग किए जा रहे हैं और कौन से नहीं। garbage collector फिर अनुपयोगी objects द्वारा घेरी गई memory को वापस ले लेता है।

यहां प्रक्रिया का एक सरल अवलोकन दिया गया है:

1.  **Live Objects की पहचान (Marking):** Garbage collector उन objects के समूह की पहचान करके शुरू करता है जो अभी भी "root" objects से पहुंच योग्य हैं। Root objects आमतौर पर वे objects होते हैं जो एप्लिकेशन द्वारा सीधे पहुंच योग्य होते हैं, जैसे:
    * वर्तमान में निष्पादित हो रही methods में local variables।
    * Static variables।
    * Native code द्वारा referenced objects।
    * Java Virtual Machine (JVM) के active threads।

    Garbage collector इन roots से object graph को पार करता है, उन सभी objects को चिह्नित (mark) करता है जो पहुंच योग्य हैं।

2.  **Memory की वसूली (Sweeping और Compacting):** एक बार live objects चिह्नित हो जाने के बाद, garbage collector को unmarked (अनपहुंच योग्य) objects द्वारा घेरी गई memory को वापस लेना होता है। विभिन्न garbage collection algorithms इसके लिए अलग-अलग रणनीतियों का उपयोग करती हैं:

    * **Mark and Sweep:** यह algorithm live objects की पहचान करता है और उन्हें चिह्नित करता है, फिर memory के माध्यम से sweep करता है, unmarked objects द्वारा घेरे गए स्थान को मुक्त करता है। इससे memory fragmentation (मेमोरी का टुकड़ों में बंट जाना) हो सकता है।
    * **Mark and Compact:** यह algorithm भी live objects को चिह्नित करता है। चिह्नित करने के बाद, यह live objects को memory में एक साथ ले जाता है (compact करता है), जिससे fragmentation समाप्त हो जाती है और नए objects के लिए सन्निकट memory blocks allocate करना आसान हो जाता है।
    * **Copying:** यह algorithm memory को दो या अधिक regions में विभाजित करता है। Live objects को एक region से दूसरी region में कॉपी किया जाता है, जिससे मूल region में स्थान प्रभावी रूप से वापस मिल जाता है।

**Java Garbage Collection में मुख्य अवधारणाएं:**

* **Heap:** memory का वह क्षेत्र जहां Java में objects allocate किए जाते हैं। Garbage collector मुख्य रूप से heap पर काम करता है।
* **Young Generation (Nursery):** यह heap का एक हिस्सा है जहां नए बनाए गए objects शुरू में allocate किए जाते हैं। इसे आगे विभाजित किया गया है:
    * **Eden Space:** जहां अधिकांश नए objects बनाए जाते हैं।
    * **Survivor Spaces (S0 और S1):** उन objects को रखने के लिए उपयोग किया जाता है जो कुछ minor garbage collection cycles से बच गए हैं।
* **Old Generation (Tenured Generation):** वे objects जो young generation में कई garbage collection cycles से बच गए हैं, अंततः old generation में स्थानांतरित कर दिए जाते हैं। Old generation में objects आम तौर पर लंबे समय तक जीवित रहने वाले होते हैं।
* **Permanent Generation (PermGen) / Metaspace:** Java के पुराने संस्करणों (Java 8 से पहले) में, Permanent Generation classes और methods के metadata को संग्रहीत करता था। Java 8 और बाद के संस्करणों में, इसे Metaspace द्वारा प्रतिस्थापित किया गया है, जो native memory का हिस्सा है (Java heap नहीं)।
* **Garbage Collection Algorithms:** Garbage collection के लिए विभिन्न algorithms का उपयोग किया जाता है, जिनमें से प्रत्येक के performance और efficiency के मामले में अपने-अपने trade-offs होते हैं।

**Generational Garbage Collection:**

Java HotSpot JVM (सबसे आम JVM) garbage collection के लिए एक generational approach का उपयोग करता है। यह इस अवलोकन पर आधारित है कि किसी एप्लिकेशन में अधिकांश objects का जीवनकाल छोटा होता है।

1.  **Minor GC (Young Generation GC):** जब Eden space भर जाता है, तो एक minor GC trigger होती है। Eden और एक Survivor space (मान लीजिए, S0) के live objects को दूसरे Survivor space (S1) में कॉपी किया जाता है। वे objects जो एक निश्चित संख्या में minor GC cycles से बच गए हैं, उन्हें old generation में स्थानांतरित कर दिया जाता है। अनपहुंच योग्य objects को discard कर दिया जाता है।

2.  **Major GC (Old Generation GC) / Full GC:** जब old generation भर जाता है, तो एक major GC (या कभी-कभी एक full GC, जिसमें young और old दोनों generations शामिल हो सकते हैं) performed की जाती है। यह प्रक्रिया आम तौर पर minor GC की तुलना में अधिक time-consuming होती है और एप्लिकेशन के निष्पादन में लंबे pauses का कारण बन सकती है।

**Java HotSpot JVM में सामान्य Garbage Collectors:**

Java HotSpot JVM कई garbage collection algorithms प्रदान करता है जिन्हें एप्लिकेशन की आवश्यकताओं (जैसे, low latency, high throughput) के आधार पर चुना जा सकता है। कुछ सामान्य ones में शामिल हैं:

* **Serial Collector:** Garbage collection के लिए एक single thread का उपयोग करता है। सीमित संसाधनों वाले छोटे applications के लिए उपयुक्त।
* **Parallel Collector:** Garbage collection के लिए multiple threads का उपयोग करता है, जिससे throughput में सुधार होता है। multi-core processors पर चलने वाले मध्यम से बड़े डेटा सेट वाले applications के लिए उपयुक्त।
* **CMS (Concurrent Mark Sweep) Collector:** एप्लिकेशन threads के साथ concurrent रूप से garbage collection के अधिकांश कार्य को performed करके pause times को कम करने का प्रयास करता है। हालाँकि, यह fragmentation का कारण बन सकता है और अंततः एक full GC की आवश्यकता हो सकती है।
* **G1 (Garbage-First) Collector:** throughput और low latency के बीच एक अच्छा संतुलन प्रदान करने का लक्ष्य रखता है। यह heap को regions में विभाजित करता है और सबसे अधिक garbage वाले regions से garbage collect करने को प्राथमिकता देता है। यह Java 9 और बाद के संस्करणों में default collector है।
* **ZGC (Z Garbage Collector):** बड़े heaps के लिए डिज़ाइन किया गया एक low-latency garbage collector। इसका लक्ष्य 10ms से कम का pause time है।
* **Shenandoah:** ZGC के समान लक्ष्यों वाला एक और low-latency garbage collector।

आप JVM command-line options के माध्यम से निर्दिष्ट कर सकते हैं कि किस garbage collector का उपयोग करना है।

**Garbage Collection कब चलती है?**

Garbage collection ज्यादातर JVM द्वारा संचालित एक स्वचालित प्रक्रिया है। यह आम तौर पर तब चलती है जब:

* Young generation (Eden space) भर जाता है।
* Old generation भर जाता है।
* सिस्टम में memory कम होती है।

हालांकि आप सीधे नियंत्रित नहीं कर सकते कि garbage collection *कब* चलेगी, आप `System.gc()` का उपयोग करके JVM को यह सुझाव दे सकते हैं कि garbage collection performed करने का यह एक अच्छा समय हो सकता है। हालाँकि, इस बात की कोई गारंटी नहीं है कि JVM वास्तव में garbage collector को तुरंत चलाएगा या जब आप इस method को call करेंगे। आम तौर पर JVM की स्वचालित garbage collection mechanism पर भरोसा करना बेहतर होता है।

**`System.gc()` और Finalization:**

* **`System.gc()`:** जैसा कि बताया गया है, यह garbage collector को चलाने का JVM के लिए एक निवेदन है। अक्सर महत्वपूर्ण memory management के लिए इस method पर भरोसा न करने की सलाह दी जाती है, क्योंकि आमतौर पर GC कब performed करना है, यह तय करने में JVM बेहतर होता है।
* **`finalize()` Method:** किसी object के garbage collected होने से पहले, JVM उसे कोई cleanup operations performed करने का मौका देता है by calling its `finalize()` method (यदि इसे implemented किया गया है)। हालाँकि, `finalize()` में कई कमियां हैं और आधुनिक Java development में इसे generally हतोत्साहित किया जाता है। यह performance issues पैदा कर सकता है और garbage collection को कम predictable बना सकता है। Resource management के लिए try-with-resources जैसे अन्य mechanisms का उपयोग करने पर विचार करें।

**एप्लिकेशन Performance पर Garbage Collection का प्रभाव:**

हालांकि garbage collection memory management के लिए आवश्यक है, यह "stop-the-world" pauses के कारण एप्लिकेशन के performance को भी प्रभावित कर सकती है। इन pauses के दौरान, जब garbage collector अपना काम performed करता है तो सभी एप्लिकेशन threads रुक जाती हैं। इन pauses की अवधि और आवृत्ति उपयोग की जा रही garbage collection algorithm और heap के आकार और विशेषताओं पर निर्भर करती है।

G1, ZGC, और Shenandoah जैसे low-latency garbage collectors एप्लिकेशन को अधिक responsive बनाने के लिए इन pause times को कम करने का लक्ष्य रखते हैं।

**Garbage Collection Tuning:**

विशिष्ट performance आवश्यकताओं वाले applications के लिए, JVM parameters को समायोजित करके garbage collection को tuned किया जा सकता है, जैसे:

* Heap size (`-Xms`, `-Xmx`)
* Young generation size (`-Xmn`)
* Survivor ratios (`-XX:SurvivorRatio`)
* किसी विशिष्ट garbage collector को चुनना (`-XX:+UseG1GC`, `-XX:+UseZGC`, आदि)
* अधिक fine-grained control के लिए garbage collection flags सेट करना।

GC tuning एक उन्नत विषय है और आमतौर पर एप्लिकेशन के व्यवहार और performance के सावधानीपूर्वक विश्लेषण की आवश्यकता होती है।

**Garbage Collector-Friendly कोड लिखने के लिए Best Practices:**

हालांकि Java memory management को स्वचालित रूप से संभालता है, garbage collector को ध्यान में रखकर कोड लिखने से बेहतर performance प्राप्त हो सकती है:

* **Object Creation को कम से कम करें:** बड़ी संख्या में अल्पकालिक objects बनाने पर garbage collector पर दबाव पड़ सकता है। उचित होने पर objects को पुन: उपयोग करने का प्रयास करें।
* **Object References जारी करें:** यदि आपके पास किसी object का reference है जिसकी आपको अब आवश्यकता नहीं है, तो reference को `null` पर सेट कर दें। इससे object garbage collection के लिए जल्दी पात्र हो जाता है।
* **Data Structures का बुद्धिमानी से उपयोग करें:** ऐसे data structures चुनें जो आपकी आवश्यकताओं के लिए उपयुक्त हों। उदाहरण के लिए, एक बड़े `ArrayList` का उपयोग करना और फिर उसके अधिकांश elements को discard करना inefficient हो सकता है।
* **Finalizers से बचें:** जैसा कि पहले बताया गया है, resource cleanup के लिए `finalize()` method पर भरोसा करने से बचें। Files और network connections जैसे resources के लिए try-with-resources का उपयोग करें।
* **Static Variables के प्रति सचेत रहें:** Static variables द्वारा referenced objects एप्लिकेशन की पूरी अवधि तक जीवित रहेंगे, इसलिए बड़ी या अनावश्यक objects को static fields में संग्रहीत करने के बारे में सावधान रहें।

**संक्षेप में:**

Java में Garbage Collection एक स्वचालित memory management प्रक्रिया है जो अनुपयोगी objects द्वारा घेरी गई memory को वापस प्राप्त करती है। यह डेवलपर्स को manual memory management से मुक्त करके development को सरल बनाती है। यह समझना कि यह कैसे काम करती है, heap की different generations, और उपलब्ध garbage collection algorithms आपको अधिक efficient और performant Java applications लिखने में मदद कर सकते हैं।