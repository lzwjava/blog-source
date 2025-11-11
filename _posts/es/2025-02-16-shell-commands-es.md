---
audio: false
generated: true
image: false
lang: es
layout: post
title: Comandos de Shell de macOS
translated: true
type: note
---

Aquí tienes 200 comandos de shell para macOS de uso común, categorizados para una referencia más fácil. Estos comandos son útiles para navegar por el sistema de archivos, gestionar archivos, monitorear el sistema y más.

### Navegación en el Sistema de Archivos
- `ls` - Listar el contenido del directorio.
- `cd` - Cambiar el directorio actual.
- `pwd` - Mostrar el directorio de trabajo actual.
- `tree` - Mostrar directorios como árboles (si está instalado).

### Operaciones con Archivos
- `cp` - Copiar archivos o directorios.
- `mv` - Mover o renombrar archivos o directorios.
- `rm` - Eliminar archivos o directorios.
- `touch` - Crear un archivo vacío o actualizar su marca de tiempo.
- `mkdir` - Crear un nuevo directorio.
- `rmdir` - Eliminar un directorio vacío.
- `ln` - Crear enlaces físicos y simbólicos.
- `chmod` - Cambiar los permisos de un archivo.
- `chown` - Cambiar el propietario y grupo de un archivo.
- `cat` - Concatenar y mostrar el contenido de un archivo.
- `less` - Ver el contenido de un archivo página por página.
- `more` - Ver el contenido de un archivo página por página.
- `head` - Mostrar las primeras líneas de un archivo.
- `tail` - Mostrar las últimas líneas de un archivo.
- `nano` - Editar archivos de texto.
- `vi` - Editar archivos de texto.
- `vim` - Editar archivos de texto (versión mejorada de `vi`).
- `find` - Buscar archivos en una jerarquía de directorios.
- `locate` - Encontrar archivos por nombre rápidamente.
- `grep` - Buscar texto usando patrones.
- `diff` - Comparar archivos línea por línea.
- `file` - Determinar el tipo de archivo.
- `stat` - Mostrar el estado de un archivo o sistema de archivos.
- `du` - Estimar el uso de espacio de un archivo.
- `df` - Reportar el uso de espacio en disco del sistema de archivos.
- `dd` - Convertir y copiar un archivo.
- `tar` - Almacenar, listar o extraer archivos en un archivo.
- `gzip` - Comprimir o descomprimir archivos.
- `gunzip` - Descomprimir archivos comprimidos con gzip.
- `zip` - Empaquetar y comprimir archivos.
- `unzip` - Extraer archivos comprimidos en un archivo ZIP.
- `rsync` - Sincronización remota de archivos y directorios.
- `scp` - Copia segura de archivos entre hosts.
- `curl` - Transferir datos desde o hacia un servidor.
- `wget` - Descargar archivos de la web.

### Información del Sistema
- `uname` - Imprimir información del sistema.
- `top` - Mostrar procesos del sistema.
- `htop` - Visor interactivo de procesos (si está instalado).
- `ps` - Reportar una instantánea de los procesos actuales.
- `kill` - Enviar una señal a un proceso.
- `killall` - Terminar procesos por nombre.
- `bg` - Ejecutar trabajos en segundo plano.
- `fg` - Ejecutar trabajos en primer plano.
- `jobs` - Listar trabajos activos.
- `nice` - Ejecutar un programa con prioridad de planificación modificada.
- `renice` - Alterar la prioridad de los procesos en ejecución.
- `time` - Cronometrar la ejecución de un comando.
- `uptime` - Mostrar cuánto tiempo ha estado funcionando el sistema.
- `who` - Mostrar quién ha iniciado sesión.
- `w` - Mostrar quién ha iniciado sesión y qué están haciendo.
- `whoami` - Imprimir el nombre del usuario actual.
- `id` - Imprimir información del usuario y grupo.
- `groups` - Imprimir los grupos a los que pertenece un usuario.
- `passwd` - Cambiar la contraseña de usuario.
- `sudo` - Ejecutar un comando como otro usuario.
- `su` - Cambiar de usuario.
- `chroot` - Ejecutar un comando con un directorio raíz diferente.
- `hostname` - Mostrar o establecer el nombre de host del sistema.
- `ifconfig` - Configurar una interfaz de red.
- `ping` - Enviar ICMP ECHO_REQUEST a hosts de la red.
- `traceroute` - Rastrear la ruta a un host de la red.
- `netstat` - Estadísticas de red.
- `route` - Mostrar o manipular la tabla de enrutamiento IP.
- `dig` - Utilidad de búsqueda DNS.
- `nslookup` - Consultar servidores de nombres de Internet interactivamente.
- `host` - Utilidad de búsqueda DNS.
- `ftp` - Programa de transferencia de archivos por Internet.
- `ssh` - Cliente SSH de OpenSSH.
- `telnet` - Interfaz de usuario para el protocolo TELNET.
- `nc` - Netcat, conexiones y escuchas arbitrarias TCP y UDP.
- `iftop` - Mostrar el uso de ancho de banda en una interfaz (si está instalado).
- `nmap` - Herramienta de exploración de red y escáner de puertos/seguridad (si está instalado).

