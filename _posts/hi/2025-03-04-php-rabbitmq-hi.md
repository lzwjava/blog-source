---
audio: false
generated: true
lang: hi
layout: post
title: RabbitMQ का उपयोग PHP में
translated: true
---

### मुख्य बिंदु
- "php-amqplib/php-amqplib" संस्करण 2.6.* का उपयोग करने के लिए, इसे Composer के माध्यम से स्थापित करना आवश्यक लगता है और RabbitMQ के साथ संदेश भेजने और प्राप्त करने के लिए मूलभूत कदमों का पालन करना चाहिए।
- प्रक्रिया में एक कनेक्शन स्थापित करना, एक क्यू घोषित करना और संदेश भेजने के लिए `basic_publish` और संदेश प्राप्त करने के लिए `basic_consume` के साथ एक लूप का उपयोग करना शामिल है, जो नए संस्करणों से थोड़ा अलग हो सकता है।
- अनुसंधान से पता चलता है कि संस्करण 2.6.* के लिए, ग्रहण प्रक्रिया में एक मैनुअल लूप के साथ `wait()` की आवश्यकता होती है, जबकि नए संस्करणों में `consume()` विधि का उपयोग हो सकता है।

---

### स्थापना और सेटअप
"php-amqplib/php-amqplib" संस्करण 2.6.* के साथ शुरू करने के लिए, पहले Composer का उपयोग करके इसे स्थापित करें:

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

यदि आपकी सेटअप अलग है, तो इसे अनुकूलित करें।

### संदेश भेजना
संदेश भेजने के लिए, आवश्यक PHP फाइलों को शामिल करें और एक कनेक्शन बनाएं:

```php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

$connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
```

एक क्यू घोषित करें और अपना संदेश प्रकाशित करें:

```php
$channel->queue_declare('hello', false, false, false, false);
$msg = new AMQPMessage('Hello World!');
$channel->basic_publish($msg, '', 'hello');
echo " [x] Sent 'Hello World!'\n";
```

अंत में, कनेक्शन बंद करें:

```php
$channel->close();
$connection->close();
```

### संदेश प्राप्त करना
प्राप्त करने के लिए, समान रूप से सेटअप करें, लेकिन संदेश हैंडलिंग के लिए एक कॉलबैक परिभाषित करें:

```php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;

$connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
$channel->queue_declare('hello', false, false, false, false);

$callback = function ($msg) {
    echo ' [x] Received ', $msg->body, "\n";
};

$channel->basic_consume('hello', '', false, true, false, false, $callback);
while (count($channel->callbacks)) {
    $channel->wait();
}

$channel->close();
$connection->close();
```

संस्करण 2.6.* के लिए, ग्रहण को जारी रखने के लिए `wait()` के साथ लूप की आवश्यकता होती है, जो नए संस्करणों के साथ अपेक्षित है।

---

### सर्वेक्षण नोट: "php-amqplib/php-amqplib" संस्करण 2.6.* का विस्तृत उपयोग

इस खंड में "php-amqplib/php-amqplib" लाइब्रेरी, विशेष रूप से संस्करण 2.6.* का उपयोग करने के लिए एक व्यापक मार्गदर्शन प्रदान किया गया है, जो एक लोकप्रिय संदेश क्यू सिस्टम RabbitMQ के साथ बातचीत करने के लिए है। यह जानकारी आधिकारिक दस्तावेज़, ट्यूटोरियल और संस्करण-विशिष्ट विवरणों से ली गई है, जिससे विकसकों के लिए एक गहन समझ सुनिश्चित होती है।

