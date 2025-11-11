---
audio: false
generated: true
lang: ja
layout: post
title: curlダウンロードのトラブルシューティング
translated: true
type: note
---

`curl -O` を使用して eclipse.org から Eclipse ZIP ファイルをダウンロードしようとすると、目的の ZIP ファイルではなく HTML ファイルがダウンロードされ、「301 Moved Permanently」エラーが発生することがあります。これは、使用している URL が別の場所にリダイレクトしており、`curl` が自動的にそのリダイレクトをたどって実際のファイルに到達しないためです。以下に解決方法を示します。

### 問題の理解

- **301 Moved Permanently**: この HTTP ステータスコードは、リソース（ZIPファイル）が新しい URL に恒久的に移動したことを意味します。サーバーは、ミラーサイトや更新された場所を指すために、ダウンロードリンクに対してリダイレクトを頻繁に使用します。
- **`curl -O` の挙動**: `-O` オプションは、ダウンロードしたコンテンツをリモートファイルと同じ名前のファイルに保存するよう `curl` に指示します。しかし、リダイレクトを明示的に処理しない場合、`curl` はリダイレクトの中間応答（多くの場合 HTML ページ）のコンテンツを保存し、ZIP ファイルまでリダイレクトをたどらない可能性があります。

### 解決策

`curl` がリダイレクトをたどり、Eclipse ZIP ファイルをダウンロードするようにするには、`-O` と一緒に `-L` オプションを使用します。`-L` フラグは、最終目的地に到達するまであらゆるリダイレクトをたどるよう `curl` に指示します。

#### コマンド

```bash
curl -L -O <URL>
```

- **`-L`**: 301 リダイレクトなどのリダイレクトを新しい場所までたどります。
- **`-O`**: 最終 URL からの元の名前でファイルを保存します。
- **`<URL>`**: これを特定の Eclipse ダウンロード URL、例えば `https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip` に置き換えてください。

### ステップバイステップの手順

1. **正しい URL を見つける**:
   - Eclipse ウェブサイト（例: `https://www.eclipse.org/downloads/`）にアクセスします。
   - 目的のパッケージ（例: Eclipse IDE for Java Developers）を選択します。
   - ダウンロードリンクまたはボタンを右クリックして URL をコピーします。または、ブラウザの開発者ツール（F12キー、Network タブ）を使用して、ダウンロードをクリックしたときの正確な URL を取得します。

2. **コマンドを実行する**:
   - ターミナルを開きます。
   - コピーした URL を使用して、`-L` と `-O` オプションを付けた `curl` コマンドを実行します:
     ```bash
     curl -L -O https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
     ```
   - これにより、ZIP ファイル（例: `eclipse-java-2023-03-R-win32-x86_64.zip`）が現在のディレクトリにダウンロードされるはずです。

### トラブルシューティング

まだ問題が発生する場合は、以下の追加手順を試してください。

- **詳細出力でリダイレクトを確認する**:
  - `-v` オプションを使用して、リクエストとリダイレクトに関する詳細情報を表示します:
    ```bash
    curl -v -L -O <URL>
    ```
  - 301 応答の `Location` ヘッダを確認し、どこにリダイレクトしているかを確認します。ZIP ファイルではなく HTML ページを指している場合、その URL は直接ダウンロードリンクではない可能性があります。

- **URL を確認する**:
  - Eclipse は多くの場合、ミラーにリダイレクトする `download.php` スクリプトを使用します。あなたの URL が ZIP ファイルへの直接リンクであるか、ファイルに解決されるリダイレクトリンクであることを確認してください。例えば、直接ミラーリンクは以下のようになります:
    ```bash
    curl -L -O https://mirror.its.dal.ca/eclipse/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
    ```

- **User-Agent ヘッダを設定する**:
  - 一部のサーバーはクライアントに基づいて異なる挙動をします。サーバーが `curl` を検出して HTML を返す場合、User-Agent を追加してブラウザを模倣します:
    ```bash
    curl -L -O -A "Mozilla/5.0" <URL>
    ```

### これが機能する理由

Eclipse ウェブサイトは、ダウンロードリクエストをミラーまたは更新された URL にリダイレクトすることがあります。`-L` なしでは、`curl -O` はリダイレクト応答（HTML ページ）を保存し、それをたどりません。`-L` を追加することで、`curl` が 301 リダイレクトをたどって実際の ZIP ファイルに到達することを保証し、問題を解決します。

これらの手順に従うことで、`curl` を使用して eclipse.org から Eclipse ZIP ファイルを正常にダウンロードできるはずです。