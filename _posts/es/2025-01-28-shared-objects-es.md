---
audio: false
generated: false
image: false
lang: es
layout: post
title: Objetos Compartidos en Múltiples Hilos
translated: true
---

## Lección

El código presenta un fallo intermitente que se manifiesta de manera inconsistente. Su naturaleza esporádica dificulta su reproducción y depuración efectivas.

Este comportamiento intermitente se debe a la manera en que la función `translate_markdown_file`, particularmente la función `translate_front_matter`, maneja los datos compartidos. Estas funciones pueden estar accediendo y modificando estructuras de datos compartidas, como diccionarios o listas, sin una sincronización adecuada.

Cuando múltiples hilos acceden y modifican los mismos datos de manera concurrente, esto puede llevar a condiciones de carrera. Las condiciones de carrera ocurren cuando el estado final de los datos depende del orden impredecible en que los hilos se ejecutan. Esto puede resultar en corrupción de datos, comportamiento inesperado del programa y los fallos intermitentes que estás observando.

Para corregir esto, debes evitar compartir datos mutables entre hilos o utilizar mecanismos de sincronización adecuados, como bloqueos, para proteger los datos compartidos. En este caso, `front_matter_dict` se está modificando en su lugar, lo cual no es seguro para hilos. La solución es crear una copia del diccionario antes de modificarlo. Esto ya se hace en el código, pero es importante entender por qué es necesario.

## Contexto

```python
  with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        for filename in changed_files:
            input_file = filename

            for lang in languages:

                print(f"Enviando trabajo de traducción para {filename} a {lang}...")
                future = executor.submit(translate_markdown_file, input_file, os.path.join(f"_posts/{lang}", os.path.basename(filename).replace(".md", f"-{lang}.md")), lang, dry_run)
                futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Un hilo falló: {e}")
```

## Antes

```python
def translate_front_matter(front_matter, target_language, input_file):
    print(f"  Traduciendo el front matter para: {input_file}")
    if not front_matter:
        print(f"  No se encontró front matter para: {input_file}")
        return ""
    try:
        front_matter_dict = {}
        if front_matter:
            front_matter_dict = yaml.safe_load(front_matter)
            print(f"  Front matter después de safe_load: {front_matter_dict}")
        if 'title' in front_matter_dict:
            print(f"  Traduciendo el título: {front_matter_dict['title']}")
            if not (input_file == 'original/2025-01-11-resume-en.md' and target_language in ['zh', 'fr']):
                if isinstance(front_matter_dict['title'], str):
                    translated_title = translate_text(front_matter_dict['title'], target_language)
                    if translated_title:
                        translated_title = translated_title.strip()
                        if len(translated_title) > 300:
                            translated_title = translated_title.split('\n')[0]
                        front_matter_dict['title'] = translated_title
                        print(f"  Traducido el título a: {translated_title}")
                    else:
                        print(f"  Falló la traducción del título para: {input_file}")
                else:
                    print(f"  El título no es una cadena, se omite la traducción para: {input_file}")
            else:
                print(f"  Se omite la traducción del título para {input_file} a {target_language}")
        # Siempre establece lang en target_language

        # Determinar si el archivo es una traducción
        original_lang = 'en' # Predeterminado a inglés
        if 'lang' in front_matter_dict:
            original_lang = front_matter_dict['lang']

        if target_language != original_lang:
            front_matter_dict['lang'] = target_language
            front_matter_dict['translated'] = True
            print(f"  Marcado como traducido a {target_language} para: {input_file}")
        else:
            front_matter_dict['translated'] = False
            print(f"  No marcado como traducido para: {input_file}")

        result = "---\n" + yaml.dump(front_matter_dict, allow_unicode=True) + "---"
        print(f"  Traducción del front matter completada para: {input_file}")
        return result
    except yaml.YAMLError as e:
        print(f"  Error al parsear el front matter: {e}")
        return front_matter
```

## Después

```python
def translate_front_matter(front_matter, target_language, input_file):
    print(f"  Traduciendo el front matter para: {input_file}")
    if not front_matter:
        print(f"  No se encontró front matter para: {input_file}")
        return ""
    try:
        front_matter_dict = {}
        if front_matter:
            front_matter_dict = yaml.safe_load(front_matter)
            print(f"  Front matter después de safe_load: {front_matter_dict}")

        front_matter_dict_copy = front_matter_dict.copy()

        if 'title' in front_matter_dict_copy:
            print(f"  Traduciendo el título: {front_matter_dict_copy['title']}")
            if not (input_file == 'original/2025-01-11-resume-en.md' and target_language in ['zh', 'fr']):
                if isinstance(front_matter_dict_copy['title'], str):
                    translated_title = translate_text(front_matter_dict_copy['title'], target_language)
                    if translated_title:
                        translated_title = translated_title.strip()
                        if len(translated_title) > 300:
                            translated_title = translated_title.split('\n')[0]
                        front_matter_dict_copy['title'] = translated_title
                        print(f"  Traducido el título a: {translated_title}")
                    else:
                        print(f"  Falló la traducción del título para: {input_file}")
                else:
                    print(f"  El título no es una cadena, se omite la traducción para: {input_file}")
            else:
                print(f"  Se omite la traducción del título para {input_file} a {target_language}")
        # Siempre establece lang en target_language

        front_matter_dict_copy['lang'] = target_language
        front_matter_dict_copy['translated'] = True

        result = "---\n" + yaml.dump(front_matter_dict_copy, allow_unicode=True) + "---"
        print(f"  Traducción del front matter completada para: {input_file}")
        return result
    except yaml.YAMLError as e:
        print(f"  Error al parsear el front matter: {e}")
        return front_matter
```