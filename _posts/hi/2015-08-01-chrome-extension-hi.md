---
audio: false
lang: hi
layout: post
title: Chrome Extension बनाना
translated: true
---

क्या आपने कभी बहुत सारे ब्राउज़र टैब खोले और उन्हें स्वचालित रूप से प्रबंधित करने के लिए एक टूल की इच्छा की है? इस ब्लॉग पोस्ट में, हम एक क्रोम एक्सटेंशन का निर्माण करने का मार्गदर्शन करेंगे जिसे **"Tabs Killer"** कहा जाता है, जो स्वचालित रूप से सबसे पुराने टैब को बंद करता है जब टैब गिनती उपयोगकर्ता निर्धारित सीमा को पार कर जाती है। मैं कोड को टुकड़ों में तोड़ूंगा, इसका काम कैसे करता है, समझाऊंगा और आपको अपने क्रोम एक्सटेंशन बनाने में मदद करने के लिए कुछ अहम सूचनाएं दूंगा।

इस पोस्ट के अंत तक, आप क्रोम एक्सटेंशन का संरचना, क्रोम एपीआई के साथ काम करने का तरीका और सेटिंग्स के साथ पॉपअप इंटरफेस बनाने का तरीका समझेंगे।

---

## "Tabs Killer" क्या करता है?

"Tabs Killer" एक क्रोम एक्सटेंशन है जो:
- खुले टैबों की संख्या को निगरानी करता है।
- उपयोगकर्ताओं को अधिकतम टैब सीमा सेट करने की अनुमति देता है।
- सीमा को पार करने पर स्वचालित रूप से सबसे पुराने टैब को बंद करता है।
- विशेष टैबों (उदाहरण के लिए, URL पैटर्न के आधार पर) को बंद होने से बचाने के लिए एक व्हाइटलिस्ट फीचर प्रदान करता है।

एक्सटेंशन में सेटिंग्स को कॉन्फ़िगर करने के लिए एक पॉपअप इंटरफेस और टैब प्रबंधन के लिए एक बैकग्राउंड स्क्रिप्ट शामिल है।

---

## प्रोजेक्ट संरचना

यहाँ "Tabs Killer" एक्सटेंशन का फ़ाइल संरचना है:

```
tabs-killer/
├── manifest.json         # एक्सटेंशन कॉन्फ़िगरेशन
├── popup.html            # पॉपअप UI
├── popup.js             # पॉपअप लॉजिक
├── background.html       # बैकग्राउंड पेज
├── app.build.js          # मुख्य ऐप लॉजिक (अनुमानित)
├── js/
│   ├── lib/              # बाहरी लाइब्रेरी (जेक्वेरी, अंडरस्कोर, बूटस्ट्रैप, रिक्वायरजेएस)
│   ├── tabmanager.js     # टैब प्रबंधन लॉजिक (अनुमानित)
│   └── settings.js       # सेटिंग्स प्रबंधन (अनुमानित)
├── css/
│   └── popup.css         # पॉपअप स्टाइल
└── img/
    ├── icon16.png        # 16x16 आइकन
    ├── icon48.png        # 48x48 आइकन
    └── icon128.png       # 128x128 आइकन
```

---

## चरण 1: मैनिफेस्ट फ़ाइल (`manifest.json`)

`manifest.json` फ़ाइल किसी भी क्रोम एक्सटेंशन का दिल है। यह मेटाडेटा, अनुमतियाँ और मुख्य घटकों को परिभाषित करता है।

```json
{
  "manifest_version": 2,
  "name": "Tabs Killer",
  "description": "टैब बहुत ज्यादा होने पर स्वचालित रूप से सबसे पुराने टैब को बंद करता है।",
  "version": "1.0",
  "browser_action": {
    "default_icon": "img/icon128.png",
    "default_popup": "popup.html"
  },
  "icons": {
    "128": "img/icon128.png",
    "48": "img/icon48.png",
    "16": "img/icon16.png"
  },
  "background": {
    "page": "background.html"
  },
  "permissions": [
    "tabs",
    "storage"
  ],
  "content_security_policy": "script-src 'self' 'unsafe-eval'; object-src 'self'"
}
```

