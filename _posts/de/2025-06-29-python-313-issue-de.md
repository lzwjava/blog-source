---
audio: false
generated: true
lang: de
layout: post
title: CuPy-Fehler mit Python 3.13
translated: true
type: note
---

### Problembeschreibung

Beim Ausführen eines Python-Skripts, das die CuPy-Bibliothek für GPU-Berechnungen importiert, tritt ein `AttributeError` auf. Der Fehler tritt während der Anweisung `import cupy as cp` auf und verhindert die Ausführung des Skripts. Der Traceback verweist auf ein Problem im internen Code von CuPy, speziell in `cupy/cuda/device.pyx` in Zeile 105, wo ein `memoize`-Dekorator versucht, das `__name__`-Attribut einer Built-in-Funktion oder -Methode zu modifizieren. Die Fehlermeldung lautet:

```
AttributeError: attribute '__name__' of 'builtin_function_or_method' objects is not writable
```

Dieses Problem scheint mit Ihrer Verwendung von Python 3.13 zusammenzuhängen, das Kompatibilitätsprobleme mit der von Ihnen installierten CuPy-Version verursachen kann.

### Ursache des Fehlers

Der Fehler tritt aus folgenden Gründen auf:

- **CuPys `memoize`-Dekorator**: CuPy verwendet einen `memoize`-Dekorator, um Funktionsergebnisse zur Leistungsoptimierung zwischenzuspeichern. Dieser Dekorator verlässt sich auf `functools.update_wrapper` von Python, um Attribute (wie `__name__`) von der ursprünglichen Funktion auf die Wrapper-Funktion zu kopieren.
- **Built-in-Funktionen**: In Python haben Built-in-Funktionen (in C implementiert) ein schreibgeschütztes `__name__`-Attribut. Wenn `update_wrapper` versucht, dieses Attribut zu setzen, schlägt es mit einem `AttributeError` fehl.
- **Python 3.13-Kompatibilität**: Die spezifische Funktion, die in CuPys `device.pyx` gememoized wird, ist wahrscheinlich eine Built-in-Funktion. Python 3.13 könnte strengere Regeln durchsetzen oder Built-ins anders behandeln als vorherige Versionen, was dieses Problem aufdeckt.

Da der Fehler während des Imports von CuPy auftritt, handelt es sich um ein systemisches Problem, das mit der Initialisierung der Bibliothek zusammenhängt, und nicht mit der Logik Ihres Skripts.

### Empfohlene Lösung

Die einfachste und praktischste Lösung ist, Ihr Skript mit einer früheren Version von Python auszuführen, in der CuPy als kompatibel bekannt ist, wie z. B. Python 3.11 oder 3.12. Dies vermeidet das Kompatibilitätsproblem mit Python 3.13, ohne dass Änderungen am Quellcode von CuPy oder komplexe Workarounds erforderlich sind.

#### Warum das funktioniert

- **Kompatibilität**: CuPy-Versionen bis zu den neuesten Releases (z. B. v11) werden auf Python-Versionen wie 3.11 und 3.12 getestet und unterstützt, bei denen dieser spezifische Fehler nicht auftritt.
- **Keine Codeänderungen**: Ihr Skript, das GPU-Sorting mit CuPy benchmarked, kann unverändert in einer früheren Python-Umgebung ausgeführt werden, was die Integrität des Benchmarks gewährleistet.
- **Einfache Implementierung**: Das Wechseln der Python-Version ist unkompliziert, indem virtuelle Umgebungen oder Tools wie `conda` verwendet werden.

### Schritt-für-Schritt-Lösung

So beheben Sie das Problem:

#### Option 1: Verwendung von `virtualenv`

1. **Python 3.11 oder 3.12 installieren**
   - Stellen Sie sicher, dass Python 3.11 oder 3.12 auf Ihrem System installiert ist (z. B. über Ihren Paketmanager oder die offizielle Python-Website).

