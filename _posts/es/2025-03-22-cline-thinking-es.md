---
audio: false
generated: true
lang: es
layout: post
title: Pensamiento de Cline - Depurando un Script de Instantánea de Servidor en la
  Nube de Hetzner
translated: true
type: note
---

$0.8984

## Proceso Inicial de Depuración

Punto de Control
Comparar
Restaurar


**Pensando**
Necesito corregir un error en el archivo `hetzner.py`. El error muestra que un objeto 'Server' no tiene el atributo 'create_snapshot'. Primero déjame revisar el contenido de este archivo para entender qué está pasando. El archivo está ubicado en `scripts/auto-ss-config/hetzner.py` según los detalles del entorno, así que necesito leer este archivo para entender el problema.

Déjame examinar el archivo hetzner.py para entender y corregir el error donde un objeto 'Server' no tiene el atributo 'create_snapshot'.