---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 使用 Flexbox 置中堆疊表單元素
translated: true
---

```css
.sort-container {
    display: flex;
    flex-direction: column; /* 添加此屬性以垂直堆疊項目 */
    align-items: center; /* 在垂直列中水平置中項目 */
    justify-content: center; /* 垂直置中整個列 */
    gap: 10px;
    margin-bottom: 1rem;
}

.sort-container select {
    padding: 5px;
    font-size: 16px;
}

.sort-container .post-number {
    font-size: 16px;
}
```

### 說明
- **flex-direction: column**：將主軸從水平（橫向）改為垂直，使 `select` 和 `.post-number` 元素從上到下堆疊。
- **align-items: center**：保持子元素的水平置中對齊。
- **justify-content: center**：在容器內垂直置中整個堆疊內容。
- 同時修正了嵌套選擇器的語法（將 `select` 和 `.post-number` 移出主區塊以符合最佳實踐，假設它們是直接子元素——如有需要請調整）。現在 `gap` 屬性會在項目之間產生垂直間距。