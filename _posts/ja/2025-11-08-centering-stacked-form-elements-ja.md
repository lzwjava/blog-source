---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: フレックスボックスで積み重ねたフォーム要素を中央揃え
translated: true
type: note
---

```css
.sort-container {
    display: flex;
    flex-direction: column; /* 縦方向にアイテムを積み重ねるために追加 */
    align-items: center; /* カラム内でアイテムを水平方向に中央揃え */
    justify-content: center; /* カラムを垂直方向に中央揃え */
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

### 説明
- **flex-direction: column**: 主軸を水平（行）から垂直に変更し、`select`と`.post-number`要素を上から下に積み重ねます。
- **align-items: center**: 子要素の水平方向の中央揃えを維持します。
- **justify-content: center**: 垂直方向に積み重なった全体をコンテナ内で中央揃えします。
- ネストされたセレクターの構文も修正しました（より良いプラクティスのために`select`と`.post-number`をメインブロックの外に移動 - 必要に応じて調整してください）。`gap`はアイテム間の垂直方向の間隔に適用されます。