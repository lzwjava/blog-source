---
audio: false
generated: true
lang: de
layout: post
title: Präzise und sichere NL-zu-SQL-Systeme
translated: true
type: note
---

### Wichtige Schwerpunkte beim Aufbau eines NL-to-SQL-Systems

Der Aufbau eines Natural Language to SQL (NL-to-SQL)-Systems beinhaltet die Übersetzung von Benutzeranfragen in Alltagssprache in ausführbare SQL-Anweisungen, oft unter Verwendung von KI-Modellen wie LLMs (z. B. GPT-Varianten oder spezialisierte Modelle von Hugging Face). Basierend auf Ihrem PostgreSQL-Schema und der Beispielabfrage sind hier die Hauptbereiche, auf die Sie sich konzentrieren sollten:

#### 1. **Genauigkeit und Verständnis des Schemas**
   - **Schema-Bewusstsein**: Stellen Sie immer das vollständige Datenbankschema (Tabellen, Spalten, Datentypen, Beziehungen) im AI-Prompt bereit. Dies hilft dem Modell, korrekte SQL-Anweisungen zu generieren. Betonen Sie in Ihrem Fall Spalten wie `first_name`, `created_at`, `date_of_birth` und `last_login`, um Halluzinationen zu vermeiden (z. B. das Erfinden nicht existierender Felder).
   - **Umgang mit Mehrdeutigkeit**: Natürliche Sprache ist vage – z. B. könnte "um den Tag letzten Monat" ±1 Tag bedeuten, klären Sie dies jedoch über Prompts, um unscharfe Begriffe zu interpretieren (z. B. "letzte Woche" als 7 Tage). Verwenden Sie Beispiele in Prompts, um Interpretationen zu steuern.
   - **Datentypen und Funktionen**: Konzentrieren Sie sich auf PostgreSQL-spezifische Syntax, wie die Verwendung von `AGE()` für Datumsangaben, `ILIKE` für Groß-/Kleinschreibung-ignorierende Zeichenketten und korrektes Casting (z. B. `CAST(created_at AS DATE)` in Ihrem Beispiel). Trainieren oder finetunen Sie das Modell auf SQL-Dialektunterschiede.
   - **Grenzfälle**: Behandeln Sie komplexe Abfragen wie Joins (bei mehreren Tabellen), Aggregationen (z. B. COUNT, SUM) oder Unterabfragen. Testen Sie Abfragen, die sensible Felder wie `password_hash` oder `account_balance` betreffen.

#### 2. **Leistung und Optimierung**
   - Generieren Sie effizientes SQL: Ermutigen Sie das Modell, Indizes zu verwenden (z. B. auf `created_at` oder `first_name`), Ergebnisse zu begrenzen (standardmäßig `LIMIT` hinzufügen) und Full-Table Scans zu vermeiden.
   - Skalierbarkeit: Integrieren Sie für große Datensätze Abfrageoptimierungstools oder validieren Sie generiertes SQL gegen einen Explain Plan.

#### 3. **Fehlerbehandlung und Validierung**
   - Parsen und validieren Sie generiertes SQL vor der Ausführung (z. B. mit einer SQL-Parser-Bibliothek wie `sqlparse` in Python).
   - Bieten Sie Fallback-Antworten: Wenn die Abfrage unklar ist, fordern Sie den Benutzer zur Klärung auf, anstatt ungültiges SQL zu generieren.

#### 4. **Sicherheit und Sicherheitsaspekte**
   - **Verhindern von SQL-Injection**: Das Risiko entsteht durch die Ausführung des generierten SQL. Fügen Sie Benutzereingaben niemals direkt in SQL-Strings ein. Verwenden Sie stattdessen:
     - **Parametrisierte Abfragen** oder Prepared Statements bei der Ausführung (z. B. in Python mit `psycopg2`: `cursor.execute("SELECT * FROM users WHERE first_name = %s", (name,))`).
     - Weisen Sie die KI an, SQL mit Platzhaltern zu generieren (z. B. `WHERE first_name ILIKE %s`) und Werte separat zu binden.
     - Bereinigen Sie NL-Eingaben: Vorverarbeiten Sie Benutzerabfragen, um schädliche Muster zu entfernen (z. B. mit Regex, um SQL-Schlüsselwörter wie "DROP" oder ";" zu erkennen).
     - Beschränken Sie auf schreibgeschützten Zugriff: Beschränken Sie die KI auf die Generierung von SELECT-Abfragen – blockieren Sie DDL (z. B. CREATE/DROP) oder DML (z. B. INSERT/UPDATE) über Prompt-Anweisungen wie "Nur SELECT-Anweisungen generieren; Daten nicht ändern."
   - **Kontrollieren des Datenzugriffs**:
     - **Row-Level Security (RLS)**: Aktivieren Sie in PostgreSQL RLS-Richtlinien für Tabellen (z. B. `ALTER TABLE users ENABLE ROW LEVEL SECURITY; CREATE POLICY user_policy ON users USING (role = current_user);`). Dies stellt sicher, dass Abfragen nur Zeilen zurückgeben, auf die der Benutzer Zugriff hat.
     - **Views und Rollen**: Erstellen Sie eingeschränkte Views (z. B. `CREATE VIEW safe_users AS SELECT id, username, first_name FROM users;`) und gewähren Sie Zugriff über Datenbankrollen. Die KI sollte Views anstelle von Basistabellen abfragen.
     - **API-Layer**: Verpacken Sie das System in eine API (z. B. mit FastAPI), die Benutzer authentifiziert und Zugriffskontrollen anwendet (z. B. JWT-Tokens zur Bestimmung der Benutzerrolle).
     - **Sandbox-Ausführung**: Führen Sie Abfragen in einer schreibgeschützten Replikationsdatenbank oder einer containerisierten Umgebung (z. B. Docker) aus, um sie von Produktionsdaten zu isolieren.
     - **Audit-Logging**: Protokollieren Sie alle generierten SQL-Anweisungen und Ausführungen zur Überwachung.
   - **Datenschutz**: Vermeiden Sie die Offenlegung sensibler Spalten (z. B. `password_hash`, `email`), indem Sie sie in Prompts auf eine Blacklist setzen: "Sensible Felder wie password_hash, email nicht auswählen, es sei denn, sie werden ausdrücklich benötigt und sind autorisiert."
   - **Ratenbegrenzung und Kontingente**: Verhindern Sie Missbrauch, indem Sie die Anzahl der Abfragen pro Benutzer/Sitzung begrenzen.

