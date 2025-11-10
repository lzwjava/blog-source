---
audio: false
generated: true
lang: ja
layout: post
title: クラウドフレアバイパスのためのSeleniumスクリプト
translated: true
type: note
---

あなたのSeleniumスクリプトは、Firefoxと特定のプロファイルを使用して「https://grok.com」と対話するように設計されていますが、Cloudflareのボット検知チャレンジ、具体的には「Verify you are human」チェックボックスに遭遇しています。チェックボックスをクリックした後でも、スクリプトは検証をバイパスできず、メインコンテンツ（例: `aria-label="Ask Grok anything"` が付いたテキストエリア）へのアクセスが妨げられているようです。Cloudflareは、HTTPヘッダー分析、TLSフィンガープリンティング、行動チェックなど、自動化されたブラウザを検出する高度な方法を採用しており、Selenium単体ではこのチャレンジをバイパスするのが難しい場合があります。しかし、現在のFirefoxベースのセットアップを維持しながらCloudflareテストを通過させるための戦略があります。以下に、あなたのスクリプトに合わせた2つの実用的なアプローチを示し、それらで不十分な場合の追加の考慮事項を説明します。

---

### **方法 1: プロファイルの再利用による手動チャレンジ完了**
スクリプトが特定のFirefoxプロファイル（`/home/lzw/.mozilla/firefox/wzfodx6v.default`）を使用しているため、これを利用して、手動でCloudflareチャレンジを通過した後のセッションデータを保存できます。手順は以下の通りです：

1. **プロファイルを使用して手動でFirefoxを開く**:
   - スクリプトで指定されたのと同じプロファイルを使用してFirefoxを起動します。コマンドラインから実行できます：
     ```bash
     firefox --profile "/home/lzw/.mozilla/firefox/wzfodx6v.default"
     ```
   - または、Firefoxのプロファイルマネージャー（`firefox --ProfileManager`）を使用して `wzfodx6v.default` を選択します。

2. **ナビゲートしてチャレンジを通過する**:
   - ブラウザで「https://grok.com」に移動します。
   - Cloudflareの「Verify you are human」チェックボックスが表示されたら、それをクリックし、追加の検証ステップが表示された場合は完了させます。
   - メインページ（例: `aria-label="Ask Grok anything"` が付いたテキストエリアが表示されるページ）に到達するまで待ちます。

3. **ブラウザを閉じる**:
   - Firefoxを終了し、プロファイルがセッションCookie（Cloudflareのクリアランストークンである `cf_clearance` など）を保存するようにします。

4. **Seleniumスクリプトを実行する**:
   - スクリプトをそのまま実行します。同じプロファイルを使用しているため、保存されたCookieとセッションデータを継承し、チャレンジをバイパスできる可能性があります。

**これが機能する可能性がある理由**: Cloudflareは、ブラウザがテストを通過したことを記憶するためにCookieに依存することがよくあります。プロファイルを手動で事前認証することにより、自動化されたセッションが検証済みの訪問の継続として表示される可能性があります。

**制限事項**: Cloudflareが各ページロードで追加のチェック（例: Seleniumの自動化フィンガープリントの検出）を実行する場合、この方法は失敗する可能性があります。その場合は、次のアプローチを試してください。

---

### **方法 2: スクリプト内でのCookieの抽出と設定**
プロファイルの再利用が機能しない場合は、チャレンジ通過後に手動でCookieを抽出し、Seleniumドライバーに注入することができます。段階的なプロセスは以下の通りです：

1. **手動でチャレンジを通過する**:
   - 方法1のステップ1と2に従って、「https://grok.com」のメインページに到達します。

2. **Cookieを抽出する**:
   - FirefoxのDeveloper Tools（F12または右クリック＞検証）を開きます。
   - **Storage**タブ（または**Network**タブで、ページをリロードしてCookieを検査）に移動します。
   - `.grok.com` に関連するCookie、特に `cf_clearance`（Cloudflareの検証Cookie）を探します。
   - 関連する各Cookieの `name`、`value`、`domain` をメモします。例：
     - 名前: `cf_clearance`, 値: `abc123...`, ドメイン: `.grok.com`
     - `__cfduid` やセッション固有のCookieなど、他のCookieも存在する可能性があります。