### Gestión de Discos
- `mount` - Montar un sistema de archivos.
- `umount` - Desmontar un sistema de archivos.
- `fdisk` - Manipulador de tabla de particiones para Linux.
- `mkfs` - Construir un sistema de archivos Linux.
- `fsck` - Comprobar y reparar un sistema de archivos Linux.
- `df` - Reportar el uso de espacio en disco del sistema de archivos.
- `du` - Estimar el uso de espacio de un archivo.
- `sync` - Sincronizar escrituras en caché al almacenamiento persistente.
- `dd` - Convertir y copiar un archivo.
- `hdparm` - Obtener/establecer parámetros del disco duro.
- `smartctl` - Controlar y monitorear unidades ATA/SCSI-3 con SMART habilitado (si está instalado).

### Gestión de Paquetes
- `brew` - Gestor de paquetes Homebrew (si está instalado).
- `port` - Gestor de paquetes MacPorts (si está instalado).
- `gem` - Gestor de paquetes RubyGems.
- `pip` - Instalador de paquetes Python.
- `npm` - Gestor de paquetes Node.js.
- `cpan` - Gestor de paquetes Perl.

### Procesamiento de Texto
- `awk` - Lenguaje de procesamiento y escaneo de patrones.
- `sed` - Editor de flujo para filtrar y transformar texto.
- `sort` - Ordenar líneas de archivos de texto.
- `uniq` - Reportar u omitir líneas repetidas.
- `cut` - Eliminar secciones de cada línea de los archivos.
- `paste` - Unir líneas de archivos.
- `join` - Unir líneas de dos archivos en un campo común.
- `tr` - Traducir o eliminar caracteres.
- `iconv` - Convertir texto de una codificación a otra.
- `strings` - Encontrar cadenas imprimibles en archivos.
- `wc` - Imprimir recuentos de líneas nuevas, palabras y bytes para cada archivo.
- `nl` - Numerar líneas de archivos.
- `od` - Volcar archivos en varios formatos.
- `xxd` - Hacer un volcado hexadecimal o lo inverso.

### Scripting de Shell
- `echo` - Mostrar una línea de texto.
- `printf` - Formatear e imprimir datos.
- `test` - Evaluar una expresión.
- `expr` - Evaluar expresiones.
- `read` - Leer una línea desde la entrada estándar.
- `export` - Establecer una variable de entorno.
- `unset` - Anular valores y atributos de variables y funciones del shell.
- `alias` - Crear un alias para un comando.
- `unalias` - Eliminar un alias.
- `source` - Ejecutar comandos desde un archivo en el shell actual.
- `exec` - Ejecutar un comando.
- `trap` - Capturar señales y otros eventos.
- `set` - Establecer o anular opciones del shell y parámetros posicionales.
- `shift` - Desplazar parámetros posicionales.
- `getopts` - Analizar parámetros posicionales.
- `type` - Describir un comando.
- `which` - Localizar un comando.
- `whereis` - Localizar los archivos binarios, fuente y de manual de un comando.

