---
audio: false
generated: false
image: false
lang: ja
layout: post
title: Chrome 拡張機能を作成する
translated: true
type: post
---

ブラウザのタブを開きすぎて管理が難しくなったことはありませんか？このブログ記事では、タブの数がユーザー定義の制限を超えた場合に自動的に最も古いタブを閉じるChrome拡張機能「Tabs Killer」の作成方法を説明します。コードを分解し、その動作方法を説明し、独自のChrome拡張機能を作成するための洞察を提供します。

この記事の終わりまでに、Chrome拡張機能の構造、Chrome APIの使用方法、設定用のポップアップインターフェースの作成方法を理解することができます。

---

## 「Tabs Killer」の機能

「Tabs Killer」は、以下の機能を持つChrome拡張機能です：
- 開いているタブの数を監視します。
- ユーザーが最大タブ数を設定できます。
- 制限を超えた場合に自動的に最も古いタブを閉じます。
- 特定のタブ（例：URLパターンに基づく）を閉じないようにするホワイトリスト機能を提供します。

この拡張機能には、設定を構成するためのポップアップインターフェースとタブ管理を処理するバックグラウンドスクリプトが含まれています。

---

## プロジェクト構造

「Tabs Killer」拡張機能のファイル構造は以下の通りです：

```
tabs-killer/
├── manifest.json         # 拡張機能の設定
├── popup.html            # ポップアップUI
├── popup.js             # ポップアップのロジック
├── background.html       # バックグラウンドページ
├── app.build.js          # メインエプリケーションロジック（仮定）
├── js/
│   ├── lib/              # 外部ライブラリ（jQuery、Underscore、Bootstrap、RequireJS）
│   ├── tabmanager.js     # タブ管理ロジック（仮定）
│   └── settings.js       # 設定管理（仮定）
├── css/
│   └── popup.css         # ポップアップスタイル
└── img/
    ├── icon16.png        # 16x16アイコン
    ├── icon48.png        # 48x48アイコン
    └── icon128.png       # 128x128アイコン
```

---

## ステップ1：マニフェストファイル（`manifest.json`）

`manifest.json`ファイルは、どのChrome拡張機能の心臓部です。メタデータ、権限、および主要なコンポーネントを定義します。

```json
{
  "manifest_version": 2,
  "name": "Tabs Killer",
  "description": "タブが多すぎる場合に自動的に最も古いタブを閉じます。",
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

### 説明：
- **`manifest_version`**：`2`でなければなりません（Chromeはバージョン1を廃棄しました）。
- **`name`、`description`、`version`**：基本的なメタデータ。
- **`browser_action`**：拡張機能のツールバーアイコンとポップアップ（`popup.html`）を定義します。
- **`icons`**：異なるサイズのアイコン（Chrome Web Storeとツールバーで使用）。
- **`background`**：常に実行されるバックグラウンドページ（`background.html`）を指定します。
- **`permissions`**：`tabs` API（タブを管理するため）と`storage` API（設定を保存するため）へのアクセスを要求します。
- **`content_security_policy`**：RequireJSなどのライブラリのために`unsafe-eval`を許可します（生産環境では慎重に使用）。

---

## ステップ2：ポップアップUI（`popup.html`）

ユーザーが拡張機能のアイコンをクリックするとポップアップが表示されます。スタイルにはBootstrapを使用し、タブ付きインターフェースと「オプション」セクションを含むHTMLを使用します。

```html
<!doctype html>
<html>
<head>
  <title>Tabs Killer拡張機能のポップアップ</title>
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
    <li><a href="#tabOptions" target="#tabOptions" data-toggle="tab">オプション</a></li>
  </ul>
  <div class="tab-content">
    <div class="tab-pane active" id="tabOptions">
      <form class="well">
        <fieldset>
          <legend>設定</legend>
          <p>
            <label for="maxTabs">最大タブ数</label>
            <input type="text" id="maxTabs" class="span1" name="maxTabs"> タブ
          </p>
        </fieldset>
        <div id="status" class="alert alert-success invisible"></div>
        <fieldset>
          <legend>自動ロック</legend>
          <label for="white-list-input">URLに含まれる文字列:</label>
          <input type="text" id="white-list-input"/>
          <button class="btn-mini add-on" disabled id="white-list-add">追加</button>
          <table class="table table-bordered table-striped" id="white-list">
            <thead>
              <tr>
                <th>URLパターン</th>
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
      <td><a class="deleteLink" href="#">削除</a></td>
    </tr>
  </script>
