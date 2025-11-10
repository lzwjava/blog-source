---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía del Formateador de Código Python Black
translated: true
type: note
---

Black es un formateador de código Python con opiniones definidas y sin concesiones, desarrollado por la Python Software Foundation (PSF). Reformatea automáticamente el código Python para ajustarse a un estilo consistente, basado principalmente en un subconjunto estricto de PEP 8, haciendo hincapié en la legibilidad, la coherencia y la minimización de los diffs en el control de versiones. Al usar Black, los desarrolladores aceptan renunciar al control sobre los detalles menores de formato a cambio de velocidad, determinismo y menos debates sobre el estilo durante las revisiones de código. Black garantiza que el código formateado ("ennegrecido") tenga un aspecto uniforme en todos los proyectos, ahorrando tiempo y energía mental para aspectos más críticos del desarrollo. Es compatible con Python 3.8 y versiones posteriores, siendo la última versión estable la 25.1.0 (publicada el 29 de enero de 2025), que introduce el estilo estable 2025 con mejoras como la normalización de las mayúsculas y minúsculas en los escapes Unicode y un manejo mejorado de las comas finales.

La filosofía de Black prioriza:
- **Consistencia**: Construcciones similares se formatean de forma idéntica.
- **Generalidad**: Las reglas se aplican ampliamente sin casos especiales.
- **Legibilidad**: Se centra en un código fácil de leer.
- **Minimización de Diffs**: Reduce los cambios en los diffs de Git para agilizar las revisiones.

Es ampliamente utilizado en proyectos de código abierto y profesionales por su fiabilidad y capacidades de integración.

## Instalación

Black está disponible en PyPI y se puede instalar usando pip. Se recomienda instalarlo en un entorno virtual para aislar el proyecto.

- Instalación básica:
  ```
  pip install black
  ```

- Para funciones adicionales como soporte para Jupyter Notebook o diffs coloreados:
  ```
  pip install 'black[jupyter,colorama]'
  ```
  (El extra `d` es para blackd, un demonio para integraciones en editores).

En Arch Linux, puedes instalarlo mediante el gestor de paquetes: `pacman -S python-black`.

Black también se puede instalar vía conda u otros gestores de paquetes. Después de la instalación, verifica con `black --version`.

Para desarrollo o pruebas, puedes clonar el repositorio de GitHub e instalar en modo editable:
```
git clone https://github.com/psf/black.git
cd black
pip install -e .
```

## Uso

Black es principalmente una herramienta de línea de comandos. El comando básico formatea archivos o directorios in situ:

```
black {archivo_o_directorio_fuente}
```

Si ejecutar Black como un script no funciona (por ejemplo, debido a problemas del entorno), usa:
```
python -m black {archivo_o_directorio_fuente}
```

### Opciones Principales de Línea de Comandos

Black ofrece varios flags para personalización y control. Aquí hay un resumen de los principales:

- `-h, --help`: Muestra la ayuda y sale.
- `-c, --code <código>`: Formatea una cadena de código (ej., `black --code "print ( 'hello, world' )"` devuelve la versión formateada).
- `-l, --line-length <int>`: Establece la longitud de línea (por defecto: 88).
- `-t, --target-version <versión>`: Especifica versiones de Python para compatibilidad (ej., `py38`, se puede especificar múltiples como `-t py311 -t py312`).
- `--pyi`: Trata los archivos como stubs de tipado (estilo `.pyi`).
- `--ipynb`: Trata los archivos como Jupyter Notebooks.
- `--python-cell-magics <magia>`: Reconoce magias personalizadas de Jupyter.
- `-x, --skip-source-first-line`: Omite formatear la primera línea (útil para shebangs).
- `-S, --skip-string-normalization`: No normaliza las comillas de las cadenas a dobles ni los prefijos.
- `-C, --skip-magic-trailing-comma`: Ignora las comas finales para saltos de línea.
- `--preview`: Habilita cambios de estilo experimentales para la próxima versión.
- `--unstable`: Habilita todos los cambios de vista previa más funciones inestables (requiere `--preview`).
- `--enable-unstable-feature <característica>`: Habilita características inestables específicas.
- `--check`: Comprueba si los archivos necesitan reformateo sin cambiarlos (código de salida 1 si se necesitan cambios).
- `--diff`: Muestra un diff de los cambios sin escribir en los archivos.
- `--color / --no-color`: Colorea la salida del diff.
- `--line-ranges <rangos>`: Formatea rangos de líneas específicos (ej., `--line-ranges=1-10`).
- `--fast / --safe`: Omite (`--fast`) o aplica (`--safe`) comprobaciones de seguridad del AST (por defecto: safe).
- `--required-version <versión>`: Requiere una versión específica de Black.
- `--exclude <regex>`: Excluye archivos/directorios mediante regex.
- `--extend-exclude <regex>`: Añade exclusiones a las predeterminadas.
- `--force-exclude <regex>`: Excluye incluso si se pasa explícitamente.
- `--include <regex>`: Incluye archivos/directorios mediante regex.
- `-W, --workers <int>`: Establece el número de workers paralelos (por defecto: número de CPUs).
- `-q, --quiet`: Suprime mensajes que no son de error.
- `-v, --verbose`: Muestra salida detallada.
- `--version`: Muestra la versión de Black.
- `--config <archivo>`: Carga la configuración desde un archivo.

