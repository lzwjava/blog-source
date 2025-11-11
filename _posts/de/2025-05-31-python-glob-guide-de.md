---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Python Glob-Modul Leitfaden zur Dateisuche
translated: true
type: note
---

### Glob importieren
Um glob in Python zu verwenden, importieren Sie das Modul aus der Standardbibliothek:
```python
import glob
```

### Grundlegende Funktionalität
Die `glob.glob()`-Funktion nimmt einen Muster-String und gibt eine Liste passender Datei- oder Verzeichnispfade zurück. Sie verwendet Unix-Shell-artige Wildcards:

- `*`: Passt auf beliebige Zeichenfolgen (außer Pfadtrennzeichen).
- `?`: Passt auf ein beliebiges einzelnes Zeichen.
- `[seq]`: Passt auf jedes Zeichen in seq (z.B. `[0-9]` für Ziffern).
- `**`: Durchsucht Verzeichnisse rekursiv (erfordert `recursive=True`).

Muster sind relativ zum aktuellen Verzeichnis, es sei denn, ein absoluter Pfad wird angegeben.

### Verwendungsbeispiele

#### 1. Alle .txt-Dateien im aktuellen Verzeichnis finden
```python
import glob

files = glob.glob("*.txt")
print(files)  # Ausgabe: ['file1.txt', 'file2.txt', ...]
```

#### 2. Dateien mit bestimmten Erweiterungen in einem Unterverzeichnis finden
```python
files = glob.glob("documents/*.pdf")
print(files)  # Ausgabe: ['documents/doc1.pdf', ...]
```

#### 3. Bestimmte Muster abgleichen (z.B. Dateien, die mit 'log' beginnen und mit Zahlen enden)
```python
files = glob.glob("log[0-9].txt")
print(files)  # Ausgabe: ['log1.txt', 'log2.txt', ...] falls solche Dateien existieren
```

#### 4. Rekursive Suche in Unterverzeichnissen
Verwenden Sie `**` mit `recursive=True`, um Verzeichnisse und Unterverzeichnisse zu durchsuchen:
```python
files = glob.glob("**/*.py", recursive=True)
print(files)  # Ausgabe: ['script1.py', 'subdir/script2.py', ...]
```

### Wichtige Hinweise
- Ergebnisse sind standardmäßig unsortiert; verwenden Sie `sorted()`, wenn Sie eine Ordnung benötigen: `sorted(glob.glob("*.txt"))`.
- Für case-insensitive Abgleiche auf case-sensitiven Dateisystemen sollten Sie eine Kombination mit `fnmatch` in Betracht ziehen oder dies im Code behandeln, da glob case-sensitiv ist.
- Glob folgt keinen symbolischen Links, es sei denn, dies wird explizit behandelt; verwenden Sie `os.walk()` für komplexere Durchläufe.
- Für einen Treffer auf einmal verwenden Sie `glob.iglob()`, das einen Iterator zurückgibt, um Speicher bei großen Ergebnismengen zu sparen: `for file in glob.iglob("*.txt"): print(file)`.

Dies deckt die Grundlagen ab; weitere Details finden Sie in der [Python-Dokumentation](https://docs.python.org/3/library/glob.html).