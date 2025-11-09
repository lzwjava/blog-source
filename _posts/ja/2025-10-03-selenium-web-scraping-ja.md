---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: SeleniumによるWebスクレイピングコードの解説
translated: true
type: note
---

### 提供されたコードにおけるSelenium APIの使用法の説明

このPythonスクリプトは、**Selenium WebDriver**ライブラリを使用してWebブラウザ（具体的にはChrome）を自動化し、Webサイト（おそらく`https://xxdata.com/index.aspx`にあるデータ/トレードポータル）との対話を行います。目標はWebスクレイピングであると思われます。ログイン、貿易/注文データの検索（'8449'のようなHSコードを使用）、ページネーションされた結果のナビゲーション、詳細のクリック、HTMLテーブルからの構造化データの抽出、そしてSQLiteデータベース（`data.db`）への保存を行います。

Seleniumはここで**ブラウザ自動化**のために使用されており、スクリプトがタイピング、クリック、スクロール、ページ読み込みの待機といった人間の対話を模倣することを可能にします。これは、単純なHTTPリクエスト（例：JavaScriptが多用されたページ、iframe、または動的コンテンツのため）では困難または不可能なことです。Seleniumは、動的Web要素、セッション、マルチウィンドウ/iframe切り替えを処理します。これらは現代のWebアプリでは一般的です。

**セクションごとに**、主要なSelenium API、その目的、そして使用方法を強調しながら説明します。注意：コード内のいくつかのメソッド（例：`find_element_by_css_selector`）は古いSeleniumバージョン（4.0以前）のもので、非推奨です。現代のSelenium（4+）では、代わりに`find_element(By.CSS_SELECTOR, ...)`を使用しますが、機能は同じです。スクリプトはまた、待機、例外、および要素処理に必要なモジュールをインポートしています。

#### 1. **インポートとセットアップ（Seleniumの初期化）**
   ```python
   from selenium import webdriver
   from selenium.webdriver.chrome.webdriver import WebDriver
   from selenium.webdriver.common.keys import Keys
   from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC
   from selenium.webdriver.common.by import By
   from selenium.webdriver.remote.webelement import WebElement
   ```
   - **目的**: これらのインポートは、Seleniumの主要なコンポーネントを提供します：
     - `webdriver`: ブラウザを制御するためのメインモジュール。
     - `WebDriver`: ブラウザインスタンスの型ヒント（型安全性を確保）。
     - `Keys`: キーボード入力（例：Page Up）をシミュレートするため。
     - 例外: タイムアウトや古くなった要素（ページ更新後に変更される要素）のような一般的なエラーを処理。
     - `WebDriverWait` と `EC` (Expected Conditions): 明示的な待機のため — 要素が条件（例：ページ上に存在する）を満たすまでポーリング。
     - `By`: 要素を見つけるためのロケーター戦略（例：CSSセレクター、ID、タグ名）。
     - `WebElement`: 対話のためのHTML要素を表す。

   `run()` 関数内:
   ```python
   options = webdriver.ChromeOptions()
   options.add_argument("--start-maximized")  # ブラウザをフルスクリーンで開く。
   options.add_argument('--log-level=3')      # コンソールログを抑制し、出力をクリーンにする。
   browser: WebDriver = webdriver.Chrome(executable_path="./chromedriver", options=options)
   ```
   - **使用されているSelenium API**: `webdriver.Chrome(options=...)`
     - ローカルの`chromedriver`実行ファイル（スクリプトのディレクトリ内にある必要がある）を使用してChromeブラウザインスタンスを初期化。
     - `ChromeOptions`: ブラウザセッションをカスタマイズ（例：`options.add_argument("--headless")`を追加してバックグラウンド実行用のヘッドレスモードに可能）。
     - これにより、ライブで制御可能なブラウザウィンドウが作成されます。SeleniumはPythonとブラウザのDevToolsプロトコルの間のブリッジとして機能します。

   ```python
   browser.get('https://xxdata.com/index.aspx')
   ```
   - **使用されているSelenium API**: `WebDriver.get(url)`
     - 開始URLに移動し、ユーザーがアドレスバーに入力するようにページを読み込みます。

