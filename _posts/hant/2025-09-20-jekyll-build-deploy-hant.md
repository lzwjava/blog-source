---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 自動化 Jekyll 建置與部署工作流程
translated: true
type: note
---

你可以完全在 GitHub Actions 中完成：在 runner 上建置網站，然後將目標儲存庫檢出到子資料夾中，並將 `_site/` 的內容推送至該處。

以下是一個可直接使用的工作流程，你可以將其新增至你的**來源**儲存庫（即你的 Python 腳本和 Jekyll 內容所在的位置）：

```yaml
# .github/workflows/build-and-deploy.yml
name: 建置並部署 Jekyll 至外部儲存庫

on:
  push:
    branches: [ main ]
  workflow_dispatch:

# 我們將使用 PAT 來推送至目標儲存庫
permissions:
  contents: read

jobs:
  build-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: 檢出來源儲存庫
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: 設定 Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.3'
          bundler-cache: true

      - name: 安裝 Jekyll 相依套件
        run: |
          bundle install --jobs 4 --retry 3

      - name: 設定 Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: 安裝 Python 相依套件
        if: hashFiles('requirements.txt') != ''
        run: pip install -r requirements.txt

      - name: 執行本地工作流程管線 (CI 模式)
        env:
          # 在此處新增你的腳本所需的任何金鑰
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
        run: |
          # 執行與你的腳本編排完全相同的步驟。
          # 如果你願意，可以直接呼叫你的腳本：
          python scripts/workflow_local.py
          # 或者，如果你偏好明確的步驟：
          # python scripts/generate/update_notes_link.py
          # python scripts/translation/update_lang.py --max_files 9 --model gemini-flash --commits 1000
          # python -m unittest discover -s tests/workflow
          # python scripts/release/update_release.py

      - name: 建置 Jekyll (至 _site)
        run: |
          # 如果你的 Python 模組在其他地方設定了 DEFAULT_DESTINATION，你仍然可以在這裡覆寫。
          bundle exec jekyll build --destination _site

      - name: 檢出目標儲存庫
        uses: actions/checkout@v4
        with:
          repository: lzwjava/lzwjava.github.io   # <-- 你的 DESTINATION_REPO_URL 目標
          token: ${{ secrets.WORKFLOW_ACCESS_TOKEN }}      # <-- 具有 "repo" 範圍的 PAT
          path: destination
          fetch-depth: 0

      - name: 同步已建置的網站至目標儲存庫
        run: |
          mkdir -p destination/_site
          rsync -av --delete _site/ destination/_site/
          cd destination
          # 可選：確保 Pages 不會再次處理 Jekyll
          touch _site/.nojekyll

          git config user.name  "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"

          if [ -n "$(git status --porcelain)" ]; then
            git add -A
            git commit --amend --no-edit
            # 如果你的目標使用其他分支（例如 gh-pages），請調整分支
            git push --force-with-lease origin HEAD:main
          else
            echo "No changes to deploy."
          fi

      - name: (可選) 上傳已建置的網站成品
        uses: actions/upload-artifact@v4
        with:
          name: site
          path: _site
```

### 你需要設定的項目

* **用於目標推送的 PAT**：在你的 GitHub 帳戶上建立一個具有 `repo` 範圍的經典 Personal Access Token（或使用授予目標儲存庫寫入權限的 fine-grained token）。將其以 `WORKFLOW_ACCESS_TOKEN` 的名稱儲存在來源儲存庫的設定中（即 `Settings → Secrets and variables → Actions → New repository secret`）。
* **分支和儲存庫名稱**：在 `檢出目標儲存庫` 步驟中，將 `repository:` 設定為外部儲存庫（可以是公開或私有的）。在推送指令中，設定你想要部署至的分支（通常是 `main` 或 `gh-pages`）。
* **GitHub Pages 設定**（如果你要從目標儲存庫提供服務）：在該儲存庫的 **Settings → Pages** 中，選擇正確的 **Branch**（例如 `main` / root），並按需保留 `CNAME`/自訂網域。
* **歷史記錄預期**：部署步驟會修訂最新提交並使用 `--force-with-lease`；請確保該分支專用於部署成品，以便重寫歷史記錄是可接受的。

### 關於你的 Python 腳本的注意事項

* 在 CI 中你不需要 `open_destination_repo_in_browser()`，因此保持原樣即可；它在此處不會被呼叫。工作流程會直接從 runner 推送。
* 在 CI 中你也不需要 `push_destination_repo()`。工作流程會處理第二次檢出和推送，因此你可以保持腳本不變以用於本地執行。
* 如果你的 `build_site()` 寫入到不同的 `DEFAULT_DESTINATION`，你仍然可以透過執行上述明確的 Jekyll 建置步驟來覆寫，該步驟會寫入 `_site/`。部署步驟會從 `_site/` 同步。

### 目標儲存庫是私有的？

* 沒問題。GitHub Pages 僅服務公開儲存庫（或具有 Pages 啟用的組織中的公開分支），但如果你的目標只是為了任何原因將成品推送至私有儲存庫，上述方法仍然有效。如果你確實需要 Pages 託管，請確保目標儲存庫/分支已設定為提供 Pages 服務（在需要時公開），或使用替代主機（例如 Cloudflare Pages、Netlify）並部署到那裡。

就是這樣——你現在可以在 GitHub 的 runner 上建置，並將 `_site/` 推送至雲端的另一個儲存庫。