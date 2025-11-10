---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Resumen de Git Fetch y Prune
translated: true
type: note
---

### ¿Qué es `git fetch`?
`git fetch` descarga los últimos cambios (commits, ramas, tags) de un repositorio remoto sin fusionarlos en tu rama actual. Actualiza tus ramas de seguimiento remotas locales (por ejemplo, `origin/main`) para que coincidan con el estado del remoto. Esto mantiene tu repositorio local sincronizado pero no altera tus archivos de trabajo ni tus ramas locales.

### ¿Qué es la opción `--prune`?
El flag `--prune` le indica a Git que elimine las ramas de seguimiento remotas que ya no existen en el remoto. Por ejemplo, si alguien elimina una rama en GitHub, tu copia local (por ejemplo, `origin/old-branch`) persistirá a menos que la podes.

### ¿Cómo funciona `git fetch --prune`?
- **Ejecución**: Ejecútalo como `git fetch --prune` (o `git fetch -p` para abreviar). Combina fetch y prune en un solo comando.
- **Pasos**:
  1. Git se conecta al remoto y obtiene las actualizaciones, actualizando las ramas de seguimiento remotas para reflejar nuevos commits, ramas añadidas o ramas eliminadas.
  2. Escanea en busca de ramas de seguimiento remotas obsoletas (aquellas que no tienen una contraparte en el remoto) y las elimina localmente.
- **Resultado**: Tu repositorio local se mantiene actualizado y limpio. No se produce ninguna fusión; es una sincronización de solo lectura.

### Ejemplo práctico
Supongamos que tienes:
- Rama local: `main`, que rastrea `origin/main`.
- Una rama de seguimiento remota local obsoleta: `origin/deleted-feature`.

Al ejecutar `git fetch --prune` para `origin`:
- Obtiene cualquier nuevo commit.
- Elimina `origin/deleted-feature` (ya que ha desaparecido en el remoto).
- No toca tus ramas locales.

### Lo que significa
Significa "obtener los últimos datos remotos y limpiar las referencias obsoletas" en tu repositorio local. Úsalo regularmente para evitar confusiones con referencias de ramas antiguas. Equivale a ejecutar `git fetch` seguido de `git remote prune origin`, pero convenientemente combinado. Por seguridad, solo afecta a las ramas de seguimiento remotas, no a tu propio trabajo.