---
audio: false
generated: true
image: false
lang: de
layout: post
title: Netzwerkdienste in macOS und Linux
translated: true
type: note
---

### Netzwerkdienste und verwandte Begriffe in macOS und Linux

Diese Begriffe beziehen sich hauptsächlich auf Netzwerkdienstnamen, die oft in der Datei `/etc/services` auf macOS- und Linux-Systemen definiert sind. Diese Datei ordnet Dienstnamen Portnummern und Protokollen für standardisierte Netzwerkdienste zu. Einige sind offizielle, bei der IANA registrierte Dienste, während andere Aliase oder Protokollnamen sind, die häufig in Systemkonfigurationen verwendet werden. Im Folgenden finden Sie eine Erläuterung jedes Begriffs, basierend auf der Standardverwendung in macOS (das eine BSD-ähnliche Basis verwendet) und Linux-Distributionen.

- **service**: Dies ist ein generischer Begriff für System-Daemons oder Prozesse in sowohl macOS (über launchd) als auch Linux (über systemd oder Init-Systeme). Es ist kein spezifischer Netzwerkdienst in `/etc/services`, kann sich aber auf den "service"-Befehl in Linux zur Verwaltung von Legacy-SysV-Init-Skripten oder allgemein auf jeden Hintergrunddienst beziehen.

- **ircu**: Bezieht sich auf den IRCU (Internet Relay Chat Undernet) Dienst, eine Variante der IRC-Server-Software. Er verwendet Port 6667/tcp (und manchmal udp). Unter Linux könnte er mit IRC-Daemons wie ircu oder undernet-ircu Paketen assoziiert sein. Nicht üblicherweise vorinstalliert auf macOS oder modernem Linux, aber über Ports oder Pakete für Chat-Server verfügbar.

- **complex-link**: Wahrscheinlich ein Tippfehler oder eine Variante von "commplex-link", einem Netzwerkdienst, der auf Port 5001/tcp registriert ist. Er wird für Communication Multiplexing Links verwendet (z.B. in einigen Netzwerktools oder Protokollen). Unter macOS ist dieser Port mit der AirPort/Time Capsule Konfiguration oder Router-Admin-Utilities (z.B. Netgear oder Apple Geräte) assoziiert. Unter Linux kann er in Firewall-Regeln oder netstat-Ausgaben für ähnliche Zwecke erscheinen.

- **dhcpc**: Alias für den DHCP-Client-Dienst, der Port 68/udp verwendet (auch bekannt als bootpc). Dies ist die Client-Seite von DHCP zum dynamischen Beziehen von IP-Adressen. Unter Linux wird er von Prozessen wie dhclient oder dhcpcd gehandhabt; unter macOS von configd oder bootpd (Client-Modus).

- **zeroconf**: Bezieht sich auf Zero Configuration Networking (Zeroconf), ein Protokoll für die automatische Dienstentdeckung ohne manuelle Konfiguration. Unter macOS ist es als Bonjour implementiert (verwendet mDNS auf Port 5353/udp). Unter Linux ist es typischerweise Avahi (ebenfalls auf Port 5353/udp). Wird verwendet, um Drucker, Freigaben und andere lokale Netzwerkdienste zu entdecken.

- **ntp**: Network Time Protocol Dienst zur Synchronisierung von Systemuhren über das Netzwerk. Verwendet Port 123/udp (und manchmal tcp). Unter Linux gehandhabt von ntpd oder chronyd; unter macOS von ntpd oder dem eingebauten Zeit-Sync-Daemon.

- **http**: HyperText Transfer Protocol, die Grundlage der Webkommunikation. Verwendet Port 80/tcp (manchmal udp). In sowohl macOS als auch Linux ist es mit Web-Servern wie Apache (httpd) oder Nginx assoziiert.

- **ssh**: Secure Shell Protokoll für sicheren Remote-Zugriff und Dateitransfer. Verwendet Port 22/tcp (und udp/sctp). Unter Linux und macOS ist der Daemon sshd, aktiviert über Systemeinstellungen oder sshd_config.

- **hgvirtgrp**: Dies scheint ein Verweis auf eine Benutzergruppe im Zusammenhang mit Virtualisierung zu sein, möglicherweise eine Variante oder ein Tippfehler für "libvirt group" in Linux (z.B. libvirt oder libvirt-qemu Gruppe). Unter Linux gewährt das Hinzufügen von Benutzern zur libvirt Gruppe Zugriff auf die Verwaltung von virtuellen Maschinen über libvirt (für KVM/QEMU). Unter macOS verwendet Virtualisierung das Hypervisor-Framework, aber es gibt keine standardmäßige "hgvirtgrp" Gruppe – es könnte sich auf benutzerdefinierte Gruppen für Hypervisor/Virtualisierungs-Tools wie QEMU oder Virt-Manager beziehen. Wenn es eine spezifische Gruppe ist, überprüfen Sie `/etc/group` auf Ihrem System.

Diese werden häufig in Tools wie `netstat`, `lsof` oder Firewall-Konfigurationen (z.B. pf auf macOS, iptables/ufw auf Linux) gesehen. Für exakte Definitionen konsultieren Sie die `/etc/services`-Datei Ihres Systems oder das IANA-Port-Register.

**Referenzen**  
[Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)  
[what is an open port with a commplex-link? - Apple Community](https://discussions.apple.com/thread/7747034)  
[Running virt-manager and libvirt on macOS](https://www.arthurkoziel.com/running-virt-manager-and-libvirt-on-macos/)