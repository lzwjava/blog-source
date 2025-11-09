---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Leitfaden für KI-Agenten in Java Spring Monorepos
translated: true
type: note
---

Fantastische Frage. Hier sind praktische, wirkungsvolle KI-Agenten, die Sie für ein Java/Spring-Monorepo (Multi-Modul, Maven/Jetty/Liberty, JaCoCo, etc.) anpassen können. Ich konzentriere mich auf konkrete Auslöser, was sie produzieren und wie man sie einbindet – ohne Tabellen.

# Kern-Engineering-Agenten

**1) PR-Code-Reviewer (Spring-kompatibel)**

* **Auslöser:** Beim Pull Request.
* **Funktion:** Liest Diffs + betroffene Spring-Beans/Konfiguration; markiert DI-Probleme, falsch gescopte Beans, fehlende `@Transactional`, N+1-Risiken mit JPA, falsche Verwendung von `@Scheduled`, Thread-Leaks bei Async, blockierende Aufrufe in Reactive-Chains.
* **Eingaben:** Diff + `pom.xml` + `application*.yml` + `@Configuration`-Klassen.
* **Ausgaben:** Zeilenkommentare als Vorschläge, Risiko-Zusammenfassung, Quick-Fix-Patches.

**2) Dependency & Plugin Upgrader**

* **Auslöser:** Täglicher/wöchentlicher Job.
* **Funktion:** Schlägt kompatible Version-Upgrades für Spring Boot/Framework, Spring Data/Cloud, Jetty/Liberty, Maven-Plugins vor, prüft CVEs, führt Smoke-Build durch.
* **Ausgaben:** PRs gruppiert nach Risiko (Patch, Minor, Major), mit Changelog und Rollback-Hinweis.

**3) API Contract Guardian**

* **Auslöser:** Bei PRs, die Controller oder `openapi.yaml` betreffen.
* **Funktion:** Hält OpenAPI-Spec mit Spring-MVC-Annotationen synchron; erkennt Breaking Changes (HTTP-Codes, Feldumbenennungen, nullable/required).
* **Ausgaben:** Kommentar mit Diff der API-Oberfläche; optionale Pact-style Contract-Test-Stubs.

**4) Test Author & Flaky-Test Doctor**

* **Auslöser:** Bei PR (geringe Test-Delta) und nächtlich.
* **Funktion:** Generiert/erweitert JUnit 5-Tests für Services/Controller/Repos; stabilisiert Flakies (Zeit, Temp-Verzeichnisse, Nebenläufigkeit), schlägt deterministische Patterns vor, isoliert Clock mit `Clock`.
* **Ausgaben:** Neue Tests, Parametrisierung, Hinweise zum Ersetzen von Sleeps durch Awaitility.

**5) Coverage Orchestrator (Unit+IT, Multi-Modul)**

* **Auslöser:** Bei CI nach Integrationstests.
* **Funktion:** Hängt JaCoCo-Agent an Jetty/Liberty, merged `jacoco.exec`/`jacoco-it.exec`, mappt Klassen über Module hinweg, hebt ungetestete kritische Pfade hervor.
* **Ausgaben:** Gemergter HTML/XML-Report; ein Kommentar, der die Top 10 ungedeckten Methoden pro Modul mit vorgeschlagenen Test-Skeletten auflistet.

**6) Log & Incident Triage**

* **Auslöser:** Bei fehlgeschlagenen CI-Jobs oder Stream aus Staging/Prod.
* **Funktion:** Cluster Stack Traces, korreliert mit letztem Deploy, verlinkt zu verdächtigen Commits; schlägt schnelle Diffs und Feature Flags zum Umschalten vor.
* **Ausgaben:** Root-Cause-Hypothesen, "Next Step"-Checkliste, Grafana/ELK-Links.

**7) Performance Profiler Coach**

* **Auslöser:** Beim Load-Test-Run oder Slow-Endpoint-Alert.
* **Funktion:** Liest JFR/async-profiler-Output + Spring-Actuator-Metriken; erkennt langsame `@Transactional`-Grenzen, N+1, heavyweight Mapper, falsch dimensionierte Pools.
* **Ausgaben:** Fokussierter Perf-Plan (JPA-Fetch-Graph-Hints, Indizes, Pool-Größen, Cache).

**8) Database Migration Assistant (Db2/MySQL/Postgres kompatibel)**

* **Auslöser:** Bei Flyway/Liquibase-Change oder Slow-Query-Reports.
* **Funktion:** Prüft DDL auf Locking, fügt Indizes hinzu, simuliert Migrationsreihenfolge; erstellt Rollback-Skripte; rewritet ineffiziente JPQL/Criteria zu SQL mit Hints.
* **Ausgaben:** Geprüfte Migrations-PR, Explain-Plan-Notizen, sichere Rollout-Schritte.

**9) Security & Secrets Sentinel**

* **Auslöser:** Bei jedem PR und nächtlichem Scan.
* **Funktion:** SAST für Spring-Security-Misconfig, CSRF/Headers, Deserialisierung, SpEL-Injection; scannt nach Secrets in YAML, Properties, Test-Fixtures.
* **Ausgaben:** Inline-PR-Annotationen, vorgeschlagene `SecurityFilterChain`-Diffs.

**10) Config Drift & Profile Auditor**

* **Auslöser:** Bei PRs, die `application*.yml` betreffen.
* **Funktion:** Validiert Profile-Overlays, Env-Var-Bindings, fehlende Defaults; erkennt Prod-only-Überraschungen (z.B. unterschiedliches `spring.jpa.open-in-view`).
* **Ausgaben:** "Effective Config"-Vorschau nach Profil und Environment.

