---
audio: false
generated: true
lang: hi
layout: post
title: PHP QR कोड जनरेट करने के लिए उपकरण
translated: true
---

### Key Points
- "endroid/qr-code" version 2.2.2 का उपयोग करने के लिए Composer के माध्यम से इसे install करना जरूरी लगता है और GD extension को enable करना जरूरी है.
- Research के अनुसार, Builder class का उपयोग करके QR codes generate किया जा सकता है, parameters जैसे data, size, और writer set करके, फिर result save या output किया जा सकता है.
- Library PNG, SVG, और अन्य formats को support करता hai, logos और labels के options के साथ, लेकिन version 2.2.2 के लिए verify करना जरूरी hai.

### Installation
Pehle, Composer ke sath library install karein, command ke sath:
```
composer require endroid/qr-code:2.2.2
```
Yadiyaphi, PHP setup mein GD extension enable hona chahiye, kyunki yeh image generation ke liye required hai.

### Usage Example
Yeh ek basic example hai Builder class ka, jo version 2.2.2 ke sath compatible hoga:
```php
use Endroid\QrCode\Builder\Builder;
use Endroid\QrCode\Encoding\Encoding;
use Endroid\QrCode\ErrorCorrectionLevel\ErrorCorrectionLevelHigh;
use Endroid\QrCode\Writer\PngWriter;

$url = 'https://example.com';
$qrCode = Builder::create()
    ->writer(new PngWriter())
    ->data($url)
    ->encoding(new Encoding('ISO-8859-1'))
    ->errorCorrectionLevel(new ErrorCorrectionLevelHigh())
    ->build();
$qrCode->saveToFile('qr_code.png');
```
Yeh ek URL ke liye QR code create karta hai aur isse PNG file ke roop mein save karta hai. Aap isse web display ke liye data URI ke roop mein bhi output kar sakte hain.

