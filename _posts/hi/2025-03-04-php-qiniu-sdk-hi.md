---
audio: false
generated: true
lang: hi
layout: post
title: क्यूनियु पीएचपी एसडीके
translated: true
type: note
---

PHP में `"qiniu/php-sdk": "^7.0"` का उपयोग करने के लिए, आपको Qiniu PHP SDK को अपने प्रोजेक्ट में इंटीग्रेट करना होगा। यह SDK आपको Qiniu क्लाउड स्टोरेज सेवाओं के साथ इंटरैक्ट करने की सुविधा देता है, जैसे फाइलें अपलोड करना, बकेट प्रबंधित करना, और भी बहुत कुछ। आरंभ करने के लिए नीचे एक चरण-दर-चरण मार्गदर्शिका दी गई है:

---

### 1. Qiniu PHP SDK इंस्टॉल करें
SDK को इंस्टॉल करने का अनुशंसित तरीका कंपोज़र के माध्यम से है, जो PHP के लिए एक डिपेंडेंसी मैनेजर है। सुनिश्चित करें कि आपके सिस्टम पर कंपोज़र इंस्टॉल है।

#### चरण:
- अपना टर्मिनल खोलें और अपने प्रोजेक्ट डायरेक्टरी में नेविगेट करें।
- अपने प्रोजेक्ट में Qiniu PHP SDK (version 7.x) जोड़ने के लिए निम्नलिखित कमांड चलाएँ:
  ```bash
  composer require qiniu/php-sdk "^7.0"
  ```
- कंपोज़र SDK और इसकी डिपेंडेंसी को `vendor/` डायरेक्टरी में डाउनलोड करेगा और एक ऑटोलोड फाइल जनरेट करेगा।

