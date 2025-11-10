---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 開放圖協定詳解
translated: true
type: note
---

在 HTML meta 標籤如 `<meta property="og:type" content="website">` 的語境中，「og」代表 Open Graph。這指的是由 Facebook（現為 Meta）最初開發的 Open Graph 協議標準，該標準允許網頁提供結構化的元數據來描述其內容。這些元數據能控制頁面在社交媒體平台或通訊軟件上分享時的外觀顯示，例如以豐富預覽格式（如帶有圖片和摘要的卡片）呈現標題、描述、圖片及其他細節。

該協議使用以「og:」為前綴的屬性來定義元素，例如：
- `og:title`：內容標題
- `og:description`：簡要概述
- `og:image`：預覽圖片的網址
- `og:type`：內容類型（例如網站、文章、影片）

雖然此協議最初為 Facebook 創建，但現今許多其他平台和應用程式（包括微信）都支援 Open Graph 標籤來生成連結預覽。當您在微信分享連結時，系統通常會解析這些標籤來一致地生成縮圖、標題和描述。若未設置這些標籤，平台可能會轉而使用其他 meta 標籤或抓取頁面內容，這可能導致顯示結果不一致。

您猜測的「open gx」很接近答案——實際應為「Open Graph」，而非「open gx」（可能是「graph」的拼寫錯誤或自動校正？）。

### 參考資料
[The Open Graph protocol](https://ogp.me/)  
[Open Graph Meta Tags: Everything You Need to Know](https://ahrefs.com/blog/open-graph-meta-tags/)  
[What is Open Graph and how can I use it for my website?](https://www.freecodecamp.org/news/what-is-open-graph-and-how-can-i-use-it-for-my-website/)  
[How does wechat choose the link's thumbnail?](https://stackoverflow.com/questions/44564614/how-does-wechat-choose-the-links-thumbnail)  
[Meta tag - WeChat](https://github.com/freeCodeCamp/freeCodeCamp/issues/38707)