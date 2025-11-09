---
audio: false
date: 2025-09-07
generated: true
image: false
lang: ja
layout: post
title: カヤマテーマでのGoogle Fontsインポート
translated: true
type: note
---

はい — それがおそらく原因です。

以下のように記述すると:

```scss
@import "jekyll-theme-cayman";
```

単にローカルのSCSSを読み込んでいるだけでなく、**テーマのスタイルシート全体**をインポートしています。これにはGoogle Fontsのインポートが含まれている（またはリンクされている）のです。Caymanはデフォルトフォントとして **Open Sans** を使用し、それを `https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap` から取得します。

したがって、流れは以下のようになります:

1.  あなたのSCSSが `@import "jekyll-theme-cayman";` と記述。
2.  Jekyllがそれをテーマの `_sass` ファイルに展開。
3.  CaymanのSCSS内に、以下のような行が含まれている:

    ```scss
    @import url("https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap");
    ```
4.  これがDevToolsで確認しているネットワークリクエストの正体です。

---

### 削除または上書きする方法

*   **フォントのインポートを上書き**: テーマのメインSCSSをプロジェクトにコピーし（例: `assets/css/style.scss`）、Google Fontsの行を削除してから、Jekyllにそれをインポートしないように指示します。

*   **フォントファミリーのみを上書き**: Caymanの他の部分は保持したまま、独自のCSSでシステムフォントスタックを強制します:

    ```css
    html, body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu,
                   "Helvetica Neue", Arial, "Noto Sans", sans-serif;
    }
    ```

    これにより、Google Fontsのリクエストが発生しても、ブラウザはそれを使用しません。

*   **Open Sansをセルフホスト**: Open Sansが好きだが外部呼び出しを避けたい場合は、フォントファイルをダウンロードし、独自のCSSで `@font-face` を使用して定義し、Caymanの `@import url(...)` を削除します。

---

👉 必要であれば、Google Fontsの行がCaymanのどのSCSSファイルにあるか、そしてあなたのJekyll設定でそれをクリーンに上書きする方法を具体的にお見せできます。ステップバイステップで説明しましょうか？