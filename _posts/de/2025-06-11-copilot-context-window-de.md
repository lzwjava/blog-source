---
audio: false
generated: true
lang: de
layout: post
title: Workarounds für den Copilot-Kontextfenster
translated: true
type: note
---

Sie treffen einen entscheidenden Punkt bei der Arbeit mit KI-Modellen in IDEs wie Copilot: die Kontextfenster-Beschränkungen. Während 4096 Token für eine große Codebasis oder ein komplexes Problem klein erscheinen mögen, gibt es in der Tat Workarounds und wichtige Überlegungen.

Zunächst wollen wir den Kontext von Copilot und GPT-4o klären:

*   **Copilot und GPT-4o Kontextfenster:** Während 4096 Token eine häufige Kontextfenstergröße für frühere Modelle war, **bietet GitHub Copilot Chat (in VS Code und JetBrains IDEs) jetzt deutlich größere Kontextfenster, die oft GPT-4o (oder sogar neuere Modelle wie GPT-4.1) mit bis zu 64k oder sogar 128k Token nutzen (insbesondere für VS Code Insiders).** Dies ist eine erhebliche Verbesserung und macht den Umgang mit größeren Dateien und komplexeren Problemen viel besser handhabbar.

Selbst mit größeren Kontextfenstern werden Sie jedoch immer noch an Grenzen stoßen, insbesondere bei massiven Codebasen oder sehr detaillierten Logs/Problemen. Daher sind Ihre vorgeschlagenen Workarounds sehr relevant:

### Workarounds für Kontextlängen-Beschränkungen:

1.  **Aufgabe aufteilen und fokussierten Kontext bereiten (Ihr Vorschlag):** Dies ist eine exzellente und hocheffektive Strategie.
    *   **"Hier ist Code, hier ist Log, hier ist Problem":** Genau das sollten Sie tun. Kuratieren Sie die Informationen, anstatt alles hineinzuwerfen.
        *   **Code:** Stellen Sie nur die relevantesten Code-Snippets oder Dateien bereit, die direkt mit dem Problem zusammenhängen. Wenn es um eine bestimmte Funktion geht, geben Sie nur diese Funktion und ihre unmittelbaren Abhängigkeiten an.
        *   **Log:** Extrahieren Sie die kritischen Zeilen aus dem Log, die den Fehler oder das ungewöhnliche Verhalten anzeigen. Stellen Sie keine Megabyte an Log-Dateien bereit.
        *   **Problembeschreibung:** Seien Sie in Ihrer Problembeschreibung klar, präzise und prägnant. Geben Sie an, was Sie erwarten, was tatsächlich passiert und alle spezifischen Fehlermeldungen.
    *   **Vorteil:** Indem Sie den Fokus eingrenzen, stellen Sie sicher, dass die wichtigsten Informationen in das aktive Kontextfenster von Copilot passen, was zu genaueren und relevanteren Vorschlägen führt.

2.  **Mehrrundige Gespräche (Ihr Vorschlag) - Ja, Copilot nutzt vorherige Gespräche:**
    *   **In VS Code und JetBrains IDEs (Copilot Chat):** Absolut. Die Chat-Oberfläche ist für mehrteilige Konversationen konzipiert. Copilot erinnert sich an die vorherigen Runden in der aktuellen Chat-Sitzung und nutzt dies als Teil des laufenden Kontexts. Dies ist entscheidend, um Lösungen zu verfeinern und iterativ an Problemen zu arbeiten.
    *   **Wie es funktioniert:** Wenn Sie in demselben Chat-Thread eine Folgefrage stellen oder zusätzliche Informationen liefern, berücksichtigt Copilot implizit Ihre vorherigen Prompts und seine eigenen Antworten, um eine informiertere Antwort zu generieren.
    *   **Strategien für mehrrundige Gespräche:**
        *   **Breit beginnen, dann eingrenzen:** Beginnen Sie mit einer allgemeinen Problembeschreibung und liefern Sie dann spezifischere Details oder relevante Codes/Logs als Follow-up, basierend auf den ersten Vorschlägen von Copilot.
        *   **Verfeinern und klären:** Wenn die erste Antwort von Copilot nicht ganz richtig ist, starten Sie nicht neu. Sagen Sie ihm stattdessen, was falsch ist oder welche zusätzlichen Einschränkungen es berücksichtigen muss.
        *   **Spezifische Aktionen anfordern:** "Wenden Sie diese Korrektur nun auf Datei X an," oder "Können Sie auch einen Testfall für dieses Szenario generieren?"

### Andere Workarounds und Tipps:

*   **Nutzen Sie `@workspace` und `#file`:**
    *   **`@workspace`:** In Copilot Chat (besonders VS Code) können Sie `@workspace` verwenden, um Copilot anzuweisen, relevante Dateien in Ihrem gesamten Workspace zu berücksichtigen. Während es nicht die *gesamte* Codebasis aufnimmt, ruft es intelligent Snippets aus Dateien ab und injiziert sie, die es basierend auf Ihrem Prompt und der aktuellen Datei für relevant hält. Dies ist eine leistungsstarke Funktion für größere Projekte.
    *   **`#file <Dateiname>`:** Sie können explizit auf bestimmte Dateien in Ihren Prompts mit `#file` verweisen. Dies stellt sicher, dass diese Dateien für diese spezielle Abfrage im Kontext berücksichtigt werden.
