---
audio: false
generated: true
lang: de
layout: post
title: Optimierung der Übersetzung mit Absatz-Hashing
translated: true
type: note
---

### Gedanken zur Optimierung Ihres Übersetzungs-Workflows

Ihr Ziel ist klar: Minimieren Sie den KI-Token-Verbrauch für die Übersetzung von Jekyll-Blogbeiträgen (geschrieben in Markdown) in 8 Sprachen, indem Sie nur geänderte oder neue Absätze neu übersetzen und unveränderte zwischencachen. Sie möchten bei Markdown für die Bearbeitung bleiben, Datenbanken/JSON/YAML für Kerninhalte vermeiden und spezielle Elemente wie Codeblöcke behandeln (die nicht übersetzt werden sollten). Ein absatzbasierter Ansatz ist sinnvoll, da er mit Ihrer Art zu schreiben und zu bearbeiten übereinstimmt – Übersetzungen können auf dieser Ebene kontextuell genauer sein als auf Satzebene.

Wesentliche Herausforderungen:
- **Änderungen identifizieren**: Ohne Versionskontroll-Diffs benötigen Sie eine Methode, um zu erkennen, was neu/geändert/unverändert ist. Das Hashen von Absätzen (z. B. mit SHA-256 für normalisierten englischen Text) ist effizient und zustandslos – es müssen keine vollständigen alten Versionen gespeichert werden.
- **Umgang mit der Markdown-Struktur**: Sie können nicht einfach nach `\n\n` aufteilen, da Codeblöcke, Überschriften, Listen oder andere Syntax dies zerstören könnten. Ein einfacher regex-basierter Splitter könnte für einfache Beiträge funktionieren, aber ein leichtgewichtiger Markdown-Parser ist besser, um die Struktur zu erhalten und nicht übersetzbare Teile zu überspringen.
- **Caching**: Halten Sie es dateibasiert und einfach (z. B. eine JSON-Datei oder ein Verzeichnis mit Dateien), um Datenbanken zu vermeiden. Cache pro Absatz-Hash, pro Sprache.
- **Token-Einsparungen**: Bei langen Beiträgen könnte dies den Verbrauch bei kleinen Änderungen um 80-90 % senken, da nur betroffene Absätze die KI-API aufrufen.
- **Randfälle**: Hinzugefügte/gelöschte Absätze (behandeln durch erneutes Hashen); kleine Änderungen (z. B. Tippfehlerkorrekturen) lösen eine Neuübersetzung aus, es sei denn, Sie normalisieren Leerzeichen/Zeichensetzung; Codeblöcke oder Inline-Code müssen ausgeschlossen werden; wenn Absätze neu angeordnet werden, stimmen die Hashes nicht überein, aber das ist in Ordnung, wenn Sie sie als "neu" behandeln.
- **Integration**: Führen Sie dies als Pre-Build-Skript in Ihrem Jekyll-Workflow aus (z. B. über ein Bash-Skript oder einen Git-Hook). Keine Notwendigkeit für Jekyll-Plugins, wenn Sie übersetzte Markdown-Dateien separat generieren.

Dies ist Satzebene (weniger genauer Kontext für KI) oder Volltext (keine Einsparungen) vorzuziehen. YAML/JSON wäre für das Schreiben von Ideen in der Tat umständlich – bleiben Sie bei Markdown.

### Vorgeschlagener Best Way: Absatz-Hashing mit Caching und Markdown-bewusstem Parsing

Verwenden Sie ein Python-Skript für:
1. Parsen des englischen Markdowns in "übersetzbare Einheiten" (Absätze, ausgenommen Codeblöcke, Überschriften nach Wunsch usw.).
2. Hashen des englischen Textes jeder Einheit (normalisiert, z. B. extra Leerzeichen entfernen).
3. Überprüfen eines dateibasierten Caches auf vorhandene Übersetzungen nach Hash/Sprache.
4. Übersetzen fehlender Einheiten über Ihr KI-Tool (z. B. DeepSeek/Mistral API).
5. Cachen neuer Übersetzungen.
6. Wiederzusammensetzen der übersetzten Markdown-Dateien unter Beibehaltung der nicht übersetzbaren Teile.

