---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Résoudre les Erreurs de Définitions Multiples de l'Éditeur de Liens C
translated: true
type: note
---

### Problèmes de compilation et correctifs pour DirB

Votre journal de compilation montre une compilation réussie des fichiers source individuels (avec quelques avertissements), mais il échoue lors de l'étape d'édition des liens finale en raison d'**erreurs de définitions multiples** pour les variables globales et les structures. C'est un problème courant en C lorsque les fichiers d'en-tête définissent (plutôt que de simplement déclarer) des variables globales. Je vais décomposer cela : d'abord les avertissements (non fatals mais utiles à corriger), puis les erreurs d'édition de liens fatales avec un correctif étape par étape.

#### 1. Avertissements de compilation (Non fatals)
Ceux-ci proviennent du drapeau `-Wall` de GCC. Ils n'arrêtent pas la compilation mais indiquent des bogues potentiels. Corrigez-les pour nettoyer la sortie.

- **utils.c** :
  - Ligne ~4 (dans `location_cmp()`) : Incompatibilité de spécificateur de format. `strlen()` renvoie `size_t` (unsigned long), mais vous utilisez `%d` (int).  
    **Correctif** : Changez `%d` en `%zu` dans le `printf` :  
    ```c
    printf("[++++] location_cmp() RESULT: %d (%zu)\n", result, strlen(A) > strlen(B) ? strlen(A) : strlen(B));
    ```
  - Ligne 287 (dans `kbhit()`) : Ignorer la valeur de retour de `read()` (elle peut échouer).  
    **Correctif** : Vérifiez la valeur de retour :  
    ```c
    if (read(0, &key, 1) != 1) {
        // Gérer l'erreur, par ex., return 0;
    }
    ```

- **resume.c** :
  - Ligne 32 (dans `dump()`) : Indentation trompeuse — `fflush(stdout)` n'est pas protégé par le `if`.  
    **Correctif** : Ajoutez des accolades ou réindentez :  
    ```c
    if (options.debuging > 2) {
        printf("[++] dump() Dumping Session State AT %s", asctime(ptr));
        fflush(stdout);
    }
    ```
  - Lignes 38–41 et 109–112 : Ignorer les valeurs de retour de `asprintf()` (elle peut échouer et laisser des pointeurs non initialisés).  
    **Correctif** : Vérifiez les retours (par ex., `if (asprintf(&dumppath, ...) < 0) { /* error */ }`). Faites cela pour tous les appels.
  - Ligne 120 (dans `resume()`) : Ignorer la valeur de retour de `fread()` (elle pourrait ne pas lire la structure complète).  
    **Correctif** : Vérifiez-la :  
    ```c
    if (fread(&options, sizeof(struct opciones), 1, desc) != 1) {
        // Gérer l'erreur, par ex., fclose(desc); return;
    }
    ```

Recompilez après les correctifs : `make clean && make` (en supposant un Makefile ; sinon, réexécutez vos commandes gcc).

#### 2. Erreurs d'édition de liens fatales (Définitions multiples)
L'éditeur de liens (`/usr/bin/ld`) se plaint de dizaines de symboles (par ex., `options`, `encontradas`, `curl`, etc.) définis plusieurs fois dans les fichiers objets (`dirb.o`, `crea_wordlist.o`, etc.). Tous remontent à `/home/lzwjava/projects/dirb/src/variables.h:XX`.

**Cause racine** :  
`variables.h` définit probablement ces globaux directement (par ex., `struct opciones options;`) au lieu de les **déclarer** comme `extern`. Lorsqu'il est inclus dans plusieurs fichiers `.c`, chacun compile vers un `.o` avec sa propre copie des définitions. L'édition de liens les fusionne, provoquant des conflits.

**Solution** :  
Utilisez le motif "extern" pour les variables globales partagées :
- **Déclarez** dans l'en-tête avec `extern` (indique au compilateur "ceci existe ailleurs").
- **Définissez** (sans `extern`) dans **exactement un** fichier `.c` (par ex., `dirb.c`).

Étapes :
1. **Modifiez `variables.h`** (dans `src/`) : Préfixez toutes les variables/structures globales avec `extern`. Exemples basés sur les erreurs :
   ```c
   // Avant (mauvais : définit dans chaque .o)
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

   // Après (bon : déclare seulement)
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
   - Incluez les en-têtes nécessaires en haut : `#include <stdio.h>`, `#include <curl/curl.h>`, etc.
   - Si `struct opciones` est défini dans l'en-tête, conservez-le (les structures peuvent être définies dans les en-têtes).

2. **Choisissez un fichier source** (par ex., `dirb.c`, le fichier principal) et **définissez** les globaux là (sans `extern`) :
   ```c
   // Dans dirb.c, après les includes
   struct opciones options = {0};  // Initialisez si nécessaire
   int contador = 0;
   int nec = 0;
   FILE *outfile = NULL;
   CURL *curl = NULL;
   // ... répétez pour tous les autres, en initialisant de manière sensée (par ex., les int à 0, les pointeurs à NULL)
   ```

3. **Nettoyez et reconstruisez** :
   ```
   make clean  # Ou rm *.o
   # Réexécutez vos commandes de compilation, puis l'édition de liens finale :
   gcc -Wall -g -O2 -o dirb crea_wordlist.o dirb.o get_url.o lanza_ataque.o calculanec.o utils.o options.o resume.o -lcurl
   ```

4. **Vérifiez** :
   - Exécutez `./dirb --help` pour tester.
   - Si de nouvelles erreurs apparaissent (par ex., symboles non définis), assurez-vous que les définitions sont dans `dirb.c` et que tous les fichiers incluent `variables.h`.

#### Notes supplémentaires
- **Makefile ?** Si cela provient d'un `Makefile`, ajoutez `-Werror` temporairement pour traiter les avertissements comme des erreurs pendant le développement.
- **Version de DirB** : Cela ressemble à un fork plus ancien/personnalisé (références à `lanza_ataque.c`, etc.). S'il provient de GitHub, vérifiez les correctifs en amont : [dirb sur GitHub](https://github.com/v0re/dirb).
- **Dépendances** : Assurez-vous que libcurl est installé (`sudo apt install libcurl4-openssl-dev` sur les systèmes basés sur Debian).
- Si les problèmes persistent (par ex., définition manquante de `struct opciones`), partagez le contenu de `variables.h` pour plus d'aide.

Cela devrait permettre une édition de liens propre ! Si vous collez plus de code/logs, je peux affiner.