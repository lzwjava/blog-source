---
audio: false
date: 2025-09-09
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Gestión de Puertos y Procesos de Windows
translated: true
type: note
---

En Windows, puedes verificar qué puertos están siendo escuchados — y por qué proceso (PID) — usando `netstat`, y luego gestionar o eliminar esos procesos con `taskkill`. Esto suele ser necesario al depurar proyectos de backend como aplicaciones Java Spring Boot, Redis o MySQL. Aquí te mostramos cómo:

---

### 1. Verificar puertos en escucha

Ejecuta **Símbolo del sistema (cmd)** o **PowerShell** como Administrador:

```bash
netstat -ano | findstr LISTENING
```

* `-a` → muestra todas las conexiones y puertos en escucha
* `-n` → muestra direcciones y puertos en forma numérica
* `-o` → incluye PID (ID del proceso)

Ejemplo de salida:

```
TCP    0.0.0.0:8080     0.0.0.0:0     LISTENING     12345
TCP    0.0.0.0:3306     0.0.0.0:0     LISTENING     6789
```

Aquí:

* El puerto `8080` es usado por el PID `12345` (probablemente tu aplicación Spring Boot).
* El puerto `3306` es usado por el PID `6789` (MySQL).

---

### 2. Encontrar a qué proceso pertenece ese PID

Puedes relacionar el PID con un nombre de proceso:

```bash
tasklist | findstr 12345
```

La salida podría mostrar:

```
java.exe                  12345 Console                    1     512,000 K
```

Eso significa que tu aplicación Spring Boot se está ejecutando en el puerto 8080.

---

### 3. Eliminar el proceso si es necesario

Si quieres detener ese proceso:

```bash
taskkill /PID 12345 /F
```

* `/PID` → especifica el ID del proceso
* `/F` → forzar la terminación

---

### 4. Puertos típicos para servicios de backend comunes

* **Spring Boot (aplicación Java):** 8080, 8081, etc.
* **MySQL:** 3306
* **Redis:** 6379
* **PostgreSQL:** 5432

Así que, si ves esos puertos en la salida de `netstat`, sabrás qué servicio se está ejecutando.

---

👉 Consejo profesional: Puedes combinar estos comandos en uno solo para encontrar directamente qué proceso está usando un puerto determinado (por ejemplo, 8080):

```bash
netstat -ano | findstr :8080
```

Luego toma el PID y verifícalo con `tasklist`.

---

¿Quieres que también te muestre un **comando de una línea en PowerShell** que mapee directamente los puertos a nombres de proceso sin necesidad de verificar por separado con `tasklist`?