**Warum dies der beste Weg ist**:
- **Einfach und mit geringem Overhead**: Keine DB, nur Dateien. Läuft lokal/offline, außer für KI-Aufrufe.
- **Flexibel**: Behandelt Codeblöcke durch Überspringen. Erweiterbar für andere Markdown-Elemente (z. B. Überschriften nicht übersetzen, wenn sie kurz sind).
- **Kosteneffektiv**: Bezahlt nur für neue/geänderte Absätze. Für einen 10-Absätze-Beitrag spart die Bearbeitung eines Absatzes ~90 % der Tokens.
- **Wartbar**: Bearbeiten Sie englischen Markdown natürlich; das Skript erledigt den Rest.
- **Benötigte Tools**: Python (haben Sie wahrscheinlich). Bibliotheken: `hashlib` (eingebaut für Hashing), `markdown` oder `mistune` für Parsing (falls nötig; beginnen Sie einfach mit Regex für Ihren "keine spezielle Syntax"-Fall).

#### Schritt-für-Schritt-Implementierung

1. **Setup**:
   - Erstellen Sie eine `translations_cache.json`-Datei (oder ein Verzeichnis wie `cache/` mit hash.json-Dateien für Skalierbarkeit).
   - Struktur: `{ "hash1": { "fr": "übersetzter Text", "es": "...", ... }, "hash2": { ... } }`
   - Speichern Sie dies in Ihrem Blog-Repo (git-ignore falls sensibel) oder einem separaten Verzeichnis.
   - Listen Sie Ihre 8 Sprachen im Skript auf (z. B. ['fr', 'es', 'de', ...]).

2. **Parsen von Markdown**:
   - Für einfache Fälle (Absätze + Codeblöcke): Verwenden Sie zeilenweise Verarbeitung, um eingefasste Codeblöcke (``````` oder `~~~`) und eingerückten Code (>3 Leerzeichen) zu erkennen.
   - Sammeln Sie "Absätze" als Blöcke aufeinanderfolgender Nicht-Code-, Nicht-Leerzeilen.
   - Besser: Verwenden Sie Python's `markdown`-Bibliothek zur Konvertierung in HTML, dann Text extrahieren, aber das ist für die Wiederzusammensetzung verlustbehaftet. Verwenden Sie stattdessen `mistune` (einen schnellen Markdown-Parser), um einen AST (Abstract Syntax Tree) zu erhalten, der Ihnen das Durchlaufen und Modifizieren übersetzbarer Knoten (z. B. 'paragraph'-Knoten) ermöglicht.
   - Installieren Sie `mistune` falls nötig (aber Ihre Umgebung hat die Grundlagen; gehen Sie davon aus, dass Sie es lokal pip-installieren können).

3. **Hashing**:
   - Normalisieren: `text.strip().lower()` oder nur `.strip()`, um Leerzeichenänderungen zu ignorieren, falls gewünscht (aber das könnte beabsichtigte Bearbeitungen übersehen).
   - Hash: `hashlib.sha256(normalized.encode()).hexdigest()`

4. **Übersetzung**:
   - Verwenden Sie Ihren KI-API-Wrapper (z. B. für DeepSeek: Prompt senden wie "Übersetzen Sie diesen Absatz ins Französische: {text}").
   - Batchweise wenn möglich, aber da Absätze klein sind, ist sequentiell in Ordnung.

5. **Wiederzusammensetzung**:
   - Bauen Sie den Markdown neu auf, indem Sie übersetzbare Blöcke durch gecachte/neue Übersetzungen ersetzen und Code/Überschriften intakt lassen.

6. **Skriptausführung**:
   - Ausführen: `python translate_blog.py pfad/zur/englisch.md`
   - Ausgaben: `pfad/zur/fr.md`, `pfad/zur/es.md`, etc.
   - Für Jekyll: Platzieren Sie diese in `_posts/` mit Sprachpräfixen oder verwenden Sie ein multilinguales Plugin wie `jekyll-polyglot` zur Handhabung.

#### Beispiel-Python-Skript

Hier ist eine Basisversion, die zeilenweises Parsing verwendet (keine externen Bibliotheken außer Built-Ins). Es setzt einfachen Markdown voraus: durch Leerzeilen getrennte Absätze, eingefasste Codeblöcke. Upgrade auf `mistune` für komplexe Syntax.

```python
import hashlib
import json
import os
import sys
# Nehmen Sie an, Sie haben eine KI-Übersetzungsfunktion; ersetzen Sie durch Ihren DeepSeek/Mistral API-Aufruf
def ai_translate(text, lang):
    # Platzhalter: Rückgabe des API-Aufrufergebnisses
    return f"Übersetzt nach {lang}: {text}"  # Ersetzen durch echte API

CACHE_FILE = 'translations_cache.json'
LANGUAGES = ['fr', 'es', 'de', 'it', 'pt', 'zh', 'ja', 'ko']  # Ihre 8 Sprachen

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=4)

