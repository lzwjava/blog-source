---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: कोडइग्नाइटर स्माइली हेल्पर कॉन्फ़िगरेशन
translated: true
type: note
---

### अवलोकन
यह CodeIgniter वेब फ्रेमवर्क की एक PHP कॉन्फ़िगरेशन फ़ाइल है, विशेष रूप से इसके **इमोटिकॉन्स/स्माइलीज़ हेल्पर** के लिए। CodeIgniter वेब ऐप्स बनाने के लिए एक PHP MVC फ्रेमवर्क है। यह फ़ाइल स्माइली/इमोटिकॉन मैपिंग का एक सेट परिभाषित करती है, जिसका उपयोग फ्रेमवर्क का `smiley_helper` टेक्स्ट-आधारित इमोटिकॉन्स (जैसे `:-)`) को स्वचालित रूप से HTML `<img>` टैग में बदलने के लिए करता है, जो संबंधित GIF छवियां प्रदर्शित करते हैं।

फ़ाइल यह सुनिश्चित करती है कि `defined('BASEPATH') OR exit('No direct script access allowed');` के माध्यम से सीधी पहुंच अवरुद्ध हो, यह CodeIgniter में एक सुरक्षा उपाय है जिसका उद्देश्य अनधिकृत सीधी स्क्रिप्ट एक्सेक्यूशन को रोकना है।

### मुख्य घटक
- **उद्देश्य**: यूजर-जनित सामग्री (जैसे फोरम पोस्ट या टिप्पणियों) में सादे टेक्स्ट इमोटिकॉन्स को बेहतर यूजर अनुभव के लिए दृश्य छवियों में परिवर्तित करना।
- **डेटा संरचना**: `$smileys` एक PHP साहचर्य सरणी है जिसकी औपचारिक संरचना इस प्रकार है:
  ```
  $smileys = array(
      'smiley_code' => array('image_file', 'width', 'height', 'alt_text'),
      // ...
  );
  ```
  - **smiley_code**: मिलान किया जाने वाला टेक्स्ट पैटर्न (जैसे `:-)`, `:lol:`, `>:(`)।
  - **image_file**: स्माइली डायरेक्टरी में GIF छवि का नाम (CodeIgniter में डिफ़ॉल्ट रूप से `application/views/smileys/`)।
  - **width/height**: `<img>` टैग के लिए पिक्सेल में आयाम (यहां सभी `'19'` हैं, जो 19x19px GIFs इंगित करता है)।
  - **alt_text**: पहुंच योग्यता/स्क्रीन रीडर के लिए वैकल्पिक पाठ, जो भावना का वर्णन करता है।

- **CodeIgniter में उपयोग**: हेल्पर को `$this->load->helper('smiley');` के साथ लोड करें, फिर इमोटिकॉन कोड वाले स्ट्रिंग्स पर `parse_smileys($text)` जैसे फ़ंक्शन को कॉल करें। यह कोड को `<img>` टैग से बदल देता है, उदाहरण के लिए:
  - इनपुट: `I'm happy :)`
    आउटपुट: `I'm happy <img src="http://example.com/smileys/smile.gif" width="19" height="19" alt="smile">`

### एंट्रीज का विवरण
सरणी में 40+ मैपिंग शामिल हैं जो भावना के प्रकार के आधार पर समूहीकृत हैं। अधिकांश छवियां 19x19px GIFs हैं। यहां एक संक्षिप्त दृश्य दिया गया है (उदाहरणों के साथ):

| स्माइली कोड | छवि | Alt टेक्स्ट | नोट्स |
|---------------|-------|----------|-------|
| `:-)`, `:)` | grin.gif, smile.gif | grin, smile | सकारात्मक मुस्कुराहट। |
| `:lol:`, `:cheese:` | lol.gif, cheese.gif | LOL, cheese | हंसना, चीज़ी ग्रिन। |
| `;-)`, `;)` | wink.gif | wink | आंख मारना। |
| `:smirk:`, `:roll:` | smirk.gif, rolleyes.gif | smirk, rolleyes | व्यंग्य। |
| `:-S`, `:wow:`, `:bug:` | confused.gif, surprise.gif, bigsurprise.gif | confused, surprised, big surprise | भ्रम/आश्चर्य। |
| `:-P`, `%-P`, `;-P`, `:P` | tongue_laugh.gif, etc. | tongue laugh, etc. | जीभ बाहर निकाले वाले वेरिएंट। |
| `:blank:`, `:long:`, `:ohh:`, `:grrr:`, `:gulp:`, `8-/` | Various | blank stare, long face, ohh, grrr, gulp, oh oh | तटस्थ या नाराज चेहरे। |
| `:down:`, `:red:`, `:sick:`, `:shut:` | Various | downer, red face, sick, shut eye | उदास, शर्मिंदा, बीमार। |
| `:-/`, `>:(` (`:mad:`), `>:-(` (`:angry:`) | hmm.gif, mad.gif, angry.gif | hmmm, mad, angry | भ्रमित, नाराज, गुस्सा। |
| `:zip:`, `:kiss:` | zip.gif, kiss.gif | zipper, kiss | ज़िप माउथ किस। |
| `:ahhh:`, `:coolsmile:`, `-:coolsmirk:`, `:coolgrin:`, `:coolhmm:`, `:coolmad:`, `:coolcheese:` | shock.gif, shade_smile.gif, etc. | shock, cool smile, cool smirk, cool grin, cool hmm, cool mad, cool cheese | हैरान या "कूल"/सनग्लास वेरिएंट। |
| `:vampire:`, `:snake:` | vampire.gif, snake.gif | vampire, snake | थीम्ड इमोटिकॉन्स। |
| `:exclaim:`, `:question:` | exclaim.gif, question.gif | exclaim, question | विराम चिह्न समकक्ष (!, ?)। |

### विस्तार और अनुकूलन
- **स्माइलीज़ जोड़ना**: नई एंट्रीज़ जोड़ें, उदाहरण के लिए, `':fire:' => array('fire.gif', '19', '19', 'fire');`।
- **छवियां बदलना**: यदि GIFs को PNGs/JPGs से बदल रहे हैं तो फ़ाइल नाम अपडेट करें (तदनुसार width/height एडजस्ट करें)।
- **डायरेक्टरी**: सुनिश्चित करें कि छवियां CodeIgniter के स्माइली पथ में मौजूद हैं।
- **सीमाएं**: यहां सभी छवियां एक ही आकार की हैं; वास्तविक कार्यान्वयन में भिन्नता हो सकती है। यह सरणी केवल मैपिंग को परिभाषित करती है—प्रतिस्थापन तर्क हेल्पर में ही है।

यदि CodeIgniter में इसे अनुकूलित करने या उपयोग करने के बारे में आपका कोई विशिष्ट प्रश्न है, तो कृपया अधिक विवरण प्रदान करें!