---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: ड्रॉपडाउन दृश्यता और विकल्प
translated: true
type: note
---

प्रदत्त HTML स्निपेट में, आप `<select>` एलिमेंट्स का उपयोग कर रहे हैं, जो डिफ़ॉल्ट रूप से ड्रॉपडाउन मेन्यू के रूप में रेंडर होते हैं। इसका मतलब है कि उपयोगकर्ता एक नज़र में केवल वर्तमान में चुने गए विकल्प को देख सकते हैं—अन्य विकल्प तब तक छिपे रहते हैं जब तक ड्रॉपडाउन पर क्लिक नहीं किया जाता या उसे विस्तारित नहीं किया जाता (कीबोर्ड/माउस इंटरैक्शन के माध्यम से)। यह HTML में `<select>` के लिए मानक व्यवहार है, क्योंकि इसे UI को अव्यवस्थित किए बिना सूची से कॉम्पैक्ट चयन के लिए डिज़ाइन किया गया है।

HTML में विकल्पों की दृश्यता को टॉगल करने के लिए एक अंतर्निहित "स्विच" एलिमेंट नहीं है। हालाँकि, आप जो वर्णन कर रहे हैं (ड्रॉपडाउन के बिना सभी विकल्पों को दृश्यमान बनाना, या उन्हें दिखाने/छिपाने के लिए एक टॉगल प्रदान करना) प्राप्त करने के कुछ तरीके हैं। मैं नीचे पेशेवरों/विपक्षों और कोड उदाहरणों की रूपरेखा प्रस्तुत करूंगा। ये दृष्टिकोण संभव होने पर मूल HTML/CSS का उपयोग करते हैं, जिसमें इंटरैक्टिविटी के लिए वैकल्पिक JavaScript शामिल है। चूंकि आपका कोड एक Jekyll साइट (Liquid टेम्प्लेटिंग के आधार पर) का हिस्सा प्रतीत होता है, इसलिए इन्हें आसानी से एकीकृत किया जाना चाहिए।

### 1. **`<select>` के बजाय रेडियो बटन का उपयोग करें (हमेशा दृश्यमान विकल्प)**
   - **क्यों?** रेडियो बटन (`<input type="radio">`) सभी विकल्पों को इनलाइन या सूची में प्रदर्शित करते हैं, जिससे वे किसी भी इंटरैक्शन के बिना पूरी तरह से दृश्यमान हो जाते हैं। यह छोटी सूचियों (जैसे आपके type-select में 2 विकल्प) के लिए बहुत अच्छा है लेकिन लंबी सूचियों (जैसे आपके language-sort में 9 विकल्प) के लिए जगह घेर सकता है।
   - **पेशेवर:** JS की आवश्यकता नहीं; सुलभ; उपयोगकर्ता तुरंत सब कुछ देख सकते हैं।
   - **विपक्ष:** अधिक जगह लेता है; यदि आपको एक्शन ट्रिगर करने की आवश्यकता हो (जैसे, पोस्ट्स को सॉर्ट/फ़िल्टर करना) तो "चयन" लॉजिक को संभालने के लिए JS की आवश्यकता होती है।
   - **उदाहरण कोड:**
     अपने `<select>` को रेडियो बटन के एक समूह से बदलें। शब्दार्थ/सुलभता के लिए उन्हें एक `<fieldset>` में लपेटें।

     ```html
     <div class="sort-container">
       <!-- रेडियो बटन के रूप में प्रकार चयन -->
       <fieldset>
         <legend>प्रकार</legend>
         <label>
           <input type="radio" name="type" value="posts" checked> Posts
         </label>
         <label>
           <input type="radio" name="type" value="notes"> Notes
         </label>
       </fieldset>

       <!-- रेडियो बटन के रूप में भाषा सॉर्ट -->
       <fieldset>
         <legend>भाषा के अनुसार क्रमबद्ध करें</legend>
         <label>
           <input type="radio" name="sort" value="en" checked> English
         </label>
         <label>
           <input type="radio" name="sort" value="zh"> 中文
         </label>
         <label>
           <input type="radio" name="sort" value="ja"> 日本語
         </label>
         <!-- es, hi, fr, de, ar, hant के लिए और लेबल जोड़ें -->
       </fieldset>

       <div>
         <span id="post-number" class="post-number">
           {{ site[type].size }} {{ type }}
           ({{ site[type].size | divided_by: 7 | times: 6 }} <a href="https://openrouter.ai">AI</a> द्वारा अनुवादित)
         </span>
       </div>
     </div>
     ```

     - स्टाइलिंग के लिए CSS जोड़ें (उदाहरण के लिए, उन्हें बटन जैसा दिखाने के लिए):
       ```css
       fieldset {
         border: none; /* डिफ़ॉल्ट बॉर्डर हटाएं */
         display: flex;
         gap: 10px;
       }
       label {
         background: #f0f0f0;
         padding: 5px 10px;
         border-radius: 5px;
         cursor: pointer;
       }
       input[type="radio"] {
         appearance: none; /* डिफ़ॉल्ट रेडियो सर्कल छिपाएं */
       }
       input[type="radio"]:checked + span { /* यदि टेक्स्ट के लिए लेबल के अंदर <span> का उपयोग कर रहे हैं */
         background: #007bff;
         color: white;
       }
       ```
     - कार्यक्षमता के लिए: UI अपडेट करने या सॉर्ट ट्रिगर करने के लिए परिवर्तन सुनने के लिए JS का उपयोग करें (जैसे, `addEventListener('change')`).

