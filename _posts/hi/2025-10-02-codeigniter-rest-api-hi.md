---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: कोडइग्नाइटर रेस्ट एपीआई कॉन्फ़िगरेशन गाइड
translated: true
type: note
---

नीचे, मैं आपके द्वारा साझा किए गए CodeIgniter REST API कॉन्फ़िगरेशन फ़ाइल (`application/config/rest.php`) को समझने और उपयोग करने के लिए एक स्पष्ट, चरण-दर-चरण मार्गदर्शिका प्रदान करूंगा। यह फ़ाइल REST_Controller लाइब्रेरी (CodeIgniter में RESTful API बनाने के लिए एक लोकप्रिय PHP लाइब्रेरी) के व्यवहार को कॉन्फ़िगर करती है, जैसे कि Phil Sturgeon की REST लाइब्रेरी (अब कुछ संस्करणों में CodeIgniter फ्रेमवर्क के हिस्से के रूप में मेंटेन की जाती है)।

मैं समझाऊंगा:
- लाइब्रेरी क्या करती है और मुख्य पूर्वापेक्षाएँ।
- इसे कैसे सेट अप करें और उपयोग करें।
- आपकी फ़ाइल से मुख्य कॉन्फ़िगरेशन विकल्प (उदाहरणों के साथ)।
- एक सरल उपयोग उदाहरण।
- सामान्य समस्याओं और सुरक्षा के लिए सुझाव।

यदि आपका प्रश्न किसी विशेष पहलू (जैसे, प्रमाणीकरण या सीमाएँ) के बारे में है, तो अधिक लक्षित सलाह के लिए कृपया स्पष्ट करें!

### 1. **पूर्वापेक्षाएँ और सेटअप**
   - **यह क्या है?** यह CodeIgniter (एक PHP फ्रेमवर्क) के लिए REST_Controller लाइब्रेरी है। यह आपको `REST_Controller` से अपने कंट्रोलर का विस्तार करके RESTful API (जैसे, एंडपॉइंट जो GET/POST अनुरोधों पर JSON/XML में प्रतिक्रिया देते हैं) बनाने देती है। आपकी कॉन्फ़िग फ़ाइल प्रमाणीकरण, प्रतिक्रिया प्रारूप, दर सीमित करना और सुरक्षा जैसे वैश्विक सेटिंग्स को नियंत्रित करती है।
   
   - **आवश्यकताएँ:**
     - CodeIgniter 3.x (या संगत संस्करण; यह कॉन्फ़िग लगभग 3.x के पुराने संस्करणों के लिए है)।
     - REST_Controller लाइब्रेरी इंस्टॉल करें यदि यह पहले से आपके CodeIgniter इंस्टॉल में नहीं है (आप इसे GitHub से डाउनलोड कर सकते हैं: `chriskacerguis/codeigniter-restserver`)। लाइब्रेरी फ़ाइलों को `application/libraries/` में रखें और `application/config/autoload.php` में इसे ऑटोलोड करें:
       ```php
       $autoload['libraries'] = ['rest_controller'];
       ```
     - डेटाबेस सेटअप (वैकल्पिक; API कुंजी, लॉगिंग, या सीमाएँ जैसी सुविधाओं के लिए आवश्यक)। कॉन्फ़िग टिप्पणियों में दिए गए SQL स्कीमा चलाएँ (जैसे, `keys`, `logs`, `access`, `limits` जैसी टेबलों के लिए)।
     - CodeIgniter में साफ़ API एंडपॉइंट्स (जैसे `/api/users`) के लिए प्रीटी URL सक्षम करें (`application/config/routes.php`)।
     - आपकी `rest.php` कॉन्फ़िग फ़ाइल `application/config/` में रखी जानी चाहिए और `application/config/autoload.php` में ऑटोलोड की जानी चाहिए:
       ```php
       $autoload['config'] = ['rest'];
       ```

   - **मूल इंस्टॉलेशन चरण:**
     1. CodeIgniter डाउनलोड करें और अनज़िप करें।
     2. REST_Controller लाइब्रेरी फ़ाइलें जोड़ें।
     3. आपके द्वारा प्रदान की गई `rest.php` को `application/config/` में कॉपी करें।
     4. `routes.php` में रूट्स सेट करें (उदाहरण के लिए, `/api/users` को एक कंट्रोलर पर मैप करने के लिए `$route['api/(:any)'] = 'api/$1';`)।
     5. API कंट्रोलर बनाएँ (नीचे उदाहरण देखें)।
     6. Postman या curl जैसे टूल से टेस्ट करें।

### 2. **मुख्य कॉन्फ़िगरेशन विकल्प**
मैं आपकी कॉन्फ़िग फ़ाइल से मुख्य सेटिंग्स का सारांश दूंगा, जिन्हें उद्देश्य के आधार पर समूहीकृत किया गया है। ये वैश्विक व्यवहार को नियंत्रित करती हैं। आप अपनी आवश्यकताओं के अनुरूप उन्हें संशोधित कर सकते हैं (उदाहरण के लिए, HTTPS सक्षम करें या डिफ़ॉल्ट प्रारूप बदलें)।

