---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía Esencial de Cobertura en Python
translated: true
type: note
---

Aquí tienes una introducción práctica y centrada en el desarrollo al paquete **coverage** (coverage.py): qué mide, cómo usarlo bien y los controles que realmente te importarán.

# Qué es coverage.py

* Una herramienta de Python que **mide qué líneas y ramas de tu código se ejecutan** durante las pruebas o cualquier ejecución.
* Genera informes en **texto, HTML, XML y JSON** para que puedas ver los huecos e integrarlo en las compuertas de calidad de CI.
* Funciona con unittest, pytest, nose o scripts simples.

# Conceptos básicos (en términos sencillos)

* **Cobertura de líneas**: ¿Se ejecutó una línea al menos una vez?
* **Cobertura de ramas**: ¿Se ejecutó cada rama posible de una decisión? (if/else, cortocircuito booleano, excepciones, comprensiones, etc.)
* **Selección de fuente**: Mide solo tu propio código para evitar ruido de venv/site-packages.
* **Almacenamiento de datos**: Las ejecuciones crean un archivo de datos `.coverage` (SQLite); puedes fusionar muchas ejecuciones.
* **Contextos**: Etiqueta la ejecución con etiquetas (por ejemplo, por prueba), para que puedas segmentar los informes por nombres de prueba, comandos, etc.

# Inicio rápido

```bash
# 1) Instalar
pip install coverage

# 2) Ejecuta tus pruebas bajo cobertura (pytest es solo un ejemplo)
coverage run -m pytest

# 3) Ve un informe en terminal (con números de líneas faltantes)
coverage report -m

# 4) Genera HTML (abre htmlcov/index.html en un navegador)
coverage html

# Opcional: informes legibles por máquina
coverage xml        # para herramientas CI como Sonar, Jenkins, Azure DevOps
coverage json       # análisis automatizado
```

# .coveragerc recomendado

Crea una configuración en la raíz de tu repositorio para que los resultados sean consistentes localmente y en CI.

```ini
[run]
# Mide solo tus paquetes para reducir el ruido
source = src, your_package
branch = True
parallel = True                 # permite que múltiples procesos/ejecuciones escriban sus propios datos
relative_files = True           # rutas más limpias en los informes (compatible con CI)
concurrency = thread, multiprocessing

# También puedes excluir archivos o patrones por completo
omit =
    */tests/*
    */.venv/*
    */site-packages/*
    */migrations/*

[report]
show_missing = True
skip_covered = False            # establece True si quieres un informe más corto
fail_under = 90                 # hace que CI falle si la cobertura está por debajo del 90%
exclude_lines =
    pragma: no cover            # pragma estándar para ignorar líneas
    if TYPE_CHECKING:
    raise NotImplementedError

[html]
directory = htmlcov
title = Coverage Report

[xml]
output = coverage.xml

[json]
output = coverage.json

[paths]
# Útil al combinar datos de diferentes máquinas/contenedores
source =
    src
    */workspace/src
    */checkouts/your_repo/src
```

# Medición de subprocesos y ejecuciones paralelas

Si tu código genera subprocesos (multiprocessing, herramientas CLI), configura la **cobertura de subprocesos**:

1. En `[run]`, mantén `parallel = True`.
2. Exporta una variable de entorno para que los subprocesos inicien automáticamente la cobertura con la misma configuración:

```bash
export COVERAGE_PROCESS_START=$(pwd)/.coveragerc
```

3. Ejecuta tu programa/pruebas normalmente (o aún a través de `coverage run -m ...`).
4. Después de que todas las ejecuciones terminen, fusiona los datos e informa:

```bash
coverage combine
coverage report -m
```

> Consejo: `concurrency = multiprocessing, thread, gevent, eventlet, greenlet` permite que coverage se enganche a diferentes modelos asíncronos.

# Cobertura de ramas y pragmas

* Habilita `branch = True` en `[run]`. Esto detecta ramas `else` omitidas, cortocircuitos, rutas de excepción, etc.
* Ignora líneas no probables con un comentario al final:

  * `# pragma: no cover` — excluye esa línea de la cobertura.
  * Para ramas complicadas, refactoriza en lugar de abusar de los pragmas.

# Contextos (segmentar la cobertura por prueba o tarea)

Los contextos adjuntan etiquetas a las líneas ejecutadas para que puedas responder: "¿Qué pruebas cubren este código?"

* Más fácil con pytest:

  * En `.coveragerc` agrega `dynamic_context = test_function`.
  * Luego `coverage html --show-contexts` o inspecciona los datos por contexto para ver qué prueba tocó una línea.
* También puedes establecer `dynamic_context = test` (test nodeid) o `dynacontext` via env en ejecutores personalizados.

# Integración con Pytest

Dos patrones comunes:

**A. CLI nativo de coverage (simple y rápido)**

```bash
coverage run -m pytest -q
coverage report -m
```

**B. Plugin pytest-cov (agrega azúcar en la CLI)**

```bash
pip install pytest-cov
pytest --cov=your_package --cov-branch --cov-report=term-missing --cov-report=html
```

Ambos terminan usando coverage.py internamente; usa el que se adapte a las convenciones de tu equipo.

# Cableado típico de CI (bosquejo de GitHub Actions)

```yaml
- name: Install
  run: pip install -U pip coverage pytest

- name: Test with coverage
  run: |
    coverage run -m pytest -q
    coverage report -m
    coverage xml
- name: Enforce threshold
  run: coverage report --fail-under=90
- name: Upload HTML
  if: always()
  uses: actions/upload-artifact@v4
  with:
    name: htmlcov
    path: htmlcov/
```

# Problemas comunes y soluciones

* **Informes enormes/lentos**: Restringe `source=` y usa `omit=` para omitir venv, pruebas, código generado.
* **Rutas diferentes en CI vs local**: Agrega una sección `[paths]` para que `coverage combine` fusione los conjuntos de datos.
* **Subprocesos no medidos**: Establece `COVERAGE_PROCESS_START` y mantén `parallel = True`, luego `coverage combine`.
* **Frameworks asíncronos**: Agrega la entrada relevante a `concurrency = ...`.
* **Extensiones C**: coverage.py mide Python, no código nativo—escribe pruebas de arnés alrededor del límite de Python.
* **Falsos negativos en código inalcanzable**: Márcalo con `# pragma: no cover`, pero considera refactorizar para que el comportamiento sea probado.

# Comandos útiles que realmente usarás

```bash
coverage erase                       # limpia datos anteriores
coverage run -m pytest               # recoge
coverage report -m                   # resumen en texto con líneas faltantes
coverage html                        # abre htmlcov/index.html
coverage xml                         # analizadores de CI
coverage json                        # scripts/automatización
coverage combine                     # fusiona datos paralelos/de subprocesos
coverage annotate                    # por línea .py, mostrando qué líneas se ejecutaron
```

# Cuándo dejar de ajustar

Apunta a un **umbral significativo** (por ejemplo, 80–95%), impónlo con `fail_under` y enfoca las revisiones en la **cobertura de diff** (¿están probadas las líneas nuevas/cambiadas?). No persigas el 100% en código difícil de ejercitar (banderas de características, guardas defensivas)—usa pragmas con moderación y prefiere un diseño más simple y probado.