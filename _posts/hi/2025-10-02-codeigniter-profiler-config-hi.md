---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: कोडइग्नाइटर प्रोफाइलर कॉन्फ़िगरेशन गाइड
translated: true
type: note
---

### CodeIgniter प्रोफाइलर कॉन्फ़िगरेशन को समझना

आपके द्वारा प्रदान किया गया कोड स्निपेट CodeIgniter की `config/profiler.php` फ़ाइल (जो आमतौर पर `application/config/profiler.php` में स्थित होती है) का हेडर और टिप्पणियाँ प्रतीत होता है। यह फ़ाइल **प्रोफाइलर** को कॉन्फ़िगर करने के लिए उपयोग की जाती है, जो आपके एप्लिकेशन के प्रदर्शन को डीबग और प्रोफाइल करने के लिए CodeIgniter का एक अंतर्निहित टूल है। यह आपको पेज लोड के अंत में डेटा के विभिन्न खंडों, जैसे एक्सिक्यूशन समय, डेटाबेस क्वेरीज़ और लोड की गई कक्षाओं को प्रदर्शित (या छिपाने) की अनुमति देता है।

आपके द्वारा साझा किया गया स्निपेट सिर्फ हेडर है—जो सभी CodeIgniter कॉन्फ़िग फ़ाइलों के लिए मानक है—जिसमें आधिकारिक उपयोगकर्ता गाइड का लिंक है (हालाँकि ध्यान दें कि यदि आप उस वर्जन का उपयोग कर रहे हैं तो CodeIgniter 3 का डॉक्स अधिक प्रासंगिक हो सकता है, क्योंकि CI 4 में कुछ अंतर हैं)। नीचे, मैं CodeIgniter में **प्रोफाइलर का उपयोग और कॉन्फ़िगर करने** के तरीके को चरण दर चरण समझाऊंगा, जिसमें पूरी कॉन्फ़िग फ़ाइल का एक संपूर्ण उदाहरण भी शामिल है।

#### चरण 1: आवश्यक शर्तें
- **CodeIgniter वर्जन**: यह CI 2.x और 3.x पर लागू होता है। यदि आप CI 4 का उपयोग कर रहे हैं, तो प्रोफाइलर को `application/Config/Toolbar.php` में Debug Toolbar के माध्यम से अलग तरह से एक्सेस किया जाता है।
- **एनवायरनमेंट**: प्रोफाइलर का उद्देश्य **सिर्फ डेवलपमेंट** के लिए है (प्रोडक्शन के लिए नहीं, क्योंकि यह संवेदनशील डेटा उजागर करता है)। इसे कॉन्फ़िग फ़ाइल के माध्यम से सक्षम करें।
- **यह कैसे काम करता है**: एक बार सक्षम होने पर, प्रोफाइलर आपके पेजों के नीचे एक संकुचित डीबग पैनल जोड़ देता है, जो बेंचमार्क, क्वेरीज़ और POST डेटा जैसे मेट्रिक्स दिखाता है। इसे चलाने के लिए कस्टम कोड की आवश्यकता नहीं होती—यह सेटअप के बाद स्वचालित रूप से काम करता है।

#### चरण 2: प्रोफाइलर को कैसे सक्षम करें
1. **कॉन्फ़िग फ़ाइल ढूंढें**:
   - अपने प्रोजेक्ट में, `application/config/profiler.php` पर जाएं।
   - यदि फ़ाइल मौजूद नहीं है, तो डिफ़ॉल्ट टेम्पलेट के आधार पर इसे बनाएं।

2. **वैश्विक रूप से सक्षम करें**:
   - `application/config/profiler.php` खोलें और `$config['enable_profiler'] = TRUE;` सेट करें।
   - यह सभी अनुरोधों के लिए प्रोफाइलर को सक्षम कर देगा (आप बाद में कंट्रोलर में इसे सशर्त रूप से सक्षम/अक्षम कर सकते हैं)।

