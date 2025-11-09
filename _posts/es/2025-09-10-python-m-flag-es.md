---
audio: false
date: 2025-09-10
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Uso del Indicador -m de Python para Módulos
translated: true
type: note
---

Sí, `-m` significa **ejecutar un módulo como un script**. Desglosemos esto con tus ejemplos:

### `python -m unittest`

Esto le indica a Python:

* Buscar el módulo `unittest` (que es parte de la librería estándar).
* Ejecutarlo como si fuera un script (eso es lo que hace `-m`).
* Es por eso que puedes hacer cosas como:

  ```bash
  python -m unittest test_example.py
  python -m unittest discover
  ```

  Esto funciona aunque no tengas un archivo `unittest` independiente en tu proyecto; es un módulo de la librería estándar.

### `python -m pip`

Este es el mismo patrón:

* Busca el módulo `pip` (instalado con Python).
* Lo ejecuta como si fuera el ejecutable `pip`.
* Así que `python -m pip install requests` es la forma "oficial" y segura de ejecutar pip, porque asegura que estás usando el pip del mismo intérprete de Python que coincide con tu comando `python`.
  (A veces, el comando `pip` en tu sistema podría estar apuntando a una instalación diferente de Python, por lo que `python -m pip` evita confusiones).

### Diferencia con `python test_xx.py`

Cuando haces:

```bash
python test_xx.py
```

estás ejecutando ese archivo específico directamente, sin usar el descubridor de pruebas (`discovery`) o el ejecutor de `unittest`.

* Si `test_xx.py` tiene un `unittest.main()` al final, ejecutará las pruebas.
* Pero si quieres que Python descubra automáticamente todas las pruebas en un directorio, usualmente dependes de `python -m unittest discover`.

---

✅ **Resumen**:

* `-m` = ejecutar un módulo como un script.
* `python -m unittest` ejecuta el ejecutor de pruebas de la librería estándar.
* `python -m pip` asegura que pip corresponda al mismo intérprete de Python.
* `python test_xx.py` solo ejecuta un archivo, no el ejecutor de pruebas general.

¿Te gustaría que también te muestre cómo **pytest** maneja esto de manera diferente, ya que podrías comparar `unittest` vs `pytest`?