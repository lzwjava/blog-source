---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Lesen von AWS CloudWatch Logs
translated: true
type: note
---

### Einführung in das Lesen von Logs in AWS CloudWatch
AWS CloudWatch Logs ist ein Dienst, der Logdateien von Ihren AWS-Ressourcen (wie EC2-Instanzen, Lambda-Funktionen oder RDS-Datenbanken) und Anwendungen zentralisiert, überwacht und speichert. Um Logs zu lesen, müssen Sie zunächst sicherstellen, dass Logs an CloudWatch gesendet werden (z. B. über den CloudWatch-Agenten auf EC2 oder automatische Integration mit anderen Diensten). Nach der Einrichtung können Sie Logs über die AWS Management Console, die AWS CLI oder programmgesteuert über SDKs einsehen.

### Voraussetzungen
- **AWS-Berechtigungen**: Stellen Sie sicher, dass Ihr IAM-Benutzer oder Ihre IAM-Rolle über die Berechtigungen `logs:DescribeLogGroups`, `logs:DescribeLogStreams`, `logs:GetLogEvents` und `logs:FilterLogEvents` verfügt (hängen Sie die Richtlinie `CloudWatchLogsReadOnlyAccess` an).
- **Log-Konfiguration**: Logs müssen an CloudWatch weitergeleitet werden. Zum Beispiel:
  - Installieren Sie den CloudWatch Logs Agent auf EC2-Instanzen.
  - Aktivieren Sie die Protokollierung in Diensten wie Lambda oder ECS.
- **AWS CLI (Optional)**: Wenn Sie die CLI verwenden, installieren und konfigurieren Sie sie mit `aws configure`.

### Anzeigen von Logs in der AWS Management Console
1. Melden Sie sich bei der [AWS Management Console](https://console.aws.amazon.com/) an und öffnen Sie den CloudWatch-Dienst.
2. Wählen Sie im linken Navigationsbereich **Logs** > **Log-Gruppen**.
3. Wählen Sie die Log-Gruppe aus, die Ihre Logs enthält (z. B. `/aws/lambda/my-function` für Lambda-Logs).
4. Wählen Sie in der Liste der Log-Streams (unter der ausgewählten Log-Gruppe) den spezifischen Stream aus (z. B. einen pro Instanz oder Ausführung).
5. Die Log-Ereignisse werden geladen. Passen Sie die Ansicht an:
   - **Ereignisse erweitern**: Klicken Sie auf den Pfeil neben einem Ereignis, um es zu erweitern, oder wechseln Sie oben über der Liste zur **Text**-Ansicht für Klartext.
   - **Filtern/Suchen**: Geben Sie einen Filter in das Suchfeld ein (z. B. "ERROR", um nur Fehlerzeilen anzuzeigen).
   - **Zeitbereich**: Klicken Sie auf die Zeitauswahl neben dem Suchfeld. Wählen Sie **Relativ** (z. B. letzte 1 Stunde) oder **Absolut** (benutzerdefinierte Daten) und schalten Sie zwischen UTC und lokaler Zeit um.
6. Scrollen Sie durch die Ereignisse oder laden Sie sie bei Bedarf herunter.

Für erweiterte Abfragen über mehrere Streams oder Gruppen hinweg verwenden Sie **CloudWatch Logs Insights** (unter Logs > Logs Insights). Schreiben Sie Abfragen wie `fields @timestamp, @message | filter @level = "ERROR" | sort @timestamp desc`, um Logs zu analysieren und zu visualisieren.

### Lesen von Logs mit der AWS CLI
Verwenden Sie diese Befehle, um Logs programmgesteuert aufzulisten und abzurufen. Ersetzen Sie Platzhalter wie `my-log-group` durch Ihre tatsächlichen Namen.

1. **Log-Gruppen auflisten**:
   ```
   aws logs describe-log-groups --log-group-name-prefix my-log-group
   ```
   Dies gibt Metadaten wie ARN, Aufbewahrungsdauer und gespeicherte Bytes zurück.

2. **Log-Streams in einer Gruppe auflisten**:
   ```
   aws logs describe-log-streams --log-group-name my-log-group --log-stream-name-prefix 2025
   ```
   Filtert Streams nach Präfix (z. B. datumsbasierte Namen) und zeigt Erstellungszeit und Größe an.

3. **Log-Ereignisse aus einem Stream abrufen**:
   ```
   aws logs get-log-events --log-group-name my-log-group --log-stream-name my-stream --start-time 1730137600000
   ```
   - `--start-time` und `--end-time`: Unix-Zeitstempel (Millisekunden) für den Zeitbereich.
   - `--limit`: Maximale Anzahl zurückzugebender Ereignisse (Standard 1.000).
   - Die Ausgabe enthält Zeitstempel, Erfassungszeit und Nachrichtentext.
   - Verwenden Sie `--next-token` aus der Antwort, um zu paginieren.

Für gefilterte Suchen über Streams hinweg verwenden Sie `filter-log-events`:
```
aws logs filter-log-events --log-group-name my-log-group --filter-pattern "ERROR" --start-time 1730137600000
```

### Tipps und Best Practices
- **Aufbewahrung**: Logs werden standardmäßig unbegrenzt aufbewahrt; passen Sie dies pro Gruppe an, um Kosten zu verwalten (z. B. 30 Tage).
- **Kosten**: Das Anzeigen ist kostenlos, aber die Erfassung und Speicherung verursacht Gebühren – überwachen Sie dies über CloudWatch-Metriken.
- **Fehlerbehebung**: Wenn keine Logs erscheinen, überprüfen Sie die Agent-Installation oder ob die Dienstprotokollierung aktiviert ist.
- Für die Echtzeitüberwachung richten Sie Metrikfilter oder Alarme auf Log-Muster ein.

[Working with log groups and log streams - Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html)  
[CloudWatch Logs examples using AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli_cloudwatch-logs_code_examples.html)  
[Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)