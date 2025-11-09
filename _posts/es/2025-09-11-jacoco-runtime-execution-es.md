---
audio: false
date: 2025-09-11
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Comportamiento del Archivo de Ejecución en Tiempo de Ejecución de JaCoCo
translated: true
type: note
---

Cuando ejecutas **WebSphere Liberty Profile** con el **agente JaCoCo** en modo `exec`, el agente JaCoCo **no modifica** el archivo `.exec` original durante el tiempo de ejecución. Esto es lo que sucede:

---

### Cómo funciona JaCoCo en modo `exec`
- **Propósito**: El agente JaCoCo recopila **datos de cobertura de código** mientras tu aplicación se ejecuta.
- **Salida**: Escribe los datos de cobertura en el archivo `.exec` (por ejemplo, `jacoco.exec`).
- **Comportamiento del archivo**:
  - Si el archivo **no existe**, JaCoCo lo crea.
  - Si el archivo **ya existe**, JaCoCo **añade** nuevos datos de cobertura a él (no sobrescribe ni modifica los datos existentes a menos que restablezcas o fusiones el archivo explícitamente).
  - El archivo `.exec` original **no se altera** de una manera que rompa o cambie su estructura—solo crece con nuevos datos.

---

### ¿Se modificará el archivo `.exec`?
- **Sí, pero solo añadiendo datos**: El archivo se actualizará con nueva información de cobertura cada vez que ejecutes tu aplicación con el agente JaCoCo.
- **Sin cambios estructurales**: El formato del archivo `.exec` permanece igual; es un archivo binario que contiene datos de cobertura.

---

### Mejores prácticas
- **Fusionar o Restablecer**: Si quieres empezar de nuevo, borra o renombra el archivo `.exec` antes de ejecutar tu aplicación otra vez.
- **Fusionar Múltiples Ejecuciones**: Usa el goal `jacoco:merge` (en Maven) o la clase `org.jacoco.agent.rt.RT` para fusionar múltiples archivos `.exec` si es necesario.

---

### Ejemplo de Configuración para Liberty
En tu `server.env` o `jvm.options` para Liberty, podrías ver:
```bash
-javaagent:/ruta/a/jacocoagent.jar=destfile=/ruta/a/jacoco.exec,append=true
```
- `append=true` asegura que los nuevos datos se añadan al archivo existente.

---