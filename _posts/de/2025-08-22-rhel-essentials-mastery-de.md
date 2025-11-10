---
audio: false
generated: true
image: false
lang: de
layout: post
title: Beherrschung der Red Hat Enterprise Linux Grundlagen
translated: true
type: note
---

## Einführung in Red Hat Linux
Red Hat Enterprise Linux (RHEL) ist ein führendes Open-Source-Betriebssystem, das von Red Hat, Inc. entwickelt wurde. Es ist für Unternehmensumgebungen konzipiert und bietet Stabilität, Sicherheit und robuste Unterstützung für geschäftskritische Anwendungen. RHEL wird häufig auf Servern, in Cloud-Umgebungen und in der Enterprise-IT-Infrastruktur eingesetzt.

### Geschichte
- **1994**: Red Hat Linux wurde erstmals als kommerzielle Linux-Distribution veröffentlicht.
- **2002**: Red Hat führte Red Hat Enterprise Linux ein, mit Fokus auf unternehmensgerechte Zuverlässigkeit.
- **2025**: RHEL 9 ist die neueste Hauptversion, während RHEL 10 sich in Entwicklung befindet und erweiterte Funktionen wie verbesserte Sicherheit und Container-Unterstützung bietet.

### Wichtige Funktionen
- **Stabilität**: RHEL priorisiert Langzeitunterstützung (LTS) mit einem 10-Jahres-Lebenszyklus pro Hauptversion.
- **Sicherheit**: Funktionen wie SELinux (Security-Enhanced Linux), firewalld und regelmäßige Sicherheitsupdates.
- **Leistung**: Optimiert für High-Performance Computing, Virtualisierung und Cloud-Bereitstellungen.
- **Abonnement-Modell**: Bietet Zugang zu Updates, Support und zertifizierter Software durch Red Hat-Abonnements.
- **Ökosystem**: Integriert mit Red Hat OpenShift, Ansible und anderen Tools für DevOps und Automatisierung.

## Installation
### Systemanforderungen
- **Minimum**:
  - 1,5 GB RAM
  - 20 GB Festplattenspeicher
  - 1 GHz Prozessor
- **Empfohlen**:
  - 4 GB RAM oder mehr
  - 40 GB+ Festplattenspeicher
  - Multi-Core-Prozessor

