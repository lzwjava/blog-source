---
audio: false
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: अवांछित गिटहब फ़ॉर्क हटाना
translated: true
type: note
---

समझ गया। संक्षेप में: आप सीधे किसी और के fork को नहीं हटा सकते। लेकिन आप (a) उनसे पूछ सकते हैं, (b) संवेदनशील सामग्री हटा सकते हैं और भविष्य में लीक होने से रोक सकते हैं, और (c) GitHub के आधिकारिक रास्तों (DMCA या सपोर्ट) का उपयोग कर सकते हैं जब यह उचित हो। यहाँ एक साफ-सुथरी योजना है, बिना टेबल के, जो पर्सनल ब्लॉग्स के लिए अच्छी तरह काम करती है।

### 1) सबसे पहले, फॉर्क करने वाले को संदेश भेजें (सबसे तेज़ रास्ता)

उनके fork पर एक issue खोलें या उन्हें ईमेल करें। यहाँ एक संक्षिप्त टेम्पलेट है जिसे आप पेस्ट कर सकते हैं:

> हाय @tornadobaflocer — इस fork में मेरे निजी नोट्स और एक्टिविटी हिस्ट्री है। मैंने यह रेपो केवल `lzwjava.github.io` डोमेन का उपयोग करने के लिए पब्लिश किया था, रीडिस्ट्रीब्यूशन के लिए नहीं। कृपया इस fork को डिलीट कर दें। मैं सोर्स को प्राइवेट बना रहा हूँ और केवल कंपाइल्ड साइट एसेट्स को पब्लिक रखूंगा।
> समझने के लिए धन्यवाद।

अगर वे इसे डिलीट कर देते हैं, तो आपका काम हो गया। अगर नहीं, तो आगे बढ़ें।

### 2) समझें कि GitHub क्या करेगा और क्या नहीं

* आपके **पब्लिक** रेपो को डिलीट या प्राइवेट करने से मौजूदा पब्लिक forks हटती **नहीं** हैं। पब्लिक forks पब्लिक ही रहती हैं और अपना अलग "नेटवर्क" बना लेती हैं। ([Stack Overflow][1])
* आप एक fork को तभी डिलीट कर सकते हैं जब आप **उस fork के एडमिन** हों (जो आप यहाँ नहीं हैं)। ([Stack Overflow][2])

### 3) अगर fork आपकी कॉपीराइटेड सामग्री को बिना अनुमति के कॉपी करता है

आप GitHub के पास DMCA टेकडाउन फाइल कर सकते हैं। यह forks में मौजूद अवैध सामग्री को हटाने का आधिकारिक रास्ता है। पॉलिसी और "how to submit" गाइड पढ़ें; वे बताते हैं कि आपको कौन सी जानकारी देनी होगी। ([GitHub Docs][3])

सुझाव: अगर आपके रेपो में **कोई लाइसेंस नहीं** था, तो डिफॉल्ट कॉपीराइट लागू होता है, जो टेकडाउन रिक्वेस्ट को मजबूत करता है (लोगों के पास पुन: उपयोग का कोई अधिकार नहीं था)। DMCA तब भी मान्य है, भले ही आपके पास कोई परमिसिव लाइसेंस था, लेकिन यह थोड़ा जटिल हो जाता है।

### 4) भविष्य में होने वाले forks को अपने सोर्स को एक्सपोज होने से रोकें

**डोमेन** को पब्लिक रखें, लेकिन **सोर्स** को प्राइवेट रखें, रेपो को अलग करके:

* **प्राइवेट सोर्स रेपो** (जैसे, `blog-source`): आपकी Jekyll/Hugo सामग्री, ड्राफ्ट, नोट्स, कॉन्फ़िग।
* **पब्लिक डिप्लॉय रेपो** जिसका नाम **`lzwjava.github.io`** हो: इसमें **केवल बिल्ट साइट** (HTML/CSS/JS) हो। कोई ड्राफ्ट नहीं, कोई हिस्ट्री नहीं।

GitHub Pages साइट्स तब भी पब्लिक होती हैं जब रेपो प्राइवेट होता है (सिवाय एंटरप्राइज क्लाउड में प्राइवेट पेजेज के)। तो एक पर्सनल ब्लॉग के लिए, दो-रेपो "डिप्लॉय ओनली" सेटअप सुरक्षित तरीका है। ([GitHub Docs][4])

डिप्लॉय के विकल्प जो आप आज इस्तेमाल कर सकते हैं:

* जनरेटर के `public/` या `docs/` आउटपुट को `lzwjava.github.io` में पुश करें। ([Quarto][5])
* या `blog-source` में एक GitHub Actions वर्कफ़्लो का उपयोग करें जो आउटपुट बनाता है और उसे `lzwjava.github.io` रेपो की डिफ़ॉल्ट ब्रांच में फोर्स-पुश करता है। (डॉक्स: "Publish from a branch" या "Publish with Actions" फ्लो चुनें।) ([GitHub Docs][6])

