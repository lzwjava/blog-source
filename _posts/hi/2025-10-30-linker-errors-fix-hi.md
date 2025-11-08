---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: सी लिंकर मल्टीपल डेफिनिशन एरर्स को ठीक करना
translated: true
type: note
---

### DirB के लिए बिल्ड समस्याएं और उनके समाधान

आपकी बिल्ड लॉग अलग-अलग स्रोत फ़ाइलों के सफल कंपाइलेशन (कुछ वार्निंग्स के साथ) को दिखाती है, लेकिन अंतिम लिंकिंग चरण में **ग्लोबल वेरिएबल्स और स्ट्रक्चर्स के लिए मल्टीपल डेफिनिशन एरर** के कारण यह विफल हो जाती है। यह एक सामान्य C समस्या है जब हेडर फाइलें ग्लोबल्स को डिफाइन करती हैं (सिर्फ डिक्लेयर करने के बजाय)। मैं इसे समझाता हूं: पहले वार्निंग्स (नॉन-फेटल लेकिन ठीक करने लायक), फिर घातक लिंकर एरर के साथ एक चरण-दर-चरण समाधान।

#### 1. कंपाइलेशन वार्निंग्स (नॉन-फेटल)
ये GCC के `-Wall` फ्लैग से हैं। ये बिल्ड को नहीं रोकतीं लेकिन संभावित बग्स की ओर इशारा करती हैं। आउटपुट साफ करने के लिए इन्हें ठीक करें।

- **utils.c**:
  - लाइन ~4 (`location_cmp()` में): फॉर्मेट स्पेसिफायर मिसमैच। `strlen()` `size_t` (अनसाइंड लॉन्ग) रिटर्न करता है, लेकिन आप `%d` (इंट) का उपयोग कर रहे हैं।
    **समाधान**: `printf` में `%d` को `%zu` में बदलें:
    ```c
    printf("[++++] location_cmp() RESULT: %d (%zu)\n", result, strlen(A) > strlen(B) ? strlen(A) : strlen(B));
    ```
  - लाइन 287 (`kbhit()` में): `read()` के रिटर्न वैल्यू को इग्नोर कर रहे हैं (यह फेल हो सकता है)।
    **समाधान**: रिटर्न वैल्यू चेक करें:
    ```c
    if (read(0, &key, 1) != 1) {
        // एरर हैंडल करें, उदा., return 0;
    }
    ```

- **resume.c**:
  - लाइन 32 (`dump()` में): मिसलीडिंग इंडेंटेशन—`fflush(stdout)` `if` द्वारा गार्डेड नहीं है।
    **समाधान**: ब्रेसिज़ जोड़ें या रीइंडेंट करें:
    ```c
    if (options.debuging > 2) {
        printf("[++] dump() Dumping Session State AT %s", asctime(ptr));
        fflush(stdout);
    }
    ```
  - लाइन 38–41 और 109–112: `asprintf()` के रिटर्न वैल्यू को इग्नोर कर रहे हैं (यह फेल हो सकता है और पॉइंटर्स को अनइनिशियलाइज्ड छोड़ सकता है)।
    **समाधान**: रिटर्न चेक करें (उदा., `if (asprintf(&dumppath, ...) < 0) { /* error */ }`)। सभी कॉल्स के लिए ऐसा करें।
  - लाइन 120 (`resume()` में): `fread()` के रिटर्न वैल्यू को इग्नोर कर रहे हैं (यह पूरी स्ट्रक्चर नहीं पढ़ सकता)।
    **समाधान**: इसे चेक करें:
    ```c
    if (fread(&options, sizeof(struct opciones), 1, desc) != 1) {
        // एरर हैंडल करें, उदा., fclose(desc); return;
    }
    ```

फिक्सेस के बाद रीकंपाइल करें: `make clean && make` (मान लें कि एक Makefile है; यदि नहीं, तो अपने gcc कमांड्स को दोबारा रन करें)।

#### 2. घातक लिंकर एरर (मल्टीपल डेफिनिशन)
लिंकर (`/usr/bin/ld`) दर्जनों सिंबल्स (जैसे `options`, `encontradas`, `curl`, आदि) के ऑब्जेक्ट फाइल्स (`dirb.o`, `crea_wordlist.o`, आदि) में मल्टीपल बार डिफाइन होने की शिकायत करता है। सभी का पता `/home/lzwjava/projects/dirb/src/variables.h:XX` से लगता है।

