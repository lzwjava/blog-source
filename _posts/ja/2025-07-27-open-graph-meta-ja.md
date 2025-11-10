---
audio: false
generated: true
image: false
lang: ja
layout: post
title: オープングラフプロトコル解説
translated: true
type: note
---

HTMLのメタタグ、例えば`<meta property="og:type" content="website">`における「og」は、Open Graphを表します。これはOpen Graphプロトコルを指しており、Facebook（現Meta）が元々開発した、ウェブページが自身のコンテンツに関する構造化メタデータを提供するための標準です。このメタデータは、ソーシャルメディアプラットフォームやメッセージングアプリで共有された際に、ページがどのように表示されるかを制御します。例えば、リッチプレビューフォーマット（画像と要約を含むカード形式など）でタイトル、説明、画像、その他の詳細を表示します。

このプロトコルでは、「og:」を接頭辞とするプロパティを使用して、以下のような要素を定義します：
- `og:title`: コンテンツのタイトル
- `og:description`: 簡単な要約
- `og:image`: プレビュー画像のURL
- `og:type`: コンテンツの種類（例: website、article、video）

Facebook向けに作成されましたが、WeChatを含む多くの他のプラットフォームやアプリがリンクプレビューのためにOpen Graphタグをサポートしています。WeChatでリンクを共有すると、多くの場合、これらのタグを解析して、サムネイル、タイトル、説明を一貫して生成します。タグが存在しない場合、プラットフォームは他のメタタグにフォールバックしたり、ページコンテンツをスクレイピングしたりする可能性があり、結果に一貫性がなくなることがあります。

「open gx」という推測は近いですが、実際には「Open Graph」です（「graph」のタイプミスまたはオートコレクトかもしれません）。

### 参考文献
[The Open Graph protocol](https://ogp.me/)  
[Open Graph Meta Tags: Everything You Need to Know](https://ahrefs.com/blog/open-graph-meta-tags/)  
[What is Open Graph and how can I use it for my website?](https://www.freecodecamp.org/news/what-is-open-graph-and-how-can-i-use-it-for-my-website/)  
[How does wechat choose the link's thumbnail?](https://stackoverflow.com/questions/44564614/how-does-wechat-choose-the-links-thumbnail)  
[Meta tag - WeChat](https://github.com/freeCodeCamp/freeCodeCamp/issues/38707)