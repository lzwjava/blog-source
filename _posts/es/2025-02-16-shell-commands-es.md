---
audio: false
generated: true
lang: es
layout: post
title: Comandos de Shell de macOS
translated: true
---

Aquí tienes 200 comandos de shell de macOS comúnmente utilizados, categorizados para una referencia más fácil. Estos comandos son útiles para navegar por el sistema de archivos, gestionar archivos, monitorear el sistema y más.

### Navegación del Sistema de Archivos
- `ls` - Listar el contenido de un directorio.
- `cd` - Cambiar el directorio actual.
- `pwd` - Imprimir el directorio de trabajo actual.
- `tree` - Mostrar directorios como árboles (si está instalado).

### Operaciones de Archivos
- `cp` - Copiar archivos o directorios.
- `mv` - Mover o renombrar archivos o directorios.
- `rm` - Eliminar archivos o directorios.
- `touch` - Crear un archivo vacío o actualizar la marca de tiempo.
- `mkdir` - Crear un nuevo directorio.
- `rmdir` - Eliminar un directorio vacío.
- `ln` - Crear enlaces duros y simbólicos.
- `chmod` - Cambiar permisos de archivo.
- `chown` - Cambiar el propietario y el grupo de un archivo.
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
- `du` - Estimar el uso de espacio de archivos.
- `df` - Informar sobre el uso del espacio en disco del sistema de archivos.
- `dd` - Convertir y copiar un archivo.
- `tar` - Almacenar, listar o extraer archivos en un archivo.
- `gzip` - Comprimir o descomprimir archivos.
- `gunzip` - Descomprimir archivos comprimidos con gzip.
- `zip` - Empaquetar y comprimir archivos.
- `unzip` - Extraer archivos comprimidos en un archivo ZIP.
- `rsync` - Sincronización de archivos y directorios remotos.
- `scp` - Copiar archivos de manera segura entre hosts.
- `curl` - Transferir datos desde o hacia un servidor.
- `wget` - Descargar archivos de la web.

### Información del Sistema
- `uname` - Imprimir información del sistema.
- `top` - Mostrar procesos del sistema.
- `htop` - Visor de procesos interactivo (si está instalado).
- `ps` - Informar sobre una instantánea de los procesos actuales.
- `kill` - Enviar una señal a un proceso.
- `killall` - Matar procesos por nombre.
- `bg` - Ejecutar trabajos en segundo plano.
- `fg` - Ejecutar trabajos en primer plano.
- `jobs` - Listar trabajos activos.
- `nice` - Ejecutar un programa con prioridad de programación modificada.
- `renice` - Alterar la prioridad de los procesos en ejecución.
- `time` - Temporizar la ejecución de un comando.
- `uptime` - Mostrar cuánto tiempo ha estado funcionando el sistema.
- `who` - Mostrar quién está conectado.
- `w` - Mostrar quién está conectado y qué están haciendo.
- `whoami` - Imprimir el nombre de usuario actual.
- `id` - Imprimir información de usuario y grupo.
- `groups` - Imprimir los grupos a los que pertenece un usuario.
- `passwd` - Cambiar la contraseña de usuario.
- `sudo` - Ejecutar un comando como otro usuario.
- `su` - Cambiar de usuario.
- `chroot` - Ejecutar un comando con un directorio raíz diferente.
- `hostname` - Mostrar o establecer el nombre de host del sistema.
- `ifconfig` - Configurar una interfaz de red.
- `ping` - Enviar una solicitud de eco ICMP a hosts de red.
- `traceroute` - Rastrear la ruta a un host de red.
- `netstat` - Estadísticas de red.
- `route` - Mostrar o manipular la tabla de enrutamiento IP.
- `dig` - Utilidad de búsqueda DNS.
- `nslookup` - Consultar servidores de nombres de Internet de manera interactiva.
- `host` - Utilidad de búsqueda DNS.
- `ftp` - Programa de transferencia de archivos de Internet.
- `ssh` - Cliente SSH de OpenSSH.
- `telnet` - Interfaz de usuario del protocolo TELNET.
- `nc` - Netcat, conexiones y escuchas TCP y UDP arbitrarias.
- `iftop` - Mostrar el uso de ancho de banda en una interfaz (si está instalado).
- `nmap` - Herramienta de exploración de red y escáner de puertos de seguridad (si está instalado).

