---
audio: false
generated: true
image: false
lang: es
layout: post
title: PyCharm Renombra Archivos de Forma Segura e Inteligente
translated: true
type: note
---

Sí — si usas **la función de refactorización de PyCharm** (haz clic derecho en el archivo → Refactor → Rename, o presiona `Shift+F6` en el nombre del archivo), no solo renombrará el archivo en el disco, sino que también actualizará **todas las referencias e instrucciones de importación** que apunten a él, siempre que sean resolubles dentro del proyecto.

Algunos detalles importantes a tener en cuenta:

* **Alcance de la refactorización**: PyCharm analiza todo tu proyecto, por lo que las importaciones en otros archivos Python dentro del proyecto se actualizarán automáticamente.
* **Importaciones no resueltas / dinámicas**: Si algunas importaciones se construyen dinámicamente (por ejemplo, usando `__import__`, `importlib` o rutas de módulos basadas en cadenas), PyCharm no las detectará, por lo que no se actualizarán.
* **Múltiples raíces / scripts externos**: Si otros scripts están fuera del proyecto de PyCharm o no están indexados (por ejemplo, no están en las raíces de origen de tu proyecto), PyCharm tampoco los capturará.
* **Tests e importaciones relativas**: Si usas importaciones relativas (`from . import something`) y la estructura de carpetas cambia, es posible que necesites verificarlo por separado.

Por lo tanto, para los casos normales de `import mymodule.something` dentro de tu proyecto, renombrar con la refactorización de PyCharm mantendrá todo consistente.

¿Quieres que también explique **cómo probar de forma segura después de renombrar** para que estés seguro de que nada se rompió?