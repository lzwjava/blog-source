---
audio: false
generated: true
lang: de
layout: post
title: Modernisierung einer veralteten Codebasis für eine neuere JDK
translated: true
type: note
---

Das Upgrade eines großen Codebestands (Zehntausende von Codezeilen) von JDK 8 und Spring 5.2.2 auf ein neueres JDK wie 11, 17 oder 21 erfordert eine sorgfältige Planung, um Unterbrechungen zu minimieren, insbesondere angesichts der Verwendung von IBM DB2 JCC-Treibern, der starken Abhängigkeit von Spring und dem Deployment auf WebSphere Liberty. Im Folgenden werden die wichtigsten Überlegungen skizziert, einschließlich Kompatibilität, potenzieller Breaking Changes, Migrationsschritte und Empfehlungen. Da Sie erwähnt haben, dass Sie Spring ebenfalls upgraden können, werde ich Szenarien behandeln, in denen dies notwendig oder vorteilhaft sein könnte.

### Allgemeine Überlegungen zum JDK-Upgrade
- **Abwärtskompatibilität und Breaking Changes**: Java strebt eine starke Abwärtskompatibilität an, aber Upgrades von JDK 8 führen Änderungen ein, die Ihren Code beeinflussen könnten:
  - **Entfernte/Deprecated APIs**: JDK 9+ entfernte interne APIs wie `sun.misc.Unsafe` und einige `sun.*`-Pakete. Falls Ihr Code (oder Abhängigkeiten) diese verwendet, benötigen Sie Alternativen (z.B. über `Unsafe`-Alternativen in Third-Party-Libs oder Javas `VarHandle`).
  - **Modulsystem (JPMS ab JDK 9)**: Kapselt interne APIs, was potenziell zu "illegal access"-Fehlern führt. Verwenden Sie vorübergehend `--add-opens`- oder `--add-exports`-Flags, streben Sie aber Refaktorierung für Modularität an.
  - **Garbage Collection-Änderungen**: Der Standard-GC wechselte von Parallel zu G1 in JDK 9, mit weiteren Anpassungen in späteren Versionen (z.B. Shenandoah oder ZGC in 11+). Testen Sie auf Leistungsauswirkungen bei speicherintensiven Teilen.
  - **Andere Änderungen**: Stärkere Kapselung, Entfernung der Applet-/Browser-Plugin-Unterstützung, Updates der Security Manager (deprecated in 17, entfernt in 21) und Sprachfeatures wie Records (14+), Sealed Classes (17) und Virtual Threads (21). Diese sind größtenteils ergänzend, können aber Codeanpassungen erfordern, wenn Reflection intensiv genutzt wird.
  - Von 8 auf 11: Moderate Änderungen (z.B. keine Java-EE-Module wie JAXB mehr, die in 9 entfernt wurden; fügen Sie sie als Abhängigkeiten hinzu).
  - Von 11 auf 17: Geringere Störungen, hauptsächlich Verbesserungen wie besseres Pattern Matching.
  - Von 17 auf 21: Minimale Breaking Changes; hauptsächlich neue Features wie Pattern Matching für Switch (21) und keine größeren Entfernungen.
- **Schrittweise Migration**: Springen Sie nicht direkt auf 21. Führen Sie das Upgrade inkrementell durch (z.B. 8 → 11 → 17 → 21), um Probleme zu isolieren. Verwenden Sie Tools wie OpenRewrite oder jdeps, um nach Inkompatibilitäten zu suchen.
- **Tests und Tooling**:
  - Führen Sie umfassende Tests (Unit, Integration, Load) auf dem neuen JDK aus. Tools wie Maven/Gradle-Plugins (z.B. `maven-enforcer-plugin`) können Kompatibilität erzwingen.
  - Bauwerkzeuge aktualisieren: Stellen Sie sicher, dass Maven/Gradle das neue JDK unterstützt (die meisten tun dies, aber überprüfen Sie Plugins wie Surefire).
  - Multi-Version-Testing: Verwenden Sie Docker oder CI/CD (z.B. GitHub Actions), um Tests gegen mehrere JDKs durchzuführen.
- **Abhängigkeiten und Bibliotheken**: Überprüfen Sie alle Third-Party-Libs auf Kompatibilität. Verwenden Sie Tools wie `mvn dependency:tree` oder OWASP Dependency-Check.
- **Leistung und Sicherheit**: Neuere JDKs bieten bessere Leistung (z.B. schnellere Startzeiten in 17+), Sicherheitsfixes und Langzeitunterstützung (LTS: 11 bis 2026, 17 bis 2029, 21 bis 2031+).
- **Aufwand für großen Codebestand**: Bei starker Spring-Nutzung konzentrieren Sie sich auf Spring-verwaltete Komponenten (z.B. Beans, AOP). Planen Sie Zeit für Refaktorierung ein (z.B. 1-2 Wochen pro Major-Version-Sprung, skaliert mit der Codegröße).

