---
audio: false
generated: false
image: false
lang: hi
layout: post
title: 'Xcode Plugin: GitHub में Reveal'
translated: true
type: post
---

यह GitHub परियोजना [https://github.com/lzwjava/Reveal-In-GitHub](https://github.com/lzwjava/Reveal-In-GitHub) की README.md है।

---

# Reveal-In-GitHub

एक Xcode प्लगइन है जो आपकी वर्तमान रिपोजिटरी में GitHub के मुख्य फंक्शनों तक की सुलभ नाविगेशन के लिए डिजाइन किया गया है। बस एक क्लिक के साथ, GitHub हिस्ट्री, ब्लेम, पुल रिक्वेस्ट, इश्यू और नोटिफिकेशन तक कुछ सेकंड में आसानी से पहुंचें।

![plugin](https://cloud.githubusercontent.com/assets/5022872/10867703/96e980be-80ab-11e5-9aaa-a06ef476b7f7.gif)

मेरे काम पर GitHub पर काम किया जाता है। मुझे GitHub खोलना बहुत आता है। कभी-कभी मैं Xcode पर संपादित करता हूँ और कुछ कोड को समझने में असमर्थ रहता हूँ, तो मैं GitHub पर ब्लेम करता हूँ। कभी-कभी एक फाइल के नए कमिट्स को ढूंढने के लिए, जिससे मुझे पता चलता है कि कोड कैसे विकसित हुआ। इसलिए मैंने सोचा कि क्या एक औजार है जो मुझे Xcode से GitHub खोलने में मदद कर सके? इसलिए मैंने इस प्लगइन को लिखा। जब आप किसी स्रोत फाइल को संपादित करते हैं, तो आप आसानी से जान सकते हैं कि आप किस GitHub रिपोजिटरी पर काम कर रहे हैं और आप किस फाइल को संपादित कर रहे हैं। इसलिए, आप आसानी से GitHub पर फाइल तक पहुँच सकते हैं, वर्तमान संपादित लाइन पर GitHub पर ब्लेम ले जा सकते हैं, और आप उन इश्यूज़ या PRs तक पहुँच सकते हैं जो आपने वर्तमान रिपोजिटरी पर काम कर रहे हैं।

## Menu Items

<img width="700" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864813/5df3f05e-8034-11e5-9f3e-03ae3fbc3cfc.png">

इसमें छह मेनू आइटम हैं:

| Menu Title     | Shortcut              | GitHub URL Pattern (जब मैं LZAlbumManager.m लाइन 40 संपादित कर रहा हूँ)                |
|----------------|-----------------------|----------------------------------|
| Setting	    |⌃⇧⌘S |
| Repo           |⌃⇧⌘R | https://github.com/lzwjava/LZAlbum |
| Issues         |⌃⇧⌘I | https://github.com/lzwjava/LZAlbum/issues |
| PRs            |⌃⇧⌘P | https://github.com/lzwjava/LZAlbum/pulls |
| Quick File     |⌃⇧⌘Q | https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40 |
| List History   |⌃⇧⌘L | https://github.com/lzwjava/LZAlbum/commits/fd7224/LZAlbum/manager/LZAlbumManager.m |
| Blame          |⌃⇧⌘B | https://github.com/lzwjava/LZAlbum/blame/fd7224/LZAlbum/manager/LZAlbumManager.m#L40 |
| Notifications  |⌃⇧⌘N | https://github.com/leancloud/LZAlbum/notifications?all=1 |

शॉर्टकट सावधानी से डिजाइन किए गए हैं। वे Xcode डिफॉल्ट शॉर्टकट्स से टकरा नहींेंगे। शॉर्टकट पैटर्न है ⌃⇧⌘ (Ctrl+Shift+Command), और मेनू शीर्षक के पहला अक्षर का बाद।

## Customize

कभी-कभार, आप Wiki तक तेजी से पहुँचना चाहेंगे। यहाँ तक पहुंचने का तरीका है, सेटिंग खोलें:

<img width="500" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864939/fa83f286-8037-11e5-97d7-e9549485b11d.png">

उदाहरण के लिए,

Quick file, पैटर्न और वास्तविक URL:

```
           {git_remote_url}       /blob/{commit}/          {file_path}         #{selection}
https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40-L43
```

{commit} वर्तमान ब्रांच की नवीनतम कमिट हैश है। यह एक ब्रांच से बेहतर है क्योंकि ब्रांच की HEAD बदल सकती है। इसलिए #L40-L43 में कोड भी बदल सकता है।

तो यदि आप वर्तमान रिपोजिटरी के Wiki तक शॉर्टकट जोड़ना चाहते हैं, तो बस एक मेनू आइटम जोड़ें और पैटर्न को `{git_remote_url}/wiki` पर सेट करें।

सेटिंग में, `Clear Default Repos` कहता है कि अगर आपने कई git रिमोट हैं, तो पहली बार ट्रिगर करने पर, यह आपको उनमें से एक चुनने के लिए पूछेगा:

<img width="400" src="https://cloud.githubusercontent.com/assets/5022872/10865120/5794994a-803c-11e5-9527-965f7e617e8f.png">

फिर प्लगइन याद रखता है कि आपने कौन सा चुना है। इसलिए जब आप फिर मेनू को ट्रिगर करते हैं, तो वह रिमोट रिपोजिटरी को डिफॉल्ट के रूप में खोलेगा। बटन `Clear Default Repos` इस सेटिंग को क्लियर कर देगा, फिर से चुनने की मांग करेंगे।

## Install

[Alcatraz](http://alcatraz.io/) से इंस्टॉल करने की सिफारिश है,

![qq20151101-1 2x](https://cloud.githubusercontent.com/assets/5022872/10867743/0ce351c6-80ae-11e5-82e2-f740887153f7.jpg)

या

1. इस रिपोजिटरी को क्लोन करें।
2. `Reveal-In-GitHub.xcodeproj` खोलें, और इसे बिल्ड करें।
3. Reveal-In-GitHub.xcplugin `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins` में होना चाहिए।
4. Xcode को फिर से शुरू करें
5. कोई GitHub परियोजना खोलें और ⌃⇧⌘B (Ctrl+Shift+Command+B) दबाएं कोड को ब्लेम करने के लिए।

## 安装

[Alcatraz](http://alcatraz.io/) का उपयोग करने की सिफारिश है, [ब्लॉग](http://blog.devtang.com/blog/2014/03/05/use-alcatraz-to-manage-xcode-plugins/) का संदर्भ ले सकते हैं, इंस्टॉल करने के बाद, ऊपर दिए गए चित्र के अनुसार `Reveal In GitHub` खोजें, `Install` बटन पर क्लिक करें।

इसे नहीं उपयोग करने के लिए, तो बस तीन कदमों की आवश्यकता है:

* इस परियोजना को स्थानीय रूप से क्लोन करें।
* xcodeproj खोलें, बिल्ड क्लिक करें। यह `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins` डाइरेक्टरी में Reveal-In-GitHub.xcplugin फ़ाइल उत्पन्न करेगा।
* Xcode को फिर से शुरू करें, किसी भी GitHub पर रखे गए परियोजना को खोलें। `Ctrl+Shift+Command+B` दबाएं, तो कोड को ब्लेम कर सकेंगे।

## Credit

इसका विकास करते समय, एक अन्य प्लगइन [ShowInGitHub](https://github.com/larsxschneider/ShowInGitHub) को देखा, जो कुछ समान काम करता है। मैं इससे कुछ तकनीक सीखा। इसके लिए धन्यवाद।

## License

MIT