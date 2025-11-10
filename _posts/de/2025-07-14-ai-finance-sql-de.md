---
audio: false
generated: true
lang: de
layout: post
title: Einsatz von KI zur Verbesserung von Produkten in Finanzprojekten
translated: true
type: note
---

Basierend auf Ihrer Erfahrung mit der Arbeit an der Finance Transformation Platform, bei der Sie Backend-Systeme für die Finanzdatenverarbeitung, Workflows und Integrationen mit Tools wie Java, Spring Boot und Db2 verwalten, kann KI tatsächlich eine transformative Rolle spielen. Ihre Idee, KI zur "Suche nach Finanz-Headern" zu verwenden, passt gut zu Anwendungen der natürlichen Sprachverarbeitung (NLP), wie z. B. die Umwandlung von Benutzeranfragen in SQL für einen effizienten Datenabruf. Dies kann den Zugang zu komplexen Finanzdatensätzen demokratisieren und es nicht-technischen Beteiligten (z. B. Finanzteams) ermöglichen, Dinge wie Ledger-Einträge, Transaktionsheader oder Genehmigungsstatus abzufragen, ohne Code schreiben zu müssen. Ihr Beispiel zur Generierung von SQL aus natürlicher Sprache ist ein perfekter Ausgangspunkt – lassen Sie uns das aufschlüsseln und auf breitere Anwendungen ausweiten.

#### Analyse Ihres SQL-Generierungsbeispiels
Ihre Anfrage in natürlicher Sprache ("get some users whose firstname is andy, created_at around the day last month, who are 20 years old as of 2025, and whose last_login like recent week") ist eine solide Demonstration dafür, wie KI Alltagssprache mit Datenbankoperationen verbinden kann. Die von Ihnen bereitgestellte generierte SQL-Abfrage ist größtenteils effektiv und nutzt PostgreSQL-Funktionen gut:

```sql
SELECT *
FROM users
WHERE first_name ILIKE 'andy'
  AND CAST(created_at AS DATE) BETWEEN 
      (CURRENT_DATE - INTERVAL '1 MONTH' - INTERVAL '1 DAY') 
      AND 
      (CURRENT_DATE - INTERVAL '1 MONTH' + INTERVAL '1 DAY')
  AND EXTRACT(YEAR FROM AGE(date_of_birth)) = 20
  AND last_login >= CURRENT_TIMESTAMP - INTERVAL '7 DAYS';
```

- **Stärken**:
  - `ILIKE 'andy'` behandelt Groß-/Kleinschreibung, was benutzerfreundlich ist.
  - Die `created_at`-Klausel interpretiert "around the day last month" als ein Fenster von ±1 Tag um das entsprechende Datum im letzten Monat (z. B. wenn heute der 14. Juli 2025 ist, fragt es den 13.–15. Juni ab). Dies ist eine sinnvolle Annäherung für "ungefähr", obwohl die Formulierung etwas mehrdeutig ist – KI-Tools benötigen oft klare Prompts, um Fehlinterpretationen zu vermeiden.
  - `last_login >= CURRENT_TIMESTAMP - INTERVAL '7 DAYS'` erfasst "recent week" genau.

- **Mögliche Verbesserungen**:
  - Die Altersbedingung (`EXTRACT(YEAR FROM AGE(date_of_birth)) = 20`) berechnet das aktuelle Alter zum 14. Juli 2025 und wählt damit Benutzer aus, die heute genau 20 Jahre alt sind (unter Berücksichtigung, ob ihr Geburtstag bereits war). "20 years old as of 2025" könnte jedoch besser bedeuten, Benutzer auszuwählen, die im Jahr 2025 20 Jahre alt werden (d. h. im Jahr 2005 geboren). Eine einfachere, präzisere Alternative könnte sein:
    ```sql
    AND date_of_birth BETWEEN '2005-01-01' AND '2005-12-31'
    ```
    Oder gleichbedeutend:
    ```sql
    AND EXTRACT(YEAR FROM date_of_birth) = 2005
    ```
    Dies vermeidet Laufzeit-Altersberechnungen und konzentriert sich auf das Geburtsjahr, was für "as of [year]"-Abfragen in Finanz- oder Compliance-Kontexten (z. B. altersbasierte Berechtigung für Konten) oft stabiler ist.
  - Um sie robuster zu machen, fügen Sie Limits hinzu (z. B. `LIMIT 10`), wenn Sie "some users" möchten, und berücksichtigen Sie Zeitzonen für Zeitstempel, wenn das System global ist.
  - Passen Sie dies in einem Finanzprojekt an Ihre Db2-Datenbank an – PostgreSQL-Syntax wie `AGE()` und `ILIKE` muss möglicherweise angepasst werden (z. B. verwenden Sie `CURRENT DATE - date_of_birth` für das Alter und `LOWER(first_name) LIKE 'andy'`).

KI-Tools wie Copilot (das Sie, wie erwähnt, intensiv nutzen) oder fortschrittliche Modelle (z. B. über APIs von OpenAI oder Google Cloud) glänzen bei dieser NL-zu-SQL-Übersetzung. Integrieren Sie es in Ihrem Setup in Workflows, indem Sie eine Chatbot-Schnittstelle erstellen, die Abfragen zu Finanz-Headern analysiert (z. B. "Show unapproved headers from last quarter with balances over $10K") und SQL sicher generiert/ausführt, mit Schutzvorkehrungen für die Sicherheit.

