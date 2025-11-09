---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 多重定義リンクエラーの修正
translated: true
type: note
---

これは**多重定義リンクエラー**です — **グローバル変数がヘッダーファイル（`variables.h`）で定義されている**代わりに、そこで*宣言*だけされている場合の典型的なC言語の間違いです。

何が起こっているのか、そしてどう修正するのか見ていきましょう。

---

### 🔍 問題点

エラーは以下のように表示されます：

```
multiple definition of `curl' ...
multiple definition of `nec' ...
multiple definition of `contador' ...
multiple definition of `descargadas' ...
```

これは、あなたのヘッダーファイル `variables.h` がおそらく以下のようになっていることを意味します：

```c
// variables.h (問題のあるコード)
#include <curl/curl.h>

CURL *curl;
int nec;
int contador;
int descargadas;
```

`variables.h` をインクルードするすべての `.c` ファイルは、これらの変数の**独自のコピー**を取得します。
リンク時には、リンカは各オブジェクトファイルから同じグローバルシンボルの*複数の定義*を見つけます。

---

### ✅ 正しいパターン

グローバル変数をヘッダーで**宣言**し、それらを単一の `.c` ファイルで一度だけ**定義**する必要があります。

#### ステップ 1: `variables.h` を修正する

以下のように変更します：

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

#### ステップ 2: 一度だけ定義する (例: `variables.c` 内)

`variables.c` を作成または更新します：

```c
#include "variables.h"

CURL *curl = NULL;
int nec = 0;
int contador = 0;
int descargadas = 0;
```

#### ステップ 3: リビルドする

クリーンしてリビルドします：

```bash
make clean
make
```

---

### 🧠 これが機能する理由

* `extern` は、その変数が*別の場所に存在する*ことをコンパイラに伝えます。
* 実際にそれを定義する（メモリを割り当てる） `.c` ファイルは一つだけです。
* リンカは一つの定義と複数の参照を持つことになり → 競合は発生しません。

---

もしよろしければ、これをより明確にするための修正前/修正後の最小限のコード例をお見せできます。ご覧になりますか？