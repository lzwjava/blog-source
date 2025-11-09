---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: دليل دمج Alipay SDK في PHP
translated: true
type: note
---

### المتطلبات الأساسية
لتكامل Alipay SDK في PHP، ستحتاج إلى:
- حساب تاجر Alipay صالح (سجل في https://open.alipay.com).
- أزواج مفاتيح RSA: أنشئ مفتاحًا خاصًا لخادمك وقم برفع المفتاح العام إلى Alipay لتوقيع المعاملات.
- PHP 5.6+ (يفضل 7.x لأمان أفضل)، مع تمكين الإضافات مثل cURL و OpenSSL.
- حمل Alipay SDK من GitHub الرسمي (مثال: https://github.com/alipay/alipay-sdk-php) – لاحظ أن مقتطف الكود المقدم يبدو أنه لإصدار أقدم (~2016); أحدث SDK يستخدم واجهات برمجة تطبيقات أحدث مثل Alipay Trade APIs. إذا كنت تستخدم دفع الأمان للجوال القديم، فقد لا يزال يعمل ولكنه مهمل.

### إعداد SDK
1. **تحميل والتضمين**: حمل SDK بصيغة ZIP من بوابة مطوري Alipay أو GitHub. استخرجه إلى دليل مشروعك (مثال: `vendor/alipay-sdk`).
2. **تضمين الملفات**: في سكريبت PHP الخاص بك، قم بتضمين ملف SDK الرئيسي، مثال:
   ```php
   require_once 'path/to/alipay-sdk/AopClient.php'; // لأحدث SDK
   ```
   للإصدار القديم في مقتطفك، قد تحتاج إلى تضمينات مخصصة مثل `AopSdk.php`.

3. **تهيئة المفاتيح والحساب**:
   - أنشئ مفاتيح RSA (2048-bit) باستخدام أوامر OpenSSL أو أدوات عبر الإنترنت. مثال:
     ```bash
     openssl genrsa -out private_key.pem 2048
     openssl rsa -in private_key.pem -pubout -out public_key.pem
     ```
   - املء مصفوفة `$config` كما هو موضح في مقتطفك:
     - `partner`: معرّف الشريك Alipay الخاص بك (16 رقماً تبدأ بـ 2088).
     - `private_key`: مفتاحك الخاص المشفر PEM (خام، بدون عناوين مثل -----BEGIN PRIVATE KEY-----).
     - `alipay_public_key`: المفتاح العام لـ Alipay (انسخه من وحدة تحكم Alipay الخاصة بك).
     - حقول أخرى: استخدم HTTPS لـ `transport`، وضِع `cacert.pem` (حمله من وثائق Alipay) في دليل السكريبت للتحقق من SSL.

### تهيئة SDK
أنشئ نسخة AopClient ومرر الإعدادات:
```php
use Orvibo\AopSdk\AopClient; // اضبط النطاق لإصدار SDK الخاص بك

$aopClient = new AopClient();
$aopClient->gatewayUrl = 'https://openapi.alipay.com/gateway.do'; // عنوان URL للإنتاج
$aopClient->appId = 'your_app_id'; // أحدث SDK يستخدم appId بدلاً من partner
$aopClient->rsaPrivateKey = $config['private_key'];
$aopClient->alipayrsaPublicKey = $config['alipay_public_key'];
$aopClient->apiVersion = '1.0';
$aopClient->signType = 'RSA2'; // أحدث SDK يفضل RSA2
$aopClient->postCharset = $config['input_charset'];
$aopClient->format = 'json';
```

لدفع الجوال القديم كما في مقتطفك، ستستخدم فئات أقدم مثل `AlipaySign`.

### عمل طلب دفع
1. **بناء معاملات الطلب**:
   ```php
   $request = new AlipayTradeAppPayRequest(); // أو مشابه لإصدار SDK الخاص بك
   $request->setBizContent("{" .
       "\"body\":\"Test transaction\"," .
       "\"subject\":\"Test Subject\"," .
       "\"out_trade_no\":\"123456789\"," .
       "\"timeout_express\":\"30m\"," .
       "\"total_amount\":\"0.01\"," .
       "\"product_code\":\"QUICK_MSECURITY_PAY\"" .
       "}");
   $request->setNotifyUrl($config['service']); // عنوان URL للإشعارات الخاص بك
   ```

2. **تنفيذ الطلب**:
   ```php
   $response = $aopClient->sdkExecute($request);
   echo $response; // هذه السلسلة الموقعة تستخدم في Alipay SDK لتطبيقك
   ```

3. **في تطبيقك للجوال (إذا كنت تدمج مع تطبيق)**: مرر الرد إلى Alipay SDK الأصلي لتطبيقك (مثال: Android/iOS) لإكمال الدفع.

### معالجة الإشعارات والردود
- **الإشعارات غير المتزامنة**: أنشئ سكريبت PHP للرد على الإستدعاء عند `notify_url` للتحقق من إشعارات Alipay.
  ```php
  $aopClient->rsaCheckV1($_POST, $alipayPublicKey, 'RSA2'); // تحقق من التوقيع
  // معالجة حالة الدفع (مثال: تحديث قاعدة البيانات)
  ```
- **الإرجاع المتزامن**: بعد الدفع، يعيد Alipay التوجيه إلى `return_url` الخاص بك (إذا تم تعيينه).

### الاختبار والنشر
- استخدم بيئة الحماية الآمنة لـ Alipay للاختبار: https://openhome.alipay.com/platform/devEnv.htm.
- المشاكل الشائعة: تأكد من أن المفاتيح منسقة بشكل صحيح (بدون أسطر إضافية). استخدم RSA2 لأمان أفضل.
- نصائح أمنية: خزن المفاتيح بشكل آمن (ليس في نظام التحكم بالإصدار). تحقق دائمًا من التوقيعات لمنع العبث.

إذا كان هذا لـ SDK القديم، ففكر في الترقية إلى أحدث Alipay SDK لـ PHP (مثال: عبر Composer: `composer require alipay/openapisdk`) لميزات وأمان أفضل. للوثائق التفصيلية، قم بزيارة https://docs.open.alipay.com/. إذا واجهت أخطاء، شارك الكود والسجلات الخاصة بك لحل المشكلات.