### 5) हिस्ट्री से कोई भी संवेदनशील सामग्री हटा दें (अपनी और बची हुई किसी भी कॉपी से)

* कोई भी एक्सपोज हुए टोकन/कीज़ को बदल दें (मान लें कि वे कम्प्रोमाइज़ हो चुके हैं)।
* हिस्ट्री को रिव्राइट करके संवेदनशील फाइलों/पाथ्स को `git filter-repo` (GitHub अब इसे रिकमेंड करता है) या BFG (कॉमन केस के लिए तेज़) से हटा दें। फिर फोर्स-पुश करें। ([GitHub Docs][7])

यह अपने आप दूसरे लोगों के forks को ठीक नहीं करेगा, लेकिन यह आपके कैननिकल रेपो को साफ करता है और यह दिखाकर कंटेंट हटा दिया गया है, किसी भी टेकडाउन क्लेम का सपोर्ट करता है।

### 6) वैकल्पिक सुरक्षा उपाय

* एक स्पष्ट LICENSE जोड़ें (अगर आप रीयूज को स्पष्ट रूप से रिस्ट्रिक्ट करना चाहते हैं)।
* README में एक डिस्क्लेमर जोड़ें: "यह रेपो केवल कंपाइल्ड साइट आउटपुट के लिए मौजूद है। कृपया सोर्स को **न** फॉर्क करें; यह प्राइवेट है।"
* अगर आप कभी किसी **ऑर्गनाइज़ेशन** में होस्ट करते हैं, तो आप प्राइवेट-रेपो फॉर्किंग को ऑर्ग-वाइड और प्रति-रेपो डिसेबल कर सकते हैं (यह पब्लिक कोड की क्लोनिंग नहीं रोकता, लेकिन प्राइवेट रेपो के लिए मददगार है)। ([GitHub Docs][8])

---

## ठोस अगले कदम (काम करने वाला क्रम)

1. @tornadobaflocer से फॉर्क डिलीट करने के लिए कहें (ऊपर दिए गए संदेश का उपयोग करें)।
2. तुरंत अपने सोर्स को एक नए **प्राइवेट** रेपो (`blog-source`) में ले जाएँ।
3. `lzwjava.github.io` को एक **पब्लिक, केवल-डिप्लॉय** रेपो बनाएं जिसमें सिर्फ बिल्ट फाइल्स हों। पेजेज को इसकी ब्रांच/फोल्डर से पब्लिश होने के लिए कॉन्फ़िगर करें। ([GitHub Docs][6])
4. अपने पुराने पब्लिक रेपो की हिस्ट्री को रिव्राइट करके संवेदनशील बिट्स हटा दें, फिर उसे आर्काइव या डिलीट कर दें। ([GitHub Docs][7])
5. अगर वे मना करते हैं और आप इसे हटवाना चाहते हैं, तो GitHub को एक **DMCA टेकडाउन** सबमिट करें। ([GitHub Docs][9])

अगर आप चाहें, तो मैं DMCA नोटिस को ठीक उस फॉर्मेट में ड्राफ्ट कर सकता हूँ जो GitHub मांगता है, और एक मिनिमल GitHub Actions वर्कफ़्लो भी जो आपकी साइट को `blog-source` से बनाता है और केवल कंपाइल्ड फाइलों को `lzwjava.github.io` में पुश करता है।

[1]: https://stackoverflow.com/questions/53052745/what-happens-to-the-forks-when-deleting-the-original-repository?utm_source=chatgpt.com "What happens to the forks when deleting the original repository?"
[2]: https://stackoverflow.com/questions/50280412/github-delete-a-fork-that-was-created-from-my-repo?utm_source=chatgpt.com "Github - Delete a fork that was created from my repo"
[3]: https://docs.github.com/articles/dmca-takedown-policy?utm_source=chatgpt.com "DMCA Takedown Policy"
[4]: https://docs.github.com/articles/creating-project-pages-manually?utm_source=chatgpt.com "Creating a GitHub Pages site"
[5]: https://quarto.org/docs/publishing/github-pages.html?utm_source=chatgpt.com "GitHub Pages"
[6]: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site?utm_source=chatgpt.com "Configuring a publishing source for your GitHub Pages site"
[7]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository?utm_source=chatgpt.com "Removing sensitive data from a repository"
[8]: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-forking-policy-for-your-repository?utm_source=chatgpt.com "Managing the forking policy for your repository"
[9]: https://docs.github.com/en/site-policy/content-removal-policies/guide-to-submitting-a-dmca-takedown-notice?utm_source=chatgpt.com "Guide to Submitting a DMCA Takedown Notice"