**11) Build Cop (Maven Multi-Modul)**

* **Auslöser:** Bei jedem Build.
* **Funktion:** Diagnostiziert Plugin-Reihenfolge, reproducible Builds, Encoding-Warnungen, Test-Fork-Settings, Surefire/Failsafe-Handoff, Module-Graph-Regressionen.
* **Ausgaben:** Spezifische `pom.xml`-Patches und ein schnelleres Build-Rezept.

**12) Release Notes & Changelog Writer**

* **Auslöser:** Beim Tag oder Release-Branch-Merge.
* **Funktion:** Gruppiert Commits nach konventionellem Scope/Modul; zieht bemerkenswerte API-Changes & Migrationen heraus; beinhaltet Upgrade-Schritte.
* **Ausgaben:** `CHANGELOG.md`-Abschnitt + GitHub-Release-Body-Entwurf.

# Übergreifende "Glue"-Patterns

**Event-Quellen:** GitHub PRs/Actions, Jenkins, Maven-Phasen, Gradle-Tasks (falls vorhanden), Log-Pipelines, JFR-Outputs, Actuator-Metriken, Pact/Postman-Runs.
**Context Packs:** Diff + betroffene Module, `pom.xml`-Bäume, OpenAPI, `application*.yml`, Key-Configs (`SecurityFilterChain`, `DataSource`, `JpaRepositories`), Test-Reports, JaCoCo-XML, Profiler/Flamegraphs.
**Response Targets:** PR-Kommentare mit Code-Fenced-Patches, Status-Checks, Auto-PRs, Markdown-Reports gespeichert als Build-Artefakte.

# Minimale Einbindung (Copy-Paste-freundlich)

**1) GitHub Action Step, um Repo-Kontext für Agenten vorzubereiten**

```yaml
- name: Prepare Spring context bundle
  run: |
    mkdir -p .agent_ctx
    git diff -U0 origin/main... > .agent_ctx/diff.patch || true
    find . -name "pom.xml" -o -name "build.gradle*" > .agent_ctx/build_files.txt
    find . -name "application*.yml" -o -name "application*.properties" > .agent_ctx/configs.txt
    find . -name "openapi*.yaml" -o -name "openapi*.yml" > .agent_ctx/openapi.txt
```

**2) JaCoCo-Merge (Unit + IT) für Multi-Modul**

```bash
mvn -q -DskipITs=false -P it-tests verify
mvn -q org.jacoco:jacoco-maven-plugin:prepare-agent verify
mvn -q org.jacoco:jacoco-maven-plugin:report-aggregate
# Wenn Sie externe IT mit einem laufenden Jetty/Liberty sammeln:
# java -javaagent:jacocoagent.jar=destfile=jacoco-it.exec,append=true ...
# dann merge:
mvn -q org.jacoco:jacoco-maven-plugin:merge \
  -DdestFile=target/jacoco-merged.exec \
  -Dfile1=target/jacoco.exec -Dfile2=target/jacoco-it.exec
mvn -q org.jacoco:jacoco-maven-plugin:report \
  -DdataFile=target/jacoco-merged.exec
```

**3) PR-Kommentar-Helper (ChatOps-Style)**

```yaml
- name: Post agent findings
  if: always()
  run: |
    echo "### API Contract Changes" > agent-comment.md
    echo "" >> agent-comment.md
    cat target/api-diff.md >> agent-comment.md || true
- uses: marocchino/sticky-pull-request-comment@v2
  with:
    path: agent-comment.md
```

# Was zuerst bauen (höchster ROI)

1.  **PR-Code-Review + Config Auditor**: Fängt 70 % der häufigen Spring-Fehler früh ab.
2.  **Coverage Orchestrator**: Merged Unit- und externe IT (Ihr Fall) und gibt Test-TODOs pro Modul aus.
3.  **API Contract Guardian**: Verhindert Breaking Clients; geringer Aufwand, großer vermiedener Ärger.
4.  **Dependency Upgrader + Security Sentinel**: Stetige Hygiene mit minimalem Rauschen.

# Guardrails & Qualität

*   **Determinismus:** Agenten sollten Rule-IDs und Links zu den analysierten Codezeilen enthalten.
*   **Change Budgets:** Begrenze Auto-Edits auf kleine Patches; größere Refactorings werden zu Draft-PRs.
*   **Privatsphäre/Zugriff:** Beschränke Prod-Logs/DB-Snapshots; redacte Secrets vor Model-Calls.
*   **Metriken:** Verfolge MTTR (Fail → Fix), Flaky-Rate, Test-Coverage-Delta, Perf-SLIs. Verwende wöchentliche Agenten-Scorecards.

# Wenn Sie möchten, kann ich:

*   Einen **einsatzbereiten GitHub-Actions-Workflow** entwerfen, der "PR-Code-Review + API-Contract-Guardian + Coverage-Orchestrator" unter Verwendung Ihrer Module und JaCoCo-Einrichtung ausführt.
*   **Starter-Rules** generieren, die auf Ihren Stack (Jetty/Liberty, Db2, Multi-Modul-Maven) abgestimmt sind.

Teilen Sie mir Ihre Repo-Struktur (Modulnamen) und Ihre aktuelle Vorgehensweise für IT (Jetty vs. Liberty) mit, und ich liefere das YAML + kleine Helper-Skripte.