### Gestión de Discos
- `mount` - Montar un sistema de archivos.
- `umount` - Desmontar un sistema de archivos.
- `fdisk` - Manipulador de tabla de particiones para Linux.
- `mkfs` - Construir un sistema de archivos de Linux.
- `fsck` - Verificar y reparar un sistema de archivos de Linux.
- `df` - Informar sobre el uso del espacio en disco del sistema de archivos.
- `du` - Estimar el uso de espacio de archivos.
- `sync` - Sincronizar escrituras en caché con almacenamiento persistente.
- `dd` - Convertir y copiar un archivo.
- `hdparm` - Obtener/establecer parámetros de disco duro.
- `smartctl` - Controlar y monitorear unidades ATA/SCSI-3 habilitadas para SMART (si está instalado).

### Gestión de Paquetes
- `brew` - Gestor de paquetes Homebrew (si está instalado).
- `port` - Gestor de paquetes MacPorts (si está instalado).
- `gem` - Gestor de paquetes RubyGems.
- `pip` - Instalador de paquetes Python.
- `npm` - Gestor de paquetes Node.js.
- `cpan` - Gestor de paquetes Perl.

### Procesamiento de Texto
- `awk` - Lenguaje de escaneo y procesamiento de patrones.
- `sed` - Editor de flujo para filtrar y transformar texto.
- `sort` - Ordenar líneas de archivos de texto.
- `uniq` - Informar o omitir líneas repetidas.
- `cut` - Eliminar secciones de cada línea de archivos.
- `paste` - Fusionar líneas de archivos.
- `join` - Unir líneas de dos archivos en un campo común.
- `tr` - Traducir o eliminar caracteres.
- `iconv` - Convertir texto de una codificación a otra.
- `strings` - Encontrar cadenas imprimibles en archivos.
- `wc` - Imprimir recuentos de líneas, palabras y bytes para cada archivo.
- `nl` - Numerar líneas de archivos.
- `od` - Volcar archivos en varios formatos.
- `xxd` - Hacer un volcado hexadecimal o hacer lo contrario.

### Scripting de Shell
- `echo` - Mostrar una línea de texto.
- `printf` - Formatear e imprimir datos.
- `test` - Evaluar una expresión.
- `expr` - Evaluar expresiones.
- `read` - Leer una línea de la entrada estándar.
- `export` - Establecer una variable de entorno.
- `unset` - Anular valores y atributos de variables y funciones de shell.
- `alias` - Crear un alias para un comando.
- `unalias` - Eliminar un alias.
- `source` - Ejecutar comandos desde un archivo en la shell actual.
- `exec` - Ejecutar un comando.
- `trap` - Capturar señales y otros eventos.
- `set` - Establecer o anular opciones y parámetros de posición de shell.
- `shift` - Desplazar parámetros de posición.
- `getopts` - Analizar parámetros de posición.
- `type` - Describir un comando.
- `which` - Localizar un comando.
- `whereis` - Localizar los archivos binarios, fuente y manuales de un comando.

### Herramientas de Desarrollo
- `gcc` - Compilador C y C++ del proyecto GNU.
- `make` - Procesador de makefile orientado a directorios.
- `cmake` - Generador de makefile multiplataforma.
- `autoconf` - Generar scripts de configuración.
- `automake` - Generar archivos Makefile.in.
- `ld` - El enlazador de GNU.
- `ar` - Crear, modificar y extraer de archivos.
- `nm` - Listar símbolos de archivos de objeto.
- `objdump` - Mostrar información de archivos de objeto.
- `strip` - Descartar símbolos de archivos de objeto.
- `ranlib` - Generar índice de archivo.
- `gdb` - El depurador de GNU.
- `lldb` - El depurador de LLVM.
- `valgrind` - Marco de instrumentación para construir herramientas de análisis dinámico (si está instalado).
- `strace` - Rastrear llamadas del sistema y señales (si está instalado).
- `ltrace` - Rastrear llamadas de biblioteca (si está instalado).
- `perf` - Herramientas de análisis de rendimiento para Linux.
- `time` - Temporizar la ejecución de un comando.
- `xargs` - Construir y ejecutar líneas de comandos desde la entrada estándar.
- `m4` - Procesador de macros.
- `cpp` - El preprocesador de C.
- `flex` - Generador de analizador léxico rápido.
- `bison` - Generador de analizador compatible con Yacc.
- `bc` - Lenguaje de cálculo de precisión arbitraria.
- `dc` - Calculadora de precisión arbitraria.

