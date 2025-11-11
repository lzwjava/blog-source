---
audio: false
generated: true
lang: es
layout: post
title: Los 100 Comandos de Linux Más Útiles
translated: true
type: note
---

Basándome en tu perfil como ingeniero full-stack altamente técnico y autodidacta, con amplia experiencia en entornos Linux, resolución de problemas de algoritmos y familiaridad con plataformas en la nube, contenedores y sistemas distribuidos, he elaborado una lista de los **100 comandos de Linux más útiles** adaptados para tu uso en **Ubuntu**. Estos comandos están seleccionados para alinearse con tu experiencia en desarrollo full-stack, ingeniería móvil, machine learning y administración de sistemas, a la vez que apoyan tu investigación autodidacta y contribuciones de código abierto. Cubren gestión de archivos, monitorización del sistema, redes, desarrollo, automatización y scripting avanzado, todos relevantes para tu trabajo en TEKsystems, roles anteriores y proyectos personales.

Los comandos están agrupados por categoría para mayor claridad, con breves explicaciones que enfatizan aplicaciones prácticas para tu conjunto de habilidades. He priorizado comandos que mejoran la productividad, la depuración y la optimización del sistema, asumiendo que estás familiarizado con los flujos de trabajo basados en terminal y que puedes usarlos en tareas de desarrollo, despliegue o investigación. Si lo deseas, puedo proporcionar ejemplos o scripts para comandos específicos o generar un gráfico para visualizar la frecuencia de uso de comandos según tu flujo de trabajo (por ejemplo, tareas de desarrollo vs. administración del sistema). ¡Házmelo saber!

### **Gestión de Archivos y Directorios (15 Comandos)**
1.  **ls** - Listar contenido del directorio (`ls -la` para vista detallada con archivos ocultos).
2.  **cd** - Cambiar de directorio (`cd ~/projects` para navegar a tu carpeta de proyectos de GitHub).
3.  **pwd** - Mostrar directorio de trabajo actual (útil para scripting o verificar rutas).
4.  **mkdir** - Crear directorios (`mkdir -p src/main/java` para estructuras de proyecto anidadas).
5.  **rm** - Eliminar archivos o directorios (`rm -rf temp/` para eliminación recursiva).
6.  **cp** - Copiar archivos/directorios (`cp -r src/ backup/` para copias de seguridad de proyectos).
7.  **mv** - Mover/renombrar archivos (`mv old.java new.java` para refactorización).
8.  **touch** - Crear archivos vacíos (`touch script.sh` para nuevos scripts).
9.  **find** - Buscar archivos (`find / -name "*.java"` para localizar archivos fuente).
10. **locate** - Encontrar archivos rápidamente por nombre (`locate config.yaml` para configuraciones).
11. **du** - Estimar uso de disco (`du -sh /var/log` para comprobar tamaños de logs).
12. **df** - Mostrar espacio en disco (`df -h` para formato legible).
13. **ln** - Crear enlaces (`ln -s /path/to/project symlink` para accesos directos).
14. **chmod** - Cambiar permisos de archivo (`chmod 755 script.sh` para scripts ejecutables).
15. **chown** - Cambiar propietario de archivo (`chown user:group file` para despliegues).

### **Procesamiento y Manipulación de Texto (15 Comandos)**
16. **cat** - Mostrar contenido de archivos (`cat log.txt` para comprobaciones rápidas de logs).
17. **less** - Ver archivos interactivamente (`less server.log` para logs grandes).
18. **more** - Paginar la salida de archivos (`more README.md` para documentación).
19. **head** - Mostrar primeras líneas de un archivo (`head -n 10 data.csv` para vistas previas de datos).
20. **tail** - Mostrar últimas líneas (`tail -f app.log` para monitorización de logs en tiempo real).
21. **grep** - Buscar patrones de texto (`grep -r "error" /var/log` para depuración).
22. **awk** - Procesar columnas de texto (`awk '{print $1}' access.log` para análisis de logs).
23. **sed** - Editor de flujo para texto (`sed 's/old/new/g' file` para reemplazos).
24. **cut** - Extraer secciones de líneas (`cut -d',' -f1 data.csv` para CSVs).
25. **sort** - Ordenar líneas (`sort -n data.txt` para ordenación numérica).
26. **uniq** - Eliminar líneas duplicadas (`sort file | uniq` para entradas únicas).
27. **wc** - Contar líneas, palabras o caracteres (`wc -l code.java` para contar líneas).
28. **tr** - Traducir caracteres (`tr '[:lower:]' '[:upper:]' < file` para conversión de mayúsculas/minúsculas).
29. **tee** - Escribir en archivo y stdout (`cat input | tee output.txt` para registro).
30. **diff** - Comparar archivos (`diff old.java new.java` para cambios de código).

