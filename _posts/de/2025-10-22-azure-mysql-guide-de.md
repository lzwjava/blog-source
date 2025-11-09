---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Leitfaden für Azure Database for MySQL Flexible Server
translated: true
type: note
---

Azure Database for MySQL ist ein vollständig verwalteter relationaler Datenbankdienst, der auf der MySQL Community Edition basiert. Er übernimmt Routineaufgaben wie Backups, Patchen und Überwachung, sodass Sie sich auf Ihre Anwendung konzentrieren können. Die empfohlene Bereitstellungsoption ist **Flexible Server**, die mehr Konfigurationsmöglichkeiten und eine bessere Leistung als der ältere Single Server (der eingestellt wird) bietet.

Diese Anleitung behandelt das Erstellen eines Servers, das Verbinden mit ihm und das Durchführen grundlegender Operationen. Sie basiert der Einfachheit halber auf dem Azure-Portal.

## Voraussetzungen
- Ein aktives Azure-Abonnement (falls benötigt, erstellen Sie eines unter [azure.microsoft.com](https://azure.microsoft.com/free/)).
- Zugriff auf das Azure-Portal (portal.azure.com).
- Grundlegende Kenntnisse von MySQL-Konzepten.
- Ausgehender Netzwerkzugriff auf Port 3306 (Standard für MySQL).
- MySQL Workbench für die Verbindung installiert (Download von [mysql.com](https://dev.mysql.com/downloads/workbench/)).

## Schritt 1: Erstellen eines Flexible Servers im Azure-Portal
Befolgen Sie diese Schritte, um Ihren Server bereitzustellen.

1. Melden Sie sich beim [Azure-Portal](https://portal.azure.com) an.

2. Suchen Sie in der oberen Suchleiste nach "Azure Database for MySQL Flexible Servers" und wählen Sie es aus.

3. Klicken Sie auf **Erstellen**, um den Assistenten zu starten.

4. Konfigurieren Sie auf dem Tab **Grundlagen**:
   - **Abonnement**: Wählen Sie Ihr Abonnement aus.
   - **Ressourcengruppe**: Erstellen Sie eine neue (z.B. `myresourcegroup`) oder wählen Sie eine bestehende aus.
   - **Servername**: Eindeutiger Name (z.B. `mydemoserver`), 3-63 Zeichen, Kleinbuchstaben/Zahlen/Bindestriche. Der vollständige Hostname lautet `<name>.mysql.database.azure.com`.
   - **Region**: Wählen Sie die Region in der Nähe Ihrer Benutzer.
   - **MySQL-Version**: 8.0 (neueste Hauptversion).
   - **Workload-Typ**: Entwicklung (für Tests; für Produktion Small/Medium verwenden).
   - **Compute + Speicher**: Burstable-Tarif, Standard_B1ms (1 vCore), 10 GiB Speicher, 100 IOPS, 7-Tage-Backups. Passen Sie dies bei Bedarf an (z.B. erhöhen Sie die IOPS für Migrationen).
   - **Verfügbarkeitszone**: Keine Präferenz (oder wählen Sie die Zone Ihrer App).
   - **Hohe Verfügbarkeit**: Für den Anfang deaktiviert (für Produktion zonenredundant aktivieren).
   - **Authentifizierung**: MySQL und Microsoft Entra (für Flexibilität).
   - **Administrator-Benutzername**: z.B. `mydemouser` (nicht root/admin/etc., max. 32 Zeichen).
   - **Passwort**: Starkes Passwort (8-128 Zeichen, Mix aus Groß-/Kleinbuchstaben/Zahlen/Symbolen).

5. Wechseln Sie zum Tab **Netzwerk**:
   - **Konnektivitätsmethode**: Öffentlicher Zugriff (der Einfachheit halber; privates VNet für Produktionssicherheit).
   - **Firewallregeln**: Fügen Sie Ihre aktuelle Client-IP-Adresse hinzu (oder erlauben Sie Azure-Dienste). Dies kann später nicht geändert werden.

6. Überprüfen Sie die Einstellungen unter **Überprüfen + erstellen** und klicken Sie dann auf **Erstellen**. Die Bereitstellung dauert 5-10 Minuten. Überwachen Sie sie über Benachrichtigungen.

7. Sobald dies abgeschlossen ist, heften Sie den Server an das Dashboard und gehen Sie zur Seite **Übersicht** der Ressource. Standarddatenbanken umfassen `information_schema`, `mysql` usw.

## Schritt 2: Verbinden mit Ihrem Server
Verwenden Sie MySQL Workbench für eine GUI-Verbindung. (Alternativen: Azure Data Studio, mysql CLI oder Azure Cloud Shell.)

1. Gehen Sie im Portal zur **Übersicht** Ihres Servers und notieren Sie:
   - Servername (z.B. `mydemoserver.mysql.database.azure.com`).
   - Administrator-Benutzername.
   - Setzen Sie das Passwort bei Bedarf zurück.

2. Öffnen Sie MySQL Workbench.

3. Klicken Sie auf **Neue Verbindung** (oder bearbeiten Sie eine bestehende).

4. Im Tab **Parameter**:
   - **Verbindungsname**: z.B. `Demo Connection`.
   - **Verbindungsmethode**: Standard (TCP/IP).
   - **Hostname**: Vollständiger Servername.
   - **Port**: 3306.
   - **Benutzername**: Administrator-Benutzername.
   - **Passwort**: Geben Sie es ein und speichern Sie es im Tresor.

5. Klicken Sie auf **Verbindung testen**. Falls dies fehlschlägt:
   - Überprüfen Sie die Details aus dem Portal.
   - Stellen Sie sicher, dass die Firewall Ihre IP-Adresse erlaubt.
   - TLS/SSL ist erzwungen (TLS 1.2); laden Sie das CA-Zertifikat von [DigiCert](https://dl.cacerts.digicert.com/DigiCertGlobalRootCA.crt.pem) herunter und binden Sie es bei Bedarf in Workbench ein (unter SSL-Tab: SSL verwenden > Erfordern und CA-Datei angeben).

6. Klicken Sie auf **OK**, um zu speichern. Doppelklicken Sie auf die Verbindungskachel, um einen Query-Editor zu öffnen.

## Schritt 3: Erstellen und Verwalten von Datenbanken
Sobald verbunden, können Sie Datenbanken über das Portal oder den Client verwalten.

### Über das Azure-Portal:
1. Wählen Sie auf der Seite Ihres Servers im linken Menü **Datenbanken** aus.
2. Klicken Sie auf **+ Hinzufügen**:
   - **Datenbankname**: z.B. `testdb`.
   - **Zeichensatz**: utf8 (Standard).
   - **Sortierung**: utf8_general_ci.
3. Klicken Sie auf **Speichern**.

Zum Löschen: Wählen Sie die Datenbank(en) aus und klicken Sie auf **Löschen**.

### Über MySQL Workbench (SQL-Abfragen):
Führen Sie diese im Query-Editor aus:

- Datenbank erstellen: `CREATE DATABASE testdb CHARACTER SET utf8 COLLATE utf8_general_ci;`
- Datenbanken auflisten: `SHOW DATABASES;`
- Datenbank verwenden: `USE testdb;`
- Tabelle erstellen: `CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));`
- Daten einfügen: `INSERT INTO users (name) VALUES ('Alice');`
- Abfrage: `SELECT * FROM users;`

Commiten Sie Änderungen mit `COMMIT;`, falls kein Auto-Commit aktiviert ist.

## Grundlegende Verwendungstipps
- **Skalierung**: Unter **Übersicht** > **Compute + Speicher** können Sie vCores/Speicher/IOPS anpassen (bei den meisten Änderungen ohne Ausfallzeit).
- **Backups**: Automatisiert täglich; Point-in-Time-Wiederherstellung bis zu 35 Tage (konfigurierbar in den **Sicherungseinstellungen**).
- **Überwachung**: Verwenden Sie **Metriken** für CPU-/Speichereinblicke; richten Sie Warnungen ein.
- **Sicherheit**: Verwenden Sie immer SSL (erzwungen). Für die Produktion, aktivieren Sie hohe Verfügbarkeit, privates Networking und Entra ID-Authentifizierung.
- **Migration**: Verwenden Sie mysqldump für kleine Datenbanken; DMS für große.
- **Kosten**: Sie zahlen für Compute/Speicher; starten Sie klein und skalieren Sie. Verwenden Sie den Rechner unter [azure.microsoft.com](https://azure.microsoft.com/pricing/calculator/).
- **Bereinigung**: Löschen Sie die Ressourcengruppe, um den Server zu entfernen und Gebühren zu vermeiden.

Für erweiterte Funktionen wie Lesereplikate oder Serverparameter, erkunden Sie das linke Menü im Portal.

## Referenzen
- [Schnellstart: Erstellen eines Flexible Servers über das Azure-Portal](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/quickstart-create-server-portal)
- [Verbinden mit MySQL Workbench](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-workbench)
- [Erstellen und Verwalten von Datenbanken](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/how-to-create-manage-databases)
- [Azure Database for MySQL-Dokumentation](https://learn.microsoft.com/en-us/azure/mysql/)