#### 2. **ログインプロセス**
   ```python
   input_username = browser.find_element_by_css_selector('input[name=username]')
   input_username.send_keys('name')
   input_password = browser.find_element_by_css_selector('input[name=password]')
   input_password.send_keys('password')
   btn_login = browser.find_element_by_css_selector('div.login-check')
   btn_login.click()
   ```
   - **使用されているSelenium API**:
     - `WebDriver.find_element_by_css_selector(css)` (非推奨；現代的: `find_element(By.CSS_SELECTOR, css)`): CSSセレクター（例：`name="username"`のような属性による）を使用して単一のHTML要素を特定。`WebElement`を返します。
     - `WebElement.send_keys(text)`: 入力フィールド（例：ユーザー名/パスワード）へのタイピングをシミュレート。
     - `WebElement.click()`: ボタンやリンク上のマウスクリックをシミュレート。
   - **Seleniumの使用方法**: フォーム送信を自動化。Seleniumがなければ、POSTリクエストをリバースエンジニアリングする必要がありますが、これはJavaScriptバリデーションや動的フォームをシームレスに処理します。資格情報はハードコードされています（本番環境では安全ではありません — 環境変数を使用してください）。

   ログイン後:
   ```python
   wait_element(browser, 'div.dsh_01')
   ```
   - ダッシュボードが読み込まれるまで一時停止するために、カスタム`wait_element`関数（後述）を呼び出します。

#### 3. **ナビゲーションと検索**
   ```python
   trade_div = browser.find_element_by_css_selector('div.dsh_01')
   trade_div.click()
   wait_element(browser, 'a.teq_icon')
   teq = browser.find_element_by_css_selector('a.teq_icon')
   teq.click()
   wait_element(browser, 'div.panel-body')
   iframe = browser.find_element_by_css_selector('div.panel-body > iframe')
   iframe_id = iframe.get_attribute('id')
   browser.switch_to.frame(iframe_id)
   ```
   - **使用されているSelenium API**:
     - `find_element_by_css_selector`: ナビゲーション要素（例：ダッシュボードdiv、アイコンリンク）を特定。
     - `WebElement.click()`: ナビゲートするためにクリック（例：「trade」セクションへ）。
     - `WebElement.get_attribute('id')`: HTML属性（ここではiframeのID）を取得。
     - `WebDriver.switch_to.frame(frame_id)`: ドライバーのコンテキストを`<iframe>`（コンテンツを埋め込むためのアプリで一般的）に切り替えます。これがないと、iframe内の要素にはアクセスできません。
   - **Seleniumの使用方法**: マルチステップのナビゲーションと埋め込みコンテンツを処理します。iframeはDOMを分離するため、内部ページをスクレイピングするには切り替えが不可欠です。

   検索プロセス:
   ```python
   input_search = browser.find_element_by_id('_easyui_textbox_input7')  # IDロケーターを使用。
   input_search.send_keys('8449')
   time.sleep(10)
   enter = browser.find_element_by_css_selector('a#btnOk > div.enter-bt')
   enter.click()
   ```
   - **使用されているSelenium API**:
     - `find_element_by_id(id)` (非推奨；現代的: `find_element(By.ID, id)`): HTMLの`id`属性で特定。
     - `send_keys`: 検索クエリ（製品のHSコード）を入力。
     - `time.sleep(10)`: 暗黙的な待機（粗悪；明示的な待機を使用する方が良い）。
     - `click()`: 検索を送信。
   - **Seleniumの使用方法**: ユーザー検索をシミュレート。`time.sleep`はAJAX/JavaScriptが結果を読み込むために一時停止します。

