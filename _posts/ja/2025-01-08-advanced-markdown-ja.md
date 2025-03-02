---
audio: false
generated: false
lang: ja
layout: post
title: 高度なMarkdownの使い方
translated: true
---

## 参考文献

参考文献 [^1]。

脚注では、正しい解析のために `[数字]` の後に `:` を追加することを忘れないでください。

---

## 画像クラス

Markdownで画像にクラスを適用するには、次のようにします：

```markdown
{: .centered }
![](assets/images/pin/pin.jpg){: .responsive }
*出典: Telegram*{: .caption }
```

これは指定されたクラスで画像をレンダリングします：

{: .centered }  
![](assets/images/pin/pin.jpg){: .responsive }  
*出典: Telegram*{: .caption }

## 目次

- [はじめに](#introduction)
- [第1章](#chapter-1)
- [結論](#conclusion)

---

### はじめに

以下が導入部です。

---

### 第1章

以下は第1章です。

---

### 結論

以下が結論です。

## Mermaid

```mermaid
graph TD
    A[充電ボックス] --> B[モバイルバッテリー]
    A --> C[Bluetoothスピーカー]
    A --> D[携帯電話]
    A --> E[電気スタンド]
    A --> F[ノートパソコン]
    A --> G[スマートウォッチ]
    A --> H[クラウドサーバー]
    B --> H
    C --> H
    D --> H
    E --> H
    F --> H
    G --> H
```

ここではまだレンダリングされていませんが、うまく動作しており、Mistralで生成することができます。もっと学ぶ時間を見つけましょう。

---

[^1]: こちらがその一つです。
```