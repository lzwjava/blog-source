---
audio: false
date: 2025-09-10
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Checkliste für das Debuggen von Unittest-Hänger
translated: true
type: note
---

Hängenbleiben in `unittest` kommt meist von Deadlocks (Threads/Async), festhängenden I/O-Operationen, Problemen mit Subprocess/Multiprocessing oder Tests, die auf einen Netzwerkaufruf warten. Hier ist eine kompakte Checkliste, um *zu sehen, wo es hängt* und *es zu lösen* – funktioniert mit Python 3.9–3.11.

### 1) Unittest ausführlich ausführen (und korrekt)

```bash
# Wenn xx.py unittest.main() aufruft
python xx.py -v

# Oder Discovery verwenden (empfohlen)
python -m unittest -v
python -m unittest discover -v -s tests -p "test_*.py"
```

> Hinweis: `python -v` ist **Interpreter-Import-Ausführlichkeit**, nicht Test-Ausführlichkeit. Verwende `-m unittest -v` für Testnamen und Fortschritt.

### 2) Faulthandler + Dev-Mode aktivieren (Stack-Dumps bei Hängen, strengere Warnungen)

```bash
# Einmalig
python -X faulthandler -X dev -u -m unittest -v
# Oder per Environment-Variable
export PYTHONFAULTHANDLER=1
python -X dev -u -m unittest -v
```

* `-X faulthandler` lässt Python Thread-Stack-Traces bei fatalen Signalen/Timeouts ausgeben.
* `-X dev` macht Warnungen/Fehler lauter.
* `-u` puffert stdout/stderr nicht, sodass man Ausgaben *in Echtzeit sieht*.

### 3) Erzwinge einen Traceback, wenn es hängenzubleiben scheint

Option A — von einem anderen Terminal (Linux/macOS):

```bash
kill -SIGUSR1 <pid>  # mit aktiviertem faulthandler werden alle Thread-Stacks gedumpt
```

Option B — zu deinem Test-Bootstrap hinzufügen (oben in `xx.py`):

```python
import faulthandler, signal, sys
faulthandler.enable()
# Dump Stacks bei SIGUSR1:
faulthandler.register(signal.SIGUSR1, all_threads=True)
# Auch automatischen Dump, wenn es > 120s hängt:
faulthandler.dump_traceback_later(120, repeat=True)
```

### 4) Schritt-für-Schritt-Ausführung verfolgen (aufwändig, aber entscheidend)

```bash
python -m trace --trace xx.py
# oder
python -m trace --trace -m unittest discover -v
```

Man sieht jede ausgeführte Zeile; stoppe, wenn die Ausgabe "einfriert" – das ist die Hängestelle.

### 5) Sofort den Debugger verwenden

```bash
python -m pdb xx.py         # wenn xx.py unittest.main() aufruft
# Breakpoint auf einer verdächtigen Zeile:
# (Pdb) b mymodule.py:123
# (Pdb) c
```

Für Discovery-Runs, füge `import pdb; pdb.set_trace()` an der verdächtigen Stelle ein.

### 6) Häufige Ursachen & schnelle Lösungen

* **Multiprocessing unter macOS/Windows**: immer Test-Einstieg absichern.

  ```python
  if __name__ == "__main__":
      import unittest
      unittest.main()
  ```

  Wenn du Prozesse in Tests unter macOS spawnst:

  ```python
  import multiprocessing as mp
  if __name__ == "__main__":
      mp.set_start_method("fork")  # vermeidet manchmal Hängen vs. Default "spawn"
  ```

  (Nur tun, wenn du weißt, dass dein Code fork-sicher ist.)

* **Thread-Deadlocks**: prüfe auf `join()` ohne Timeouts, nicht freigegebene Locks oder Hintergrund-Threads, die auf den Main-Thread warten. Ersetze:

  ```python
  t.join()
  ```

  mit:

  ```python
  t.join(timeout=5); assert not t.is_alive()
  ```

* **Async-Tests**: stelle sicher, dass `IsolatedAsyncioTestCase` (3.8+) oder `asyncio.run()` verwendet wird. Doppelte Event-Loops oder vergessenes `await` führen oft zu Hängen.

* **Netzwerkaufrufe**: füge **kurze Timeouts** überall hinzu:

  ```python
  requests.get(url, timeout=5)
  ```

* **stdin-Wartezeiten**: entferne `input()` oder sichere es in Tests; CI/stdin kann ewig blockieren.

* **Fehlgeschlagenes Mocking**: eine gemockte Methode, die nie ein `Future`/Promise auflöst, oder ein gestubbter Server, der nicht gestartet wurde.

### 7) Zusätzliche Sichtbarkeit

* Allokationen anzeigen, wenn Leck/Spin vermutet wird:

  ```bash
  python -X tracemalloc=25 -m unittest -v
  ```
* Import-Lärm anzeigen (selten für Hängen benötigt):

  ```bash
  python -v -m unittest -v
  ```

### 8) Wenn es nur bei einer Python-Version hängt

* Beide ausprobieren:

  ```bash
  pyenv local 3.11.9
  python -X faulthandler -X dev -m unittest -v

  pyenv local 3.9.19
  python -X faulthandler -X dev -m unittest -v
  ```

  Unterschiede zeigen sich meist bei `multiprocessing`, `asyncio` oder C-Extension-Verhalten.

---

Wenn du den Traceback von `faulthandler` (oder die letzten Zeilen von `trace --trace`) einfügst, zeige ich auf den genauen Verursacher und schlage eine gezielte Lösung vor.