### व्याख्या:
- **`manifest_version`**: `2` होना चाहिए (क्रोम ने वर्जन 1 को अवैध कर दिया है)।
- **`name`, `description`, `version`**: बुनियादी मेटाडेटा।
- **`browser_action`**: एक्सटेंशन के टूलबार आइकन और पॉपअप (`popup.html`) को परिभाषित करता है।
- **`icons`**: विभिन्न आकारों के लिए आइकन (क्रोम वेब स्टोर और टूलबार में उपयोग किए जाते हैं)।
- **`background`**: एक बैकग्राउंड पेज (`background.html`) को परिभाषित करता है जो स्थायी रूप से चलता है।
- **`permissions`**: `tabs` एपीआई (टैब प्रबंधन के लिए) और `storage` एपीआई (सेटिंग्स को सेट करने के लिए) तक पहुंच की मांग करता है।
- **`content_security_policy`**: लाइब्रेरी जैसे रिक्वायरजेएस के लिए `unsafe-eval` की अनुमति देता है (प्रोडक्शन में सावधानी से उपयोग करें)।

---

## चरण 2: पॉपअप UI (`popup.html`)

जब उपयोगकर्ता एक्सटेंशन आइकन पर क्लिक करता है, तो पॉपअप दिखाई देता है। यह स्टाइलिंग के लिए बूटस्ट्रैप का उपयोग करता है और एक टैब इंटरफेस के साथ एक "ऑप्शंस" सेक्शन शामिल करता है।

```html
<!doctype html>
<html>
<head>
  <title>Tabs Killer एक्सटेंशन का पॉपअप</title>
  <link rel="stylesheet" href="js/lib/bootstrap/css/bootstrap.css" type="text/css"/>
  <link rel="stylesheet" href="css/popup.css"/>
  <script src="js/lib/jquery.min.js"></script>
  <script src="js/lib/underscore.js"></script>
  <script src="js/lib/bootstrap/js/bootstrap.min.js"></script>
  <script src="js/lib/bootstrap/js/bootstrap-tab.js"></script>
  <script src="js/lib/require.js"></script>
  <script src="app.build.js"></script>
  <script src="popup.js"></script>
</head>
<body>
  <ul class="nav nav-tabs">
    <li><a href="#tabOptions" target="#tabOptions" data-toggle="tab">ऑप्शंस</a></li>
  </ul>
  <div class="tab-content">
    <div class="tab-pane active" id="tabOptions">
      <form class="well">
        <fieldset>
          <legend>सेटिंग्स</legend>
          <p>
            <label for="maxTabs">टैबों की अधिकतम संख्या</label>
            <input type="text" id="maxTabs" class="span1" name="maxTabs"> टैब
          </p>
        </fieldset>
        <div id="status" class="alert alert-success invisible"></div>
        <fieldset>
          <legend>ऑटो-लॉक</legend>
          <label for="white-list-input">URL में स्ट्रिंग जो शामिल है:</label>
          <input type="text" id="white-list-input"/>
          <button class="btn-mini add-on" disabled id="white-list-add">जोड़ें</button>
          <table class="table table-bordered table-striped" id="white-list">
            <thead>
              <tr>
                <th>URL पैटर्न</th>
                <th></th>
              </tr>
            </thead>
            <tbody></tbody>
          </table>
        </fieldset>
      </form>
    </div>
  </div>
  <script type="text/html" id="url-item-template">
    <tr>
      <td><%=url%></td>
      <td><a class="deleteLink" href="#">हटाएं</a></td>
    </tr>
  </script>
</body>
</html>
```

### व्याख्या:
- **लाइब्रेरी**: जेक्वेरी, अंडरस्कोर, बूटस्ट्रैप और रिक्वायरजेएस के लिए कार्य और स्टाइलिंग के लिए उपयोग किया जाता है।
- **UI एलेमेंट्स**:
  - एक टेक्स्ट इनपुट (`#maxTabs`) अधिकतम टैब संख्या सेट करने के लिए।
  - एक व्हाइटलिस्ट इनपुट (`#white-list-input`) और "जोड़ें" बटन (`#white-list-add`) विशेष URL को बचाने के लिए।
  - एक टेबल (`#white-list`) व्हाइटलिस्ट पैटर्न दिखाने के लिए एक "हटाएं" लिंक के साथ।
  - एक स्टेटस संदेश (`#status`) सेटिंग्स को सेट करने के लिए फीडबैक दिखाने के लिए।
