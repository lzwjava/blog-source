---
audio: false
lang: ar
layout: post
title: بناء امتداد Chrome
translated: true
---

هل سبق لك أن فتحت الكثير من علامات التبويب في المتصفح وتأملت في وجود أداة لتسييرها تلقائيًا؟ في هذا المقال، سنمر عبر إنشاء امتداد Chrome يُدعى **"Tabs Killer"**، الذي يُغلق علامات التبويب الأقدم تلقائيًا عندما يتجاوز عدد علامات التبويب الحد الذي يحدده المستخدم. سأشرح لك الكود، وأشرح لك كيف يعمل، وأقدم لك بعض الأفكار التي تساعدك في بناء امتداد Chrome الخاص بك.

في نهاية هذا المقال، ستفهم بنية امتداد Chrome، وكيفية التعامل مع API Chrome، وكيفية إنشاء واجهة Popup مع الإعدادات.

---

## ما يفعله "Tabs Killer"?

"Tabs Killer" هو امتداد Chrome الذي:
- يراقب عدد علامات التبويب المفتوحة.
- يسمح للمستخدمين بتحديد حد أقصى لعدد علامات التبويب.
- يُغلق علامات التبويب الأقدم تلقائيًا عندما يتجاوز الحد.
- يقدم ميزة قائمة بيضاء لحماية علامات التبويب المحددة (مثلًا، بناءً على نماذج URL) من الإغلاق.

يضم الاضافة واجهة Popup لتكوين الإعدادات ونسخة خلفية لتسيير علامات التبويب.

---

## بنية المشروع

هذه هي بنية ملفات امتداد "Tabs Killer":

```
tabs-killer/
├── manifest.json         # تكوين الاضافة
├── popup.html            # واجهة المستخدم Popup
├── popup.js             # منطق Popup
├── background.html       # صفحة الخلفية
├── app.build.js          # منطق التطبيق الرئيسي (مفترض)
├── js/
│   ├── lib/              # مكتبات خارجية (jQuery, Underscore, Bootstrap, RequireJS)
│   ├── tabmanager.js     # منطق تسيير علامات التبويب (مفترض)
│   └── settings.js       # إدارة الإعدادات (مفترض)
├── css/
│   └── popup.css         # أنماط Popup
└── img/
    ├── icon16.png        # أيقونة 16x16
    ├── icon48.png        # أيقونة 48x48
    └── icon128.png       # أيقونة 128x128
```

---

## الخطوة 1: ملف البيان (`manifest.json`)

يعد ملف `manifest.json` قلب أي امتداد Chrome. يحدد البيانات الوصفية، الإذن، والمكونات الرئيسية.

```json
{
  "manifest_version": 2,
  "name": "Tabs Killer",
  "description": "يغلق علامات التبويب الأقدم تلقائيًا عندما يكون هناك الكثير من علامات التبويب.",
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

### شرح:
- **`manifest_version`**: يجب أن يكون `2` (Chrome قد ألغى الإصدار 1).
- **`name`, `description`, `version`**: بيانات وصفية أساسية.
- **`browser_action`**: يحدد أيقونة شريط الأدوات للاضافة وPopup (`popup.html`).
- **`icons`**: أيقونات مختلفة الأحجام (تستخدم في متجر Chrome وشريط الأدوات).
- **`background`**: يحدد صفحة الخلفية (`background.html`) التي تعمل بشكل مستمر.
- **`permissions`**: يطلب الوصول إلى API `tabs` (لتسيير علامات التبويب) وAPI `storage` (لحفظ الإعدادات).
- **`content_security_policy`**: يسمح بـ `unsafe-eval` لمكتبات مثل RequireJS (استخدم بحذر في الإنتاج).

---

## الخطوة 2: واجهة المستخدم Popup (`popup.html`)

تظهر واجهة Popup عندما ينقر المستخدم على أيقونة الاضافة. تستخدم Bootstrap لتزيينها وتضم واجهة تبويب مع قسم "Options".

```html
<!doctype html>
<html>
<head>
  <title>Popup Extension Tabs Killer</title>
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
    <li><a href="#tabOptions" target="#tabOptions" data-toggle="tab">Options</a></li>
  </ul>
  <div class="tab-content">
    <div class="tab-pane active" id="tabOptions">
      <form class="well">
        <fieldset>
          <legend>Settings</legend>
          <p>
            <label for="maxTabs">أقصى عدد من علامات التبويب للبقاء</label>
            <input type="text" id="maxTabs" class="span1" name="maxTabs"> علامات تبويب
          </p>
        </fieldset>
        <div id="status" class="alert alert-success invisible"></div>
        <fieldset>
          <legend>Auto-Lock</legend>
          <label for="white-list-input">علامة تبويب تحتوي على نص URL:</label>
          <input type="text" id="white-list-input"/>
          <button class="btn-mini add-on" disabled id="white-list-add">Add</button>
          <table class="table table-bordered table-striped" id="white-list">
            <thead>
              <tr>
                <th>نموذج URL</th>
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
      <td><a class="deleteLink" href="#">Remove</a></td>
    </tr>
  </script>
