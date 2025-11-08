---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Corrección de Errores de Definiciones Múltiples del Enlazador de C
translated: true
type: note
---

### Problemas y Soluciones de Compilación para DirB

Tu registro de compilación muestra una compilación exitosa de los archivos fuente individuales (con algunas advertencias), pero falla durante el paso de enlace final debido a **errores de definiciones múltiples** para variables globales y estructuras. Este es un problema común en C cuando los archivos de cabecera definen (en lugar de solo declarar) globales. Lo desglosaré: primero las advertencias (no fatales pero vale la pena corregirlas), luego los errores fatales del enlazador con una solución paso a paso.

#### 1. Advertencias de Compilación (No Fatales)
Estas provienen del flag `-Wall` de GCC. No detienen la compilación pero indican posibles errores. Corrígelas para limpiar la salida.

- **utils.c**:
  - Línea ~4 (en `location_cmp()`): Desajuste en el especificador de formato. `strlen()` devuelve `size_t` (unsigned long), pero estás usando `%d` (int).  
    **Solución**: Cambia `%d` por `%zu` en el `printf`:  
    ```c
    printf("[++++] location_cmp() RESULT: %d (%zu)\n", result, strlen(A) > strlen(B) ? strlen(A) : strlen(B));
    ```
  - Línea 287 (en `kbhit()`): Se ignora el valor de retorno de `read()` (puede fallar).  
    **Solución**: Verifica el valor de retorno:  
    ```c
    if (read(0, &key, 1) != 1) {
        // Manejar el error, ej., return 0;
    }
    ```

- **resume.c**:
  - Línea 32 (en `dump()`): Sangría engañosa—`fflush(stdout)` no está protegido por el `if`.  
    **Solución**: Añade llaves o re-sangra:  
    ```c
    if (options.debuging > 2) {
        printf("[++] dump() Dumping Session State AT %s", asctime(ptr));
        fflush(stdout);
    }
    ```
  - Líneas 38–41 y 109–112: Se ignoran los valores de retorno de `asprintf()` (puede fallar y dejar punteros sin inicializar).  
    **Solución**: Verifica los retornos (ej., `if (asprintf(&dumppath, ...) < 0) { /* error */ }`). Haz esto para todas las llamadas.
  - Línea 120 (en `resume()`): Se ignora el valor de retorno de `fread()` (podría no leer la estructura completa).  
    **Solución**: Verifícalo:  
    ```c
    if (fread(&options, sizeof(struct opciones), 1, desc) != 1) {
        // Manejar el error, ej., fclose(desc); return;
    }
    ```

Recompila después de las correcciones: `make clean && make` (asumiendo un Makefile; si no, vuelve a ejecutar tus comandos gcc).

#### 2. Errores Fatales del Enlazador (Definiciones Múltiples)
El enlazador (`/usr/bin/ld`) se queja de docenas de símbolos (ej., `options`, `encontradas`, `curl`, etc.) que están definidos múltiples veces en los archivos objeto (`dirb.o`, `crea_wordlist.o`, etc.). Todos se remontan a `/home/lzwjava/projects/dirb/src/variables.h:XX`.

**Causa Raíz**:  
Es probable que `variables.h` **defina** estas globales directamente (ej., `struct opciones options;`) en lugar de **declararlas** como `extern`. Cuando se incluye en múltiples archivos `.c`, cada uno compila a un `.o` con su propia copia de las definiciones. Al enlazar se fusionan, causando conflictos.

**Solución**:  
Usa el patrón "extern" para las globales compartidas:
- **Declara** en la cabecera con `extern` (le dice al compilador "esto existe en otro lugar").
- **Define** (sin `extern`) en **exactamente un** archivo `.c` (ej., `dirb.c`).

Pasos:
1. **Edita `variables.h`** (en `src/`): Añade el prefijo `extern` a todas las variables/estructuras globales. Ejemplos basados en los errores:
   ```c
   // Antes (malo: define en cada .o)
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

   // Después (bueno: solo declara)
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
   - Incluye las cabeceras necesarias al principio: `#include <stdio.h>`, `#include <curl/curl.h>`, etc.
   - Si `struct opciones` está definida en la cabecera, mantén eso (las estructuras pueden definirse en cabeceras).

2. **Elige un archivo fuente** (ej., `dirb.c`, el archivo principal) y **define** las globales allí (sin `extern`):
   ```c
   // En dirb.c, después de los includes
   struct opciones options = {0};  // Inicializa si es necesario
   int contador = 0;
   int nec = 0;
   FILE *outfile = NULL;
   CURL *curl = NULL;
   // ... repite para todos los demás, inicializando de forma sensata (ej., ints a 0, punteros a NULL)
   ```

3. **Limpia y recompila**:
   ```
   make clean  # O rm *.o
   # Vuelve a ejecutar tus comandos de compilación, luego el enlace final:
   gcc -Wall -g -O2 -o dirb crea_wordlist.o dirb.o get_url.o lanza_ataque.o calculanec.o utils.o options.o resume.o -lcurl
   ```

4. **Verifica**:
   - Ejecuta `./dirb --help` para probar.
   - Si aparecen nuevos errores (ej., símbolos no definidos), asegúrate de que las definiciones estén en `dirb.c` y que todos los archivos incluyan `variables.h`.

#### Notas Adicionales
- **¿Makefile?** Si esto es de un `Makefile`, añade `-Werror` temporalmente para tratar las advertencias como errores durante el desarrollo.
- **Versión de DirB**: Esto parece un fork antiguo/personalizado (referencias a `lanza_ataque.c`, etc.). Si es de GitHub, busca correcciones upstream: [dirb en GitHub](https://github.com/v0re/dirb).
- **Dependencias**: Asegúrate de que libcurl esté instalado (`sudo apt install libcurl4-openssl-dev` en sistemas basados en Debian).
- Si los problemas persisten (ej., falta la definición de `struct opciones`), comparte el contenido de `variables.h` para más ayuda.

¡Esto debería hacer que el enlace se realice correctamente! Si pegas más código/registros, puedo refinar la ayuda.