- **टेम्पलेट**: एक अंडरस्कोर.जेएस टेम्पलेट (`#url-item-template`) डायनामिक रूप से टेबल रows बनाता है।

---

## चरण 3: पॉपअप लॉजिक (`popup.js`)

इस स्क्रिप्ट पॉपअप के इंटरैक्टिविटी को संभालता है, जैसे सेटिंग्स को सेट करना और व्हाइटलिस्ट प्रबंधित करना।

```javascript
require([], function () {
  var GlobalObject = chrome.extension.getBackgroundPage().GlobalObject;

  Popup = {};
  Popup.optionsTab = {};

  Popup.optionsTab.init = function (context) {
    function onBlurInput() {
      var key = this.id;
      Popup.optionsTab.saveOption(key, $(this).val());
    }
    $('#maxTabs').keyup(_.debounce(onBlurInput, 200));
    Popup.optionsTab.loadOptions();
  };

  Popup.optionsTab.loadOptions = function () {
    $('#maxTabs').val(GlobalObject.settings.get('maxTabs'));
    var whiteList = GlobalObject.settings.get('whiteList');
    Popup.optionsTab.buildWhiteListTable(whiteList);

    var $whiteListInput = $('#white-list-input');
    var $whiteListAdd = $('#white-list-add');

    var isValid = function (pattern) {
      return /\S/.test(pattern);
    };

    $whiteListInput.on('input', function () {
      if (isValid($whiteListInput.val())) {
        $whiteListAdd.removeAttr('disabled');
      } else {
        $whiteListAdd.attr('disabled', 'disabled');
      }
    });

    $whiteListAdd.click(function () {
      if (!isValid($whiteListInput.val())) return;
      whiteList.push($whiteListInput.val());
      $whiteListInput.val('').trigger('input').focus();
      Popup.optionsTab.saveOption('whiteList', whiteList);
      Popup.optionsTab.buildWhiteListTable(whiteList);
    });
  };

  Popup.optionsTab.saveOption = function (key, value, hideStatus) {
    if (!hideStatus) $('#status').html('');
    GlobalObject.settings.set(key, value);
    if (!hideStatus) {
      $('#status').removeClass('invisible').css('opacity', '100')
        .html('सेटिंग्स को सेट कर रहा है...').delay(50).animate({opacity: 0});
    }
  };

  Popup.optionsTab.buildWhiteListTable = function (whiteList) {
    var urlItemTemplate = _.template($("#url-item-template").html());
    var $wlTable = $('table#white-list tbody');
    $wlTable.html('');
    for (var i = 0; i < whiteList.length; i++) {
      var $tr = $(urlItemTemplate({url: whiteList[i]}));
      var $deleteLink = $tr.find('a.deleteLink').parent();
      $deleteLink.click(function () {
        whiteList.splice(whiteList.indexOf($(this).data('pattern')), 1);
        Popup.optionsTab.saveOption('whiteList', whiteList, true);
        Popup.optionsTab.buildWhiteListTable(whiteList);
      }).data('pattern', whiteList[i]);
      $wlTable.append($tr);
    }
  };

  $(document).ready(function () {
    $('a[data-toggle="tab"]').on('show', function (e) {
      var tabId = e.target.hash;
      if (tabId === '#tabOptions') {
        Popup.optionsTab.init($('div#tabOptions'));
      }
    });
    $('a[href="#tabOptions"]').click();
  });
});
```

### व्याख्या:
- **इनिशियलाइज़ेशन**: बैकग्राउंड पेज के `GlobalObject` के साथ सेटिंग्स और टैब प्रबंधन के लिए कनेक्ट करता है।
- **`init`**: इवेंट लिसनर्स सेट करता है, जैसे `#maxTabs` के लिए डेबाउंस्ड इनपुट।
- **`loadOptions`**: सेटिंग्स (अधिकतम टैब और व्हाइटलिस्ट) को लोड करता है और UI को पॉपुलेट करता है।
- **`saveOption`**: सेटिंग्स को `GlobalObject.settings` में सेट करता है और "सेटिंग्स को सेट कर रहा है..." एनिमेशन दिखाता है।
- **`buildWhiteListTable`**: व्हाइटलिस्ट टेबल को हटाने के साथ डायनामिक रूप से बनाता है।
- **इवेंट लिसनर्स**: इनपुट वैलिडेशन, व्हाइटलिस्ट एंट्री जोड़ना और टैब स्विचिंग को संभालता है।

