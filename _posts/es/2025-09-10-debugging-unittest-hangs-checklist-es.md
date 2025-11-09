---
audio: false
date: 2025-09-10
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Lista de Verificación para Depurar Bloqueos en Unittest
translated: true
type: note
---

Los bloqueos en `unittest` suelen deberse a interbloqueos (hilos/async), E/S bloqueadas, problemas con subprocesos/multiprocesamiento, o una prueba que espera una llamada de red. Aquí tienes una lista concisa para *ver dónde se bloquea* y *desbloquearla*—funciona en Python 3.9–3.11.

### 1) Ejecutar unittest en modo verbose (y correctamente)

```bash
# Si xx.py llama a unittest.main()
python xx.py -v

# O usar discovery (recomendado)
python -m unittest -v
python -m unittest discover -v -s tests -p "test_*.py"
```

> Nota: `python -v` es **verbose de importación del intérprete**, no verbose de pruebas. Usa `-m unittest -v` para ver nombres de pruebas y progreso.

### 2) Activar faulthandler + modo dev (volcados de pila en bloqueos, advertencias más estrictas)

```bash
# Una vez
python -X faulthandler -X dev -u -m unittest -v
# O vía entorno
export PYTHONFAULTHANDLER=1
python -X dev -u -m unittest -v
```

* `-X faulthandler` permite a Python imprimir trazas de pila de hilos ante señales fatales/timeouts.
* `-X dev` hace que las advertencias/errores sean más notorios.
* `-u` libera stdout/stderr para que *veas* las impresiones en tiempo real.

### 3) Forzar un traceback cuando parezca bloqueado

Opción A — desde otra terminal (Linux/macOS):

```bash
kill -SIGUSR1 <pid>  # con faulthandler activado, vuelca todas las pilas de hilos
```

Opción B — añadir al inicio de tu script de prueba (al principio de `xx.py`):

```python
import faulthandler, signal, sys
faulthandler.enable()
# Volcar pilas con SIGUSR1:
faulthandler.register(signal.SIGUSR1, all_threads=True)
# También volcar automáticamente si se bloquea > 120s:
faulthandler.dump_traceback_later(120, repeat=True)
```

### 4) Trazar la ejecución paso a paso (pesado pero decisivo)

```bash
python -m trace --trace xx.py
# o
python -m trace --trace -m unittest discover -v
```

Verás cada línea ejecutada; detente cuando la salida se "congele"—ese es el punto del bloqueo.

### 5) Usar el depurador inmediatamente

```bash
python -m pdb xx.py         # si xx.py llama a unittest.main()
# Punto de interrupción en una línea sospechosa:
# (Pdb) b mymodule.py:123
# (Pdb) c
```

Para ejecuciones con discovery, añade `import pdb; pdb.set_trace()` en el punto sospechoso.

### 6) Causas comunes y soluciones rápidas

* **Multiprocesamiento en macOS/Windows**: siempre proteger el punto de entrada de la prueba.

  ```python
  if __name__ == "__main__":
      import unittest
      unittest.main()
  ```

  Si generas procesos en pruebas en macOS:

  ```python
  import multiprocessing as mp
  if __name__ == "__main__":
      mp.set_start_method("fork")  # a veces evita bloqueos vs el valor por defecto "spawn"
  ```

  (Haz esto solo si sabes que tu código es seguro para fork.)

* **Interbloqueos de hilos**: comprueba `join()` sin timeouts, locks no liberados, o hilos en segundo plano esperando al hilo principal. Reemplaza:

  ```python
  t.join()
  ```

  con:

  ```python
  t.join(timeout=5); assert not t.is_alive()
  ```

* **Pruebas Async**: asegúrate de usar `IsolatedAsyncioTestCase` (3.8+) o `asyncio.run()`. Bucles de eventos duplicados o `await` olvidados suelen causar bloqueos.

* **Llamadas de red**: añade **timeouts cortos** en todas partes:

  ```python
  requests.get(url, timeout=5)
  ```

* **Esperas a stdin**: elimina `input()` o protégela en las pruebas; CI/stdin puede bloquearse para siempre.

* **Mocking que sale mal**: un método simulado que nunca resuelve un `Future`/promesa o un servidor stub no iniciado.

### 7) Visibilidad extra

* Ver asignaciones si se sospecha de fuga/giro:

  ```bash
  python -X tracemalloc=25 -m unittest -v
  ```
* Mostrar ruido de importación (rara vez necesario para bloqueos):

  ```bash
  python -v -m unittest -v
  ```

### 8) Si solo se bloquea en una versión de Python

* Prueba ambas:

  ```bash
  pyenv local 3.11.9
  python -X faulthandler -X dev -m unittest -v

  pyenv local 3.9.19
  python -X faulthandler -X dev -m unittest -v
  ```

  Las diferencias suelen aparecer en torno al comportamiento de `multiprocessing`, `asyncio` o las extensiones C.

---

Si pegas el traceback de `faulthandler` (o las últimas líneas de `trace --trace`), señalaré el culpable exacto y sugeriré una solución específica.