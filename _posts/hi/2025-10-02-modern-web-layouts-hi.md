---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: आधुनिक वेब शैलियाँ और लेआउट
translated: true
type: note
---

### अवलोकन
यह SCSS (Sass) सिंटैक्स में लिखा गया CSS कोड प्रतीत होता है, जिसमें नेस्टिंग, प्स्यूडोक्लासेस के लिए एम्परसेंड (&) सेलेक्टर और @extend डायरेक्टिव शामिल हैं। यह एक बुनियादी वेब पेज लेआउट, फॉर्म, बटन और यूटिलिटी के लिए स्टाइल को परिभाषित करता है, जिसमें एक साफ-सुथरा, आधुनिक सौंदर्यशास्त्र (जैसे, गोल कोने, हल्की छाया, होवर ट्रांजिशन) है। बिना इकाई वाले प्रॉपर्टीज (जैसे `font-size 16px`) SCSS के लिए शॉर्टहैंड हैं। मैं इसे सेक्शन के अनुसार तोड़कर समझाऊंगा, सेलेक्टर और उनके प्रभावों की व्याख्या करते हुए।

### ग्लोबल स्टाइल्स (html, body)
```css
html, body
  font-family Verdana
  font-size 16px
  height 100%
  background-color #D2D2D2
```
- एक सरल फॉन्ट स्टैक (ज़रूरत पड़ने पर वर्डाना फॉलबैक) 16px आकार पर लागू करता है।
- पूरे पेज के लेआउट के लिए पूरी ऊंचाई (100%) सेट करता है, अक्सर केंद्रित करने या व्यूपोर्ट को कवर करने के लिए।
- बैकग्राउंड एक हल्का ग्रे (#D2D2D2) है, जो एक न्यूट्रल बेस कलर के लिए है।

### लिस्ट और लिंक स्टाइल्स (ul, a)
```css
ul
  list-style-type none
  padding 0
  margin 0

a
  color #000
  cursor pointer
  text-decoration none
```
- अनऑर्डर्ड लिस्ट से डिफॉल्ट बुलेट्स, पैडिंग और मार्जिन हटाता है ताकि कस्टम स्टाइलिंग अधिक साफ-सुथरी हो।
- लिंक काले (#000) होते हैं, होवर पर पॉइंटर कर्सर होता है, और कोई अंडरलाइन नहीं होती, जिससे वे बटन जैसे महसूस होते हैं।

### कलर और टेक्स्ट यूटिलिटी (.a-blue)
```css
.a-blue
  color #00BDEF
```
- नीले टेक्स्ट (#00BDEF, एक हल्का नीला) के लिए एक क्लास, संभवतः एक्सेंट के लिए।

### बटन स्टाइल्स (.btn, .btn-blue, .btn-gray, .btn-gray-2)
```css
.btn
  border-radius 3px
  padding 10px

.btn-blue
  background #00BDEF
  color #fff
  -webkit-box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset,0px 1px 2px rgba(0,0,0,0.15)
  box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset,0px 1px 2px rgba(0,0,0,0.15)
  &:hover
    background #00ABD8
    transition .5s

.btn-gray
  background #eee
  color #333
  border 1px solid #d5d5d5
  border-radius 3px
  -webkit-box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset,0px 1px 2px rgba(0,0,0,0.15)
  box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset,0px 1px 2px rgba(0,0,0,0.15)
  &:hover
    background #ddd
    transition 0.5s

.btn-gray-2
  background #eee
  color #333
  border 1px solid #d5d5d5
  border-radius 3px
  &:hover
    background #ddd
    transition 0.5s
```
- `.btn` 3px गोल कोनों और 10px पैडिंग के लिए एक बेस क्लास है।
- `.btn-blue`: नीला बटन (#00BDEF बैकग्राउंड, सफेद टेक्स्ट) जिसमें गहराई के लिए इनसेट हाइलाइट्स और ड्रॉप शैडो हैं। होवर पर नीला रंग गहरा हो जाता है और 0.5s का स्मूद ट्रांजिशन होता है।
- `.btn-gray` और `.btn-gray-2`: ग्रे बटन (हल्का बैकग्राउंड #eee, गहरा टेक्स्ट #333, सूक्ष्म बॉर्डर #d5d5d5) जिनमें समान शैडो हैं। `.btn-gray-2` में एक्सप्लिसिट बॉक्स-शैडो नहीं है लेकिन उसका होवर इफेक्ट समान है (#ddd पर हल्का हो जाता है)। सेकेंडरी एक्शन के लिए उपयोगी।

### पोजिशनिंग यूटिलिटीज (.absolute-center, .full-space)
```css
.absolute-center
    margin auto
    position absolute
    top 0
    left 0
    bottom 0
    right 0

.full-space
    position absolute
    top 0
    left 0
    bottom 0
    right 0
```
- `.absolute-center`: किसी एलिमेंट को उसके पैरेंट में पूर्ण रूप से केंद्रित करता है (ऊपर/नीचे/बाएं/दाएं 0 पर, ऑटो मार्जिन के साथ)।
- `.full-space`: किसी एलिमेंट को उसके पैरेंट की पूरी जगह को पूर्ण रूप से भरने के लिए बनाता है।

### फॉर्म स्टाइल्स (.base-form, input/textarea/select, button)
```css
.base-form
  @extend .absolute-center
  max-width 350px
  height 400px
  background #fff
  border-radius 20px
  text-align center
  padding 20px 10px

input, textarea, select
  box-sizing border-box
  border none
  outline none
  &:focus
    border none
    outline none
    box-shadow 0px 1px 4px 0px rgba(0,0,0,.06)
    -webkit-box-shadow 0px 1px 4px 0px rgba(0,0,0,.06)

button
  border-style none
  outline none
```
- `.base-form`: `.absolute-center` को एक्सटेंड करता है ताकि एक मोडल जैसा फॉर्म केंद्रित हो सके (350px अधिकतम चौड़ाई, 400px ऊंचाई, सफेद बैकग्राउंड, 20px बॉर्डर रेडियस, केंद्रित टेक्स्ट, आंतरिक पैडिंग)। लॉगिन/साइनअप फॉर्म के लिए आदर्श।
- इनपुट, टेक्स्टएरिया, सेलेक्ट: बॉर्डरलेस होते हैं जिनमें बॉक्स-साइज़िंग होती है ताकि चौड़ाई में पैडिंग शामिल हो; फोकस आउटलाइन नहीं होती, लेकिन UX के लिए फोकस पर एक सूक्ष्म ग्रे शैडो जोड़ता है।
- बटन: डिफॉल्ट बॉर्डर और आउटलाइन हटाता है, यह मानते हुए कि बेहतर दिखावट के लिए `.btn` स्टाइल्स लागू होंगी।

यह कोड स्टाइलिश बटन और इनपुट के साथ एक रिस्पॉन्सिव, केंद्रित फॉर्म पेज सेट करता है। यदि SCSS का उपयोग कर रहे हैं, तो इसे स्टैंडर्ड CSS में कंपाइल करें। कस्टमाइज़ेशन के लिए, रंग या आकार को आवश्यकतानुसार समायोजित करें।