---
audio: false
generated: false
image: true
lang: hant
layout: post
title: 進階Markdown使用
translated: true
---

## 參考文獻

參考文獻 [^1]。

在腳註中，記得在 `[數字]` 後加上 `:` 以便正確解析。

---

## 圖片類別

你可以像這樣在 Markdown 中為圖片應用類別：

```markdown
{: .centered }
![](assets/images/pin/pin.jpg){: .responsive }
*來源：Telegram*{: .caption }
```

這將以指定的類別渲染圖片：

{: .centered }  
![](assets/images/pin/pin.jpg){: .responsive }  
*來源：Telegram*{: .caption }

## 目錄

- [介紹](#介紹)
- [第一章](#第一章)
- [結論](#結論)

---

### 介紹

這裡是介紹。

---

### 第一章

這裡是第一章。

---

### 結論

這裡是結論。

## Mermaid

```mermaid
graph TD
    A[充電盒] --> B[行動電源]
    A --> C[藍牙喇叭]
    A --> D[手機]
    A --> E[電燈]
    A --> F[筆記型電腦]
    A --> G[智能手錶]
    A --> H[雲端伺服器]
    B --> H
    C --> H
    D --> H
    E --> H
    F --> H
    G --> H
```

這裡還沒有渲染出來，但在 Mistral 中運行良好。我們找時間多學習一下。

---

[^1]: 這裡是一個參考文獻。