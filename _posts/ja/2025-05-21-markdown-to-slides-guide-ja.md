---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Markdownスライドクイックガイド
translated: true
type: note
---

Marp CLIを使うと、Markdownファイルをスライド（HTML、PDF、PPTX）に変換できます。最小限の書式設定でプレゼンテーションをプレーンなMarkdownで書きたい場合に特に便利です。

ステップバイステップガイドは以下の通りです：

---

### 1. Marp CLIのインストール

まずNode.jsが必要です。

```bash
npm install -g @marp-team/marp-cli
```

インストールを確認：

```bash
marp --version
```

---

### 2. Markdownプレゼンテーションの作成

ファイルを作成します（例：`slides.md`）。

```markdown
---
marp: true
theme: default
paginate: true
---

# Hello, Marp!

---

## スライド 2

- 箇条書き 1
- 箇条書き 2
```

重要なポイント：

* `---`（YAML frontmatter）はMarpと設定を有効にします。
* `---`（コンテンツ間）はスライドを区切ります。

---

### 3. ブラウザでプレビュー

自動リロード付きのローカルサーバーを実行：

```bash
marp -p slides.md
```

ブラウザで [http://localhost:8080](http://localhost:8080) を開きます。

---

### 4. スライドのエクスポート

様々な形式を生成：

* HTML（自己完結型）：

  ```bash
  marp slides.md -o slides.html
  ```

* PDF：

  ```bash
  marp slides.md -o slides.pdf
  ```

* PowerPoint（PPTX）：

  ```bash
  marp slides.md -o slides.pptx
  ```

---

### 5. 便利なオプション

* **変更の監視**（自動リビルド）：

  ```bash
  marp -w slides.md
  ```

* **テーマの設定**（default、gaia、uncover、またはカスタムCSS）：

  ```bash
  marp --theme-set ./my-theme.css slides.md -o slides.html
  ```

* **スピーカーノートを含める**：

  ```markdown
  ---
  marp: true
  ---

  # タイトル

  <!--
  これはスピーカーノートです
  -->
  ```

---

### 6. エディタ統合

* VSCodeには[Marp拡張機能](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)があります。
* Markdown編集時にライブプレビューを表示します。

---

👉 このセットアップで、プレーンな`.md`ファイルから数分で洗練されたプレゼンテーションを作成できます。

**すぐに使い始められるテンプレートMarkdownファイル**（タイトルスライド、アジェンダ、コンテンツ、クロージングスライド付き）を提供しましょうか？