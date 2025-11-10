---
audio: false
generated: true
image: false
lang: es
layout: post
title: Excluir archivos en IntelliJ IDEA
translated: true
type: note
---

En IntelliJ IDEA, puedes excluir archivos o directorios para que no aparezcan en búsquedas, indexación, autocompletado de código o builds. Hay varias formas de hacerlo dependiendo de tu propósito:

---

### 1. Marcar un directorio como *Excluido*

* En la vista **Project**, haz clic derecho en la carpeta que quieres excluir.
* Elige **Mark Directory as → Excluded**.
* IDEA dejará de indexarla, por lo que no aparecerá en búsquedas, navegación o análisis de código.

Esto se usa típicamente para carpetas de salida de build (`target/`, `out/`, `dist/`, etc.).

---

### 2. Excluir del Control de Versiones (VCS Ignore)

Si no quieres que IDEA (y Git) rastree ciertos archivos:

* Crea o edita un archivo `.gitignore` en tu proyecto.
* Añade los patrones de directorio o nombre de archivo allí.
* IDEA reconocerá `.gitignore` y los ocultará de las operaciones de VCS.

---

### 3. Excluir archivos del Análisis de Código / Inspecciones

* Ve a **Settings → Editor → Inspections**.
* Allí puedes configurar **Scopes** y asignar inspecciones solo a ciertos conjuntos de archivos excluyendo otros.

---

### 4. Excluir del Build (Gradle/Maven)

Si estás usando Gradle o Maven, puedes configurar `build.gradle` o `pom.xml` para excluir ciertos directorios (como código generado o recursos). IDEA respeta estas configuraciones de las herramientas de build.

---

### 5. Excluir tipos de archivo específicos

* Ve a **Settings → Editor → File Types**.
* Añade patrones (como `*.log`, `*.tmp`) a la lista "Ignore files and folders".

---

👉 Consejo rápido: Si tu objetivo es solo evitar que IDEA gaste recursos indexando carpetas grandes (como `node_modules/`), la opción **Mark Directory as Excluded** es la más rápida y efectiva.

¿Quieres que también te muestre cómo excluir directorios de prueba (como `src/test/java`) de las ejecuciones de **code coverage** en IDEA?