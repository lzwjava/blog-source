---
audio: false
generated: true
lang: hi
layout: post
title: Qiniu PHP SDK का उपयोग
translated: true
---

Qiniu PHP SDK का उपयोग करने के लिए, आपko PHP में Qiniu PHP SDK को apne project mein integrate karna padega. Yeh SDK aapko Qiniu Cloud Storage services ke saath interact karne mein madad karta hai, jaise ki files upload karna, buckets manage karna, aur aur bhi zyada. Niche diye gaye steps se aapko shuru karne mein madad milegi:

---

### 1. Qiniu PHP SDK ko Install Karein
SDK ko install karne ka recommended tareeka Composer ke through hai, jo PHP ka dependency manager hai. Yakeen rakhein ki aapke system par Composer install hai.

#### Steps:
- Apne terminal ko kholain aur apne project directory mein navigate karein.
- Niche diye gaye command ko run karein taaki Qiniu PHP SDK (version 7.x) ko apne project mein add kar sakein:
  ```bash
  composer require qiniu/php-sdk "^7.0"
  ```
- Composer SDK aur uske dependencies ko `vendor/` directory mein download karega aur ek autoload file generate karega.

Agar aapke paas Composer install nahi hai, to aap ise [getcomposer.org](https://getcomposer.org/) se download kar sakte hain.

---

### 2. Apne Project ko Setup Karein
Installation ke baad, aapko apne PHP script mein autoloader ko include karna padega taaki SDK classes ka use kar sakein.

#### Example:
Apne project directory mein ek PHP file (e.g., `index.php`) create karein aur niche diye gaye line ko top par add karein:
```php
require_once 'vendor/autoload.php';
```

Yeh ensure karta hai ki SDK classes jab zaroorat hota hai tab automatically load ho jaye.

---

### 3. Authentication ko Configure Karein
Qiniu SDK ka use karne ke liye, aapko apne Qiniu `AccessKey` aur `SecretKey` chahiye, jo aap apne Qiniu account dashboard se obtain kar sakte hain.

#### Example:
```php
use Qiniu\Auth;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';

$auth = new Auth($accessKey, $secretKey);
```

`'YOUR_ACCESS_KEY'` aur `'YOUR_SECRET_KEY'` ko apne actual credentials se replace karein.

---

### 4. Basic Usage: Ek File ko Upload Karein
Qiniu SDK ke saath sabse common task ek file ko bucket mein upload karna hai. Yeh ek example hai ki kaise ek local file ko upload karein.

#### Example:
```php
use Qiniu\Storage\UploadManager;

$bucket = 'YOUR_BUCKET_NAME'; // Apne Qiniu bucket name se replace karein
$filePath = '/path/to/your/file.txt'; // Upload karne wale file ka path
$key = 'file.txt'; // Qiniu storage mein file ka name (null set kar sakte hain taaki original filename ka use ho sake)

$token = $auth->uploadToken($bucket); // Ek upload token generate karein
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "Upload failed: " . $error->message();
} else {
    echo "Upload successful! File hash: " . $ret['hash'];
}
```

- `$bucket`: Apne Qiniu bucket ka name.
- `$filePath`: Upload karne wale file ka local path.
- `$key`: Qiniu mein file ko store karne ke liye file key (name). Agar null set kiya gaya hai, to Qiniu file ke hash ke basis par ek key generate karega.
- `$token`: Apne credentials aur bucket name ke saath generate kiya gaya upload token.
- `putFile` method ek array return karta hai: `$ret` (success info) aur `$error` (agar koi error hai to error info).

---

### 5. Additional Features
Qiniu PHP SDK bahut sare aur functionalities provide karta hai, jaise ki:
- **Buckets ko Manage Karna**: `Qiniu\Storage\BucketManager` ka use karke files ko list karna, delete karna, ya bucket settings ko manage karna.
- **File Operations**: Apne bucket mein files ko copy, move, ya delete karna.
- **Image Processing**: Resized ya formatted images ke liye URLs generate karna.

#### Example: Ek Bucket mein Files ko List Karein
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

### 6. Error Handling
Hamesha SDK operations ke baad `$error` variable ko check karein. Agar koi operation fail ho gaya, to `$error` mein details hoga ki kya ghalat hua.

#### Example:
```php
if ($error !== null) {
    var_dump($error);
} else {
    var_dump($ret);
}
```

---

### 7. Requirements
- PHP version: SDK version `^7.0` PHP 5.3.3 aur uske upar (PHP 8.x tak later releases mein) support karta hai.
- Extensions: Yakeen rakhein ki `cURL` aur `xml` PHP extensions enable hain, kyunki yeh SDK ke liye zaroori hain.

Aap apne PHP version aur extensions ko check kar sakte hain:
```bash
php -v
php -m
```

---

### 8. Aage Kahan Jaana Hai
- **Documentation**: Aur details ke liye, refer karein [official Qiniu PHP SDK documentation](https://developer.qiniu.com/kodo/sdk/php) ya [GitHub repository](https://github.com/qiniu/php-sdk).
- **Examples**: GitHub repo mein `examples/` directory ko check karein aur aur use cases ke liye.
- **Support**: Agar aapko koi issue milta hai, to Qiniu support (<support@qiniu.com>) ko ek ticket submit karein ya unke community forums mein pooch sakte hain.

---

### Full Example Code
Yeh ek complete script hai ek file ko upload karne ke liye:
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

Placeholder values (`YOUR_ACCESS_KEY`, `YOUR_SECRET_KEY`, `YOUR_BUCKET_NAME`, `/path/to/your/file.txt`) ko apne actual data se replace karein, aur aap ready hain!

Agar aapko kisi specific feature ke saath madad chahiye, to bataiye!