---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修正多重定義連結錯誤
translated: true
type: note
---

這是一個**多重定義連結錯誤**——當**全域變數被定義在標頭檔（`variables.h`）** 而非僅在該處*宣告*時，典型的 C 語言錯誤。

讓我們來解析問題發生的原因及解決方法。

---

### 🔍 問題所在

你的錯誤訊息顯示：

```
multiple definition of `curl` ...
multiple definition of `nec` ...
multiple definition of `contador` ...
multiple definition of `descargadas` ...
```

這表示你的標頭檔 `variables.h` 可能長這樣：

```c
// variables.h（有問題的版本）
#include <curl/curl.h>

CURL *curl;
int nec;
int contador;
int descargadas;
```

每個引入 `variables.h` 的 `.c` 檔案都會獲得這些變數的**獨立副本**。
在連結階段，連結器會發現每個目的檔中都存在相同全域符號的*多重定義*。

---

### ✅ 正確的模式

你必須在標頭檔中**宣告**全域變數，並僅在單一個 `.c` 檔案中**定義**它們。

#### 步驟 1：修正 `variables.h`

改為：

```c
// variables.h
#ifndef VARIABLES_H
#define VARIABLES_H

#include <curl/curl.h>

extern CURL *curl;
extern int nec;
extern int contador;
extern int descargadas;

#endif
```

#### 步驟 2：僅定義一次（例如在 `variables.c` 中）

建立或更新 `variables.c`：

```c
#include "variables.h"

CURL *curl = NULL;
int nec = 0;
int contador = 0;
int descargadas = 0;
```

#### 步驟 3：重新編譯

清除並重新編譯：

```bash
make clean
make
```

---

### 🧠 為何這樣可行

* `extern` 告訴編譯器該變數*在其他地方定義*。
* 只有一個 `.c` 檔案實際定義它（為其分配記憶體）。
* 連結器隨後會找到一個定義和多個參考 → 沒有衝突。

---

如果你需要，我可以提供一個前後對照的簡易程式碼範例，讓這個概念更清晰。需要嗎？