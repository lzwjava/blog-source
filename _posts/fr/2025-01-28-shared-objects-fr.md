---
audio: false
generated: false
lang: fr
layout: post
title: Objets Partagés dans Plusieurs Threads
translated: true
---

## Leçon

Le code présente un bug intermittent, se manifestant de manière inconsistante. Son caractère sporadique le rend difficile à reproduire et à déboguer efficacement.

Ce comportement intermittent provient de la manière dont la fonction `translate_markdown_file`, en particulier la fonction `translate_front_matter`, gère les données partagées. Ces fonctions peuvent accéder et modifier des structures de données partagées, telles que des dictionnaires ou des listes, sans synchronisation appropriée.

Lorsque plusieurs threads accèdent et modifient les mêmes données simultanément, cela peut entraîner des conditions de course. Les conditions de course se produisent lorsque l'état final des données dépend de l'ordre imprévisible dans lequel les threads s'exécutent. Cela peut entraîner la corruption des données, des comportements inattendus du programme et les bugs intermittents que vous observez.

Pour corriger cela, vous devez soit éviter de partager des données mutables entre les threads, soit utiliser des mécanismes de synchronisation appropriés, tels que des verrous, pour protéger les données partagées. Dans ce cas, `front_matter_dict` est modifié en place, ce qui n'est pas sûr pour les threads. La correction consiste à créer une copie du dictionnaire avant de le modifier. Cela est déjà fait dans le code, mais il est important de comprendre pourquoi cela est nécessaire.

## Contexte

```python
  with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        for filename in changed_files:
            input_file = filename

            for lang in languages:

                print(f"Submission de la tâche de traduction pour {filename} en {lang}...")
                future = executor.submit(translate_markdown_file, input_file, os.path.join(f"_posts/{lang}", os.path.basename(filename).replace(".md", f"-{lang}.md")), lang, dry_run)
                futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Un thread a échoué: {e}")
```

## Avant

```python
def translate_front_matter(front_matter, target_language, input_file):
    print(f"  Traduction du front matter pour: {input_file}")
    if not front_matter:
        print(f"  Pas de front matter trouvé pour: {input_file}")
        return ""
    try:
        front_matter_dict = {}
        if front_matter:
            front_matter_dict = yaml.safe_load(front_matter)
            print(f"  Front matter après safe_load: {front_matter_dict}")
        if 'title' in front_matter_dict:
            print(f"  Traduction du titre: {front_matter_dict['title']}")
            if not (input_file == 'original/2025-01-11-resume-en.md' and target_language in ['zh', 'fr']):
                if isinstance(front_matter_dict['title'], str):
                    translated_title = translate_text(front_matter_dict['title'], target_language)
                    if translated_title:
                        translated_title = translated_title.strip()
                        if len(translated_title) > 300:
                            translated_title = translated_title.split('\n')[0]
                        front_matter_dict['title'] = translated_title
                        print(f"  Titre traduit en: {translated_title}")
                    else:
                        print(f"  La traduction du titre a échoué pour: {input_file}")
                else:
                    print(f"  Le titre n'est pas une chaîne, saut de traduction pour: {input_file}")
            else:
                print(f"  Saut de traduction du titre pour {input_file} en {target_language}")
        # Toujours définir lang en target_language

        # Déterminer si le fichier est une traduction
        original_lang = 'en' # Par défaut en anglais
        if 'lang' in front_matter_dict:
            original_lang = front_matter_dict['lang']

        if target_language != original_lang:
            front_matter_dict['lang'] = target_language
            front_matter_dict['translated'] = True
            print(f"  Marqué comme traduit en {target_language} pour: {input_file}")
        else:
            front_matter_dict['translated'] = False
            print(f"  Non marqué comme traduit pour: {input_file}")

        result = "---\n" + yaml.dump(front_matter_dict, allow_unicode=True) + "---"
        print(f"  Traduction du front matter terminée pour: {input_file}")
        return result
    except yaml.YAMLError as e:
        print(f"  Erreur de parsing du front matter: {e}")
        return front_matter
```

## Après

```python
def translate_front_matter(front_matter, target_language, input_file):
    print(f"  Traduction du front matter pour: {input_file}")
    if not front_matter:
        print(f"  Pas de front matter trouvé pour: {input_file}")
        return ""
    try:
        front_matter_dict = {}
        if front_matter:
            front_matter_dict = yaml.safe_load(front_matter)
            print(f"  Front matter après safe_load: {front_matter_dict}")

        front_matter_dict_copy = front_matter_dict.copy()

        if 'title' in front_matter_dict_copy:
            print(f"  Traduction du titre: {front_matter_dict_copy['title']}")
            if not (input_file == 'original/2025-01-11-resume-en.md' and target_language in ['zh', 'fr']):
                if isinstance(front_matter_dict_copy['title'], str):
                    translated_title = translate_text(front_matter_dict_copy['title'], target_language)
                    if translated_title:
                        translated_title = translated_title.strip()
                        if len(translated_title) > 300:
                            translated_title = translated_title.split('\n')[0]
                        front_matter_dict_copy['title'] = translated_title
                        print(f"  Titre traduit en: {translated_title}")
                    else:
                        print(f"  La traduction du titre a échoué pour: {input_file}")
                else:
                    print(f"  Le titre n'est pas une chaîne, saut de traduction pour: {input_file}")
            else:
                print(f"  Saut de traduction du titre pour {input_file} en {target_language}")
        # Toujours définir lang en target_language

        front_matter_dict_copy['lang'] = target_language
        front_matter_dict_copy['translated'] = True

        result = "---\n" + yaml.dump(front_matter_dict_copy, allow_unicode=True) + "---"
        print(f"  Traduction du front matter terminée pour: {input_file}")
        return result
    except yaml.YAMLError as e:
        print(f"  Erreur de parsing du front matter: {e}")
        return front_matter
```