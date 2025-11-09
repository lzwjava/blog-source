---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Conceptos Básicos del Editor Vi para Red Hat Linux
translated: true
type: note
---

Vi es un editor de texto potente y orientado al teclado que es estándar en sistemas Linux, incluido Red Hat Enterprise Linux (RHEL). Es ligero y eficiente para editar archivos de configuración, scripts y más. En Red Hat, el comando `vi` típicamente apunta a `vim` (Vi IMproved), que añade características como resaltado de sintaxis. Esta guía cubre lo básico para principiantes.

## Instalación
Vi viene preinstalado en la mayoría de los sistemas Red Hat. Si necesitas el paquete completo de `vim` (o si falta), instálalo mediante el gestor de paquetes:

- Para RHEL 7/8:  
  ```
  sudo yum install vim
  ```

- Para RHEL 9+:  
  ```
  sudo dnf install vim
  ```

Después de la instalación, puedes usar `vi` o `vim` indistintamente.

## Iniciar Vi
1. Abre una terminal.
2. Ejecuta `vi nombre_de_archivo.txt` (reemplaza `nombre_de_archivo.txt` con la ruta de tu archivo).  
   - Si el archivo existe, se abre para edición.  
   - Si no, se crea un nuevo archivo vacío.  
3. Para abrir sin un archivo (para practicar): `vi`.  
Vi inicia en **modo comando** (el predeterminado). Verás una pantalla en blanco o el contenido del archivo con un cursor en la parte superior izquierda.

## Entender los Modos
Vi tiene tres modos principales—cambiar entre ellos es clave:
- **Modo Comando**: Predeterminado para navegación, eliminación y la mayoría de las acciones. Presiona `Esc` para entrar/volver aquí desde otros modos.
- **Modo Inserción**: Para escribir/editar texto. Entra desde el modo comando (por ejemplo, presiona `i`).
- **Modo Ex**: Para comandos avanzados como guardar. Entra escribiendo `:` en el modo comando.

Los comandos distinguen entre mayúsculas y minúsculas. Prefija números para repetir acciones (por ejemplo, `3dd` elimina 3 líneas).

## Navegación Básica (en Modo Comando)
Usa las teclas de la fila central para mover el cursor—no se necesita el ratón:
- `h`: Izquierda un carácter
- `j`: Abajo una línea
- `k`: Arriba una línea
- `l`: Derecha un carácter
- `w`: Adelante una palabra
- `b`: Atrás una palabra
- `0` (cero): Inicio de la línea
- `$`: Fin de la línea
- `gg`: Parte superior del archivo
- `G`: Parte inferior del archivo
- `Ctrl + F`: Bajar una página
- `Ctrl + B`: Subir una página

## Entrar en Modo Inserción y Editar
Desde el modo comando, presiona uno de estos para cambiar al modo inserción y empezar a escribir:
- `i`: Insertar antes del cursor
- `I`: Insertar al inicio de la línea
- `a`: Añadir después del cursor
- `A`: Añadir al final de la línea
- `o`: Nueva línea debajo
- `O`: Nueva línea arriba

Para salir del modo inserción: Presiona `Esc` (volver al modo comando).

Comandos de edición comunes (en modo comando):
- **Eliminar**:
  - `x`: Eliminar carácter bajo el cursor
  - `X`: Eliminar carácter antes del cursor
  - `dd`: Eliminar línea actual
  - `dw`: Eliminar palabra actual
  - `D`: Eliminar hasta el final de la línea
- **Copiar (Yank)**:
  - `yy`: Copiar línea actual
  - `y`: Copiar selección (después de `v` para seleccionar)
- **Pegar**:
  - `p`: Pegar después del cursor
  - `P`: Pegar antes del cursor
- **Deshacer**:
  - `u`: Deshacer último cambio
  - `U`: Deshacer todos los cambios en la línea actual
- **Repetir**: `.` (repite el último comando)

## Guardar y Salir
Estos son **comandos Ex**—escribe `:` en el modo comando, luego el comando, y presiona `Enter`:
- `:w`: Guardar (escribir) cambios
- `:q`: Salir (si no hay cambios)
- `:wq` o `ZZ` (en modo comando): Guardar y salir
- `:q!`: Salir sin guardar (forzar descartar cambios)
- `:w nombre_de_archivo`: Guardar como nuevo archivo

Si estás atascado, `:q!` te saca de forma segura.

## Buscar y Reemplazar
- Buscar hacia adelante: `/patrón` (por ejemplo, `/error`), luego `n` para la siguiente coincidencia, `N` para la anterior.
- Buscar hacia atrás: `?patrón`.
- Reemplazar todo: `:%s/viejo/nuevo/g` (reemplazo global; añade `c` para confirmación, por ejemplo, `:%s/viejo/nuevo/gc`).

## Consejos para Usuarios de Red Hat
- Personaliza en `~/.vimrc` (crea si es necesario):  
  ```
  set number          # Mostrar números de línea
  syntax on           # Resaltado de sintaxis
  set tabstop=4       # Ancho de tabulación
  set autoindent      # Auto-sangrado
  ```
  Edita con `vi ~/.vimrc`, añade las líneas, luego `:wq`.
- Para múltiples archivos: `vi archivo1.txt archivo2.txt`, cambia con `:n` (siguiente) o `:prev` (anterior).
- Practica en un archivo de prueba para evitar errores en archivos del sistema.

Vi requiere práctica pero se vuelve intuitivo. ¡Comienza de forma simple y usa `Esc` a menudo!

## Referencias
[How to get started with the Vi editor - Red Hat](https://www.redhat.com/en/blog/get-started-vi-editor)  
[LFCS #2: How to Install and Use Vi/Vim as a Full Text Editor in Linux](https://www.tecmint.com/vi-editor-usage/)  
[vi Editor in Linux - GeeksforGeeks](https://www.geeksforgeeks.org/linux-unix/vi-editor-unix/)