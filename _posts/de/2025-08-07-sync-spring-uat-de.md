---
audio: false
generated: true
image: false
lang: de
layout: post
title: Synchronisierung der UAT-Branches und des Codes im Frühjahr
translated: true
type: note
---

Hier ist eine Sammlung von Best Practices und Patterns, die Sie kombinieren können, um Ihre drei UAT-Branches synchron zu halten, Ihre Historie sauber zu halten und länderspezifischen Code in einer Spring-App zu verwalten – plus ein paar Hinweise, wo KI helfen kann.

---

## 1. Branching & Synchronisation

1.  **Trunk-based mit kurzlebigen Feature-Branches**

    *   Halten Sie einen einzigen **main**- (oder **develop**-) Branch.
    *   Erstellen Sie für jedes Jira-Ticket (z.B. FT-103) und Land Feature-Branches mit den Namen:
        ```
        feature/FT-103-cn
        feature/FT-103-sg
        feature/FT-103-tw
        ```
    *   Wenn die Arbeit fertig ist, mergen Sie zurück in **main** und cherry-picken oder mergen Sie dann in jeden `uat_cn`, `uat_sg`, `uat_tw`.
    *   Vorteil: Merges in main passieren nur einmal; Country-Branches nehmen nur das auf, was sie benötigen.

2.  **Regelmäßige Synchronisierung der UAT-Branches**

    *   Planen Sie einen täglichen (oder pro-Build) Job, der jeden `uat_*`-Branch auf `main` rebased, damit sie sich nicht zu weit voneinander entfernen.
    *   Automatisieren Sie dies in der CI (z.B. eine GitHub Action, die `uat_cn` jede Nacht rebased).

3.  **Verwenden Sie Pull-Requests + Review-Erzwingung**

    *   Erzwingen Sie einen PR für jeden Merge von einem Feature-Branch → main.
    *   Stellen Sie sicher, dass das "FT-xxx"-Ticket im Branch-Namen und im PR-Titel/-Beschreibung steht.

---

## 2. Commit-Message-Konventionen & Squashing

1.  **Conventional-style mit JIRA-Key**

    ```
    FT-103: fix null-pointer in customer lookup
    ```

2.  **Micro-commit → Squash beim Merge**

    *   Während der Feature-Entwicklung committen Entwickler nach Bedarf:
        ```
        FT-103 #1: initial wiring of service beans
        FT-103 #2: add validation logic
        FT-103 #3: update error handling
        ```
    *   Beim PR-Merge verwenden Sie "Squash and merge", um alle FT-103-Commits in einen prägnanten Commit zusammenzufassen:
        ```
        FT-103: customer-service validation and error handling
        ```

3.  **Nummerierung innerhalb eines Tickets**

    *   Wenn mehrere distinct Schritte im selben Ticket verfolgt werden, ist eine Nummerierung (`#1`, `#2`) während der Entwicklung in Ordnung.
    *   Sobald gemerged, squashen Sie alles in einen *einzigen* FT-103-Commit; die Historie bleibt sauber und jedes Ticket ist eine logische Änderung.

