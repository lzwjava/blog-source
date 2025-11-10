---
audio: false
generated: true
image: false
lang: de
layout: post
title: WAS Spring JDBC Timeout-Leitfaden
translated: true
type: note
---

Hier ist das mentale Modell und ein schneller Triage-Leitfaden.

# Funktionsweise (WAS + Spring + JDBC)

1.  **DataSource lebt in der WAS**

    *   Sie definieren einen JDBC Provider und eine **DataSource** (normalerweise `XA` für globale Transaktionen oder non-XA) in der WAS Admin Console.
    *   Die WAS verwaltet den **JCA Connection Pool** und gibt JDBC Connections heraus.

2.  **Spring erhält die DataSource via JNDI**

    *   Ihre Spring-App sucht die DataSource des Servers (z.B. `java:comp/env/jdbc/MyDS`) und verpackt sie:

        *   Plain JDBC: `JdbcTemplate` verwendet diese DataSource.
        *   JPA/Hibernate: Die `EntityManagerFactory` verwendet sie.
    *   Transaktionen sind typischerweise **Container JTA** (`WebSphereUowTransactionManager` oder Standard JTA). Springs `@Transactional` tritt der Container-Transaktion bei.

3.  **Aufrufpfad**

    *   Web Request → WebContainer Thread → Spring Service → Transaktion beginnt (JTA) → `DataSource.getConnection()` aus dem **WAS-Pool** → SQL via Treiber → DB.
    *   Timeouts können auf mehreren Ebenen auftreten (Spring, JPA, WAS-Pool, JTA-Transaktion, JDBC-Treiber/DB, Netzwerk).

# Wenn ein Timeout auftritt – identifizieren Sie die Art

Denken Sie in vier Kategorien. Die Nachricht/der Stacktrace verrät Ihnen normalerweise welche.

1.  **Connection Acquisition Timeout**
    Symptom: Warten auf eine gepoolte Verbindung.
    Suchen Sie nach Meldungen über Pool-Erschöpfung oder `J2CA0086W / J2CA0030E`.
    Typische Stellschrauben: *Maximum Connections*, *Connection Timeout*, *Aged Timeout*, *Purge Policy*.

2.  **Transaction Timeout (JTA)**
    Symptom: `WTRN`/`Transaction` Meldungen; Exception wie *"Transaction timed out after xxx seconds"*.
    Typische Stellschraube: **Total transaction lifetime timeout**. Kann lange DB-Operationen abbrechen, selbst wenn die DB noch arbeitet.

3.  **Query/Statement Timeout**
    Symptom: `java.sql.SQLTimeoutException`, Hibernate/JPA "query timeout", oder Spring `QueryTimeoutException`.
    Stellschrauben:

    *   Spring: `JdbcTemplate.setQueryTimeout(...)`, Hibernate `javax.persistence.query.timeout` / `hibernate.jdbc.timeout`.
    *   WAS DataSource Custom Properties (DB2 Beispiele): `queryTimeout`, `queryTimeoutInterruptProcessingMode`.
    *   Treiber-/DB-seitiger Statement Timeout.

4.  **Socket/Read Timeout / Netzwerk**
    Symptom: Nach einer Leerlaufzeit während eines langen Fetches; Low-Level `SocketTimeoutException` oder Vendor-Code.
    Stellschrauben: Treiber `loginTimeout`/`socketTimeout`, Firewall/NAT Idle-Timeout, DB Keepalives.

# Wo man nachschaut (nach Ebene)

**WAS Admin Console Pfade (traditionelle WAS)**

*   JDBC Provider / DataSource:
    Resources → JDBC → Data sources → *IhreDS* →

    *   *Connection pool properties*: **Connection timeout**, **Maximum connections**, **Reap time**, **Unused timeout**, **Aged timeout**, **Purge policy**.
    *   *Custom properties*: Herstellerspezifisch (z.B. DB2 `queryTimeout`, `currentSQLID`, `blockingReadConnectionTimeout`, `queryTimeoutInterruptProcessingMode`).
    *   *JAAS – J2C* falls Auth Aliases relevant sind.
*   Transactions:
    Application servers → *server1* → Container Settings → **Container Services → Transaction Service** → **Total transaction lifetime timeout**, **Maximum transaction timeout**.
*   WebContainer:
    Thread Pool Size (falls Requests sich stapeln).

**Logs & Traces**

*   Traditionelle WAS: `<profile_root>/logs/<server>/SystemOut.log` und `SystemErr.log`.
    Wichtige Komponenten: `RRA` (Resource Adapters), `JDBC`, `ConnectionPool`, `WTRN` (Transaktionen).
    Trace aktivieren (prägnanter Starter):

    ```
    RRA=all:WTRN=all:Transaction=all:JDBC=all:ConnectionPool=all
    ```

    Suchen Sie nach:

    *   `J2CA0086W`, `J2CA0114W` (Pool/Verbindungsprobleme)
    *   `WTRN0037W`, `WTRN0124I` (Transaktion Timeouts/Rollbacks)
    *   `DSRA`/`SQL` Exceptions mit Vendor SQL-Codes.
*   Liberty: `messages.log` unter `wlp/usr/servers/<server>/logs/`.

**PMI / Monitoring**

*   Aktivieren Sie **PMI** für JDBC Connection Pools und Transaction Metrics. Beobachten Sie:

    *   Pool Size, In-Use Count, Waiters, Wait Time, Timeouts.
    *   Transaction Timeouts/Rollback Counts.

**Spring/JPA App Logs**

