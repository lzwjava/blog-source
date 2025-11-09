---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: अलीपे एसडीके पीएचपी एकीकरण गाइड
translated: true
type: note
---

### पूर्वआवश्यकताएँ
PHP में Alipay SDK को एकीकृत करने के लिए, आपको चाहिए:
- एक वैध Alipay व्यापारी खाता (https://open.alipay.com पर साइन अप करें)।
- RSA कुंजी जोड़े: अपने सर्वर के लिए एक निजी कुंजी जनरेट करें और लेन-देन पर हस्ताक्षर करने के लिए सार्वजनिक कुंजी Alipay पर अपलोड करें।
- PHP 5.6+ (बेहतर सुरक्षा के लिए 7.x पसंदीदा), cURL और OpenSSL जैसे एक्सटेंशन सक्षम के साथ।
- Alipay SDK उनके आधिकारिक GitHub (जैसे, https://github.com/alipay/alipay-sdk-php) से डाउनलोड करें – ध्यान दें कि प्रदान किया गया कोड स्निपेट एक पुराने संस्करण (~2016) के लिए प्रतीत होता है; नवीनतम SDK नए APIs जैसे Alipay Trade APIs का उपयोग करता है। यदि आप लीगेसी मोबाइल सिक्योरिटी पे का उपयोग कर रहे हैं, तो यह अभी भी काम कर सकता है लेकिन अब उपयोग नहीं किया जाता।

### SDK सेटअप
1. **डाउनलोड और शामिल करें**: Alipay के डेवलपर पोर्टल या GitHub से SDK ZIP डाउनलोड करें। इसे अपनी प्रोजेक्ट डायरेक्टरी (जैसे, `vendor/alipay-sdk`) में एक्सट्रैक्ट करें।
2. **फाइलें शामिल करें**: अपनी PHP स्क्रिप्ट में, मुख्य SDK फाइल को शामिल करें, उदाहरण के लिए:
   ```php
   require_once 'path/to/alipay-sdk/AopClient.php'; // आधुनिक SDK के लिए
   ```
   आपके स्निपेट में लीगेसी संस्करण के लिए, आपको कस्टम इन्क्लूड जैसे `AopSdk.php` की आवश्यकता हो सकती है।

3. **कुंजियाँ और खाता कॉन्फ़िगर करें**:
   - OpenSSL कमांड या ऑनलाइन टूल्स का उपयोग करके RSA कुंजियाँ (2048-बिट) जनरेट करें। उदाहरण:
     ```bash
     openssl genrsa -out private_key.pem 2048
     openssl rsa -in private_key.pem -pubout -out public_key.pem
     ```
   - अपने स्निपेट में दिखाए गए अनुसार `$config` ऐरे को भरें:
     - `partner`: आपका Alipay पार्टनर ID (2088 से शुरू होने वाला 16 अंक)।
     - `private_key`: आपकी PEM-एन्कोडेड निजी कुंजी (कच्ची, हेडर जैसे -----BEGIN PRIVATE KEY----- के बिना)।
     - `alipay_public_key`: Alipay की सार्वजनिक कुंजी (अपने Alipay कंसोल से कॉपी करें)।
     - अन्य फ़ील्ड्स: SSL सत्यापन के लिए `transport` के लिए HTTPS का उपयोग करें, और `cacert.pem` (Alipay डॉक्स से डाउनलोड करें) को स्क्रिप्ट डायरेक्टरी में रखें।

### SDK आरंभ करना
एक AopClient इंस्टेंस बनाएं और कॉन्फ़िग पास करें:
```php
use Orvibo\AopSdk\AopClient; // अपने SDK संस्करण के लिए नेमस्पेस एडजस्ट करें

$aopClient = new AopClient();
$aopClient->gatewayUrl = 'https://openapi.alipay.com/gateway.do'; // प्रोडक्शन URL
$aopClient->appId = 'your_app_id'; // नए SDK में partner के बजाय appId का उपयोग करता है
$aopClient->rsaPrivateKey = $config['private_key'];
$aopClient->alipayrsaPublicKey = $config['alipay_public_key'];
$aopClient->apiVersion = '1.0';
$aopClient->signType = 'RSA2'; // आधुनिक SDK RSA2 को प्राथमिकता देता है
$aopClient->postCharset = $config['input_charset'];
$aopClient->format = 'json';
```

आपके स्निपेट में लीगेसी मोबाइल पे के लिए, आप पुरानी क्लासेज जैसे `AlipaySign` का उपयोग करेंगे।

### एक भुगतान अनुरोध बनाना
1. **अनुरोध पैरामीटर बनाएं**:
   ```php
   $request = new AlipayTradeAppPayRequest(); // या आपके SDK संस्करण के लिए इसी तरह
   $request->setBizContent("{" .
       "\"body\":\"Test transaction\"," .
       "\"subject\":\"Test Subject\"," .
       "\"out_trade_no\":\"123456789\"," .
       "\"timeout_express\":\"30m\"," .
       "\"total_amount\":\"0.01\"," .
       "\"product_code\":\"QUICK_MSECURITY_PAY\"" .
       "}");
   $request->setNotifyUrl($config['service']); // आपका नोटिफिकेशन URL
   ```

2. **अनुरोध निष्पादित करें**:
   ```php
   $response = $aopClient->sdkExecute($request);
   echo $response; // यह साइन्ड स्ट्रिंग आपके ऐप के Alipay SDK में उपयोग की जाती है
   ```

3. **आपके मोबाइल ऐप में (यदि ऐप के साथ एकीकृत कर रहे हैं)**: भुगतान पूरा करने के लिए प्रतिक्रिया को अपने ऐप के नेटिव Alipay SDK (जैसे, Android/iOS) को पास करें।

### सूचनाएँ और प्रतिक्रियाएँ संभालना
- **अतुल्यकालिक सूचनाएँ**: Alipay की सूचनाओं को सत्यापित करने के लिए `notify_url` पर एक कॉलबैक PHP स्क्रिप्ट सेटअप करें।
  ```php
  $aopClient->rsaCheckV1($_POST, $alipayPublicKey, 'RSA2'); // हस्ताक्षर सत्यापित करें
  // भुगतान स्थिति प्रोसेस करें (जैसे, डेटाबेस अपडेट करें)
  ```
- **समकालिक वापसी**: भुगतान के बाद, Alipay आपके `return_url` (यदि सेट है) पर रीडायरेक्ट करता है।

### परीक्षण और तैनाती
- परीक्षण के लिए Alipay के सैंडबॉक्स वातावरण का उपयोग करें: https://openhome.alipay.com/platform/devEnv.htm।
- सामान्य समस्याएँ: सुनिश्चित करें कि कुंजियाँ सही ढंग से फॉर्मेटेड हैं (अतिरिक्त लाइनें नहीं)। बेहतर सुरक्षा के लिए RSA2 का उपयोग करें।
- सुरक्षा युक्तियाँ: कुंजियों को सुरक्षित रूप से संग्रहीत करें (वर्जन कंट्रोल में नहीं)। छेड़छाड़ को रोकने के लिए हमेशा हस्ताक्षर सत्यापित करें।

यदि यह पुराने SDK के लिए है, तो बेहतर सुविधाओं और सुरक्षा के लिए Alipay के नवीनतम PHP SDK (जैसे, Composer के माध्यम से: `composer require alipay/openapisdk`) में अपग्रेड करने पर विचार करें। विस्तृत दस्तावेज़ के लिए, https://docs.open.alipay.com/ पर जाएँ। यदि आपको त्रुटियाँ मिलती हैं, तो समस्या निवारण के लिए अपना कोड और लॉग साझा करें।