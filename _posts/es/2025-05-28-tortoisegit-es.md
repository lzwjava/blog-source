---
audio: false
generated: true
lang: es
layout: post
title: TortoiseGit
translated: true
type: note
---

TortoiseGit es una extensión del shell de Windows que proporciona una interfaz de usuario para Git, el popular sistema de control de versiones. Se integra directamente en el Explorador de Windows, permitiéndole realizar operaciones de Git a través de menús contextuales. Esta guía cubre la instalación, configuración y uso de TortoiseGit en Windows, junto con tareas comunes y mejores prácticas.

### Descripción general de TortoiseGit
TortoiseGit está construido sobre msysGit (Git para Windows) y proporciona una interfaz gráfica para los comandos de Git. Es ideal para usuarios que prefieren una GUI sobre las operaciones de Git por línea de comandos. Las características clave incluyen:
- Integración de menús contextuales en el Explorador de Windows.
- Herramientas visuales de diff y merge.
- Soporte para flujos de trabajo comunes de Git (commit, push, pull, branch, merge, etc.).
- Integración con rastreadores de incidencias populares y herramientas externas.

### Prerrequisitos
Antes de instalar TortoiseGit, asegúrese de tener:
- Un sistema operativo Windows (se recomienda Windows 10 o posterior).
- Git para Windows instalado (TortoiseGit depende de él).
- Comprensión básica de los conceptos de Git (repositorios, commits, ramas, etc.).