</body>
</html>
```

### 説明：
- **ライブラリ**：jQuery、Underscore、Bootstrap、RequireJSを使用して機能とスタイルを提供します。
- **UI要素**：
  - 最大タブ数を設定するためのテキスト入力（`#maxTabs`）。
  - 特定のURLを保護するためのホワイトリスト入力（`#white-list-input`）と「追加」ボタン（`#white-list-add`）。
  - ホワイトリストパターンを表示するためのテーブル（`#white-list`）と「削除」リンク。
  - 保存のフィードバックを表示するためのステータスメッセージ（`#status`）。
- **テンプレート**：Underscore.jsテンプレート（`#url-item-template`）がテーブル行を動的に生成します。

---

## ステップ3：ポップアップロジック（`popup.js`）

このスクリプトは、設定の保存やホワイトリストの管理など、ポップアップのインタラクティブな部分を処理します。

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
        .html('保存中...').delay(50).animate({opacity: 0});
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

### 説明：
- **初期化**：バックグラウンドページの`GlobalObject`に接続して設定とタブ管理を行います。
- **`init`**：`#maxTabs`の入力イベントリスナーを設定します。
- **`loadOptions`**：保存された設定（最大タブ数とホワイトリスト）を読み込み、UIに反映します。
- **`saveOption`**：設定を`GlobalObject.settings`に保存し、「保存中...」のアニメーションを表示します。
- **`buildWhiteListTable`**：ホワイトリストテーブルを動的に構築し、削除機能を追加します。
- **イベントリスナー**：入力の検証、ホワイトリストエントリの追加、タブの切り替えを処理します。

---

## ステップ4：バックグラウンドロジック（`background.html`および仮定されたスクリプト）

バックグラウンドページ（`background.html`）は常に実行され、コアロジックを読み込みます。

```javascript
// background.js（仮定、提供されたスニペットに基づく）
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

### 假定：
- **`settings.js`**：`chrome.storage`などのストレージを管理します。
- **`tabmanager.js`**：`tabs` APIを使用してタブを監視し、`maxTabs`の制限と`whiteList`に基づいてタブを閉じます。

仮定の`tabmanager.js`（仮定）：
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
        chrome.tabs.remove(tabsToRemove[0].id); // 最も古いタブを削除
      }
    });
  }
};
```

---

## 拡張機能のテスト方法

1. Chromeを開き、`chrome://extensions/`に移動します。
2. 右上のトグルで「開発者モード」を有効にします。
3. 「アンパックされたものを読み込む」をクリックし、`tabs-killer`フォルダを選択します。
4. 拡張機能のアイコンをクリックしてポップアップを開き、設定をテストします。

---

## 自分のChrome拡張機能を作成するためのヒント

1. **小さく始める**：シンプルなマニフェストとポップアップまたはバックグラウンドスクリプトから始めます。
2. **Chrome APIを使用する**：必要に応じて`chrome.tabs`、`chrome.storage`などを活用します。
3. **デバッグ**：`console.log`とChromeのDevTools（ポップアップの右クリック > インスペクト）を使用します。
4. **セキュリティ**：生産環境では`unsafe-eval`を避け、より厳格なコンテンツセキュリティポリシーを使用します。
5. **UIライブラリ**：BootstrapとjQueryはUI開発を簡素化しますが、拡張機能を軽量に保つようにします。

---

## 結論

「Tabs Killer」は、ポップアップUI、バックグラウンドロジック、Chrome APIを組み合わせて機能する拡張機能の作成方法を示しています。この基盤を使用してさらにカスタマイズすることができます。通知を追加し、タブの閉じ方のロジックを精緻化し、UIを向上させるなど、自由に実験してください！楽しいコーディングを！