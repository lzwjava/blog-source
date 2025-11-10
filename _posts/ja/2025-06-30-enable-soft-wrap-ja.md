---
audio: false
generated: true
lang: ja
layout: post
title: Zedでソフトラップを有効にする
translated: true
type: note
---

Zedは、多くのモダンなテキストエディタと同様に、「ソフトラップ」の概念を使用して行を折り返します。これは、行がエディタ内で折り返されて表示されますが、ファイルに実際の改行文字が挿入されるわけではないことを意味します。

以下は、Zedで行の折り返しを有効にする方法です：

1.  **Zedの設定を開く：**

      * `Command + Shift + P`（macOS）または `Ctrl + Shift + P`（Windows/Linux）を押して、コマンドパレットを開きます。
      * 「local」と入力し、「zed: Open Local Settings」を選択します。これにより、あなたの `settings.json` ファイルが開きます。

2.  **`soft_wrap` 設定を追加する：**

      * `settings.json` ファイルで、`"soft_wrap"` 設定を追加または変更します。いくつかのオプションがあります：

          * **`"editor_width"`:** これは最も一般的で、通常推奨されるオプションです。現在のエディタウィンドウの幅に合わせて行を折り返します。
            ```json
            {
              "soft_wrap": "editor_width"
            }
            ```
          * **`"preferred_line_length"`:** これは、指定された `preferred_line_length`（例：80文字）に基づいて行を折り返します。`preferred_line_length` も定義する必要があります。
            ```json
            {
              "soft_wrap": "preferred_line_length",
              "preferred_line_length": 80
            }
            ```
          * **`"bounded"`:** このオプションは、より高度な折り返し動作を提供しますが、ほとんどのユーザーには `editor_width` または `preferred_line_length` で十分です。
          * **`"none"`:** これは行の折り返しを無効にします。

3.  **ファイルを保存する：**

      * `Command + S`（macOS）または `Ctrl + S`（Windows/Linux）を押して、`settings.json` ファイルを保存します。

Zedは、選択した設定に従って行を折り返すようになります。

**重要な注意点：**

  * **プロジェクトレベルの設定:** プロジェクトディレクトリに `.zed` フォルダを作成し、その中に目的の `soft_wrap` 設定を含む `settings.json` ファイルを配置することで、プロジェクトレベルでワードラップを有効にすることもできます。これは、その特定のプロジェクトに対してグローバル設定を上書きします。
  * **言語固有の設定:** 特定の言語に対して `soft_wrap` を設定することもできます。例えば、Markdownファイルに対してソフトラップを設定するには：
    ```json
    {
      "languages": {
        "Markdown": {
          "soft_wrap": "editor_width"
        }
      }
    }
    ```
  * **「Rewrap」コマンド:** 単に視覚的に折り返すのではなく、テキストを「ハードラップ」（実際の改行を挿入）するコマンドをお探しの場合、Zedには「Rewrap」コマンド（多くの場合 `Alt-Q` または `Alt-W` にバインドされている）もあります。これはコメントや長い散文の行をフォーマットするのに便利です。