### Installationsschritte
1. **RHEL herunterladen**:
   - Holen Sie sich das RHEL-ISO vom [Red Hat Customer Portal](https://access.redhat.com) (erfordert ein Abonnement oder Entwicklerkonto).
   - Alternativ können Sie ein kostenloses Entwickler-Abonnement für den Nicht-Produktiv-Einsatz nutzen.
2. **Bootfähiges Medium erstellen**:
   - Verwenden Sie Tools wie `dd` oder Rufus, um ein bootfähiges USB-Laufwerk zu erstellen.
   - Beispielbefehl: `sudo dd if=rhel-9.3-x86_64.iso of=/dev/sdX bs=4M status=progress`
3. **Starten und installieren**:
   - Starten Sie vom USB-Stick oder der DVD.
   - Folgen Sie dem Anaconda-Installer:
     - Wählen Sie Sprache und Region.
     - Konfigurieren Sie die Festplattenpartitionierung (manuell oder automatisch).
     - Richten Sie die Netzwerkeinstellungen ein.
     - Legen Sie ein Root-Passwort und Benutzerkonten an.
4. **System registrieren**:
   - Registrieren Sie das System nach der Installation beim Red Hat Subscription Manager: `subscription-manager register --username <Benutzername> --password <Passwort>`.
   - Fügen Sie ein Abonnement hinzu: `subscription-manager attach --auto`.

## Systemadministration
### Paketverwaltung
RHEL verwendet **DNF** (Dandified YUM) für die Paketverwaltung.
- Paket installieren: `sudo dnf install <Paketname>`
- System aktualisieren: `sudo dnf update`
- Nach Paketen suchen: `sudo dnf search <Suchbegriff>`
- Repositorys aktivieren: `sudo subscription-manager repos --enable <Repository-ID>`

### Benutzerverwaltung
- Benutzer hinzufügen: `sudo useradd -m <Benutzername>`
- Passwort setzen: `sudo passwd <Benutzername>`
- Benutzer ändern: `sudo usermod -aG <Gruppe> <Benutzername>`
- Benutzer löschen: `sudo userdel -r <Benutzername>`

### Dateisystemverwaltung
- Speicherplatz prüfen: `df -h`
- Eingehängte Dateisysteme auflisten: `lsblk`
- Partitionen verwalten: Verwenden Sie `fdisk` oder `parted` für die Festplattenpartitionierung.
- LVM (Logical Volume Manager) konfigurieren:
  - Physikalischen Volume erstellen: `pvcreate /dev/sdX`
  - Volume-Gruppe erstellen: `vgcreate <VG-Name> /dev/sdX`
  - Logischen Volume erstellen: `lvcreate -L <Größe> -n <LV-Name> <VG-Name>`

### Netzwerkkonfiguration
- Netzwerk mit `nmcli` konfigurieren:
  - Verbindungen auflisten: `nmcli connection show`
  - Statische IP hinzufügen: `nmcli con mod <Verbindungsname> ipv4.addresses 192.168.1.100/24 ipv4.gateway 192.168.1.1 ipv4.method manual`
  - Verbindung aktivieren: `nmcli con up <Verbindungsname>`
- Firewall mit `firewalld` verwalten:
  - Port öffnen: `sudo firewall-cmd --add-port=80/tcp --permanent`
  - Firewall neu laden: `sudo firewall-cmd --reload`

### Sicherheit
- **SELinux**:
  - Status prüfen: `sestatus`
  - Modus setzen (enforcing/permissive): `sudo setenforce 0` (permissive) oder `sudo setenforce 1` (enforcing)
  - Richtlinien ändern: Verwenden Sie `semanage` und `audit2allow` für benutzerdefinierte Richtlinien.
- **Updates**:
  - Sicherheitsupdates anwenden: `sudo dnf update --security`
- **SSH**:
  - SSH absichern: Bearbeiten Sie `/etc/ssh/sshd_config`, um Root-Login zu deaktivieren (`PermitRootLogin no`) und den Standardport zu ändern.
  - SSH neu starten: `sudo systemctl restart sshd`

## Erweiterte Funktionen
### Container und Virtualisierung
- **Podman**: RHELs rootless Container-Tool.
  - Container ausführen: `podman run -it docker.io/library/centos bash`
  - Image erstellen: `podman build -t <Image-Name> .`
- **Virtualisierung**: Verwenden Sie `libvirt` und `virt-manager` zur Verwaltung von VMs.
  - Installieren: `sudo dnf install libvirt virt-manager`
  - Libvirt starten: `sudo systemctl start libvirtd`

### Automatisierung mit Ansible
- Ansible installieren: `sudo dnf install ansible`
- Playbook erstellen:
  ```yaml
  - name: Installiere Apache
    hosts: all
    tasks:
      - name: Installiere httpd
        dnf:
          name: httpd
          state: present
  ```
- Playbook ausführen: `ansible-playbook playbook.yml`

### Cloud-Integration
- RHEL integriert sich mit AWS, Azure und Google Cloud.
- Verwenden Sie Red Hat OpenShift für die Container-Orchestrierung.
- Stellen Sie RHEL-Images in Cloud-Umgebungen über Red Hat Cloud Access bereit.

## Problembehandlung
- **Logs**: Prüfen Sie `/var/log` auf Systemprotokolle (z.B. `/var/log/messages` oder `/var/log/secure`).
- **Systemd**: Verwalten Sie Dienste mit `systemctl`:
  - Dienststatus prüfen: `systemctl status <Dienst>`
  - Dienst neu starten: `systemctl restart <Dienst>`
- **Leistung**: Verwenden Sie `top`, `htop` oder `vmstat`, um die Systemleistung zu überwachen.
- **Netzwerkprobleme**: Verwenden Sie `ping`, `traceroute` oder `nslookup` für die Diagnose.

## Best Practices
- Aktualisieren Sie das System regelmäßig, um Schwachstellen zu patchen.
- Verwenden Sie starke Passwörter und setzen Sie SELinux-Richtlinien durch.
- Sichern Sie kritische Daten mit Tools wie `rsync` oder Red Hats `rear`.
- Überwachen Sie die Systemintegrität mit Tools wie Cockpit (`sudo dnf install cockpit`).

## Ressourcen
- [Red Hat Customer Portal](https://access.redhat.com)
- [RHEL-Dokumentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux)
- [Red Hat Developer Program](https://developers.redhat.com)
- Community-Foren wie [Red Hat Discuss](https://discuss.redhat.com)