### Herramientas de Desarrollo
- `gcc` - Compilador C y C++ del proyecto GNU.
- `make` - Procesador de makefile orientado a directorios.
- `cmake` - Generador de makefiles multiplataforma.
- `autoconf` - Generar scripts de configuración.
- `automake` - Generar archivos Makefile.in.
- `ld` - El enlazador GNU.
- `ar` - Crear, modificar y extraer de archivos.
- `nm` - Listar símbolos de archivos objeto.
- `objdump` - Mostrar información de archivos objeto.
- `strip` - Descartar símbolos de archivos objeto.
- `ranlib` - Generar índice para archivo.
- `gdb` - El depurador GNU.
- `lldb` - El depurador LLVM.
- `valgrind` - Marco de instrumentación para construir herramientas de análisis dinámico (si está instalado).
- `strace` - Rastrear llamadas al sistema y señales (si está instalado).
- `ltrace` - Rastrear llamadas a bibliotecas (si está instalado).
- `perf` - Herramientas de análisis de rendimiento para Linux.
- `time` - Cronometrar la ejecución de un comando.
- `xargs` - Construir y ejecutar líneas de comando desde la entrada estándar.
- `m4` - Procesador de macros.
- `cpp` - El Preprocesador C.
- `flex` - Generador de Analizadores Léxicos Rápidos.
- `bison` - Generador de analizadores sintácticos compatible con Yacc.
- `bc` - Un lenguaje de calculadora de precisión arbitraria.
- `dc` - Una calculadora de precisión arbitraria.

### Control de Versiones
- `git` - Sistema de control de versiones distribuido.
- `svn` - Sistema de control de versiones Subversion.
- `hg` - Sistema de control de versiones distribuido Mercurial.
- `cvs` - Sistema de Versiones Concurrentes.

### Misceláneos
- `man` - Formatear y mostrar las páginas del manual en línea.
- `info` - Leer documentos Info.
- `apropos` - Buscar en los nombres y descripciones de las páginas del manual.
- `whatis` - Mostrar descripciones de una línea de las páginas del manual.
- `history` - Mostrar o manipular la lista del historial.
- `yes` - Output una cadena repetidamente hasta ser terminado.
- `cal` - Mostrar un calendario.
- `date` - Mostrar o establecer la fecha y hora.
- `sleep` - Retrasar durante una cantidad de tiempo especificada.
- `watch` - Ejecutar un programa periódicamente, mostrando la salida a pantalla completa.
- `xargs` - Construir y ejecutar líneas de comando desde la entrada estándar.
- `seq` - Imprimir una secuencia de números.
- `shuf` - Generar permutaciones aleatorias.
- `tee` - Leer desde la entrada estándar y escribir en la salida estándar y archivos.
- `tput` - Inicializar una terminal o consultar la base de datos terminfo.
- `stty` - Cambiar e imprimir la configuración de línea de la terminal.
- `clear` - Limpiar la pantalla de la terminal.
- `reset` - Restablecer la terminal a un estado sensato.
- `script` - Hacer un registro de la sesión de terminal.
- `wall` - Escribir un mensaje a todos los usuarios.
- `write` - Enviar un mensaje a otro usuario.
- `mesg` - Controlar el acceso de escritura a tu terminal.
- `talk` - Hablar con otro usuario.
- `ytalk` - Otro programa de talk (si está instalado).
- `crontab` - Mantener archivos crontab para usuarios individuales.
- `at` - Programar comandos para ejecutarse una vez en un momento posterior.
- `batch` - Programar comandos para ejecutarse en una cola por lotes.
- `nice` - Ejecutar un programa con prioridad de planificación modificada.
- `renice` - Alterar la prioridad de los procesos en ejecución.
- `time` - Cronometrar la ejecución de un comando.
- `ulimit` - Establecer o reportar límites de recursos del usuario.
- `pr` - Convertir archivos de texto para imprimir.
- `lp` - Enviar archivos a una impresora.
- `lpr` - Imprimir archivos.
- `lpq` - Mostrar el estado de la cola de impresión.
- `lprm` - Eliminar trabajos de la cola de impresión.
- `enscript` - Convertir texto a PostScript, HTML o RTF, con resaltado de sintaxis (si está instalado).
- `a2ps` - Filtro de cualquier formato a PostScript.
- `ps2pdf` - Convertir PostScript a PDF.
- `pdf2ps` - Convertir PDF a PostScript.
- `gs` - Intérprete de Ghostscript.
- `convert` - Convertir entre formatos de imagen (si está instalado).
- `mogrify` - Redimensionar, rotar y transformar imágenes (si está instalado).
- `exiftool` - Leer, escribir y editar metainformación en archivos (si está instalado).
- `jpegoptim` - Optimizar archivos JPEG (si está instalado).
- `optipng` - Optimizar archivos PNG (si está instalado).

Estos comandos cubren una amplia gama de funcionalidades y son esenciales para los usuarios que desean gestionar e interactuar de manera eficiente con su sistema macOS a través de la terminal.