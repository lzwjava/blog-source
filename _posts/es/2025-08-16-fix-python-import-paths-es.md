---
audio: false
generated: true
image: false
lang: es
layout: post
title: Corregir Rutas de Importación de Módulos de Python
translated: true
type: note
---

La respuesta corta: necesitas `sys` aquí para poder modificar la ruta de búsqueda de módulos de Python (`sys.path`) antes de hacer el `from scripts.create.delete import delete_md`.

---

### Por qué se necesita `sys`

* Python busca módulos/paquetes para importar en una lista de directorios almacenada en `sys.path`.
* Por defecto, contiene:

  * El directorio del script actual.
  * Directorios de la librería estándar.
* Los `site-packages` instalados.
* Si tu archivo `scripts/create/delete.py` no está en uno de esos lugares por defecto, la importación fallará con `ModuleNotFoundError`.

Así que el código hace:

```python
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
```

Eso significa:

* Tomar la ruta absoluta del archivo actual (`__file__`).
* Subir tres directorios.
* Añadir ese directorio a `sys.path`.

Después de eso, Python puede resolver `scripts.create.delete` como si estuviera instalado o en la raíz del proyecto.

---

### Sin `sys`

Si tu proyecto está organizado así:

```
project/
├── scripts/
│   └── create/
│       └── delete.py
└── tools/
    └── myscript.py   <-- estás ejecutando este
```

y ejecutas `myscript.py` directamente, Python no sabrá automáticamente que `project/` es la raíz. La importación fallará a menos que:

* Lo ejecutes con `PYTHONPATH=...` (ej., `PYTHONPATH=.. python myscript.py`), o
* Empaquetes el proyecto y lo instales (`pip install -e .`), o
* Añadas la ruta dinámicamente en el código con `sys.path.append(...)` (como se hace aquí).

---

👉 Así que `sys` es necesario puramente para **manipular la ruta de importación en tiempo de ejecución**, permitiéndote importar módulos relativos a la raíz de tu proyecto.

¿Quieres que también te muestre **alternativas más limpias** para evitar modificar `sys.path` manualmente?