### Instalación
1. **Instalar Git para Windows**:
   - Descargue la última versión desde [Git for Windows](https://gitforwindows.org/) o [Git SCM](https://git-scm.com/downloads).
   - Ejecute el instalador y siga las indicaciones. Configuración recomendada:
     - Use el editor predeterminado (por ejemplo, Bloc de notas) o elija uno como VS Code.
     - Seleccione "Usar Git desde el Símbolo del sistema de Windows" para accesibilidad.
     - Elija "OpenSSL" para el transporte HTTPS.
     - Seleccione "Checkout as-is, commit as-is" para los fines de línea (a menos que trabaje con equipos multiplataforma).
   - Complete la instalación.

2. **Instalar TortoiseGit**:
   - Descargue la última versión desde [el sitio web oficial de TortoiseGit](https://tortoisegit.org/download/).
   - Ejecute el instalador:
     - Elija el idioma y los componentes predeterminados.
     - Asegúrese de que Git para Windows sea detectado (TortoiseGit le avisará si falta).
     - Instale TortoiseGitPlink (recomendado para SSH) si es necesario.
   - Reinicie su computadora si se le solicita.

3. **Verificar la instalación**:
   - Haga clic con el botón derecho en cualquier carpeta en el Explorador de Windows. Debería ver opciones de TortoiseGit como "Git Clone", "Git Create Repository here", etc.

### Configuración inicial
Después de la instalación, configure TortoiseGit para sus datos de usuario y preferencias:
1. **Establecer información del usuario**:
   - Haga clic con el botón derecho en una carpeta, seleccione **TortoiseGit > Configuración**.
   - En la ventana de configuración, navegue a **Git > Config**.
   - Ingrese su nombre y correo electrónico (los mismos que usa en GitHub, GitLab, etc.):
     ```
     Name: Su Nombre
     Email: su.correo@ejemplo.com
     ```
   - Haga clic en **Aplicar** y **Aceptar**.

2. **Configurar SSH (Opcional)**:
   - Si usa SSH para repositorios remotos, configure una clave SSH:
     - Abra **PuTTYgen** (instalado con TortoiseGit).
     - Genere un nuevo par de claves SSH, guarde la clave privada y copie la clave pública.
     - Agregue la clave pública a su servicio de alojamiento de Git (por ejemplo, GitHub, GitLab).
     - En la configuración de TortoiseGit, en **Git > Remoto**, seleccione TortoiseGitPlink como el cliente SSH.

3. **Establecer herramientas Diff y Merge**:
   - En **TortoiseGit > Configuración > Visor de diferencias**, elija una herramienta como TortoiseGitMerge (predeterminada) o una herramienta externa como Beyond Compare.
   - Para la fusión, configure en **Herramienta de fusión** (TortoiseGitMerge es recomendable para principiantes).

### Uso básico
A continuación se presentan operaciones comunes de TortoiseGit, accesibles a través de menús contextuales al hacer clic con el botón derecho en el Explorador de Windows.

#### 1. **Clonar un repositorio**
   - Haga clic con el botón derecho en una carpeta y seleccione **Git Clone**.
   - En el cuadro de diálogo:
     - Ingrese la URL del repositorio (por ejemplo, `https://github.com/usuario/repo.git`).
     - Especifique el directorio local para el repositorio.
     - Opcionalmente, seleccione una rama o cargue las claves SSH.
   - Haga clic en **Aceptar** para clonar el repositorio.

#### 2. **Crear un nuevo repositorio**
   - Navegue a una carpeta, haga clic con el botón derecho y seleccione **Git Create Repository here**.
   - Marque "Make it Bare" si crea un repositorio del lado del servidor (poco común para uso local).
   - Haga clic en **Aceptar**. Se crea una carpeta `.git`, inicializando el repositorio.

#### 3. **Confirmar cambios**
   - Agregue archivos a la carpeta de su repositorio.
   - Haga clic con el botón derecho en la carpeta o en los archivos seleccionados, luego elija **Git Commit -> "main"** (o la rama actual).
   - En el cuadro de diálogo de confirmación:
     - Ingrese un mensaje de confirmación que describa los cambios.
     - Seleccione los archivos para staging (casillas de verificación).
     - Haga clic en **Aceptar** o **Commit & Push** para enviar los cambios al repositorio remoto.

#### 4. **Enviar cambios (Push)**
   - Después de confirmar, haga clic con el botón derecho y seleccione **TortoiseGit > Push**.
   - Elija el repositorio remoto y la rama.
   - Autentíquese si se le solicita (nombre de usuario/contraseña para HTTPS o clave SSH).
   - Haga clic en **Aceptar** para enviar.

#### 5. **Traer cambios (Pull)**
   - Para actualizar su repositorio local con cambios remotos, haga clic con el botón derecho y seleccione **TortoiseGit > Pull**.
   - Seleccione la rama remota y haga clic en **Aceptar**.
   - Resuelva los conflictos si se le solicita (use la herramienta de fusión).

#### 6. **Crear y cambiar de ramas**
   - Haga clic con el botón derecho y seleccione **TortoiseGit > Create Branch**.
   - Ingrese un nombre de rama y haga clic en **Aceptar**.
   - Para cambiar de rama, haga clic con el botón derecho y seleccione **TortoiseGit > Switch/Checkout**, luego elija la rama.

#### 7. **Ver el historial**
   - Haga clic con el botón derecho y seleccione **TortoiseGit > Show Log**.
   - Vea el historial de confirmaciones, incluido el autor, la fecha y los mensajes.
   - Haga clic con el botón derecho en una confirmación para ver los cambios, revertir o hacer cherry-pick.

#### 8. **Resolver conflictos de fusión**
   - Durante una operación de pull o merge, si ocurren conflictos, TortoiseGit le notificará.
   - Haga clic con el botón derecho en los archivos en conflicto y seleccione **TortoiseGit > Resolve**.
   - Use la herramienta de fusión para editar los conflictos manualmente, luego márquelos como resueltos.
   - Confirme los cambios resueltos.

### Características avanzadas
1. **Guardar cambios temporalmente (Stash)**:
   - Para guardar cambios no confirmados temporalmente, haga clic con el botón derecho y seleccione **TortoiseGit > Stash Save**.
   - Para recuperar los cambios guardados, seleccione **TortoiseGit > Stash Pop**.

2. **Reorganizar (Rebasing)**:
   - Haga clic con el botón derecho y seleccione **TortoiseGit > Rebase**.
   - Elija la rama sobre la cual reorganizar y siga las indicaciones para reordenar o combinar (squash) confirmaciones.

3. **Submódulos**:
   - Para gestionar submódulos, haga clic con el botón derecho y seleccione **TortoiseGit > Submodule Update** o **Add**.
   - Configure la configuración de los submódulos en la configuración de TortoiseGit.

4. **Búsqueda binaria (Bisecting)**:
   - Para encontrar una confirmación que introdujo un error, use **TortoiseGit > Bisect Start**.
   - Marque las confirmaciones como "good" o "bad" para localizar la confirmación problemática.

### Mejores prácticas
- **Confirmar a menudo**: Realice confirmaciones pequeñas y frecuentes con mensajes claros.
- **Hacer Pull regularmente**: Mantenga su repositorio local actualizado para evitar conflictos.
- **Usar ramas**: Cree ramas de características para nuevo trabajo para mantener estable la rama principal.
- **Hacer copia de seguridad de las claves SSH**: Almacene las claves SSH de forma segura y haga copias de seguridad.
- **Revisar cambios**: Use el visor de diferencias para revisar los cambios antes de confirmar.

### Resolución de problemas
- **Problemas de autenticación**: Asegúrese de que las claves SSH o las credenciales estén configuradas correctamente en su servicio de alojamiento de Git.
- **Conflictos de fusión**: Use TortoiseGitMerge para resolver conflictos visualmente. Haga una copia de seguridad de los archivos antes de fusionar.
- **Menú contextual faltante**: Compruebe si TortoiseGit está instalado correctamente y si la integración con el Explorador está habilitada en la configuración.
- **Rendimiento lento**: Desactive las superposiciones innecesarias en **TortoiseGit > Configuración > Icon Overlays**.

### Flujo de trabajo de ejemplo
A continuación se muestra un flujo de trabajo de ejemplo para contribuir a un proyecto:

# Flujo de trabajo de ejemplo con TortoiseGit

## 1. Clonar el repositorio
- Haga clic con el botón derecho en una carpeta, seleccione **Git Clone**.
- Ingrese la URL del repositorio y el directorio local.
- Haga clic en **Aceptar**.

## 2. Crear una rama de característica
- Haga clic con el botón derecho, seleccione **TortoiseGit > Create Branch**.
- Nombre la rama (por ejemplo, `feature/add-login`).
- Haga clic en **Aceptar** y cambie a la nueva rama.

## 3. Hacer cambios
- Edite archivos en la carpeta del repositorio.
- Haga clic con el botón derecho, seleccione **Git Commit -> "feature/add-login"**.
- Escriba un mensaje de confirmación y agregue los archivos al staging.
- Haga clic en **Commit**.

## 4. Enviar cambios
- Haga clic con el botón derecho, seleccione **TortoiseGit > Push**.
- Elija la rama remota (por ejemplo, `origin/feature/add-login`).
- Haga clic en **Aceptar**.

## 5. Crear una Pull Request
- En su servicio de alojamiento de Git (por ejemplo, GitHub), cree una pull request desde su rama a la rama principal.
- Espere la revisión y fusión.

## 6. Actualizar el repositorio local
- Cambie a la rama principal (**TortoiseGit > Switch/Checkout**).
- Traiga las actualizaciones (**TortoiseGit > Pull**).


### Recursos
- **Documentación oficial**: [Documentación de TortoiseGit](https://tortoisegit.org/docs/)
- **Git para Windows**: [Git SCM](https://git-scm.com/)
- **Tutoriales**: Busque "tutorial de TortoiseGit" en YouTube o blogs técnicos para guías visuales.

TortoiseGit simplifica las operaciones de Git con su interfaz intuitiva, haciendo que el control de versiones sea accesible para los usuarios de Windows. ¡Si necesita ayuda con tareas específicas o configuraciones avanzadas, hágamelo saber!