- **प्रोटोकॉल और आउटपुट:**
  - `$config['force_https'] = FALSE;`: सभी API कॉल को HTTPS का उपयोग करने के लिए मजबूर करता है। प्रोडक्शन सुरक्षा के लिए `TRUE` सेट करें।
  - `$config['rest_default_format'] = 'json';`: डिफ़ॉल्ट प्रतिक्रिया प्रारूप (विकल्प: json, xml, csv, आदि)। अनुरोध URL के माध्यम से ओवरराइड कर सकते हैं (उदाहरण के लिए, `/api/users.format=xml`)।
  - `$config['rest_supported_formats']`: अनुमत प्रारूपों की सूची। सुरक्षा के लिए अवांछित ones को हटा दें।
  - `$config['rest_ignore_http_accept'] = FALSE;`: प्रतिक्रियाओं को तेज करने के लिए क्लाइंट HTTP Accept हेडर को अनदेखा करें (उपयोगी यदि आप कोड में हमेशा `$this->rest_format` का उपयोग करते हैं)।

- **प्रमाणीकरण (सुरक्षा):**
  - `$config['rest_auth'] = FALSE;`: मुख्य auth मोड। विकल्प:
    - `FALSE`: कोई auth आवश्यक नहीं।
    - `'basic'`: HTTP Basic Auth (बेस64 हेडर में उपयोगकर्ता नाम/पासवर्ड)।
    - `'digest'`: अधिक सुरक्षित डाइजेस्ट auth।
    - `'session'`: PHP session वेरिएबल के लिए जाँच करें।
  - `$config['auth_source'] = 'ldap';`: क्रेडेंशियल्स कहाँ जाँचें (उदाहरण के लिए, config array, LDAP, कस्टम लाइब्रेरी)।
  - `$config['rest_valid_logins'] = ['admin' => '1234'];`: सरल उपयोगकर्ता नाम/पासवर्ड array (यदि LDAP का उपयोग कर रहे हैं तो अनदेखा की जाती है)।
  - `$config['auth_override_class_method']`: विशिष्ट कंट्रोलर/मेथड के लिए auth ओवरराइड करें (उदाहरण के लिए, `'users' => 'view' => 'basic'`)।
  - `$config['auth_library_class/function']`: यदि कस्टम लाइब्रेरी का उपयोग कर रहे हैं, तो सत्यापन के लिए क्लास/मेथड निर्दिष्ट करें।
  - IP नियंत्रण:
    - `$config['rest_ip_whitelist_enabled/blacklist_enabled']`: आपके API पर आधारित IP फ़िल्टरिंग।
    - एक्सेस प्रतिबंधित करने के लिए उपयोगी (उदाहरण के लिए, अपने ऐप के IPs को व्हाइटलिस्ट करें)।

- **API कुंजियाँ (वैकल्पिक सुरक्षा परत):**
  - `$config['rest_enable_keys'] = FALSE;`: API key जाँच सक्षम करता है (DB टेबल `keys` में संग्रहीत)। क्लाइंट को हेडर में कुंजी भेजनी होगी (उदाहरण के लिए, `X-API-KEY`)।
  - `$config['rest_key_column/name/length']`: key फ़ील्ड्स और हेडर नाम कस्टमाइज़ करें।
  - विशिष्ट कंट्रोलर/मेथड तक कुंजी प्रतिबंधित करने के लिए `$config['rest_enable_access']` के साथ जोड़ें।

- **लॉगिंग और सीमाएँ:**
  - `$config['rest_enable_logging/limits'] = FALSE;`: अनुरोधों (URI, params, आदि) के DB-आधारित लॉगिंग या दर सीमित करना (उदाहरण के लिए, प्रति key प्रति घंटे X कॉल) सक्षम करें।
  - टेबल्स: `logs`, `limits` (उन्हें बनाने के लिए टिप्पणियों में दिए गए SQL चलाएँ)।
  - `$config['rest_limits_method']`: सीमाएँ कैसे लागू करें (API key, URL, आदि द्वारा)।
  - कंट्रोलर में प्रति मेथड कस्टमाइज़ करें (उदाहरण के लिए, `$this->method['get']['limit'] = 100;`)।

- **अन्य:**
  - `$config['rest_ajax_only'] = FALSE;`: केवल AJAX अनुरोधों तक सीमित करें (अन्यथा 505 त्रुटि देता है)।
  - `$config['rest_language'] = 'english';`: त्रुटि संदेशों के लिए भाषा।

संशोधित करने के लिए: `rest.php` संपादित करें और अपना ऐप रीस्टार्ट करें। परिवर्तनों का सावधानीपूर्वक परीक्षण करें!

