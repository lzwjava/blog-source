---
audio: false
generated: true
image: false
lang: es
layout: post
title: Mejores Prácticas para la Estructura de Directorios de Proyectos
translated: true
type: note
---

Buena pregunta.

La convención general es:

* **`scripts/`** es para tu código de aplicación (cosas que quieres ejecutar en producción o como parte de tu proyecto).
* **`tests/`** es para tu código de prueba (cosas que validan la corrección de tus scripts/módulos).

Por lo tanto, si estás agregando un nuevo archivo de prueba, normalmente debería ir en **`tests/llm/`**, no en `scripts/`.

Por ejemplo:

```
scripts/
  llm/
    main.py
    utils.py
tests/
  llm/
    test_main.py
    test_utils.py
```

De esta manera, tus pruebas están separadas de tu implementación, y herramientas como `pytest` pueden descubrirlas fácilmente.

👉 Ahora puedes agregar algo como:

```python
# tests/llm/test_basic.py
import pytest
from scripts.llm import utils

def test_addition():
    assert utils.add(2, 3) == 5
```

Luego ejecuta:

```bash
pytest tests/llm/
```

¿Te gustaría que también te muestre cómo configurar un `conftest.py` para que puedas compartir fixtures entre tus archivos `tests/llm/`?