#### 4. **ページネーションと結果処理**
   ```python
   result_count_span = browser.find_element_by_css_selector('span#ResultCount')
   page = math.ceil(int(result_count_span.text) / 20)  # 総ページ数を計算（1ページあたり20結果）。
   skip = 0
   page = page - skip

   for p in range(page):
       input_page = browser.find_element_by_css_selector('input.laypage_skip')
       input_page.send_keys(str(p + skip + 1))
       btn_confirm = browser.find_element_by_css_selector('button.laypage_btn')
       btn_confirm.click()
       time.sleep(2)

       locates = browser.find_elements_by_css_selector('div.rownumber-bt')  # 複数の要素。
       print('page ' + str(p) + ' size: ' + str(len(locates)))
       for locate in locates:
           browser.execute_script("arguments[0].scrollIntoView();", locate)  # JavaScriptスクロール。
           time.sleep(1)
           browser.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)  # キーボードスクロール。
           time.sleep(1)
           try:
               locate.click()
           except ElementClickInterceptedException:
               print('ElementClickInterceptedException')
               continue
           except StaleElementReferenceException:
               print('StaleElementReferenceException')
               continue
           # ... (以下続く)
   ```
   - **使用されているSelenium API**:
     - `find_element_by_css_selector`: spanから結果数を取得。
     - `WebElement.text`: 要素から表示テキストを抽出（例：「100」のようなカウント）。
     - `find_elements_by_css_selector` (複数形；非推奨: `find_elements(By.CSS_SELECTOR, ...)`): 複数の要素（例：ページ上の行リンク）を検索。`WebElement`のリストを返します。
     - `WebDriver.execute_script(js_code, *args)`: ブラウザでカスタムJavaScriptを実行（ここでは、クリックの問題を避けるために要素をビューにスクロール）。
     - `WebDriver.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)`: キーボードスクロールをシミュレート（`Keys`列挙型を使用）。
     - 例外: クリックの失敗（例：オーバーレイがクリックをブロック）または古くなった要素（DOMが更新され、参照が無効化 — 動的UIで一般的）をキャッチ。
   - **Seleniumの使用方法**: ページ番号を入力して「移動」をクリックすることでページネーションを自動化します。各結果行（`div.rownumber-bt`）について、可視性を確保するためにスクロールし、詳細を新しいウィンドウで開くためにクリックします。これは、遅延読み込みや無限スクロールのような動作を処理します。

#### 5. **ウィンドウ/Iframe切り替えとデータ抽出**
   ループからの続き:
   ```python
   time.sleep(1)
   browser.switch_to.window(browser.window_handles[1])  # 新しいタブ/ウィンドウに切り替え。
   wait_element(browser, 'div#content')
   try:
       save_page(browser)
   except IndexError:
       print('IndexError')
       continue
   browser.close()  # 詳細ウィンドウを閉じる。
   browser.switch_to.window(browser.window_handles[0])  # メインウィンドウに戻る。
   browser.switch_to.frame(iframe_id)  # iframeコンテキストに戻る。
   ```
   - **使用されているSelenium API**:
     - `WebDriver.window_handles`: 開いているウィンドウ/タブのIDのリスト。
     - `WebDriver.switch_to.window(handle)`: 特定のウィンドウ（インデックス0 = メイン、1 = クリックで開かれた新しいタブ）にフォーカスを切り替え。
     - `WebDriver.close()`: 現在のウィンドウを閉じる。
   - **Seleniumの使用方法**: クリックで詳細を新しいタブで開くため、それらをスクレイピングするためにコンテキストを切り替え、その後戻ります。これはマルチタブアプリでは不可欠です。

