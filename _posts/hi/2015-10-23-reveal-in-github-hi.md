---
audio: false
lang: hi
layout: post
title: 'Xcode प्लगइन: घिका में बदलना'
translated: true
---

यह GitHub प्रोजेक्ट [https://github.com/lzwjava/Reveal-In-GitHub](https://github.com/lzwjava/Reveal-In-GitHub) से README.md है।

---

# Reveal-In-GitHub

यह एक Xcode प्लगइन है जो आपके वर्तमान रिपोज़िटरी के भीतर GitHub के मुख्य फ़ंक्शन की ओर सीधे-navigation करें. एक क्लिक में, GitHub हिस्ट्री, Blame, Pull Requests, Issues, और Notifications को कुछ सेकंडों में आसानी से एक्सेस करें।

![plugin](https://cloud.githubusercontent.com/assets/5022872/10867703/96e980be-80ab-11e5-9aaa-a06ef476b7f7.gif)

मेरा कंपनी GitHub पर काम करता है. मैं GitHub खुलवाना बहुत बार करता हूँ. कभी कभी, मैं Xcode पर संपादन करता हूँ और कुछ कोड को समझ नहीं पाता हूँ, तो मैं GitHub पर Blame करता हूँ. कभी कभी, मैं किसी फ़ाइल के सबसे नए कमिट्स के बारे में जानना चाहता हूँ ताकि मुझे समझने में मदद मिल सके कि कोड कैसे विकसित हुआ है. तो मुझे लगता है कि एक ऐसी टूल है जो मुझे GitHub को Xcode से जल्दी खोलने में मदद करेगी. तो मैंने इस प्लगइन को लिखा. जब आप कुछ स्रोत फ़ाइल पर Xcode पर संपादित कर रहे हैं, तो यह आसान है जानने के लिए कि आप किस GitHub रिपोज़िटरी पर काम कर रहे हैं और कौन सी फ़ाइल आप संपादित कर रहे हैं. तो यह संभावना है कि आप जल्दी से GitHub पर फ़ाइल पर जा सकते हैं, आप जो कुछ भी संपादित कर रहे हैं उस लाइन को GitHub पर जल्दी से Blame कर सकते हैं, आप जो भी रिपोज़िटरी पर काम कर रहे हैं उस पर आप जल्दी से Issues या PRs पर जा सकते हैं.

## Menu Items

<img width="700" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864813/5df3f05e-8034-11e5-9f3e-03ae3fbc3cfc.png">

इसमें छह मेनू इंसान हैं:

 Menu Title     | Shortcut              | GitHub URL Pattern (जब मैं LZAlbumManager.m लाइन 40 संपादित कर रहा हूँ)
----------------|-----------------------|----------------------------------
 Setting	    |⌃⇧⌘S |
 Repo           |⌃⇧⌘R | https://github.com/lzwjava/LZAlbum
 Issues         |⌃⇧⌘I | https://github.com/lzwjava/LZAlbum/issues
 PRs            |⌃⇧⌘P | https://github.com/lzwjava/LZAlbum/pulls
 Quick File     |⌃⇧⌘Q | https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 List History   |⌃⇧⌘L | https://github.com/lzwjava/LZAlbum/commits/fd7224/LZAlbum/manager/LZAlbumManager.m
 Blame          |⌃⇧⌘B | https://github.com/lzwjava/LZAlbum/blame/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 Notifications  |⌃⇧⌘N | https://github.com/leancloud/LZAlbum/notifications?all=1

शॉर्टकट डिजाइन की गई हैं. वे Xcode डिफ़ॉल्ट शॉर्टकट्स से संघर्ष नहीं करेंगे. शॉर्टकट पैटर्न है ⌃⇧⌘ (Ctrl+Shift+Command), मेनू शीर्षक का पहला अक्षर के साथ.

## Customize

कभी कभी, आप Wiki पर जल्दी से उछालना चाहते हैं. यहाँ तरीका है:

<img width="500" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864939/fa83f286-8037-11e5-97d7-e9549485b11d.png">

उदाहरण के लिए,

Quick file, पैटर्न और वास्तविक URL:

```
           {git_remote_url}       /blob/{commit}/          {file_path}         #{selection}
https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40-L43
```

{commit} वर्तमान ब्रांच का सबसे नया कमिट हैश है. यह ब्रांच का उपयोग करने से बेहतर है. क्योंकि ब्रांच के HEAD को बदल सकते हैं. तो कोड #L40-L43 भी बदल सकता है.

तो अगर आप वर्तमान रिपोज़िटरी के Wiki पर एक शॉर्टकट जोड़ना चाहते हैं, तो बस एक मेनू इंसान जोड़ें और पैटर्न को `{git_remote_url}/wiki` सेट करें.

सेटिंग में, `Clear Default Repos` कहता है अगर आपके पास कई git remotes हैं, तो पहली बार ट्रिगर करने के लिए, आपको उनमें से एक चुनने के लिए पूछा जाएगा:

<img width="400" src="https://cloud.githubusercontent.com/assets/5022872/10865120/5794994a-803c-11e5-9527-965f7e617e8f.png">

फिर प्लगइन याद रखता है कि आपने कौन चुना है. तो जब आप फिर से मेनू ट्रिगर करते हैं, तो वह रिमोट रिपोज़िटरी उसको डिफ़ॉल्ट के रूप में खोलेगा. बटन `Clear Default Repos` को इस सेटिंग को क्लियर करेगा, फिर से चुनने के लिए पूछेगा.

## Install

[Alcatraz](http://alcatraz.io/) से सिफारिश है,

![qq20151101-1 2x](https://cloud.githubusercontent.com/assets/5022872/10867743/0ce351c6-80ae-11e5-82e2-f740887153f7.jpg)

या

1. इस रिपो को क्लोन करें.
2. `Reveal-In-GitHub.xcodeproj` को खोलें और इसे बिल्ड करें.
3. Reveal-In-GitHub.xcplugin को `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins` में स्थानांतरित करना होगा
4. Xcode को फिर से शुरू करें
5. किसी भी GitHub प्रोजेक्ट को खोलें और ⌃⇧⌘B (Ctrl+Shift+Command+B) दबाएं कोड को Blame करने के लिए.

## 安装

[Alcatraz](http://alcatraz.io/) का उपयोग करने की सिफारिश है, आप [डेवटंग की](http://blog.devtang.com/blog/2014/03/05/use-alcatraz-to-manage-xcode-plugins/) एक पोस्ट को सन्दर्भ में ले सकते हैं। इंस्टॉल करने के बाद, ऊपर दिए गए चित्र के अनुसार "Reveal In GitHub" खोजें और "Install" पर क्लिक करें।

अगर आप इस टूल का उपयोग नहीं कर रहे हैं, तो बस तीन कदम हैं:

* इस प्रोजेक्ट को अपने पास क्लोन करें।
* xcodeproj को खोलें, Build क्लिक करें. यह `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins` डायरेक्टरी में Reveal-In-GitHub.xcplugin फाइल पैदा करेगा।
* Xcode को फिर से शुरू करें, किसी भी GitHub पर रखी गई प्रोजेक्ट को खोलें। `Ctrl+Shift+Command+B` दबाएं।

## Credit

इसका विकास करते समय, एक और प्लगइन [ShowInGitHub](https://github.com/larsxschneider/ShowInGitHub) को कुछ ऐसा करने को देखा. मैं उससे कुछ टेक्निक सीखा. उस लिए धन्यवाद.

## License

MIT