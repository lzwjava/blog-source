---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Cリンカー多重定義エラーの修正
translated: true
type: note
---

### DirBのビルド問題と修正方法

ビルドログでは個々のソースファイルのコンパイルは成功していますが（いくつかの警告あり）、最終的なリンクステップでグローバル変数と構造体に対する**多重定義エラー**により失敗しています。これはヘッダーファイルがグローバル変数を宣言ではなく定義している場合に発生する一般的なC言語の問題です。まず警告（致命的ではないが修正すべき）から説明し、次に致命的なリンカーエラーと段階的な修正方法を説明します。

#### 1. コンパイル警告（非致命的）
これらはGCCの`-Wall`フラグによるものです。ビルドを停止させるものではありませんが、潜在的なバグを示しています。出力をクリーンアップするために修正してください。

- **utils.c**:
  - 4行目付近（`location_cmp()`内）: フォーマット指定子の不一致。`strlen()`は`size_t`（符号なしlong）を返しますが、`%d`（int）を使用しています。  
    **修正**: `printf`の`%d`を`%zu`に変更:  
    ```c
    printf("[++++] location_cmp() RESULT: %d (%zu)\n", result, strlen(A) > strlen(B) ? strlen(A) : strlen(B));
    ```
  - 287行目（`kbhit()`内）: `read()`の戻り値を無視しています（失敗する可能性あり）。  
    **修正**: 戻り値をチェック:  
    ```c
    if (read(0, &key, 1) != 1) {
        // エラー処理、例: return 0;
    }
    ```

- **resume.c**:
  - 32行目（`dump()`内）: 誤解を招くインデント - `fflush(stdout)`が`if`文でガードされていません。  
    **修正**: 中括弧を追加するか再インデント:  
    ```c
    if (options.debuging > 2) {
        printf("[++] dump() Dumping Session State AT %s", asctime(ptr));
        fflush(stdout);
    }
    ```
  - 38-41行目および109-112行目: `asprintf()`の戻り値を無視しています（失敗するとポインタが初期化されないままになる可能性あり）。  
    **修正**: 戻り値をチェック（例: `if (asprintf(&dumppath, ...) < 0) { /* エラー処理 */ }`）。すべての呼び出しで実施。
  - 120行目（`resume()`内）: `fread()`の戻り値を無視しています（完全な構造体を読み取らない可能性あり）。  
    **修正**: チェックを追加:  
    ```c
    if (fread(&options, sizeof(struct opciones), 1, desc) != 1) {
        // エラー処理、例: fclose(desc); return;
    }
    ```

修正後は再コンパイル: `make clean && make`（Makefileがある場合。ない場合はgccコマンドを再実行）。

#### 2. 致命的リンカーエラー（多重定義）
リンカー（`/usr/bin/ld`）が数十のシンボル（例: `options`, `encontradas`, `curl`など）が複数のオブジェクトファイル（`dirb.o`, `crea_wordlist.o`など）間で多重定義されていると報告しています。すべて`/home/lzwjava/projects/dirb/src/variables.h:XX`に起因しています。

**根本原因**:  
`variables.h`がおそらくこれらのグローバルを`extern`として**宣言**するのではなく、直接**定義**しています（例: `struct opciones options;`）。複数の`.c`ファイルにインクルードされると、それぞれが独自の定義のコピーを持つ`.o`ファイルにコンパイルされます。リンク時にこれらがマージされ、競合が発生します。

**解決策**:  
共有グローバル変数には「extern」パターンを使用:
- ヘッダーで`extern`を付けて**宣言**（コンパイラに「これは別の場所に存在する」と伝える）。
- **正確に1つの**`.c`ファイル（例: `dirb.c`）で`extern`なしで**定義**。

手順:
1. **`variables.h`を編集**（`src/`内）: すべてのグローバル変数/構造体に`extern`を接頭辞として追加。エラーに基づく例:
   ```c
   // 修正前（悪い例: すべての.oで定義）
   struct opciones options;
   int contador;
   int nec;
   FILE *outfile;
   CURL *curl;
   int errores;
   int existant;
   int descargadas;
   int encontradas;
   char *wordlist_base;
   char *wordlist_current;
   char *wordlist_final;
   char *exts_base;
   char *exts_current;
   int exts_num;
   char *muts_base;
   char *dirlist_base;
   char *dirlist_current;
   char *dirlist_final;
   int listable;
   int resuming;
   char *next_dir;

   // 修正後（良い例: 宣言のみ）
   extern struct opciones options;
   extern int contador;
   extern int nec;
   extern FILE *outfile;
   extern CURL *curl;
   extern int errores;
   extern int existant;
   extern int descargadas;
   extern int encontradas;
   extern char *wordlist_base;
   extern char *wordlist_current;
   extern char *wordlist_final;
   extern char *exts_base;
   extern char *exts_current;
   extern int exts_num;
   extern char *muts_base;
   extern char *dirlist_base;
   extern char *dirlist_current;
   extern char *dirlist_final;
   extern int listable;
   extern int resuming;
   extern char *next_dir;
   ```
   - 必要に応じてヘッダーを上部にインクルード: `#include <stdio.h>`, `#include <curl/curl.h>`など。
   - `struct opciones`がヘッダーで定義されている場合はそのまま保持（構造体はヘッダーで定義可能）。

2. **1つのソースファイルを選択**（例: メインファイルの`dirb.c`）し、そこでグローバル変数を**定義**（`extern`なし）:
   ```c
   // dirb.c内、インクルード後
   struct opciones options = {0};  // 必要に応じて初期化
   int contador = 0;
   int nec = 0;
   FILE *outfile = NULL;
   CURL *curl = NULL;
   // ... 他も同様に、適切に初期化（例: intは0、ポインタはNULL）
   ```

3. **クリーンとリビルド**:
   ```
   make clean  # または rm *.o
   # コンパイルコマンドを再実行、その後最終リンク:
   gcc -Wall -g -O2 -o dirb crea_wordlist.o dirb.o get_url.o lanza_ataque.o calculanec.o utils.o options.o resume.o -lcurl
   ```

4. **検証**:
   - `./dirb --help`を実行してテスト。
   - 新しいエラーが発生した場合（例: 未定義シンボル）、定義が`dirb.c`にあり、すべてのファイルが`variables.h`をインクルードしていることを確認。

#### 追加注記
- **Makefile?** `Makefile`からビルドしている場合、開発中は一時的に`-Werror`を追加して警告をエラーとして扱うことができます。
- **DirBバージョン**: これは古い/カスタムフォークのように見えます（`lanza_ataque.c`などへの参照）。GitHubからのものであれば、アップストリームの修正を確認してください: [GitHubのdirb](https://github.com/v0re/dirb)。
- **依存関係**: libcurlがインストールされていることを確認（Debianベースシステムでは`sudo apt install libcurl4-openssl-dev`）。
- 問題が解決しない場合（例: `struct opciones`定義の欠落）、さらなる支援のために`variables.h`の内容を共有してください。

これでクリーンにリンクされるはずです！さらにコード/ログを貼り付けて頂ければ、より詳細なアドバイスができます。