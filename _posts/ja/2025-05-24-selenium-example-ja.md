---
audio: false
generated: true
lang: ja
layout: post
title: セレニウムスクリプト
translated: true
type: note
---

以下は、高度な機能を備えたPythonのSeleniumスクリプトの洗練された例です。Page Object Model（POM）、レスポンシブレイアウトのための明示的なFacetGrid、明示的待機、動的コンテンツの処理、エラーハンドリングなどを実演しています。このスクリプトは、eコマースウェブサイトから商品データをスクレイピングし、複数のページをナビゲートし、サマリーレポートを生成する複雑なシナリオを自動化します。この例はデモンストレーションのための仮想的なeコマースウェブサイトを想定していますが、概念は実際のウェブサイトに適応できます。

この例が示すもの:
- **Page Object Model (POM)** - 整理され保守しやすいコードのため。
- **明示的待機** - 動的コンテンツを扱うため。
- **FacetGrid** - レスポンシブなテーブル操作のため。
- **ヘッドレスブラウザ** - 効率的な実行のため。
- **データ処理** - JSONレポートを生成するため。
- **エラーハンドリング** - 堅牢性のため。

```python
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

# 商品一覧ページのページオブジェクト
class ProductListingPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_cards = (By.CLASS_NAME, "product-card")
        self.product_name = (By.CLASS_NAME, "product-name")
        self.product_price = (By.CLASS_NAME, "product-price")
        self.next_page_button = (By.ID, "next-page")
        self.sort_dropdown = (By.ID, "sort-options")

    def sort_by_price(self):
        try:
            sort_select = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.sort_dropdown)
            )
            select = Select(sort_select)
            select.select_by_value("price-asc")
            time.sleep(2)  # ソートが適用されるのを待機
        except TimeoutException:
            print("ソートドロップダウンが見つからないかタイムアウトしました")

    def get_products(self):
        try:
            cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.product_cards)
            )
            products = []
            for card in cards:
                name = card.find_element(*self.product_name).text
                price = card.find_element(*self.product_price).text
                products.append({"name": name, "price": price})
            return products
        except (TimeoutException, NoSuchElementException) as e:
            print(f"商品の取得中にエラーが発生しました: {e}")
            return []

    def go_to_next_page(self):
        try:
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.next_page_button)
            )
            next_button.click()
            time.sleep(2)  # ページ読み込みを待機
            return True
        except TimeoutException:
            print("次のページボタンが見つからないかタイムアウトしました")
            return False

# 検索ページのページオブジェクト
class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.ID, "search-bar")
        self.search_button = (By.ID, "search-submit")

    def search(self, query):
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.search_input)
            )
            search_box.clear()
            search_box.send_keys(query)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.search_button)
            ).click()
            time.sleep(2)  # 検索結果を待機
        except TimeoutException as e:
            print(f"検索に失敗しました: {e}")

# メインスクリプト
def scrape_ecommerce_site():
    # ヘッドレスChromeをセットアップ
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    all_products = []

    try:
        # ウェブサイトにナビゲート
        driver.get("https://example.com")
        
        # ページオブジェクトを初期化
        search_page = SearchPage(driver)
        product_page = ProductListingPage(driver)
        
        # 検索を実行
        search_page.search("laptop")
        
        # 価格でソート
        product_page.sort_by_price()
        
        # 複数ページをスクレイピング
        page_count = 0
        max_pages = 3  # デモ用の制限
        
        while page_count < max_pages:
            products = product_page.get_products()
            all_products.extend(products)
            print(f"ページ {page_count + 1} をスクレイピング: {len(products)} 商品")
            
            if not product_page.go_to_next_page():
                break
            page_count += 1

        # サマリーを生成
        summary = {
            "total_products": len(all_products),
            "average_price": calculate_average_price(all_products),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # 結果をJSONに保存
        with open("product_data.json", "w") as f:
            json.dump({"products": all_products, "summary": summary}, f, indent=2)
        print("結果を product_data.json に保存しました")

    except Exception as e:
        print(f"エラーが発生しました: {e}")
    
    finally:
        driver.quit()

def calculate_average_price(products):
    if not products:
        return 0
    prices = []
    for product in products:
        try:
            price_str = product["price"].replace("$", "").replace(",", "")
            prices.append(float(price_str))
        except (ValueError, AttributeError):
            continue
    return sum(prices) / len(prices) if prices else 0

if __name__ == "__main__":
    scrape_ecommerce_site()
```

