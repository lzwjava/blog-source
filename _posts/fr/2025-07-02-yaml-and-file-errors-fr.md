---
audio: false
generated: true
lang: fr
layout: post
title: Résoudre les erreurs YAML et de fichiers dans Jekyll
translated: true
type: note
---

La sortie que vous avez fournie montre deux types d'erreurs :

1.  **Exception YAML :** Cela indique un problème avec le front matter (le bloc YAML en haut) de vos fichiers Markdown :

      * `/Users/lzwjava/projects/lzwjava.github.io/notes/2025-06-25-company-valuation-comparison-en.md`
      * `/Users/lzwjava/projects/lzwjava.github.io/notes/2025-06-25-top-companies-evolve-en.md`
        L'erreur "did not find expected key while parsing a block mapping at line 2 column 1" suggère que la syntaxe YAML dans ces fichiers est incorrecte, probablement due à une clé manquante ou à un problème d'indentation dans le front matter.

2.  **`Errno::ENOENT: No such file or directory @ rb_sysopen - /Users/lzwjava/projects/lzwjava.github.io/wandb/debug-internal.log`** : Cette erreur indique que Jekyll tente d'accéder à un fichier ou un répertoire qui n'existe pas, spécifiquement `/wandb/debug-internal.log`. Il pourrait s'agir d'un fichier temporaire ou d'une dépendance d'un autre outil (comme Weights & Biases - `wandb`) que Jekyll tente de traiter.

Pour répondre à votre question sur la façon de demander à Jekyll d'ignorer certains répertoires, vous pouvez utiliser l'option `exclude` dans votre fichier `_config.yml`.

Voici comment procéder :

1.  **Ouvrez votre fichier `_config.yml`** (situé à la racine de votre projet Jekyll).

2.  **Ajoutez ou modifiez la directive `exclude`.** Cette directive prend un tableau de chemins (fichiers ou répertoires) que Jekyll doit ignorer pendant son processus de build.

    Par exemple, pour ignorer le répertoire `wandb` et tout autre répertoire que vous souhaitez exclure, ajoutez ce qui suit à votre `_config.yml` :

    ```yaml
    exclude:
      - wandb/
      - some_other_directory/
      - another_file_to_ignore.md
    ```

    **Notes importantes :**

      * Assurez-vous d'inclure la barre oblique finale (`/`) pour les répertoires afin que tout leur contenu soit ignoré.
      * Les chemins sont relatifs à la racine de votre projet Jekyll.

**Résolution de vos erreurs spécifiques avec `exclude` :**

  * **Pour l'erreur du répertoire `wandb` :** Ajouter `wandb/` à votre liste `exclude` dans `_config.yml` devrait empêcher Jekyll de tenter de lire les fichiers qu'il contient, résolvant ainsi l'erreur `No such file or directory` pour `wandb/debug-internal.log`.

  * **Pour l'exception YAML :** La directive `exclude` ne corrigera pas les erreurs YAML dans vos fichiers Markdown. Vous devez **corriger manuellement le front matter** dans `notes/2025-06-25-company-valuation-comparison-en.md` et `notes/2025-06-25-top-companies-evolve-en.md`.

    **Structure typique du Front Matter Jekyll :**

    ```yaml
    ---
    layout: post
    title: "Mon Article Génial"
    date: 2025-07-02 10:00:00 +0800
    categories: [notes, tech]
    tags: [jekyll, markdown]
    ---

    Votre contenu va ici.
    ```

    Vérifiez soigneusement les fichiers mentionnés dans l'exception YAML pour vous assurer qu'ils suivent cette structure, en particulier en ce qui concerne l'indentation et les paires clé-valeur correctes. L'erreur "did not find expected key while parsing a block mapping at line 2 column 1" suggère qu'un problème survient dès le début de votre front matter, peut-être une clé manquante ou un espace supplémentaire là où une clé devrait se trouver.

Après avoir apporté ces modifications à votre `_config.yml` et corrigé vos fichiers Markdown, essayez de relancer votre commande Jekyll `build` ou `serve`.