### 2. **क्लिक करने योग्य विकल्पों के लिए बटन या Div का उपयोग करें (कस्टम "बटन ग्रुप")**
   - **क्यों?** यदि आप एक अधिक बटन जैसा इंटरफ़ेस चाहते हैं, तो बटन के रूप में स्टाइल किए गए `<button>` या `<div>` एलिमेंट्स का उपयोग करें। यह सभी विकल्पों को स्पष्ट रूप से दिखाता है और कस्टम टॉगलिंग की अनुमति देता है।
   - **पेशेवर:** लचीली स्टाइलिंग; टैब या पिल्स की नकल कर सकता है; रिस्पॉन्सिव बनाना आसान।
   - **विपक्ष:** सक्रिय स्टेट और एक्शन को प्रबंधित करने के लिए JS की आवश्यकता होती है; फॉर्म एलिमेंट्स जितना शब्दार्थ रूप से सही नहीं (सुलभता के लिए ARIA विशेषताओं का उपयोग करें)।
   - **उदाहरण कोड:**
     ```html
     <div class="sort-container">
       <!-- बटन ग्रुप के रूप में प्रकार -->
       <div class="button-group" role="group" aria-label="प्रकार चयन">
         <button data-type="posts" class="active">Posts</button>
         <button data-type="notes">Notes</button>
       </div>

       <!-- बटन ग्रुप के रूप में भाषा -->
       <div class="button-group" role="group" aria-label="भाषा चयन">
         <button data-sort="en" class="active">English</button>
         <button data-sort="zh">中文</button>
         <button data-sort="ja">日本語</button>
         <!-- अन्य भाषाओं के लिए और बटन जोड़ें -->
       </div>

       <div>
         <span id="post-number" class="post-number">
           {{ site[type].size }} {{ type }}
           ({{ site[type].size | divided_by: 7 | times: 6 }} <a href="https://openrouter.ai">AI</a> द्वारा अनुवादित)
         </span>
       </div>
     </div>
     ```

     - बटन स्टाइलिंग के लिए CSS:
       ```css
       .button-group {
         display: flex;
         gap: 5px;
         flex-wrap: wrap; /* लंबी सूचियों के लिए */
       }
       button {
         padding: 5px 10px;
         border: 1px solid #ccc;
         border-radius: 5px;
         cursor: pointer;
       }
       button.active {
         background: #007bff;
         color: white;
       }
       ```
     - क्लिक को हैंडल करने के लिए JS (इसे एक `<script>` टैग या एक्सटर्नल फ़ाइल में जोड़ें):
       ```javascript
       document.querySelectorAll('.button-group button').forEach(button => {
         button.addEventListener('click', function() {
           // सिबलिंग्स से active क्लास हटाएं
           this.parentNode.querySelectorAll('button').forEach(btn => btn.classList.remove('active'));
           this.classList.add('active');
           // यहां अपनी सॉर्ट लॉजिक ट्रिगर करें, उदाहरण के लिए, post-number अपडेट करें या कंटेंट फ़िल्टर करें
           console.log('चयनित:', this.dataset.type || this.dataset.sort);
         });
       });
       ```