#### पृष्ठभूमि और संदर्भ
"php-amqplib/php-amqplib" एक PHP लाइब्रेरी है जो RabbitMQ के साथ बातचीत करने के लिए AMQP 0.9.1 प्रोटोकॉल को लागू करता है। संस्करण 2.6.* एक पुराना रिलीज़ है, और जबकि लाइब्रेरी मार्च 2025 तक 3.x.x संस्करण तक विकसित हो गया है, इस विशेष संस्करण का उपयोग करने की समझ पुराने सिस्टमों या विशेष परियोजना आवश्यकताओं के लिए महत्वपूर्ण है। इस लाइब्रेरी को Ramūnas Dronga और Luke Bakken सहित योगदानकर्ताओं द्वारा बनाया गया है, जिसमें VMware इंजीनियरों का महत्वपूर्ण योगदान है जो RabbitMQ पर काम करते हैं ([GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib))।

RabbitMQ ट्यूटोरियल, जैसे कि आधिकारिक RabbitMQ वेबसाइट पर, उदाहरण प्रदान करते हैं जो आम तौर पर लागू होते हैं, लेकिन नए संस्करणों को दर्शाते हैं। संस्करण 2.6.* के लिए, विशेष रूप से ग्रहण प्रक्रिया में, नीचे वर्णित तदर्थ समायोजन आवश्यक हैं।

#### स्थापना प्रक्रिया
शुरू करने के लिए, Composer, PHP निर्भरता प्रबंधक का उपयोग करके लाइब्रेरी को स्थापित करें। अपने परियोजना डायरेक्टरी में निम्नलिखित कमांड चलाएं:

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