---

## चरण 4: बैकग्राउंड लॉजिक (`background.html` और अनुमानित स्क्रिप्ट)

बैकग्राउंड पेज (`background.html`) स्थायी रूप से चलता है और कोर लॉजिक लोड करता है।

```javascript
// background.js (अनुमानित, दिए गए स्निपेट के आधार पर)
GlobalObject = {};

require(['tabmanager', 'settings'], function (tabmanager, settings) {
  var startup = function () {
    GlobalObject.settings = settings;
    GlobalObject.tabmanager = tabmanager;
    settings.init();
    tabmanager.init();
  };
  startup();
});
```

### अनुमान:
- **`settings.js`**: सेटिंग्स जैसे `maxTabs` और `whiteList` के लिए स्टोरेज (उदाहरण के लिए, `chrome.storage`) को प्रबंधित करता है।
- **`tabmanager.js`**: `tabs` एपीआई का उपयोग करके टैब को `maxTabs` सीमा और `whiteList` के आधार पर निगरानी और बंद करता है।

उदाहरण `tabmanager.js` (हाइपोथेटिकल):
```javascript
var tabmanager = {
  init: function () {
    chrome.tabs.onCreated.addListener(this.checkTabCount);
  },
  checkTabCount: function () {
    chrome.tabs.query({}, function (tabs) {
      var maxTabs = GlobalObject.settings.get('maxTabs') || 10;
      var whiteList = GlobalObject.settings.get('whiteList') || [];
      if (tabs.length > maxTabs) {
        var tabsToRemove = tabs.filter(tab => !whiteList.some(pattern => tab.url.includes(pattern)));
        chrome.tabs.remove(tabsToRemove[0].id); // सबसे पुराने टैब को हटाएं
      }
    });
  }
};
```

---

## एक्सटेंशन को टेस्ट करने का तरीका

1. क्रोम खोलें और `chrome://extensions/` पर जाएं।
2. "डेवलपर मोड" को "ऑन" करें (ऊपरी दाहिने कोने में टॉगल)।
3. "लोड अनपैक्ड" पर क्लिक करें और `tabs-killer` फ़ोल्डर चुनें।
4. एक्सटेंशन आइकन पर क्लिक करें पॉपअप को खोलें और सेटिंग्स को टेस्ट करें।

---

## अपने क्रोम एक्सटेंशन लिखने के लिए टिप्स

1. **छोटे से शुरू करें**: एक सादे मैनिफेस्ट और एक पॉपअप या बैकग्राउंड स्क्रिप्ट से शुरू करें।
2. **क्रोम एपीआई का उपयोग करें**: आवश्यकता के अनुसार `chrome.tabs`, `chrome.storage` और अन्य का उपयोग करें।
3. **डिबगिंग**: `console.log` और क्रोम के डेवलपर टूल्स (पॉपअप पर राइट क्लिक > इंस्पेक्ट) का उपयोग करें।
4. **सुरक्षा**: प्रोडक्शन में `unsafe-eval` से बचें; अधिक सख्त कंटेंट सिक्योरिटी पॉलिसी का उपयोग करें।
5. **UI लाइब्रेरी**: बूटस्ट्रैप और जेक्वेरी UI विकास को सरल बनाते हैं लेकिन एक्सटेंशन को हल्के रखें।

---

## निष्कर्ष

"Tabs Killer" दिखाता है कि कैसे एक पॉपअप UI, बैकग्राउंड लॉजिक और क्रोम एपीआई को मिलाकर एक कार्यात्मक एक्सटेंशन बनाया जा सकता है। इस आधार के साथ, आप इसे और अधिक अनुकूलित कर सकते हैं—नोटिफिकेशन जोड़ें, टैब बंद करने के लॉजिक को सुधारें या UI को बेहतर बनाएं।

अपने क्रोम एक्सटेंशन के विचार को साझा करने और कोड के साथ प्रयोग करने में स्वतंत्र हैं! खुशी से कोडिंग करें!