*   **Fassen Sie große Eingaben zusammen:** Wenn Sie ein sehr langes Log oder Dokument haben, das relevant ist, aber nicht hineinpasst, bitten Sie Copilot (oder ein anderes LLM), es zunächst zusammenzufassen, und verwenden Sie dann diese Zusammenfassung als Kontext.
*   **Konzentrieren Sie sich auf das "Warum":** Erklären Sie anstatt nur Code bereitzustellen, *warum* Sie denken, dass es ein Problem gibt oder was das Ziel ist. Dies hilft Copilot, die Absicht zu verstehen, auch wenn es nicht den gesamten umgebenden Code sehen kann.
*   **Brechen Sie komplexe Probleme herunter:** Für eine große Bugfix oder neue Funktion bitten Sie Copilot nicht, alles auf einmal zu erledigen. Unterteilen Sie es in kleinere, handhabbare Teilaufgaben. Zum Beispiel:
    1.  "Erklären Sie das Problem in dieser Funktion."
    2.  "Schlagen Sie ein Refactoring für diesen Teil vor."
    3.  "Generieren Sie Unit-Tests für den refaktorisierten Code."
*   **Verwenden Sie beschreibende Variablen-/Funktionsnamen:** Während dies kein direkter Workaround für Tokenlimits ist, bieten gut benannte Variablen und Funktionen Copilot impliziten Kontext und machen seine Vorschläge auch bei begrenztem explizitem Kontext genauer.
*   **Repository-spezifische Custom Instructions:** Wenn Sie ein Copilot Pro-Abonnement haben, können Sie repository-weite benutzerdefinierte Anweisungen einrichten. Dies ermöglicht es Ihnen, übergreifenden Kontext über Ihr Projekt, Ihren Codierstil oder häufige Fehlerquellen bereitzustellen, den Copilot bei allen Interaktionen innerhalb dieses Repositorys berücksichtigt. Dies ist extrem wertvoll für langfristige Konsistenz und Qualität.

Zusammenfassend lässt sich sagen, dass zwar ältere Informationen eine strenge 4096-Token-Grenze für GPT-4o nahelegen könnten, Copilot in modernen IDEs jedoch oft größere Kontextfenster verwendet. Trotzdem sind Ihre Instinkte bezüglich des Aufteilens von Aufgaben und der Nutzung mehrrundiger Konversationen genau richtig und stellen die Best Practices für eine effektive Arbeit mit Copilot dar, insbesondere bei komplexen Softwareentwicklungs-Herausforderungen.

---

Basierend auf den Suchergebnissen finden Sie hier die Informationen zu den Tokenlimits und der Kontextspeicherung für GPT-4.1 und GitHub Copilot:

### GPT-4.1 Token-Limit
- GPT-4.1 hat ein deutlich größeres Kontextfenster im Vergleich zu seinen Vorgängern. Es unterstützt ein Kontextfenster von bis zu 1 Million Token, was eine erhebliche Steigerung gegenüber dem 128K-Token-Limit von GPT-4o darstellt. Dies macht es geeignet für Aufgaben, die das Verarbeiten großer Codebasen oder umfangreicher Textkorpora in einem einzigen Prompt erfordern.

### GitHub Copilot Token-Limit und Kontextspeicherung
- GitHub Copilot, das auf Modellen wie GPT-4 basiert, hat typischerweise ein Token-Limit von etwa 4096 Token für Interaktionen innerhalb von IDEs wie VSCode und IntelliJ IDEA. Es gibt jedoch Variationen, abhängig vom spezifischen Setup und der verwendeten Copilot-Version.

- Für Nutzer von GitHub Copilot mit Visual Studio Code Insiders gibt es Zugang zu einem noch größeren Kontextfenster von bis zu 128K Token, was dem Maximum entspricht, das von OpenAIs GPT-4o-Modell unterstützt wird. Dieses größere Kontextfenster kann den Umgang mit großen Dateien und Repositories verbessern.

- GitHub Copilot Chat kann Mehrrunden-Gespräche verwalten, aber die Speicherung des Kontexts über diese Gespräche hinweg kann variieren. Während es einen Teil des Kontexts aus vorherigen Interaktionen behalten kann, wird generell empfohlen, Zusammenfassungen oder Kernpunkte aus früheren Runden bereitzustellen, um die Kontinuität zu wahren, insbesondere bei komplexen Aufgaben.

### Workarounds für Token-Limits
- **Chunking**: Unterteilen Sie große Aufgaben in kleinere, handhabbare Teile. Dies kann helfen, innerhalb der Tokenlimits zu bleiben und gleichzeitig jedes Segment der Aufgabe effektiv zu bearbeiten.
- **Zusammenfassung**: Fassen Sie lange Codeabschnitte oder Logs zusammen, bevor Sie sie Copilot bereitstellen. Dies hilft, wesentliche Informationen innerhalb des Tokenlimits zu behalten.
- **Fokussierte Abfragen**: Konzentrieren Sie sich anstatt des gesamten Kontexts auf einmal auf spezifische Teile des Codes oder der Logs, die für das zu lösende Problem am relevantesten sind.
- **Mehrrundige Gespräche**: Verwenden Sie mehrrundige Gespräche, um den Kontext schrittweise aufzubauen. Auch wenn Copilot möglicherweise nicht den gesamten Kontext aus vorherigen Interaktionen behält, kann das manuelle Bereitstellen von Zusammenfassungen oder Kernpunkten helfen, die Kontinuität aufrechtzuerhalten.

Diese Strategien können Ihnen helfen, GitHub Copilot effektiv innerhalb seiner Tokenlimits zu nutzen und die Kontextspeicherung über Mehrrunden-Gespräche hinweg zu verbessern.