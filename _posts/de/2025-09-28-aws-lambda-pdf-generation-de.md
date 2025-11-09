---
audio: false
generated: true
image: false
lang: de
layout: post
model: anthropic/claude-sonnet-4
title: AWS Lambda für die PDF-Generierung
translated: true
type: note
---

Ja, AWS Lambda (oder ähnliche serverlose Funktionen) ist perfekt für Ihren Anwendungsfall! Genau dafür wurde serverlose Rechenleistung entwickelt – für unregelmäßige, sporadische Workloads, bei denen Sie keine Infrastruktur im Leerlauf betreiben möchten.

Hier ist der Grund, warum Lambda für Ihre PDF-Generierung sinnvoll ist:

**Kostenvorteile:**
- Sie zahlen nur, wenn die Funktion ausgeführt wird (pro Anfrage + Ausführungszeit)
- Keine Kosten im Leerlauf – entscheidend für Ihre Nutzung 1-2 Mal pro Tag
- Der Lambda Free Tier beinhaltet 1 Mio. Anfragen/Monat und 400.000 GB-Sekunden
- Bei einigen hundert Nutzern mit geringer PDF-Nutzung bleiben Sie wahrscheinlich im Free Tier

**Technischer Ansatz:**
```
Blog → API Gateway → Lambda-Funktion → PDF-Generierung → S3-Speicher → URL zurückgeben
```

**Architektur-Optionen:**

1. **Einfache Lambda + Puppeteer/Playwright:**
   - Lambda-Funktion mit Headless-Browser zur Konvertierung von HTML in PDF
   - Gut für gestylte Blog-Inhalte
   - Kalter Start ~2-3 Sekunden, aber für Ihre Nutzung akzeptabel

2. **Lambda + PDF-Bibliotheken:**
   - Verwenden Sie Bibliotheken wie jsPDF, PDFKit oder wkhtmltopdf
   - Schnellere Ausführung, kleinere Paketgröße
   - Besser für textlastige Inhalte

3. **Hybrid-Ansatz:**
   - Lambda generiert PDF und speichert es in S3
   - CloudFront für PDF-Auslieferung
   - Optional: SQS für asynchrone Verarbeitung

**Alternative serverlose Optionen:**
- **Vercel Functions** – falls Ihr Blog auf Vercel läuft
- **Netlify Functions** – ähnliches Konzept
- **Google Cloud Functions** – vergleichbare Preise
- **Railway/Render** – serverlose Container

Für Ihre Größenordnung (einige hundert Nutzer, 1-2 PDF-Anfragen/Tag) würde Lambda Sie praktisch nichts kosten und gleichzeitig die Server-Wartung vollständig eliminieren. Viel besser, als einen Server 24/7 für gelegentliche PDF-Generierung am Laufen zu halten.

Möchten Sie, dass ich einen bestimmten Implementierungsansatz näher erläutere?