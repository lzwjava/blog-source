---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إصلاح أخطار التعريف المتعدد لرابط لغة سي
translated: true
type: note
---

### مشاكل وحلول بناء DirB

يظهر سجل البناء الخاص بك نجاح تجميع ملفات المصدر الفردية (مع بعض التحذيرات)، لكنه يفشل أثناء خطوة الربط النهائية بسبب **أخطار تعريف متعددة** للمتغيرات والهياكل العامة. هذه مشكلة شائعة في لغة C عندما تقوم ملفات الرأس بتعريف (بدلاً من مجرد الإعلان عن) المتغيرات العامة. سأقوم بتحليلها: أولاً التحذيرات (غير القاتلة ولكنها تستحق الإصلاح)، ثم أخطاء الرابط القاتلة مع حل خطوة بخطوة.

#### 1. تحذيرات الترجمة (غير قاتلة)
هذه من علم `-Wall` في GCC. إنها لا توقف عملية البناء ولكنها تشير إلى أخطاء محتملة. أصلحها لتنظيف المخرجات.

- **utils.c**:
  - السطر ~4 (في `location_cmp()`): عدم تطابق محدد التنسيق. `strlen()` تُرجع `size_t` (unsigned long)، لكنك تستخدم `%d` (int).  
    **الحل**: غيّر `%d` إلى `%zu` في `printf`:  
    ```c
    printf("[++++] location_cmp() RESULT: %d (%zu)\n", result, strlen(A) > strlen(B) ? strlen(A) : strlen(B));
    ```
  - السطر 287 (في `kbhit()`): تجاهل قيمة الإرجاع لـ `read()` (قد تفشل).  
    **الحل**: تحقق من قيمة الإرجاع:  
    ```c
    if (read(0, &key, 1) != 1) {
        // التعامل مع الخطأ، مثلاً: return 0;
    }
    ```

- **resume.c**:
  - السطر 32 (في `dump()`): مسافة بادئة مضللة — `fflush(stdout)` ليست محمية بشرط `if`.  
    **الحل**: أضف أقواسًا أو أعد المسافة البادئة:  
    ```c
    if (options.debuging > 2) {
        printf("[++] dump() Dumping Session State AT %s", asctime(ptr));
        fflush(stdout);
    }
    ```
  - الأسطر 38–41 و 109–112: تجاهل قيم إرجاع `asprintf()` (قد تفشل وتترك المؤشرات غير مهيأة).  
    **الحل**: تحقق من القيم المرجعة (مثلاً، `if (asprintf(&dumppath, ...) < 0) { /* error */ }`). افعل هذا لجميع الاستدعاءات.
  - السطر 120 (في `resume()`): تجاهل قيمة إرجاع `fread()` (قد لا تقرأ الهيكل بالكامل).  
    **الحل**: تحقق منها:  
    ```c
    if (fread(&options, sizeof(struct opciones), 1, desc) != 1) {
        // التعامل مع الخطأ، مثلاً: fclose(desc); return;
    }
    ```

أعد الترجمة بعد الإصلاحات: `make clean && make` (بافتراض وجود Makefile؛ إذا لم يكن، أعد تشغيل أوامر gcc الخاصة بك).

#### 2. أخطاء الرابط القاتلة (تعريفات متعددة)
يشكو الرابط (`/usr/bin/ld`) من عشرات الرموز (مثل `options`, `encontradas`, `curl`، إلخ.) يتم تعريفها عدة مرات عبر ملفات الكائن (`dirb.o`, `crea_wordlist.o`، إلخ.). كلها تعود إلى `/home/lzwjava/projects/dirb/src/variables.h:XX`.

**السبب الجذري**:  
من المرجح أن `variables.h` **تعرف** هذه المتغيرات العامة مباشرة (مثلاً، `struct opciones options;`) بدلاً من **الإعلان عنها** كـ `extern`. عند تضمينها في ملفات `.c` متعددة، يترجم كل منها إلى ملف `.o` يحتوي على نسخته الخاصة من التعريفات. يؤدي الربط إلى دمجها، مسببًا تعارضات.

**الحل**:  
استخدم نمط "extern" للمتغيرات العامة المشتركة:
- **أعلن** في الرأس باستخدام `extern` (يخبر المترجم "هذا موجود في مكان آخر").
- **عرف** (بدون `extern`) في **ملف `.c` واحد فقط بالضبط** (مثلاً، `dirb.c`).

الخطوات:
1. **عدّل `variables.h`** (في `src/`): أضف بادئة `extern` لجميع المتغيرات/الهياكل العامة. أمثلة بناءً على الأخطاء:
   ```c
   // قبل (سيء: يعرف في كل .o)
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

   // بعد (جيد: يعلن فقط)
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
   - قم بتضمين الرؤوس الضرورية في الأعلى: `#include <stdio.h>`, `#include <curl/curl.h>`، إلخ.
   - إذا تم تعريف `struct opciones` في الرأس، احتفظ بذلك (يمكن تعريف الهياكل في الرؤوس).

2. **اختر ملف مصدر واحد** (مثلاً، `dirb.c`، الملف الرئيسي) و**عرف** المتغيرات العامة فيه (بدون `extern`):
   ```c
   // في dirb.c، بعد التضمينات
   struct opciones options = {0};  // هيّئ إذا لزم الأمر
   int contador = 0;
   int nec = 0;
   FILE *outfile = NULL;
   CURL *curl = NULL;
   // ... كرر للباقي، مع التهيئة المنطقية (مثلاً، ints إلى 0، pointers إلى NULL)
   ```

3. **نظف وأعد البناء**:
   ```
   make clean  # أو rm *.o
   # أعد تشغيل أوامر الترجمة الخاصة بك، ثم الربط النهائي:
   gcc -Wall -g -O2 -o dirb crea_wordlist.o dirb.o get_url.o lanza_ataque.o calculanec.o utils.o options.o resume.o -lcurl
   ```

4. **تحقق**:
   - شغّل `./dirb --help` للاختبار.
   - إذا ظهرت أخطاء جديدة (مثلاً، رموز غير معرفة)، تأكد من أن التعريفات موجودة في `dirb.c` وأن جميع الملفات تضمن `variables.h`.

#### ملاحظات إضافية
- **Makefile؟** إذا كان هذا من `Makefile`، أضف `-Werror` مؤقتًا لمعاملة التحذيرات كأخطاء أثناء التطوير.
- **إصدار DirB**: يبدو هذا وكأنه نسخة قديمة/معدلة (إشارات إلى `lanza_ataque.c`، إلخ.). إذا كان من GitHub، تحقق من إصلاحات المصدر الأصلي: [dirb on GitHub](https://github.com/v0re/dirb).
- **التبعيات**: تأكد من تثبيت libcurl (`sudo apt install libcurl4-openssl-dev` في أنظمة دبيان).
- إذا استمرت المشاكل (مثلاً، تعريف `struct opciones` مفقود)، شارك محتويات `variables.h` للمساعدة أكثر.

هذا يجب أن يجعل عملية الربط نظيفة! إذا قمت بلصق المزيد من الأكواد/السجلات، يمكنني التحسين.