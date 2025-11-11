---
audio: false
generated: true
lang: es
layout: post
title: Cómo Funciona Docker
translated: true
type: note
---

Adentrémonos en cómo funciona Docker, centrándonos en su uso del sistema de archivos de Linux y cómo aísla las aplicaciones entre sí.

---

### ¿Qué es Docker, en esencia?
Docker es una plataforma que te permite empaquetar, distribuir y ejecutar aplicaciones dentro de entornos ligeros y aislados llamados **contenedores**. A diferencia de las máquinas virtuales (VM), que incluyen un sistema operativo completo, los contenedores de Docker comparten el kernel del sistema operativo anfitrión y utilizan sus características para proporcionar aislamiento y eficiencia.

---

### Cómo funciona Docker
Docker aprovecha varias características del kernel de Linux para crear y gestionar contenedores:
1.  **Namespaces** - Para el aislamiento.
2.  **Grupos de Control (cgroups)** - Para la gestión de recursos.
3.  **Sistemas de Archivos Union (Union Filesystems)** - Para un almacenamiento y una estratificación eficientes.

Así es como estas piezas se unen:

---

#### 1. Namespaces de Linux: Mecanismo de Aislamiento
Los namespaces crean "vistas" aisladas de los recursos del sistema, garantizando que los procesos en un contenedor no interfieran con los de otro. Los namespaces clave que Docker utiliza incluyen:

-   **PID Namespace**: Cada contenedor tiene su propio espacio de ID de proceso. El ID de proceso 1 dentro de un contenedor está aislado del PID 1 del anfitrión (normalmente `init` o `systemd`).
-   **Network Namespace**: Los contenedores obtienen su propia pila de red (dirección IP, puertos, tablas de enrutamiento). Es por eso que dos contenedores pueden escuchar en el puerto 8080 sin conflictos.
-   **Mount Namespace**: Cada contenedor tiene su propia vista del sistema de archivos, aislada del anfitrión y de otros contenedores.
-   **UTS Namespace**: Los contenedores pueden tener su propio nombre de host y nombre de dominio.
-   **IPC Namespace**: Aísla la comunicación entre procesos (por ejemplo, memoria compartida, colas de mensajes).
-   **User Namespace** (opcional): Asigna usuarios del contenedor a usuarios del anfitrión, mejorando la seguridad.

**Ejemplo**: Si ejecutas `ps` dentro de un contenedor, solo ves los procesos dentro del namespace PID de ese contenedor, no los procesos del anfitrión.

---

#### 2. Grupos de Control (cgroups): Límites de Recursos
Los cgroups limitan y monitorizan el uso de recursos (CPU, memoria, E/S de disco, etc.) para cada contenedor. Esto evita que un contenedor acapare todos los recursos del sistema y deje sin recursos a los demás.

-   **Cómo funciona**: Docker asigna un cgroup a cada contenedor. Puedes establecer límites como:
    ```bash
    docker run --memory="512m" --cpus="0.5" myapp
    ```
    Esto restringe el contenedor a 512 MB de RAM y medio núcleo de CPU.

-   **Aislamiento**: Mientras que los namespaces aíslan la visibilidad, los cgroups aíslan el consumo de recursos.

---

#### 3. Sistemas de Archivos Union: Almacenamiento en Capas
Docker utiliza un **sistema de archivos union** (por ejemplo, OverlayFS, AUFS) para gestionar las imágenes de los contenedores y sus sistemas de archivos de manera eficiente. Así es como se relaciona con el sistema de archivos de Linux:

-   **Capas de Imagen**: Una imagen de Docker se construye a partir de capas superpuestas y de solo lectura. Cada capa representa un conjunto de cambios (por ejemplo, instalar un paquete, copiar archivos) definidos en tu `Dockerfile`.
    -   Ejemplo: `FROM openjdk:17` es una capa, `COPY app.jar` añade otra.
    -   Las capas se almacenan en caché y se reutilizan, ahorrando espacio en disco y acelerando las construcciones.

