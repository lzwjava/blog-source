---
audio: false
generated: true
lang: es
layout: post
title: Configurar TortoiseGit como herramienta de fusión de Git
translated: true
type: note
---

Para configurar TortoiseGit como herramienta de fusión (merge tool) para Git, necesitas configurar TortoiseGitMerge (la herramienta de fusión incluida con TortoiseGit) en tu configuración de Git. A continuación se detallan los pasos para lograrlo:

### Prerrequisitos
- Asegúrate de que TortoiseGit esté instalado en tu sistema. Puedes descargarlo desde [tortoisegit.org](https://tortoisegit.org).
- Verifica que el ejecutable TortoiseGitMerge esté disponible (normalmente se encuentra en `C:\Program Files\TortoiseGit\bin\TortoiseGitMerge.exe`).

### Pasos para Configurar TortoiseGitMerge como Git Mergetool

1. **Abre un Símbolo del Sistema o Git Bash**
   - Puedes usar el Símbolo del sistema de Windows, PowerShell o Git Bash para ejecutar los comandos de configuración de Git necesarios.

2. **Establece TortoiseGitMerge como la Herramienta de Fusión**
   Ejecuta los siguientes comandos para configurar Git para que use TortoiseGitMerge:

   ```bash
   git config --global merge.tool tortoisegitmerge
   git config --global mergetool.tortoisemerge.cmd "\"C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe\" -base:\"$BASE\" -theirs:\"$REMOTE\" -mine:\"$LOCAL\" -merged:\"$MERGED\""
   ```

   **Explicación**:
   - `merge.tool tortoisegitmerge`: Establece el nombre de la herramienta de fusión como `tortoisegitmerge` (puedes elegir cualquier nombre, pero esta es una convención).
   - `mergetool.tortoisemerge.cmd`: Especifica el comando para ejecutar TortoiseGitMerge con los parámetros apropiados:
     - `-base:"$BASE"`: El archivo ancestro común.
     - `-theirs:"$REMOTE"`: El archivo de la rama que se está fusionando.
     - `-mine:"$LOCAL"`: El archivo de tu rama actual.
     - `-merged:"$MERGED"`: El archivo de salida donde se guardará la fusión resuelta.
   - Usa barras inclinadas hacia adelante (`/`) en la ruta y escapa las comillas según sea necesario, especialmente si la ruta contiene espacios.

   **Nota**: Ajusta la ruta (`C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe`) si TortoiseGit está instalado en una ubicación diferente (por ejemplo, `E:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe`).

3. **Opcional: Desactivar el Aviso de Mergetool**
   Para evitar que se te pregunte cada vez que ejecutas `git mergetool`, puedes desactivar el aviso:

   ```bash
   git config --global mergetool.prompt false
   ```

4. **Opcional: Asegurar que TortoiseGitMerge esté en la Ruta del Sistema (PATH)**
   Si Git no puede encontrar TortoiseGitMerge, asegúrate de que su directorio esté en la variable de entorno PATH de tu sistema:
   - Haz clic derecho en "Este equipo" o "Mi PC" → Propiedades → Configuración avanzada del sistema → Variables de entorno.
   - En "Variables del sistema", busca y edita la variable `Path` para incluir `C:\Program Files\TortoiseGit\bin`.
   - Alternativamente, establece la ruta explícitamente en la configuración de Git:

     ```bash
     git config --global mergetool.tortoisemerge.path "C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe"
     ```

5. **Probar la Configuración**
   - Crea un conflicto de fusión en un repositorio Git (por ejemplo, fusionando dos ramas con cambios conflictivos).
   - Ejecuta el siguiente comando para lanzar la herramienta de fusión:

     ```bash
     git mergetool
     ```

   - TortoiseGitMerge debería abrirse, mostrando una vista de tres paneles con las versiones base, theirs y mine del archivo en conflicto. El panel inferior es el resultado fusionado.

6. **Resolver Conflictos en TortoiseGitMerge**
   - En la vista de tres paneles, TortoiseGitMerge muestra:
     - **Panel izquierdo**: La versión "theirs" (de la rama que se está fusionando).
     - **Panel derecho**: La versión "mine" (de tu rama actual).
     - **Panel central**: La versión base (ancestro común).
     - **Panel inferior**: El resultado fusionado donde resuelves los conflictos.
   - Haz clic derecho en las secciones conflictivas para elegir opciones como "Usar bloque de texto de 'theirs'", "Usar bloque de texto de 'mine'", o edita manualmente el archivo fusionado.
   - Una vez resuelto, guarda el archivo (Archivo → Guardar) y cierra TortoiseGitMerge.
   - Git marcará el archivo como resuelto si TortoiseGitMerge sale exitosamente (código de salida 0). Si se te solicita, confirma para marcar el conflicto como resuelto.

7. **Confirmar (Commit) la Fusión Resuelta**
   Después de resolver los conflictos, confirma los cambios:

   ```bash
   git commit
   ```

   **Nota**: Si el conflicto ocurrió durante un rebase o cherry-pick, usa los diálogos respectivos de TortoiseGit (Rebase o Cherry-pick) para continuar el proceso en lugar del diálogo de confirmación estándar.[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-conflicts.html)

### Usar TortoiseGitMerge mediante la GUI de TortoiseGit
Si prefieres usar la GUI de TortoiseGit para resolver conflictos:
1. Haz clic derecho en el archivo en conflicto en el Explorador de Windows.
2. Selecciona **TortoiseGit → Editar Conflictos**.
3. TortoiseGitMerge se abrirá, permitiéndote resolver los conflictos como se describió anteriormente.
4. Después de guardar, haz clic derecho nuevamente y selecciona **TortoiseGit → Resuelto** para marcar el archivo como resuelto.
5. Confirma los cambios usando el diálogo de Confirmar (Commit) de TortoiseGit.

### Resolución de Problemas
- **Error: "Unsupported merge tool 'tortoisemerge'"**
  - Asegúrate de que la ruta a `TortoiseGitMerge.exe` sea correcta y accesible.
  - Verifica que el nombre de la herramienta coincida exactamente en las configuraciones `merge.tool` y `mergetool.<tool>.cmd`.
  - Comprueba que TortoiseGitMerge esté en el PATH o establecido explícitamente usando `mergetool.tortoisemerge.path`.[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)
- **Espacios en las Rutas de Archivo**
  - Si las rutas de archivo contienen espacios, la sintaxis del comando con comillas escapadas (como se muestra arriba) debería manejarlas correctamente.[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)
- **Usuarios de Cygwin**
  - Si usas Cygwin, ajusta la ruta para usar el punto de montaje de Cygwin, por ejemplo:

    ```bash
    git config --global mergetool.tortoisemerge.cmd '"/cygdrive/c/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe" -base:"$BASE" -theirs:"$REMOTE" -mine:"$LOCAL" -merged:"$MERGED"'
    ```

    Esto tiene en cuenta la estructura de ruta `/cygdrive/c/` de Cygwin.[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)
- **TortoiseGitMerge No Encontrado**
  - Si usaste anteriormente TortoiseMerge de TortoiseSVN, asegúrate de que estás apuntando a `TortoiseGitMerge.exe`, ya que el nombre del ejecutable cambió en TortoiseGit versión 1.8.[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)[](https://stackoverflow.com/questions/15881449/why-doesnt-tortoisemerge-work-as-my-mergetool)

### Notas Adicionales
- TortoiseGitMerge soporta una vista de tres paneles para la resolución de conflictos, lo cual es ideal para fusionar. Fusiona automáticamente los cambios no conflictivos y resalta los conflictos para su resolución manual.[](https://tortoisegit.org/docs/tortoisegitmerge/tmerge-dug.html)[](https://manios.org/2018/05/30/git-merge-conflicts-using-tortoise-git-merge-windows)
- Si también quieres usar TortoiseGitMerge como herramienta de diferencias (diff tool), configúrala de manera similar:

  ```bash
  git config --global diff.tool tortoisediff
  git config --global difftool.tortoisediff.cmd "\"C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe\" -mine:\"$REMOTE\" -base:\"$LOCAL\""
  ```

  Luego usa `git difftool` para comparar archivos.[](https://stackoverflow.com/questions/16493368/can-tortoisemerge-be-used-as-a-difftool-with-windows-git-bash)
- Para configuraciones avanzadas, puedes configurar TortoiseGit para que espere a que la herramienta de fusión se cierre y marque automáticamente los archivos como resueltos basándose en el código de salida. En Configuración de TortoiseGit → Programas Externos → Herramienta de Fusión, selecciona "Bloquear TortoiseGit mientras se ejecuta la herramienta de fusión externa" y habilita "Confiar en el código de salida."[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-settings.html)

### Fuentes
- Documentación de TortoiseGit:[](https://tortoisegit.org/docs/tortoisegitmerge/tmerge-dug.html)[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-merge.html)[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-conflicts.html)
- Stack Overflow y otros recursos web:[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)[](https://stackoverflow.com/questions/16493368/can-tortoisemerge-be-used-as-a-difftool-with-windows-git-bash)

Siguiendo estos pasos, deberías poder usar TortoiseGitMerge como tu herramienta de fusión de Git efectivamente, ya sea desde la línea de comandos o mediante la GUI de TortoiseGit.