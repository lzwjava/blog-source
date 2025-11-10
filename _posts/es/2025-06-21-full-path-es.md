---
audio: false
generated: true
lang: es
layout: post
title: Cómo Obtener la Ruta Completa de un Archivo en Ubuntu
translated: true
type: note
---

En Ubuntu, puedes obtener la ruta completa de un archivo usando los comandos `realpath` o `readlink -f`. Para tu ejemplo con `geckodriver`, puedes ejecutar:

```bash
realpath ./geckodriver
```

o

```bash
readlink -f ./geckodriver
```

Ambos mostrarán la ruta completa, por ejemplo:

```
/home/lzw/bin/geckodriver
```

El comando `realpath` es directo y se usa comúnmente para este propósito. Si `realpath` no está instalado, puedes instalarlo con:

```bash
sudo apt install realpath
```

Alternativamente, `readlink -f` suele estar disponible por defecto como parte de coreutils.