---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: 自動化Jekyllビルド・デプロイワークフロー
translated: true
type: note
---

これは完全に GitHub Actions 内で実行できます。ランナー上でサイトをビルドし、宛先リポジトリをサブフォルダにチェックアウトして、`_site/` の内容をそこにプッシュします。

以下は、あなたの**ソース**リポジトリ（Python スクリプトと Jekyll コンテンツがある場所）に追加できるそのまま使えるワークフローです：

```yaml
# .github/workflows/build-and-deploy.yml
name: Build & Deploy Jekyll to External Repo

on:
  push:
    branches: [ main ]
  workflow_dispatch:

# 宛先リポジトリへのプッシュには PAT を使用します
permissions:
  contents: read

jobs:
  build-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Check out source repo
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.3'
          bundler-cache: true

      - name: Install Jekyll deps
        run: |
          bundle install --jobs 4 --retry 3

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Python deps
        if: hashFiles('requirements.txt') != ''
        run: pip install -r requirements.txt

      - name: Run your local workflow pipeline (CI mode)
        env:
          # スクリプトに必要なキーをここに追加してください
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
        run: |
          # スクリプトが調整するのと全く同じステップを実行します。
          # 必要であれば、スクリプトを直接呼び出すこともできます：
          python scripts/workflow_local.py
          # または、明示的なステップを好む場合は：
          # python scripts/generate/update_notes_link.py
          # python scripts/translation/update_lang.py --max_files 9 --model gemini-flash --commits 1000
          # python -m unittest discover -s tests/workflow
          # python scripts/release/update_release.py

      - name: Build Jekyll (to _site)
        run: |
          # もし Python モジュールが DEFAULT_DESTINATION を別の場所に設定している場合でも、ここで上書きできます。
          bundle exec jekyll build --destination _site

      - name: Check out destination repo
        uses: actions/checkout@v4
        with:
          repository: lzwjava/lzwjava.github.io   # <-- あなたの DESTINATION_REPO_URL ターゲット
          token: ${{ secrets.WORKFLOW_ACCESS_TOKEN }}      # <-- "repo" スコープを持つ PAT
          path: destination
          fetch-depth: 0

      - name: Sync built site to destination repo
        run: |
          mkdir -p destination/_site
          rsync -av --delete _site/ destination/_site/
          cd destination
          # オプション: Pages が再度 Jekyll を処理しないようにします
          touch _site/.nojekyll

          git config user.name  "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"

          if [ -n "$(git status --porcelain)" ]; then
            git add -A
            git commit --amend --no-edit
            # 宛先が別のブランチ（例: gh-pages）を使用している場合は調整してください
            git push --force-with-lease origin HEAD:main
          else
            echo "No changes to deploy."
          fi

      - name: (Optional) Upload built site artifact
        uses: actions/upload-artifact@v4
        with:
          name: site
          path: _site
```

### 設定が必要なもの

*   **宛先へのプッシュ用 PAT**: GitHub アカウントで `repo` スコープを持つクラシック Personal Access Token を作成する（または、宛先リポジトリへの書き込みアクセス権を付与する細かいトークンを使用する）。ソースリポジトリの設定で `WORKFLOW_ACCESS_TOKEN` として保存する（つまり、`Settings → Secrets and variables → Actions → New repository secret`）。
*   **ブランチとリポジトリ名**: `Check out destination repo` ステップで、`repository:` を外部リポジトリに設定する（公開または非公開でかまいません）。プッシュコマンドで、デプロイしたいブランチを設定する（多くの場合 `main` または `gh-pages`）。
*   **GitHub Pages 設定**（宛先リポジトリから提供する場合）: そのリポジトリの **Settings → Pages** で、正しい **Branch**（例: `main` / root）を選択し、`CNAME`/カスタムドメインを好みに応じて維持する。
*   **履歴に関する期待**: デプロイステップは最新のコミットを修正し、`--force-with-lease` を使用します。このブランチがデプロイアーティファクト専用であることを確認し、履歴の書き換えが受け入れられるようにしてください。

### Python スクリプトに関する注意点

*   CI では `open_destination_repo_in_browser()` は必要ないので、そのまま残しておいて問題ありません。ここでは呼び出されません。ワークフローはランナーから直接プッシュします。
*   CI では `push_destination_repo()` も必要ありません。ワークフローは 2 回目のチェックアウトとプッシュを処理するので、ローカル実行用にスクリプトを変更せずに維持できます。
*   もし `build_site()` が別の `DEFAULT_DESTINATION` に書き込む場合でも、上記の明示的な Jekyll ビルドステップを実行することで上書きできます。これは `_site/` に書き込みます。デプロイステップは `_site/` から同期します。

### 宛先リポジトリが非公開？

*   それでも問題ありません。GitHub Pages は公開リポジトリ（または Pages が有効な組織の公開ブランチ）のみを提供しますが、目的が何らかの理由で非公開リポジトリにアーティファクトをプッシュすることだけである場合は、上記の方法が引き続き機能します。Pages ホスティングを希望する場合は、その宛先リポジトリ/ブランチが Pages を提供するように設定されていることを確認する（必要な場合は公開にする）か、代替ホスト（例: Cloudflare Pages, Netlify）を使用してそこにデプロイしてください。

以上です。これで GitHub のランナー上でビルドし、`_site/` をクラウド内の別のリポジトリにプッシュできるようになります。