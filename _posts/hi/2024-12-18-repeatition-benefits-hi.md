---
audio: false
generated: false
image: false
lang: hi
layout: post
title: प्रोग्रामिंग में दोहराव के लाभ
translated: true
type: post
---

> export PATH=/opt/homebrew/opt/ruby/bin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:"$HOME/Library/Python/3.9/bin":/Library/TeX/texbin:/Users/lzwjava/bin:/Users/lzwjava/platform-tools:/Users/lzwjava/Downloads/google-cloud-sdk/bin

(यह एक बैश कमांड है जो PATH वातावरण चर को सेट करता है। इसे हिंदी में अनुवाद करने की आवश्यकता नहीं है क्योंकि यह एक सिस्टम कमांड है और इसे वैसे ही रखना चाहिए।)

इस मामले में, वेरिएबल का उपयोग करने से बचें:

`"$HOME/Library/Python/3.9/bin"` को हिंदी में अनुवाद करने की आवश्यकता नहीं है क्योंकि यह एक फ़ाइल पथ है और इसे मूल रूप में ही रखना चाहिए।

> export PATH=/opt/homebrew/opt/ruby/bin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/lzwjava/Library/Python/3.9/bin:/Library/TeX/texbin:/Users/lzwjava/bin:/Users/lzwjava/platform-tools:/Users/lzwjava/Downloads/google-cloud-sdk/bin

यह कमांड `PATH` पर्यावरण चर को सेट करता है, जो सिस्टम को यह बताता है कि कमांड और प्रोग्राम कहाँ खोजने हैं। इसमें विभिन्न डायरेक्टरीज़ शामिल हैं जहाँ सॉफ्टवेयर और टूल्स इंस्टॉल किए गए हैं।

दूसरा संस्करण थोड़ा दोहराव वाला लगता है क्योंकि `/Users/lzwjava` डायरेक्टरी कई बार दिखाई देती है, लेकिन यह ज्यादा साफ और पढ़ने में आसान है।

प्रोग्रामिंग में दोहराव वास्तव में फायदेमंद हो सकता है। हमें हमेशा हर चीज़ को वेरिएबल्स या फ़ंक्शंस के साथ एब्स्ट्रैक्ट या सरल बनाने की आवश्यकता नहीं होती है। इस मामले में, होम डायरेक्टरी `/Users/lzwjava` शायद ही बार-बार बदलेगी, इसलिए इसे दोहराना पूरी तरह से स्वीकार्य है।

यह उसी तरह है जैसे हम लोगों के नामों का उल्लेख करते हैं: यदि हम "वह", "वह" या "वे" जैसे सर्वनामों का अत्यधिक उपयोग करते हैं, तो यह स्पष्ट नहीं होता कि हम किसके बारे में बात कर रहे हैं। नाम स्वयं बदलने की संभावना नहीं होती है, और उन्हें सीधे उपयोग करने से स्पष्टता बढ़ सकती है।

अमूर्तीकरण और सरलीकरण महत्वपूर्ण हैं, लेकिन कुछ मामलों में, वे अनावश्यक जटिलता पैदा करते हैं। कभी-कभी, दोहराव सरल और अधिक समझने योग्य होता है।