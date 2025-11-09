---
audio: false
date: 2025-09-09
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Prevención de Bifurcaciones de Repositorios en GitHub
translated: true
type: note
---

En GitHub, **no puedes impedir que las personas hagan un fork de un repositorio público**. Hacer fork es una característica fundamental de GitHub para la colaboración abierta. Si tu repositorio es público, cualquiera puede hacer un fork.

Estas son tus opciones dependiendo de tu objetivo:

### 1. Si quieres evitar que se hagan forks por completo

* La única forma es hacer que tu repositorio sea **privado**.
* Los repositorios privados no se pueden bifurcar hacia cuentas externas.
* Dentro de una organización, los administradores pueden controlar si los repositorios privados se pueden bifurcar hacia otros miembros.

### 2. Si quieres reducir la exposición pero mantenerlo público

* Puedes **restringir la licencia**: añadir una licencia que no permita la redistribución (por ejemplo, "Todos los derechos reservados"). Esto técnicamente no detendrá los forks, pero te brinda protección legal.
* Puedes **deshabilitar GitHub Pages** y otras funciones de exposición para reducir la visibilidad.

### 3. Si tu repositorio ya ha sido bifurcado

* No puedes "eliminar el fork" de la copia de otra persona.
* Solo puedes pedirle al propietario del fork que lo elimine, o presentar una **solicitud de eliminación DMCA** con GitHub si están violando tu licencia o tus derechos.

---

👉 En resumen:

* Repositorio público → siempre se puede hacer fork.
* Repositorio privado → protección contra forks, a menos que se permita explícitamente dentro de tu organización.

¿Quieres que te explique **cómo configurar un repositorio como privado y deshabilitar los forks internos**?