### Ejemplos

- Formatear un solo archivo: `black ejemplo.py`
- Comprobar sin formatear: `black --check .`
- Mostrar diff: `black --diff ejemplo.py`
- Formatear desde stdin: `echo "print('hello')" | black -`
- Formatear con longitud de línea personalizada: `black -l 79 ejemplo.py`
- Formatear Jupyter Notebook: `black notebook.ipynb`

### Consejos y Notas

- Black formatea archivos completos; usa `# fmt: off` / `# fmt: on` para omitir bloques o `# fmt: skip` para líneas.
- Para stdin, usa `--stdin-filename` para respetar exclusiones.
- Black es determinista: la misma entrada siempre produce la misma salida.
- Usa `--preview` para probar estilos futuros, pero ten en cuenta que pueden cambiar.

## Configuración

Black se puede configurar mediante flags de línea de comandos o un archivo `pyproject.toml` (preferido para proyectos). La configuración en `pyproject.toml` va en una sección `[tool.black]`.

### Usando pyproject.toml

Ejemplo:
```
[tool.black]
line-length = 79
target-version = ['py311']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''
skip-string-normalization = true
```

Las opciones admitidas reflejan los flags CLI (ej., `line-length`, `skip-string-normalization`). Las opciones multi-valor como `target-version` usan arrays.

### Precedencia

- Los flags de línea de comandos anulan la configuración del archivo.
- Si no se encuentra un `pyproject.toml`, Black usa los valores predeterminados y busca en los directorios padre.
- Usa `--config` para especificar un archivo de configuración personalizado.

### Descubrimiento e Ignorado de Archivos

Black descubre automáticamente los archivos Python en los directorios, respetando `.gitignore` por defecto. Usa `--include`/`--exclude` para personalizar. Ignora directorios comunes como `.git`, `.venv`, etc., a menos que se anule.

Para el control de versiones, integra con herramientas como pre-commit para hacer cumplir el formateo.

## El Estilo de Código Black

Black impone un estilo específico con una capacidad de configuración limitada. Reglas clave:

### Longitud de Línea
- Por defecto: 88 caracteres. Puede excederse si es irrompible (ej., cadenas largas).

### Cadenas de Texto
- Prefiere comillas dobles; normaliza los prefijos a minúsculas (ej., `r` antes de `f`).
- Convierte a minúsculas las secuencias de escape (excepto los nombres `\N`).
- Procesa docstrings: arregla la indentación, elimina espacios en blanco/nuevas líneas extra, preserva tabulaciones en el texto.

### Literales Numéricos
- Partes sintácticas en minúsculas (ej., `0xAB`), dígitos en mayúsculas.

### Saltos de Línea y Operadores
- Rompe antes de los operadores binarios.
- Un solo espacio alrededor de la mayoría de los operadores; sin espacios para operadores unarios/potencia con operandos simples.

### Comas Finales
- Las añade a colecciones multi-línea/argumentos de función (si es Python 3.6+).
- La coma final "mágica" explota las listas si está presente.

### Comentarios
- Dos espacios antes de los comentarios en línea; un espacio antes del texto.
- Preserva el espaciado especial para shebangs, comentarios de documentación, etc.

### Indentación
- 4 espacios; coincide los corchetes con cierres desindentados.