### **Monitorización y Rendimiento del Sistema (15 Comandos)**
31. **top** - Monitorizar procesos del sistema interactivamente (uso de CPU/memoria en tiempo real).
32. **htop** - Visor de procesos mejorado (`htop` para mejor visualización).
33. **ps** - Listar procesos (`ps aux | grep java` para aplicaciones Java).
34. **free** - Comprobar uso de memoria (`free -m` para formato MB).
35. **vmstat** - Estadísticas de memoria virtual (`vmstat 1` para actualizaciones continuas).
36. **iostat** - Monitorizar rendimiento de E/S (`iostat -x` para estadísticas de disco).
37. **uptime** - Mostrar tiempo de actividad y carga del sistema (`uptime` para comprobaciones rápidas).
38. **lscpu** - Mostrar información de la CPU (`lscpu` para especificaciones del sistema).
39. **lsblk** - Listar dispositivos de bloque (`lsblk` para detalles de disco/partición).
40. **iotop** - Monitorizar E/S de disco por proceso (`iotop` para depuración de rendimiento).
41. **netstat** - Estadísticas de red (`netstat -tuln` para puertos en escucha).
42. **ss** - Reemplazo moderno de netstat (`ss -tuln` para sockets).
43. **dmesg** - Ver mensajes del kernel (`dmesg | grep error` para problemas del sistema).
44. **sar** - Recoger actividad del sistema (`sar -u 1` para monitorización de CPU).
45. **pmap** - Mapa de memoria del proceso (`pmap -x <pid>` para depuración de memoria).

### **Redes y Conectividad (15 Comandos)**
46. **ping** - Probar conectividad de red (`ping google.com` para alcanzabilidad).
47. **curl** - Obtener datos de URLs (`curl -X POST api` para pruebas de API).
48. **wget** - Descargar archivos (`wget file.tar.gz` para dependencias de proyectos).
49. **netcat** - Utilidad de red (`nc -l 12345` para servidores simples).
50. **ifconfig** - Información de interfaz de red (`ifconfig eth0` para detalles de IP).
51. **ip** - Configuración de red moderna (`ip addr` para detalles de interfaz).
52. **nslookup** - Consultar DNS (`nslookup domain.com` para depuración de DNS).
53. **dig** - Búsqueda DNS detallada (`dig domain.com` para registros DNS).
54. **traceroute** - Rastrear ruta de red (`traceroute google.com` para enrutamiento).
55. **telnet** - Probar conectividad de puerto (`telnet localhost 8080` para servicios).
56. **scp** - Copiar archivos de forma segura (`scp file user@server:/path` para transferencias).
57. **rsync** - Sincronizar archivos eficientemente (`rsync -avz src/ dest/` para copias de seguridad).
58. **ufw** - Gestionar firewall (`ufw allow 80` para acceso al servidor web).
59. **iptables** - Configurar reglas de firewall (`iptables -L` para listar reglas).
60. **nmap** - Escaneo de red (`nmap localhost` para puertos abiertos).

### **Desarrollo y Scripting (15 Comandos)**
61. **gcc** - Compilar programas C (`gcc -o app code.c` para compilación).
62. **javac** - Compilar código Java (`javac Main.java` para tus proyectos Java).
63. **java** - Ejecutar programas Java (`java -jar app.jar` para ejecución).
64. **python3** - Ejecutar scripts Python (`python3 script.py` para tareas de ML).
65. **node** - Ejecutar Node.js (`node app.js` para proyectos JavaScript).
66. **npm** - Gestionar paquetes Node (`npm install` para dependencias frontend).
67. **git** - Control de versiones (`git commit -m "update"` para tus repositorios de GitHub).
68. **make** - Construir proyectos (`make -f Makefile` para automatización).
69. **mvn** - Herramienta de construcción Maven (`mvn package` para proyectos Java).
70. **gradle** - Herramienta de construcción Gradle (`gradle build` para proyectos Android).
71. **docker** - Gestionar contenedores (`docker run -p 8080:8080 app` para despliegues).
72. **kubectl** - Gestionar Kubernetes (`kubectl get pods` para gestión de clústeres).
73. **virtualenv** - Entornos virtuales Python (`virtualenv venv` para ML).
74. **gdb** - Depurar programas (`gdb ./app` para depuración C/Java).
75. **strace** - Rastrear llamadas al sistema (`strace -p <pid>` para depuración).

