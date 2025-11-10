---
audio: false
generated: true
image: false
lang: es
layout: post
title: Dominando los Fundamentos de Red Hat Enterprise Linux
translated: true
type: note
---

## Introducción a Red Hat Linux
Red Hat Enterprise Linux (RHEL) es un sistema operativo líder de código abierto desarrollado por Red Hat, Inc. Está diseñado para entornos empresariales, ofreciendo estabilidad, seguridad y soporte robusto para aplicaciones críticas. RHEL es ampliamente utilizado en servidores, entornos cloud e infraestructura IT empresarial.

### Historia
- **1994**: Red Hat Linux se lanzó por primera vez como una distribución comercial de Linux.
- **2002**: Red Hat introdujo Red Hat Enterprise Linux, centrándose en la fiabilidad de grado empresarial.
- **2025**: RHEL 9 es el último lanzamiento principal, con RHEL 10 en desarrollo, que ofrece características avanzadas como seguridad mejorada y soporte para contenedores.

### Características Principales
- **Estabilidad**: RHEL prioriza el soporte a largo plazo (LTS) con un ciclo de vida de 10 años por lanzamiento principal.
- **Seguridad**: Características como SELinux (Security-Enhanced Linux), firewalld y parches de seguridad regulares.
- **Rendimiento**: Optimizado para computación de alto rendimiento, virtualización y despliegues en la nube.
- **Modelo de Suscripción**: Proporciona acceso a actualizaciones, soporte y software certificado a través de suscripciones de Red Hat.
- **Ecosistema**: Se integra con Red Hat OpenShift, Ansible y otras herramientas para DevOps y automatización.

## Instalación
### Requisitos del Sistema
- **Mínimos**:
  - 1.5 GB de RAM
  - 20 GB de espacio en disco
  - Procesador de 1 GHz
- **Recomendados**:
  - 4 GB de RAM o más
  - 40 GB+ de espacio en disco
  - Procesador multi-núcleo