### Spezifische Überlegungen nach Ziel-JDK
#### Upgrade auf JDK 11
- **Vorteile**: LTS mit guter Stabilität; näher an JDK 8, daher weniger Änderungen. End-of-Life nähert sich (2026), aber immer noch weitgehend unterstützt.
- **Nachteile**: Verpasst moderne Features wie Virtual Threads (21) oder verbesserte GC (17+).
- **Spring-Kompatibilität**: Spring 5.2.2 funktioniert auf JDK 11, aber upgraden Sie auf Spring 5.3.x (neueste in der 5.x-Linie) für bessere JDK 11/17-Unterstützung und Bugfixes. Keine größeren Spring-Änderungen nötig.
- **DB2 JCC-Treiber**: Kompatibel mit neueren Treiberversionen (z.B. 4.x+). Einige ältere Treiber hatten Probleme mit OpenJDK 11, also aktualisieren Sie auf die neueste Version (z.B. von der IBM-Website) und testen Sie Verbindungen.
- **WebSphere Liberty**: Vollständig unterstützt (Liberty läuft auf JDK 8/11/17/21).
- **Wichtige Änderungen ab JDK 8**:
  - Fügen Sie Abhängigkeiten für entfernte Module hinzu (z.B. `javax.xml.bind:jaxb-api` für JAXB).
  - Beheben Sie illegalen Reflective Access (häufig in älteren Libs).
  - Vorgehensweise: Aktualisieren Sie Ihre Build-Datei (z.B. Maven `<java.version>11</java.version>`), kompilieren Sie neu und führen Sie Tests aus. Verwenden Sie den JDK 11 Migration Guide von Oracle für Schritt-für-Schritt-Prüfungen.
- **Aufwand**: Niedrig bis mittel; minimale Codeänderungen, wenn keine internen APIs verwendet werden.

#### Upgrade auf JDK 17
- **Vorteile**: Aktuelles LTS mit starker Verbreitung; beinhaltet Features wie Text Blocks, Records und erweiterte Switch-Anweisungen. Bessere Leistung als 11.
- **Nachteile**: SecurityManager deprecated (falls verwendet, planen Sie die Entfernung). Einige Libs benötigen möglicherweise Updates.
- **Spring-Kompatibilität**: Spring 5.3.x unterstützt JDK 17 vollständig (auf LTS-Releases getestet). Upgrade von 5.2.2 auf 5.3.x für optimale Kompatibilität – keine Breaking Changes in Spring selbst.
- **DB2 JCC-Treiber**: Explizit unterstützt in neueren Versionen (z.B. JCC 4.29+ für DB2 11.5). IBM-Dokumentation bestätigt JDK 17-Runtime-Unterstützung; testen Sie auf SQLJ-Erweiterungen.
- **WebSphere Liberty**: Vollständig unterstützt.
- **Wichtige Änderungen ab JDK 11**:
  - Strengere Kapselung; mehr Warnungen zu veralteten Features.
  - Neue APIs (z.B. `java.net.http` für HTTP/2-Clients) können Code modernisieren, sind aber nicht zwingend erforderlich.
  - Vorgehensweise: Nach JDK 11, wechseln Sie in den Builds auf 17. Verwenden Sie Migrationsleitfäden, um Entfernungen von Applet/Corba zu prüfen (falls vorhanden).
- **Aufwand**: Mittel; baut auf JDK 11-Migration auf.

