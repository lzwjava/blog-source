---
audio: false
date: 2025-09-07
generated: true
image: false
lang: ja
layout: post
title: ブロックされたGoogle Fontsリクエストの修正
translated: true
type: note
---

そのリクエストは、あなたのページが Google Fonts からウェブフォントのスタイルシートを読み込もうとしているものです：

* **内容:** `https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap` は、**Open Sans** フォントフェイスを定義する CSS です。あなたのテーマまたはカスタム CSS がこれを読み込んでいるため、サイトは Open Sans で表示されます。
* **「Status: — / 0 B / no headers」と表示される理由:** この表示は、リクエストが**ブロックまたはキャンセルされた**場合（例: 広告ブロッカー/プライバシーブロッカー、厳格な Content-Security-Policy、不安定なネットワーク、国レベルでのブロッキング）に DevTools が示すものです。ページは依然としてそれを*リクエストしようとする*ため、ネットワーク行に表示されます。

### Jekyll ブログで考えられる発生源

通常、以下のいずれかが該当します：

1. **テーマが `<head>` 内で読み込んでいる**
   `_layouts/default.html` または `_includes/head.html`（あるいは `remote_theme` を使用している場合はテーマの同等ファイル）内で、以下のような行を探してください：
   `<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap" rel="stylesheet">`

2. **SCSS でインポートしている**
   `/assets/css/*.scss` または `/_sass/**` 内で以下を確認してください：
   `@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap");`

3. **リモートテーマ** (例: jekyll-theme-cayman) が、その head インクルードに Google Fonts をハードコードしている。テーマの head/レイアウトをリポジトリ内でオーバーライドすれば削除できます。

### 素早く見つける方法

サイトのリポジトリルートから、以下のいずれかを実行してください：

```
rg -n "fonts.googleapis.com"
rg -n "Open Sans"
rg -n "display=swap"
```

### 修正または変更するためのオプション

**A) Google Fonts を削除してシステムフォントスタックを使用する (最速 & プライバシーに優しい)**

1.  Google Fonts を読み込んでいる `<link>`（または SCSS の `@import`）を削除します。
2.  メインのスタイルシートで、システムフォントスタックを設定します：

    ```css
    html, body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu,
                   "Helvetica Neue", Arial, "Noto Sans", sans-serif,
                   "Apple Color Emoji", "Segoe UI Emoji";
    }
    ```

    (Jekyll では、これを `assets/css/style.scss` に、先頭にフロントマターの `---` 行を付けて記述します。)

**B) Open Sans を維持するが、セルフホストする**

1.  Open Sans (400 & 700) の WOFF2 ファイルをダウンロードし、`assets/fonts/` 以下に配置します。
2.  CSS に以下を追加します：

    ```css
    @font-face {
      font-family: "Open Sans";
      font-style: normal;
      font-weight: 400;
      font-display: swap;
      src: url("/assets/fonts/OpenSans-400.woff2") format("woff2");
    }
    @font-face {
      font-family: "Open Sans";
      font-style: normal;
      font-weight: 700;
      font-display: swap;
      src: url("/assets/fonts/OpenSans-700.woff2") format("woff2");
    }
    body { font-family: "Open Sans", system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; }
    ```
3.  Google Fonts の `<link>`/`@import` を削除します。

**C) 現状のままにするが、リクエストの失敗を止める**

*   あなたのサイトに対してブロッキング拡張機能を無効にするか、CSP を緩和して `https://fonts.googleapis.com` と `https://fonts.gstatic.com` を許可します。
*   これらのドメインがブロックされている地域にいる場合は、A または B を優先してください。

### Jekyll 特有のオーバーライドのヒント

*   **リモートテーマ:** テーマの `/_includes/head.html` または `/_layouts/default.html` を同じパスでリポジトリにコピーし、Google Fonts の行を削除します。Jekyll はあなたのオーバーライドを使用します。
*   **ミニファイされた head インクルード:** 時々、テーマは変数を介してフォントを注入します。その場合は、その変数を空に設定するか、フォントを除外するようにインクルードをオーバーライドします。

あなたのテーマ名（または `_config.yml` の `theme` / `remote_theme`）を貼り付けて頂ければ、オーバーライドする正確なファイルと最小限の差分をお示しします。