### Additional Notes
Library various writers (jaise PNG, SVG) ko support karta hai aur customization jaise logos ya labels add karna allow karta hai. Lekin version 2.2.2 purana hai, to current documentation mein jo features hain (jaise advanced logo options), wo available nahi hote, to specific version ke liye documentation check karein [GitHub](https://github.com/endroid/qr-code) par.

---

### Survey Note: Detailed Guide on Using "endroid/qr-code" Version 2.2.2

Yeh note "endroid/qr-code" library, version 2.2.2 ka comprehensive guide provide karta hai, PHP applications mein QR codes generate karne ke liye. Yeh direct answer par expand karta hai, sabhi relevant details ko include karke, ensuring a thorough understanding for developers, especially jo library ke naye hain. Content ko professional article ke roop mein structure kiya gaya hai, tables ke sath clarity ke liye aur inline URLs ke sath further reference ke liye.

#### Introduction
"endroid/qr-code" library ek PHP tool hai QR codes generate karne ke liye, widely use kiya jaata hai applications jaise product tracking, document management, aur marketing ke liye. Version 2.2.2, jo query mein specify kiya gaya hai, ek purana release hai, aur [Packagist](https://packagist.org/packages/endroid/qr-code) par library ko abandoned note kiya gaya hai, lekin yeh basic QR code generation ke liye functional hai. Yeh guide installation aur usage par focus karta hai, version 2.2.2 ke sath compatibility ensure karke, aur naye versions se potential differences ko acknowledge karke.

#### Installation Process
Pehle, aapko library ko Composer ke sath install karna padta hai, PHP package manager. Command hai:
```
composer require endroid/qr-code:2.2.2
```
Yeh ensure karta hai ki aapke paas exact version 2.2.2 hai. Ek critical requirement hai GD extension PHP ke liye, jo enable aur configure hona chahiye, kyunki yeh image generation ke liye essential hai. Bina iske, library visual QR codes produce nahi kar sakti.

| Step                  | Details                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| Install Command       | `composer require endroid/qr-code:2.2.2`                                |
| PHP Requirement       | Ensure GD extension is enabled (check `phpinfo()` for confirmation)     |

Research ke anusaar, library ka GitHub repository ([GitHub](https://github.com/endroid/qr-code)) aur [Packagist](https://packagist.org/packages/endroid/qr-code) pages yeh installation method ko confirm karte hain, specific version 2.2.2 documentation nahi mila, suggesting reliance on general usage patterns.

#### Usage Details
Library do primary methods provide karta hai QR code generation ke liye: Builder class ka use karke ya directly QrCode class ke sath. Query ke focus usage par hai, to Builder approach recommend kiya gaya hai simplicity ke liye, lekin dono detailed hain completeness ke liye.

##### Using the Builder Class
Builder class ek fluent interface provide karta hai QR codes ko configure karne ke liye. Recent documentation ke examples ke basis par, ek basic implementation hai:
```php
use Endroid\QrCode\Builder\Builder;
use Endroid\QrCode\Encoding\Encoding;
use Endroid\QrCode\ErrorCorrectionLevel\ErrorCorrectionLevelHigh;
use Endroid\QrCode\Writer\PngWriter;

$url = 'https://example.com';
$qrCode = Builder::create()
    ->writer(new PngWriter())
    ->data($url)
    ->encoding(new Encoding('ISO-8859-1'))
    ->errorCorrectionLevel(new ErrorCorrectionLevelHigh())
    ->build();
$qrCode->saveToFile('qr_code.png');
```
Yeh code ek URL ke liye QR code create karta hai, PNG format ka use karke, ISO-8859-1 encoding ke sath better scanner compatibility ke liye aur high error correction ke sath. Aap isse data URI ke roop mein bhi output kar sakte hain:
```php
$qrCodeDataUri = $qrCode->getDataUri();
```
Yeh HTML mein embed karne ke liye useful hai, jaise `<img src="<?php echo $qrCodeDataUri; ?>">`.

Lekin version 2.2.2 ke age ke karan, kuch classes jaise `ErrorCorrectionLevelHigh` alag name ho sakte hain (jaise `ErrorCorrectionLevel::HIGH` older versions mein). Research ke anusaar Stack Overflow posts ([Stack Overflow](https://stackoverflow.com/questions/40777377/endroid-qr-code)) ke sath, older versions ne methods jaise `setErrorCorrection('high')` ka use kiya, to 2.2.2 ke liye API ko verify karein.

##### Using the QrCode Class Directly
Zyada control ke liye, aap QrCode class ka use kar sakte hain, jaise examples mein dekha gaya hai:
```php
use Endroid\QrCode\QrCode;
use Endroid\QrCode\Writer\PngWriter;

$qrCode = new QrCode('Life is too short to be generating QR codes');
$qrCode->setSize(300);
$qrCode->setMargin(10);
$writer = new PngWriter();
$result = $writer->write($qrCode);
$result->saveToFile('qrcode.png');
```
Yeh method zyada verbose hai, lekin fine-tuning allow karta hai, jaise foreground aur background colors set karna, jo version 2.2.2 ke liye relevant ho sakte hain. Phir bhi, method availability ke liye documentation check karein.

#### Configuration Options
Library various writers ke sath different output formats ke liye support karta hai, jaise table mein detailed hai, current documentation ke basis par, version 2.2.2 ke liye verify karne ke sath:

| Writer Class          | Format   | Notes                                                                 |
|-----------------------|----------|----------------------------------------------------------------------|
| PngWriter             | PNG      | Compression level configurable, default -1                           |
| SvgWriter             | SVG      | Suitable for vector graphics, no compression options                 |
| WebPWriter            | WebP     | Quality 0-100, default 80, good for web use                          |
| PdfWriter             | PDF      | Unit in mm, default, good for print                                 |

Encoding options mein UTF-8 (default) aur ISO-8859-1 shamil hain, jo latter barcode scanner compatibility ke liye recommend kiya gaya hai. Round block size modes (margin, enlarge, shrink, none) readability ko improve kar sakte hain, lekin unka availability 2.2.2 mein confirm karna padta hai.

#### Advanced Features and Considerations
Advanced use ke liye, jaise logos ko embed karna, Builder class methods jaise `logoPath()` aur `logoResizeToWidth()` ko support karta hai, jaise ek Medium article mein dekha gaya hai ([Medium](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)). Lekin yeh post-2.2.2 additions ho sakte hain, to compatibility test karein. Generated QR codes ka validation possible hai, lekin yeh performance ko impact karta hai aur default disabled hai, ek detail [GitHub](https://github.com/endroid/qr-code) se.

[Packagist](https://packagist.org/packages/endroid/qr-code) par library ka abandonment note ke karan, potential security ya maintenance concerns ko note karna chahiye, lekin basic use ke liye yeh viable hai. Symfony users ke liye ek bundle hai ([GitHub](https://github.com/endroid/qr-code-bundle)), lekin yeh general PHP usage ke bahar hai.

#### Version-Specific Notes
Research mein direct documentation version 2.2.2 ke liye nahi mila, GitHub tags mein yeh list nahi kiya gaya, suggesting yeh ek purana release ho sakta hai ya typo. Current repository versions tak 6.0.0 tak dikhata hai, aur [Packagist](https://packagist.org/packages/endroid/qr-code) yeh list karta hai abandoned, endroid/qr-code ko recommend karta hai, jo confusing hai kyunki yeh same package hai. Yeh potential renaming ya versioning issues ko indicate karta hai, to users ko dependencies ko lock karna chahiye aur upgrades ko test karna chahiye.

#### Conclusion
"endroid/qr-code" version 2.2.2 ka use Composer ke sath install karke, GD extension ko ensure karke, aur Builder ya QrCode class ke sath QR codes generate karke hota hai. Yadi examples current documentation ke basis par hain, to 2.2.2 ke liye API differences ko verify karein, especially advanced features ke liye. Further details ke liye, library ka GitHub page aur related Stack Overflow discussions ko consult karein.

#### Key Citations
- [QR Code Generator GitHub Repository](https://github.com/endroid/qr-code)
- [endroid/qr-code Packagist Page](https://packagist.org/packages/endroid/qr-code)
- [Creating QR Codes with Embedded Images Medium Article](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)
- [Endroid QR Code Stack Overflow Discussion](https://stackoverflow.com/questions/40777377/endroid-qr-code)