#### 5. **Prompt-Engineering für kontrollierte Konvertierung**
   - Die Qualität von NL-to-SQL hängt stark davon ab, wie Sie die KI anweisen. Verwenden Sie strukturierte Prompts mit diesen Elementen:
     - **System-Prompt-Vorlage**:
       ```
       Sie sind ein Experte für die SQL-Generierung für PostgreSQL. Generieren Sie anhand des untenstehenden Schemas und einer natürlichen Sprachabfrage eine sichere, genaue SELECT-Abfrage.

       Schema:
       [Fügen Sie hier das vollständige Schema ein, z. B. CREATE TABLE users (...)]

       Regeln:
       - Generieren Sie nur SELECT-Anweisungen. Keine INSERT-, UPDATE-, DELETE- oder DDL-Anweisungen.
       - Verwenden Sie parametrisierte Platzhalter (z. B. %s) für vom Benutzer bereitgestellte Werte, um Injection zu verhindern.
       - Behandeln Sie Datumsangaben mit PostgreSQL-Funktionen wie AGE(), CURRENT_DATE, INTERVAL.
       - Interpretieren Sie mehrdeutige Begriffe (z. B. "um letzten Monat") als [spezifische Regel, z. B. ±1 Tag vom gleichen Tag letzten Monats].
       - Begrenzen Sie die Ergebnisse auf 100 Zeilen, sofern nicht anders angegeben.
       - Wenn die Abfrage das Alter betrifft, berechnen Sie es auf Basis des aktuellen Jahres oder eines bestimmten Jahres (z. B. EXTRACT(YEAR FROM AGE(CURRENT_DATE, date_of_birth)) = 20).
       - Wählen Sie keine sensiblen Spalten wie password_hash, email aus.
       - Wenn die Abfrage unklar ist, antworten Sie mit "Klärung erforderlich: [Frage]".

       Benutzerabfrage: [NL-Abfrage]
       ```
     - **Beispiele in Prompts**: Nehmen Sie 2-3 Beispiele (Few-Shot) auf, wie Ihre bereitgestellte Abfrage und generiertes SQL, um das Modell zu führen.
     - **Chain of Thought**: Weisen Sie das Modell an, schrittweise zu argumentieren: "Erstens, identifizieren Sie die Schlüsselfilter. Zweitens, ordnen Sie diese Spalten zu. Drittens, bauen Sie die WHERE-Klausel auf."
     - **Fine-Tuning**: Wenn Sie ein benutzerdefiniertes Modell verwenden, finetunen Sie es auf Datensätzen wie Spider oder WikiSQL, angereichert mit Ihren schema-spezifischen Beispielen.
     - **Testen**: Evaluieren Sie mit Metriken wie Ausführungsgenauigkeit (läuft es ohne Fehler?) und semantischer Übereinstimmung (liefert es die erwarteten Ergebnisse?).

#### Mögliche Verbesserungen an Ihrer Beispielabfrage
Obwohl nicht die Hauptfrage, hat Ihr generiertes SQL einige gute Elemente, könnte aber sicherer/präziser sein:
- Verwenden Sie Parameter: Ändern Sie zu `WHERE first_name ILIKE %s` und binden Sie 'andy'.
- Alter "Stand 2025": Verwenden Sie `EXTRACT(YEAR FROM AGE('2025-12-31'::date, date_of_birth)) = 20`, um auf ein bestimmtes Jahresende zu fixieren.
- Fügen Sie `ORDER BY last_login DESC LIMIT 10;` für mehr Sicherheit hinzu.

Die sichere Implementierung erfordert eine Backend-Schicht (d. h. führen Sie SQL nicht direkt aus der AI-Ausgabe aus). Fangen Sie klein an mit einem Skript, das eine LLM-Bibliothek verwendet (z. B. LangChain für NL-to-SQL-Chains).

Wenn Sie Codebeispiele oder Hilfe zu bestimmten Teilen benötigen (z. B. eine Python-Implementierung), geben Sie bitte weitere Details an!

**Referenzen**  
[PostgreSQL-Dokumentation: Row-Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)  
[LangChain NL-to-SQL Tutorial](https://python.langchain.com/docs/tutorials/sql_qa/)  
[Preventing SQL Injection in Python](https://realpython.com/prevent-python-sql-injection/)