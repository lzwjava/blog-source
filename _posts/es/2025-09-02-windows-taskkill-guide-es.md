---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía del Comando Taskkill de Windows
translated: true
type: note
---

En Windows, `taskkill` es una herramienta integrada de línea de comandos que puedes usar para detener (matar) procesos por su **ID de proceso (PID)** o **nombre de imagen (nombre del ejecutable)**.

### Sintaxis Básica

```bat
taskkill /PID <process_id> [/F]
taskkill /IM <image_name> [/F]
```

* `/PID <process_id>` → Matar por ID de proceso.
* `/IM <image_name>` → Matar por nombre de proceso (p. ej., `notepad.exe`).
* `/F` → Terminar el proceso forzosamente.
* `/T` → Matar el proceso especificado y todos los procesos secundarios.

---

### Ejemplos

1. **Matar un proceso por PID:**

```bat
taskkill /PID 1234
```

Esto intentará detener el proceso con PID 1234.

2. **Matar forzosamente un proceso por PID:**

```bat
taskkill /PID 1234 /F
```

3. **Matar un proceso por nombre:**

```bat
taskkill /IM notepad.exe
```

4. **Matar forzosamente por nombre:**

```bat
taskkill /IM notepad.exe /F
```

5. **Matar un proceso y sus hijos:**

```bat
taskkill /IM cmd.exe /T /F
```

---

### Encontrar el PID

Si no conoces el PID:

```bat
tasklist
```

Esto lista todos los procesos en ejecución con sus PIDs. Luego puedes usar `taskkill /PID` en el correcto.

---

⚠️ **Notas**

* Algunos procesos del sistema no se pueden terminar.
* Es posible que necesites ejecutar el Símbolo del sistema como **Administrador** para terminar procesos protegidos.

---

¿Quieres que también te muestre cómo combinar `tasklist` y `taskkill` en un solo comando (p. ej., matar todos los procesos que coincidan con un nombre automáticamente)?