---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Gestión de Paquetes DNF en RHEL
translated: true
type: note
---

### Introducción a DNF en Red Hat Enterprise Linux

DNF (Dandified YUM) es la herramienta principal de gestión de paquetes en Red Hat Enterprise Linux (RHEL), a partir de RHEL 8 y continuando en RHEL 9. Sirve como el sucesor de la antigua herramienta YUM (Yellowdog Updater, Modified), ofreciendo un mejor rendimiento, una mejor resolución de dependencias y soporte para contenido modular. En RHEL, DNF maneja la instalación, actualización y eliminación de paquetes de software distribuidos a través de repositorios RPM (Red Hat Package Manager). Garantiza el acceso a conjuntos de contenido esenciales como BaseOS (para la funcionalidad central del sistema operativo) y AppStream (para aplicaciones de espacio de usuario, runtimes y herramientas), todos gestionados a través de su suscripción RHEL.

El propósito de DNF es simplificar la gestión del ciclo de vida del software manteniendo la estabilidad del sistema. Permite a los administradores y usuarios trabajar con paquetes RPM tradicionales junto con formatos modulares modernos, donde componentes como lenguajes o bases de datos pueden tener múltiples versiones paralelas (llamadas "streams") sin interrumpir el sistema operativo base.

#### Características Clave
- **Soporte de Contenido Modular**: Gestiona módulos (grupos de RPM relacionados), streams (repositorios específicos de versión) y perfiles (conjuntos de paquetes preconfigurados para casos de uso específicos, por ejemplo, servidor web o entorno de desarrollo).
- **Gestión de Repositorios**: Permite buscar, habilitar/deshabilitar repositorios y configurar fuentes como BaseOS, AppStream y otras suplementarias.
- **Instalación y Actualizaciones**: Resuelve automáticamente las dependencias al instalar paquetes, grupos o módulos completos; admite la comprobación de actualizaciones, la actualización de paquetes específicos o de todo el sistema.
- **Eliminación y Reversión**: Elimina software de forma segura y proporciona un historial de transacciones para deshacer cambios.
- **Personalización y Automatización**: Configurable mediante `/etc/dnf/dnf.conf` para exclusiones, plugins o almacenamiento en caché; se integra con herramientas como DNF Automatic para actualizaciones programadas.
- **Compatibilidad con Versiones Anteriores**: El comando `yum` tiene un alias a `dnf` en RHEL, facilitando la transición desde versiones anteriores.

Para comenzar, los comandos básicos incluyen `dnf install <paquete>` para la instalación, `dnf update` para las actualizaciones y `dnf search <término>` para buscar software. Para un uso más avanzado, consulte la documentación oficial.

[Red Hat Enterprise Linux 9: Managing Software with the DNF Tool](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/managing_software_with_the_dnf_tool/index)