### Líneas Vacías
- Mínimo espacio en blanco: una sola línea en funciones, doble a nivel de módulo.
- Reglas específicas para docstrings, clases y funciones.

### Importaciones
- Divide importaciones largas; compatible con el perfil `black` de isort.

### Otras Reglas
- Prefiere paréntesis sobre barras invertidas.
- Normaliza los finales de línea según el archivo.
- Estilo conciso para archivos `.pyi` (ej., sin líneas extra entre métodos).
- Colapsa líneas vacías después de importaciones en modo preview.

Black pretende reducir los diffs y mejorar la legibilidad, con cambios principalmente para correcciones de errores o soporte de nueva sintaxis.

## Integraciones

Black se integra perfectamente con editores y control de versiones para el formateo automatizado.

### Editores

- **VS Code**: Usa la extensión Python con Black como formateador. Establece `"python.formatting.provider": "black"` en settings.json. Para LSP, instala python-lsp-server y python-lsp-black.
- **PyCharm/IntelliJ**:
  - Integrado (2023.2+): Configuración > Herramientas > Black, configurar la ruta.
  - Herramienta Externa: Configuración > Herramientas > Herramientas Externas, añadir Black con el argumento `$FilePath$`.
  - File Watcher: Para auto-formatear al guardar.
  - Plugin BlackConnect para formateo basado en demonio.
- **Vim**: Usa el plugin oficial (vía vim-plug: `Plug 'psf/black', { 'branch': 'stable' }`). Comandos: `:Black` para formatear. Auto-guardado: Añade autocmd al vimrc. Variables de configuración como `g:black_linelength`.
- **Emacs**: Usa reformatter.el o el paquete python-black para formateo al guardar.
- **Otros**: Soporta Sublime Text, JupyterLab, Spyder, etc., mediante plugins o extensiones.

### Control de Versiones

- **Ganchos Pre-commit**: Añade a `.pre-commit-config.yaml`:
  ```
  repos:
    - repo: https://github.com/psf/black-pre-commit-mirror
      rev: 25.1.0
      hooks:
        - id: black
          language_version: python3.11
  ```
  Para Jupyter: Usa `id: black-jupyter`.
- **GitHub Actions**: Usa acciones como `psf/black-action` en los flujos de trabajo para comprobaciones CI.
- **Git**: Ejecuta Black en scripts pre-commit o husky para su aplicación.

## Temas Avanzados

- **Estilos Preview e Inestables**: Usa `--preview` para cambios futuros (ej., mejor ajuste de paréntesis). `--unstable` para características experimentales.
- **Blackd**: Servidor HTTP para integraciones (`blackd --bind-host 127.0.0.1 --bind-port 45484`).
- **Soporte Jupyter**: Formatea notebooks, preservando las magias.
- **Stubs de Tipado**: Formateo especial conciso para archivos `.pyi`.
- **Compatibilidad**: Apunta a Python 3.8+; usa `--target-version` para código más antiguo.
- **Alternativas**: Comparado con autopep8 (más flexible pero menos opinado) o Ruff (más rápido, incluye linting).

Para resolución de problemas, consulta las FAQ en la documentación oficial o los issues de GitHub.

## Referencias

- [Documentación de Black 25.1.0](https://black.readthedocs.io/en/stable/)
- [Repositorio GitHub psf/black](https://github.com/psf/black)
- [El Estilo de Código Black](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)
- [Uso y Configuración](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html)
- [Integraciones con Editores](https://black.readthedocs.io/en/stable/integrations/editors.html)
- [Integración con Control de Versiones](https://black.readthedocs.io/en/stable/integrations/source_version_control.html)
- [Formateo de Código Python Usando Black - GeeksforGeeks](https://www.geeksforgeeks.org/python/python-code-formatting-using-black/)
- [Cómo Auto-Formatear Tu Código Python con Black - freeCodeCamp](https://www.freecodecamp.org/news/auto-format-your-python-code-with-black/)
- [Black - PyPI](https://pypi.org/project/black/)
- [Introducción al Módulo Python Black - GeeksforGeeks](https://www.geeksforgeeks.org/introduction-to-python-black-module/)
- [Auto Formateador Python: Autopep8 vs. Black - Built In](https://builtin.com/data-science/autopep8-vs-black)