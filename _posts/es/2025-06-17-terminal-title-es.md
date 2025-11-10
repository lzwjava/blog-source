---
audio: false
generated: true
lang: es
layout: post
title: Terminal de GNOME con Directorio Personalizado
translated: true
type: note
---

Para personalizar el título de la pestaña de GNOME Terminal para mostrar solo el directorio actual (por ejemplo, `blog-server`) en lugar del formato predeterminado (por ejemplo, `lzw@lzw-MS:~/Projects/blog-server`), puedes modificar la configuración del prompt o del título del terminal. Aquí te explicamos cómo lograrlo:

### Pasos para configurar el título de la pestaña de GNOME Terminal para mostrar solo el directorio actual

1. **Editar el archivo de configuración de Bash**:
   GNOME Terminal usa el shell Bash por defecto, y el título de la pestaña a menudo se deriva de la variable `PS1` (prompt) o de un comando específico para establecer el título. Para personalizar el título, puedes modificar el archivo `~/.bashrc`.

2. **Modificar el título del terminal**:
   Añade un comando para establecer el título del terminal al directorio actual en tu `~/.bashrc`. Abre el archivo en un editor de texto:

   ```bash
   nano ~/.bashrc
   ```

   Añade las siguientes líneas al final del archivo:

   ```bash
   # Establecer el título de la pestaña del terminal al directorio actual
   case "$TERM" in
   xterm*|rxvt*)
       PS1="\[\e]0;\W\a\]$PS1"
       ;;
   *)
       ;;
   esac
   ```

   **Explicación**:
   - `\e]0;...` establece el título del terminal.
   - `\W` representa el nombre base del directorio actual (por ejemplo, `blog-server` en lugar de la ruta completa `~/Projects/blog-server`).
   - `\a` es un carácter de campana para terminar la cadena del título.
   - Este código verifica si el terminal es compatible con `xterm` (como lo es GNOME Terminal) antes de aplicar el cambio.

3. **Aplicar los cambios**:
   Guarda el archivo y recarga la configuración de Bash:

   ```bash
   source ~/.bashrc
   ```

   Alternativamente, cierra y vuelve a abrir el terminal para aplicar los cambios.

4. **Verificar el resultado**:
   Navega a un directorio (por ejemplo, `cd ~/Projects/blog-server`), y el título de la pestaña del terminal ahora debería mostrar solo `blog-server`.

### Alternativa: Modificar la configuración del perfil de GNOME Terminal
Si deseas personalizar el título más a fondo o evitar editar `~/.bashrc`, puedes usar la configuración de perfiles de GNOME Terminal:

1. Abre GNOME Terminal.
2. Ve a **Editar** > **Preferencias** (o **Terminal** > **Preferencias**, dependiendo de tu versión).
3. Selecciona el perfil que estás usando (por ejemplo, "Unnamed" o un perfil personalizado).
4. Ve a la pestaña **Comando**.
5. En **Título y comando**, establece:
   - **Título inicial**: Déjalo en blanco o establece algo genérico.
   - **Cuando el comando termina**: Elige **Mantener el título inicial** o **Reemplazar con la salida del comando**.
6. En la sección **Comando**, habilita **Ejecutar un comando personalizado en lugar de mi shell** y establece el comando a:

   ```bash
   bash --rcfile <(echo '. ~/.bashrc; PS1="\[\e]0;\W\a\]$PS1"')
   ```

   Esto asegura que el terminal use un prompt personalizado que establece el título al directorio actual.

7. Cierra el diálogo y prueba abriendo una nueva pestaña o navegando a un directorio.

### Notas
- Si usas un shell diferente a Bash (por ejemplo, Zsh), necesitarás modificar el archivo de configuración equivalente (por ejemplo, `~/.zshrc`) y ajustar la sintaxis en consecuencia. Para Zsh, puedes añadir:

  ```zsh
  precmd() { echo -ne "\e]0;${PWD##*/}\a" }
  ```

- Si el título no se actualiza como se espera, asegúrate de que tu emulador de terminal sea compatible con `xterm` y de que ningún otro script (por ejemplo, configuraciones personalizadas de `PS1` en `~/.bashrc`) esté sobrescribiendo el título.
- Para cambios persistentes en todos los terminales, asegúrate de que la configuración esté en el perfil del shell del usuario o en la configuración de GNOME Terminal.

Esto debería darte un título de pestaña que muestre solo el nombre del directorio actual, como `blog-server`. ¡Avísame si necesitas más aclaraciones!