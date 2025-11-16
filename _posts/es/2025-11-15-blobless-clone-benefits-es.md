---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Beneficios de un Clon de Git Sin Blobs
translated: true
type: note
---

El comando de Git:

```bash
git clone --filter=blob:none <url-del-repositorio>
```

es un **clon parcial** que descarga **casi ningún contenido de archivo** (blobs) en el momento del checkout. Esto es exactamente lo que hace y por qué es útil:

### Qué significa `--filter=blob:none`
- `--filter=blob:none` le dice a Git que use **clonación sin blobs**.
- Git aún descarga:
  - Todos los commits (historial)
  - Todos los objetos de árbol (estructura de directorios)
  - Todas las referencias/ramas/etiquetas
- Pero descarga **cero contenidos de archivo** (blobs) durante el clon inicial.
- Cuando posteriormente haces `git checkout` o cambias de rama, Git descarga solo los blobs (contenidos de archivo) para los archivos que realmente se necesitan en tu árbol de trabajo en ese momento.

### Beneficios clave
- Clon inicial extremadamente rápido y pequeño (a menudo solo unos pocos MB incluso para repositorios enormes como el kernel de Linux, Android o el código fuente de Windows).
- Usa mucho menos ancho de banda de red y espacio en disco al principio.
- Perfecto para CI/CD, consultas rápidas o cuando solo necesitas el historial (ej. `git log`, blame, diff entre commits) sin necesidad de hacer checkout de los archivos.

### Ejemplo de comparación de tamaño (mundo real)

| Repositorio      | Clon normal | Clon `blob:none` | Ganancia de velocidad |
|------------------|-------------|------------------|------------------------|
| torvalds/linux   | ~5+ GB      | ~300–400 MB      | 10–20× más rápido      |
| microsoft/vscode | ~2–3 GB     | ~200 MB          | mucho más rápido       |

### Comandos de seguimiento comunes después de un clon blob:none
```bash
# La primera vez que necesites un árbol de trabajo:
git checkout <rama>          # descarga solo los blobs necesarios

# O si quieres todo más tarde:
git fetch --unshallow        # no es necesario para blobless
# Para llenar los blobs que faltan permanentemente:
git repack -a -d             # opcional, fuerza la descarga de todos los blobs
```

### Filtros relacionados que podrías ver
- `--filter=blob:none` → ningún blob inicialmente (el más agresivo)
- `--filter=tree:0`    → descarga árboles pero no blobs (efecto similar)
- `--filter=sparse:oid=<oid>` → para sparse-checkout con blobs parciales

### Resumen
```bash
git clone --filter=blob:none https://github.com/example/repo.git
```
= "Dame el historial y la estructura completos inmediatamente, pero descarga los contenidos de los archivos bajo demanda más tarde."  
Excelente para monorepos enormes o cuando solo quieres navegar por el historial sin esperar horas.