#### Weitere Möglichkeiten, KI in finanziellen Backend-Systemen einzusetzen
In Projekten wie Ihrem – mit Fokus auf Datenimport/Validierung/Export, Workflows und Bankensystemen – kann KI die Effizienz steigern, Fehler reduzieren und Innovationen ermöglichen. Basierend auf Branchentrends hier einige praktische Anwendungen, die auf die Backend-Entwicklung zugeschnitten sind:

- **Automatisierung der Datenverarbeitung und -validierung**:
  - Verwenden Sie Machine-Learning (ML)-Modelle, um Anomalien in Finanzdatenimporten zu erkennen (z. B. ungewöhnliche Ledger-Einträge oder Ungleichheiten in Headern). Trainieren Sie beispielsweise Modelle auf historischen Daten, um Betrug oder Fehler während der Validierung zu kennzeichnen, was manuelle Überprüfungen potenziell um 30–50 % reduzieren könnte. Tools wie scikit-learn oder TensorFlow von Python (in Ihrer Umgebung verfügbar) können dies prototypisch umsetzen.
  - KI-gestützte OCR und NLP zur Dokumentenverarbeitung: Extrahieren Sie automatisch Daten aus PDFs oder gescannten Finanzberichten, klassifizieren Sie Header und integrieren Sie sie in Db2.

- **Optimierung von Workflows und Genehmigungen**:
  - Implementieren Sie prädiktive KI, um Engpässe in Workflows vorherzusagen (z. B. Genehmigungsverzögerungen für neue Header) basierend auf historischen Mustern. Dies könnte Zeitreihenanalysen verwenden, um Aufgaben in Control-M-Zeitplänen zu priorisieren.
  - Generative KI für dynamisches Routing: In Einreichungs-/Genehmigungsabläufen kann KI nächste Schritte vorschlagen oder niedrigrisiko Elemente automatisch genehmigen, was Releases von UAT zur Produktion beschleunigt.

- **Verbesserung der Code-Entwicklung und -Wartung**:
  - Erweitern Sie, wie Sie es mit Copilot für Root-Cause-Analysen, Python-Skripte und Dokumentation getan haben, auf KI-gestützte Code-Reviews oder Bug-Fixes. Für Multithreading-Probleme in Java/Spring Boot kann KI optimierte Code-Snippets generieren oder die Leistung profilen (ergänzend zu YourKit).
  - Ihre AspectJ-basierte KI-Agenten-Idee ist innovativ – das Sammeln von Logs und das Konvertieren von Debug-Zuständen in Text für die KI-Analyse. Dies könnte sich zu einer "bankenspezifischen IDE" wie Cursor entwickeln, in der KI Logs in natürlicher Sprache abfragt (z. B. "Why did this transaction fail?") und Lösungen vorschlägt. Zur Implementierung: Verwenden Sie AspectJ für Instrumentation, leiten Sie Logs an ein LLM weiter (über xAI API oder ähnliches) und bauen Sie eine Feedback-Schleife für kontinuierliche Verbesserung ein.

- **Erweiterte Analysen und Einblicke**:
  - NL-zu-SQL-Erweiterungen: Gehen Sie über Abfragen hinaus und nutzen Sie KI zur Generierung von Berichten über Finanztrends (z. B. "Summarize header submissions by department last month").
  - Risiko und Compliance: KI-Modelle für die Echtzeit-Bewertung von Kreditrisiken oder regulatorische Prüfungen, die Ledger-Daten analysieren, um Probleme vor dem Export vorherzusagen.

- **Skalierbarkeit und Integration**:
  - Nutzen Sie KI zur Systemoptimierung, wie z. B. automatische Skalierung von Ressourcen in WebSphere basierend auf Lastvorhersagen.
  - In Outsourcing-Setups kann KI die Dokumentation standardisieren (Sie erwähnten 50 Handbücher) und sie über semantische Suche auffindbar machen.

Diese Ansätze können zu Kosteneinsparungen (z. B. 20–30 % Produktivitätssteigerung in der Softwareentwicklung) und besseren Produkten führen, aber fangen Sie klein an: Testen Sie NL-zu-SQL in einer Sandbox, stellen Sie Datenschutz sicher (kritisch im Bankwesen) und messen Sie den ROI durch Metriken wie reduzierte Bereitstellungszeit.

Wenn Sie diesen KI-Agenten aufbauen, ziehen Sie Open-Source-Frameworks wie LangChain in Betracht, um Log-Analyse mit SQL-Generierung zu verketten. Für Preise zu APIs oder Abonnements prüfen Sie die offiziellen Websites, da die Details variieren.

**Referenzen**  
- [AI and bank software development | Deloitte Insights](https://www.deloitte.com/us/en/insights/industry/financial-services/financial-services-industry-predictions/2025/ai-and-bank-software-development.html)  
- [AI in Banking: Applications, Benefits and Examples | Google Cloud](https://cloud.google.com/discover/ai-in-banking)  
- [Extracting value from AI in banking: Rewiring the enterprise | McKinsey](https://www.mckinsey.com/industries/financial-services/our-insights/extracting-value-from-ai-in-banking-rewiring-the-enterprise)  
- [AI in Finance: Applications, Examples & Benefits | Google Cloud](https://cloud.google.com/discover/finance-ai)  
- [Top AI Applications in Finance for 2025: [Benefits & Success Stories] | Acropolium](https://acropolium.com/blog/artificial-intelligence-applications-in-finance-real-world-success-cases/)  
- [QueryGPT - Natural Language to SQL using Generative AI | Uber Blog](https://www.uber.com/blog/query-gpt/)  
- [NL2SQL with BigQuery and Gemini | Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/nl2sql-with-bigquery-and-gemini)