</body>
</html>
```

### شرح:
- **المكتبات**: تستخدم jQuery، Underscore، Bootstrap، وRequireJS للوظائف والتزيين.
- **عناصر واجهة المستخدم**:
  - مدخل نصي (`#maxTabs`) لتحديد أقصى عدد من علامات التبويب.
  - مدخل قائمة بيضاء (`#white-list-input`) وزر "Add" (`#white-list-add`) لحماية URLs محددة.
  - جدول (`#white-list`) لعرض نماذج القائمة البيضاء مع رابط "Remove".
  - رسالة حالة (`#status`) لعرض ردود الفعل.
- **قالب**: قالب Underscore.js (`#url-item-template`) يولد صفوف الجدول بشكل ديناميكي.

---

## الخطوة 3: منطق Popup (`popup.js`)

يستقبل هذا الكود التفاعلية في Popup، مثل حفظ الإعدادات وتسيير القائمة البيضاء.

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
        .html('Saving...').delay(50).animate({opacity: 0});
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

### شرح:
- **التنشيط**: يربط إلى `GlobalObject` في الصفحة الخلفية لإعدادات وتسيير علامات التبويب.
- **`init`**: يحدد مستمعين للحدث، مثل إدخال معلق لـ `#maxTabs`.
- **`loadOptions`**: يحمّل الإعدادات المحفوظة (أقصى عدد من علامات التبويب و القائمة البيضاء) ويملأ واجهة المستخدم.
- **`saveOption`**: يحفظ الإعدادات في `GlobalObject.settings` ويظهر "Saving...".
- **`buildWhiteListTable`**: يبنى جدول القائمة البيضاء بشكل ديناميكي مع وظيفة الحذف.
- **مستمعين للحدث**: يدير التحقق من صحة الإدخال، إضافة عناصر القائمة البيضاء، وتغيير التبويب.

---

## الخطوة 4: منطق الخلفية (`background.html` وScripts المفترضة)

تعمل صفحة الخلفية (`background.html`) بشكل مستمر وتحمّل المنطقية الأساسية.

```javascript
// background.js (مفترض، بناءً على مقطع المقدم)
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

### الافتراضات:
- **`settings.js`**: يدير التخزين (مثلًا، `chrome.storage`) لإعدادات مثل `maxTabs` و `whiteList`.
- **`tabmanager.js`**: يستخدم API `tabs` لمراقبة وإغلاق علامات التبويب بناءً على الحد `maxTabs` و `whiteList`.

مثال `tabmanager.js` (مفترض):
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
        chrome.tabs.remove(tabsToRemove[0].id); // إغلاق علامة التبويب الأقدم
      }
    });
  }
};
```

---

## كيفية اختبار الاضافة

1. افتح Chrome واذهب إلى `chrome://extensions/`.
2. قم بتفعيل "Developer mode" (المزاحم في اليمين العلوي).
3. انقر على "Load unpacked" واختر مجلد `tabs-killer`.
4. انقر على أيقونة الاضافة لفتح Popup واختبار الإعدادات.

---

## نصائح لكتابة امتداد Chrome الخاص بك

1. **ابدأ بشيء بسيط**: ابدأ ببيان بسيط وPopup أو نصية خلفية.
2. **استخدم APIs Chrome**: استغل `chrome.tabs`، `chrome.storage` وغيرها حسب الحاجة.
3. **التشخيص**: استخدم `console.log` وChrome’s DevTools (انقر باليمين على Popup > Inspect).
4. **الأمان**: تجنب `unsafe-eval` في الإنتاج؛ استخدم سياسات أمان محتوى أكثر صرامة.
5. **مكتبات واجهة المستخدم**: Bootstrap وjQuery تسهل تطوير واجهة المستخدم ولكن احرص على خفة الاضافة.

---

## الخاتمة

"Tabs Killer" يوضح كيفية دمج واجهة Popup، منطق الخلفية، وAPIs Chrome لإنشاء امتداد وظيفي. مع هذه الأساس، يمكنك تخصيصه أكثر—إضافة إشعارات، تحسين منطق إغلاق علامات التبويب، أو تحسين واجهة المستخدم.

لا تتردد في تجربة الكود وشارك أفكارك الخاصة باضافات Chrome! سعيد بالبرمجة!