3. **कॉन्फ़िग फ़ाइल का पूरा उदाहरण**:
   मानक CI संरचना के आधार पर, पूर्ण `config/profiler.php` आमतौर पर कुछ इस तरह दिखता है (यदि यह गायब है तो आप इसे अपनी फ़ाइल में कॉपी-पेस्ट कर सकते हैं)। आपके द्वारा प्रदान किया गया स्निपेट सिर्फ शीर्ष भाग है; कॉन्फ़िग एरे उसके बाद आती है।

   ```php
   <?php
   defined('BASEPATH') OR exit('No direct script access allowed');

   /*
   | -------------------------------------------------------------------------
   | Profiler Sections
   | -------------------------------------------------------------------------
   | This file lets you determine whether or not various sections of Profiler
   | data are displayed when the Profiler is enabled.
   | Please see the user guide for info:
   |
   |    http://codeigniter.com/user_guide/general/profiling.html
   |
   */

   $config['enable_profiler'] = TRUE;  // Set to TRUE to enable, FALSE to disable globally

   // Configurable sections (set to TRUE to show, FALSE to hide)
   $config['config']         = TRUE;   // Displays all config variables
   $config['queries']        = TRUE;   // Displays all executed database queries and their execution time
   $config['get']            = TRUE;   // Displays all GET data passed to controllers
   $config['post']           = TRUE;   // Displays all POST data passed to controllers
   $config['uri_string']     = TRUE;   // Displays the requested URI string
   $config['controller_info'] = TRUE;  // Displays controller and method information
   $config['models']         = TRUE;   // Displays details about loaded models
   $config['libraries']      = TRUE;   // Displays details about loaded libraries
   $config['helpers']        = TRUE;   // Displays details about loaded helpers
   $config['memory_usage']   = TRUE;   // Shows memory usage
   $config['elapsed_time']   = TRUE;   // Shows total execution time
   $config['benchmarks']     = TRUE;   // Shows benchmark data
   $config['http_headers']   = TRUE;   // Displays HTTP headers
   $config['session_data']   = TRUE;   // Displays session data

   /* End of file profiler.php */
   /* Location: ./application/config/profiler.php */
   ```

   - **मुख्य सेटिंग्स**:
     - `$config['enable_profiler']`: मास्टर स्विच।
     - प्रत्येक सेक्शन (जैसे, `config['queries']`) दृश्यता को नियंत्रित करता है। आप जो डीबग करना चाहते हैं उसके आधार पर `TRUE`/`FALSE` सेट करें।

4. **सशर्त सक्षम करना (वैकल्पिक)**:
   - आपको इसे वैश्विक रूप से सक्षम करने की आवश्यकता नहीं है। एक कंट्रोलर में, आप इसका उपयोग कर सकते हैं:
     ```php
     $this->output->enable_profiler(TRUE);  // इस विशिष्ट मेथड/अनुरोध के लिए सक्षम करें
     $this->output->enable_profiler(FALSE); // अक्षम करें
     ```
   - यह उस पेज के लिए वैश्विक कॉन्फ़िग को ओवरराइड कर देता है।

#### चरण 3: प्रोफाइलर का व्यवहारिक उपयोग कैसे करें
1. **आउटपुट तक पहुँचना**:
   - अपने ऐप में कोई भी पेज लोड करें (जैसे, एक कंट्रोलर मेथड)।
   - नीचे स्क्रॉल करें—प्रोफाइलर "Elapsed Time," "Database Queries," आदि जैसे सेक्शन के साथ एक संकुचित बॉक्स के रूप में दिखाई देगा।
   - दृश्यता टॉगल करने के लिए "Close" या "Open" पर क्लिक करें।

