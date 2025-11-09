---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Herencia Unix de macOS y Linux
translated: true
type: note
---

### Orígenes comunes de macOS y Linux

macOS (anteriormente OS X) y Linux comparten raíces conceptuales en Unix, un sistema operativo pionero de multitarea desarrollado en Bell Labs en la década de 1970. Linux, creado por Linus Torvalds en 1991, es un kernel de código abierto modelado a partir de Unix pero desarrollado de forma independiente; no se deriva del código fuente de Unix. macOS, por su parte, está construido sobre Darwin (un sistema operativo tipo Unix de Apple, basado en FreeBSD), que incluye componentes Unix y está certificado como compatible con Unix por The Open Group. Esta herencia compartida explica muchas similitudes en herramientas y comandos, ya que ambos buscan proporcionar funcionalidad tipo Unix.

Evidencia de apoyo: Los estándares de Unix (por ejemplo, POSIX) influyeron en ambos sistemas para garantizar la compatibilidad. Las distribuciones de Linux como Ubuntu son explícitamente tipo Unix, y macOS hereda herramientas Unix a través de BSD (Berkeley Software Distribution), otra rama temprana de Unix.

### Por qué ambos tienen el comando 'ps'

El comando 'ps' (process status) muestra información sobre los procesos en ejecución y se origina directamente en Unix, donde se implementó por primera vez en la década de 1970. Tanto macOS como Linux incluyen 'ps' porque:
- Es parte de su herencia Unix: macOS a través de Darwin/FreeBSD, y Linux a través del sistema de archivos PROC y las utilidades estándar de las especificaciones GNU o POSIX.
- Es esencial para diagnósticos del sistema, scripting y administración, por lo que se incluye por defecto en sus conjuntos de herramientas principales (por ejemplo, en la Terminal de macOS o en el shell de Linux).

La sintaxis del comando, como `ps -p pid -o pid,ppid,lstart,etime,command`, es compatible en ambos debido a los estándares POSIX compartidos, aunque las opciones pueden variar ligeramente (por ejemplo, macOS tiene flags con variantes BSD, mientras que Linux a menudo usa variantes GNU). Esto no es una coincidencia; es un linaje directo de Unix.

### ¿Podemos decir que macOS y Linux son ambos Unix?

No exactamente: "Unix" es una familia de sistemas operativos y una marca registrada. macOS califica como Unix porque Darwin está certificado (por The Open Group) y cumple con la Single Unix Specification (SUS). Linux, sin embargo, es un kernel que forma la base para sistemas operativos completos (distribuciones como Debian), pero el kernel en sí y sus distribuciones no son oficialmente "Unix"; son tipo Unix o compatibles con Unix debido a su adhesión a POSIX sin una certificación completa o una base de código compartida.

Se podría decir que son "tipo Unix" o "portadores de las tradiciones de Unix", pero llamarlos "todos Unix" sería inexacto para Linux. En la práctica, esto no importa mucho para la mayoría de los usuarios, ya que se comportan de manera similar para comandos como 'ps'. Si la precisión es clave, verifique las certificaciones o consulte las definiciones oficiales.