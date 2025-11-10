---
audio: false
generated: true
image: false
lang: es
layout: post
title: Servicios de Red en macOS y Linux
translated: true
type: note
---

### Servicios de red y términos relacionados en macOS y Linux

Estos términos parecen referirse principalmente a nombres de servicios de red, a menudo definidos en el archivo `/etc/services` en sistemas tanto macOS como Linux. Este archivo asigna nombres de servicios a números de puerto y protocolos para servicios de red estándar. Algunos son servicios oficiales registrados por IANA, mientras que otros son alias o nombres de protocolos comúnmente utilizados en configuraciones del sistema. A continuación se presenta una explicación de cada uno, basada en el uso estándar en macOS (que utiliza una base tipo BSD) y distribuciones de Linux.

- **service**: Este es un término genérico para demonios o procesos del sistema tanto en macOS (a través de launchd) como en Linux (a través de systemd o sistemas init). No es un servicio de red específico en `/etc/services`, pero puede referirse al comando "service" en Linux para gestionar scripts de init SysV heredados, o en general a cualquier servicio en segundo plano.

- **ircu**: Se refiere al servicio IRCU (Internet Relay Chat Undernet), una variante del software de servidor IRC. Utiliza el puerto 6667/tcp (y a veces udp). En Linux, podría estar asociado con demonios IRC como paquetes ircu o undernet-ircu. No viene preinstalado comúnmente en macOS o Linux moderno, pero está disponible mediante ports o paquetes para servidores de chat.

- **complex-link**: Probablemente un error ortográfico o una variante de "commplex-link", un servicio de red registrado en el puerto 5001/tcp. Se utiliza para enlaces de multiplexación de comunicación (por ejemplo, en algunas herramientas o protocolos de red). En macOS, este puerto está asociado con la configuración de AirPort/Time Capsule o utilidades de administración de routers (por ejemplo, dispositivos Netgear o Apple). En Linux, puede aparecer en reglas de firewall o en la salida de netstat para propósitos similares.

- **dhcpc**: Alias para el servicio cliente DHCP, que utiliza el puerto 68/udp (también conocido como bootpc). Este es el lado cliente de DHCP para obtener direcciones IP de forma dinámica. En Linux, lo manejan procesos como dhclient o dhcpcd; en macOS, por configd o bootpd (modo cliente).

- **zeroconf**: Se refiere a Zero Configuration Networking (Zeroconf), un protocolo para el descubrimiento automático de servicios sin configuración manual. En macOS, se implementa como Bonjour (usando mDNS en el puerto 5353/udp). En Linux, es típicamente Avahi (también en el puerto 5353/udp). Se utiliza para descubrir impresoras, recursos compartidos y otros servicios de red locales.

- **ntp**: Servicio Network Time Protocol para sincronizar relojes del sistema a través de la red. Utiliza el puerto 123/udp (y a veces tcp). En Linux, lo manejan ntpd o chronyd; en macOS, por ntpd o el daemon de sincronización de hora integrado.

- **http**: HyperText Transfer Protocol, la base de la comunicación web. Utiliza el puerto 80/tcp (a veces udp). Tanto en macOS como en Linux, está asociado con servidores web como Apache (httpd) o Nginx.

- **ssh**: Protocolo Secure Shell para acceso remoto seguro y transferencia de archivos. Utiliza el puerto 22/tcp (y udp/sctp). En Linux y macOS, el demonio es sshd, habilitado a través de las preferencias del sistema o sshd_config.

- **hgvirtgrp**: Esto parece ser una referencia a un grupo de usuarios relacionado con la virtualización, posiblemente una variante o error tipográfico para "libvirt group" en Linux (por ejemplo, grupo libvirt o libvirt-qemu). En Linux, agregar usuarios al grupo libvirt otorga acceso para gestionar máquinas virtuales a través de libvirt (para KVM/QEMU). En macOS, la virtualización utiliza el framework Hypervisor, pero no existe un grupo "hgvirtgrp" estándar; puede referirse a grupos personalizados para herramientas de hipervisor/virtualización como QEMU o Virt-Manager. Si es un grupo específico, verifica `/etc/group` en tu sistema.

Estos se ven comúnmente en herramientas como `netstat`, `lsof` o configuraciones de firewall (por ejemplo, pf en macOS, iptables/ufw en Linux). Para definiciones exactas, consulta el archivo `/etc/services` de tu sistema o el registro de puertos de IANA.

**Referencias**  
[Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)  
[what is an open port with a commplex-link? - Apple Community](https://discussions.apple.com/thread/7747034)  
[Running virt-manager and libvirt on macOS](https://www.arthurkoziel.com/running-virt-manager-and-libvirt-on-macos/)