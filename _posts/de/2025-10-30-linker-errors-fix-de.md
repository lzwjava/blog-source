---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Beheben von C Linker-Fehlern durch Mehrfachdefinitionen
translated: true
type: note
---

### Build-Probleme und Lösungen für DirB

Ihr Build-Protokoll zeigt eine erfolgreiche Kompilierung der einzelnen Quelldateien (mit einigen Warnungen), aber es scheitert im finalen Linking-Schritt aufgrund von **Mehrfachdefinitionsfehlern** für globale Variablen und Strukturen. Dies ist ein häufiges C-Problem, wenn Header-Dateien Globale definieren (anstatt sie nur zu deklarieren). Ich werde es aufschlüsseln: zuerst die Warnungen (nicht fatal, aber behebenswert), dann die fatalen Linker-Fehler mit einer Schritt-für-Schritt-Lösung.

#### 1. Kompilierungs-Warnungen (Nicht Fatal)
Diese stammen von GCCs `-Wall`-Flag. Sie stoppen den Build nicht, deuten aber auf potenzielle Fehler hin. Beheben Sie sie, um die Ausgabe zu bereinigen.

- **utils.c**:
  - Zeile ~4 (in `location_cmp()`): Format-Spezifizierer stimmen nicht überein. `strlen()` gibt `size_t` (unsigned long) zurück, aber Sie verwenden `%d` (int).  
    **Fix**: Ändern Sie `%d` zu `%zu` im `printf`:  
    ```c
    printf("[++++] location_cmp() RESULT: %d (%zu)\n", result, strlen(A) > strlen(B) ? strlen(A) : strlen(B));
    ```
  - Zeile 287 (in `kbhit()`): Der Rückgabewert von `read()` wird ignoriert (er kann fehlschlagen).  
    **Fix**: Überprüfen Sie den Rückgabewert:  
    ```c
    if (read(0, &key, 1) != 1) {
        // Fehler behandeln, z.B. return 0;
    }
    ```

- **resume.c**:
  - Zeile 32 (in `dump()`): Irreführende Einrückung – `fflush(stdout)` ist nicht durch das `if` geschützt.  
    **Fix**: Fügen Sie geschweifte Klammern hinzu oder ändern Sie die Einrückung:  
    ```c
    if (options.debuging > 2) {
        printf("[++] dump() Dumping Session State AT %s", asctime(ptr));
        fflush(stdout);
    }
    ```
  - Zeilen 38–41 und 109–112: Die Rückgabewerte von `asprintf()` werden ignoriert (es kann fehlschlagen und Zeiger uninitialisiert lassen).  
    **Fix**: Überprüfen Sie die Rückgaben (z.B. `if (asprintf(&dumppath, ...) < 0) { /* error */ }`). Machen Sie das für alle Aufrufe.
  - Zeile 120 (in `resume()`): Der Rückgabewert von `fread()` wird ignoriert (es könnte nicht die gesamte Struktur lesen).  
    **Fix**: Überprüfen Sie ihn:  
    ```c
    if (fread(&options, sizeof(struct opciones), 1, desc) != 1) {
        // Fehler behandeln, z.B. fclose(desc); return;
    }
    ```

Kompilieren Sie nach den Fixes erneut: `make clean && make` (angenommen, es gibt ein Makefile; wenn nicht, führen Sie Ihre gcc-Befehle erneut aus).

#### 2. Fatale Linker-Fehler (Mehrfachdefinitionen)
Der Linker (`/usr/bin/ld`) beklagt sich über Dutzende von Symbolen (z.B. `options`, `encontradas`, `curl`, etc.), die in mehreren Objektdateien (`dirb.o`, `crea_wordlist.o`, etc.) mehrfach definiert sind. Alle führen zurück auf `/home/lzwjava/projects/dirb/src/variables.h:XX`.

**Ursache**:  
`variables.h` definiert diese Globale wahrscheinlich **direkt** (z.B. `struct opciones options;`) anstatt sie nur als `extern` zu **deklarieren**. Wenn sie in mehreren `.c`-Dateien eingebunden wird, kompiliert jede zu einer `.o` mit ihrer eigenen Kopie der Definitionen. Beim Linking werden diese zusammengeführt, was zu Konflikten führt.

**Lösung**:  
Verwenden Sie das "extern"-Muster für gemeinsame Globale:
- **Deklarieren** Sie im Header mit `extern` (teilt dem Compiler mit "dies existiert woanders").
- **Definieren** Sie (ohne `extern`) in **genau einer** `.c`-Datei (z.B. `dirb.c`).

Schritte:
1. **Bearbeiten Sie `variables.h`** (in `src/`): Setzen Sie allen globalen Variablen/Strukturen `extern` voran. Beispiele basierend auf den Fehlern:
   ```c
   // Vorher (schlecht: definiert in jeder .o)
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

   // Nachher (gut: deklariert nur)
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
   - Binden Sie notwendige Header oben ein: `#include <stdio.h>`, `#include <curl/curl.h>`, etc.
   - Wenn `struct opciones` im Header definiert ist, belassen Sie das (Strukturen können in Headern definiert werden).

2. **Wählen Sie eine Quelldatei** (z.B. `dirb.c`, die Hauptdatei) und **definieren** Sie die Globale dort (ohne `extern`):
   ```c
   // In dirb.c, nach den Includes
   struct opciones options = {0};  // Initialisieren falls nötig
   int contador = 0;
   int nec = 0;
   FILE *outfile = NULL;
   CURL *curl = NULL;
   // ... Wiederholen Sie dies für alle anderen, mit sinnvoller Initialisierung (z.B. ints auf 0, Zeiger auf NULL)
   ```

3. **Bereinigen und neu erstellen**:
   ```
   make clean  # Oder rm *.o
   # Führen Sie Ihre Kompilierungsbefehle erneut aus, dann den finalen Link:
   gcc -Wall -g -O2 -o dirb crea_wordlist.o dirb.o get_url.o lanza_ataque.o calculanec.o utils.o options.o resume.o -lcurl
   ```

4. **Überprüfen Sie**:
   - Führen Sie `./dirb --help` zum Testen aus.
   - Wenn neue Fehler auftauchen (z.B. undefinierte Symbole), stellen Sie sicher, dass die Definitionen in `dirb.c` sind und alle Dateien `variables.h` einbinden.

#### Zusätzliche Hinweise
- **Makefile?** Wenn dies aus einem `Makefile` stammt, fügen Sie vorübergehend `-Werror` hinzu, um Warnungen während der Entwicklung als Fehler zu behandeln.
- **DirB Version**: Dies sieht nach einem älteren/geforkten Code aus (Verweise auf `lanza_ataque.c`, etc.). Wenn es von GitHub stammt, prüfen Sie auf Upstream-Fixes: [dirb on GitHub](https://github.com/v0re/dirb).
- **Abhängigkeiten**: Stellen Sie sicher, dass libcurl installiert ist (`sudo apt install libcurl4-openssl-dev` auf Debian-basierten Systemen).
- Falls Probleme bestehen bleiben (z.B. fehlende `struct opciones` Def.), teilen Sie den Inhalt von `variables.h` für weitere Hilfe mit.

Dies sollte das Linking sauber durchführen lassen! Wenn Sie mehr Code/Logs posten, kann ich die Lösung verfeinern.