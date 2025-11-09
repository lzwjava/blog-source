---
audio: false
date: 2025-09-10
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Resolución del Búfer de Salida de Python en Pruebas Unitarias
translated: true
type: note
---

Sí — ese retraso casi siempre es **output buffering**, y Git-Bash/mintty en Windows puede hacerlo más notable. No necesitas una cola a menos que estés haciendo logging multi-proceso; primero haz que stdout/stderr no tengan buffer y evita el buffering propio de unittest.

### Haz esto cuando ejecutes

```bash
# PowerShell / CMD:
py -3.11 -u -m unittest -v

# Git-Bash:
PYTHONUNBUFFERED=1 py -3.11 -u -m unittest -v
# o
PYTHONUNBUFFERED=1 python -u -m unittest -v
```

* `-u` = stdio sin buffer
* `PYTHONUNBUFFERED=1` = lo mismo, también afecta a los procesos hijos

Si usas `xx.py` directamente:

```bash
python -u xx.py -v
```

### Hazlo inmediato dentro de tu código (drop-in)

Pon esto al principio de tu bootstrap de tests (o bloque `if __name__ == "__main__":`):

```python
import os, sys
os.environ.setdefault("PYTHONUNBUFFERED", "1")

# Python 3.7+
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True, write_through=True)
    sys.stderr.reconfigure(line_buffering=True, write_through=True)

print("booting tests...", flush=True)
```

Y cada vez que hagas `print(...)`, añade `flush=True` para los puntos críticos.

### Si usas el módulo `logging`

```python
import logging, sys
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
    force=True,  # 3.8+
)
# StreamHandler hace flush de cada registro; esto asegura que apunte a stdout
```

### Cuidado con el buffering de unittest

Si tú (o un framework) lo habilitaste, la salida se retiene hasta el final del test:

* **Evita**: `unittest.main(buffer=True)` o `python -m unittest -b`
* Usa el valor por defecto (sin `-b`) para que los logs se impriman según ocurren.

### Consejos específicos para Git-Bash

* Mintty a veces hace que los programas piensen que stdout no es una TTY → más buffering. Tus dos mejores soluciones son la combinación **`-u`/`PYTHONUNBUFFERED`** mencionada arriba o simplemente ejecutar desde **Windows Terminal/PowerShell/CMD** para comparar.
* Si generas subprocesos, ellos también harán buffering a menos que hereden el entorno. Con `PYTHONUNBUFFERED=1` exportado, los procesos hijos de Python se comportarán correctamente.

### Cuándo una cola *sí* vale la pena

Solo si estás haciendo logging con **multiprocessing**: usa `logging.handlers.QueueHandler/QueueListener` para enviar los logs desde los workers al proceso principal; de lo contrario, los buffers de los hijos o la intercalación pueden causar problemas.

Si pegas un pequeño fragmento de cómo ejecutas las pruebas (comando + cualquier argumento de `unittest.main(...)`) y cómo haces logging/print, adaptaré el cambio mínimo para que toda la salida sea instantánea.