**मूल कारण**:
`variables.h` संभवतः इन ग्लोबल्स को सीधे **डिफाइन** करती है (उदा., `struct opciones options;`) बजाय उन्हें `extern` के रूप में **डिक्लेयर** करने के। जब इसे कई `.c` फाइलों में शामिल किया जाता है, तो प्रत्येक अपनी खुद की डेफिनिशन की एक कॉपी के साथ एक `.o` में कंपाइल हो जाता है। लिंकिंग उन्हें मर्ज करती है, जिससे कॉन्फ्लिक्ट होते हैं।

**समाधान**:
शेयर्ड ग्लोबल्स के लिए "extern" पैटर्न का उपयोग करें:
- हेडर में `extern` के साथ **डिक्लेयर** करें (कंपाइलर को बताता है "यह कहीं और मौजूद है")।
- **एक्सैक्टली एक** `.c` फाइल (उदा., `dirb.c`) में **डिफाइन** करें (`extern` के बिना)।

चरण:
1. **`variables.h` एडिट करें** (`src/` में): सभी ग्लोबल वेरिएबल/स्ट्रक्चर्स को `extern` से प्रीफिक्स करें। एरर के आधार पर उदाहरण:
   ```c
   // पहले (खराब: हर .o में डिफाइन करता है)
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

   // बाद में (अच्छा: सिर्फ डिक्लेयर करता है)
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
   - टॉप पर आवश्यक हेडर शामिल करें: `#include <stdio.h>`, `#include <curl/curl.h>`, आदि।
   - यदि `struct opciones` हेडर में डिफाइन है, तो उसे रखें (स्ट्रक्चर्स हेडर में डिफाइन किए जा सकते हैं)।

2. **एक सोर्स फाइल चुनें** (उदा., `dirb.c`, मुख्य फाइल) और वहां ग्लोबल्स को **डिफाइन** करें (`extern` के बिना):
   ```c
   // dirb.c में, इंक्लूड्स के बाद
   struct opciones options = {0};  // आवश्यकता होने पर इनिशियलाइज़ करें
   int contador = 0;
   int nec = 0;
   FILE *outfile = NULL;
   CURL *curl = NULL;
   // ... बाकी सभी के लिए दोहराएं, समझदारी से इनिशियलाइज़ करते हुए (उदा., इंट्स को 0, पॉइंटर्स को NULL)
   ```

3. **क्लीन और रीबिल्ड करें**:
   ```
   make clean  # या rm *.o
   # अपने कंपाइल कमांड्स को दोबारा रन करें, फिर अंतिम लिंक:
   gcc -Wall -g -O2 -o dirb crea_wordlist.o dirb.o get_url.o lanza_ataque.o calculanec.o utils.o options.o resume.o -lcurl
   ```

4. **वेरिफाई करें**:
   - टेस्ट करने के लिए `./dirb --help` रन करें।
   - यदि नई एरर आती हैं (उदा., अनडिफाइंड सिंबल्स), सुनिश्चित करें कि डेफिनिशन `dirb.c` में हैं और सभी फाइलें `variables.h` को इंक्लूड करती हैं।

#### अतिरिक्त नोट्स
- **Makefile?** यदि यह `Makefile` से है, तो डेव के दौरान वार्निंग्स को एरर की तरह ट्रीट करने के लिए अस्थायी रूप से `-Werror` ऐड करें।
- **DirB वर्जन**: यह एक पुराने/कस्टम फोर्क जैसा दिखता है (`lanza_ataque.c` आदि के संदर्भ)। यदि यह GitHub से है, तो अपस्ट्रीम फिक्सेस के लिए चेक करें: [dirb on GitHub](https://github.com/v0re/dirb)।
- **डिपेंडेंसीज**: सुनिश्चित करें कि libcurl इंस्टॉल है (`sudo apt install libcurl4-openssl-dev` डेबियन-आधारित सिस्टम पर)।
- यदि समस्याएं बनी रहती हैं (उदा., `struct opciones` डेफ गायब), तो और मदद के लिए `variables.h` की सामग्री शेयर करें।

इससे यह क्लीनली लिंक हो जाना चाहिए! यदि आप और कोड/लॉग पेस्ट करते हैं, तो मैं रिफाइन कर सकता हूं।