2. **Eine virtuelle Umgebung erstellen**
   ```bash
   virtualenv -p python3.11 venv
   ```
   Dies erstellt eine virtuelle Umgebung namens `venv` unter Verwendung von Python 3.11. Ersetzen Sie `python3.11` durch `python3.12`, wenn gewünscht.

3. **Die virtuelle Umgebung aktivieren**
   ```bash
   source venv/bin/activate
   ```

4. **CuPy installieren**
   ```bash
   pip install cupy
   ```
   Dies installiert die neueste kompatible Version von CuPy für Python 3.11.

5. **Ihr Skript ausführen**
   ```bash
   python scripts/benchmark/cudamark.py
   ```
   Ihr Skript sollte nun ohne den `AttributeError` ausgeführt werden.

6. **Deaktivieren (wenn fertig)**
   ```bash
   deactivate
   ```

#### Option 2: Verwendung von `conda`

1. **Conda-Umgebung erstellen**
   ```bash
   conda create -n cudabench python=3.11
   ```
   Dies erstellt eine Umgebung namens `cudabench` mit Python 3.11. Verwenden Sie `python=3.12`, wenn Sie Python 3.12 bevorzugen.

2. **Die Umgebung aktivieren**
   ```bash
   conda activate cudabench
   ```

3. **CuPy installieren**
   ```bash
   pip install cupy
   ```

4. **Ihr Skript ausführen**
   ```bash
   python scripts/benchmark/cudamark.py
   ```

5. **Deaktivieren (wenn fertig)**
   ```bash
   conda deactivate
   ```

### Überprüfung der Lösung

Nach dem Einrichten der Umgebung und dem Ausführen des Skripts sollten Sie eine Ausgabe ähnlich der folgenden sehen:

```
CPU cores: <Ihre_CPU-Kerne>
Threads: 1, Time taken: X.XXXX seconds
Threads: 2, Time taken: X.XXXX seconds
...
ThreadCount,TimeTakenSeconds
1,X.XXXXXX
2,X.XXXXXX
...
```

Wenn das Skript ohne den `AttributeError` läuft, war die Lösung erfolgreich.

### Zusätzliche Hinweise

- **Thread-Anzahlen in Ihrem Skript**: Ihr Skript iteriert über Thread-Anzahlen (`1, 2, 4, 8, 16, 32, 64, 128`), aber die Funktion `parallel_sort_gpu` verwendet das GPU-basierte Sortieren von CuPy (`cp.sort`), das keine CPU-Threads direkt nutzt. Die Thread-Anzahl-Schleife beeinflusst die GPU-Sortierleistung möglicherweise nicht wie erwartet. Falls dies für zukünftige Modifikationen beabsichtigt ist (z. B. das Hinzufügen von CPU-Threading), ist das in Ordnung; andernfalls könnten Sie den Benchmark vereinfachen, um sich ausschließlich auf die GPU-Leistung zu konzentrieren.
- **CuPy-Version**: Wenn Sie eine veraltete CuPy-Version vermuten, stellen Sie sicher, dass Sie die neueste Version installieren, indem Sie `pip install cupy --upgrade` ausführen. Das Hauptproblem hier ist jedoch die Python 3.13-Kompatibilität, nicht allein die CuPy-Version.
- **Langfristige Lösung**: Wenn Sie Python 3.13 verwenden müssen, können Sie CuPys GitHub-Repository oder Issue-Tracker auf Updates überprüfen, die Python 3.13 unterstützen (Stand Juni 2025 könnte dies verfügbar sein). Alternativ könnten Sie CuPy forken und den `memoize`-Dekorator patchen, um Built-in-Funktionen zu behandeln, aber dies ist komplexer und für einen Benchmark unnötig.

Durch die Verwendung von Python 3.11 oder 3.12 können Sie Ihren GPU-Benchmark zuverlässig ausführen, ohne auf diesen Fehler zu stoßen.