-   **Sistema de Archivos del Contenedor**: Cuando ejecutas un contenedor, Docker añade una capa fina y escribible sobre las capas de imagen de solo lectura. Esto se denomina mecanismo **copy-on-write (CoW)**:
    -   Las lecturas se realizan desde las capas de la imagen.
    -   Las escrituras (por ejemplo, archivos de registro, datos temporales) van a la capa escribible.
    -   Si se modifica un archivo en una capa inferior, primero se copia a la capa escribible (de ahí "copy-on-write").

-   **Aislamiento**: Cada contenedor obtiene su propia capa escribible, por lo que los cambios en un contenedor no afectan a otros, incluso si comparten la misma imagen base.

-   **En Disco**: En el anfitrión, estas capas se almacenan en `/var/lib/docker` (por ejemplo, `/var/lib/docker/overlay2` para OverlayFS). No interactúas con esto directamente; Docker lo gestiona.

---

### Cómo se Aíslan las Aplicaciones Entre Sí
Así es como los componentes anteriores trabajan juntos para aislar las aplicaciones:

1.  **Aislamiento de Procesos (PID Namespace)**:
    -   Cada contenedor ejecuta su aplicación como un árbol de procesos independiente, sin conocimiento de otros contenedores o del anfitrión.

2.  **Aislamiento de Red (Network Namespace)**:
    -   Los contenedores tienen interfaces de red separadas. La red "bridge" por defecto de Docker asigna a cada contenedor una IP única, y NAT maneja la comunicación externa.
    -   Ejemplo: Dos aplicaciones Spring Boot pueden vincularse al puerto 8080 dentro de sus contenedores sin conflictos.

3.  **Aislamiento del Sistema de Archivos (Mount Namespace + UnionFS)**:
    -   Cada contenedor ve solo su propio sistema de archivos, construido a partir de las capas de la imagen más su capa escribible.
    -   Si el Contenedor A escribe en `/tmp`, el Contenedor B no lo ve.

4.  **Aislamiento de Recursos (cgroups)**:
    -   Una aplicación no puede agotar la CPU o la memoria del anfitrión y bloquear a otra.

5.  **Kernel Compartido**:
    -   Los contenedores comparten el kernel de Linux del anfitrión, pero los namespaces garantizan que no se pisen los unos a los otros. Las syscalls se filtran o redirigen según sea necesario.

---

### Flujo de Trabajo Simplificado
1.  **Build**: Creas una imagen con un `Dockerfile`, definiendo la aplicación y sus dependencias. Docker las apila en capas usando un sistema de archivos union.
2.  **Run**: Docker crea un contenedor mediante:
    -   La configuración de namespaces para el aislamiento.
    -   La asignación de cgroups para los límites de recursos.
    -   El montaje de las capas de la imagen más una capa escribible.
    -   El inicio de tu aplicación como punto de entrada (por ejemplo, `java -jar app.jar`).
3.  **Cleanup**: Cuando el contenedor se detiene, la capa escribible se descarta (a menos que se guarde como una nueva imagen con `docker commit`).

---

### ¿Por qué Linux?
Docker depende de características del kernel de Linux (namespaces, cgroups, sistemas de archivos union) que están profundamente integradas en su funcionamiento. En macOS o Windows, Docker ejecuta una máquina virtual Linux ligera (a través de HyperKit o WSL2) para proporcionar estas capacidades, y luego las asigna al sistema operativo anfitrión.

---

### Analogía Visual
Piensa en los contenedores de Docker como apartamentos en un edificio:
-   **Namespaces**: Las paredes y puertas mantienen a los inquilinos separados.
-   **Cgroups**: El propietario limita el agua o la electricidad por unidad.
-   **UnionFS**: Todos los apartamentos comparten un plano común (capas de imagen), pero cada inquilino puede decorar su espacio (capa escribible).

---

¿Aclara esto cómo funciona Docker y cómo aísla las aplicaciones? ¡Házme saber si te gustaría profundizar en alguna parte!