---
audio: false
generated: true
lang: hi
layout: post
title: पीएचपी में रैबिटएमक्यू का उपयोग
translated: true
type: note
---

### मुख्य बिंदु
- ऐसा प्रतीत होता है कि "php-amqplib/php-amqplib" संस्करण 2.6.* का उपयोग करने के लिए, आपको इसे Composer के माध्यम से इंस्टॉल करना होगा और RabbitMQ के साथ संदेश भेजने और प्राप्त करने के बुनियादी चरणों का पालन करना होगा।
- इस प्रक्रिया में एक कनेक्शन स्थापित करना, एक कतार घोषित करना और भेजने के लिए `basic_publish` तथा प्राप्त करने के लिए लूप के साथ `basic_consume` जैसे तरीकों का उपयोग करना शामिल है, जो नए संस्करणों से थोड़ा भिन्न हो सकता है।
- शोध से पता चलता है कि संस्करण 2.6.* के लिए, उपभोग करने की प्रक्रिया के लिए `wait()` के साथ एक मैन्युअल लूप की आवश्यकता होती है, नए संस्करणों के विपरीत जो `consume()` विधि का उपयोग कर सकते हैं।

---

### इंस्टॉलेशन और सेटअप
"php-amqplib/php-amqplib" संस्करण 2.6.* के साथ शुरुआत करने के लिए, पहले इसे Composer का उपयोग करके इंस्टॉल करें:

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

सुनिश्चित करें कि RabbitMQ आपके सिस्टम पर इंस्टॉल और चल रहा है, जो आमतौर पर डिफ़ॉल्ट क्रेडेंशियल (`guest/guest`) के साथ `localhost:5672` पर पहुँच योग्य होता है। यदि आपका सेटअप भिन्न है तो इन सेटिंग्स को समायोजित करें।

### संदेश भेजना
एक संदेश भेजने के लिए, आवश्यक PHP फ़ाइलों को शामिल करें और एक कनेक्शन बनाएँ:

```php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

$connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
```

एक कतार घोषित करें और अपना संदेश प्रकाशित करें:

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
प्राप्त करने के लिए, इसी तरह सेटअप करें लेकिन संदेश हैंडलिंग के लिए एक कॉलबैक परिभाषित करें:

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

ध्यान दें कि संस्करण 2.6.* के लिए, उपभोग जारी रखने के लिए आपको `wait()` के साथ लूप की आवश्यकता होती है, जो नए संस्करणों की तुलना में एक अप्रत्याशित विवरण है जो एक सरल `consume()` विधि का उपयोग कर सकते हैं।

---

### सर्वे नोट: "php-amqplib/php-amqplib" संस्करण 2.6.* का विस्तृत उपयोग

यह खंड RabbitMQ, एक लोकप्रिय संदेश कतार प्रणाली, के साथ इंटरैक्ट करने के लिए "php-amqplib/php-amqplib" लाइब्रेरी, विशेष रूप से संस्करण 2.6.* के उपयोग पर एक व्यापक मार्गदर्शिका प्रदान करता है। जानकारी आधिकारिक दस्तावेज़ीकरण, ट्यूटोरियल और संस्करण-विशिष्ट विवरणों से प्राप्त की गई है, जो डेवलपर्स के लिए एक संपूर्ण समझ सुनिश्चित करती है।

#### पृष्ठभूमि और संदर्भ
"php-amqplib/php-amqplib" RabbitMQ के साथ संचार के लिए एक PHP लाइब्रेरी है, जो AMQP 0.9.1 प्रोटोकॉल को लागू करती है। संस्करण 2.6.* एक पुराना रिलीज़ है, और जबकि मार्च 2025 तक लाइब्रेरी संस्करण 3.x.x तक विकसित हो चुकी है, इस विशिष्ट संस्करण में इसके उपयोग को समझना लीगेसी सिस्टम या विशिष्ट परियोजना आवश्यकताओं के लिए महत्वपूर्ण है। लाइब्रेरी को Ramūnas Dronga और Luke Bakken सहित योगदानकर्ताओं द्वारा बनाए रखा जाता है, जिसमें RabbitMQ पर काम कर रहे VMware इंजीनियरों की महत्वपूर्ण भागीदारी है ([GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib))।

