---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Hipervisores y Gestión de Máquinas Virtuales
translated: true
type: note
---

Un **hipervisor** (también llamado **monitor de máquina virtual** o VMM) es el software central (o a veces firmware/hardware) que crea, ejecuta y gestiona **máquinas virtuales (VM)** en un ordenador físico anfitrión. Es lo que hace posible la virtualización al abstraer y compartir los recursos de hardware físico (CPU, memoria, almacenamiento, red, etc.) entre múltiples máquinas virtuales aisladas.

### Dos Tipos Principales de Hipervisores

| Tipo | Descripción | ¿Se ejecuta directamente sobre el hardware? | Ejemplos | Ventajas | Desventajas |
|------|-------------|---------------------------------------------|----------|----------|-------------|
| **Tipo 1 (Bare-metal o nativo)** | Se instala y ejecuta directamente sobre el hardware físico. No hay un sistema operativo anfitrión debajo del hipervisor. | Sí | VMware ESXi, Microsoft Hyper-V (en modo hipervisor), Xen, KVM (cuando se usa bare-metal), Proxmox VE, Oracle VM Server | Mejor rendimiento, mayor seguridad, menor sobrecarga, se usa en entornos de producción/centros de datos | Más difícil de gestionar para principiantes, menos controladores/herramientas integrados |
| **Tipo 2 (Alojado)** | Se ejecuta como una aplicación sobre un sistema operativo convencional (Windows, macOS, Linux). El SO anfitrión es el propietario del hardware. | No (se ejecuta sobre el SO anfitrión) | VMware Workstation, VMware Fusion, VirtualBox, Parallels Desktop, QEMU (cuando se usa con un SO anfitrión) | Fácil de instalar y usar, bueno para escritorios/portátiles, puede usar controladores y herramientas del SO anfitrión | Rendimiento ligeramente inferior, mayor superficie de ataque debido al SO anfitrión |

### Cómo Funciona un Hipervisor (Simplificado)

1.  **Abstracción de recursos** – El hipervisor presenta CPUs virtuales (vCPUs), RAM virtual, discos virtuales, NICs virtuales, etc., a cada VM.
2.  **Aislamiento** – Cada VM está completamente aislada; que una VM falle o sea comprometida normalmente no afecta a las demás.
3.  **Planificación** – El hipervisor planifica qué VM puede usar la CPU/RAM física en un momento dado (time-sharing o tiempo compartido).
4.  **Captura y emulación** – Cuando una VM intenta ejecutar instrucciones privilegiadas (ej., cambiar tablas de páginas, acceder al hardware), la CPU captura la instrucción y pasa el control al hipervisor, que emula o maneja la petición de forma segura.
5.  **Aceleración por hardware** – Las CPU modernas tienen extensiones de virtualización (Intel VT-x, AMD-V) que hacen que el proceso de captura y emulación sea extremadamente rápido (rendimiento casi nativo).

### Casos de Uso Comunes

-   Consolidación de servidores (ejecutar docenas de VMs en un solo servidor físico)
-   Computación en la nube (AWS EC2, Azure VMs, GCP Compute Engine usan hipervisores internamente)
-   Entornos de desarrollo y pruebas
-   Virtualización de escritorio (ejecutar Windows en macOS o múltiples distribuciones de Linux simultáneamente)
-   Sandboxes de seguridad y análisis de malware

### Hipervisores Populares Actualmente (2025)

-   **VMware ESXi** – Dominante en el ámbito empresarial (parte de Broadcom ahora)
-   **Microsoft Hyper-V** – Integrado en Windows Server y Windows 10/11 Pro
-   **KVM** – Por defecto en Linux, impulsa la mayoría de OpenStack y nubes públicas (Google Cloud, AWS Nitro, etc.)
-   **Proxmox VE** – Tipo 1 de código abierto basado en Debian + KVM + LXC
-   **Xen** – Usado por Oracle Cloud, AWS (generaciones anteriores), XCP-ng
-   **VirtualBox** – Tipo 2 gratuito de Oracle, muy popular para uso personal
-   **Nutanix AHV** – Acropolis Hypervisor (basado en KVM) para HCI

En resumen: el hipervisor es el "director de orquesta" que permite a múltiples sistemas operativos compartir de forma segura y eficiente el mismo ordenador físico. El Tipo 1 es lo que encontrarás en centros de datos y nubes; el Tipo 2 es lo que los usuarios de escritorio suelen instalar.