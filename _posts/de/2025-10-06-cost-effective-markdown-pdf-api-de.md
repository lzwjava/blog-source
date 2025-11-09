---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Kostengünstige Markdown-zu-PDF-API
translated: true
type: note
---

### Empfohlene günstige Option: Google Cloud Run

Für eine einfache Java-basierte API, die Markdown in PDF konvertiert (z.B. mit einer Bibliothek wie Flying Saucer oder iText), mit nur ~100 Anfragen pro Woche für die persönliche Blog-Nutzung, ist **Google Cloud Run** die kostengünstigste Wahl. Es ist eine serverlose Plattform, die containerisierte Apps ausführt, bei Inaktivität auf Null skaliert und nur für die tatsächliche Nutzung abrechnet. Keine Notwendigkeit, VMs zu verwalten oder sich um Always-On-Kosten zu kümmern – perfekt für Szenarien mit geringem Datenverkehr wie Ihres.

#### Warum Cloud Run statt anderer Optionen?
- **Verglichen mit Compute Engine (VMs)**: VMs haben feste Stundenkosten, selbst wenn sie im Leerlauf sind, was übertrieben und teurer wäre (~$5–10/Monat Minimum für eine kleine Instanz).
- **Verglichen mit App Engine**: Ähnliche serverlose Vorteile, aber Cloud Run ist flexibler für Java-Container und oft günstiger für sporadische Nutzung.
- Ihre Arbeitslast passt vollständig in den Free Tier, also erwarten Sie in der Praxis **$0/Monat**.

#### Geschätzte Kosten
Bei 100 Anfragen/Woche (~400/Monat):
- Gehen Sie davon aus, dass jede Anfrage 1 vCPU und 0,5 GiB Speicher für 10 Sekunden nutzt (konservativ für eine schnelle Markdown-zu-PDF-Konvertierung).
- Gesamtnutzung: ~4.000 vCPU-Sekunden und ~2.000 GiB-Sekunden/Monat.
- **Free Tier deckt alles ab**: 180.000 vCPU-Sekunden, 360.000 GiB-Sekunden und 2 Millionen Anfragen pro Monat (in den meisten Regionen).
- Falls Sie die Limits überschreiten (unwahrscheinlich), sind die Kosten ~$0,000024/vCPU-Sekunde + $0,0000025/GiB-Sekunde + $0,40/Million Anfragen nach den Free-Tier-Limits – immer noch unter $0,10/Monat.

Keine Egress-Gebühren für Ihren Anwendungsfall (interne API-Aufrufe innerhalb derselben Region bleiben kostenfrei).

#### Empfohlene Region: us-central1 (Iowa)
- Dies ist die günstigste Tier-1-Region für Cloud Run, mit den niedrigsten Sätzen für Compute und ohne Aufpreis für Latenz in Nordamerika.
- Die Preisgestaltung ist in allen Tier-1-Regionen (USA/Europa) ähnlich, aber us-central1 hat durchschnittlich geringere Instanzkosten.
- Wenn Sie sich außerhalb Nordamerikas befinden (z.B. Europa oder Asien), wechseln Sie zur nächstgelegenen Tier-1-Region wie europe-west1 (Belgien) für eine bessere Latenz – die Kosten unterscheiden sich um <10 %.
- Vermeiden Sie Tier-2-Regionen (z.B. asia-southeast1), da diese 20–50 % teurer sind.

#### Kurzanleitung für Ihren Java-Server
1. **Bauen Sie Ihre App**: Verwenden Sie Spring Boot für eine einfache REST-API. Endpunkt-Beispiel: POST `/convert` mit Markdown-Body, gibt PDF zurück.
   - Fügen Sie die Abhängigkeit hinzu: `implementation 'org.xhtmlrenderer:flying-saucer-pdf:9.1.22'` (oder ähnlich).
   - Code-Beispiel:
     ```java:disable-run
     @RestController
     public class MarkdownController {
         @PostMapping("/convert")
         public ResponseEntity<byte[]> convert(@RequestBody String markdown) {
             // Konvertierungslogik hier (z.B. Markdown zu HTML, dann zu PDF)
             byte[] pdfBytes = // Ihr Konvertierungsergebnis;
             return ResponseEntity.ok()
                 .header("Content-Type", "application/pdf")
                 .body(pdfBytes);
         }
     }
     ```
2. **Containerisieren**: Erstellen Sie eine `Dockerfile`:
   ```
   FROM openjdk:17-jdk-slim
   COPY target/your-app.jar app.jar
   ENTRYPOINT ["java", "-jar", "/app.jar"]
   ```
   Bauen: `docker build -t gcr.io/your-project/markdown-api .`
3. **Bereitstellung auf Cloud Run**:
   - Aktivieren Sie die Cloud Run API in der GCP Console.
   - `gcloud run deploy markdown-api --image gcr.io/your-project/markdown-api --platform managed --region us-central1 --allow-unauthenticated --memory 512Mi --cpu 1 --max-instances 1`
   - Erhalten Sie die URL: `https://markdown-api-abc.run.app/convert`
4. **Test**: Senden Sie eine Markdown-POST-Anfrage; sie skaliert automatisch.

Melden Sie sich für den $300-Free-Trial an, wenn Sie neu bei GCP sind. Überwachen Sie die Kosten im Billing-Dashboard.

[Cloud Run Pricing](https://cloud.google.com/run/pricing)  
[GCP Regions Guide](https://www.cloudzero.com/blog/gcp-regions/)  
[Cloud Run Quickstart](https://cloud.google.com/run/docs/quickstarts/build-and-deploy)