---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Configuración de Desencadenadores de Rama en Azure DevOps
translated: true
type: note
---

Azure DevOps Pipelines permite configurar qué ramas activan compilaciones e implementaciones. Esto se realiza principalmente mediante **desencadenadores de CI** (para compilaciones en pushes de código) y **desencadenadores de PR** (para pull requests). La configuración difiere ligeramente entre pipelines YAML (recomendado para control de versiones) y pipelines clásicos. A continuación, me centraré primero en YAML, ya que es el enfoque moderno, luego cubriré brevemente el clásico. Todos los ejemplos asumen un repositorio Git.

## Pipelines YAML: Configurar desencadenadores de rama

Los pipelines YAML definen los desencadenadores directamente en su archivo `azure-pipelines.yml`. Por defecto, los pipelines se activan con pushes en **todas las ramas** (equivalente a `trigger: branches: include: - '*'`). Puede personalizar esto para un control más detallado.

### Paso 1: Configuración básica
1. En su proyecto de Azure DevOps, vaya a **Pipelines > Builds** (o **Releases** para CD).
2. Cree o edite un pipeline y seleccione **YAML** como plantilla.
3. En el editor YAML, agregue una sección `trigger` en el nivel superior.

### Paso 2: Inclusión simple de ramas
Use una lista simple para activar en ramas o patrones específicos:
```yaml
trigger:
- main          # Se activa con pushes a 'main'
- develop       # También 'develop'
- releases/*    # Cualquier rama que comience con 'releases/' (ej., releases/v1.0)
```
- Guarde y confirme el archivo YAML en su repositorio. El pipeline ahora solo se ejecutará para estas ramas.
- Se admiten comodines como `*` (cero o más caracteres) y `?` (un solo carácter). Ponga entre comillas los patrones que comiencen con `*` (ej., `*-hotfix`).

### Paso 3: Inclusión/Exclusión avanzada
Para exclusiones o más precisión:
```yaml
trigger:
  branches:
    include:
    - main
    - releases/*
    - feature/*
    exclude:
    - releases/old-*     # Excluye 'releases/old-v1', etc.
    - feature/*-draft    # Excluye características en borrador
```
- **Include**: Ramas que *pueden* activar (comienza con todas si se omite).
- **Exclude**: Filtra de la lista de inclusiones (se aplica después de los includes).
- Si especifica cualquier cláusula `branches`, anula el valor predeterminado (todas las ramas): solo las inclusiones explícitas activarán el pipeline.
- Para etiquetas: Use `refs/tags/v1.*` en los includes.

### Paso 4: Filtros de ruta (Opcional)
Combine con rutas de archivo para un control granular:
```yaml
trigger:
  branches:
    include:
    - main
  paths:
    include:
    - src/*.cs          # Solo si hay cambios en la carpeta 'src'
    exclude:
    - docs/*.md         # Ignora cambios en documentos
```
- Las rutas son relativas a la raíz del repositorio y distinguen entre mayúsculas y minúsculas.

### Paso 5: Procesamiento por lotes y exclusión voluntaria
- **Ejecuciones por lotes**: Para agrupar múltiples pushes en una sola compilación (reduce el ruido):
  ```yaml
  trigger:
    batch: true
    branches:
      include:
      - main
  ```
- **Desactivar desencadenadores**: Establezca `trigger: none` para no tener CI.
- **Omitir por commit**: Agregue `[skip ci]` o `***NO_CI***` a los mensajes de commit.

### Desencadenadores de PR
Para pull requests, agregue una sección `pr`:
```yaml
pr:
  branches:
    include:
    - main
    - develop
  paths:
    include:
    - src/*
```
- Esto valida los PRs dirigidos a estas ramas.

### Pruebas
- Haga un push a una rama que coincida: El pipeline se ejecuta automáticamente.
- Vea las ejecuciones en **Pipelines > Runs** y verifique los detalles del desencadenador.

## Pipelines Clásicos: Configurar desencadenadores de rama
Para pipelines clásicos/heredados (basados en UI):
1. Edite su pipeline en **Pipelines > Builds**.
2. Vaya a **Triggers > Continuous integration**.
3. Marque **Enable continuous integration**.
4. En **Branch filters**, agregue inclusiones (ej., `main`) o exclusiones (ej., `develop`).
5. Para rutas: Use **Path filters** en la misma pestaña.
6. Para PRs: Vaya a **Triggers > Pull request validation** y configure los filtros de rama.

Cambie a YAML para una mejor mantenibilidad.

## Mejores prácticas
- Comience de forma simple: Active solo en `main` y `develop`.
- Use exclusiones para ramas ruidosas como `*-hotfix`.
- Asegure con políticas de rama (Repos > Branches > Policies) para revisores requeridos.
- Monitoree: Use análisis de pipeline para la frecuencia de activación.

Para los detalles más recientes, consulte la documentación oficial.

[Compilar repositorios Git de Azure Repos](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/azure-repos-git?view=azure-devops&tabs=yaml)  
[Desencadenadores en Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/triggers?view=azure-devops&tabs=yaml)