RabbitMQ ट्यूटोरियल, जैसे कि आधिकारिक RabbitMQ वेबसाइट पर, उदाहरण प्रदान करते हैं जो आम तौर पर लागू होते हैं लेकिन नए संस्करणों को प्रतिबिंबित कर सकते हैं। संस्करण 2.6.* के लिए, समायोजन आवश्यक हैं, विशेष रूप से उपभोग करने की प्रक्रिया में, जैसा कि नीचे विस्तृत है।

#### इंस्टॉलेशन प्रक्रिया
शुरुआत करने के लिए, Composer, PHP डिपेंडेंसी मैनेजर का उपयोग करके लाइब्रेरी को इंस्टॉल करें। अपनी प्रोजेक्ट डायरेक्टरी में निम्नलिखित कमांड चलाएँ:

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

यह कमांड सुनिश्चित करती है कि लाइब्रेरी डाउनलोड और उपयोग के लिए कॉन्फ़िगर की गई है, साथ ही Composer डिपेंडेंसीज़ को प्रबंधित करता है। सुनिश्चित करें कि RabbitMQ इंस्टॉल और चल रहा है, जो आमतौर पर डिफ़ॉल्ट क्रेडेंशियल (`guest/guest`) के साथ `localhost:5672` पर पहुँच योग्य होता है। प्रोडक्शन के लिए, होस्ट, पोर्ट और क्रेडेंशियल को आवश्यकतानुसार समायोजित करें, और प्रबंधित ब्रोकर सेटअप के लिए [CloudAMQP PHP Documentation](https://www.cloudamqp.com/docs/php.html) से परामर्श लें।

#### संदेश भेजना: चरण-दर-चरण
संदेश भेजने में एक कनेक्शन स्थापित करना और एक कतार पर प्रकाशित करना शामिल है। प्रक्रिया इस प्रकार है:

1. **आवश्यक फ़ाइलें शामिल करें:**
   लाइब्रेरी को शामिल करने के लिए Composer ऑटोलोडर का उपयोग करें:

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   use PhpAmqpLib\Message\AMQPMessage;
   ```

2. **कनेक्शन और चैनल बनाएँ:**
   RabbitMQ से कनेक्शन प्रारंभ करें और एक चैनल खोलें:

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

   पैरामीटर होस्ट, पोर्ट, उपयोगकर्ता नाम और पासवर्ड हैं, जैसा कि दिखाया गया है। SSL या अन्य कॉन्फ़िगरेशन के लिए, [RabbitMQ PHP Tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-php) देखें।

3. **कतार घोषित करें और प्रकाशित करें:**
   यह सुनिश्चित करने के लिए एक कतार घोषित करें कि यह मौजूद है, फिर एक संदेश प्रकाशित करें:

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   $msg = new AMQPMessage('Hello World!');
   $channel->basic_publish($msg, '', 'hello');
   echo " [x] Sent 'Hello World!'\n";
   ```

   यहाँ, `queue_declare` डिफ़ॉल्ट सेटिंग्स (गैर-टिकाऊ, गैर-विशिष्ट, ऑटो-डिलीट) के साथ 'hello' नामक एक कतार बनाता है। `basic_publish` संदेश को कतार पर भेजता है।

4. **कनेक्शन बंद करें:**
   भेजने के बाद, संसाधनों को मुक्त करने के लिए चैनल और कनेक्शन बंद करें:

   ```php
   $channel->close();
   $connection->close();
   ```

यह प्रक्रिया संस्करणों में मानक है, और संस्करण 2.6.* के लिए बाद के रिलीज़ की तुलना में चेंजलॉग में कोई महत्वपूर्ण परिवर्तन नहीं दर्ज किया गया है।

#### संदेश प्राप्त करना: संस्करण-विशिष्ट विवरण
संस्करण 2.6.* में संदेश प्राप्त करने के लिए सावधानीपूर्वक ध्यान देने की आवश्यकता होती है, क्योंकि उपभोग करने का तंत्र नए संस्करणों से भिन्न होता है। विस्तृत प्रक्रिया इस प्रकार है:

1. **आवश्यक फ़ाइलें शामिल करें:**
   भेजने के समान, ऑटोलोडर और आवश्यक कक्षाओं को शामिल करें:

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   ```

2. **कनेक्शन और चैनल बनाएँ:**
   पहले की तरह कनेक्शन और चैनल स्थापित करें:

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

3. **कतार घोषित करें:**
   कतार के अस्तित्व में होने की पुष्टि करें, भेजने वाले की घोषणा से मेल खाते हुए:

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   ```

4. **कॉलबैक परिभाषित करें:**
   प्राप्त संदेशों को संभालने के लिए एक कॉलबैक फ़ंक्शन बनाएँ:

   ```php
   $callback = function ($msg) {
       echo ' [x] Received ', $msg->body, "\n";
   };
   ```

   यह फ़ंक्शन प्रत्येक संदेश के लिए कॉल किया जाएगा, इस उदाहरण में बॉडी प्रिंट करेगा।

5. **संदेशों का उपभोग करें:**
   संस्करण 2.6.* के लिए, कॉलबैक को पंजीकृत करने के लिए `basic_consume` का उपयोग करें, फिर उपभोग जारी रखने के लिए एक लूप में प्रवेश करें:

   ```php
   $channel->basic_consume('hello', '', false, true, false, false, $callback);
   while (count($channel->callbacks)) {
       $channel->wait();
   }
   ```

   `basic_consume` विधि कतार नाम, उपभोक्ता टैग, नो-लोकल, नो-एक, विशिष्ट, नो-वेट और कॉलबैक के लिए पैरामीटर लेती है। `wait()` के साथ लूप उपभोक्ता को चलाए रखता है, संदेशों की जाँच करता है। यह एक महत्वपूर्ण विवरण है, क्योंकि नए संस्करण (जैसे, 3.2) `consume()` विधि का उपयोग कर सकते हैं, जो API दस्तावेज़ीकरण समीक्षा के आधार पर 2.6.* में उपलब्ध नहीं थी।

6. **कनेक्शन बंद करें:**
   उपभोग करने के बाद, संसाधनों को बंद करें:

   ```php
   $channel->close();
   $connection->close();
   ```

एक अप्रत्याशित विवरण संस्करण 2.6.* में मैन्युअल लूप की आवश्यकता है, जिसके लिए उत्पादन उपयोग में कनेक्शन समस्याओं के लिए अपवादों को पकड़ने जैसे अतिरिक्त त्रुटि हैंडलिंग की आवश्यकता हो सकती है।

#### संस्करण-विशिष्ट विचार
संस्करण 2.6.* पुराने रिलीज़ का हिस्सा है, और जबकि चेंजलॉग स्पष्ट रूप से इसे सूचीबद्ध नहीं करता है, 2.5 से 2.7 के आसपास के संस्करण हार्टबीट सपोर्ट और PHP 5.3 संगतता जैसे उन्नयन दिखाते हैं। बड़े संदेशों के लिए, संस्करण 2.6.* मेमोरी सीमा को संभालने के लिए चैनल पर `setBodySizeLimit` का समर्थन करता है, आवश्यकता पड़ने पर संदेशों को छोटा करता है, जिसका विवरण [GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib) में है।

संस्करण 3.2 से तुलना करने पर, परिवर्तनों में PHP 8 सपोर्ट और `consume()` जैसी नई विधियाँ शामिल हैं, लेकिन भेजने और बुनियादी उपभोग के लिए मुख्य कार्यक्षमता समान रहती है। उपयोगकर्ताओं को संगतता के लिए परीक्षण करना चाहिए, विशेष रूप से PHP संस्करणों के साथ, क्योंकि चेंजलॉग प्रविष्टियों के अनुसार 2.6.* संभवतः PHP 5.3 से 7.x का समर्थन करता है।

#### समस्या निवारण और सर्वोत्तम अभ्यास
- यदि भेजने में विफल होता है, तो डिस्क स्थान 50 MB से कम जैसे संसाधन अलार्म के लिए RabbitMQ लॉग्स की जाँच करें, और [RabbitMQ Configuration Guide](https://www.rabbitmq.com/configure.html#config-items) के माध्यम से सेटिंग्स समायोजित करें।
- उपभोग के लिए, सुनिश्चित करें कि उपभोक्ता लगातार चलता रहे; उत्पादन में डीमनाइज़ करने के लिए Supervisor जैसे टूल्स का उपयोग करें।
- Linux पर `rabbitmqctl list_queues` या Windows पर `rabbitmqctl.bat list_queues` का उपयोग करके कतारों को सूचीबद्ध करें, जैसा कि [RabbitMQ Command Line Tools](https://www.rabbitmq.com/cli.html) के अनुसार एक विशेषाधिकार प्राप्त उपयोगकर्ता के रूप में।

#### तालिका: प्रमुख विधियों के लिए संस्करण तुलना

| विधि               | संस्करण 2.6.* व्यवहार                          | संस्करण 3.2 व्यवहार                          |
|--------------------|------------------------------------------------|----------------------------------------------|
| `basic_publish`    | मानक, कतार पर प्रकाशित करता है                 | अपरिवर्तित, समान उपयोग                      |
| `basic_consume`    | उपभोग के लिए `wait()` के साथ लूप की आवश्यकता   | समान, लेकिन `consume()` विधि उपलब्ध         |
| `setBodySizeLimit` | बड़े संदेशों के लिए समर्थित, सेट होने पर छोटा करता है | समर्थित, समान कार्यक्षमता                  |
| PHP संगतता        | संभवतः 5.3 से 7.x                              | PHP 7.x और 8.x का समर्थन करता है            |

यह तालिका उपभोग में मुख्य अंतर को उजागर करती है, जो संस्करण 2.6.* उपयोगकर्ताओं के लिए महत्वपूर्ण है।

#### निष्कर्ष
"php-amqplib/php-amqplib" संस्करण 2.6.* का उपयोग करने में मानक Composer इंस्टॉलेशन शामिल है, जिसमें `basic_publish` के माध्यम से संदेश भेजना और `basic_consume` के साथ एक मैन्युअल लूप के माध्यम से प्राप्त करना शामिल है। जबकि यह नए संस्करणों के समान है, उपभोग करने की प्रक्रिया के लिए अतिरिक्त ध्यान देने की आवश्यकता होती है, जिससे डेवलपर्स के लिए लीगेसी सिस्टम के लिए परीक्षण और समायोजन करना आवश्यक हो जाता है। अधिक जानकारी के लिए, आधिकारिक RabbitMQ ट्यूटोरियल और GitHub रिपॉजिटरी से परामर्श लें।

---

### प्रमुख उद्धरण
- [GitHub - php-amqplib/php-amqplib The most widely used PHP client for RabbitMQ](https://github.com/php-amqplib/php-amqplib)
- [RabbitMQ tutorial - "Hello World!" PHP example](https://www.rabbitmq.com/tutorials/tutorial-one-php)
- [CloudAMQP PHP Documentation Get started with CloudAMQP and PHP](https://www.cloudamqp.com/docs/php.html)
- [php-amqplib/php-amqplib Packagist Formerly videlalvaro/php-amqplib](https://packagist.org/packages/php-amqplib/php-amqplib)
- [GitHub - php-amqplib/php-amqplib CHANGELOG file](https://github.com/php-amqplib/php-amqplib/blob/master/CHANGELOG.md)
- [RabbitMQ Configuration Guide Config items and settings](https://www.rabbitmq.com/configure.html#config-items)
- [RabbitMQ Command Line Tools CLI reference and usage](https://www.rabbitmq.com/cli.html)