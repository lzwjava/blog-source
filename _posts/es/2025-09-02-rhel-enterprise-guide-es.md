---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía Completa de Red Hat Enterprise Linux
translated: true
type: note
---

Aquí tienes una **guía completa de Red Hat Enterprise Linux (RHEL)**. La estructuraré paso a paso para que puedas usarla tanto como una ruta de aprendizaje como una referencia.

---

## 1. Introducción a Red Hat Linux

Red Hat Enterprise Linux (RHEL) es una distribución comercial de Linux desarrollada por **Red Hat, Inc.**, diseñada para **estabilidad, seguridad y soporte empresarial**. Es ampliamente utilizada en banca, salud, gobierno y TI corporativa debido a su ciclo de vida de soporte a largo plazo y su ecosistema de software certificado.

Aspectos destacados:

* Soporte de grado empresarial (ciclo de vida de más de 10 años por versión principal).
* Certificado en hardware principal (Dell, HP, IBM, etc.).
* Ampliamente utilizado en la nube (AWS, Azure, GCP), contenedores (OpenShift, Kubernetes) y virtualización.

---

## 2. Instalación y Configuración

* **Descarga**: Las imágenes ISO oficiales están disponibles a través del Portal del Cliente de Red Hat (requiere suscripción).
* **Instaladores**: Utiliza el **instalador Anaconda** con modos gráfico y de texto.
* **Particionado**: Opciones para LVM, XFS (sistema de archivos por defecto) y discos cifrados.
* **Herramientas post-instalación**: `subscription-manager` para registrar el sistema.

---

## 3. Gestión de Paquetes

* **RPM (Red Hat Package Manager)** – el formato subyacente para el software.
* **DNF (Dandified Yum)** – el gestor de paquetes por defecto en RHEL 8 y posteriores.

  * Instalar un paquete:

    ```bash
    sudo dnf install httpd
    ```
  * Actualizar el sistema:

    ```bash
    sudo dnf update
    ```
  * Buscar paquetes:

    ```bash
    sudo dnf search nginx
    ```

RHEL también admite **AppStreams** para múltiples versiones de software (por ejemplo, Python 3.6 vs 3.9).

---

## 4. Conceptos Básicos de Administración del Sistema

* **Gestión de Usuarios**:
  `useradd`, `passwd`, `usermod`, `/etc/passwd`, `/etc/shadow`
* **Gestión de Procesos**:
  `ps`, `top`, `htop`, `kill`, `systemctl`
* **Gestión de Discos**:
  `lsblk`, `df -h`, `mount`, `umount`, `fdisk`, `parted`
* **Servicios del Sistema** (systemd):

  ```bash
  systemctl start nginx
  systemctl enable nginx
  systemctl status nginx
  ```

---

## 5. Redes

* La configuración se almacena en `/etc/sysconfig/network-scripts/`.
* Comandos:

  * `nmcli` (CLI de NetworkManager)
  * `ip addr`, `ip route`, `ping`, `traceroute`
* Cortafuegos:

  * Gestionado por **firewalld** (`firewall-cmd`).
  * Ejemplo:

    ```bash
    firewall-cmd --add-service=http --permanent
    firewall-cmd --reload
    ```

---

## 6. Seguridad

* **SELinux**: Sistema de control de acceso obligatorio.

  * Verificar estado: `sestatus`
  * Modos: enforcing, permissive, disabled
* **FirewallD**: Gestiona la seguridad de red.
* **Actualizaciones del Sistema**: Parches de seguridad mediante `dnf update`.
* **Auditd**: Registro y cumplimiento.

---

## 7. Registro y Monitorización

* **Registros del sistema**:
  Almacenados en `/var/log/`.
* **Journald**:
  `journalctl -xe`
* **Herramientas de rendimiento**:

  * `sar` (paquete sysstat)
  * `vmstat`, `iostat`, `dstat`
* **Red Hat Insights**: Análisis del sistema basado en la nube.

---

## 8. Virtualización y Contenedores

* **KVM** (Kernel-based Virtual Machine) para virtualización.
* **Podman** (en lugar de Docker):

  ```bash
  podman run -it centos /bin/bash
  ```
* **OpenShift** (plataforma Kubernetes) para orquestación.

---

## 9. Gestión de Almacenamiento

* **LVM (Logical Volume Manager)** para una gestión flexible de discos.
* **XFS**: Sistema de archivos por defecto.
* **Stratis**: Gestión de almacenamiento con aprovisionamiento ligero e instantáneas.

---

## 10. Automatización y Gestión de Configuración

* **Ansible**: Plataforma de automatización de Red Hat.
* **Kickstart**: Automatiza las instalaciones del SO.
* **System Roles**: Roles predefinidos de Ansible para RHEL.

---

## 11. Suscripciones y Soporte

* Red Hat utiliza un **modelo de suscripción**.
* `subscription-manager` para registrar, adjuntar suscripciones y habilitar repositorios.
* La suscripción de desarrollador de RHEL es **gratuita para individuos**.

---

## 12. Mejores Prácticas

* Mantén siempre los sistemas actualizados con parches de seguridad.
* Usa SELinux en modo enforcing a menos que estés depurando.
* Centraliza el registro con `rsyslog` o la pila ELK.
* Automatiza tareas repetitivas con Ansible.
* Monitoriza el estado del sistema con Red Hat Insights.

---

## 13. Recursos de Aprendizaje

* [Documentación de Red Hat](https://access.redhat.com/documentation)
* [Red Hat Academy](https://www.redhat.com/en/services/training-and-certification/red-hat-academy)
* Certificaciones:

  * **RHCSA** (Red Hat Certified System Administrator)
  * **RHCE** (Red Hat Certified Engineer)
  * **RHCA** (Red Hat Certified Architect)

---

✅ Esa es la base.
¿Te gustaría que **amplíe esto a una "guía práctica"** con comandos y flujos de trabajo del mundo real (como configurar un servidor web, una base de datos, un cortafuegos, etc.), o prefieres mantenerlo más **teórico y conceptual**?