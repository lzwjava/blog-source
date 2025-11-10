---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: CFFI Python C-Schnittstellenleitfaden
translated: true
type: note
---

### Was ist CFFI?
CFFI (C Foreign Function Interface) ist eine Python-Bibliothek zum Aufruf von C-Funktionen aus Python-Code. Sie ist kompatibel mit CPython und PyPy und bietet eine sicherere und portablere Alternative zu Bibliotheken wie ctypes. Sie unterstützt zwei Hauptmodi: ABI (Aufruf vorhandener Shared Libraries) und API (Kompilierung von C-Code inline).

### Installation
Installieren Sie CFFI mit pip:
```bash
pip install cffi
```
CFFI benötigt einen C-Compiler (z.B. GCC unter Linux, Visual Studio unter Windows), um Module zu bauen.

### Grundlegendes Anwendungsbeispiel
Hier ist eine schrittweise Anleitung für einen einfachen Anwendungsfall: Aufruf einer C-Funktion, die zwei Ganzzahlen addiert, im API-Modus (empfohlen für neuen Code).

1. **FFI importieren und einrichten**:
   ```python
   from cffi import FFI
   ffibuilder = FFI()
   ```

2. **C-Deklarationen definieren**:
   Geben Sie die C-Funktionssignaturen in einem String an:
   ```python
   ffibuilder.cdef("""
       int add(int a, int b);
   """)
   ```

3. **C-Quellcode bereitstellen**:
   Fügen Sie die C-Implementierung ein:
   ```python
   ffibuilder.set_source("_example",
       """
       int add(int a, int b) {
           return a + b;
       }
       """)
   ```

4. **Das Modul kompilieren**:
   Führen Sie dieses Skript einmal aus, um die C-Erweiterung zu bauen:
   ```python
   if __name__ == "__main__":
       ffibuilder.compile(verbose=True)
   ```
   Dies erzeugt ein kompiliertes Modul (z.B. `_example.cpython-39-x86_64-linux-gnu.so`).

5. **Das kompilierte Modul verwenden**:
   Importieren und rufen Sie die Funktion in Ihrem Python-Code auf:
   ```python
   from _example import lib
   result = lib.add(5, 3)
   print(result)  # Ausgabe: 8
   ```

### Wichtige Konzepte
- **FFI-Objekt**: Die Hauptschnittstelle, erstellt mit `FFI()`. Verwenden Sie `cdef()` für Deklarationen und `set_source()` für Code.
- **Deklarationen**: Informieren Python über C-Typen, Structs, Funktionen usw. Die Strings müssen exakt der C-Syntax entsprechen.
- **Typkonvertierung**: CFFI handhabt grundlegende Typen (int, float, Zeiger) automatisch. Verwenden Sie Arrays, Structs oder Callbacks für komplexere Fälle.
- **Fehlerbehandlung**: Bei ungültigen C-Definitionen treten Exceptions wie `CDefError` auf. C-Laufzeitfehler (z.B. über `errno`) können mit `ffi.errno` überprüft werden.
- **Speicherverwaltung**: Verwenden Sie `ffi.new()` für C-Structs/Arrays und stellen Sie eine ordnungsgemäße Freigabe sicher, um Leaks zu vermeiden.

### Modi: ABI vs. API
- **ABI-Modus** (für vorhandene Bibliotheken): Laden Sie eine Shared Library (z.B. `ffi.dlopen("mylib.so")`) und rufen Sie Funktionen direkt auf. Beispiel:
  ```python
  from cffi import FFI
  ffi = FFI()
  ffi.cdef("int add(int a, int b);")
  lib = ffi.dlopen("/path/to/libmylib.so")
  result = lib.add(5, 3)
  ```
  Dies ist schneller für vorgebaute Bibliotheken, aber weniger portabel – Sie benötigen das exakte Binärfile.

- **API-Modus** (empfohlen): Kompilieren Sie C-Code inline, wie im obigen Beispiel. Dies ist sicherer, optimiert besser und funktiert plattformübergreifend.

### Erweiterte Funktionen
- **Structs und Unions**: Definieren Sie komplexe Typen, z.B. `cdef("struct Point { int x, y; }")`.
- **Arrays und Zeiger**: Verwenden Sie `ffi.new("int[10]")` für Arrays oder `ffi.cast("int*", ptr)` für Casts.
- **Callbacks**: Übergeben Sie Python-Funktionen an C mit `ffi.callback()`.
- **Integration mit Paketen**: Viele Bibliotheken (z.B. cryptography, NumPy) verwenden CFFI für Performance.
- **Performance-Tipps**: Die Kompilierung dauert eine Weile; verwenden Sie Inplace-Builds oder CFFI-Pakete für die Distribution. Vermeiden Sie häufige Python-C-Übergänge in Schleifen.

Die vollständige Dokumentation finden Sie in den [offiziellen CFFI-Docs](https://cffi.readthedocs.io/). Dies deckt die Grundlagen ab – experimentieren Sie mit den Beispielen, um sie an Ihre Bedürfnisse anzupassen. Wenn Sie einen spezifischen Anwendungsfall haben, geben Sie mehr Details für eine maßgeschneiderte Beratung an.