### Pasos de Instalación
1. **Descargar RHEL**:
   - Obtener la ISO de RHEL desde el [Portal del Cliente de Red Hat](https://access.redhat.com) (requiere una suscripción o cuenta de desarrollador).
   - Alternativamente, usar una suscripción de desarrollador gratuita para uso no productivo.
2. **Crear Medio de Arranque**:
   - Usar herramientas como `dd` o Rufus para crear una unidad USB de arranque.
   - Comando de ejemplo: `sudo dd if=rhel-9.3-x86_64.iso of=/dev/sdX bs=4M status=progress`
3. **Arrancar e Instalar**:
   - Arrancar desde el USB o DVD.
   - Seguir el instalador Anaconda:
     - Seleccionar idioma y región.
     - Configurar particionado de disco (manual o automático).
     - Configurar ajustes de red.
     - Crear una contraseña de root y cuentas de usuario.
4. **Registrar el Sistema**:
   - Después de la instalación, registrar con Red Hat Subscription Manager: `subscription-manager register --username <usuario> --password <contraseña>`.
   - Adjuntar una suscripción: `subscription-manager attach --auto`.

## Administración del Sistema
### Gestión de Paquetes
RHEL utiliza **DNF** (Dandified YUM) para la gestión de paquetes.
- Instalar un paquete: `sudo dnf install <nombre-del-paquete>`
- Actualizar el sistema: `sudo dnf update`
- Buscar paquetes: `sudo dnf search <palabra-clave>`
- Habilitar repositorios: `sudo subscription-manager repos --enable <id-del-repo>`

### Gestión de Usuarios
- Añadir un usuario: `sudo useradd -m <nombredeusuario>`
- Establecer contraseña: `sudo passwd <nombredeusuario>`
- Modificar usuario: `sudo usermod -aG <grupo> <nombredeusuario>`
- Eliminar usuario: `sudo userdel -r <nombredeusuario>`

### Gestión del Sistema de Archivos
- Comprobar uso del disco: `df -h`
- Listar sistemas de archivos montados: `lsblk`
- Gestionar particiones: Usar `fdisk` o `parted` para el particionado de discos.
- Configurar LVM (Logical Volume Manager):
  - Crear volumen físico: `pvcreate /dev/sdX`
  - Crear grupo de volúmenes: `vgcreate <nombre-vg> /dev/sdX`
  - Crear volumen lógico: `lvcreate -L <tamaño> -n <nombre-lv> <nombre-vg>`

### Redes
- Configurar red con `nmcli`:
  - Listar conexiones: `nmcli connection show`
  - Añadir una IP estática: `nmcli con mod <nombre-conexión> ipv4.addresses 192.168.1.100/24 ipv4.gateway 192.168.1.1 ipv4.method manual`
  - Activar conexión: `nmcli con up <nombre-conexión>`
- Gestionar firewall con `firewalld`:
  - Abrir un puerto: `sudo firewall-cmd --add-port=80/tcp --permanent`
  - Recargar firewall: `sudo firewall-cmd --reload`

### Seguridad
- **SELinux**:
  - Comprobar estado: `sestatus`
  - Establecer modo (enforcing/permissive): `sudo setenforce 0` (permissive) o `sudo setenforce 1` (enforcing)
  - Modificar políticas: Usar `semanage` y `audit2allow` para políticas personalizadas.
- **Actualizaciones**:
  - Aplicar parches de seguridad: `sudo dnf update --security`
- **SSH**:
  - Asegurar SSH: Editar `/etc/ssh/sshd_config` para deshabilitar el login de root (`PermitRootLogin no`) y cambiar el puerto por defecto.
  - Reiniciar SSH: `sudo systemctl restart sshd`

## Características Avanzadas
### Contenedores y Virtualización
- **Podman**: Herramienta de contenedores sin root de RHEL.
  - Ejecutar un contenedor: `podman run -it docker.io/library/centos bash`
  - Construir una imagen: `podman build -t <nombre-imagen> .`
- **Virtualización**: Usar `libvirt` y `virt-manager` para gestionar máquinas virtuales.
  - Instalar: `sudo dnf install libvirt virt-manager`
  - Iniciar libvirt: `sudo systemctl start libvirtd`

### Automatización con Ansible
- Instalar Ansible: `sudo dnf install ansible`
- Crear un playbook:
  ```yaml
  - name: Install Apache
    hosts: all
    tasks:
      - name: Install httpd
        dnf:
          name: httpd
          state: present
  ```
- Ejecutar playbook: `ansible-playbook playbook.yml`

### Integración con la Nube
- RHEL se integra con AWS, Azure y Google Cloud.
- Usar Red Hat OpenShift para orquestación de contenedores.
- Desplegar imágenes RHEL en entornos cloud a través de Red Hat Cloud Access.

## Resolución de Problemas
- **Registros**: Revisar `/var/log` para registros del sistema (ej., `/var/log/messages` o `/var/log/secure`).
- **Systemd**: Gestionar servicios con `systemctl`:
  - Comprobar estado del servicio: `systemctl status <servicio>`
  - Reiniciar servicio: `systemctl restart <servicio>`
- **Rendimiento**: Usar `top`, `htop` o `vmstat` para monitorizar el rendimiento del sistema.
- **Problemas de Red**: Usar `ping`, `traceroute` o `nslookup` para diagnósticos.

## Mejores Prácticas
- Actualizar el sistema regularmente para parchear vulnerabilidades.
- Usar contraseñas fuertes y hacer cumplir las políticas de SELinux.
- Hacer copias de seguridad de datos críticos con herramientas como `rsync` o `rear` de Red Hat.
- Monitorizar el estado del sistema con herramientas como Cockpit (`sudo dnf install cockpit`).

## Recursos
- [Portal del Cliente de Red Hat](https://access.redhat.com)
- [Documentación de RHEL](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux)
- [Programa para Desarrolladores de Red Hat](https://developers.redhat.com)
- Foros de la comunidad como [Red Hat Discuss](https://discuss.redhat.com)