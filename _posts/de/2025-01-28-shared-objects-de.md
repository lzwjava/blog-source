---
audio: false
generated: true
lang: de
layout: post
title: Gemeinsame Objekte in Mehreren Threads
translated: true
---

## Lektion

Der Code zeigt einen intermittierenden Fehler, der sich unkonsistent manifestiert. Seine sporadische Natur macht es schwierig, ihn reproduzierbar und effektiv zu debuggen.

Dieses intermittierende Verhalten hängt damit zusammen, wie die `translate_markdown_file`-Funktion, insbesondere die `translate_front_matter`-Funktion, geteilte Daten behandelt. Diese Funktionen könnten geteilte Datenstrukturen, wie Wörterbücher oder Listen, ohne ordnungsgemäße Synchronisation lesen und ändern.

Wenn mehrere Threads gleichzeitig auf die gleichen Daten zugreifen und diese ändern, kann dies zu Rennenbedingungen führen. Rennenbedingungen treten auf, wenn der finale Zustand der Daten von der unvorhersehbaren Reihenfolge abhängt, in der die Threads ausgeführt werden. Dies kann zu Datenkorruption, unerwartetem Programmverhalten und den intermittierenden Fehlern führen, die Sie beobachten.

Um dies zu beheben, sollten Sie entweder vermeiden, zwischen Threads mutable Daten zu teilen, oder ordnungsgemäße Synchronisierungsmechanismen, wie Sperren, verwenden, um geteilte Daten zu schützen. In diesem Fall wird `front_matter_dict` in place geändert, was nicht thread-sicher ist. Die Lösung besteht darin, eine Kopie des Wörterbuchs vor dem Ändern zu erstellen. Dies wird bereits im Code durchgeführt, es ist jedoch wichtig zu verstehen, warum dies erforderlich ist.

## Kontext

```python
  with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        for filename in changed_files:
            input_file = filename

            for lang in languages:

                print(f"Übermittlung der Übersetzungsaufgabe für {filename} an {lang}...")
                future = executor.submit(translate_markdown_file, input_file, os.path.join(f"_posts/{lang}", os.path.basename(filename).replace(".md", f"-{lang}.md")), lang, dry_run)
                futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Ein Thread ist fehlgeschlagen: {e}")
```

## Vorher

```python
def translate_front_matter(front_matter, target_language, input_file):
    print(f"  Übersetzung der Frontmatter für: {input_file}")
    if not front_matter:
        print(f"  Keine Frontmatter für: {input_file} gefunden")
        return ""
    try:
        front_matter_dict = {}
        if front_matter:
            front_matter_dict = yaml.safe_load(front_matter)
            print(f"  Frontmatter nach safe_load: {front_matter_dict}")
        if 'title' in front_matter_dict:
            print(f"  Übersetzung des Titels: {front_matter_dict['title']}")
            if not (input_file == 'original/2025-01-11-resume-en.md' and target_language in ['zh', 'fr']):
                if isinstance(front_matter_dict['title'], str):
                    translated_title = translate_text(front_matter_dict['title'], target_language)
                    if translated_title:
                        translated_title = translated_title.strip()
                        if len(translated_title) > 300:
                            translated_title = translated_title.split('\n')[0]
                        front_matter_dict['title'] = translated_title
                        print(f"  Titelübersetzung abgeschlossen: {translated_title}")
                    else:
                        print(f"  Übersetzung des Titels fehlgeschlagen für: {input_file}")
                else:
                    print(f"  Titel ist kein String, Übersetzung wird für: {input_file} übersprungen")
            else:
                print(f"  Übersetzung des Titels für {input_file} zu {target_language} wird übersprungen")
        # Sprache immer auf target_language setzen

        # Ermitteln, ob die Datei eine Übersetzung ist
        original_lang = 'en' # Standardmäßig Englisch
        if 'lang' in front_matter_dict:
            original_lang = front_matter_dict['lang']

        if target_language != original_lang:
            front_matter_dict['lang'] = target_language
            front_matter_dict['translated'] = True
            print(f"  Als übersetzt markiert: {target_language} für: {input_file}")
        else:
            front_matter_dict['translated'] = False
            print(f"  Nicht als übersetzt markiert für: {input_file}")

        result = "---\n" + yaml.dump(front_matter_dict, allow_unicode=True) + "---"
        print(f"  Übersetzung der Frontmatter abgeschlossen für: {input_file}")
        return result
    except yaml.YAMLError as e:
        print(f"  Fehler beim Parsen der Frontmatter: {e}")
        return front_matter
```

## Danach

```python
def translate_front_matter(front_matter, target_language, input_file):
    print(f"  Übersetzung der Frontmatter für: {input_file}")
    if not front_matter:
        print(f"  Keine Frontmatter für: {input_file} gefunden")
        return ""
    try:
        front_matter_dict = {}
        if front_matter:
            front_matter_dict = yaml.safe_load(front_matter)
            print(f"  Frontmatter nach safe_load: {front_matter_dict}")

        front_matter_dict_copy = front_matter_dict.copy()

        if 'title' in front_matter_dict_copy:
            print(f"  Übersetzung des Titels: {front_matter_dict_copy['title']}")
            if not (input_file == 'original/2025-01-11-resume-en.md' and target_language in ['zh', 'fr']):
                if isinstance(front_matter_dict_copy['title'], str):
                    translated_title = translate_text(front_matter_dict_copy['title'], target_language)
                    if translated_title:
                        translated_title = translated_title.strip()
                        if len(translated_title) > 300:
                            translated_title = translated_title.split('\n')[0]
                        front_matter_dict_copy['title'] = translated_title
                        print(f"  Titelübersetzung abgeschlossen: {translated_title}")
                    else:
                        print(f"  Übersetzung des Titels fehlgeschlagen für: {input_file}")
                else:
                    print(f"  Titel ist kein String, Übersetzung wird für: {input_file} übersprungen")
            else:
                print(f"  Übersetzung des Titels für {input_file} zu {target_language} wird übersprungen")
        # Sprache immer auf target_language setzen

        front_matter_dict_copy['lang'] = target_language
        front_matter_dict_copy['translated'] = True

        result = "---\n" + yaml.dump(front_matter_dict_copy, allow_unicode=True) + "---"
        print(f"  Übersetzung der Frontmatter abgeschlossen für: {input_file}")
        return result
    except yaml.YAMLError as e:
        print(f"  Fehler beim Parsen der Frontmatter: {e}")
        return front_matter
```