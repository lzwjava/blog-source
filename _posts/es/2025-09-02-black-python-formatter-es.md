---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía del Formateador de Código Python Negro
translated: true
type: note
---

El paquete `black` en PyPI es un **formateador de código Python**. Reformatea automáticamente tu código Python para seguir reglas de estilo consistentes (compatible con PEP 8, pero con sus propias opiniones estrictas). Aquí te mostramos cómo usarlo:

---

### 1. Instalar Black

```bash
pip install black
```

Si quieres asegurarte de obtener siempre la última versión estable:

```bash
pip install -U black
```

---

### 2. Formatear un Archivo o Directorio

Ejecuta Black en un archivo:

```bash
black my_script.py
```

Ejecuta Black en un directorio completo (de forma recursiva):

```bash
black src/
```

Por defecto, sobrescribirá los archivos en el lugar con el código formateado.

---

### 3. Verificar el Formato Sin Cambiar

Usa `--check` para ver si tus archivos necesitan reformatearse:

```bash
black --check my_script.py
```

Esto es útil para pipelines de CI, para garantizar la consistencia del estilo.

---

### 4. Opciones Comunes

* `--line-length 88` → Cambiar la longitud de línea (por defecto: 88).
* `--diff` → Mostrar qué cambiaría, sin modificar el archivo.
* `--skip-string-normalization` → No cambiar las comillas de las cadenas.
* `--exclude` → Omitir ciertos archivos/carpetas.

Ejemplo:

```bash
black --line-length 100 --diff src/
```

---

### 5. Integración

* **Soporte para IDE**: Black está disponible como un plugin en PyCharm, VS Code, Vim, Emacs, etc.
* **Pre-commit hook**: Añade Black a `.pre-commit-config.yaml` para que el código se formatee antes de los commits:

  ```yaml
  repos:
    - repo: https://github.com/psf/black
      rev: stable
      hooks:
        - id: black
  ```
* **CI/CD**: Añade `black --check .` en tu pipeline de CI.

---

👉 ¿Quieres que también te muestre cómo configurar **el formateo automático en VSCode o PyCharm**, para que no necesites ejecutar `black` manualmente?