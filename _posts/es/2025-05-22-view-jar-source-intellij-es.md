---
audio: false
generated: true
image: false
lang: es
layout: post
title: Ver Código Fuente JAR en IntelliJ IDEA
translated: true
type: note
---

En IntelliJ IDEA, puedes ver fácilmente el código fuente de un archivo JAR. Existen varios métodos dependiendo de si el JAR contiene archivos fuente o solo archivos compilados `.class`:

---

### 1. Abrir el JAR en IDEA

* Ve a **File > Open…**
* Selecciona el archivo JAR.
* IDEA lo abrirá en la **vista Project** como un archivo regular.
* Si el JAR contiene archivos fuente `.java`, puedes navegarlos directamente.
* Si solo contiene archivos `.class`, IDEA los descompilará automáticamente a código Java legible.

---

### 2. Adjuntar Fuentes a un JAR de Biblioteca

Si el JAR es parte de una biblioteca (como dependencias de Maven o Gradle):

* Ve a **File > Project Structure > Libraries** (o **Modules > Dependencies** si es específico del módulo).
* Selecciona el JAR.
* Haz clic en **Attach Sources…** e indica a IDEA la ruta al `-sources.jar` (si está disponible).
* Ahora IDEA mostrará el código fuente real en lugar del código descompilado.

---

### 3. Navegación Rápida

* Mantén presionada **Ctrl (Cmd en macOS)** y haz clic en una clase o método que provenga del JAR.
* Si no hay fuentes adjuntas, IDEA muestra la versión descompilada.
* Si las fuentes están adjuntas, verás el código Java original.

---

### 4. Plugins de Descompilador Externos (Opcional)

IDEA ya incluye un descompilador integrado, pero puedes instalar plugins como **Fernflower** o **CFR** si deseas una descompilación alternativa.

---

👉 Normalmente, si es una dependencia gestionada por Maven/Gradle, IDEA puede descargar y adjuntar automáticamente el `-sources.jar` desde el repositorio. Si es un JAR independiente, necesitarás adjuntar las fuentes manualmente o depender del descompilador.

¿Quieres que también explique **cómo extraer el código fuente del JAR fuera de IDEA** (usando herramientas como `jd-gui` o `jar xf`), o prefieres centrarte en trabajar dentro de IDEA?