---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Guía de Matrices de Compilación de GitHub Actions
translated: true
type: note
---

Parece que estás preguntando sobre el uso de compilaciones de matriz de **GitHub Actions** para ejecutar pruebas en paralelo, y cómo usar la opción `fail-fast` en una estrategia de matriz. Permíteme desglosarlo para ti.

---

### Compilaciones de Matriz en GitHub Actions
La **estrategia de matriz** te permite ejecutar el mismo trabajo en paralelo con diferentes parámetros; por ejemplo, probar en múltiples versiones de Python o Node, o en diferentes sistemas operativos.

Un ejemplo mínimo:

```yaml
name: CI

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10]
        os: [ubuntu-latest, windows-latest]
      fail-fast: false
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
```

---

### Puntos Clave

- **`matrix`:** Define las variables para crear combinaciones de trabajos.  
  El ejemplo anterior ejecuta pruebas para todas las combinaciones de (`python-version`, `os`).

- **Ejecución en paralelo:** Cada trabajo generado por la matriz se ejecuta **en paralelo** por defecto.

- **`fail-fast`:**
  - El valor por defecto es `true`. Esto significa que si un trabajo falla, el resto de los trabajos de la matriz se cancelan.
  - Configura `fail-fast: false` si quieres que todos los trabajos de la matriz continúen ejecutándose, incluso si uno falla.

  Ejemplo:
  ```yaml
  strategy:
    matrix:
      node: [14, 16, 18]
    fail-fast: false
  ```

- **Limitar el total de trabajos:** Puedes excluir algunas combinaciones:
  ```yaml
  strategy:
    matrix:
      python-version: [3.8, 3.9, 3.10]
      os: [ubuntu-latest, windows-latest]
    exclude:
      - python-version: 3.8
        os: windows-latest
  ```

---

### Ejecución de Pruebas en Paralelo
- Cada **trabajo de la matriz se ejecuta en paralelo** en su propio runner, por lo que no necesitas hacer nada especial.
- Dentro de cada trabajo, si deseas **ejecución de pruebas en paralelo** (por ejemplo, pytest `-n auto`), puedes agregarlo a nivel del comando de prueba.

Ejemplo:
```yaml
- name: Run pytest in parallel
  run: pytest -n auto
```

---

✅ **Resumen:**
- Usa `strategy.matrix` para definir diferentes combinaciones de parámetros.
- Configura `fail-fast: false` si quieres que todos los trabajos de la matriz se ejecuten incluso si uno falla.
- Los trabajos de la matriz se ejecutan en paralelo automáticamente.
- Para un tiempo de ejecución más rápido dentro de cada trabajo, usa la paralelización del framework de pruebas (por ejemplo, pytest-xdist).

---

¿Te gustaría que te muestre un ejemplo real para **ejecutar pruebas de Node/JavaScript** con matriz (múltiples versiones de Node, `fail-fast: false`, pruebas paralelizadas con `npm test`)?