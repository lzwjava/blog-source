---
audio: false
generated: true
image: false
lang: de
layout: post
title: RHEL Kompletter Enterprise Linux Leitfaden
translated: true
type: note
---

Hier ist ein **umfassender Leitfaden zu Red Hat Enterprise Linux (RHEL)**. Ich habe ihn Schritt für Schritt strukturiert, damit du ihn sowohl als Lernpfad als auch als Nachschlagewerk verwenden kannst.

---

## 1. Einführung in Red Hat Linux

Red Hat Enterprise Linux (RHEL) ist eine kommerzielle Linux-Distribution, die von **Red Hat, Inc.** entwickelt wurde und auf **Stabilität, Sicherheit und Enterprise-Support** ausgelegt ist. Aufgrund seines langfristigen Support-Lebenszyklus und zertifizierten Software-Ökosystems wird es häufig im Banken- und Gesundheitswesen, in Regierungsbehörden und in Unternehmens-IT-Abteilungen eingesetzt.

Wichtige Highlights:

* Enterprise-grade Support (10+ Jahre Lebenszyklus pro Major-Release).
* Zertifiziert für Major-Hardware (Dell, HP, IBM, etc.).
* Weit verbreitet in der Cloud (AWS, Azure, GCP), in Containern (OpenShift, Kubernetes) und in der Virtualisierung.

---

## 2. Installation und Einrichtung

* **Download**: Offizielle ISO-Images sind über das Red Hat Customer Portal erhältlich (erfordert ein Subscription).
* **Installer**: Verwendet den **Anaconda-Installer** mit grafischen und Text-Modi.
* **Partitionierung**: Optionen für LVM, XFS (Standard-Dateisystem) und verschlüsselte Festplatten.
* **Tools nach der Installation**: `subscription-manager` zum Registrieren des Systems.

---

## 3. Paketverwaltung

* **RPM (Red Hat Package Manager)** – das zugrundeliegende Format für Software.
* **DNF (Dandified Yum)** – der standardmäßige Paketmanager in RHEL 8 und höher.

  * Ein Paket installieren:

    ```bash
    sudo dnf install httpd
    ```
  * System aktualisieren:

    ```bash
    sudo dnf update
    ```
  * Pakete durchsuchen:

    ```bash
    sudo dnf search nginx
    ```

RHEL unterstützt auch **AppStreams** für mehrere Versionen von Software (z. B. Python 3.6 vs. 3.9).

---

## 4. Systemadministrations-Grundlagen

* **Benutzerverwaltung**:
  `useradd`, `passwd`, `usermod`, `/etc/passwd`, `/etc/shadow`
* **Prozessverwaltung**:
  `ps`, `top`, `htop`, `kill`, `systemctl`
* **Festplattenverwaltung**:
  `lsblk`, `df -h`, `mount`, `umount`, `fdisk`, `parted`
* **Systemdienste** (systemd):

  ```bash
  systemctl start nginx
  systemctl enable nginx
  systemctl status nginx
  ```

---

## 5. Netzwerkkonfiguration

* Die Konfiguration wird in `/etc/sysconfig/network-scripts/` gespeichert.
* Befehle:

  * `nmcli` (NetworkManager CLI)
  * `ip addr`, `ip route`, `ping`, `traceroute`
* Firewall:

  * Verwaltet von **firewalld** (`firewall-cmd`).
  * Beispiel:

    ```bash
    firewall-cmd --add-service=http --permanent
    firewall-cmd --reload
    ```

---

## 6. Sicherheit

* **SELinux**: Mandatory-Access-Control-System.

  * Status prüfen: `sestatus`
  * Modi: enforcing, permissive, disabled
* **FirewallD**: Verwaltet die Netzwerksicherheit.
* **Systemupdates**: Sicherheitspatches via `dnf update`.
* **Auditd**: Protokollierung und Compliance.

---

## 7. Protokollierung und Monitoring

* **Systemprotokolle**:
  Gespeichert unter `/var/log/`.
* **Journald**:
  `journalctl -xe`
* **Performance-Tools**:

  * `sar` (sysstat-Paket)
  * `vmstat`, `iostat`, `dstat`
* **Red Hat Insights**: Cloud-basierte Systemanalyse.

---

## 8. Virtualisierung und Container

* **KVM** (Kernel-based Virtual Machine) für Virtualisierung.
* **Podman** (anstelle von Docker):

  ```bash
  podman run -it centos /bin/bash
  ```
* **OpenShift** (Kubernetes-Plattform) für Orchestrierung.

---

## 9. Speicherverwaltung

* **LVM (Logical Volume Manager)** für flexible Festplattenverwaltung.
* **XFS**: Standard-Dateisystem.
* **Stratis**: Speicherverwaltung mit Thin Provisioning und Snapshots.

---

## 10. Automatisierung und Konfigurationsmanagement

* **Ansible**: Die Automatisierungsplattform von Red Hat.
* **Kickstart**: Automatisiert Betriebssysteminstallationen.
* **System Roles**: Vordefinierte Ansible-Rollen für RHEL.

---

## 11. Subscriptions und Support

* Red Hat verwendet ein **Subscription-Modell**.
* `subscription-manager` zum Registrieren, Zuweisen von Subscriptions und Aktivieren von Repositories.
* Die RHEL-Developer-Subscription ist **für Einzelpersonen kostenlos**.

---

## 12. Best Practices

* Halten Sie Systeme stets mit Sicherheitspatches aktuell.
* Verwenden Sie SELinux im Enforcing-Modus, es sei denn, Sie debuggen.
* Zentralisieren Sie die Protokollierung mit `rsyslog` oder dem ELK-Stack.
* Automatisieren Sie repetitive Aufgaben mit Ansible.
* Überwachen Sie die Systemintegrität mit Red Hat Insights.

---

## 13. Lernressourcen

* [Red Hat Dokumentation](https://access.redhat.com/documentation)
* [Red Hat Academy](https://www.redhat.com/en/services/training-and-certification/red-hat-academy)
* Zertifizierungen:

  * **RHCSA** (Red Hat Certified System Administrator)
  * **RHCE** (Red Hat Certified Engineer)
  * **RHCA** (Red Hat Certified Architect)

---

✅ Das ist die Grundlage.
Soll ich dies zu einem praktischen **"Hands-on-Leitfaden"** mit realen Befehlen und Workflows erweitern (wie das Einrichten eines Webservers, einer Datenbank, einer Firewall usw.) oder soll es **theoretischer und konzeptioneller** bleiben?