यह कमांड सुनिश्चित करता है कि लाइब्रेरी डाउनलोड और उपयोग के लिए कॉन्फ़िगर हो जाती है, Composer निर्भरताओं को प्रबंधित करता है। सुनिश्चित करें कि RabbitMQ स्थापित और चल रहा है, आम तौर पर `localhost:5672` पर पहुंच योग्य है, साथ ही डिफ़ॉल्ट क्रेडेंशियल (`guest/guest`) के साथ। उत्पादन के लिए, होस्ट, पोर्ट और क्रेडेंशियल को अनुकूलित करें, और [CloudAMQP PHP Documentation](https://www.cloudamqp.com/docs/php.html) पर प्रबंधित ब्रोकर सेटअप के लिए सलाह लीजिए।

#### संदेश भेजना: कदम-दर-कदम
संदेश भेजना एक कनेक्शन स्थापित करना और एक क्यू में प्रकाशित करना शामिल करता है। यहाँ प्रक्रिया है:

1. **आवश्यक फाइलों को शामिल करें:**
   Composer autoloader का उपयोग करें लाइब्रेरी को शामिल करने के लिए:

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   use PhpAmqpLib\Message\AMQPMessage;
   ```

2. **कनेक्शन और चैनल बनाएं:**
   RabbitMQ के साथ एक कनेक्शन को प्रारंभ करें और एक चैनल खोलें:

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

   पैरामीटर होस्ट, पोर्ट, यूजरनेम और पासवर्ड हैं, जैसे दिखाया गया है। SSL या अन्य कॉन्फ़िगरेशन के लिए, [RabbitMQ PHP Tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-php) देखें।

3. **क्यू घोषित करें और प्रकाशित करें:**
   एक क्यू को सुनिश्चित करें कि यह मौजूद है, फिर एक संदेश प्रकाशित करें:

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   $msg = new AMQPMessage('Hello World!');
   $channel->basic_publish($msg, '', 'hello');
   echo " [x] Sent 'Hello World!'\n";
   ```

   यहाँ, `queue_declare` एक क्यू 'hello' को बनाता है, डिफ़ॉल्ट सेटिंग्स के साथ (नॉन-ड्यूरेबल, नॉन-एक्सक्लूसिव, ऑटो-डिलीट)। `basic_publish` संदेश को क्यू में भेजता है।

4. **कनेक्शन बंद करें:**
   भेजने के बाद, चैनल और कनेक्शन को बंद करें संसाधनों को मुक्त करने के लिए:

   ```php
   $channel->close();
   $connection->close();
   ```

यह प्रक्रिया संस्करणों के बीच समान है, और संस्करण 2.6.* के लिए चेंजलॉग में कोई महत्वपूर्ण बदलाव नहीं दर्ज किया गया है।

#### संदेश प्राप्त करना: संस्करण-विशिष्ट विवरण
संस्करण 2.6.* में संदेश प्राप्त करना सावधानी से ध्यान देने की आवश्यकता होती है, क्योंकि ग्रहण यंत्र नए संस्करणों से अलग होता है। यहाँ विस्तृत प्रक्रिया है:

1. **आवश्यक फाइलों को शामिल करें:**
   भेजने के समान, autoloader और आवश्यक क्लासों को शामिल करें:

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   ```

2. **कनेक्शन और चैनल बनाएं:**
   कनेक्शन और चैनल को पहले की तरह स्थापित करें:

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

3. **क्यू घोषित करें:**
   क्यू को सुनिश्चित करें कि यह मौजूद है, भेजने वाले घोषणा के साथ मिलता है:

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   ```

4. **कॉलबैक परिभाषित करें:**
   प्राप्त संदेशों को हैंडल करने के लिए एक कॉलबैक फंक्शन बनाएं:

   ```php
   $callback = function ($msg) {
       echo ' [x] Received ', $msg->body, "\n";
   };
   ```

   यह फंक्शन प्रत्येक संदेश के लिए कॉल किया जाएगा, इस उदाहरण में बॉडी को प्रिंट करता है।

5. **संदेश ग्रहण करें:**
   संस्करण 2.6.* के लिए, `basic_consume` का उपयोग करें कॉलबैक को रजिस्टर करने के लिए, फिर एक लूप में प्रवेश करें ग्रहण को जारी रखने के लिए:

   ```php
   $channel->basic_consume('hello', '', false, true, false, false, $callback);
   while (count($channel->callbacks)) {
       $channel->wait();
   }
   ```

   `basic_consume` विधि क्यू नाम, कंस्यूमर टैग, नो-लोकल, नो-अक, एक्सक्लूसिव, नो-वेट और कॉलबैक के लिए पैरामीटर लेती है। लूप `wait()` के साथ ग्राहक को चलने के लिए रखता है, संदेशों की जांच करता है। यह एक महत्वपूर्ण विवरण है, क्योंकि नए संस्करणों (जैसे 3.2) में `consume()` विधि हो सकती है, जो 2.6.* में API दस्तावेज़ समीक्षा के आधार पर उपलब्ध नहीं थी।

6. **कनेक्शन बंद करें:**
   ग्रहण के बाद, संसाधनों को बंद करें:

   ```php
   $channel->close();
   $connection->close();
   ```

एक अपेक्षित विवरण संस्करण 2.6.* में मैनुअल लूप की आवश्यकता है, जो उत्पादन उपयोग के लिए अतिरिक्त त्रुटि हैंडलिंग की आवश्यकता हो सकती है, जैसे कि कनेक्शन समस्याओं के लिए अपवाद पकड़ना।

#### संस्करण-विशिष्ट विचार
संस्करण 2.6.* पुराने रिलीजों का हिस्सा है, और जबकि चेंजलॉग इसे स्पष्ट रूप से सूचीबद्ध नहीं करता, संस्करण 2.5 से 2.7 तक के आसपास के परिवर्तन में हर्टबिट समर्थन और PHP 5.3 समर्थन जैसे सुधार शामिल हैं। संस्करण 2.6.* के लिए, बड़े संदेशों के लिए, चैनल पर `setBodySizeLimit` समर्थित है, जो यादृच्छिक रूप से संदेशों को काटता है, यदि आवश्यक हो, और विवरण [GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib) में दिए गए हैं।

संस्करण 3.2 के साथ तुलना करने पर, परिवर्तन PHP 8 समर्थन और नए विधियों जैसे `consume()` शामिल हैं, लेकिन संदेश भेजने और बुनियादी ग्रहण के लिए मुख्य कार्यकर्ता समान रहता है। उपयोगकर्ताओं को परीक्षण के लिए सलाह दी जाती है, विशेष रूप से PHP संस्करणों के साथ, क्योंकि 2.6.* संभवतः PHP 5.3 से 7.x तक समर्थन करता है, चेंजलॉग प्रविष्टियों के अनुसार।

#### समस्या निपटान और सर्वोत्तम अभ्यास
- अगर भेजना विफल हो जाता है, तो RabbitMQ लॉग्स को चेक करें संसाधनों के लिए अलार्म, जैसे कि डिस्क स्पेस 50 MB से नीचे, और [RabbitMQ Configuration Guide](https://www.rabbitmq.com/configure.html#config-items) के माध्यम से सेटिंग्स को अनुकूलित करें।
- ग्रहण के लिए, सुनिश्चित करें कि ग्राहक निरंतर चल रहा है; उत्पादन में Supervisor जैसे टूल का उपयोग करें डेमोनाइज़ करने के लिए।
- क्यू सूचीबद्ध करें `rabbitmqctl list_queues` Linux पर या `rabbitmqctl.bat list_queues` Windows पर एक प्रिविलेज्ड उपयोगकर्ता के रूप में, [RabbitMQ Command Line Tools](https://www.rabbitmq.com/cli.html) के अनुसार।

#### तालिका: मुख्य विधियों के लिए संस्करण तुलना

| विधि             | संस्करण 2.6.* व्यवहार                          | संस्करण 3.2 व्यवहार                          |
|--------------------|------------------------------------------------|----------------------------------------------|
| `basic_publish`    | मानक, क्यू में प्रकाशित करता है                    | अपरिवर्तित, समान उपयोग                        |
| `basic_consume`    | ग्रहण के लिए लूप के साथ `wait()` की आवश्यकता होती है       | समान, लेकिन `consume()` विधि उपलब्ध है     |
| `setBodySizeLimit` | बड़े संदेशों के लिए समर्थित, यदि सेट किया गया है तो काटता है | समर्थित, समान कार्यकर्ता                |
| PHP समर्थन       | संभवतः 5.3 से 7.x                               | PHP 7.x और 8.x समर्थन करता है                     |

यह तालिका ग्रहण में मुख्य अंतर को उजागर करता है, जो संस्करण 2.6.* उपयोगकर्ताओं के लिए महत्वपूर्ण है।

#### निष्कर्ष
"php-amqplib/php-amqplib" संस्करण 2.6.* का उपयोग Composer स्थापना के साथ शुरू होता है, संदेश भेजने के लिए `basic_publish` और ग्रहण के लिए `basic_consume` के साथ एक मैनुअल लूप का उपयोग करता है। जबकि नए संस्करणों के समान, ग्रहण प्रक्रिया में अतिरिक्त ध्यान की आवश्यकता होती है, जिससे विकसकों को पुराने सिस्टमों के लिए परीक्षण और अनुकूलित करना आवश्यक होता है। अधिक विवरण के लिए, आधिकारिक RabbitMQ ट्यूटोरियल और GitHub रिपोजिटरी देखें।

---

### मुख्य सन्दर्भ
- [GitHub - php-amqplib/php-amqplib RabbitMQ के लिए सबसे व्यापक रूप से उपयोग की जाने वाली PHP क्लाइंट](https://github.com/php-amqplib/php-amqplib)
- [RabbitMQ ट्यूटोरियल - "Hello World!" PHP उदाहरण](https://www.rabbitmq.com/tutorials/tutorial-one-php)
- [CloudAMQP PHP Documentation CloudAMQP और PHP के साथ शुरू करें](https://www.cloudamqp.com/docs/php.html)
- [php-amqplib/php-amqplib Packagist पूर्व videlalvaro/php-amqplib](https://packagist.org/packages/php-amqplib/php-amqplib)
- [GitHub - php-amqplib/php-amqplib CHANGELOG फ़ाइल](https://github.com/php-amqplib/php-amqplib/blob/master/CHANGELOG.md)
- [RabbitMQ Configuration Guide Config items और सेटिंग्स](https://www.rabbitmq.com/configure.html#config-items)
- [RabbitMQ Command Line Tools CLI संदर्भ और उपयोग](https://www.rabbitmq.com/cli.html)