---
audio: false
lang: hant
layout: post
title: NumPy
translated: true
type: note
---

### 陣列建立常式

*   `np.empty`：回傳一個指定形狀和類型的新陣列，不初始化內容。
*   `np.empty_like`：回傳一個與指定陣列形狀和類型相同的新陣列。
*   `np.eye`：回傳一個對角線為1，其餘為0的二維陣列。
*   `np.identity`：回傳單位陣列。
*   `np.ones`：回傳一個指定形狀和類型，並填充為1的新陣列。
*   `np.ones_like`：回傳一個與指定陣列形狀和類型相同，並填充為1的陣列。
*   `np.zeros`：回傳一個指定形狀和類型，並填充為0的新陣列。
*   `np.zeros_like`：回傳一個與指定陣列形狀和類型相同，並填充為0的陣列。
*   `np.full`：回傳一個指定形狀和類型，並填充為 fill_value 的新陣列。
*   `np.full_like`：回傳一個與指定陣列形狀和類型相同，並填充指定值的完整陣列。
*   `np.array`：建立一個陣列。
*   `np.asarray`：將輸入轉換為陣列。
*   `np.asanyarray`：將輸入轉換為 ndarray，但保留 ndarray 子類別。
*   `np.ascontiguousarray`：回傳記憶體中的連續陣列（C 順序）。
*   `np.asfortranarray`：回