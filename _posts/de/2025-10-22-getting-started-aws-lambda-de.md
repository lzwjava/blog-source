---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Erste Schritte mit AWS Lambda
translated: true
type: note
---

### Erste Schritte mit AWS Lambda

AWS Lambda ist ein serverloser Compute-Service, der Ihren Code als Reaktion auf Ereignisse ausführt, ohne dass Sie Server verwalten müssen. Hier ist eine einsteigerfreundliche Schritt-für-Schritt-Anleitung zum Erstellen, Bereitstellen und Verwenden Ihrer ersten Lambda-Funktion. Diese basiert auf der offiziellen AWS-Dokumentation.

#### Voraussetzungen
- Ein aktives AWS-Konto. Falls Sie noch keines haben, können Sie sich unter [aws.amazon.com](https://aws.amazon.com/) registrieren.
- Grundlegende Kenntnisse einer Programmiersprache wie Node.js oder Python (Lambda unterstützt viele Laufzeitumgebungen).

#### Schritt 1: Erstellen einer Lambda-Funktion
1. Melden Sie sich in der AWS Management Console an und navigieren Sie zum Service Lambda (suchen Sie im Services-Menü nach "Lambda").
2. Klicken Sie auf der Seite "Functions" auf **Funktion erstellen**.
3. Wählen Sie **Von Grund auf neu authoren**.
4. Geben Sie einen **Funktionsnamen** ein (z. B. `my-first-function`).
5. Wählen Sie eine **Laufzeitumgebung** (z. B. Node.js 22.x oder Python 3.13).
6. Belassen Sie die Standardarchitektur (x86_64) und klicken Sie auf **Funktion erstellen**.

Dadurch wird automatisch eine Ausführungsrolle (eine IAM-Rolle) mit grundlegenden Berechtigungen erstellt, z. B. zum Schreiben von Logs in Amazon CloudWatch.

#### Schritt 2: Schreiben Sie Ihren Code
Ersetzen Sie im Code-Editor der Lambda-Konsole (unter dem Reiter **Code**) den standardmäßigen "Hello World"-Code durch etwas Einfacheres. Hier ist ein Beispiel, das die Fläche eines Rechtecks basierend auf einer JSON-Eingabe mit den Schlüsseln `length` und `width` berechnet.

- **Node.js-Beispiel**:
  ```javascript
  exports.handler = async (event) => {
    const length = event.length;
    const width = event.width;
    const area = length * width;
    console.log(`Die Fläche beträgt ${area}`);
    console.log('Log-Gruppe: /aws/lambda/' + process.env.AWS_LAMBDA_FUNCTION_NAME);
    return { area: area };
  };
  ```

- **Python-Beispiel**:
  ```python
  import json

  def lambda_handler(event, context):
    length = event['length']
    width = event['width']
    area = length * width
    print(f"Die Fläche beträgt {area}")
    print(f"Log-Gruppe: /aws/lambda/{context.function_name}")
    return {
        'statusCode': 200,
        'body': json.dumps({'area': area})
    }
  ```

Speichern Sie die Änderungen – die Bereitstellung erfolgt für interpretierte Sprachen automatisch.

Für kompilierte Sprachen (z. B. Java) erstellen Sie ein Bereitstellungspaket lokal und laden es über die Konsole oder die AWS CLI hoch.

#### Schritt 3: Testen Sie Ihre Funktion
1. Klicken Sie im Reiter **Test** auf **Neues Testereignis erstellen**.
2. Geben Sie einen Namen ein (z. B. `test-area-calc`).
3. Fügen Sie eine Beispiel-JSON-Eingabe ein:
   ```json
   {
     "length": 6,
     "width": 7
   }
   ```
4. Speichern Sie und klicken Sie auf **Test**.

Sehen Sie sich die Ergebnisse im Abschnitt **Ausführungsergebnisse** an (z. B. `{"area": 42}`). Überprüfen Sie die Logs in CloudWatch auf Details wie Dauer und Speichernutzung.

#### Schritt 4: Aufrufen und Überwachen
- **Manueller Aufruf**: Verwenden Sie die Test-Schaltfläche in der Konsole oder die AWS CLI: `aws lambda invoke --function-name my-first-function output.json`.
- **Ereignisgesteuerter Aufruf**: Verbinden Sie Trigger wie API Gateway, S3 Buckets oder DynamoDB Streams. Gehen Sie zum Reiter **Konfiguration** > **Trigger**, um sie hinzuzufügen.
- **Logs**: Werden automatisch an CloudWatch Logs gesendet. Einsehen unter [console.aws.amazon.com/cloudwatch/home#logsV2:log-groups](https://console.aws.amazon.com/cloudwatch/home#logsV2:log-groups) unter `/aws/lambda/Ihr-Funktionsname`.

Wichtige Konzepte:
- **Ereignisquellen/Trigger**: Services (z. B. S3-Upload), die Ihre Funktion mit Ereignisdaten (JSON-Payload) aufrufen.
- **Handler**: Der Einstiegspunkt (z. B. `index.handler` für Node.js), der das Ereignis verarbeitet.

#### Schritt 5: Bereinigung (Optional)
Löschen Sie die Funktion über die Konsole: Aktionen > Löschen. Entfernen Sie auch zugehörige Logs und IAM-Rollen, um Kosten zu vermeiden.

#### Tipps
- Beginnen Sie mit dem Free Tier (1 Mio. Anfragen/Monat).
- Verwenden Sie AWS SAM oder das Serverless Framework für erweiterte Bereitstellungen.
- Konfigurieren Sie für den Produktionseinsatz Umgebungsvariablen, Layers und VPC-Einstellungen im Reiter **Konfiguration**.

[Erstellen Sie Ihre erste Lambda-Funktion](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)