### Control de Versiones
- `git` - Sistema de control de versiones distribuido.
- `svn` - Sistema de control de versiones Subversion.
- `hg` - Sistema de control de versiones distribuido Mercurial.
- `cvs` - Sistema de versiones concurrentes.

### Diversos
- `man` - Formatear y mostrar las páginas del manual en línea.
- `info` - Leer documentos Info.
- `apropos` - Buscar nombres y descripciones de páginas del manual.
- `whatis` - Mostrar descripciones de una línea de páginas del manual.
- `history` - Mostrar o manipular la lista de historial.
- `yes` - Salida de una cadena repetidamente hasta que se mate.
- `cal` - Mostrar un calendario.
- `date` - Mostrar o establecer la fecha y la hora.
- `sleep` - Retrasar una cantidad de tiempo especificada.
- `watch` - Ejecutar un programa periódicamente, mostrando la salida en pantalla completa.
- `xargs` - Construir y ejecutar líneas de comandos desde la entrada estándar.
- `seq` - Imprimir una secuencia de números.
- `shuf` - Generar permutaciones aleatorias.
- `tee` - Leer de la entrada estándar y escribir en la salida estándar y archivos.
- `tput` - Inicializar un terminal o consultar la base de datos terminfo.
- `stty` - Cambiar e imprimir la configuración de la línea del terminal.
- `clear` - Limpiar la pantalla del terminal.
- `reset` - Restablecer el terminal a un estado sensato.
- `script` - Hacer un typescript de la sesión del terminal.
- `wall` - Escribir un mensaje a todos los usuarios.
- `write` - Enviar un mensaje a otro usuario.
- `mesg` - Controlar el acceso de escritura a tu terminal.
- `talk` - Hablar con otro usuario.
- `ytalk` - Otro programa de charla (si está instalado).
- `crontab` - Mantener archivos crontab para usuarios individuales.
- `at` - Programar comandos para ser ejecutados una vez a una hora posterior.
- `batch` - Programar comandos para ser ejecutados en una cola por lotes.
- `nice` - Ejecutar un programa con prioridad de programación modificada.
- `renice` - Alterar la prioridad de los procesos en ejecución.
- `time` - Temporizar la ejecución de un comando.
- `ulimit` - Establecer o informar sobre los límites de recursos del usuario.
- `pr` - Convertir archivos de texto para imprimir.
- `lp` - Enviar archivos a una impresora.
- `lpr` - Imprimir archivos.
- `lpq` - Mostrar el estado de la cola de la impresora.
- `lprm` - Eliminar trabajos de la cola de la impresora.
- `enscript` - Convertir texto a PostScript, HTML o RTF, con resaltado de sintaxis (si está instalado).
- `a2ps` - Filtro de cualquier cosa a PostScript.
- `ps2pdf` - Convertir PostScript a PDF.
- `pdf2ps` - Convertir PDF a PostScript.
- `gs` - Intérprete de Ghostscript.
- `convert` - Convertir entre formatos de imagen (si está instalado).
- `mogrify` - Redimensionar, rotar y transformar imágenes (si está instalado).
- `exiftool` - Leer, escribir y editar metainformación en archivos (si está instalado).
- `jpegoptim` - Optimizar archivos JPEG (si está instalado).
- `optipng` - Optimizar archivos PNG (si está instalado).

Estos comandos cubren una amplia gama de funcionalidades y son esenciales para los usuarios que desean gestionar y interactuar con su sistema macOS de manera eficiente a través de la terminal.