#### Upgrade auf JDK 21
- **Vorteile**: Neuestes LTS mit modernsten Features (z.B. Virtual Threads für Concurrency, Sequenced Collections). Am besten für Zukunftssicherheit.
- **Nachteile**: Erfordert Spring-Upgrade (siehe unten); potenzielle Probleme mit sehr alten Libs.
- **Spring-Kompatibilität**: Spring 5.x unterstützt JDK 21 nicht offiziell (Maximum ist JDK 17). Sie müssen auf Spring 6.1+ upgraden (was JDK 17+ als Basislinie erfordert). Dies ist eine große Veränderung:
  - **Jakarta EE-Migration**: Spring 6 wechselt von Java EE (javax.*) zu Jakarta EE 9+ (jakarta.*). Ändern Sie Imports (z.B. `javax.servlet` → `jakarta.servlet`), aktualisieren Sie Konfigurationen und refaktorieren Sie EE-bezogenen Code (z.B. JPA, Servlets, JMS).
  - **Breaking Changes**: Entfernte deprecated APIs (z.B. alte Transaction Manager); AOT-Kompilierungsunterstützung; erfordert Aktualisierung von Abhängigkeiten wie Hibernate (auf 6.1+).
  - **Migrationsleitfaden**: Befolgen Sie den offiziellen Spring-Leitfaden: Aktualisieren Sie zuerst auf Spring 5.3.x, dann auf 6.0/6.1. Verwenden Sie Tools wie OpenRewrite-Recipes für automatisierte javax → jakarta-Wechsel. Für Ihren großen Codebestand könnte dies Hunderte von Änderungen bedeuten – testen Sie in Modulen.
  - Falls Spring Boot verwendet wird (implizit durch Spring-Nutzung), aligniert Boot 3.x mit Spring 6 und JDK 17+.
- **DB2 JCC-Treiber**: Kompatibel über Abwärtskompatibilität mit JDK 17-Unterstützung; aktualisieren Sie auf den neuesten Treiber (z.B. 4.32+) und verifizieren Sie.
- **WebSphere Liberty**: Vollständig unterstützt (bis JDK 24).
- **Wichtige Änderungen ab JDK 17**:
  - SecurityManager entfernt; falls verwendet, ersetzen Sie durch Alternativen.
  - Neue Features wie String Templates (Preview) brechen vorhandenen Code nicht.
  - Vorgehensweise: Bauen Sie zuerst auf JDK 17 auf, dann wechseln Sie. Keine größeren absichtlichen Breaking Changes zwischen 17 und 21.
- **Aufwand**: Hoch, wenn Spring upgegradet wird; ansonsten ähnlich wie 17.

### Zusätzliche projektspezifische Überlegungen
- **IBM DB2 JCC-Bibliothek**: Stellen Sie sicher, dass Ihre Treiberversion zur DB2-Version passt (z.B. für DB2 11.5, verwenden Sie JCC 4.29+). Testen Sie JDBC-Verbindungen, SQLJ und benutzerdefinierte Abfragen – neuere JDKs könnten Charset- oder Zeitzonenprobleme aufdecken.
- **WebSphere Liberty Deployment**: Keine Blockierer; Liberty ist flexibel mit JDKs. Aktualisieren Sie server.xml bei Bedarf für JVM-Argumente (z.B. `--add-opens` für Modulprobleme). Testen Sie Deployments frühzeitig.
- **Großer Codebestand und Spring-Nutzung**: Priorisieren Sie modulare Upgrades (z.B. zuerst Core-Services upgraden). Wenn Spring tief integriert ist (z.B. MVC, Data, Security), prüfen Sie auf veraltete Features in 5.2.2. Ein Spring-Upgrade bringt Vorteile wie bessere AOT und Observability, erhöht aber die Kosten.
- **Risiken und Abschwächungen**: Ausfallzeiten durch Inkompatibilitäten; mildern Sie mit Rollback-Plänen. Budgetieren Sie Vendor Support, falls kommerzielles DB2/Liberty verwendet wird.
- **Kosten**: Zeit (Wochen bis Monate für vollständige Migration), potenzielle Lizenzen (z.B. kommerzielle JDKs wie Oracles) und Schulung zu neuen Features.

### Empfehlungen
- **Bevorzugter Pfad**: Beginnen Sie mit JDK 11 oder 17, während Sie bei/upgraden zu Spring 5.3.x bleiben – geringeres Risiko für Ihren Codebestand. Gehen Sie zu 21 nur, wenn Sie dessen Features benötigen (z.B. Virtual Threads) und bereit sind, auf Spring 6 zu upgraden (was aufgrund der Jakarta-Änderungen erheblichen Aufwand bedeuten könnte).
- **Nächste Schritte**:
  1. Scannen Sie Code mit jdeps/jlink auf Probleme.
  2. Richten Sie einen Branch für Migrationstests ein.
  3. Konsultieren Sie offizielle Leitfäden: Oracle JDK Migration Guide, Spring Versions Wiki, IBM DB2 JDBC Downloads, Liberty Java Support.
  4. Wenn Sie Spring auf 6 upgraden, folgen Sie dem Migrationsleitfaden für Jakarta-Änderungen.

Wenn Sie weitere Details angeben (z.B. spezifische Spring-Module oder DB2-Version), kann ich dies weiter verfeinern.