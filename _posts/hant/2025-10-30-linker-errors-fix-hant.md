---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 C 語言連結器多重定義錯誤
translated: true
type: note
---

### DirB 建置問題與修復方案

您的建置記錄顯示原始碼檔案編譯成功（伴隨一些警告），但在最終連結階段因全域變數和結構的**重複定義錯誤**而失敗。這是 C 語言中當標頭檔案定義（而非僅宣告）全域變數時的常見問題。我將分步說明：先處理警告（非致命但建議修復），再解決致命的連結器錯誤並提供逐步修復方案。

#### 1. 編譯警告（非致命）
這些警告來自 GCC 的 `-Wall` 旗標。雖不阻礙建置，但暗示潛在錯誤。建議修復以保持輸出整潔。

- **utils.c**：
  - 第 ~4 行（於 `location_cmp()` 中）：格式指定符不匹配。`strlen()` 回傳 `size_t`（無號長整型），但您使用了 `%d`（整型）。  
    **修復**：將 `printf` 中的 `%d` 改為 `%zu`：  
    ```c
    printf("[++++] location_cmp() RESULT: %d (%zu)\n", result, strlen(A) > strlen(B) ? strlen(A) : strlen(B));
    ```
  - 第 287 行（於 `kbhit()` 中）：忽略 `read()` 回傳值（它可能執行失敗）。  
    **修復**：檢查回傳值：  
    ```c
    if (read(0, &key, 1) != 1) {
        // 處理錯誤，例如：return 0;
    }
    ```

- **resume.c**：
  - 第 32 行（於 `dump()` 中）：縮排誤導——`fflush(stdout)` 未受 `if` 條件保護。  
    **修復**：添加大括號或重新縮排：  
    ```c
    if (options.debuging > 2) {
        printf("[++] dump() Dumping Session State AT %s", asctime(ptr));
        fflush(stdout);
    }
    ```
  - 第 38–41 行與 109–112 行：忽略 `asprintf()` 回傳值（它可能失敗並導致指標未初始化）。  
    **修復**：檢查所有呼叫的回傳值（例如：`if (asprintf(&dumppath, ...) < 0) { /* 錯誤處理 */ }`）。
  - 第 120 行（於 `resume()` 中）：忽略 `fread()` 回傳值（可能未完整讀取結構）。  
    **修復**：檢查回傳值：  
    ```c
    if (fread(&options, sizeof(struct opciones), 1, desc) != 1) {
        // 處理錯誤，例如：fclose(desc); return;
    }
    ```

修復後重新編譯：執行 `make clean && make`（假設存在 Makefile；若無，請重新執行您的 gcc 指令）。

#### 2. 致命連結器錯誤（重複定義）
連結器（`/usr/bin/ld`）回報數十個符號（例如 `options`、`encontradas`、`curl` 等）在多個物件檔案（`dirb.o`、`crea_wordlist.o` 等）中重複定義。所有錯誤皆追溯至 `/home/lzwjava/projects/dirb/src/variables.h:XX`。

**根本原因**：  
`variables.h` 很可能直接**定義**了這些全域變數（例如：`struct opciones options;`），而非使用 `extern` **宣告**它們。當此標頭被多個 `.c` 檔案包含時，每個檔案編譯後的 `.o` 都會擁有自己的定義副本。連結時合併這些副本便導致衝突。

**解決方案**：  
對共享的全域變數採用 "extern" 模式：
- 在標頭中使用 `extern` **宣告**（告知編譯器「此變數存在於他處」）。
- 在**唯一一個** `.c` 檔案（例如 `dirb.c`）中**定義**（不使用 `extern`）。

步驟：
1. **編輯 `variables.h`**（位於 `src/` 目錄）：在所有全域變數/結構前添加 `extern`。根據錯誤訊息示例：
   ```c
   // 修改前（錯誤：在每個 .o 中定義）
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

   // 修改後（正確：僅作宣告）
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
   - 在檔案頂部包含必要標頭：`#include <stdio.h>`、`#include <curl/curl.h>` 等。
   - 若 `struct opciones` 定義於此標頭中，請保留其定義（結構體可在標頭中定義）。

2. **選擇一個原始碼檔案**（例如主檔案 `dirb.c`）並在其中**定義**全域變數（不使用 `extern`）：
   ```c
   // 在 dirb.c 的 include 之後
   struct opciones options = {0};  // 若需要可初始化
   int contador = 0;
   int nec = 0;
   FILE *outfile = NULL;
   CURL *curl = NULL;
   // ... 其餘變數依此類推，進行合理初始化（例如整型設為 0，指標設為 NULL）
   ```

3. **清除並重新建置**：
   ```
   make clean  # 或 rm *.o
   # 重新執行編譯指令，然後進行最終連結：
   gcc -Wall -g -O2 -o dirb crea_wordlist.o dirb.o get_url.o lanza_ataque.o calculanec.o utils.o options.o resume.o -lcurl
   ```

4. **驗證**：
   - 執行 `./dirb --help` 進行測試。
   - 若出現新錯誤（例如未定義符號），請確認所有定義皆位於 `dirb.c` 中且所有檔案皆包含 `variables.h`。

#### 補充說明
- **Makefile？** 若專案使用 `Makefile`，可在開發期間暫時添加 `-Werror` 將警告視為錯誤。
- **DirB 版本**：這似乎是較舊或自訂的分支（參考 `lanza_ataque.c` 等）。若源自 GitHub，請檢查上游修復：[GitHub 上的 dirb](https://github.com/v0re/dirb)。
- **相依套件**：請確保已安裝 libcurl（在 Debian 系系統上執行 `sudo apt install libcurl4-openssl-dev`）。
- 若問題持續（例如缺少 `struct opciones` 定義），請分享 `variables.h` 內容以獲進一步協助。

以上步驟應能讓專案順利完成連結！若您提供更多程式碼或記錄，我可進一步優化建議。