3. **スクリプトを修正する**:
   - URLに移動する前に、SeleniumドライバーにCookieを追加します。コードを以下のように更新します：
     ```python
     # ... (既存のインポートとセットアップは変更なし)

     # geckodriverサービスをセットアップ
     service = Service(executable_path="/home/lzw/bin/geckodriver")
     driver = webdriver.Firefox(service=service, options=firefox_options)

     # 最初に空白ページを開いてCookieを設定（Cookieはページロード後にのみ設定可能）
     driver.get("about:blank")

     # 抽出したCookieを追加
     cookies = [
         {"name": "cf_clearance", "value": "abc123...", "domain": ".grok.com"},
         # 必要に応じて他のCookieを追加、例:
         # {"name": "__cfduid", "value": "xyz789...", "domain": ".grok.com"},
     ]
     for cookie in cookies:
         driver.add_cookie(cookie)

     # 次にターゲットURLに移動
     driver.get("https://grok.com")

     # ページのタイトルを表示
     print("Title of the page:", driver.title)

     # ... (スクリプトの残りは同じ)
     ```

4. **スクリプトをテストする**:
   - 修正したスクリプトを実行します。事前設定されたCookieにより、Cloudflareにブラウザが既にチャレンジを通過したことを通知できるはずです。

**これが機能する可能性がある理由**: `cf_clearance` Cookieを明示的に設定することで、検証済みセッションを模倣し、チェックボックスとの対話の必要性をバイパスできる可能性があります。

**制限事項**: Cookieはブラウザのフィンガープリント（例: ユーザーエージェント、IP、TLS設定）に関連付けられている可能性があります。Seleniumのフィンガープリントが手動セッションのものと異なる場合、CloudflareはCookieを拒否するか、ブラウザに再チャレンジする可能性があります。

---

### **追加のデバッグと機能強化**
どちらの方法でも問題が完全に解決しない場合は、Cloudflareチャレンジと正しく対話していることを確認するために、スクリプトに以下の調整を加えてください：

- **iframeの確認**: 「Verify you are human」チェックボックスがiframe内にある可能性があります。チェックボックスをクリックするコードを修正して、最初にiframeに切り替えてください：
  ```python
  try:
      wait = WebDriverWait(driver, 20)
      iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'cloudflare')]")))
      driver.switch_to.frame(iframe)
      label = wait.until(EC.presence_of_element_located((By.XPATH, "//label[@class='cb-lb']")))
      checkbox = label.find_element(By.TAG_NAME, "input")
      print("Checkbox found:", checkbox.is_displayed())
      checkbox.click()
      driver.switch_to.default_content()  # メインコンテンツに戻る
      print("Checkbox clicked.")
  except Exception as e:
      print("Checkbox not found or not clickable:", e)
  ```

- **待機ロジックの改善**: チェックボックスをクリックした後、チャレンジが通過した明確な兆候（例: 検証ページが消える）を待ちます：
  ```python
  try:
      wait.until(EC.invisibility_of_element_located((By.XPATH, "//*[contains(text(), 'Verify you are human')]")))
      print("Challenge passed.")
  except Exception as e:
      print("Challenge not passed:", e)
  ```

- **自動化のマスキング**: Seleniumの自動化痕跡を隠すためのJavaScriptを追加します：
  ```python
  driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
  ```

---

### **それでもダメな場合: 代替アプローチ**
Cloudflareの検出が持続する場合、現在のセットアップでは回避できない高度なフィンガープリンティングが原因である可能性があります。以下は、Firefoxの設定から逸脱しますが、エスカレーションオプションです：

- **Undetected ChromeDriverを使用したChromeへの切り替え**:
  - インストール: `pip install undetected-chromedriver`
  - セットアップを修正：
    ```python
    import undetected_chromedriver as uc
    driver = uc.Chrome()
    driver.get("https://grok.com")
    ```
  - このライブラリは、一般的な検出方法を回避するようにChromeにパッチを適用します。

- **プロキシまたはCAPTCHAソルバーの使用**: 2Captchaやレジデンシャルプロキシなどのサービスはチャレンジを処理できますが、複雑さとコストが増加します。

---

### **推奨される次のステップ**
既存のFirefox構成を最大限に活用し、新しいツールを必要としないため、最もシンプルでスクリプトのセットアップに沿った**方法1**（プロファイルの再利用）から始めてください。それが失敗した場合は、iframeチェックを追加した**方法2**（Cookie注入）を試してください。各アプローチをテストし、出力（例: `driver.title` と例外メッセージ）を監視して、チャレンジがバイパスされているか確認してください。それでも問題が解決しない場合は、プロジェクトの柔軟性に基づいて代替アプローチを検討してください。

これらのソリューションの実装やトラブルシューティングに助けが必要な場合は、お知らせください！