def compute_hash(text):
    normalized = text.strip()  # Normalisierung anpassen
    return hashlib.sha256(normalized.encode('utf-8')).hexdigest()

def parse_markdown(md_text):
    lines = md_text.splitlines()
    blocks = []
    current_block = []
    in_code = False
    for line in lines:
        if line.strip().startswith('```') or line.strip().startswith('~~~'):
            in_code = not in_code
            if current_block:
                blocks.append(('text', '\n'.join(current_block)))
                current_block = []
            blocks.append(('code', line))
            continue
        if in_code:
            blocks.append(('code', line))
        else:
            if line.strip():  # Nicht leer
                current_block.append(line)
            else:
                if current_block:
                    blocks.append(('text', '\n'.join(current_block)))
                    current_block = []
    if current_block:
        blocks.append(('text', '\n'.join(current_block)))
    return blocks

def translate_post(english_md_path):
    with open(english_md_path, 'r') as f:
        md_text = f.read()
    
    blocks = parse_markdown(md_text)
    cache = load_cache()
    
    for lang in LANGUAGES:
        translated_blocks = []
        for block_type, content in blocks:
            if block_type == 'code':
                translated_blocks.append(content)
            else:  # text
                h = compute_hash(content)
                if h not in cache:
                    cache[h] = {}
                if lang not in cache[h]:
                    translation = ai_translate(content, lang)
                    cache[h][lang] = translation
                translated_blocks.append(cache[h][lang])
        
        # Mit Zeilenumbrüchen wieder zusammensetzen
        translated_md = '\n\n'.join(translated_blocks)  # Für Markdown-Formatierung anpassen
        output_path = english_md_path.replace('.md', f'_{lang}.md')
        with open(output_path, 'w') as f:
            f.write(translated_md)
    
    save_cache(cache)
    print("Übersetzungen aktualisiert.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Verwendung: python skript.py pfad/zur/englisch.md")
    else:
        translate_post(sys.argv[1])
```

**Anwendung**:
- Ersetzen Sie `ai_translate` durch Ihre API-Logik.
- Führen Sie es für Ihre Beitragsdatei nach Bearbeitungen aus.
- Für Überschriften/Listen: Erweitern Sie `parse_markdown`, um diese zu erkennen (z. B. Zeilen, die mit `#` oder `-` beginnen, als separate Blöcke).
- Falls Beiträge Bilder/Links haben: Sie bleiben unverändert, da sie in Textblöcken sind.
- Normalisierungstipp: Wenn Sie kleine Änderungen in der Zeichensetzung ignorieren möchten, verwenden Sie Regex, um diese vor dem Hashing zu entfernen.

#### Erweiterungen
- **Git-Integration**: Verwenden Sie `git diff`, um vorab geänderte Zeilen zu identifizieren, aber Hashing ist einfacher.
- **Batch-Übersetzung**: Falls die API es unterstützt, senden Sie mehrere neue Absätze gleichzeitig.
- **Fehlerbehandlung**: Wiederholen Sie fehlgeschlagene API-Aufrufe; validieren Sie Übersetzungen.
- **Erweitertes Parsing**: Pip `mistune` und verwenden Sie dessen Renderer zur Anpassung (z. B. 'code_block'-Knoten überspringen).
- **Tests**: Hash-Kollisionen sind mit SHA-256 selten; testen Sie mit Beispielbeiträgen.

Dies sollte Ihnen Tokens sparen, ohne Ihren Workflow zu komplizieren. Wenn Ihr Markdown komplexer ist, beginnen Sie damit und iterieren Sie. Lassen Sie mich wissen, wenn Sie Anpassungen oder Hilfe mit der API-Integration benötigen!