#### 6. **`save_page(browser: WebDriver)`関数内のデータ抽出**
   これがスクレイピングロジックの核心です:
   ```python
   ts = browser.find_elements_by_css_selector('table')  # ページ上のすべてのテーブル。
   t0 = ts[0]
   tds0 = t0.find_elements_by_tag_name('td')  # 最初のテーブル内のTDセル。
   order_number = tds0[2].text  # 特定のセルからテキストを抽出。
   # ... (他のテーブル t1, t2 などについて同様)
   ```
   - **使用されているSelenium API**:
     - `find_elements_by_css_selector('table')` / `find_elements_by_tag_name('td')` (非推奨: `By.TAG_NAME`を使用): すべての`<table>`とその`<td>`セルを検索。
     - `WebElement.text`: セルからテキストコンテンツを引き出す（例：注文番号、輸入者名）。
     - カスタム `tds_to_text(tds: list[WebElement])`: ペアになった`<td>`（例：ラベル + 値）からのテキストを連結。
   - **Seleniumの使用方法**: ページのDOM構造（注文/輸入者/輸出者の詳細を含むテーブル）を解析します。可変のテーブル数（例：`len(ts) == 8`の場合、追加のテーブルが存在）を処理します。データはその後SQLiteに挿入されます（Selenium以外の部分）。

   条件付きロジックは、テーブルのインデックスに基づいて、固定レイアウトを仮定して、`order_number`、`importer`、`exporter`などのフィールドを抽出します。

#### 7. **待機とエラー処理（`wait_element`関数）**
   ```python
   def wait_element(browser, css):
       timeout = 30
       try:
           element_present = EC.presence_of_element_located((By.CSS_SELECTOR, css))
           WebDriverWait(browser, timeout).until(element_present)
       except TimeoutException:
           print('Timed out waiting for page to load')
   ```
   - **使用されているSelenium API**:
     - `expected_conditions.presence_of_element_located(locator)`: 要素がDOMに存在する（必ずしも表示されている必要はない）まで待機。
     - `WebDriverWait(driver, timeout).until(condition)`: 条件に対して最大30秒間、0.5秒ごとにポーリング。
     - `TimeoutException`: 待機が失敗した場合に発生。
   - **Seleniumの使用方法**: 競合状態（例：ページが読み込まれる前にクリック）を防ぎます。要素固有で効率的であるため、`time.sleep`よりも優れています。

#### 8. **クリーンアップ**
   ```python
   time.sleep(1000)  # 長い一時停止（デバッグ用？）。
   browser.quit()    # ブラウザを閉じ、セッションを終了。
   ```
   - **使用されているSelenium API**: `WebDriver.quit()`: ドライバーを終了し、すべてのウィンドウを閉じ、リソースを解放します。

#### Seleniumの全体的な役割
- **自動化フロー**: Seleniumは実際のブラウザを起動し、ページを読み込み、DOMクエリ（CSS/IDなどのロケーター）を介して対話し、動的動作（JS実行、待機、切り替え）を処理します。SPAやセッション/クッキーを持つ保護されたサイトに理想的です。
- **ここでの強み**: ログイン状態、iframe、新しいタブ、スクロールを処理 — BeautifulSoup/Requestsのようなスクレイピングツールだけではこれらはできません。
- **コードの制限/問題点**:
  - 非推奨のロケーター: 将来性のために`By`に更新。
  - ハードコードされたスリープ: 速度向上/不安定性低減のため、より多くの待機に置き換え。
  - 例外: 良い処理ですが、StaleElementでリトライ可能。
  - 倫理/合法性: スクレイピングは利用規約に違反する可能性あり；ユーザーエージェントヘッダーやプロキシを追加して人間を模倣。
  - パフォーマンス: ヘッドフル（表示されるブラウザ）で実行；本番環境ではヘッドレスに。
- **実行方法**: ChromeDriverが必要（Seleniumサイトからダウンロード、Chromeバージョンに一致）。`pip install selenium`でSeleniumをインストール。

特定の部分、コードの近代化、またはデバッグについて質問があれば、お知らせください！