2. **प्रत्येक सेक्शन क्या दिखाता है**:
   - **बेंचमार्क**: आपके कोड के विभिन्न हिस्सों के लिए CPU समय (ऑप्टिमाइज़ेशन के लिए उपयोगी)।
   - **क्वेरीज़**: चलाई गई सभी SQL क्वेरीज़, जिसमें एक्सिक्यूशन समय और एरर शामिल हैं (DB समस्याओं को डीबग करने के लिए बढ़िया)।
   - **POST/GET**: सबमिट किया गया फॉर्म डेटा, फॉर्म वैलिडेशन के लिए सहायक।
   - **मेमोरी यूसेज**: आपकी स्क्रिप्ट ने कितनी RAM का उपयोग किया (लीक के लिए मॉनिटर करें)।
   - उदाहरण: यदि कोई पेज धीमा है, तो बॉटलनेक की पहचान करने के लिए `benchmarks` और `queries` को सक्षम करें।

3. **कस्टम बेंचमार्किंग**:
   - विशिष्ट ब्लॉकों को समय देने के लिए अपने कोड में कस्टम मार्कर जोड़ें:
     ```php
     $this->benchmark->mark('query_start');  // टाइमर शुरू करें
     // आपका कोड यहाँ (जैसे, एक foreach लूप या DB क्वेरी)
     $this->benchmark->mark('query_end');    // टाइमर समाप्त करें
     ```
   - यह स्वचालित रूप से "Benchmarks" सेक्शन में दिखाई देगा।

4. **एक कंट्रोलर में उदाहरण उपयोग**:
   मान लीजिए आपके पास एक कंट्रोलर मेथड है जो धीमी है—आप उसे डीबग करने के लिए वहाँ प्रोफाइलर सक्षम कर सकते हैं:
   ```php
   class Example extends CI_Controller {
       public function index() {
           $this->load->database();
           $this->output->enable_profiler(TRUE);  // सिर्फ इस पेज के लिए सक्षम करें

           // आपका लॉजिक यहाँ, जैसे, डेटा फ़ेच करना
           $data['results'] = $this->db->get('users')->result();
           $this->load->view('example_view', $data);
       }
   }
   ```
   - इस पेज को लोड करने के बाद, प्रोफाइलर डेटा के लिए नीचे देखें।

#### चरण 4: सुझाव और समस्या निवारण
- **सुरक्षा नोट**: प्रोडक्शन में कभी सक्षम न करें—`$config['enable_profiler'] = FALSE;` के माध्यम से या एनवायरनमेंट वेरिएबल का उपयोग करके अक्षम करें (जैसे, DEV एनवायरनमेंट के लिए हुक्स के माध्यम से)।
- **सामान्य समस्याएं**:
  - दिख नहीं रहा? सुनिश्चित करें कि `$config['enable_profiler']` TRUE है और आप प्रोडक्शन सर्वर पर नहीं हैं।
  - एरर? जांचें कि क्या आपकी `view` फ़ाइलों में उचित क्लोजिंग टैग हैं (जैसे, `</html>`)।
- **उन्नत**: अधिक नियंत्रण के लिए, IP या एनवायरनमेंट के आधार पर सशर्त रूप से सक्षम करने के लिए `config/hooks.php` में **हुक्स** का उपयोग करें।
- **संसाधन**:
  - आधिकारिक डॉक्स: [CodeIgniter 3 प्रोफाइलिंग](https://codeigniter.com/user_guide/general/profiling.html) या [CI 4 डीबगिंग](https://codeigniter.com/user_guide/testing/debugging.html)।
  - यदि आप CI 4 का उपयोग कर रहे हैं, तो इसके बजाय Debug Toolbar पर स्विच करें (जो `Toolbar.php` में सक्षम है)।

यदि यह आपके इरादे से मेल नहीं खाता (जैसे, यदि आपके पास कोई अलग कॉन्फ़िग या एरर है), तो अपना पूरा कोड या CI वर्जन जैसे अधिक संदर्भ प्रदान करें, और मैं जवाब को परिष्कृत कर दूंगा!