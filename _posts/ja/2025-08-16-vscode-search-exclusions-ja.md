---
audio: false
generated: true
image: false
lang: ja
layout: post
title: VS Codeで検索除外をカスタマイズ
translated: true
type: note
---

VS Codeでは、グローバルファイル検索は設定した**検索除外**を尊重します。特定のファイルやフォルダを検索結果に表示しないように無視するよう設定できます。

主な方法は以下の通りです：

---

### 1. **settings.json**で`search.exclude`を使用する

設定を開き（`⌘,` / `Ctrl+,` → 右上の「設定(JSON)を開く」）、以下を追加：

```json
"search.exclude": {
  "**/node_modules": true,
  "**/dist": true,
  "**/*.log": true
}
```

* キーは[グロブパターン](https://code.visualstudio.com/docs/editor/codebasics#_advanced-search-options)です。
* `true`は「検索から除外」を意味します。
* 例：

  * `**/node_modules` → すべてのnode_modulesフォルダ
  * `**/*.log` → 任意の場所にあるすべての`.log`ファイル
  * `**/build/**` → buildフォルダ内のすべて

---

### 2. `.gitignore`を使用する

プロジェクトに`.gitignore`がある場合、VS Codeに検索中にそれを尊重するよう指示できます：

```json
"search.useIgnoreFiles": true
```

これにより、Gitで無視されたものは検索結果に表示されません。

---

### 3. `.ignore`を使用する

プロジェクトルートに（`.gitignore`と同じ形式で）特にエディタツーリング用の`.ignore`ファイルを作成できます。`search.useIgnoreFiles`が有効な場合、VS Codeはこれを尊重します。

---

### 4. 検索UIでクイック除外

検索時、結果内のファイル/フォルダにホバーして**「除外」**をクリックします。これにより、そのパスが設定の`search.exclude`に一時的に追加されます。

---

👉 したがって、最も一般的な設定は：

* プロジェクト全体で一般的な無視を`.gitignore`に追加。
* エディタ固有の無視（`dist`、`.vscode`など）を`search.exclude`に追加。

---

**検索時のみ除外**して、それらのファイルをエクスプローラーには残す方法、またはエクスプローラーのサイドパネルからも非表示にする方法について説明しましょうか？