### 例の説明
1. **Page Object Model (POM)**:
   - スクリプトは2つのページオブジェクトクラス（`SearchPage` と `ProductListingPage`）を使用して、ページ固有のロジックをカプセル化し、コードをモジュール化して保守しやすくしています。
   - 各クラスには、特定のページ要素と対話するためのロケーターとメソッドが含まれています。

2. **ヘッドレスブラウザ**:
   - スクリプトは効率性のためにChromeをヘッドレスモードで実行し、CI/CDパイプラインやサーバーに適しています。

3. **明示的待機**:
   - `WebDriverWait` と `expected_conditions` を使用して動的コンテンツを扱い、要素が対話可能になる前に存在することを保証します。

4. **レスポンシブテーブル処理**:
   - スクリプトはFacetGridに似たロジックを使用して商品一覧テーブルをスクレイピングし、各カードから商品名と価格を抽出します。
   - ページネーションを処理し、複数のページをナビゲートします（この例では最大3ページまで）。

5. **エラーハンドリング**:
   - スクリプトは `TimeoutException` と `NoSuchElementException` をキャッチして、要素が見つからない場合やタイムアウトの場合を適切に処理します。
   - `try-finally` ブロックにより、エラーが発生してもブラウザが確実に閉じられます。

6. **データ処理**:
   - スクレイピングしたデータは辞書のリストに保存され、要約されます（例：総商品数、平均価格）。
   - 結果はさらに使用するためにJSONファイル（`product_data.json`）に保存されます。

7. **動的ソート**:
   - スクリプトはドロップダウンと対話して商品を価格でソートし、実際のユーザーの行動をシミュレートします。

### 出力
スクリプトは以下の構造のJSONファイル（`product_data.json`）を生成します:
```json
{
  "products": [
    {"name": "Laptop Model A", "price": "$999.99"},
    {"name": "Laptop Model B", "price": "$1299.99"},
    ...
  ],
  "summary": {
    "total_products": 30,
    "average_price": 1099.45,
    "timestamp": "2025-05-24 21:33:00"
  }
}
```

### 注意点
- **ウェブサイトへの適応**: ロケーター（`By.ID`, `By.CLASS_NAME`）とURL（`https://example.com`）はプレースホルダーです。ターゲットウェブサイトのHTML構造から実際の値に置き換えてください。これはブラウザの開発者ツールを使用して調べることができます。
- **依存関係**: `selenium` がインストールされていること（`pip install selenium`）、および適切なブラウザドライバ（例：ChromeDriver）がPATHにあることを確認してください。
- **改善点**:
  - より良いデバッグのためのロギングを追加。
  - 不安定なネットワークリクエストのためのリトライロジックを実装。
  - ロケーターと設定のための設定ファイルを使用。
  - 認証やCAPTCHAなどのより複雑なシナリオを扱うように拡張。

### スクリプトの実行方法
1. 依存関係をインストール: `pip install selenium`
2. ChromeDriverをダウンロードして設定
3. URLとロケーターを実際のeコマースサイト（例：Amazon、eBay）のものに置き換える
4. スクリプトを実行: `python advanced_selenium_ecommerce_scraper.py`

この例は、ベストプラクティスに沿った本番環境対応のSeleniumスクリプトを示しています。特定のウェブサイトへの適応や、認証やSelenium Gridを用いた並列実行などの機能の追加についてサポートが必要な場合はお知らせください！