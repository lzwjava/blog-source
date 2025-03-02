---
audio: false
generated: false
lang: hi
layout: post
title: फूल पहचान एप
translated: true
---

यह गीथब प्रोजेक्ट [https://github.com/lzwjava/flower-recognition](https://github.com/lzwjava/flower-recognition) का README.md है।

---

### फूल पहचान एप्लिकेशन

यह एक फूल पहचान एंडरॉइड ऐप्लिकेशन है, जो उपयोगकर्ताओं को फूलों को पहचानने में मदद करने के लिए फोटो लेने और पहचान को सहायता करने के लिए चक्कर खींचने की सुविधा प्रदान करता है।

#### विशेषताएँ:
- **फोटो लेना**: उपयोगकर्ता ऐप के भीतर फूलों का फोटो ले सकते हैं.
- **ड्रॉइंग फंक्शनैलिटी**: फूलों के छवियों पर चक्कर और अनेक टिप्पणियां ड्रॉइंग करने की क्षमता.
- **पहचान**: सिक्योर उपयोगकर्ता पहचान लॉगिन स्क्रीन के साथ.
- **परिणाम प्रदर्शन**: पहचान परिणाम एक उपयोगकर्ता-फ्रेंडली इंटरफेस में प्रदर्शित.
- **मेटेरियल डिज़ाइन**: एक आधुनिक और आंतरिक उपयोगकर्ता अनुभव के लिए मेटेरियल डिज़ाइन सिद्धांतों का लागू.

#### फ़ाइल संरचना:
```
└── com
    └── lzw
        └── flower
            ├── activity
            │   ├── LoginActivity.java
            │   └── PhotoActivity.java
            ├── adapter
            │   └── PhotoAdapter.java
            ├── avobject
            │   └── Photo.java
            ├── base
            │   ├── App.java
            │   ├── ImageLoader.java
            │   └── SplashActivity.java
            ├── deprecated
            │   ├── CameraActivity.java
            │   └── Deprecated.java
            ├── draw
            │   ├── Draw.java
            │   ├── DrawActivity.java
            │   ├── DrawFragment.java
            │   ├── DrawView.java
            │   ├── HelpBtn.java
            │   ├── History.java
            │   ├── Tooltip.java
            │   └── ZoomImageView.java
            ├── fragment
            │   ├── RecogFragment.java
            │   └── WaitFragment.java
            ├── material
            │   └── MaterialActivity.java
            ├── result
            │   ├── FlowerAdapter.java
            │   ├── FlowerData.java
            │   ├── Image.java
            │   ├── ResultActivity.java
            │   └── ResultFragment.java
            ├── service
            │   └── PhotoService.java
            ├── utils
            │   ├── BitmapUtils.java
            │   ├── Crop.java
            │   ├── ImageListDialogBuilder.java
            │   ├── Logger.java
            │   ├── PathUtils.java
            │   └── Utils.java
            └── web
                ├── Upload.java
                ├── UploadImage.java
                └── Web.java
```

#### घटक:
- **Activities**: अलग-अलग ऐपलिकेशन गतिविधियों जैसे लॉगिन, फोटो लेना और स्प्लैश स्क्रीन को सँभालने वाले क्लासों को शामिल करता है.
- **Adapters**: फोटो और पहचान परिणामों का प्रदर्शन संभालता है.
- **AVObject**: फोटो ऑब्जेक्ट्स के साथ संबद्ध मेटादेटा.
- **ड्रॉइंग**: फूलों के छवियों पर चक्कर और टिप्पणियों को ड्रॉइंग करने से संबंधित क्लास.
- **Fragments**: पहचान परिणामों और इंतजार संकेतकों को प्रदर्शित करने के लिए UI घटकों को प्रदान करता है.
- **Material**: संभवतः मेटेरियल डिज़ाइन दिशानिर्देशों को लागू करने से संबंधित हो सकता है.
- **Services**: फोटो से संबंधित पृष्ठभूमि कार्यों और डेटा म्यानिपुलेशन को संभालता है.
- **Utils**: विभिन्न कार्यों जैसे छवि मैनिपुलेशन और लॉगिंग के लिए उपयोगिता क्लासों को शामिल करता है.

#### उपयोग:
1. रिपोजिटरी को क्लोन करें।
2. प्रोजेक्ट को एंड्रॉइड स्टूडियो में खोलें।
3. ऐप को एंड्रॉइड डिवाइस या एमुलेटर पर बिल्ड और चलाएं।

#### लाइसेंस:
यह प्रोजेक्ट [MIT लाइसेंस](LICENSE) के तहत लाइसेंस प्राप्त है।