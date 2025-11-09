---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: GitHub Actions プッシュ認証エラーの修正
translated: true
type: note
---

その403エラーは、プッシュが **書き込み権限のないトークンを使用して `lzwjava` として認証している** ことを意味します（多くの場合、ジョブがまだデフォルトの `GITHUB_TOKEN` を使用しており、別のリポジトリにプッシュできないことが原因です）。**宛先のチェックアウト/プッシュ用に実際の認証情報を注入して**修正します。

以下に3つの確実な方法を示します。1つを選んでください。最も簡単な方法から紹介します。

---

### オプション A — PATを使用してリモートに埋め込む（最速）

1. **クラシックPAT** を `repo` スコープで作成する（または、**コンテンツ: 読み取りと書き込み**権限を `lzwjava/lzwjava.github.io` に付与したファイングレインドPAT）。ソースリポジトリの `DEPLOY_TOKEN` シークレットとして保存します。

2. ワークフローのデプロイステップを更新し、**リモートがそのトークンを強制的に使用するように**します：

```yaml
- name: 宛先リポジトリをチェックアウト
  uses: actions/checkout@v4
  with:
    repository: lzwjava/lzwjava.github.io
    token: ${{ secrets.DEPLOY_TOKEN }}
    path: destination
    fetch-depth: 0

- name: ビルドしたサイトを宛先にプッシュ
  run: |
    rsync -av --delete _site/ destination/
    cd destination
    touch .nojekyll

    git config user.name  "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"

    # リモートがPATを明示的に使用するように強制（credential-helperの競合を回避）
    git remote set-url origin https://${{ secrets.DEPLOY_TOKEN }}@github.com/lzwjava/lzwjava.github.io.git

    if [ -n "$(git status --porcelain)" ]; then
      git add -A
      git commit -m "deploy: ${GITHUB_SHA}"
      git push origin HEAD:main
    else
      echo "No changes to deploy."
    fi
```

それでも403エラーが表示される場合は、PATにスコープが不足しているか、（リポジトリがOrganization内にある場合）SSO承認が必要です。`repo` スコープで再生成して再試行してください。

---

### オプション B — 認証情報の混入を避ける：最初のチェックアウトでデフォルトの認証情報を無効化する

**最初のチェックアウト**がデフォルトの `GITHUB_TOKEN` をcredential helperに書き込み、後で再利用されてしまうことがあります。これを無効にします：

```yaml
- name: ソースリポジトリをチェックアウト
  uses: actions/checkout@v4
  with:
    fetch-depth: 0
    persist-credentials: false   # <- 重要
```

その後、オプションAで示したように、PATを使用した宛先のチェックアウトを続行します（動作する場合は `remote set-url` 行をスキップできますが、あっても問題ありません）。

---

### オプション C — SSHデプロイキー（非常に堅牢）

1. お使いのマシンで： `ssh-keygen -t ed25519 -C "deploy@actions" -f deploy_key`
2. **公開鍵** (`deploy_key.pub`) を、**書き込み権限**付きの **デプロイキー** として `lzwjava/lzwjava.github.io` に追加します。
3. **秘密鍵** (`deploy_key`) を、**ソース**リポジトリの `ACTIONS_DEPLOY_KEY` シークレットとして追加します。

ワークフロー：

```yaml
- name: SSH経由で宛先リポジトリをチェックアウト
  uses: actions/checkout@v4
  with:
    repository: lzwjava/lzwjava.github.io
    ssh-key: ${{ secrets.ACTIONS_DEPLOY_KEY }}
    path: destination
    fetch-depth: 0

- name: ビルドしたサイトをプッシュ (SSH)
  run: |
    rsync -av --delete _site/ destination/
    cd destination
    touch .nojekyll
    git config user.name  "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"
    if [ -n "$(git status --porcelain)" ]; then
      git add -A
      git commit -m "deploy: ${GITHUB_SHA}"
      git push origin HEAD:main
    else
      echo "No changes to deploy."
    fi
```

---

### 再度失敗した場合の簡単な診断

プッシュの直前に以下を実行して、実際にどの認証が設定されているかを確認します：

```bash
cd destination
git remote -v
git config --get user.name
git config --get user.email
git config --get url.https://github.com/.insteadof || true
git config --global --list | sed -n 's/^credential\.helper.*/&/p'
```

`remote -v` が、PATが注入されていない（オプションA）プレーンな `https://github.com/...`、または `git@github.com:`（オプションC）ではないものを表示する場合、間違った認証情報をまだ使用しています。

---

### よくある落とし穴

* **ファイングレインドPAT** は、**その特定のリポジトリ**に対して **コンテンツ: 読み取りと書き込み** を明示的に付与する必要があります。
* `main` ブランチの **ブランチ保護** がボットのプッシュをブロックすることがあります（必須のチェック/署名）。その場合は、保護されていないブランチ（例: `gh-pages`）にデプロイするか、ルールを調整してください。
* **PATの有効期限切れ** → 再生成してください。
* **OrganizationのSSO**（ユーザーリポジトリの場合は該当なし） → PATに対してOrganizationの承認を行ってください。

上記の3つのオプションのいずれかを実行すれば、403エラーは解消されます。