यदि आपके पास कंपोज़र इंस्टॉल नहीं है, तो आप इसे [getcomposer.org](https://getcomposer.org/) से डाउनलोड कर सकते हैं।

---

### 2. अपना प्रोजेक्ट सेट अप करें
इंस्टॉलेशन के बाद, आपको SDK क्लासेस का उपयोग करने के लिए अपने PHP स्क्रिप्ट में ऑटोलोडर को शामिल करना होगा।

#### उदाहरण:
अपने प्रोजेक्ट डायरेक्टरी में एक PHP फाइल (जैसे, `index.php`) बनाएँ और सबसे ऊपर निम्नलिखित लाइन जोड़ें:
```php
require_once 'vendor/autoload.php';
```

यह सुनिश्चित करता है कि SDK क्लासेस ज़रूरत पड़ने पर स्वचालित रूप से लोड हो जाएँ।

---

### 3. प्रमाणीकरण कॉन्फ़िगर करें
Qiniu SDK का उपयोग करने के लिए, आपको अपनी Qiniu `AccessKey` और `SecretKey` की आवश्यकता होगी, जो आप अपने Qiniu अकाउंट डैशबोर्ड से प्राप्त कर सकते हैं।

#### उदाहरण:
```php
use Qiniu\Auth;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';

$auth = new Auth($accessKey, $secretKey);
```

`'YOUR_ACCESS_KEY'` और `'YOUR_SECRET_KEY'` को अपने वास्तविक क्रेडेंशियल्स से बदलें।

---

### 4. बेसिक उपयोग: एक फाइल अपलोड करना
Qiniu SDK के साथ सबसे आम कार्यों में से एक बकेट में फाइलें अपलोड करना है। यहाँ एक स्थानीय फाइल अपलोड करने का तरीका बताया गया है।

#### उदाहरण:
```php
use Qiniu\Storage\UploadManager;

$bucket = 'YOUR_BUCKET_NAME'; // अपने Qiniu बकेट के नाम से बदलें
$filePath = '/path/to/your/file.txt'; // उस फाइल का पथ जिसे आप अपलोड करना चाहते हैं
$key = 'file.txt'; // Qiniu स्टोरेज में फाइल का नाम (मूल फाइलनाम का उपयोग करने के लिए null भी हो सकता है)

$token = $auth->uploadToken($bucket); // एक अपलोड टोकन जनरेट करें
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "Upload failed: " . $error->message();
} else {
    echo "Upload successful! File hash: " . $ret['hash'];
}
```

- `$bucket`: आपके Qiniu बकेट का नाम।
- `$filePath`: उस फाइल का स्थानीय पथ जिसे आप अपलोड करना चाहते हैं।
- `$key`: फाइल की (नाम) जिसके तहत इसे Qiniu में संग्रहीत किया जाएगा। यदि `null` सेट किया जाता है, तो Qiniu फाइल के हैश के आधार पर एक की जनरेट करेगा।
- `$token`: आपके क्रेडेंशियल्स और बकेट नाम का उपयोग करके जनरेट किया गया एक अपलोड टोकन।
- `putFile` मेथड एक ऐरे रिटर्न करती है: `$ret` (सफलता की जानकारी) और `$error` (त्रुटि की जानकारी, यदि कोई हो)।

---

### 5. अतिरिक्त सुविधाएँ
Qiniu PHP SDK कई अन्य कार्यक्षमताएँ प्रदान करता है, जैसे:
- **बकेट प्रबंधन**: फाइलों को सूचीबद्ध करने, फाइलें हटाने, या बकेट सेटिंग्स प्रबंधित करने के लिए `Qiniu\Storage\BucketManager` का उपयोग करें।
- **फाइल ऑपरेशन**: अपने बकेट में फाइलों को कॉपी करना, मूव करना या हटाना।
- **इमेज प्रोसेसिंग**: रीसाइज़ या फॉर्मेट की गई इमेज के लिए URL जनरेट करना।

#### उदाहरण: एक बकेट में फाइलों की सूची बनाना
```php
use Qiniu\Storage\BucketManager;

$bucketMgr = new BucketManager($auth);
list($ret, $error) = $bucketMgr->listFiles($bucket);

if ($error !== null) {
    echo "Error: " . $error->message();
} else {
    echo "Files in bucket:\n";
    foreach ($ret['items'] as $item) {
        echo $item['key'] . "\n";
    }
}
```

---

### 6. एरर हैंडलिंग
SDK ऑपरेशन के बाद हमेशा `$error` वेरिएबल की जाँच करें। यदि कोई ऑपरेशन विफल होता है, तो `$error` में विफलता का विवरण होगा।

#### उदाहरण:
```php
if ($error !== null) {
    var_dump($error);
} else {
    var_dump($ret);
}
```

---

### 7. आवश्यकताएँ
- PHP वर्जन: SDK वर्जन `^7.0`, PHP 5.3.3 और उच्चतर (बाद के रिलीज़ में PHP 8.x तक) को सपोर्ट करता है।
- एक्सटेंशन: सुनिश्चित करें कि `cURL` और `xml` PHP एक्सटेंशन सक्षम हैं, क्योंकि SDK के लिए इनकी आवश्यकता होती है।

आप अपना PHP वर्जन और एक्सटेंशन इसके साथ चेक कर सकते हैं:
```bash
php -v
php -m
```

---

### 8. आगे कहाँ जाएँ
- **डॉक्यूमेंटेशन**: अधिक विवरण के लिए, [आधिकारिक Qiniu PHP SDK डॉक्यूमेंटेशन](https://developer.qiniu.com/kodo/sdk/php) या [GitHub रिपॉजिटरी](https://github.com/qiniu/php-sdk) देखें।
- **उदाहरण**: अधिक उपयोग के मामलों के लिए GitHub रेपो में `examples/` डायरेक्टरी देखें।
- **सपोर्ट**: यदि आपको कोई समस्या आती है, तो Qiniu सपोर्ट (<support@qiniu.com>) को एक टिकट सबमिट करें या उनके कम्युनिटी फोरम में पूछें।

---

### पूर्ण उदाहरण कोड
यहाँ एक फाइल अपलोड करने के लिए एक संपूर्ण स्क्रिप्ट दी गई है:
```php
<?php
require_once 'vendor/autoload.php';

use Qiniu\Auth;
use Qiniu\Storage\UploadManager;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';
$bucket = 'YOUR_BUCKET_NAME';
$filePath = '/path/to/your/file.txt';
$key = 'file.txt';

$auth = new Auth($accessKey, $secretKey);
$token = $auth->uploadToken($bucket);
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "Upload failed: " . $error->message();
} else {
    echo "Upload successful! File hash: " . $ret['hash'];
}
```

प्लेसहोल्डर वैल्यूज़ (`YOUR_ACCESS_KEY`, `YOUR_SECRET_KEY`, `YOUR_BUCKET_NAME`, `/path/to/your/file.txt`) को अपने वास्तविक डेटा से बदलें, और आप तैयार हैं!

यदि आपको किसी विशिष्ट सुविधा के साथ सहायता की आवश्यकता है तो मुझे बताएं!