*   Schalten Sie SQL + Timing in Ihrer App ein (`org.hibernate.SQL`, `org.hibernate.type`, Spring JDBC debug), um Dauer und Timeouts zu korrelieren.

**Datenbank & Treiber**

*   DB2: `db2diag.log`, `MON_GET_PKG_CACHE_STMT`, Activity Event Monitors, Statement-Level Timeouts.
*   Treibereigenschaften in der WAS DataSource oder `DriverManager`, falls Sie keine Container-DS verwenden (nicht typisch auf WAS).

**Netzwerk**

*   Middleboxes mit Idle-Timeout. OS Keepalive / Treiber Keepalive Einstellungen.

# Schneller Triage-Ablauf

1.  **Klassifizieren Sie den Timeout**

    *   *Connection Wait?* Suchen Sie nach `J2CA` Pool-Warnungen. Wenn ja, erhöhen Sie **Maximum connections**, beheben Sie Leaks, optimieren Sie den Pool, setzen Sie **Purge Policy = EntirePool** für Poison Events.
    *   *Tx Timeout?* `WTRN` Meldungen. Erhöhen Sie **Total transaction lifetime timeout** oder reduzieren Sie die Arbeit pro Transaktion; vermeiden Sie es, große Batch-Jobs in einer Transaktion zu wrappen.
    *   *Query Timeout?* `SQLTimeoutException` oder Spring/Hibernate `QueryTimeout`. Stimmen Sie **Spring/Hibernate** Timeouts mit **WAS DS** und **DB** Timeouts ab; vermeiden Sie konfligierende Einstellungen.
    *   *Socket/Read Timeout?* Netzwerk/Treiber Meldungen. Prüfen Sie den `socketTimeout`/`loginTimeout` des Treibers, DB Keepalives und Firewalls.

2.  **Korrelieren Sie die Zeiten**

    *   Vergleichen Sie die fehlgeschlagene Dauer mit den konfigurierten Schwellwerten (z.B. "scheitert bei ~30s" → finden Sie eine 30s Einstellung: Spring Query Timeout 30s? Tx Lifetime 30s? Pool Wait 30s?).

3.  **Prüfen Sie die Pool-Gesundheit**

    *   PMI: Sind **Waiters** > 0? Ist **In-Use** nahe an **Max**? Long-Running Holder? Erwägen Sie, die **Connection Leak Detection** zu aktivieren (RRA Trace zeigt, wer die Connection genommen hat).

4.  **DB-Sichtbarkeit**

    *   Bestätigen Sie auf der DB: Läuft das Statement noch? Wurde es abgebrochen? Irgendwelche Lock-Waits? Falls Locks → erwägen Sie Lock Timeout vs. Statement Timeout.

# Nützliche Stellschrauben & Fallstricke (WAS + DB2 Beispiele)

*   **Total transaction lifetime timeout** (Server-Level) tötet lange Queries, selbst wenn Sie einen höheren Spring/Hibernate Timeout setzen. Halten Sie diese konsistent.
*   **queryTimeoutInterruptProcessingMode** (DataSource Custom Property für DB2): Steuert, wie DB2 eine getimete Query unterbrechen soll (kooperativ/forciert). Hilft, Threads zu vermeiden, die nach Timeouts hängen bleiben.
*   **Purge policy**: `EntirePool` kann schneller von fatalen SQL-States (z.B. DB-Neustart) recoveren, kostet aber einen kurzen Ausreißer.
*   **Aged/Unused timeout**: Stale Connections aussondern, um Firewall/NAT Idle-Timeout zu umgehen.
*   **Validation**: Aktivieren Sie **validation by SQL** oder **validation timeout**, damit tote Connections vor der Nutzung erkannt werden.
*   **Thread pools**: Wenn WebContainer Threads gesättigt sind, *sehen Symptome wie Timeouts aus*. Stellen Sie sicher, dass WebContainer und Default Thread Pools angemessen dimensioniert sind.

# Minimale Spring Wiring Beispiele

**JNDI DataSource (XML)**

```xml
<jee:jndi-lookup id="dataSource" jndi-name="java:comp/env/jdbc/MyDS" expected-type="javax.sql.DataSource"/>
<bean id="txManager" class="org.springframework.transaction.jta.JtaTransactionManager"/>
<tx:annotation-driven transaction-manager="txManager"/>
```

**JdbcTemplate Query Timeout (Java)**

```java
@Bean JdbcTemplate jdbcTemplate(DataSource ds) {
  JdbcTemplate jt = new JdbcTemplate(ds);
  jt.setQueryTimeout(60); // Sekunden
  return jt;
}
```

**Hibernate/JPA Timeout**

```properties
javax.persistence.query.timeout=60000  # ms
hibernate.jdbc.timeout=60              # Sekunden
```

# Was man erfassen sollte, wenn man es eskaliert

*   Exakter Exception-Text + Stacktrace.
*   Zeitstempel: Request-Start, Tx-Beginn, Query-Start, Fehlerzeit.
*   WAS DS Pool Konfig (Screenshot oder Werte), Transaction Service Timeouts.
*   PMI Snapshot (Pool Waiters, In-Use, Timeout Counts).
*   DB-Ansicht der Session/des Statements zum Fehlerzeitpunkt.
*   Netzwerk-Topologie-Notizen (Firewalls, Proxies, Idle-Timer).

Wenn Sie einen spezifischen Exception-Snippet (J2CA/WTRN/SQL-State) einfügen, kann ich die genaue Ebene und die passende Einstellung zum Anpassen identifizieren.