---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Nutzung von Amazon RDS für MySQL
translated: true
type: note
---

Amazon RDS (Relational Database Service) für MySQL ist ein verwalteter Datenbankdienst, der das Einrichten, Betreiben und Skalieren von MySQL-Datenbanken in der Cloud erleichtert. Er übernimmt Routineaufgaben wie Backups, Patchen und Skalieren, sodass Sie sich auf Ihre Anwendung konzentrieren können. Diese Anleitung führt Sie durch die Grundlagen: Erstellen einer MySQL-DB-Instanz, Verbinden mit dieser und Durchführen einfacher Operationen. Wir verwenden der Einfachheit halber die AWS Management Console.

**Hinweis zu Kosten:** Der AWS Free Tier bietet für neue Konten eingeschränkte Nutzung, aber für Ressourcen, die darüber hinausgehen, fallen Gebühren an. Löschen Sie Ressourcen immer, wenn Sie fertig sind, um unerwartete Rechnungen zu vermeiden. Für die Produktion befolgen Sie Sicherheits-Best Practices wie die Verwendung von VPCs, Verschlüsselung und Prinzip der geringsten Rechte.

## Voraussetzungen
- Ein AWS-Konto (falls benötigt, registrieren Sie sich unter [aws.amazon.com](https://aws.amazon.com)).
- Grundlegende Vertrautheit mit der AWS-Konsole und MySQL.
- Für Tests sicherer Verbindungen erstellen wir eine EC2-Instanz in derselben VPC (Virtual Private Cloud). Ermitteln Sie Ihre öffentliche IP-Adresse (z.B. über [checkip.amazonaws.com](https://checkip.amazonaws.com)) für SSH-Zugriff.
- Wählen Sie eine AWS-Region in Ihrer Nähe (z.B. US East (N. Virginia)).

**Best Practice:** Verwenden Sie eine private DB-Instanz in einer VPC, um den Zugriff nur auf vertrauenswürdige Ressourcen zu beschränken. Aktivieren Sie SSL/TLS für verschlüsselte Verbindungen.

## Schritt 1: Erstellen einer EC2-Instanz für die Verbindung
Dies richtet einen einfachen Linux-Server ein, um eine Verbindung zu Ihrer privaten DB-Instanz herzustellen.

1. Melden Sie sich in der [AWS Management Console](https://console.aws.amazon.com) an und öffnen Sie die EC2-Konsole.
2. Wählen Sie Ihre Region.
3. Klicken Sie auf **Launch instance**.
4. Konfigurieren Sie:
   - **Name:** `ec2-database-connect`.
   - **AMI:** Amazon Linux 2023 (Free Tier berechtigt).
   - **Instance type:** t3.micro (Free Tier berechtigt).
   - **Key pair:** Erstellen oder wählen Sie einen vorhandenen für SSH-Zugriff.
   - **Network settings:** Bearbeiten > Erlauben Sie SSH-Datenverkehr von **My IP** (oder Ihrer spezifischen IP, z.B. `192.0.2.1/32`). Vermeiden Sie `0.0.2.0/0` aus Sicherheitsgründen.
   - Belassen Sie die Standardeinstellungen für Storage und Tags.
5. Klicken Sie auf **Launch instance**.
6. Notieren Sie sich die Instance-ID, Public IPv4 DNS und den Key Pair-Namen aus den Instanzdetails.
7. Warten Sie, bis der Status **Running** anzeigt (2-5 Minuten).

**Sicherheitstipp:** Beschränken Sie SSH auf Ihre IP. Laden Sie den Key Pair (.pem-Datei) sicher herunter.

## Schritt 2: Erstellen einer MySQL-DB-Instanz
Verwenden Sie "Easy create" für einen schnellen Setup mit Standardeinstellungen.

1. Öffnen Sie die [RDS-Konsole](https://console.aws.amazon.com/rds/).
2. Wählen Sie dieselbe Region wie Ihre EC2-Instanz.
3. Klicken Sie im Navigationsbereich auf **Databases** > **Create database**.
4. Wählen Sie **Easy create**.
5. Unter **Configuration**:
   - Engine type: **MySQL**.
   - Templates: **Free tier** (oder **Sandbox** für kostenpflichtige Konten).
   - DB instance identifier: `database-test1` (oder Ihre Wahl).
   - Master username: `admin` (oder benutzerdefiniert).
   - Master password: Automatisch generieren oder setzen Sie ein starkes Passwort (speichern Sie es sicher).
6. (Optional) Unter **Connectivity** wählen Sie **Connect to an EC2 compute resource** und wählen Ihre EC2-Instanz für einfacheren Setup.
7. Klicken Sie auf **Create database**.
8. Sehen Sie sich das Anmeldeinformationen-Popup an (Benutzername/Passwort) – speichern Sie diese, da das Passwort später nicht abrufbar ist.
9. Warten Sie, bis sich der Status zu **Available** ändert (bis zu 10-20 Minuten). Notieren Sie den **Endpoint** (DNS-Name) und Port (Standard: 3306) vom Tab **Connectivity & security**.

**Best Practice:** Für die Produktion verwenden Sie "Standard create", um VPC, Backups (automatisiert aktivieren) und Storage anzupassen. Aktivieren Sie Deletion Protection und Multi-AZ für hohe Verfügbarkeit.

## Schritt 3: Verbinden mit der DB-Instanz
Stellen Sie von Ihrer EC2-Instanz aus eine Verbindung mit dem MySQL-Client her.

1. SSH in Ihre EC2-Instanz:
   ```
   ssh -i /pfad/zu/ihrem-key-pair.pem ec2-user@ihr-ec2-public-dns
   ```
   (Ersetzen Sie mit Ihren Daten; z.B. `ssh -i ec2-database-connect-key-pair.pem ec2-user@ec2-12-345-678-90.compute-1.amazonaws.com`.)

2. Aktualisieren Sie auf der EC2-Instanz die Pakete:
   ```
   sudo dnf update -y
   ```

3. Installieren Sie den MySQL-Client:
   ```
   sudo dnf install mariadb105 -y
   ```

4. Verbinden Sie sich mit der DB:
   ```
   mysql -h ihr-db-endpoint -P 3306 -u admin -p
   ```
   Geben Sie das Master-Passwort ein, wenn dazu aufgefordert.

Bei Erfolg sehen Sie die MySQL-Eingabeaufforderung (`mysql>`).

**Fehlerbehebung:** Stellen Sie sicher, dass die Security Groups eingehenden Datenverkehr auf Port 3306 von der EC2-Instanz erlauben. Für externe Verbindungen machen Sie die DB öffentlich (nicht empfohlen) oder verwenden Sie Bastion Hosts/VPN.

**Sicherheitstipp:** Verwenden Sie `--ssl-mode=REQUIRED` für verschlüsselte Verbindungen: `mysql -h endpoint -P 3306 -u admin -p --ssl-mode=REQUIRED`.

## Schritt 4: Grundlegende Verwendung
Sobald verbunden, können Sie SQL-Befehle ausführen. Beispiele:

- Datenbanken anzeigen: `SHOW DATABASES;`
- Eine Beispieldatenbank erstellen: `CREATE DATABASE myapp;`
- Verwenden: `USE myapp;`
- Eine Tabelle erstellen:
  ```
  CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
  );
  ```
- Daten einfügen: `INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');`
- Abfrage: `SELECT * FROM users;`
- Beenden: `EXIT;`

Verwenden Sie von Anwendungen (z.B. Python, Node.js) aus Standard-MySQL-Treiber mit Endpoint, Port, Benutzername und Passwort als Verbindungszeichenfolgen.

**Best Practice:** Überwachen Sie die Leistung via CloudWatch, aktivieren Sie automatisierte Backups und skalieren Sie vertikal (Instanzgröße) oder horizontal (Read Replicas) nach Bedarf.

## Bereinigung: Ressourcen löschen
Um Gebühren zu stoppen:

1. **EC2-Instanz löschen:** EC2-Konsole > Instanz auswählen > **Instance state** > **Terminate** > Bestätigen.
2. **DB-Instanz löschen:** RDS-Konsole > DB auswählen > **Actions** > **Delete** > Snapshot-Erstellung deaktivieren > Bestätigen.

Überprüfen Sie die AWS Billing-Konsole auf laufende Ressourcen.

Für fortgeschrittene Themen wie Migrationen, Performance-Optimierung oder API/CLI-Nutzung lesen Sie die AWS-Dokumentation.

## Referenzen
- [Creating and connecting to a MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html)
- [Amazon RDS for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html)
- [Getting started with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html)