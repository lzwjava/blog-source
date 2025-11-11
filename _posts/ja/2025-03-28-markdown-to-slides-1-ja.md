---
audio: false
generated: true
image: false
lang: ja
layout: post
title: マークダウンからスライド作成を簡単に
translated: true
type: note
---

Marp CLI を使うと、Markdown ファイルをスライド (HTML, PDF, PPTX) に変換できます。最小限の書式設定でプレゼンテーションをプレーンな Markdown で書きたい場合に特に便利です。

ステップバイステップガイドは以下の通りです。

---

### 1. Marp CLI のインストール

まず Node.js が必要です。

```bash
npm install -g @marp-team/marp-cli
```

インストールを確認します：

```bash
marp --version
```

---

### 2. Markdown プレゼンテーションを書く

ファイルを作成します（例: `slides.md`）。

```markdown
---
marp: true
theme: default
paginate: true
---

# Hello, Marp!

---

## Slide 2

- Bullet 1
- Bullet 2
```

重要なポイント:

* `---` (YAML frontmatter) は Marp と設定を有効にします。
* `---` (コンテンツ間) はスライドを区切ります。

---

### 3. ブラウザでプレビュー

自動リロード付きのローカルサーバーを実行します：

```bash
marp -p slides.md
```

ブラウザで [http://localhost:8080](http://localhost:8080) を開きます。

---

### 4. スライドをエクスポート

様々な形式を生成します：

* HTML (自己完結型):

  ```bash
  marp slides.md -o slides.html
  ```

* PDF:

  ```bash
  marp slides.md -o slides.pdf
  ```

* PowerPoint (PPTX):

  ```bash
  marp slides.md -o slides.pptx
  ```

---

### 5. 便利なオプション

* **変更を監視** (自動リビルド):

  ```bash
  marp -w slides.md
  ```

* **テーマを設定** (default, gaia, uncover、またはカスタム CSS):

  ```bash
  marp --theme-set ./my-theme.css slides.md -o slides.html
  ```

* **スピーカーノートを含める**:

  ```markdown
  ---
  marp: true
  ---

  # Title

  <!--
  これはスピーカーノートです
  -->
  ```

---

### 6. エディタ統合

* VSCode には [Marp 拡張機能](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) があります。
* Markdown を編集しながらライブプレビューを表示します。

---

👉 このセットアップで、プレーンな `.md` ファイルから数分で洗練されたプレゼンテーションを作成できます。

**すぐに使い始められるテンプレート Markdown ファイル** (タイトルスライド、アジェンダ、コンテンツ、クロージングスライド付き) を提供しましょうか？