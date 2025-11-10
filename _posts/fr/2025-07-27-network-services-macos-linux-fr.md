---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Services réseau dans macOS et Linux
translated: true
type: note
---

### Services réseau et termes associés dans macOS et Linux

Ces termes semblent faire principalement référence à des noms de services réseau, souvent définis dans le fichier `/etc/services` sur les systèmes macOS et Linux. Ce fichier associe des noms de services à des numéros de port et des protocoles pour les services réseau standard. Certains sont des services officiels enregistrés par l'IANA, tandis que d'autres sont des alias ou des noms de protocoles couramment utilisés dans les configurations système. Voici une explication pour chacun, basée sur l'usage standard dans macOS (qui utilise une base de type BSD) et les distributions Linux.

- **service** : C'est un terme générique pour les démons ou processus système dans macOS (via launchd) et Linux (via systemd ou les systèmes init). Ce n'est pas un service réseau spécifique dans `/etc/services`, mais il peut faire référence à la commande "service" sous Linux pour gérer les anciens scripts d'init SysV, ou plus largement à tout service en arrière-plan.

- **ircu** : Fait référence au service IRCU (Internet Relay Chat Undernet), une variante du logiciel serveur IRC. Il utilise le port 6667/tcp (et parfois udp). Sous Linux, il pourrait être associé à des démons IRC comme les paquets ircu ou undernet-ircu. N'est pas couramment préinstallé sur macOS ou les Linux modernes, mais disponible via les ports ou paquets pour les serveurs de discussion.

- **complex-link** : Probablement une faute de frappe ou une variante de "commplex-link", un service réseau enregistré sur le port 5001/tcp. Il est utilisé pour la multiplexion des liens de communication (par exemple, dans certains outils ou protocoles de mise en réseau). Sous macOS, ce port est associé à la configuration AirPort/Time Capsule ou aux utilitaires d'administration de routeur (par exemple, les appareils Netgear ou Apple). Sous Linux, il peut apparaître dans les règles de pare-feu ou la sortie de netstat pour des usages similaires.

- **dhcpc** : Alias pour le service client DHCP, utilisant le port 68/udp (aussi connu sous le nom de bootpc). C'est le côté client du DHCP pour l'obtention dynamique d'adresses IP. Sous Linux, il est géré par des processus comme dhclient ou dhcpcd ; sous macOS, par configd ou bootpd (mode client).

- **zeroconf** : Fait référence au Zero Configuration Networking (Zeroconf), un protocole pour la découverte automatique de services sans configuration manuelle. Sous macOS, il est implémenté sous le nom de Bonjour (utilisant mDNS sur le port 5353/udp). Sous Linux, c'est typiquement Avahi (également sur le port 5353/udp). Utilisé pour découvrir les imprimantes, les partages et autres services réseau locaux.

- **ntp** : Service Network Time Protocol pour synchroniser les horloges système sur le réseau. Utilise le port 123/udp (et parfois tcp). Sous Linux, géré par ntpd ou chronyd ; sous macOS, par ntpd ou le démon de synchronisation horaire intégré.

- **http** : HyperText Transfer Protocol, la base de la communication web. Utilise le port 80/tcp (parfois udp). Dans macOS et Linux, il est associé à des serveurs web comme Apache (httpd) ou Nginx.

- **ssh** : Protocole Secure Shell pour l'accès à distance sécurisé et le transfert de fichiers. Utilise le port 22/tcp (et udp/sctp). Sous Linux et macOS, le démon est sshd, activé via les préférences système ou sshd_config.

- **hgvirtgrp** : Cela semble être une référence à un groupe d'utilisateurs lié à la virtualisation, peut-être une variante ou une faute de frappe pour "libvirt group" sous Linux (par exemple, le groupe libvirt ou libvirt-qemu). Sous Linux, l'ajout d'utilisateurs au groupe libvirt accorde l'accès pour gérer les machines virtuelles via libvirt (pour KVM/QEMU). Sous macOS, la virtualisation utilise le framework Hypervisor, mais il n'y a pas de groupe "hgvirtgrp" standard — cela peut faire référence à des groupes personnalisés pour des outils d'hyperviseur/de virtualisation comme QEMU ou Virt-Manager. S'il s'agit d'un groupe spécifique, vérifiez le fichier `/etc/group` sur votre système.

On les rencontre couramment dans des outils comme `netstat`, `lsof` ou les configurations de pare-feu (par exemple, pf sur macOS, iptables/ufw sur Linux). Pour des définitions exactes, consultez le fichier `/etc/services` de votre système ou le registre des ports de l'IANA.

**Références**  
[Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)  
[what is an open port with a commplex-link? - Apple Community](https://discussions.apple.com/thread/7747034)  
[Running virt-manager and libvirt on macOS](https://www.arthurkoziel.com/running-virt-manager-and-libvirt-on-macos/)