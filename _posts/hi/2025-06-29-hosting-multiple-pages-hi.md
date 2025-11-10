---
audio: false
generated: true
lang: hi
layout: post
title: संगठनों के साथ एकाधिक GitHub पेज होस्ट करें
translated: true
type: note
---

हाँ, GitHub संगठन बनाना अतिरिक्त GitHub Pages साइटों को अद्वितीय `*.github.io` सबडोमेन के साथ होस्ट करने का एक व्यवहार्य तरीका है, क्योंकि प्रत्येक संगठन की अपनी `organization.github.io` साइट हो सकती है, जो आपकी व्यक्तिगत `username.github.io` साइट से अलग होती है। यहाँ बताया गया है कि आप इसे कैसे कर सकते हैं और आपको क्या जानने की आवश्यकता है:

### मुख्य बिंदु
- **व्यक्तिगत खाते की सीमा**: प्रत्येक GitHub उपयोगकर्ता खाते के पास केवल एक ही यूजर साइट हो सकती है, जो `username.github.io` पर होस्ट होती है और `username.github.io` नामक रिपॉजिटरी से जुड़ी होती है। यदि आपने इसे अपने व्यक्तिगत खाते के लिए पहले ही उपयोग कर लिया है, तो आप उसी खाते के तहत दूसरा `*.github.io` सबडोमेन नहीं बना सकते।
- **संगठन साइटें**: प्रत्येक GitHub संगठन की अपनी ऑर्गनाइजेशन साइट भी हो सकती है, जो `organization.github.io` पर होस्ट होती है, `organization.github.io` नामक एक रिपॉजिटरी बनाकर। यह आपको कई संगठन स्थापित करके अतिरिक्त `*.github.io` सबडोमेन बनाने की अनुमति देता है।
- **प्रोजेक्ट साइटें**: दोनों उपयोगकर्ता और संगठन खाते अन्य रिपॉजिटरी से कई प्रोजेक्ट साइटें (जैसे, `username.github.io/project` या `organization.github.io/project`) होस्ट कर सकते हैं, लेकिन ये सबपाथ होते हैं, सबडोमेन नहीं। यदि आप विशिष्ट सबडोमेन (जैसे, `sub.example.github.io`) चाहते हैं, तो आप इसे कस्टम डोमेन के बिना सीधे GitHub Pages के साथ हासिल नहीं कर सकते, क्योंकि GitHub `github.io` डोमेन के तहत `sub.example.github.io` जैसे कस्टम सबडोमेन का समर्थन नहीं करता।[](https://github.com/orgs/community/discussions/54144)

### अतिरिक्त `*.github.io` सबडोमेन के लिए GitHub संगठन बनाने के चरण
1. **एक GitHub संगठन बनाएँ**:
   - GitHub पर जाएं और अपने खाते से साइन इन करें।
   - शीर्ष-दाएं कोने में "+" आइकन पर क्लिक करें और **New organization** चुनें।
   - संगठन स्थापित करने के लिए संकेतों का पालन करें, एक अद्वितीय नाम (जैसे, `myorg`) चुनें। यह नाम सबडोमेन (जैसे, `myorg.github.io`) निर्धारित करेगा।
   - ध्यान दें: संगठन मुफ्त में बनाए जा सकते हैं, लेकिन कुछ सुविधाएँ (जैसे निजी रिपॉजिटरी) के लिए आपकी आवश्यकताओं के आधार पर एक भुगतान योजना की आवश्यकता हो सकती है। सार्वजनिक रिपॉजिटरी के लिए GitHub Pages, GitHub Free के साथ उपलब्ध है।[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)

2. **संगठन की GitHub Pages रिपॉजिटरी बनाएँ**:
   - नए संगठन में, बिल्कुल `myorg.github.io` नामक एक रिपॉजिटरी बनाएँ (`myorg` को अपने संगठन के नाम से बदलें)।
   - यह रिपॉजिटरी ऑर्गनाइजेशन साइट को होस्ट करेगी, जो `https://myorg.github.io` पर एक्सेस होगी।

3. **GitHub Pages सेट अप करें**:
   - `myorg.github.io` रिपॉजिटरी के **Settings** टैब पर जाएं।
   - **Pages** सेक्शन तक स्क्रॉल करें।
   - **Source** के तहत, वह ब्रांच चुनें जिसे आप प्रकाशित करना चाहते हैं (जैसे, `main` या `gh-pages`) और सेव करें।
   - एक बार कॉन्फ़िगर हो जाने के बाद, कुछ मिनटों में साइट `https://myorg.github.io` पर लाइव हो जाएगी।[](https://dev.to/mohammedasker/how-to-get-github-subdomain-with-github-pages-4g0p)

4. **सामग्री जोड़ें**:
   - रिपॉजिटरी की प्रकाशित होने वाली ब्रांच में एक `index.html` फ़ाइल जोड़ें या Jekyll जैसे स्टेटिक साइट जनरेटर का उपयोग करें।
   - अपने परिवर्तनों को कमिट और पुश करें। उदाहरण के लिए:
     ```bash
     git clone https://github.com/myorg/myorg.github.io
     cd myorg.github.io
     echo "Hello World" > index.html
     git add --all
     git commit -m "Initial commit"
     git push origin main
     ```
   - यह सत्यापित करने के लिए कि साइट लाइव है, `https://myorg.github.io` पर जाएं।[](https://dev.to/mohammedasker/how-to-get-github-subdomain-with-github-pages-4g0p)

5. **अतिरिक्त सबडोमेन के लिए दोहराएँ**:
   - अतिरिक्त संगठन (जैसे, `myorg2`, `myorg3`) बनाएं और प्रक्रिया को दोहराएं ताकि `myorg2.github.io`, `myorg3.github.io`, आदि प्राप्त हो सकें।
   - प्रत्येक संगठन का एक `*.github.io` सबडोमेन हो सकता है, जिससे आप जितने संगठन बनाते हैं, उतने सबडोमेन बना सकते हैं।

### सीमाएँ और विचार
- **`github.io` पर कस्टम सबडोमेन**: आप GitHub Pages के साथ सीधे `sub.myorg.github.io` जैसे सबडोमेन नहीं बना सकते। `github.io` डोमेन GitHub द्वारा प्रबंधित किया जाता है, और केवल `username.github.io` या `organization.github.io` का समर्थन किया जाता है। कस्टम सबडोमेन (जैसे, `blog.example.com`) का उपयोग करने के लिए, आपके पास एक कस्टम डोमेन होना चाहिए और DNS सेटिंग्स (CNAME रिकॉर्ड) को `myorg.github.io` की ओर इशारा करने के लिए कॉन्फ़िगर करना चाहिए।[](https://github.com/orgs/community/discussions/54144)[](https://github.com/orgs/community/discussions/64133)
- **सबडोमेन प्रति एकल रिपॉजिटरी**: प्रत्येक `*.github.io` सबडोमेन एक एकल रिपॉजिटरी (`username.github.io` या `organization.github.io`) से जुड़ा होता है। आप कस्टम डोमेन और अतिरिक्त होस्टिंग या प्रॉक्सी सेवाओं के बिना एक ही रिपॉजिटरी से कई सबडोमेन नहीं दे सकते।[](https://webmasters.stackexchange.com/questions/144484/separate-subdomains-on-one-github-page)
- **प्रबंधन ओवरहेड**: प्रत्येक संगठन के लिए अलग प्रबंधन (जैसे सदस्य, अनुमतियाँ, बिलिंग) की आवश्यकता होती है। सुनिश्चित करें कि आप कई संगठनों के प्रबंधन के लिए सहज हैं।
- **DNS और कस्टम डोमेन**: यदि आप `*.github.io` के बजाय कस्टम डोमेन (जैसे, `example.com` या `sub.example.com`) का उपयोग करना चाहते हैं, तो आप इसे रिपॉजिटरी की **Pages** सेटिंग्स में कॉन्फ़िगर कर सकते हैं और अपने DNS प्रदाता के साथ एक CNAME रिकॉर्ड जोड़ सकते हैं। उदाहरण के लिए, `sub.example.com` को `myorg.github.io` की ओर इशारा करें। टेकओवर के जोखिमों से बचने के लिए डोमेन को सत्यापित करना सुनिश्चित करें।[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)[](https://dev.to/scc33/how-to-host-a-site-with-a-subdomain-on-github-pages-5a1j)
- **निजी रिपॉजिटरी**: निजी रिपॉजिटरी के लिए GitHub Pages के लिए GitHub Pro, Team, या Enterprise प्लान की आवश्यकता होती है। यदि आप मुफ्त प्लान का उपयोग कर रहे हैं, तो सुनिश्चित करें कि आपकी `myorg.github.io` रिपॉजिटरी सार्वजनिक है।[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)

### एकाधिक सबडोमेन के लिए विकल्प
यदि आपका लक्ष्य एक ही कस्टम डोमेन के तहत कई सबडोमेन (जैसे, `blog.example.com`, `shop.example.com`) रखना है, तो आप यह कर सकते हैं:
1. Namecheap या GoDaddy जैसे रजिस्ट्रार से एक कस्टम डोमेन (जैसे, `example.com`) खरीदें।
2. अपने संगठन में कई रिपॉजिटरी (जैसे, `myorg/blog`, `myorg/shop`) बनाएँ।
3. प्रत्येक रिपॉजिटरी के लिए GitHub Pages सक्षम करें, उनकी संबंधित **Pages** सेटिंग्स में `blog.example.com` और `shop.example.com` जैसे कस्टम डोमेन सेट करें।
4. अपने DNS प्रदाता के साथ CNAME रिकॉर्ड कॉन्फ़िगर करें ताकि `blog.example.com` `myorg.github.io` की ओर और `shop.example.com` `myorg.github.io` की ओर इशारा करे। ध्यान दें कि अपने स्वयं के कस्टम डोमेन के बिना सभी रिपॉजिटरी संगठन के कस्टम डोमेन के तहत सबपाथ (जैसे, `example.com/blog`) के रूप में दिखाई देंगी।[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)[](https://stackoverflow.com/questions/68505452/github-pages-with-single-custom-subdomain-for-multiple-repositories-using-paths)
5. ध्यान रखें कि एक ही रिपॉजिटरी से कई सबडोमेन परोसना GitHub Pages द्वारा मूल रूप से समर्थित नहीं है और इसके लिए CDN या रिवर्स प्रॉक्सी जैसी बाहरी सेवाओं की आवश्यकता हो सकती है।[](https://webmasters.stackexchange.com/questions/144484/separate-subdomains-on-one-github-page)

### उदाहरण परिदृश्य
- आपने अपनी व्यक्तिगत साइट के लिए `username.github.io` का उपयोग किया है।
- `myorg` नामक एक संगठन बनाएँ और `myorg.github.io` रिपॉजिटरी बनाकर `myorg.github.io` प्राप्त करें।
- `myorg2` नामक एक और संगठन बनाएँ और `myorg2.github.io` रिपॉजिटरी बनाकर `myorg2.github.io` प्राप्त करें।
- कस्टम सबडोमेन के लिए, `example.com` के मालिक बनें, और CNAME रिकॉर्ड के माध्यम से `blog.example.com` (जो `myorg.github.io` की ओर इशारा करता है) और `shop.example.com` (जो `myorg2.github.io` की ओर इशारा करता है) सेट अप करें।

### अंतिम नोट्स
- कई संगठन बनाना, कस्टम डोमेन की आवश्यकता के बिना अतिरिक्त `*.github.io` सबडोमेन प्राप्त करने का एक सीधा तरीका है।
- यदि आप वास्तविक सबडोमेन (जैसे, `sub.myorg.github.io`) चाहते हैं, तो आपको एक कस्टम डोमेन और DNS कॉन्फ़िगरेशन की आवश्यकता होगी, क्योंकि GitHub का `github.io` इसका मूल रूप से समर्थन नहीं करता है।
- डोमेन टेकओवर जैसे सुरक्षा जोखिमों से बचने के लिए हमेशा कस्टम डोमेन को सत्यापित करें।[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- DNS परिवर्तनों को प्रसारित होने में 24 घंटे तक का समय लग सकता है।[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)

यदि आपके पास और प्रश्न हैं या विशिष्ट कॉन्फ़िगरेशन में सहायता की आवश्यकता है, तो मुझे बताएं!