### 3. **इसे कैसे उपयोग करें: चरण-दर-चरण उपयोग**
एक बार सेटअप हो जाने पर, ऐसे कंट्रोलर बनाकर API एंडपॉइंट्स बनाएँ जो `REST_Controller` का विस्तार करते हों। यहाँ एक उच्च-स्तरीय प्रक्रिया है:

1. **एक कंट्रोलर बनाएँ:**
   - `application/controllers/` में, `Api.php` बनाएँ (या उदाहरण के लिए, किसी विशिष्ट संसाधन के लिए `Users.php`):
     ```php
     <?php
     defined('BASEPATH') OR exit('No direct script access allowed');
     require_once(APPPATH . 'libraries/REST_Controller.php');

     class Api extends REST_Controller {
         public function __construct() {
             parent::__construct();
             // वैकल्पिक: प्रति मेथड auth, सीमाएँ सेट करें
             $this->load->database();
             $this->method['index_get']['limit'] = 100; // 100 requests/hour
         }

         // GET /api
         public function index_get() {
             $data = ['message' => 'Welcome to the API', 'status' => 'success'];
             $this->response($data, REST_Controller::HTTP_OK);
         }

         // POST /api/users
         public function users_post() {
             $data = $this->input->post(); // POST डेटा प्राप्त करें
             if (empty($data['name'])) {
                 $this->response(['error' => 'Name required'], REST_Controller::HTTP_BAD_REQUEST);
             }
             // प्रक्रिया करें (उदाहरण के लिए, DB में इन्सर्ट करें)
             $this->response(['message' => 'User created'], REST_Controller::HTTP_CREATED);
         }

         // PUT /api/users/{id}
         public function users_put($id) {
             $data = $this->put(); // PUT डेटा प्राप्त करें
             // $id वाले user को अपडेट करें
             $this->response(['message' => 'User updated'], REST_Controller::HTTP_OK);
         }

         // DELETE आदि के लिए
     }
     ```

2. **अनुरोध भेजें:**
   - कोई भी HTTP क्लाइंट उपयोग करें:
     - GET: `curl http://yourdomain.com/api` → JSON लौटाता है {"message": "Welcome to the API", "status": "success"}
     - POST: `curl -X POST http://yourdomain.com/api/users -d "name=John"` → एक user बनाता है।
   - यदि auth/keys का उपयोग कर रहे हैं तो हेडर शामिल करें (उदाहरण के लिए, `Authorization: Basic base64(user:pass)` या `X-API-KEY: yourkey`)।

3. **परीक्षण और डीबग करें:**
   - त्रुटियों के लिए CodeIgniter लॉग्स जाँचें।
   - यदि auth विफल होता है, तो सुनिश्चित करें कि क्रेडेंशियल्स सही ढंग से सेट हैं।
   - सीमाओं/लॉगिंग के लिए, अपनी DB टेबल्स क्वेरी करें।

### 4. **सामान्य सुझाव और सर्वोत्तम अभ्यास**
- **सुरक्षा:** प्रोडक्शन में हमेशा HTTPS का उपयोग करें (`force_https = TRUE`)। यदि बाहरी क्लाइंट को एक्सपोज़ कर रहे हैं तो keys सक्षम करें। SQL इंजेक्शन को रोकने के लिए इनपुट सैनिटाइज़ करें।
- **त्रुटियाँ:** प्रतिक्रियाओं में `status` और `error` फ़ील्ड शामिल होते हैं (कॉन्फ़िग में अनुकूलन योग्य)। डीबगिंग के लिए CodeIgniter के प्रोफाइलर का उपयोग करें।
- **प्रदर्शन:** यदि लॉगिंग/सीमाएँ सक्षम हैं, तो आपका DB क्वेरीज़ को संभालेगा—धीमे प्रदर्शन के लिए निगरानी करें।
- **अपग्रेड करना:** यह कॉन्फ़िग CodeIgniter के पुराने संस्करणों के लिए है। CI 4 के लिए, उनके बिल्ट-इन API संसाधनों का उपयोग करें (इस सेटअप को ट्वीक्स की आवश्यकता हो सकती है)।
- **समस्या निवारण:**
  - "कोई प्रतिक्रिया नहीं"? रूट्स, ऑटोलोड, और लाइब्रेरी पथ जाँचें।
  - Auth समस्याएँ? `$auth_source` और क्रेडेंशियल्स सत्यापित करें।
  - प्रारूप त्रुटियाँ? सुनिश्चित करें कि आपका प्रारूप `rest_supported_formats` में है।
- **संसाधन:** codeigniter-restserver.org पर दस्तावेज़। CI4 माइग्रेशन के लिए, आधिकारिक दस्तावेज़ देखें।

यदि यह आपके सटीक प्रश्न का उत्तर नहीं देता है या आपको किसी विशिष्ट उपयोग के मामले (जैसे, OAuth सक्षम करना) के लिए कोड चाहिए, तो अधिक विवरण प्रदान करें!