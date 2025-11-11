---
audio: false
generated: true
lang: es
layout: post
title: Guía de Control de Código Fuente de VS Code
translated: true
type: note
---

Visual Studio Code (VS Code) tiene un soporte integrado robusto para el control de código fuente, permitiendo a los desarrolladores gestionar sistemas de control de versiones (VCS) como Git, Mercurial y otros directamente dentro del editor. Esta guía proporciona una descripción general completa del uso del control de código fuente en VS Code, centrándose en Git, ya que es el VCS más utilizado, y cubre la configuración, características clave, flujos de trabajo y uso avanzado.

### Descripción General del Control de Código Fuente en VS Code
La vista de Control de Código Fuente de VS Code proporciona una interfaz intuitiva para interactuar con los sistemas de control de versiones. Se integra con Git por defecto y admite extensiones para otros VCS. La vista de Control de Código Fuente muestra los cambios, permite el staging, commit, branching, merging y más, todo sin salir del editor. A continuación, se presenta una guía paso a paso para aprovechar el control de código fuente de manera efectiva.

### 1. **Configurar el Control de Código Fuente en VS Code**
Para usar el control de código fuente, necesitas tener Git instalado y un repositorio inicializado. Así es como se configura:

#### Prerrequisitos
- **Instalar Git**: Descarga e instala Git desde [git-scm.com](https://git-scm.com/). Verifica la instalación ejecutando `git --version` en una terminal.
- **Configurar Git**:
  ```bash
  git config --global user.name "Tu Nombre"
  git config --global user.email "tu.email@ejemplo.com"
  ```
- **Instalar VS Code**: Asegúrate de tener la última versión de VS Code instalada desde [code.visualstudio.com](https://code.visualstudio.com/).

#### Inicializar un Repositorio Git
1. Abre una carpeta de proyecto en VS Code.
2. Abre la Terminal (Ctrl+` o Cmd+` en macOS) y ejecuta:
   ```bash
   git init
   ```
   Esto crea una carpeta `.git` en tu proyecto, inicializándolo como un repositorio Git.
3. Alternativamente, clona un repositorio existente:
   ```bash
   git clone <url-del-repositorio>
   ```
   Luego abre la carpeta clonada en VS Code.

#### Habilitar la Vista de Control de Código Fuente
- Abre la vista de Control de Código Fuente haciendo clic en el icono de Control de Código Fuente en la Barra de Actividad (tercer icono desde la parte superior, que se asemeja a una rama) o presionando `Ctrl+Shift+G` (Windows/Linux) o `Cmd+Shift+G` (macOS).
- Si se detecta un repositorio Git, VS Code muestra la vista de Control de Código Fuente con opciones para gestionar los cambios.

### 2. **Usar la Vista de Control de Código Fuente**
La vista de Control de Código Fuente es el centro central para las tareas de control de versiones. Muestra:
- **Cambios**: Archivos modificados, agregados o eliminados desde el último commit.
- **Cambios Preparados (Staged)**: Archivos listos para ser confirmados (committed).
- **Caja de Mensaje de Commit**: Donde introduces los mensajes de commit.
- **Acciones**: Botones para confirmar (commit), actualizar y más.

#### Flujo de Trabajo Común
1. **Realizar Cambios**: Edita archivos en tu proyecto. VS Code detecta automáticamente los cambios y los lista bajo "Cambios" en la vista de Control de Código Fuente.
2. **Preparar Cambios (Stage)**:
   - Haz clic en el icono `+` junto a un archivo para prepararlo (stage), o usa la opción `Preparar Todos los Cambios` (menú de tres puntos > Preparar Todos los Cambios).
   - Preparar (staging) los cambios los deja listos para el próximo commit.
3. **Escribir un Mensaje de Commit**:
   - Introduce un mensaje descriptivo en el cuadro de texto en la parte superior de la vista de Control de Código Fuente.
   - Ejemplo: `Agregar función de autenticación de usuario`.
4. **Confirmar Cambios (Commit)**:
   - Haz clic en el icono de marca de verificación o presiona `Ctrl+Enter` (Windows/Linux) o `Cmd+Enter` (macOS) para confirmar los cambios preparados.
   - Usa el menú de tres puntos para elegir entre `Confirmar Todo`, `Confirmar Preparados` o `Confirmar Todo y Empujar (Push)`.
5. **Empujar al Repositorio Remoto (Push)**:
   - Si estás conectado a un repositorio remoto (ej., GitHub), empuja los cambios usando la opción `Empujar (Push)` en el menú de tres puntos o ejecuta `git push` en la terminal.

### 3. **Características Clave del Control de Código Fuente en VS Code**
VS Code proporciona varias características para optimizar el control de versiones:

#### Vista de Diferencias (Diff View)
- Haz clic en un archivo bajo "Cambios" para abrir una vista de diferencias lado a lado, mostrando las modificaciones comparadas con el último commit.
- Usa las acciones en línea para preparar (stage) o descartar líneas específicas.

#### Gestión de Ramas (Branching)
- Cambiar de rama: Haz clic en el nombre de la rama en la barra de estado inferior izquierda o usa el menú de ramas de la vista de Control de Código Fuente (tres puntos > Rama > Checkout to...).
- Crear una nueva rama: Selecciona `Crear Rama` desde el menú de ramas, introduce un nombre y confirma.
- Fusionar ramas (Merge): Usa `Rama > Fusionar Rama` y selecciona la rama que quieres fusionar en la actual.

#### Pull y Fetch
- **Pull**: Sincroniza los cambios desde el repositorio remoto usando la opción `Pull` en el menú de tres puntos.
- **Fetch**: Recupera los cambios remotos sin fusionarlos usando `Fetch`.

#### Resolver Conflictos
- Al fusionar (merge) o hacer pull, pueden surgir conflictos. VS Code resalta los conflictos en los archivos y proporciona una interfaz de resolución de conflictos en línea:
  - Elige `Aceptar Cambio Actual`, `Aceptar Cambio Entrante`, `Aceptar Ambos Cambios` o edita el archivo manualmente.
  - Prepara (stage) y confirma (commit) el archivo resuelto.

#### Extensión Git Lens
Para características avanzadas de Git, instala la extensión **GitLens**:
- Ver el historial de commits, anotaciones de blame (culpable) y cambios en archivos.
- Acceder a información del repositorio como commits recientes y stashes.
- Instálala a través de la vista de Extensiones (`Ctrl+Shift+X` o `Cmd+Shift+X`).

### 4. **Uso Avanzado**
#### Guardar Cambios Temporalmente (Stashing)
- Guarda cambios no confirmados temporalmente:
  - Ve al menú de tres puntos > Stash > Stash.
  - Aplica o recupera (pop) los stashes más tarde a través del mismo menú.
- Útil para cambiar de rama sin confirmar trabajo incompleto.

#### Comandos de Git en la Terminal
- Para tareas no soportadas directamente en la UI, usa la terminal integrada:
  ```bash
  git rebase <rama>
  git cherry-pick <commit>
  git log --oneline
  ```

#### Personalizar el Control de Código Fuente
- **Configuración**: Ajusta el comportamiento del control de código fuente en la configuración de VS Code (`Ctrl+,` o `Cmd+,`):
  - `git.autoRepositoryDetection`: Habilita/deshabilita la detección automática de repositorios Git.
  - `git.enableSmartCommit`: Confirma todos los cambios cuando no hay archivos preparados (staged).
- **Proveedores SCM**: Instala extensiones para otros VCS como Mercurial o SVN.

#### Integración con GitHub
- Usa la extensión **GitHub Pull Requests and Issues** para gestionar PRs e issues directamente en VS Code.
- Autentícate con GitHub a través del menú de Cuentas (esquina inferior izquierda) para empujar (push)/halar (pull) desde repositorios de GitHub.

### 5. **Flujo de Trabajo de Ejemplo: Crear y Empujar una Rama de Característica (Feature Branch)**
Aquí tienes un ejemplo práctico de un flujo de trabajo común de Git en VS Code:

# Flujo de Trabajo de Git de Ejemplo en VS Code

## Pasos para Crear y Empujar una Rama de Característica (Feature Branch)

1. **Crear una Nueva Rama**:
   - En la vista de Control de Código Fuente, haz clic en el nombre de la rama en la barra de estado o usa el menú de tres puntos > Rama > Crear Rama.
   - Nombra la rama, ej., `feature/agregar-login`.
   - VS Code cambia a la nueva rama.

2. **Realizar y Preparar Cambios (Stage)**:
   - Edita archivos (ej., agrega un componente de login a `src/Login.js`).
   - En la vista de Control de Código Fuente, los archivos aparecen bajo "Cambios".
   - Haz clic en el icono `+` para preparar los cambios o selecciona "Preparar Todos los Cambios".

3. **Confirmar Cambios (Commit)**:
   - Introduce un mensaje de commit, ej., `Agregar componente de login`.
   - Haz clic en la marca de verificación o presiona `Ctrl+Enter` (Windows/Linux) o `Cmd+Enter` (macOS) para confirmar.

4. **Empujar la Rama (Push)**:
   - Si no existe un remoto, agrégalo:
     ```bash
     git remote add origin <url-del-repositorio>
     ```
   - Empuja la rama: Menú de tres puntos > Empujar (Push), o ejecuta:
     ```bash
     git push -u origin feature/agregar-login
     ```

5. **Crear una Pull Request**:
   - Si usas GitHub, abre el repositorio en un navegador o usa la extensión GitHub Pull Requests para crear una PR.
   - Vincula la PR a la rama `feature/agregar-login`.

## Consejos
- Haz pull de las actualizaciones de la rama principal regularmente para evitar conflictos.
- Usa mensajes de commit descriptivos para una mejor colaboración.
- Instala GitLens para vistas mejoradas del historial de commits y blame.

### 6. **Solución de Problemas Comunes**
- **Git No Detectado**: Asegúrate de que Git esté instalado y agregado a la variable de entorno PATH de tu sistema. Reinicia VS Code después de la instalación.
- **Errores de Autenticación**: Configura claves SSH o usa un token de acceso personal para GitHub/GitLab. Autentícate a través del menú de Cuentas.
- **Conflictos de Fusión (Merge Conflicts)**: Usa las herramientas de resolución de conflictos en línea o edita los archivos manualmente, luego prepáralos (stage) y confírmalos (commit).
- **Rendimiento Lento**: Deshabilita `git.autoRepositoryDetection` para proyectos grandes o usa GitLens para operaciones Git optimizadas.

### 7. **Mejores Prácticas**
- **Confirma (Commit) Seguido**: Realiza commits pequeños y lógicos para rastrear el progreso.
- **Usa Mensajes Descriptivos**: Sigue una convención como `<tipo>(<alcance>): <descripción>` (ej., `feat(auth): agregar endpoint de login`).
- **Haz Pull Regularmente**: Mantente sincronizado con el repositorio remoto para minimizar conflictos.
- **Respaldos de Stashes**: Antes de aplicar stashes, asegúrate de que no sobrescribirán cambios importantes.
- **Aprovecha las Extensiones**: Usa GitLens, Git History o Git Graph para una funcionalidad mejorada.

### 8. **Recursos Adicionales**
- **Documentación de VS Code**: [Control de Versiones en VS Code](https://code.visualstudio.com/docs/editor/versioncontrol)
- **Documentación de Git**: [git-scm.com/doc](https://git-scm.com/doc)
- **Extensión GitLens**: Disponible en el Marketplace de VS Code.
- **Extensión GitHub Pull Requests**: Para gestionar PRs e issues.

Esta guía cubre los aspectos esenciales y las características avanzadas del control de código fuente en VS Code, con un enfoque en Git. Siguiendo estos pasos y mejores prácticas, puedes gestionar eficientemente los flujos de trabajo de control de versiones directamente dentro del editor.