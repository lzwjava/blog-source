---
audio: false
generated: true
lang: de
layout: post
title: Warum Python `__init__.py` benötigt
translated: true
type: note
---

### Korrektur des Tippfehlers
Es sieht so aus, als ob du `__init__.py` (mit "init" als Abkürzung für "initialization" - Initialisierung) gemeint hast und nicht `__int__.py`. Falls das nicht der Fall ist, kläre es bitte auf! Gehen wir davon aus, dass es `__init__.py` ist, hier die Erklärung.

### Warum Python `__init__.py` in einem Verzeichnis benötigt
In Python wird ein Verzeichnis nicht automatisch als Modul oder Paket behandelt, nur weil es Python-Dateien enthält. Um Code in wiederverwendbare Pakete zu organisieren (was im Wesentlichen Verzeichnisse mit verwandten Modulen sind), benötigt Python eine `__init__.py`-Datei in diesem Verzeichnis. Hier ist der Grund:

- **Kennzeichnung des Verzeichnisses als Paket**: Das Vorhandensein von `__init__.py` teilt Python mit, dass das Verzeichnis als Paket betrachtet werden soll. Dies ermöglicht es dir, Module daraus mit Punktnotation zu importieren, wie z.B. `import mypackage.mymodule`. Ohne diese Datei (in Standardfällen) würde Python das Verzeichnis als einen normalen Ordner behandeln und keine Imports daraus erlauben.

- **Vermeidung von Namenskonflikten**: Es verhindert das versehentliche Überschatten von Modulen. Wenn du beispielsweise ein Verzeichnis namens `string` hast (ein gebräuchlicher Name), könnte es ohne `__init__.py` unbeabsichtigt Pythons eingebautes `string`-Modul im Import-Pfad verbergen.

- **Initialisierung und Anpassung**: Die Datei kann leer sein (was bei einfachen Paketen üblich ist), aber sie kann auch Code enthalten, der ausgeführt wird, wenn das Paket importiert wird. Dies ist nützlich für Setup-Aufgaben, wie das automatische Importieren von Submodulen. Zusätzlich kannst du eine spezielle Variable namens `__all__` in `__init__.py` definieren, um zu steuern, was importiert wird, wenn jemand `from mypackage import *` verwendet (z.B. `__all__ = ['module1', 'module2']`).

### Historischer und versionsspezifischer Kontext
- Diese Anforderung besteht seit den frühen Tagen von Python, um das Modulsystem explizit und organisiert zu halten.
- Ab Python 3.3 wurden "Namespace-Pakete" eingeführt, die keine `__init__.py` benötigen. Diese erlauben es, Pakete über mehrere Verzeichnisse verteilt zu haben (z.B. für Distributionszwecke) ohne diese Datei, unter Verwendung von Tools wie `pkgutil` oder `importlib`. Dies wird jedoch als fortgeschrittenes Feature betrachtet, und für die meisten alltäglichen Anwendungsfälle ist `__init__.py` für reguläre Pakete nach wie vor empfohlen und weit verbreitet.

Wenn du mit Python 3.3+ arbeitest, kannst du mit Namespace-Paketen experimentieren, aber für Anfänger ist es einfacher und unkomplizierter, bei `__init__.py` zu bleiben.

[Python Tutorial: Modules](https://docs.python.org/3/tutorial/modules.html#packages)