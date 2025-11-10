---
audio: false
generated: true
lang: hant
layout: post
title: 加速 Jekyll 構建：探索多線程方法
translated: true
type: note
---

Jekyll 的建置過程預設為單線程，對於大型網站來說可能會很慢。雖然 Jekyll 中沒有內建的多線程建置設定選項，但您可以探索一些方法來實現平行處理。下面，我根據現有資訊和技術考量，概述了可能性、挑戰和實際步驟。

### 為什麼 Jekyll 建置是單線程的
Jekyll 依序處理頁面，以確保依賴項（如 `site.related_posts` 或 Liquid 模板）能正確處理。某些組件（例如 Liquid 和某些外掛）可能不是線程安全的，這使得多線程變得複雜 ()。這種設計優先考慮正確性而非速度，但對於大型網站，這可能導致建置時間長達數分鐘 (,)。[](https://github.com/jekyll/jekyll/issues/9485)[](https://github.com/jekyll/jekyll/issues/1855)[](https://github.com/jekyll/jekyll/issues/4297)

### 實現多線程 Jekyll 建置的方法
以下是在 Jekyll 建置中引入平行處理的潛在方法，特別是在像您提供的 GitHub Actions 工作流程的背景下：

#### 1. **使用自訂外掛進行多線程渲染**
有人提出了一個用於多線程渲染的概念驗證外掛 ()。在一個測試案例中，它將建置時間從 45 秒減少到 10 秒，但存在線程安全問題，導致頁面內容不正確。此外掛還與依賴順序渲染的外掛（如 `jekyll-feed`）發生衝突。[](https://github.com/jekyll/jekyll/issues/9485)

**嘗試自訂外掛的步驟：**
- **建立外掛**：實作一個 Ruby 外掛，擴展 Jekyll 的 `Site` 類別以平行化頁面渲染。例如，您可以修改 `render_pages` 方法以使用 Ruby 的 `Thread` 類別或線程池 ()。[](https://github.com/jekyll/jekyll/issues/9485)
  ```ruby
  module Jekyll
    module UlyssesZhan::MultithreadRendering
      def render_pages(*args)
        @rendering_threads = []
        super # 呼叫原始方法
        @rendering_threads.each(&:join) # 等待線程完成
      end
    end
  end
  Jekyll::Site.prepend(Jekyll::UlyssesZhan::MultithreadRendering)
  ```
- **添加到 Gemfile**：將外掛放在您的 `_plugins` 目錄中，並確保 Jekyll 載入它。
- **測試線程安全性**：由於 Liquid 和某些外掛（例如 `jekyll-feed`）可能會出錯，請徹底測試。您可能需要修補 Liquid 或對某些功能避免使用多線程 ()。[](https://github.com/jekyll/jekyll/issues/9485)
- **與 GitHub Actions 整合**：更新您的工作流程以在您的儲存庫中包含此外掛。確保 `jekyll-build-pages` 操作使用您的自訂 Jekyll 設定：
  ```yaml
  - name: Build with Jekyll
    uses: actions/jekyll-build-pages@v1
    with:
      source: ./
      destination: ./_site
    env:
      BUNDLE_GEMFILE: ./Gemfile # 確保使用包含外掛的自訂 Gemfile
  ```

**挑戰**：
- 與 Liquid 和外掛（如 `jekyll-feed`）的線程安全問題 ()。[](https://github.com/jekyll/jekyll/issues/9485)
- 可能導致頁面渲染不正確（例如，一個頁面的內容出現在另一個頁面中）。
- 需要 Ruby 專業知識來除錯和維護。

#### 2. **使用多個配置平行化建置**
與其多線程單一建置，您可以將網站拆分為較小的部分（例如，按集合或目錄），並使用多個 Jekyll 程序平行建置它們。這種方法避免了線程安全問題，但需要更多設定。

**步驟**：
- **拆分網站**：將您的網站組織成集合（例如 `posts`、`pages`、`docs`）或目錄，並為每個部分建立獨立的 `_config.yml` 檔案 (,)。[](https://amcrouch.medium.com/configuring-environments-when-building-sites-with-jekyll-dd6eb2603c39)[](https://coderwall.com/p/tfcj2g/using-different-build-configuration-in-jekyll-site)
  ```yaml
  # _config_posts.yml
  collections:
    posts:
      output: true
  destination: ./_site/posts

  # _config_pages.yml
  collections:
    pages:
      output: true
  destination: ./_site/pages
  ```
- **更新 GitHub Actions 工作流程**：修改您的工作流程以平行執行多個 Jekyll 建置，每個建置使用不同的配置檔案。
  ```yaml
  name: Build Jekyll Site
  on:
    push:
      branches: [main]
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - name: Setup Ruby
          uses: ruby/setup-ruby@v1
          with:
            ruby-version: '3.1'
            bundler-cache: true
        - name: Build Posts
          run: bundle exec jekyll build --config _config_posts.yml
        - name: Build Pages
          run: bundle exec jekyll build --config _config_pages.yml
        - name: Combine Outputs
          run: |
            mkdir -p ./_site
            cp -r ./_site/posts/* ./_site/
            cp -r ./_site/pages/* ./_site/
        - name: Deploy
          uses: actions/upload-artifact@v4
          with:
            name: site
            path: ./_site
  ```
- **合併輸出**：在平行建置後，將輸出目錄合併到單一的 `_site` 資料夾中以進行部署。

**挑戰**：
- 管理集合之間的相互依賴性（例如 `site.related_posts`）。
- 配置和部署的複雜性增加。
- 對於具有緊密耦合內容的網站，可能擴展性不佳。

#### 3. **對大型網站使用線程池**
一個針對 `amp-jekyll` 外掛的 pull request 建議使用線程池來處理頁面，並可配置線程數量以避免系統超載 ()。這種方法在效能和資源使用之間取得平衡。[](https://github.com/juusaw/amp-jekyll/pull/26)

**步驟**：
- **實作線程池**：修改或建立一個外掛以使用 Ruby 的 `Thread::Queue` 來管理固定數量的工作線程（例如 4 或 8，取決於您的系統）。
  ```ruby
  require 'thread'

  module Jekyll
    module ThreadPoolRendering
      def render_pages(*args)
        queue = Queue.new
        site.pages.each { |page| queue << page }
        threads = (1..4).map do # 4 個線程
          Thread.new do
            until queue.empty?
              page = queue.pop(true) rescue nil
              page&.render_with_liquid(site)
            end
          end
        end
        threads.each(&:join)
        super
      end
    end
  end
  Jekyll::Site.prepend(Jekyll::ThreadPoolRendering)
  ```
- **添加配置選項**：允許使用者在 `_config.yml` 中切換多線程或設定線程數量：
  ```yaml
  multithreading:
    enabled: true
    thread_count: 4
  ```
- **與工作流程整合**：確保外掛包含在您的儲存庫中，並在 GitHub Actions 建置期間載入。

**挑戰**：
- 與第一種方法類似的線程安全問題。
- 對於具有許多短任務的大型網站，上下文切換開銷 ()。[](https://github.com/juusaw/amp-jekyll/pull/26)
- 需要測試以確保與所有外掛的相容性。

#### 4. **在不使用多線程的情況下進行優化**
如果多線程過於複雜或風險太高，您可以優化單線程建置過程：
- **啟用增量建置**：使用 `jekyll build --incremental` 僅重建已變更的檔案 (,)。添加到您的工作流程：[](https://github.com/jekyll/jekyll/blob/master/lib/jekyll/commands/build.rb)[](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)
  ```yaml
  - name: Build with Jekyll
    uses: actions/jekyll-build-pages@v1
    with:
      source: ./
      destination: ./_site
      incremental: true
  ```
- **減少外掛使用**：自訂外掛可能會顯著減慢建置速度 ()。稽核並移除不必要的內掛。[](https://github.com/jekyll/jekyll/issues/4297)
- **使用更快的轉換器**：從 Kramdown 切換到更快的 markdown 處理器，如 CommonMark，或針對特定使用案例測試 Pandoc ()。[](https://github.com/jekyll/jekyll/issues/9485)
- **快取依賴項**：在您的 GitHub Actions 工作流程中確保 `bundler-cache: true` 以避免重新安裝 gem ()。[](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)

### 建議
- **從增量建置開始**：這是在不冒線程安全風險的情況下加速建置的最簡單方法。將 `--incremental` 添加到您的工作流程並測試其影響。
- **嘗試線程池外掛**：如果您具備 Ruby 專業知識，嘗試實作一個具有可配置線程數量的線程池外掛（選項 3）。首先在一個小網站上測試線程安全性。
- **暫時避免完全多線程**：考慮到 Liquid 和外掛的線程安全問題 ()，完全多線程可能需要大量重構或自訂 Liquid 分支，除非您參與 Jekyll 核心開發，否則可能不實用。[](https://github.com/jekyll/jekyll/issues/9485)
- **監控建置時間**：使用 GitHub Actions 日誌來測量建置時間並識別瓶頸。例如，一個需要 6 分鐘建置的網站 () 表明外掛或大型資源處理可能是問題所在。[](https://github.com/jekyll/jekyll/issues/1855)

### 使用增量建置的 GitHub Actions 範例
這是您的工作流程的更新版本，啟用了增量建置：
```yaml
name: Build Jekyll Site
on:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.1'
          bundler-cache: true
      - name: Build with Jekyll
        uses: actions/jekyll-build-pages@v1
        with:
          source: ./
          destination: ./_site
          incremental: true
      - name: Deploy
        uses: actions/upload-artifact@v4
        with:
          name: site
          path: ./_site
```

### 注意事項
- **線程安全**：Jekyll 中的多線程是實驗性的，可能會破壞外掛或產生不正確的輸出 ()。首先在一個小網站上徹底測試。[](https://github.com/jekyll/jekyll/issues/9485)
- **GitHub Actions 限制**：平行建置（選項 2）會增加資源使用量，因此請確保您的工作流程保持在 GitHub 免費層限制內。
- **Jekyll 5 的潛力**：未來版本的 Jekyll 可能會原生解決多線程問題，因為已經討論過 ()。目前，需要自訂解決方案。[](https://github.com/jekyll/jekyll/issues/9485)

如果您需要幫助實作特定方法（例如編寫外掛或拆分建置），請告訴我，我可以提供更詳細的指導或程式碼！