---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía de Control de Fin de Línea de Git
translated: true
type: note
---

`git config core.autocrlf` controla cómo Git maneja los fines de línea cuando extraes archivos del repositorio y cuando los confirmas. Es importante porque Windows usa **CRLF** (`\r\n`) para fines de línea, mientras que Linux y macOS usan **LF** (`\n`). Sin un manejo adecuado, los archivos pueden cambiar de formato dependiendo de quién los edite, lo que genera diferencias "sucias" y cambios innecesarios.

---

### Cómo Funciona

* **Al extraer (leer)** un archivo, Git puede convertir los fines de línea para que coincidan con la convención de tu sistema operativo (para que se vean naturales en tu editor).
* **Al confirmar (escribir)** un archivo, Git puede convertir los fines de línea de nuevo a LF (el estándar multiplataforma en los repositorios).

---

### Configuraciones

Se configura con:

```bash
git config --global core.autocrlf <valor>
```

Los valores comunes:

* `true`
  Convierte **LF → CRLF** al extraer y **CRLF → LF** al confirmar.
  Lo mejor para **desarrolladores en Windows** que editan código en editores de Windows.

* `input`
  **No** modifica los archivos al extraer, pero convierte **CRLF → LF** al confirmar.
  Lo mejor para **desarrolladores en Linux/macOS** para garantizar repositorios con solo LF.

* `false`
  Sin conversión alguna. Git almacena y extrae los archivos exactamente como están.
  Lo mejor si tu equipo o editor maneja los fines de línea de manera consistente.

---

### Recomendaciones Típicas

* **Windows**:

  ```bash
  git config --global core.autocrlf true
  ```
* **Linux/macOS**:

  ```bash
  git config --global core.autocrlf input
  ```

Para equipos mixtos, también es bueno agregar un archivo `.gitattributes` en el repositorio para imponer fines de línea consistentes, por ejemplo:

```
* text=auto
```

---

¿Quieres que también te muestre una **configuración recomendada para `.gitattributes`** que funcione bien para equipos multiplataforma (para que no dependas solo de `core.autocrlf`)?