### 3. **विकल्पों को विस्तारित करने के लिए एक टॉगल/स्विच जोड़ें (हाइब्रिड दृष्टिकोण)**
   - **क्यों?** यदि आप कॉम्पैक्ट `<select>` को बनाए रखना चाहते हैं लेकिन उपयोगकर्ताओं को सभी विकल्प दिखाने वाले व्यू में "स्विच" करने की अनुमति देना चाहते हैं, तो विस्तारित सूची की दृश्यता को दिखाने/छिपाने के लिए टॉगल स्विच के रूप में स्टाइल किए गए `<input type="checkbox">` का उपयोग करें।
   - **पेशेवर:** डिफ़ॉल्ट कॉम्पैक्टनेस बनाए रखता है; टॉगल के लिए मूल HTML।
   - **विपक्ष:** CSS/JS की आवश्यकता होती है; जटिलता बढ़ाता है।
   - **उदाहरण:** स्विच के लिए `<input type="checkbox">` का उपयोग करें, और सभी विकल्पों वाले एक div की दृश्यता टॉगल करें।
     ```html
     <div class="sort-container">
       <!-- आपके मूल select यहां -->

       <!-- टॉगल स्विच -->
       <label class="switch">
         <input type="checkbox" id="show-all-toggle">
         <span>सभी विकल्प दिखाएं</span>
       </label>

       <!-- छिपा हुआ विस्तारित व्यू -->
       <div id="expanded-options" style="display: none;">
         <!-- सभी प्रकार और सॉर्ट विकल्पों को सादे टेक्स्ट या बटन के रूप में सूचीबद्ध करें -->
         <ul>
           <li>Posts</li>
           <li>Notes</li>
           <li>English</li>
           <li>中文</li>
           <!-- आदि -->
         </ul>
       </div>

       <!-- आपका post-number span -->
     </div>
     ```

     - स्विच के लिए CSS:
       ```css
       .switch input {
         opacity: 0;
         width: 0;
         height: 0;
       }
       .switch span {
         /* टॉगल स्लाइडर के रूप में स्टाइल करें */
         position: relative;
         display: inline-block;
         width: 40px;
         height: 20px;
         background: #ccc;
         border-radius: 20px;
         transition: background 0.3s;
       }
       .switch input:checked + span {
         background: #007bff;
       }
       /* ::before या ::after के साथ एक स्लाइडर नॉब जोड़ें */
       ```
     - टॉगल करने के लिए JS:
       ```javascript
       document.getElementById('show-all-toggle').addEventListener('change', function() {
         document.getElementById('expanded-options').style.display = this.checked ? 'block' : 'none';
       });
       ```

### सिफारिशें
- आपके **type-select** (केवल 2 विकल्प) के लिए, रेडियो बटन या बटन अच्छी तरह से काम करते हैं और चीजों को सरल रखते हैं।
- **sort-select** (9 भाषाएं) के लिए, यदि जगह अनुमति देती है तो बटन का एक समूह ठीक है; अन्यथा, `<select>` के साथ बने रहें और एक टूलटिप या लेबल जोड़ें जो इसे समझाए।
- सुलभता (जैसे, स्क्रीन रीडर का उपयोग करके) और मोबाइल रिस्पॉन्सिवनेस के लिए परीक्षण करें।
- यदि यह एक डायनामिक साइट के लिए है, तो चयन के आधार पर `post-number` को अपडेट करने के लिए अपने मौजूदा JS के साथ एकीकृत करें।

यदि यह आपके द्वारा "स्विच" से अभिप्रेत से मेल नहीं खाता है, या यदि आप और संदर्भ साझा करते हैं (जैसे, कि select क्या करते हैं), तो मैं इसे परिष्कृत कर सकता हूं!