4.  **Automatisieren Sie commit-lint**

    *   Verwenden Sie einen Git-Hook oder ein CI-Plugin (z.B. [commitlint](https://commitlint.js.org)), um `FT-\d+` am Anfang jeder Message zu erzwingen.
    *   Optional können Sie einen Scope erzwingen: `FT-103(sg): …`.

---

## 3. Umgang mit länderspezifischem Code in Spring

1.  **Profile & conditional beans**

    *   Definieren Sie ein Spring Profile pro Land: `@Profile("cn")`, `@Profile("sg")`, `@Profile("tw")`.
    *   Legen Sie in `application-cn.yml`, `application-sg.yml` usw. länderspezifische Properties fest.
    *   Übergeben Sie beim Start `--spring.profiles.active=cn` (oder sg, tw), um die richtigen Beans auszuwählen.

2.  **Strategy pattern / plugin modules**

    *   Erstellen Sie ein Interface `PaymentProcessor` mit drei Implementierungen (`CnPaymentProcessor`, etc.).
    *   Verwenden Sie `@Component` + `@Profile` oder eine Factory, die die Bean basierend auf einem Runtime-Flag auswählt.

3.  **Resource bundles / feature flags**

    *   Wenn die Unterschiede klein sind (z.B. Datumsformate, Endpoint-URLs), halten Sie einen Code-Pfad bei und externalisieren Sie die Unterschiede in Property-Dateien oder einem Feature-Flag-Service.

4.  **Separate modules (if large)**

    *   Für sehr unterschiedliche Logik, teilen Sie sie in Sub-Module auf:
        ```
        /core
        /country-cn
        /country-sg
        /country-tw
        ```
    *   Die Haupt-App bindet nur das aktive Country-Module zur Build/Deploy-Zeit ein.

---

## 4. Trennung von Aufgaben nach Autor vs. nach Ticket

*   **Nach Ticket, nicht nach Autor.** Aufgaben sollten um *Features* (Jira-IDs) herum aufgebaut sein, nicht um die Person.
*   Wenn mehrere Entwickler an FT-103 arbeiten, kollaborieren sie im selben Branch oder verwenden Topic-Branches, die davon abzweigen – aber letztendlich mergen sie zurück in den einzelnen FT-103-Branch.
*   Autor-Metadaten bleiben im Commit-Author-Feld; Sie müssen nicht nach Autor squashen.

---

## 5. KI einsetzen

1.  **Commit-Message-Generierung**

    *   Tools wie GitHub Copilot oder OpenAI können saubere, conventional Commit Messages aus Ihrem Diff vorschlagen.
    *   Integrieren Sie einen Pre-Commit-Hook, der `ai-commit --preview` ausführt, um den Message-Entwurf zur Überprüfung zu erstellen.

2.  **PR-Beschreibung & Changelog**

    *   Verwenden Sie einen KI-Assistenten, um alle Commits eines Tickets in eine kohärente PR-Beschreibung oder Release Note zusammenzufassen:
        > “Fassen Sie die Änderungen in feature/FT-103 in Stichpunkten zusammen.”

3.  **Code-Review-Unterstützung**

    *   KI-gestützte Linter (SonarQube mit KI-Plugins, DeepCode) können auf Probleme in länderspezifischen Code-Pfaden hinweisen.

4.  **Automatisierung von Cherry-Picks/Rebases**

    *   Schreiben Sie ein kleines Skript (oder verwenden Sie eine Low-Code-Plattform), das, wenn FT-103 in `main` landet, diesen Commit automatisch in jeden `uat_*`-Branch cherry-picked und PRs für etwaige Merge-Konflikte öffnet.

---

### Alles zusammenfügen

1.  **Entwickeln auf** `feature/FT-XXX-<cn/sg/tw>`.
2.  **Commiten Sie frei** (nummerierte Schritte OK), immer mit Referenz auf den JIRA-Key.
3.  **Öffnen Sie einen PR** → main; wählen Sie **Squash-and-merge**, sodass jedes FT-XXX ein sauberer Commit ist.
4.  **CI-Job** rebased/merged diesen Commit automatisch in jeden `uat_cn`, `uat_sg`, `uat_tw`.
5.  **Spring Profile** wählen zur Laufzeit die korrekte Country-Logik aus – keine Code-Duplikation in drei Branches.
6.  **KI-Tools** helfen dabei, den Commit-Style durchzusetzen, PRs zusammenzufassen und Merges zu verwalten.

Dieser Workflow hält Ihre Historie sauber, stellt sicher, dass jedes Ticket über alle Umgebungen hinweg zu einem einzigen Commit zurückverfolgt werden kann, trennt die Country-Logik zur Laufzeit anstatt in der Git-Historie und nutzt KI dort, wo sie den größten Mehrwert bietet.