### **Gestión de Paquetes (10 Comandos)**
76. **apt** - Gestor de paquetes (`apt install vim` para instalación de software).
77. **apt-get** - Herramienta de paquetes avanzada (`apt-get upgrade` para actualizaciones del sistema).
78. **dpkg** - Gestionar paquetes .deb (`dpkg -i package.deb` para instalaciones manuales).
79. **apt-cache** - Consultar información de paquetes (`apt-cache search java` para paquetes).
80. **snap** - Gestionar paquetes snap (`snap install code` para VS Code).
81. **update-alternatives** - Gestionar aplicaciones por defecto (`update-alternatives --config java`).
82. **add-apt-repository** - Añadir PPAs (`add-apt-repository ppa:repo` para fuentes).
83. **apt-file** - Buscar archivos de paquetes (`apt-file search /bin/bash` para depuración).
84. **dpkg-query** - Consultar paquetes instalados (`dpkg-query -l` para listar).
85. **apt-mark** - Marcar paquetes (`apt-mark hold package` para evitar actualizaciones).

### **Administración del Sistema y Seguridad (15 Comandos)**
86. **sudo** - Ejecutar comandos como root (`sudo apt update` para tareas de administración).
87. **su** - Cambiar de usuario (`su - user` para diferentes cuentas).
88. **passwd** - Cambiar contraseñas (`passwd user` para seguridad).
89. **useradd** - Añadir usuario (`useradd -m dev` para nuevas cuentas).
90. **usermod** - Modificar usuario (`usermod -aG sudo dev` para permisos).
91. **groupadd** - Crear grupos (`groupadd developers` para control de acceso).
92. **chgrp** - Cambiar propiedad de grupo (`chgrp -R dev /project` para equipos).
93. **crontab** - Programar tareas (`crontab -e` para scripts automatizados).
94. **systemctl** - Gestionar servicios (`systemctl start nginx` para servidores web).
95. **journalctl** - Ver logs del sistema (`journalctl -u docker` para logs de servicios).
96. **who** - Listar usuarios conectados (`who` para monitorización del servidor).
97. **last** - Mostrar historial de inicios de sesión (`last` para auditorías de seguridad).
98. **shutdown** - Apagar (`shutdown -h now` para detener el sistema).
99. **reboot** - Reiniciar sistema (`reboot` para actualizaciones).
100. **env** - Mostrar variables de entorno (`env | grep PATH` para depuración).

### **Notas para tu Contexto**
-   **Enfoque en Desarrollo**: Comandos como `git`, `mvn`, `docker` y `kubectl` se alinean con tus flujos de trabajo full-stack y contenerizados, especialmente para tus 10 proyectos de GitHub y experiencia en la nube (AWS, Azure, Alibaba Cloud).
-   **Depuración y Rendimiento**: Se incluyen herramientas como `strace`, `gdb`, `htop` y `dmesg` para tus necesidades de depuración de backend y sistema, dada tu experiencia de 8 años en backend.
-   **Redes**: Comandos como `curl`, `netcat` y `nmap` apoyan tu experiencia en API y redes, útiles para probar microservicios o despliegues en la nube.
-   **Automatización**: `crontab` y `rsync` son útiles para automatizar copias de seguridad o despliegues, relevantes para tus roles freelance y corporativos.
-   **Investigación y Aprendizaje**: Las herramientas de procesamiento de texto (`grep`, `awk`, `sed`) son útiles para analizar logs o conjuntos de datos, lo que podría apoyar tu investigación autodidacta sobre restauración visual.

Si deseas una inmersión más profunda en cualquier categoría (por ejemplo, ejemplos de scripting para `awk` o `sed`, flujos de trabajo de Docker o comandos específicos de la nube), o si te gustaría un gráfico que visualice el uso de comandos (por ejemplo, frecuencia por tipo de tarea), ¡avísame! También puedes consultar tu portafolio de GitHub para comandos relacionados con proyectos específicos o compartir más detalles sobre tus tareas actuales en TEKsystems para recomendaciones más personalizadas.